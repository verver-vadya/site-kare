# Источники и лицензии

## Фото

Все фото с [Burst](https://burst.shopify.com) (Shopify), лицензия [Burst Some Rights Reserved](https://www.shopify.com/stock-photos/licenses/shopify-some-rights-reserved): можно использовать бесплатно, в том числе в коммерческих целях, указывать автора не обязательно; нельзя перепродавать сами фото. Снимки обрезаны, слегка утеплены по цвету и сжаты в WebP; портреты мастеров и ч/б работы переведены в тёплый дуотон (скрипт `tools/photos.py`). Неоновая вывеска на первом экране нарисована поверх фото, на исходном снимке её нет.

| Файлы в `public/assets/img/` | Источник |
| --- | --- |
| `hero-l-*`, `hero-p-*` | https://burst.shopify.com/photos/couch-by-interior-brick-wall |
| `int-sinks-*` | https://burst.shopify.com/photos/hair-salon-sinks-on-red-brick |
| `int-place-*` | https://burst.shopify.com/photos/hair-salon-mail-hair-stylist |
| `int-shelf-*` | https://burst.shopify.com/photos/interior-decor-shelving-with-ceramic-art |
| `int-chairs-*` | https://burst.shopify.com/photos/pair-of-green-and-white-chairs-in-barbershop |
| `int-court-*` | https://burst.shopify.com/photos/cafe-chairs-and-brick-wall |
| `int-towel-*` | https://burst.shopify.com/photos/white-towels-and-rob-in-salon |
| `int-clock-*` | https://burst.shopify.com/photos/clock-and-flowers-on-side-table |
| `p-parting-*` | https://burst.shopify.com/photos/close-up-stylist-parting-hair |
| `p-combing-*` | https://burst.shopify.com/photos/combing-hair-at-salon |
| `p-blow-*`, `g-ukladki-*` | https://burst.shopify.com/photos/salon-blow-drying-hair |
| `p-blow2-*` | https://burst.shopify.com/photos/hands-blow-drying-hair |
| `p-cut-*`, `g-strizhki-*` | https://burst.shopify.com/photos/woman-getting-hair-cut-at-salon |
| `p-cut2-*` | https://burst.shopify.com/photos/woman-stylist-cuts-hair-at-salon |
| `p-wash-*` | https://burst.shopify.com/photos/wash-and-trim |
| `p-wet-*` | https://burst.shopify.com/photos/stylist-combs-wet-hair |
| `p-tools-*` | https://burst.shopify.com/photos/hair-scissors-and-tools |
| `p-combs-*` | https://burst.shopify.com/photos/repeat-pattern-of-combs-laying-on-a-beige-surface |
| `p-swatch-*` | https://burst.shopify.com/photos/color-swatches |
| `p-first-*` | https://burst.shopify.com/photos/the-first-cut |
| `g-okrashivanie-*`, `w-honey-*` | https://burst.shopify.com/photos/brunette-woman-in-salon-chair |
| `g-uhod-*` | https://burst.shopify.com/photos/hair-in-messy-bun |
| `m-anna-*` | https://burst.shopify.com/photos/monochrome-portrait-of-a-woman-holding-hand-to-her-chin |
| `m-mark-*` | https://burst.shopify.com/photos/profile-of-a-man-with-beard-and-styled-hair |
| `m-mariam-*` | https://burst.shopify.com/photos/portrait-of-a-woman-in-a-white-shirt |
| `m-timur-*` | https://burst.shopify.com/photos/portrait-of-a-person-leaning-in-chair |
| `m-vera-*` | https://burst.shopify.com/photos/portrait-of-a-woman-with-long-brown-hair-and-crossed-arms |
| `w-camera-*` | https://burst.shopify.com/photos/woman-with-short-dark-hair-takes-a-photo |
| `w-profile-*` | https://burst.shopify.com/photos/black-and-white-photo-of-a-woman-profile |
| `w-fringe-*` | https://burst.shopify.com/photos/women-looks-down-in-concentration |
| `w-redwall-*` | https://burst.shopify.com/photos/woman-sandwiched-between-a-red-wall-and-a-curtain-of-white-chains |
| `w-blond-*` | https://burst.shopify.com/photos/long-blond-hair |
| `w-pink-*` | https://burst.shopify.com/photos/woman-portrait-on-pink-brick |
| `w-balayage-*` | https://burst.shopify.com/photos/twirling-hair-and-batting-eyes |
| `w-red-*` | https://burst.shopify.com/photos/woman-with-red-hair-half-hides-behind-red-flowers |
| `w-waves-*` | https://burst.shopify.com/photos/smiling-brunette-woman |
| `w-curls-*` | https://burst.shopify.com/photos/woman-looks-down |
| `w-leaf-*` | https://burst.shopify.com/photos/monochrome-person-with-a-leaf-silhouette-on-their-face |
| `w-evening-*` | https://burst.shopify.com/photos/person-with-brown-hair-in-a-white-silk-robe |
| `w-candle-*` | https://burst.shopify.com/photos/woman-on-bed-in-candle-light |
| `w-window-*` | https://burst.shopify.com/photos/woman-poses-by-large-window |
| `w-soft-*` | https://burst.shopify.com/photos/soft-gaze |
| `og.jpg` | снимок первого экрана сайта |

Люди на фото — модели фотостока, а не сотрудники салона, имена мастеров вымышленные. Для настоящего салона их нужно заменить на фото мастеров, работ и зала салона.

## Шрифты

Лицензия SIL Open Font License 1.1, тексты лицензий в `src/fonts/OFL-*.txt`. Файлы взяты из пакетов [Fontsource](https://fontsource.org).

- [Amatic SC](https://github.com/googlefonts/AmaticSC) — Vernon Adams, Ben Nathan: заголовки и меню
- [Manrope](https://github.com/sharanda/manrope) — Mikhail Sharanda: основной текст и буквы «АРЕ» в логотипе (переведены в кривые, `src/data/logo.ts`)

## Код

- [Astro](https://astro.build), лицензия MIT.
- [morphicons](https://www.npmjs.com/package/morphicons) в `public/assets/vendor/morphicons/`, лицензия в этой папке.
