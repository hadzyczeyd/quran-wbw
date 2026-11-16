"use client";

import { useDeferredValue, useMemo, useState } from "react";
import Link from "next/link";
import { JUZ_STARTS, surahsInJuz } from "@/lib/quranMeta";
import { SURAHS, type SurahMeta } from "@/lib/surahs";
import { Icon } from "./Icon";

function normalize(text: string): string {
  return text
    .toLowerCase()
    .replace(/đ/g, "d")
    .normalize("NFD")
    .replace(/[̀-ͯ'’\-\s]/g, "");
}

function ayahLabel(n: number) {
  const d = n % 10;
  const dd = n % 100;
  return d === 1 && dd !== 11 ? "ajet" : "ajeta";
}

function SurahRow({ surah, available }: { surah: SurahMeta; available: boolean }) {
  const body = (
    <>
      <span className="surah-num">{surah.id}</span>
      <span className="surah-main">
        <span className="surah-name">{surah.nameBs}</span>
        <span className="surah-meta">
          {surah.revelationType === "meccan" ? "Mekkanska" : "Medinska"}, {surah.ayahCount}&nbsp;
          {ayahLabel(surah.ayahCount)}
        </span>
      </span>
      <span className="surah-ar" lang="ar" dir="rtl">
        {surah.nameArabic}
      </span>
    </>
  );
  return (
    <li>
      {available ? (
        <Link href={`/sura/${surah.id}`} className="surah-row">
          {body}
        </Link>
      ) : (
        <span className="surah-row is-unavailable" aria-disabled="true">
          {body}
        </span>
      )}
    </li>
  );
}

export function SurahGrid({
  availableSurahIds,
  headingLevel = 2,
}: {
  availableSurahIds: Set<number>;
  headingLevel?: 1 | 2;
}) {
  const [query, setQuery] = useState("");
  const [view, setView] = useState<"sure" | "dzuz">("sure");
  const deferred = useDeferredValue(query);

  const filtered = useMemo(() => {
    const q = normalize(deferred.trim());
    if (q === "") return SURAHS;
    return SURAHS.filter(
      (s) => String(s.id) === q || normalize(s.nameBs).includes(q) || s.nameArabic.includes(deferred.trim()),
    );
  }, [deferred]);

  const Heading = headingLevel === 1 ? "h1" : "h2";

  return (
    <section className="surah-index" aria-labelledby="surah-index-heading">
      <div className="surah-index-head">
        <Heading id="surah-index-heading" className="section-title">
          Sure
        </Heading>
        <div className="segmented" role="tablist" aria-label="Prikaz">
          <button type="button" role="tab" aria-selected={view === "sure"} onClick={() => setView("sure")}>
            Po surama
          </button>
          <button type="button" role="tab" aria-selected={view === "dzuz"} onClick={() => setView("dzuz")}>
            Po džuzevima
          </button>
        </div>
      </div>

      {view === "sure" ? (
        <>
          <label className="search">
            <Icon name="search" />
            <span className="visually-hidden">Pretraži sure</span>
            <input
              type="search"
              placeholder="Ime ili broj sure, npr. Ja-Sin ili 36…"
              value={query}
              onChange={(e) => setQuery(e.target.value)}
              autoComplete="off"
              enterKeyHint="search"
            />
          </label>

          {filtered.length === 0 ? (
            <div className="empty-state">
              <p>Nijedna sura ne odgovara pretrazi „{query}”.</p>
              <button type="button" className="btn btn-secondary" onClick={() => setQuery("")}>
                Očisti pretragu
              </button>
            </div>
          ) : (
            <ul className="surah-list">
              {filtered.map((surah) => (
                <SurahRow key={surah.id} surah={surah} available={availableSurahIds.has(surah.id)} />
              ))}
            </ul>
          )}
        </>
      ) : (
        <JuzList availableSurahIds={availableSurahIds} />
      )}
    </section>
  );
}

function JuzList({ availableSurahIds }: { availableSurahIds: Set<number> }) {
  return (
    <ol className="juz-list">
      {JUZ_STARTS.map(([juz, startSurah, startAyah]) => {
        const start = SURAHS.find((s) => s.id === startSurah);
        return (
          <li key={juz} className="juz-card">
            <div className="juz-card-head">
              <h3 className="juz-card-title">Džuz {juz}</h3>
              {availableSurahIds.has(startSurah) ? (
                <Link href={`/sura/${startSurah}#ajet-${startAyah}`} className="juz-card-start">
                  Počinje: {start?.nameBs} {startAyah}
                </Link>
              ) : (
                <span className="juz-card-start">
                  Počinje: {start?.nameBs} {startAyah}
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
                      <Link href={fromAyah > 1 ? `/sura/${surahId}#ajet-${fromAyah}` : `/sura/${surahId}`}>
                        {label}
                      </Link>
                    ) : (
                      <span className="is-unavailable">{label}</span>
                    )}
                  </li>
                );
              })}
            </ul>
          </li>
        );
      })}
    </ol>
  );
}
