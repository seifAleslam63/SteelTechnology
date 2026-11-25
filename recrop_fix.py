import os
from PIL import Image

out_dir = r'C:\Users\seif\.gemini\antigravity\scratch\steel-technology\assets\portfolio'
raw_dir = r'C:\Users\seif\.gemini\antigravity\scratch\steel-technology\assets\extracted_raw'

# Re-crop st_05 (trim partial sleeve on far right 5.5%) and st_23 (trim bottom to 88% to clear Redmi dots)
from clean_photos import trim_white_bars

im5 = trim_white_bars(Image.open(os.path.join(raw_dir, 'raw_05.jpg')))
w5, h5 = im5.size
im5 = im5.crop((0, 0, int(w5 * 0.945), h5))
im5.save(os.path.join(out_dir, 'st_05.jpg'), 'JPEG', quality=88, optimize=True)
print('st_05.jpg recropped:', im5.size)

im23 = trim_white_bars(Image.open(os.path.join(raw_dir, 'raw_23.jpg')))
w23, h23 = im23.size
im23 = im23.crop((0, 0, w23, int(h23 * 0.88)))
im23.save(os.path.join(out_dir, 'st_23.jpg'), 'JPEG', quality=88, optimize=True)
print('st_23.jpg recropped:', im23.size)
