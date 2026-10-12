// 1. Рисует надпись из src/data/wordmark.ts крупно (3000 px) в glyphs.png.
//    node tools/neon/raster.mjs (нужен npm ci в .github/check). Промежуточные файлы остаются в tools/neon.
import { chromium } from "../../.github/check/node_modules/playwright/index.mjs";
import fs from "node:fs";
const src = fs.readFileSync(new URL("../../src/data/wordmark.ts", import.meta.url), "utf8");
const d = src.match(/d:\s*"([^"]+)"/)[1];
const W = 3000, H = Math.round(3000 * 1466 / 1878);
const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: W, height: H } });
await p.setContent(`<body style="margin:0;background:#fff"><svg width="${W}" height="${H}" viewBox="-47 -1016 1878 1466"><path d="${d}" fill="#000"/></svg></body>`);
await p.screenshot({ path: new URL("glyphs.png", import.meta.url).pathname }); await b.close(); console.log(W, H);
