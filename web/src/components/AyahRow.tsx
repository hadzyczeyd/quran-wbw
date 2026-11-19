"use client";

import { memo, useState } from "react";
import type { ClientAyah, ClientToken, ClientWord } from "@/lib/types";
import { ArabicWord } from "./ArabicWord";
import { AyahEndMark } from "./AyahEndMark";
import { BosnianTokenSpan } from "./BosnianTokenSpan";
import { Icon } from "./Icon";

interface AyahRowProps {
  surahId: number;
  ayah: ClientAyah;
  activeWordId: string | null;
  activeTokenIds: Set<string>;
  onWordClick: (word: ClientWord) => void;
  onTokenClick: (token: ClientToken) => void;
  onPlayAyah: (ayahNumber: number) => void;
  isAyahPlaying: boolean;
  /** Broj džuza koji počinje ovim ajetom. */
  juzStart?: number;
}

function CopyLinkButton({ surahId, ayahNumber }: { surahId: number; ayahNumber: number }) {
  const [copied, setCopied] = useState(false);
  return (
    <button
      type="button"
      className="icon-btn"
      aria-label={copied ? "Link kopiran" : `Kopiraj link na ajet ${ayahNumber}`}
      onClick={async (e) => {
        e.stopPropagation();
        const url = `${location.origin}/sura/${surahId}#ajet-${ayahNumber}`;
        try {
          await navigator.clipboard.writeText(url);
          setCopied(true);
          setTimeout(() => setCopied(false), 1800);
        } catch {
          // Bez dozvole za clipboard — ništa.
        }
      }}
    >
      <Icon name={copied ? "check" : "link"} size={18} />
    </button>
  );
}

export const AyahRow = memo(function AyahRow({
  surahId,
  ayah,
  activeWordId,
  activeTokenIds,
  onWordClick,
  onTokenClick,
  onPlayAyah,
  isAyahPlaying,
  juzStart,
}: AyahRowProps) {
  return (
    <article className="ayah" id={`ajet-${ayah.n}`} data-ayah={ayah.n} aria-label={`Ajet ${ayah.n}`}>
      <div className="ayah-bar">
        <span className="ayah-number">{ayah.n}</span>
        {juzStart && <span className="ayah-juz">Početak {juzStart}. džuza</span>}
        <span className="ayah-actions">
          <CopyLinkButton surahId={surahId} ayahNumber={ayah.n} />
          <button
            type="button"
            className="icon-btn play-btn"
            onClick={(e) => {
              e.stopPropagation();
              onPlayAyah(ayah.n);
            }}
            aria-label={isAyahPlaying ? `Zaustavi ajet ${ayah.n}` : `Preslušaj ajet ${ayah.n}`}
            aria-pressed={isAyahPlaying}
          >
            <Icon name={isAyahPlaying ? "pause" : "play"} size={18} />
          </button>
        </span>
      </div>

      <p className="ayah-arabic" dir="rtl" lang="ar">
        {ayah.words.map((w) => (
          <span key={w.id}>
            <ArabicWord word={w} isHighlighted={activeWordId === w.id} onWordClick={onWordClick} />{" "}
          </span>
        ))}
        <AyahEndMark number={ayah.n} />
      </p>

      <p className="ayah-translation" lang="bs">
        {ayah.tokens.map((t) => (
          <span key={t.id}>
            <BosnianTokenSpan token={t} isHighlighted={activeTokenIds.has(t.id)} onTokenClick={onTokenClick} />{" "}
          </span>
        ))}
      </p>
    </article>
  );
});
