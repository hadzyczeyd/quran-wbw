import { getSurahExtraMeta } from "@/lib/quranMeta";
import type { SurahMeta } from "@/lib/surahs";
import { RevelationIcon } from "./RevelationIcon";

interface SurahInfoSidebarProps {
  surah: SurahMeta;
}

function juzLabel(juz: number[]): string {
  return juz.length === 1 ? `${juz[0]}.` : `${juz[0]}.–${juz[juz.length - 1]}.`;
}

/**
 * Kartica o suri, lijevo od teksta u čitaču (samo širi ekran — vidi
 * reader.css), iznad legende boja. Isti vizuelni jezik kao kartice
 * sure na početnoj (SurahGrid), uz opširnije provjerljive podatke.
 */
export function SurahInfoSidebar({ surah }: SurahInfoSidebarProps) {
  const extra = getSurahExtraMeta(surah.id);

  return (
    <aside className="surah-info-sidebar" aria-label="Informacije o suri">
      <span className="surah-card-number">{surah.id}</span>
      <span className="surah-card-arabic">{surah.nameArabic}</span>
      <span className="surah-card-name">{surah.nameBs}</span>
      <span className="surah-card-meta">
        <RevelationIcon type={surah.revelationType} />
        {surah.revelationType === "meccan" ? "Mekkanska" : "Medinska"} ·{" "}
        {surah.ayahCount} ajeta
      </span>
      {extra && (
        <dl className="surah-info-details">
          <div>
            <dt>Redoslijed objave</dt>
            <dd>{extra.order}.</dd>
          </div>
          <div>
            <dt>Džuz</dt>
            <dd>{juzLabel(extra.juz)}</dd>
          </div>
          <div>
            <dt>Rukua</dt>
            <dd>{extra.rukus}</dd>
          </div>
          <div>
            <dt>Riječi</dt>
            <dd>{extra.words.toLocaleString("bs-BA")}</dd>
          </div>
          {extra.sajda.length > 0 && (
            <div>
              <dt>Sedžda</dt>
              <dd>{extra.sajda.map(([a]) => `${a}. ajet`).join(", ")}</dd>
            </div>
          )}
        </dl>
      )}
    </aside>
  );
}
