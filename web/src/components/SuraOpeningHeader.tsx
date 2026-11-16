import { getSurahExtraMeta } from "@/lib/quranMeta";
import type { SurahMeta } from "@/lib/surahs";
import { Bismillah } from "./Bismillah";

/**
 * Otvarajući blok sure: arapski i bosanski naziv, osnovni podaci i bismilla.
 * Sura 9 (Et-Tevba) nema bismillu; El-Fatiha je nosi kao prvi ajet.
 */
export function SuraOpeningHeader({ surah }: { surah: SurahMeta }) {
  const showBismillah = surah.id !== 1 && surah.id !== 9;
  const extra = getSurahExtraMeta(surah.id);
  const juz = extra?.juz ?? [];

  const facts: [string, string][] = [
    ["Objava", surah.revelationType === "meccan" ? "Mekka" : "Medina"],
    ["Ajeta", String(surah.ayahCount)],
  ];
  if (juz.length > 0) facts.push(["Džuz", juz.length === 1 ? `${juz[0]}` : `${juz[0]}–${juz[juz.length - 1]}`]);
  if (extra) facts.push(["Redoslijed objave", `${extra.order}.`]);
  if (extra && extra.sajda.length > 0) facts.push(["Sedžda", extra.sajda.map(([a]) => `${a}. ajet`).join(", ")]);

  return (
    <header className="sura-opening">
      <p className="sura-opening-ar" lang="ar" dir="rtl">
        {surah.nameArabic}
      </p>
      <h1 className="sura-opening-name">
        <span className="visually-hidden">Sura </span>
        {surah.nameBs}
      </h1>
      <dl className="sura-facts">
        {facts.map(([k, v]) => (
          <div key={k}>
            <dt>{k}</dt>
            <dd>{v}</dd>
          </div>
        ))}
      </dl>
      {showBismillah && <Bismillah plain />}
    </header>
  );
}
