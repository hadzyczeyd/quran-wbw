"use client";

import { useMemo, useState } from "react";
import Link from "next/link";
import { JUZ_STARTS, surahsInJuz } from "@/lib/quranMeta";
import { SURAHS } from "@/lib/surahs";
import { RevelationIcon } from "./RevelationIcon";

function normalize(text: string): string {
  return text
    .toLowerCase()
    .replace(/đ/g, "d")
    .normalize("NFD")
    .replace(/[̀-ͯ]/g, "");
}

interface SurahGridProps {
  availableSurahIds: Set<number>;
}

export function SurahGrid({ availableSurahIds }: SurahGridProps) {
  const [query, setQuery] = useState("");
  const [view, setView] = useState<"sure" | "dzuz">("sure");
  const availableCount = availableSurahIds.size;

  const filtered = useMemo(() => {
    const q = normalize(query.trim());
    if (q === "") return SURAHS;
    return SURAHS.filter(
      (s) =>
        String(s.id) === q ||
        normalize(s.nameBs).includes(q) ||
        s.nameArabic.includes(query.trim()),
    );
  }, [query]);

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
        <h2
          id="grid-heading"
          style={{ fontSize: "1rem", color: "var(--color-text-muted)" }}
        >
          Sve sure
        </h2>
        <span style={{ fontSize: "0.85rem", color: "var(--color-text-muted)" }}>
          {availableCount} / {SURAHS.length}
        </span>
      </div>

      <div className="surah-view-toggle" role="tablist" aria-label="Prikaz">
        <button
          type="button"
          role="tab"
          aria-selected={view === "sure"}
          onClick={() => setView("sure")}
        >
          Sure
        </button>
        <button
          type="button"
          role="tab"
          aria-selected={view === "dzuz"}
          onClick={() => setView("dzuz")}
        >
          Džuzevi
        </button>
      </div>

      {view === "dzuz" ? (
        <JuzList availableSurahIds={availableSurahIds} />
      ) : (
        <>
          <input
            type="search"
            className="surah-search"
            placeholder="Pretraži suru po imenu ili broju…"
            value={query}
            onChange={(e) => setQuery(e.target.value)}
            aria-label="Pretraži sure"
          />

          {filtered.length === 0 ? (
            <p
              style={{ color: "var(--color-text-muted)", paddingBlock: "1rem" }}
            >
              Nema sure koja odgovara pretrazi &quot;{query}&quot;.
            </p>
          ) : (
            <div className="surah-grid">
              {filtered.map((surah) => {
                const available = availableSurahIds.has(surah.id);
                const card = (
                  <>
                    <div className="surah-card-row">
                      <span className="surah-card-number">{surah.id}</span>
                      <span className="surah-card-meta">
                        <RevelationIcon type={surah.revelationType} />
                        {surah.ayahCount} ajeta
                      </span>
                    </div>
                    <div className="surah-card-row">
                      <span className="surah-card-name">{surah.nameBs}</span>
                      <span className="surah-card-arabic">
                        {surah.nameArabic}
                      </span>
                    </div>
                  </>
                );

                return available ? (
                  <Link
                    key={surah.id}
                    href={`/sura/${surah.id}`}
                    className="surah-card"
                  >
                    {card}
                  </Link>
                ) : (
                  <span
                    key={surah.id}
                    className="surah-card is-unavailable"
                    aria-disabled="true"
                  >
                    {card}
                  </span>
                );
              })}
            </div>
          )}
        </>
      )}
    </section>
  );
}

function JuzList({ availableSurahIds }: { availableSurahIds: Set<number> }) {
  return (
    <div className="juz-grid">
      {JUZ_STARTS.map(([juz, startSurah, startAyah]) => {
        const start = SURAHS.find((s) => s.id === startSurah);
        const startHref = `/sura/${startSurah}#ajet-${startAyah}`;
        return (
          <section
            key={juz}
            className="juz-card"
            aria-labelledby={`juz-${juz}`}
          >
            <div className="juz-card-head">
              <h3 id={`juz-${juz}`} className="juz-card-title">
                Džuz {juz}
              </h3>
              {availableSurahIds.has(startSurah) ? (
                <Link href={startHref} className="juz-card-start">
                  od {start?.nameBs} {startAyah}
                </Link>
              ) : (
                <span className="juz-card-start is-unavailable">
                  od {start?.nameBs} {startAyah}
                </span>
              )}
            </div>
            <ul className="juz-card-surahs">
              {surahsInJuz(juz).map(({ surahId, fromAyah }) => {
                const s = SURAHS.find((x) => x.id === surahId);
                const label = `${surahId}. ${s?.nameBs ?? ""}`;
                return (
                  <li key={surahId}>
                    {availableSurahIds.has(surahId) ? (
                      <Link
                        href={
                          fromAyah > 1
                            ? `/sura/${surahId}#ajet-${fromAyah}`
                            : `/sura/${surahId}`
                        }
                      >
                        {label}
                      </Link>
                    ) : (
                      <span className="is-unavailable">{label}</span>
                    )}
                  </li>
                );
              })}
            </ul>
          </section>
        );
      })}
    </div>
  );
}
