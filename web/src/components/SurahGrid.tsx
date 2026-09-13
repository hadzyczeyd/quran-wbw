"use client";

import { useMemo, useState } from "react";
import Link from "next/link";
import { AVAILABLE_SURAH_IDS, SURAHS } from "@/lib/surahs";
import { RevelationIcon } from "./RevelationIcon";

function normalize(text: string): string {
  return text
    .toLowerCase()
    .replace(/đ/g, "d")
    .normalize("NFD")
    .replace(/[̀-ͯ]/g, "");
}

export function SurahGrid() {
  const [query, setQuery] = useState("");
  const availableCount = AVAILABLE_SURAH_IDS.size;

  const filtered = useMemo(() => {
    const q = normalize(query.trim());
    if (q === "") return SURAHS;
    return SURAHS.filter(
      (s) =>
        String(s.id) === q ||
        normalize(s.nameBs).includes(q) ||
        s.nameArabic.includes(query.trim())
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
        <h2 id="grid-heading" style={{ fontSize: "1rem", color: "var(--color-text-muted)" }}>
          Sve sure
        </h2>
        <span style={{ fontSize: "0.85rem", color: "var(--color-text-muted)" }}>
          {availableCount} / {SURAHS.length}
        </span>
      </div>

      <input
        type="search"
        className="surah-search"
        placeholder="Pretraži suru po imenu ili broju…"
        value={query}
        onChange={(e) => setQuery(e.target.value)}
        aria-label="Pretraži sure"
      />

      {filtered.length === 0 ? (
        <p style={{ color: "var(--color-text-muted)", paddingBlock: "1rem" }}>
          Nema sure koja odgovara pretrazi &quot;{query}&quot;.
        </p>
      ) : (
        <div className="surah-grid">
          {filtered.map((surah) => {
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
      )}
    </section>
  );
}
