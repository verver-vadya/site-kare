// Карта сайта для поисковиков: все страницы, кроме 404
import type { APIRoute } from "astro";
import { groups } from "../data/services";
import { masters } from "../data/masters";
import { articles } from "../data/journal";

export const GET: APIRoute = ({ site }) => {
  const paths = [
    "/", "/uslugi/", ...groups.map((g) => `/uslugi/${g.slug}/`),
    "/mastera/", ...masters.map((m) => `/mastera/${m.slug}/`),
    "/raboty/", "/zhurnal/", ...articles.map((a) => `/zhurnal/${a.slug}/`),
    "/o-salone/", "/sertifikaty/", "/kontakty/", "/zapis/", "/privacy/",
  ];
  const body = `<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
${paths.map((p) => `  <url><loc>${new URL(p, site)}</loc></url>`).join("\n")}
</urlset>
`;
  return new Response(body, { headers: { "Content-Type": "application/xml" } });
};
