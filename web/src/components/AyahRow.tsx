"use client";

import { memo, useState } from "react";
import type { Ayah, BosnianToken, QacWord } from "@/lib/types";
import { ArabicWord } from "./ArabicWord";
import { AyahEndMark } from "./AyahEndMark";
import { BosnianTokenSpan } from "./BosnianTokenSpan";
import { Icon } from "./Icon";

interface AyahRowProps {
  surahId: number;
  ayah: Ayah;
  activeWordId: string | null;
  activeTokenIds: Set<string>;
  onWordClick: (word: QacWord) => void;
  onTokenClick: (token: BosnianToken) => void;
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
    <article className="ayah" id={`ajet-${ayah.ayah_number}`} data-ayah={ayah.ayah_number} aria-label={`Ajet ${ayah.ayah_number}`}>
      <div className="ayah-bar">
        <span className="ayah-number">{ayah.ayah_number}</span>
        {juzStart && <span className="ayah-juz">Početak {juzStart}. džuza</span>}
        <span className="ayah-actions">
          <CopyLinkButton surahId={surahId} ayahNumber={ayah.ayah_number} />
          <button
            type="button"
            className="icon-btn play-btn"
            onClick={(e) => {
              e.stopPropagation();
              onPlayAyah(ayah.ayah_number);
            }}
            aria-label={isAyahPlaying ? `Zaustavi ajet ${ayah.ayah_number}` : `Preslušaj ajet ${ayah.ayah_number}`}
            aria-pressed={isAyahPlaying}
          >
            <Icon name={isAyahPlaying ? "pause" : "play"} size={18} />
          </button>
        </span>
      </div>

      <p className="ayah-arabic" dir="rtl" lang="ar">
        {ayah.words.map((w) => (
          <span key={w.word_id}>
            <ArabicWord word={w} isHighlighted={activeWordId === w.word_id} onWordClick={onWordClick} />{" "}
          </span>
        ))}
        <AyahEndMark number={ayah.ayah_number} />
      </p>

      <p className="ayah-translation" lang="bs">
        {ayah.bosnian_tokens.map((t) => (
          <span key={t.token_id}>
            <BosnianTokenSpan
              token={t}
              isHighlighted={activeTokenIds.has(t.token_id)}
              onTokenClick={onTokenClick}
            />{" "}
          </span>
        ))}
      </p>
    </article>
  );
});
