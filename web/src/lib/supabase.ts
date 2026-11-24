import { createClient } from "@supabase/supabase-js";

/**
 * Oznaka keša za upit prema suri na koju se odnosi (surah_id=eq.N ili raspon
 * ID-ova "SNNN-"), da /api/revalidate može obrisati keširane podatke samo te
 * sure. Bez toga osvježena stranica bi se iscrtala iznova, ali sa starim
 * podacima iz Next keša upita (fetch cache).
 */
function suraTag(url: string): string | null {
  const u = decodeURIComponent(url);
  const m = /surah_id=eq\.(\d{1,3})\b/.exec(u) ?? /=gte\.S(\d{3})-/.exec(u);
  return m ? `sura-${Number(m[1])}` : null;
}

const taggedFetch: typeof fetch = (input, init) => {
  const url = typeof input === "string" ? input : input instanceof URL ? input.href : input.url;
  const tag = suraTag(url);
  return fetch(input, tag ? { ...init, next: { tags: ["supabase", tag] } } : init);
};

/**
 * Javni klijent — koristi "anon" ključ, ograničen RLS politikama (samo
 * čitanje sadržaja, samo upis na contact_messages). Bezbjedan za browser
 * i server komponente podjednako.
 */
export const supabase = createClient(process.env.NEXT_PUBLIC_SUPABASE_URL!, process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY!, {
  global: { fetch: taggedFetch },
});
