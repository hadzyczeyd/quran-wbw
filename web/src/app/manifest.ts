import type { MetadataRoute } from "next";

/** Web app manifest — omogućava instalaciju na početni ekran i pakovanje za Play Store (TWA). */
export default function manifest(): MetadataRoute.Manifest {
  return {
    id: "/",
    name: "Kur'an riječ po riječ",
    short_name: "Riječ po riječ",
    description:
      "Učenje kur'anskog arapskog kroz bosanski jezik — riječ po riječ, obojeno prema gramatičkoj ulozi.",
    lang: "bs",
    dir: "ltr",
    // utm_source se bilježi u statistici (ConsentManager) — vidi se koliko posjeta dolazi iz instalirane aplikacije.
    start_url: "/?utm_source=pwa",
    scope: "/",
    display: "standalone",
    background_color: "#f7f6f3",
    theme_color: "#f7f6f3",
    categories: ["education", "books"],
    icons: [
      { src: "/icons/any-192.png", sizes: "192x192", type: "image/png", purpose: "any" },
      { src: "/icons/any-512.png", sizes: "512x512", type: "image/png", purpose: "any" },
      { src: "/icons/maskable-192.png", sizes: "192x192", type: "image/png", purpose: "maskable" },
      { src: "/icons/maskable-512.png", sizes: "512x512", type: "image/png", purpose: "maskable" },
    ],
    shortcuts: [
      { name: "Sve sure", url: "/sure", icons: [{ src: "/icons/any-192.png", sizes: "192x192" }] },
      { name: "El-Fatiha", url: "/sura/1", icons: [{ src: "/icons/any-192.png", sizes: "192x192" }] },
    ],
  };
}
