import { supabase } from "./supabase";

/** Sure koje stvarno imaju uvezene ajete u bazi (ne cijela statička lista). */
export async function getAvailableSurahIds(): Promise<Set<number>> {
  const { data, error } = await supabase.from("ayahs").select("surah_id");
  if (error || !data) return new Set();
  return new Set(data.map((r) => r.surah_id));
}
