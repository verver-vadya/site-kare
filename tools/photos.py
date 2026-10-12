# Фото для «Каре»: кадрирование, тёплая цветокоррекция (warm) или тёплый дуотон для ч/б портретов (duo),
# WebP нескольких ширин. Исходники (полноразмерные JPG с Burst, ссылки в CREDITS.md) кладутся в папку full/.
#   python3 tools/photos.py public/assets/img tools/photos.json
# Размеры готовых файлов пишутся в tools/images.json: их нужно перенести в src/data/images.ts.
import sys, os, json
from PIL import Image, ImageOps, ImageEnhance
SRC = 'full'; OUT = sys.argv[1]
os.makedirs(OUT, exist_ok=True)

def warm(im, k=1.0):
    r, g, b = im.split()
    r = r.point(lambda v: min(255, v * (1 + 0.035 * k) + 2 * k))
    b = b.point(lambda v: v * (1 - 0.06 * k))
    im = Image.merge('RGB', (r, g, b))
    return ImageEnhance.Contrast(im).enhance(1 + 0.04 * k)

def duo(im):
    g = ImageOps.grayscale(im)
    g = ImageOps.autocontrast(g, cutoff=0.5)
    return ImageOps.colorize(g, black='#1d140f', white='#f7eadb', mid='#8a6450')

def crop(im, box, ratio):
    """box = (cx, cy) центр в долях; ratio = w/h; берём максимально большой кадр."""
    W, H = im.size
    cx, cy = box
    if W / H > ratio: h = H; w = round(H * ratio)
    else: w = W; h = round(W / ratio)
    x = min(max(round(cx * W - w / 2), 0), W - w)
    y = min(max(round(cy * H - h / 2), 0), H - h)
    return im.crop((x, y, x + w, y + h))

def save(im, key, widths, q=76):
    meta = []
    for w in widths:
        if w > im.width: continue
        h = round(im.height * w / im.width)
        im.resize((w, h), Image.LANCZOS).save(f'{OUT}/{key}-{w}.webp', 'WEBP', quality=q, method=6)
        meta.append(w)
    return {'widths': meta, 'w': im.width, 'h': im.height}

jobs = json.load(open(sys.argv[2]))
result = {}
for j in jobs:
    im = Image.open(f"{SRC}/{j['src']}.jpg").convert('RGB')
    if 'px' in j: im = im.crop(tuple(j['px']))
    if 'ratio' in j: im = crop(im, j.get('focus', (0.5, 0.5)), j['ratio'])
    mode = j.get('mode', 'warm')
    if mode == 'warm': im = warm(im, j.get('k', 1))
    elif mode == 'duo': im = duo(im)
    maxw = max(j['widths'])
    if im.width > maxw: im = im.resize((maxw, round(im.height * maxw / im.width)), Image.LANCZOS)
    result[j['key']] = save(im, j['key'], j['widths'], j.get('q', 76))
    print(j['key'], result[j['key']])
json.dump(result, open(os.path.join(os.path.dirname(sys.argv[2]), 'images.json'), 'w'), indent=1)
