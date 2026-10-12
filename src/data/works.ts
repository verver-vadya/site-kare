// Работы для лукбука: фото, рубрика, мастер, подпись. Фото — модели фотостока (см. CREDITS.md),
// у настоящего салона здесь будут работы мастеров.

export const categories = [
  { id: "kare", name: "Каре" },
  { id: "short", name: "Короткие" },
  { id: "color", name: "Цвет" },
  { id: "curly", name: "Кудри" },
  { id: "styling", name: "Укладки" },
  { id: "long", name: "Длинные" },
] as const;

export type Work = {
  key: string;
  alt: string;
  title: string;
  text: string;
  cats: string[];
  master: string;
  service: string;
};

export const works: Work[] = [
  { key: "w-camera", alt: "Девушка с чёрным каре и густой чёлкой держит плёночный фотоаппарат", title: "Каре с прямой чёлкой", text: "Срез по линии скул, чёлка до бровей", cats: ["kare", "short"], master: "anna-vetrova", service: "kare" },
  { key: "w-honey", alt: "Длинные волосы с медовым отливом, вид сбоку", title: "Медовый на тёмно-русом", text: "Тонирование поверх натурального цвета", cats: ["color", "long"], master: "mariam-osmanova", service: "toning" },
  { key: "w-profile", alt: "Девушка с короткой стрижкой и асимметричной чёлкой, профиль", title: "Короткий боб с асимметрией", text: "Затылок короче, чёлка на одну сторону", cats: ["short", "kare"], master: "mark-ilin", service: "pixie" },
  { key: "w-balayage", alt: "Девушка в шапке, светлые волосы с плавным переходом от тёмных корней", title: "Балаяж с тёмными корнями", text: "Корни отрастают незаметно, обновлять раз в 3–4 месяца", cats: ["color", "long"], master: "mariam-osmanova", service: "balayage" },
  { key: "w-curls", alt: "Девушка с длинными вьющимися волосами смотрит вниз", title: "Кудри без пушения", text: "Стрижка по сухим волосам, по одному локону", cats: ["curly", "long"], master: "timur-garanin", service: "curly" },
  { key: "w-redwall", alt: "Девушка с рыжеватыми волосами до плеч у красной стены", title: "Каре до плеч, медный", text: "Удлинённое каре и тонирование в медь", cats: ["kare", "color"], master: "anna-vetrova", service: "kare" },
  { key: "w-evening", alt: "Длинные волосы, уложенные крупными локонами, с заколкой, вид сзади", title: "Свадебные локоны", text: "Крупная волна на одну сторону, держится весь вечер", cats: ["styling", "long"], master: "vera-polyakova", service: "evening" },
  { key: "w-blond", alt: "Длинные светлые волосы, вид со спины", title: "Холодный блонд", text: "Осветление в два визита и тонирование", cats: ["color", "long"], master: "mariam-osmanova", service: "one-tone" },
  { key: "w-fringe", alt: "Девушка с короткой стрижкой и чёлкой работает за ноутбуком", title: "Короткая с длинной чёлкой", text: "Чёлку можно убрать за ухо или носить вперёд", cats: ["short"], master: "mark-ilin", service: "pixie" },
  { key: "w-red", alt: "Девушка с рыжими волосами среди красных цветов", title: "Рыжий без красноты", text: "Тёплая медь, подобрана под цвет кожи", cats: ["color"], master: "mariam-osmanova", service: "one-tone" },
  { key: "w-leaf", alt: "Портрет девушки с объёмными кудрями, на лице тень от листа", title: "Объём на кудрях", text: "Форма для густых вьющихся волос", cats: ["curly"], master: "timur-garanin", service: "curly" },
  { key: "w-candle", alt: "Девушка с мягкими волнами сидит на кровати при свечах", title: "Мягкие волны", text: "Локоны, которые к вечеру становятся только лучше", cats: ["styling"], master: "vera-polyakova", service: "waves" },
  { key: "w-pink", alt: "Девушка со светлыми волнистыми волосами у розовой кирпичной стены", title: "Тёплый блонд", text: "Блонд с бежевым отливом, без желтизны", cats: ["color"], master: "mariam-osmanova", service: "toning" },
  { key: "w-window", alt: "Девушка с длинными тёмными волосами сидит у окна", title: "Длина без секущихся концов", text: "Убрали 4 см, сохранили длину и густоту", cats: ["long"], master: "timur-garanin", service: "long" },
  { key: "w-waves", alt: "Светло-каштановые волосы до плеч уложены мягкой волной", title: "Укладка на каждый день", text: "Феном за 20 минут, без лака", cats: ["styling"], master: "vera-polyakova", service: "blowdry" },
  { key: "w-soft", alt: "Девушка с длинными тёмными волосами на оранжевом фоне", title: "Глянец после ухода", text: "Уход для окрашенных волос и укладка", cats: ["long"], master: "vera-polyakova", service: "color-care" },
];

export const workByKey = (key: string) => works.find((w) => w.key === key);
