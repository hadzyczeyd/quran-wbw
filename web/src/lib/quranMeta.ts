import meta from "@/data/quranMeta.json";

/** Metapodaci sure iz Tanzil quran-data.xml (redoslijed objave, rukui, džuzevi, sedžde) i broj riječi iz QAC-a. */
export interface SurahExtraMeta {
  order: number;
  rukus: number;
  words: number;
  juz: number[];
  /** [ajet, "obligatory" | "recommended"] */
  sajda: [number, string][];
}

const SURAHS = meta.surahs as unknown as Record<string, SurahExtraMeta>;

/** Početak svakog džuza: [broj džuza, sura, ajet]. */
export const JUZ_STARTS = meta.juz as [number, number, number][];

export function getSurahExtraMeta(surahId: number): SurahExtraMeta | null {
  return SURAHS[String(surahId)] ?? null;
}

/** Ajeti u ovoj suri na kojima počinje novi džuz: ajet → broj džuza. */
export function juzStartsInSurah(surahId: number): Record<number, number> {
  const out: Record<number, number> = {};
  for (const [juz, s, a] of JUZ_STARTS) if (s === surahId) out[a] = juz;
  return out;
}

/** Sure koje se (bar djelimično) nalaze u džuzu, s ajetom od kojeg u tom džuzu počinju. */
export function surahsInJuz(
  juz: number,
): { surahId: number; fromAyah: number }[] {
  const out: { surahId: number; fromAyah: number }[] = [];
  for (const [id, m] of Object.entries(SURAHS)) {
    if (!m.juz.includes(juz)) continue;
    const start = JUZ_STARTS[juz - 1];
    const fromAyah = Number(id) === start[1] ? start[2] : 1;
    out.push({ surahId: Number(id), fromAyah });
  }
  return out.sort((a, b) => a.surahId - b.surahId);
}
