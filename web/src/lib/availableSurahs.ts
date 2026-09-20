import { supabase } from "./supabase";

const PAGE_SIZE = 1000;

/**
 * Sure koje stvarno imaju uvezene ajete u bazi (ne cijela statička lista).
 *
 * Supabase/PostgREST po defaultu vraća najviše 1000 redova po upitu
 * (db-max-rows), bez obzira što JS klijent ne traži limit — kad je
 * ukupan broj ajeta prešao 1000, upit bez paginacije tiho odsijeca
 * ostatak, pa su sure koje "padnu" iza tog reza nestajale s liste
 * dostupnih iako im podaci postoje. Zato se ovdje čita stranicu po
 * stranicu dok se ne dobije nepotpuna (zadnja) stranica.
 */
export async function getAvailableSurahIds(): Promise<Set<number>> {
  const ids = new Set<number>();
  let from = 0;

  for (;;) {
    const { data, error } = await supabase
      .from("ayahs")
      .select("surah_id")
      .range(from, from + PAGE_SIZE - 1);
    if (error || !data) break;
    for (const row of data) ids.add(row.surah_id);
    if (data.length < PAGE_SIZE) break;
    from += PAGE_SIZE;
  }

  return ids;
}
