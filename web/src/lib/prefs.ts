/**
 * Korisničke postavke prikaza (tema, veličina teksta, boje, prijevod).
 * Čuvaju se u localStorage i primjenjuju kao data-atributi na <html>, pa
 * CSS reaguje bez ponovnog iscrtavanja React stabla. PREFS_SCRIPT ih
 * postavlja prije prvog iscrtavanja (bez bljeska pogrešne teme).
 */
export type Theme = "system" | "light" | "dark";
export type Size = "s" | "m" | "l" | "xl";

export interface Prefs {
  theme: Theme;
  arSize: Size;
  trSize: Size;
  colors: "on" | "off";
  translation: "on" | "off";
}

export const DEFAULT_PREFS: Prefs = {
  theme: "system",
  arSize: "m",
  trSize: "m",
  colors: "on",
  translation: "on",
};

const KEY = "rpr-prefs";
const EVENT = "rpr-prefs-change";

const ATTR: Record<keyof Prefs, string> = {
  theme: "data-theme",
  arSize: "data-ar-size",
  trSize: "data-tr-size",
  colors: "data-colors",
  translation: "data-translation",
};

/** Inline skripta za <head>: čita postavke i postavlja atribute prije iscrtavanja. */
export const PREFS_SCRIPT = `(function(){try{var p=JSON.parse(localStorage.getItem(${JSON.stringify(
  KEY,
)})||"{}"),a=${JSON.stringify(ATTR)},d=document.documentElement;for(var k in a){var v=p[k];if(v&&!(k==="theme"&&v==="system"))d.setAttribute(a[k],v)}}catch(e){}})();`;

let cached: Prefs | null = null;

export function readPrefs(): Prefs {
  if (cached) return cached;
  try {
    cached = { ...DEFAULT_PREFS, ...JSON.parse(localStorage.getItem(KEY) ?? "{}") };
  } catch {
    cached = DEFAULT_PREFS;
  }
  return cached!;
}

export function getServerPrefs(): Prefs {
  return DEFAULT_PREFS;
}

export function setPref<K extends keyof Prefs>(key: K, value: Prefs[K]) {
  const next = { ...readPrefs(), [key]: value };
  cached = next;
  try {
    localStorage.setItem(KEY, JSON.stringify(next));
  } catch {
    // Privatni prozor / blokirana pohrana — postavka važi do zatvaranja stranice.
  }
  const el = document.documentElement;
  if (key === "theme" && value === "system") el.removeAttribute(ATTR.theme);
  else el.setAttribute(ATTR[key], String(value));
  if (key === "theme") syncThemeColor();
  window.dispatchEvent(new Event(EVENT));
}

export function subscribePrefs(cb: () => void) {
  window.addEventListener(EVENT, cb);
  return () => window.removeEventListener(EVENT, cb);
}

/** Boja statusne trake (PWA / mobilni browser) prati izabranu temu. */
export function syncThemeColor() {
  const bg = getComputedStyle(document.documentElement).getPropertyValue("--bg").trim();
  document.querySelectorAll('meta[name="theme-color"]').forEach((m) => {
    if (bg) m.setAttribute("content", bg);
    m.removeAttribute("media");
  });
}
