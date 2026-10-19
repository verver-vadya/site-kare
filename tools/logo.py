"""Логотип «Каре»: буква «К» из раскрытых ножниц и «АРЕ» шрифтом Manrope SemiBold (переведён в кривые).

Пишет src/data/logo.ts (пути знака «К» и букв «АРЕ», размеры) и public/favicon.svg (знак на терракоте).
Запуск: python3 tools/logo.py
(нужны fonttools и brotli). Единицы — единицы шрифта Manrope: высота прописных 1440, базовая линия y = 0.
"""
import os, math, json
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen

os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
font = TTFont("src/fonts/manrope-cyrillic-600-normal.woff2")
cmap, glyphs = font.getBestCmap(), font.getGlyphSet()
CAP = 1440          # высота прописных
STEM = 214          # толщина основного штриха Manrope SemiBold при этой высоте
TRACK = 300         # разрядка между буквами

def f(v):
    return f"{v:.0f}"

def poly(points):
    return "M" + " L".join(f"{f(x)} {f(y)}" for x, y in points) + " Z"

# --- Знак «К»: ствол буквы, ось ножниц на стволе, два раскрытых лезвия вместо диагоналей ---
pivot = (STEM + 150, CAP * 0.47)
def blade(tip, back_side):
    """Лезвие: прямая режущая кромка от оси до кончика, спинка выгнута наружу (back_side = ±1)."""
    px, py = pivot
    tx, ty = tip
    L = math.hypot(tx - px, ty - py)
    ux, uy = (tx - px) / L, (ty - py) / L
    nx, ny = -uy * back_side, ux * back_side
    back = []
    for i in range(0, 21):
        t = i / 20
        w = 330 * (1 - t) ** 0.9 * min(1, (t + 0.1) / 0.25)  # шире у оси, к кончику сходится в точку
        back.append((px + ux * L * t + nx * w, py + uy * L * t + ny * w))
    # кромка: от оси по спинке к кончику и обратно по прямой
    return "M" + f(px) + " " + f(py) + " " + " ".join("L" + f(x) + " " + f(y) for x, y in back[1:]) + f" L{f(tx)} {f(ty)} Z"

top = blade((1180, CAP + 10), -1)
bottom = blade((1220, -10), 1)
stem = poly([(0, 0), (STEM, 0), (STEM, CAP), (0, CAP)])
screw_r = 135
k_width = 1230

def circle(cx, cy, r):
    return f"M{f(cx - r)} {f(cy)} a{f(r)} {f(r)} 0 1 0 {f(2 * r)} 0 a{f(r)} {f(r)} 0 1 0 {f(-2 * r)} 0 Z"

# Винт на оси: кольцо, в отверстие видно фон (fill-rule evenodd)
screw = circle(*pivot, screw_r) + " " + circle(*pivot, screw_r * 0.4)

# --- «АРЕ» из шрифта ---
x = k_width + TRACK
letters = []
for ch in "АРЕ":
    g = cmap[ord(ch)]
    pen = SVGPathPen(glyphs)
    glyphs[g].draw(TransformPen(pen, (1, 0, 0, 1, x, 0)))
    letters.append(pen.getCommands())
    x += glyphs[g].width + TRACK
width = x - TRACK

# В SVG ось y смотрит вниз: переворачиваем всё одной трансформацией в компоненте
data = {
    "cap": CAP, "width": round(width), "markWidth": k_width,
    "stem": stem, "blades": [top, bottom], "screw": screw,
    "letters": " ".join(letters),
}
with open("src/data/logo.ts", "w") as out:
    out.write("// Собрано tools/logo.py: знак «К» из ножниц и «АРЕ» шрифтом Manrope SemiBold в кривых.\n")
    out.write("// Единицы шрифта: высота прописных 1440, базовая линия y = 0, ось y вверх.\n")
    out.write("export const logo = " + json.dumps(data, ensure_ascii=False, indent=2) + ";\n")
print("width", round(width))

# Иконка вкладки: знак цвета штукатурки на терракотовом квадрате
SIZE = 2000
dx, dy = (SIZE - k_width) / 2 + 20, (SIZE + CAP) / 2
mark = f'<path d="{stem}"/><path d="{top}"/><path d="{bottom}"/><path d="{screw}" fill-rule="evenodd"/>'
with open("public/favicon.svg", "w") as out:
    out.write(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {SIZE} {SIZE}"><rect width="{SIZE}" height="{SIZE}" rx="360" fill="#9c3f22"/>'
              f'<g fill="#f4ebe0" transform="translate({f(dx)} {f(dy)}) scale(1 -1)">{mark}</g></svg>\n')
