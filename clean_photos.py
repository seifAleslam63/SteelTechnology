import os
from PIL import Image, ImageChops

raw_dir = r'C:\Users\seif\.gemini\antigravity\scratch\steel-technology\assets\extracted_raw'
out_dir = r'C:\Users\seif\.gemini\antigravity\scratch\steel-technology\assets\portfolio'
os.makedirs(out_dir, exist_ok=True)

# Unique curated pages from the 18-page Portfolio PDF + key workshop pages
target_pages = [
    1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19,
    20, 21, 22, 23, 24, 25, 26, 27, 29, 30, 31, 32, 33, 35, 37, 38,
    60, 69, 71, 72, 73
]

def trim_white_bars(im, threshold=242):
    """Trim pure/near-white letterbox borders from top/bottom/sides."""
    w, h = im.size
    rgb = im.convert('RGB')
    px = rgb.load()

    def is_white_row(y):
        non_white = 0
        for x in range(0, w, 4):
            r, g, b = px[x, y]
            if r < threshold or g < threshold or b < threshold:
                non_white += 1
        return non_white <= (w // 4) * 0.04

    def is_white_col(x):
        non_white = 0
        for y in range(top, bottom + 1, 4):
            r, g, b = px[x, y]
            if r < threshold or g < threshold or b < threshold:
                non_white += 1
        return non_white <= ((bottom - top + 1) // 4) * 0.04

    top = 0
    while top < h - 10 and is_white_row(top):
        top += 1
    bottom = h - 1
    while bottom > top + 10 and is_white_row(bottom):
        bottom -= 1

    left = 0
    while left < w - 10 and is_white_col(left):
        left += 1
    right = w - 1
    while right > left + 10 and is_white_col(right):
        right -= 1

    # Add 2px inward safety margin to avoid thin white fringe
    top = min(top + 2, bottom - 10)
    bottom = max(bottom - 2, top + 10)
    left = min(left + 2, right - 10)
    right = max(right - 2, left + 10)
    return im.crop((left, top, right + 1, bottom + 1))

# Specific bottom crops (fraction of post-trim height to keep) to remove phone watermarks
# Pages 30, 31, 32, 33, 35, 37 have white Vivo V50 ZEISS bar at bottom
# Pages 21, 23 have Redmi Note 10 5G overlay text at bottom ~6%
# Page 22 has Scanned with CamScanner overlay in bottom-left ~10%
custom_bottom_crop = {
    21: 0.93,
    22: 0.88,
    23: 0.92,
    30: 0.90,
    31: 0.90,
    32: 0.90,
    33: 0.90,
    35: 0.90,
    37: 0.90,
}

# Page 5 has a tiny partial person's sleeve on the far right edge; trim 3% right if desired, or keep full
for p in target_pages:
    src = os.path.join(raw_dir, f'raw_{p:02d}.jpg')
    im = Image.open(src)
    im = trim_white_bars(im)
    if p in custom_bottom_crop:
        w, h = im.size
        im = im.crop((0, 0, w, int(h * custom_bottom_crop[p])))
        # Trim again in case Vivo white strip was slightly taller
        im = trim_white_bars(im)
    dst = os.path.join(out_dir, f'st_{p:02d}.jpg')
    im.save(dst, 'JPEG', quality=88, optimize=True)
    print(f'st_{p:02d}.jpg -> {im.size[0]}x{im.size[1]} ({os.path.getsize(dst)//1024} KB)')
