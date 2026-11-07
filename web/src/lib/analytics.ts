/**
 * Pomoćne funkcije za statistiku posjeta (server). Iz User-Agenta i
 * preporučioca izvlače se samo grube kategorije — ništa što identifikuje
 * osobu. IP adresa se ne čuva; država dolazi iz zaglavlja hostinga ili iz
 * GeoLite2 pretrage u memoriji (vidi api/track).
 */

const BOT_RE =
  /bot|crawl|spider|slurp|preview|fetch|monitor|headless|lighthouse|pagespeed|phantom|puppeteer|playwright|selenium|curl|wget|python|axios|node-fetch|go-http|java\/|electron|claude/i;

export function isBot(ua: string): boolean {
  return !ua || BOT_RE.test(ua);
}

export function parseDevice(ua: string): "mobile" | "tablet" | "desktop" {
  if (/ipad|tablet|kindle|silk|(android(?!.*mobile))/i.test(ua)) return "tablet";
  if (/mobi|iphone|ipod|android/i.test(ua)) return "mobile";
  return "desktop";
}

export function parseBrowser(ua: string): string {
  if (/edg\//i.test(ua)) return "Edge";
  if (/opr\/|opera/i.test(ua)) return "Opera";
  if (/samsungbrowser/i.test(ua)) return "Samsung Internet";
  if (/firefox|fxios/i.test(ua)) return "Firefox";
  if (/chrome|crios/i.test(ua)) return "Chrome";
  if (/safari/i.test(ua)) return "Safari";
  return "Ostalo";
}

export function parseOs(ua: string): string {
  if (/windows/i.test(ua)) return "Windows";
  if (/iphone|ipad|ipod/i.test(ua)) return "iOS";
  if (/android/i.test(ua)) return "Android";
  if (/mac os x|macintosh/i.test(ua)) return "macOS";
  if (/cros/i.test(ua)) return "ChromeOS";
  if (/linux/i.test(ua)) return "Linux";
  return "Ostalo";
}

/** In-app preglednik društvene mreže/aplikacije, ako se može prepoznati. */
export function parseInApp(ua: string): string | null {
  if (/FBAN|FBAV|FB_IAB|FBIOS/i.test(ua)) return "Facebook";
  if (/Instagram/i.test(ua)) return "Instagram";
  if (/musical_ly|BytedanceWebview|TikTok/i.test(ua)) return "TikTok";
  if (/WhatsApp/i.test(ua)) return "WhatsApp";
  if (/Viber/i.test(ua)) return "Viber";
  if (/Telegram/i.test(ua)) return "Telegram";
  if (/Snapchat/i.test(ua)) return "Snapchat";
  if (/LinkedInApp/i.test(ua)) return "LinkedIn";
  if (/Twitter/i.test(ua)) return "X (Twitter)";
  if (/Pinterest/i.test(ua)) return "Pinterest";
  if (/Line\//i.test(ua)) return "LINE";
  return null;
}

const SOURCES: [RegExp, string][] = [
  [/(^|\.)google\./, "Google"],
  [/(^|\.)bing\.com$/, "Bing"],
  [/(^|\.)duckduckgo\.com$/, "DuckDuckGo"],
  [/(^|\.)yahoo\./, "Yahoo"],
  [/(^|\.)yandex\./, "Yandex"],
  [/(^|\.)(facebook\.com|fb\.com|fb\.me|m\.facebook\.com|l\.facebook\.com|lm\.facebook\.com)$/, "Facebook"],
  [/(^|\.)instagram\.com$/, "Instagram"],
  [/(^|\.)(whatsapp\.com|wa\.me)$/, "WhatsApp"],
  [/(^|\.)(t\.co|twitter\.com|x\.com)$/, "X (Twitter)"],
  [/(^|\.)(youtube\.com|youtu\.be)$/, "YouTube"],
  [/(^|\.)tiktok\.com$/, "TikTok"],
  [/(^|\.)(t\.me|telegram\.org)$/, "Telegram"],
  [/(^|\.)viber\.com$/, "Viber"],
  [/(^|\.)(linkedin\.com|lnkd\.in)$/, "LinkedIn"],
  [/(^|\.)reddit\.com$/, "Reddit"],
  [/(^|\.)pinterest\./, "Pinterest"],
  [/(^|\.)(chatgpt\.com|openai\.com)$/, "ChatGPT"],
  [/(^|\.)(claude\.ai|perplexity\.ai)$/, "AI asistent"],
];

/** Izvor dolaska: utm_source ima prednost, zatim domen preporučioca. */
export function classifySource(referrerHost: string | null, utmSource: string | null): string {
  const utm = (utmSource ?? "").trim().toLowerCase();
  if (utm) {
    for (const [re, name] of SOURCES) if (re.test(utm) || name.toLowerCase().startsWith(utm)) return name;
    return utm.slice(0, 60);
  }
  if (!referrerHost) return "Direktno";
  for (const [re, name] of SOURCES) if (re.test(referrerHost)) return name;
  return referrerHost.slice(0, 60);
}

const UUID_RE = /^[0-9a-f]{8}-[0-9a-f]{4}-[1-8][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$/i;

export function isUuid(v: unknown): v is string {
  return typeof v === "string" && UUID_RE.test(v);
}
