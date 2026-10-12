"""Вывеска с картинки-образца: вырезает выключенные стеклянные трубки и свет включённых.

Образец (sign-ref.jpg): сверху вывеска горит, снизу выключена, фон один и тот же.
На выходе:
  public/assets/img/neon-glass.webp — выключенные трубки с держателями и тенью (с прозрачностью);
  public/assets/img/neon-light.webp — свет: горящие трубки и свечение на стене (на чёрном, кладётся режимом screen);
  src/data/neon-photo.ts — где лежит холст в координатах образца и провода.
Запуск: python3 tools/neon/photo.py
"""
import os, json
import cv2, numpy as np
from scipy.optimize import nnls

os.chdir(os.path.dirname(os.path.abspath(__file__)))
U = 3  # во сколько раз увеличиваем образец
ref = cv2.imread("sign-ref.jpg")
on = ref[0:530, 0:700]
off = ref[546:1076, 3:703]  # нижняя половина, сдвинута на (3, 5) к верхней
up = lambda im: cv2.resize(im, None, fx=U, fy=U, interpolation=cv2.INTER_LANCZOS4)
on_u, off_u = up(on), up(off)
H, W = off_u.shape[:2]

def disk(r):
    r = max(1, int(round(r)))
    return cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (2 * r + 1, 2 * r + 1))

# Область вывески без заголовка сайта, попавшего в образец слева внизу
roi = np.zeros((H, W), np.uint8)
roi[130 * U:478 * U, 108 * U:575 * U] = 255
roi[405 * U:, :200 * U] = 0

# Горящая трубка: почти белая. Выключенная: светлое серое стекло
hsv = cv2.cvtColor(on_u, cv2.COLOR_BGR2HSV)
core = (((hsv[..., 2] > 235) & (hsv[..., 1] < 120)).astype(np.uint8) * 255) & roi
hsv = cv2.cvtColor(off_u, cv2.COLOR_BGR2HSV)
glass = (((hsv[..., 1] < 70) & (hsv[..., 2] > 110)).astype(np.uint8) * 255) & roi
glass &= cv2.dilate(core, disk(30))
glass = cv2.morphologyEx(glass, cv2.MORPH_OPEN, disk(2))

# Совмещаем горящую половину с выключенной (картинки нарисованы чуть по-разному)
blur = lambda m, s: cv2.GaussianBlur(m.astype(np.float32) / 255, (0, 0), s)
Wm = np.eye(2, 3, dtype=np.float32)
_, Wm = cv2.findTransformECC(blur(glass, 6), blur(core, 6), Wm, cv2.MOTION_AFFINE,
                             (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 300, 1e-6), None, 5)
warp = lambda im, f: cv2.warpAffine(im, Wm, (W, H), flags=f + cv2.WARP_INVERSE_MAP, borderMode=cv2.BORDER_REPLICATE)
on_al = warp(on_u, cv2.INTER_LANCZOS4)
core = (warp(core, cv2.INTER_LINEAR) > 127).astype(np.uint8) * 255

# Держатели (чёрные и серые колпачки на концах), координаты образца
boots = [(176, 153), (267, 152), (128, 361), (257, 349), (356, 363), (414, 254), (370, 456), (536, 354)]
tube = cv2.morphologyEx(core | glass, cv2.MORPH_CLOSE, disk(4))
tube = cv2.dilate(tube, disk(1.6 * U))
# Мелкие дырки внутри трубки закрашиваем, просветы внутри букв оставляем
n, lab, st, _ = cv2.connectedComponentsWithStats(255 - tube)
for i in range(1, n):
    if st[i, cv2.CC_STAT_AREA] < 60 * U * U:
        tube[lab == i] = 255
for x, y in boots:
    cv2.circle(tube, (x * U, y * U), int(6.5 * U), 255, -1)
a = cv2.GaussianBlur(tube.astype(np.float32) / 255, (0, 0), 0.8 * U)

# Тень трубок на стене: вниз и вправо, мягкая
sh = np.roll(np.roll(tube, int(3 * U), 1), int(5 * U), 0).astype(np.float32) / 255
sh = cv2.GaussianBlur(sh, (0, 0), 2.5 * U) * 0.5
alpha = a + sh * (1 - a)
# Наше фото светлее образца, поэтому стекло чуть светлее; тень чёрная
col = np.clip(off_u.astype(np.float32) / 255 * 1.2, 0, 1)
col = col * (a / np.maximum(alpha, 1e-4))[..., None]
# Холст: только вокруг вывески
x0, y0, x1, y1 = 40, 90, 680, 505
crop = lambda im: im[y0 * U:y1 * U, x0 * U:x1 * U]
rgba = np.dstack([crop(col), crop(alpha)])
rgba = np.clip(rgba * 255 + 0.5, 0, 255).astype(np.uint8)
cv2.imwrite("../../public/assets/img/neon-glass.webp", rgba, [cv2.IMWRITE_WEBP_QUALITY, 88])

# Свет. Внутри трубок — в точности горящая трубка образца поверх выключенной (screen: L = 1 - (1-on)/(1-off)).
onf, offf = on_al.astype(np.float32) / 255, off_u.astype(np.float32) / 255
L_tube = np.clip(1 - (1 - onf) / np.maximum(1 - offf, 0.02), 0, 1)
# Снаружи — свечение как сумма размытых трубок, веса подобраны по образцу
sig = [2, 5, 12, 28, 60]
G = [cv2.GaussianBlur(tube.astype(np.float32) / 255, (0, 0), s * U) for s in sig]
far = 150
dist = cv2.distanceTransform(255 - tube, cv2.DIST_L2, 5) / U
sample = (dist > 1.5) & (dist < far) & (roi > 0)
idx = np.flatnonzero(sample.ravel())[::37]
A = np.stack([g.ravel()[idx] for g in G], 1)
L_glow = np.zeros_like(onf)
weights = []
for c in range(3):
    target = np.clip(1 - (1 - onf[..., c]) / np.maximum(1 - offf[..., c], 0.02), 0, 1).ravel()[idx]
    w, _ = nnls(A, target)
    weights.append(w.round(3).tolist())
    L_glow[..., c] = sum(wi * g for wi, g in zip(w, G))
# Наша стена светлее образца, на ней свечение теряется: усиливаем его и чуть теплее делаем трубку
L_glow *= np.float32([1.0, 1.2, 1.75])  # BGR
L_tube *= np.float32([0.45, 0.88, 1.0])  # BGR
L = np.clip(a[..., None] * L_tube + (1 - a[..., None]) * L_glow, 0, 1)
# Края холста гасим плавно, дальше свет даёт тёплый слой на всю комнату
yy, xx = np.mgrid[0:H, 0:W].astype(np.float32) / U
edge = np.minimum.reduce([xx - x0, x1 - xx, yy - y0, y1 - yy])
L *= np.clip(edge / 45, 0, 1)[..., None] ** 1.5
light = np.clip(crop(L) * 255 + 0.5, 0, 255).astype(np.uint8)
light = cv2.resize(light, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)  # свет мягкий, хватит половины
cv2.imwrite("../../public/assets/img/neon-light.webp", light, [cv2.IMWRITE_WEBP_QUALITY, 82])
print("weights BGR", weights)

wires = [
    "M183 158 C200 163 228 168 257 163",  # верх К
    "M293 365 C310 368 330 368 352 365",  # низ а
    "M128 366 L128 494",  # от К вниз
    "M371 461 L372 494",  # от хвоста р
    "M415 367 L415 494",  # из-под р
    "M536 359 L536 494",  # от е
]
data = {"canvas": {"x": x0, "y": y0, "w": x1 - x0, "h": y1 - y0}, "wires": wires}
with open("../../src/data/neon-photo.ts", "w") as f:
    f.write("// Собрано tools/neon/photo.py: холст вывески и провода в координатах образца tools/neon/sign-ref.jpg\n")
    f.write("export const neonPhoto = " + json.dumps(data, ensure_ascii=False, indent=2) + ";\n")
