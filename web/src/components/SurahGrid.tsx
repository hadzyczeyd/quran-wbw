import Link from "next/link";
import { AVAILABLE_SURAH_IDS, SURAHS } from "@/lib/surahs";
import { RevelationIcon } from "./RevelationIcon";

export function SurahGrid() {
  const availableCount = AVAILABLE_SURAH_IDS.size;

  return (
    <section aria-labelledby="grid-heading">
      <div
        style={{
          display: "flex",
          justifyContent: "space-between",
          alignItems: "baseline",
          paddingBlock: "0.5rem",
        }}
      >
        <h2 id="grid-heading" style={{ fontSize: "1rem", color: "var(--color-text-muted)" }}>
          Sve sure
        </h2>
        <span style={{ fontSize: "0.85rem", color: "var(--color-text-muted)" }}>
          {availableCount} / {SURAHS.length}
        </span>
      </div>

      <div className="surah-grid">
        {SURAHS.map((surah) => {
          const available = AVAILABLE_SURAH_IDS.has(surah.id);
          const card = (
            <>
              <span className="surah-card-number">{surah.id}</span>
              <span className="surah-card-arabic">{surah.nameArabic}</span>
              <span className="surah-card-name">{surah.nameBs}</span>
              <span className="surah-card-meta">
                <RevelationIcon type={surah.revelationType} />
                {surah.ayahCount} ajeta
              </span>
            </>
          );

          return available ? (
            <Link key={surah.id} href={`/sura/${surah.id}`} className="surah-card">
              {card}
            </Link>
          ) : (
            <span key={surah.id} className="surah-card is-unavailable" aria-disabled="true">
              {card}
            </span>
          );
        })}
      </div>
    </section>
  );
}
