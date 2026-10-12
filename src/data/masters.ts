// Мастера. level — от него зависят цены (см. services.ts), groups — какие услуги мастер делает.
import type { LevelId } from "./services";

export type Master = {
  slug: string;
  name: string;
  nameDative: string; // «Записаться к Анне»
  level: LevelId;
  role: string;
  since: number;
  photo: string;
  photoAlt: string;
  groups: string[];
  quote: string;
  about: string[];
  best: string[];
  works: string[];
};

export const masters: Master[] = [
  {
    slug: "anna-vetrova",
    name: "Анна Ветрова",
    nameDative: "Анне",
    level: "art",
    role: "Основательница салона, каре и короткие стрижки",
    since: 2009,
    photo: "m-anna",
    photoAlt: "Анна Ветрова, портрет",
    groups: ["strizhki", "ukladki", "uhod"],
    quote: "Хорошее каре видно через месяц, а не в день стрижки.",
    about: [
      "Анна открыла «Каре» в 2014 году, после пяти лет работы в салонах на Патриарших. Придумала технику, по которой в салоне стригут каре: срез по линии скул и внутренняя градуировка, чтобы форма не разваливалась при отрастании.",
      "Сама учит всех мастеров салона и раз в квартал проводит открытый урок для стилистов из других салонов.",
    ],
    best: ["Каре и боб", "Пикси", "Исправление неудачных стрижек"],
    works: ["w-camera", "w-profile", "w-redwall"],
  },
  {
    slug: "mariam-osmanova",
    name: "Мариам Османова",
    nameDative: "Мариам",
    level: "lead",
    role: "Колорист, окрашивание и тонирование",
    since: 2013,
    photo: "m-mariam",
    photoAlt: "Мариам Османова, портрет",
    groups: ["okrashivanie", "uhod"],
    quote: "Блонд без желтизны — это не краситель, а правильное тонирование и уход дома.",
    about: [
      "Мариам отвечает за цвет в салоне: подбирает оттенки, ведёт сложные окрашивания и учит колористов.",
      "Любит медовые и карамельные оттенки на тёмных волосах и честно говорит, если желаемый цвет за один раз получить не выйдет.",
    ],
    best: ["Балаяж", "Блонд и тонирование", "Выход из тёмного цвета"],
    works: ["w-honey", "w-balayage", "w-blond", "w-pink"],
  },
  {
    slug: "mark-ilin",
    name: "Марк Ильин",
    nameDative: "Марку",
    level: "lead",
    role: "Мужские и короткие женские стрижки",
    since: 2015,
    photo: "m-mark",
    photoAlt: "Марк Ильин, портрет в профиль",
    groups: ["strizhki"],
    quote: "Короткая стрижка должна выглядеть хорошо и на третий день без укладки.",
    about: [
      "Марк пришёл в «Каре» из барбершопа и стрижёт и мужчин, и женщин. Работает машинкой и ножницами, делает короткие стрижки с чёткой текстурой.",
    ],
    best: ["Мужские стрижки", "Пикси", "Короткие стрижки с текстурой"],
    works: ["w-fringe", "w-profile"],
  },
  {
    slug: "timur-garanin",
    name: "Тимур Гаранин",
    nameDative: "Тимуру",
    level: "stylist",
    role: "Вьющиеся и длинные волосы, укладки",
    since: 2019,
    photo: "m-timur",
    photoAlt: "Тимур Гаранин, портрет",
    groups: ["strizhki", "ukladki"],
    quote: "Кудри не надо выпрямлять, им нужна правильная форма.",
    about: [
      "Тимур стрижёт вьющиеся волосы по сухим, по одному локону, и учит клиентов укладывать кудри без фена.",
    ],
    best: ["Стрижка вьющихся волос", "Длинные волосы", "Локоны"],
    works: ["w-curls", "w-leaf", "w-window"],
  },
  {
    slug: "vera-polyakova",
    name: "Вера Полякова",
    nameDative: "Вере",
    level: "stylist",
    role: "Укладки и уход",
    since: 2021,
    photo: "m-vera",
    photoAlt: "Вера Полякова, портрет",
    groups: ["ukladki", "uhod", "strizhki"],
    quote: "Вечерняя укладка должна пережить и танцы, и дождь.",
    about: [
      "Вера делает вечерние и свадебные укладки, ведёт уходы и стрижёт длинные волосы.",
    ],
    best: ["Вечерние укладки", "Свадебные укладки", "Уход"],
    works: ["w-evening", "w-candle", "w-waves"],
  },
];

export const masterBySlug = (slug: string) => masters.find((m) => m.slug === slug);
export const mastersFor = (group: string) => masters.filter((m) => m.groups.includes(group));
