import { supabase } from "@/lib/supabase";
import {
  classifySource,
  isBot,
  isUuid,
  parseBrowser,
  parseDevice,
  parseInApp,
  parseOs,
} from "@/lib/analytics";

/**
 * Prima jedan pregled stranice od posjetioca koji je pristao na statistiku
 * (vidi ConsentManager). Broji se samo na produkciji, bez botova; IP adresa
 * se ne čuva — koristi se samo država iz zaglavlja hostinga (Vercel/Cloudflare).
 * Produkcija: Vercel (VERCEL_ENV=production) ili Hostinger (PRODUKCIJA=1).
 */
export async function POST(request: Request) {
  const empty = new Response(null, { status: 204 });

  const isProduction =
    process.env.VERCEL_ENV === "production" || process.env.PRODUKCIJA === "1";
  if (!isProduction) return empty;

  const ua = request.headers.get("user-agent") ?? "";
  if (isBot(ua)) return empty;

  // Samo zahtjevi s vlastite stranice.
  const origin = request.headers.get("origin");
  // Iza Hostingerovog proxyja izvorni host može stići u x-forwarded-host.
  const host = request.headers.get("x-forwarded-host")?.split(",")[0].trim() || request.headers.get("host");
  if (!origin || !host || new URL(origin).host !== host) return empty;

  let body: Record<string, unknown>;
  try {
    body = await request.json();
  } catch {
    return empty;
  }

  const { visitorId, sessionId } = body;
  const path = typeof body.path === "string" ? body.path : "";
  if (!isUuid(visitorId) || !isUuid(sessionId) || !path.startsWith("/") || path.length > 300) {
    return empty;
  }

  let referrerHost: string | null = null;
  let source = "Interno";
  if (body.firstInSession === true) {
    if (typeof body.referrer === "string" && body.referrer) {
      try {
        const h = new URL(body.referrer).hostname.toLowerCase().replace(/^www\./, "");
        if (h && h !== host.replace(/^www\./, "").split(":")[0]) referrerHost = h.slice(0, 200);
      } catch {
        /* neispravan referrer — ignoriše se */
      }
    }
    const utm = typeof body.utmSource === "string" ? body.utmSource.slice(0, 60) : null;
    source = classifySource(referrerHost, utm);
  }

  const country =
    request.headers.get("x-vercel-ip-country") ??
    request.headers.get("cf-ipcountry") ??
    request.headers.get("x-country-code");

  await supabase.rpc("record_page_view", {
    p_visitor_id: visitorId,
    p_session_id: sessionId,
    p_path: path,
    p_source: source,
    p_referrer_host: referrerHost,
    p_country: country && /^[A-Za-z]{2}$/.test(country) && country.toUpperCase() !== "XX" ? country.toUpperCase() : null,
    p_device: parseDevice(ua),
    p_browser: parseBrowser(ua),
    p_os: parseOs(ua),
    p_in_app: parseInApp(ua),
  });

  return empty;
}
