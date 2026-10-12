# Переводит надпись «Каре» шрифтом Bad Script (OFL, пакет @fontsource/bad-script) в кривые для src/data/wordmark.ts.
#   python3 tools/wordmark.py путь/к/bad-script-cyrillic-400-normal.woff2
import re, sys
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.boundsPen import BoundsPen
from fontTools.pens.transformPen import TransformPen

font = TTFont(sys.argv[1])
glyphs, cmap, hmtx = font.getGlyphSet(), font.getBestCmap(), font["hmtx"]
pen, bounds, x = SVGPathPen(glyphs), BoundsPen(glyphs), 0
for ch in "Каре":
    g = cmap[ord(ch)]
    glyphs[g].draw(TransformPen(pen, (1, 0, 0, -1, x, 0)))
    glyphs[g].draw(TransformPen(bounds, (1, 0, 0, -1, x, 0)))
    x += hmtx[g][0]
x0, y0, x1, y1 = bounds.bounds
pad = 40
d = re.sub(r"-?\d+\.\d+", lambda m: str(round(float(m.group()))), pen.getCommands())
print(f'viewBox: "{x0 - pad:.0f} {y0 - pad:.0f} {x1 - x0 + 2 * pad:.0f} {y1 - y0 + 2 * pad:.0f}"')
print(f'd: "{d}"')
