/**
 * Recitacija cijelog ajeta — everyayah.com, jedan mp3 fajl po ajetu,
 * pušta se cijeli bez timinga.
 */
export function ayahAudioUrl(surahId: number, ayahNumber: number): string {
  const s = String(surahId).padStart(3, "0");
  const a = String(ayahNumber).padStart(3, "0");
  return `https://everyayah.com/data/Husary_128kbps/${s}${a}.mp3`;
}

/**
 * Izolovan izgovor JEDNE riječi — Quran Foundation / Tafsir Center for
 * Quranic Studies, servirano preko javnog CDN-a audio.qurancdn.com.
 * Putanja je deterministička (wbw/{sura}_{ajet}_{riječ}.mp3, potvrđeno
 * direktnim testom), pa se gradi lokalno iz qac_location bez potrebe za
 * pozivom Content API-ja u browseru.
 *
 * Samo streaming — bez trajnog offline keširanja (Quran Foundation
 * Developer Terms 3.1 ograničavaju čuvanje njihovog sadržaja na 7 dana).
 */
export function wordAudioUrl(surahId: number, ayahNumber: number, wordPosition: number): string {
  const s = String(surahId).padStart(3, "0");
  const a = String(ayahNumber).padStart(3, "0");
  const w = String(wordPosition).padStart(3, "0");
  return `https://audio.qurancdn.com/wbw/${s}_${a}_${w}.mp3`;
}
