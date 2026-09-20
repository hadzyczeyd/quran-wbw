import type { SurahMeta } from "@/lib/surahs";
import { Bismillah } from "./Bismillah";
import { RevelationIcon } from "./RevelationIcon";

interface SuraOpeningHeaderProps {
  surah: SurahMeta;
}

/**
 * Blok prije prvog ajeta — bismilla (bez prijevoda, isto kao na
 * hero sekciji početne) i meta-linija. Nije fiksiran, dio normalnog
 * toka teksta (vidi reader.css .sura-opening).
 *
 * Sura 9 (Et-Tevba) tradicionalno nema bismillu; sura 1 (El-Fatiha)
 * je već nosi kao svoj prvi ajet, pa se ovdje ne ponavlja.
 */
export function SuraOpeningHeader({ surah }: SuraOpeningHeaderProps) {
  const showBismillah = surah.id !== 1 && surah.id !== 9;

  return (
    <div className="sura-opening">
      {showBismillah && <Bismillah />}
      <p className="sura-opening-name-arabic">{surah.nameArabic}</p>
      <h2 className="sura-opening-name">{surah.nameBs}</h2>
      <p className="sura-opening-meta">
        <RevelationIcon type={surah.revelationType} />
        {surah.revelationType === "meccan" ? "Mekkanska sura" : "Medinska sura"} · {surah.ayahCount} ajeta
      </p>
    </div>
  );
}
