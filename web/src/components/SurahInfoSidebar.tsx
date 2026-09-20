import type { SurahMeta } from "@/lib/surahs";
import { RevelationIcon } from "./RevelationIcon";

interface SurahInfoSidebarProps {
  surah: SurahMeta;
}

/**
 * Fiksna kartica o suri, lijevo od teksta u čitaču (samo širi ekran —
 * vidi reader.css). Ogledalo desne legend-sidebar trake, isti vizuelni
 * jezik kao kartice sure na početnoj (SurahGrid).
 */
export function SurahInfoSidebar({ surah }: SurahInfoSidebarProps) {
  return (
    <aside className="surah-info-sidebar" aria-label="Informacije o suri">
      <span className="surah-card-number">{surah.id}</span>
      <span className="surah-card-arabic">{surah.nameArabic}</span>
      <span className="surah-card-name">{surah.nameBs}</span>
      <span className="surah-card-meta">
        <RevelationIcon type={surah.revelationType} />
        {surah.ayahCount} ajeta
      </span>
    </aside>
  );
}
