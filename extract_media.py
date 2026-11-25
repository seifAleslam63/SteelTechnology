import os, re, zlib, io, zipfile
from PIL import Image
import xml.etree.ElementTree as ET

pdf_path = r'C:\Users\seif\.gemini\antigravity\brain\22c3a75b-6258-440b-82e1-f52e00bd37b5\.user_uploaded\media_1795611847900_b35c386b.pdf'
raw_dir = r'C:\Users\seif\.gemini\antigravity\scratch\steel-technology\assets\extracted_raw'
clean_dir = r'C:\Users\seif\.gemini\antigravity\scratch\steel-technology\assets\portfolio'
os.makedirs(raw_dir, exist_ok=True)
os.makedirs(clean_dir, exist_ok=True)

with open(pdf_path, 'rb') as f:
    data = f.read()

# Exact parser using /Length
obj_hdr_re = re.compile(rb'(\d+)\s+0\s+obj\s*<<(.*?)>>\s*stream(\r\n|\n)', re.DOTALL)
count = 0
extracted = {}

for m in obj_hdr_re.finditer(data):
    header = m.group(2)
    if b'/Image' in header and b'/DCTDecode' in header:
        count += 1
        len_m = re.search(rb'/Length\s+(\d+)', header)
        if not len_m:
            continue
        length = int(len_m.group(1))
        start = m.end()
        stream = data[start:start+length]
        raw = zlib.decompress(stream) if b'/FlateDecode' in header else stream
        img = Image.open(io.BytesIO(raw))
        fname = f'raw_{count:02d}.jpg'
        with open(os.path.join(raw_dir, fname), 'wb') as out_f:
            out_f.write(raw)
        extracted[count] = (img.size[0], img.size[1], os.path.join(raw_dir, fname))

print(f'Exact extraction complete: {len(extracted)} / 74 pages. Page 6 size:', extracted.get(6))

# Check PPTX slide -> image mapping for Equipment Catalog Structure.pptx
pptx_path = r'C:\Users\seif\.gemini\antigravity\brain\22c3a75b-6258-440b-82e1-f52e00bd37b5\.user_uploaded\media_1795392466267_f41e2a5c.pptx'
with zipfile.ZipFile(pptx_path) as z:
    for s in range(2, 11):
        rels_name = f'ppt/slides/_rels/slide{s}.xml.rels'
        slide_name = f'ppt/slides/slide{s}.xml'
        xml = z.read(slide_name).decode('utf-8', errors='ignore')
        texts = [t.strip() for t in re.findall(r'<a:t>([^<]+)</a:t>', xml) if t.strip()]
        rels = z.read(rels_name).decode('utf-8', errors='ignore')
        imgs = re.findall(r'Target="\.\./media/([^"]+)"', rels)
        print(f'\nSlide {s}: {texts[-1] if texts else ""}')
        print(f'  Images ({len(imgs)}): {imgs}')
        for im in imgs:
            sz = z.getinfo('ppt/media/' + im).file_size
            if sz > 12000:
                img_bytes = z.read('ppt/media/' + im)
                im_obj = Image.open(io.BytesIO(img_bytes))
                print(f'    {im}: {im_obj.size[0]}x{im_obj.size[1]} ({sz//1024} KB)')
