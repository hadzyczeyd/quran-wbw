/*
 * Service worker za PWA (instalacija na početni ekran + rad bez interneta).
 *
 * - Stranice (HTML i RSC podaci za navigaciju unutar aplikacije):
 *   prvo mreža, pa keš, pa /offline. Online korisnik uvijek dobija svježu
 *   verziju; offline se otvaraju sure koje je već jednom otvorio.
 * - /_next/static: hashirani fajlovi, keš prvo (nikad se ne mijenjaju).
 * - Kartice korijena (/api/root-panel): keš odmah, osvježavanje u pozadini.
 * - Statistika, admin i prijava nikad ne idu kroz keš.
 * Supabase i audio su na drugim domenima i ne diraju se.
 */
const VERSION = "v1";
const STATIC_CACHE = `static-${VERSION}`;
const PAGE_CACHE = `pages-${VERSION}`;
const DATA_CACHE = `data-${VERSION}`;
const MAX_PAGES = 160;
const OFFLINE_URL = "/offline";

self.addEventListener("install", (event) => {
  event.waitUntil(
    caches
      .open(PAGE_CACHE)
      .then((cache) => cache.addAll([OFFLINE_URL, "/", "/sure"]))
      .then(() => self.skipWaiting()),
  );
});

self.addEventListener("activate", (event) => {
  const keep = new Set([STATIC_CACHE, PAGE_CACHE, DATA_CACHE]);
  event.waitUntil(
    caches
      .keys()
      .then((keys) => Promise.all(keys.filter((k) => !keep.has(k)).map((k) => caches.delete(k))))
      .then(() => self.clients.claim()),
  );
});

function isBypassed(url) {
  return (
    url.pathname.startsWith("/api/track") ||
    url.pathname.startsWith("/admin") ||
    url.pathname.startsWith("/login") ||
    url.pathname.startsWith("/_next/webpack-hmr")
  );
}

async function trim(cacheName, max) {
  const cache = await caches.open(cacheName);
  const keys = await cache.keys();
  for (let i = 0; i < keys.length - max; i++) await cache.delete(keys[i]);
}

async function networkFirst(request, { fallbackToOffline }) {
  const cache = await caches.open(PAGE_CACHE);
  try {
    const response = await fetch(request);
    if (response.ok && response.type === "basic") {
      cache.put(request, response.clone()).then(() => trim(PAGE_CACHE, MAX_PAGES));
    }
    return response;
  } catch (err) {
    const cached = await cache.match(request);
    if (cached) return cached;
    if (fallbackToOffline) {
      const offline = await cache.match(OFFLINE_URL);
      if (offline) return offline;
    }
    throw err;
  }
}

async function cacheFirst(request, cacheName) {
  const cache = await caches.open(cacheName);
  const cached = await cache.match(request);
  if (cached) return cached;
  const response = await fetch(request);
  if (response.ok) cache.put(request, response.clone());
  return response;
}

async function staleWhileRevalidate(request, cacheName) {
  const cache = await caches.open(cacheName);
  const cached = await cache.match(request);
  const network = fetch(request)
    .then((response) => {
      if (response.ok) cache.put(request, response.clone());
      return response;
    })
    .catch(() => cached);
  return cached || network;
}

self.addEventListener("fetch", (event) => {
  const { request } = event;
  if (request.method !== "GET") return;
  const url = new URL(request.url);
  if (url.origin !== self.location.origin || isBypassed(url)) return;

  if (url.pathname.startsWith("/_next/static/") || url.pathname.startsWith("/icons/")) {
    event.respondWith(cacheFirst(request, STATIC_CACHE));
    return;
  }

  if (url.pathname.startsWith("/api/root-panel/")) {
    event.respondWith(staleWhileRevalidate(request, DATA_CACHE));
    return;
  }

  if (request.mode === "navigate") {
    event.respondWith(networkFirst(request, { fallbackToOffline: true }));
    return;
  }

  // RSC podaci za navigaciju unutar aplikacije (Next šalje zaglavlje RSC: 1).
  if (request.headers.get("RSC") === "1") {
    event.respondWith(networkFirst(request, { fallbackToOffline: false }));
  }
});
