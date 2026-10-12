// Данные салона в одном месте: всё, что повторяется на нескольких страницах.
export const site = {
  name: "Каре",
  tagline: "Салон стрижки и цвета",
  since: 2014,
  city: "Москва",
  address: "ул. Малая Бронная, 24",
  addressFull: "Москва, ул. Малая Бронная, 24, вход со двора",
  metro: "«Пушкинская» и «Маяковская», 7 минут пешком",
  hours: "Ежедневно 10:00–22:00",
  phone: "+7 495 000-00-00",
  phoneHref: "tel:+74950000000",
  telegram: "kare_salon",
  mapUrl: "https://yandex.ru/maps/?text=%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0%2C%20%D0%9C%D0%B0%D0%BB%D0%B0%D1%8F%20%D0%91%D1%80%D0%BE%D0%BD%D0%BD%D0%B0%D1%8F%2C%2024",
  // Заявки с формы записи. Пока адреса формы нет, форма честно пишет, что не подключена
  formAction: "https://formspree.io/f/YOUR_FORM_ID",
};

// Меню в шапке. Записаться — отдельной кнопкой
export const nav = [
  { href: "/uslugi/", label: "Услуги и цены" },
  { href: "/mastera/", label: "Мастера" },
  { href: "/raboty/", label: "Работы" },
  { href: "/zhurnal/", label: "Журнал" },
  { href: "/o-salone/", label: "О салоне" },
  { href: "/kontakty/", label: "Контакты" },
];
