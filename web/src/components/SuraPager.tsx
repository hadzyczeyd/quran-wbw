import Link from "next/link";
import { SURAHS } from "@/lib/surahs";
import { Icon } from "./Icon";

/**
 * Prethodna / sljedeća sura na kraju čitača. Svih 114 sura je uvezeno, pa
 * se dostupnost ne provjerava u bazi (to bi pri buildu bio upit po suri).
 */
export function SuraPager({ surahId }: { surahId: number }) {
  const prev = SURAHS.find((s) => s.id === surahId - 1);
  const next = SURAHS.find((s) => s.id === surahId + 1);
  return (
    <nav className="sura-pager" aria-label="Susjedne sure">
      {prev ? (
        <Link prefetch={false} href={`/sura/${prev.id}`} className="sura-pager-link is-prev">
          <Icon name="chevronLeft" />
          <span>
            <span className="sura-pager-label">Prethodna sura</span>
            <span className="sura-pager-name">
              {prev.id}. {prev.nameBs}
            </span>
          </span>
        </Link>
      ) : (
        <span />
      )}
      {next ? (
        <Link prefetch={false} href={`/sura/${next.id}`} className="sura-pager-link is-next">
          <span>
            <span className="sura-pager-label">Sljedeća sura</span>
            <span className="sura-pager-name">
              {next.id}. {next.nameBs}
            </span>
          </span>
          <Icon name="chevronRight" />
        </Link>
      ) : (
        <span />
      )}
    </nav>
  );
}
