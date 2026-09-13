"use client";

import type { Ayah, BosnianToken, QacWord } from "@/lib/types";
import { ArabicWord } from "./ArabicWord";
import { AyahEndMark } from "./AyahEndMark";
import { BosnianTokenSpan } from "./BosnianTokenSpan";

interface AyahRowProps {
  ayah: Ayah;
  activeWordId: string | null;
  activeTokenIds: Set<string>;
  onWordClick: (word: QacWord) => void;
  onTokenClick: (token: BosnianToken) => void;
  onPlayAyah: (ayahNumber: number) => void;
  isAyahPlaying: boolean;
}

export function AyahRow({
  ayah,
  activeWordId,
  activeTokenIds,
  onWordClick,
  onTokenClick,
  onPlayAyah,
  isAyahPlaying,
}: AyahRowProps) {
  return (
    <div className="ayah-row">
      <div className="ayah-gutter">
        <span className="ayah-number">{ayah.ayah_number}</span>
        <button
          type="button"
          className="ayah-play-button"
          onClick={(e) => {
            e.stopPropagation();
            onPlayAyah(ayah.ayah_number);
          }}
          aria-label={`Preslušaj ajet ${ayah.ayah_number}`}
          aria-pressed={isAyahPlaying}
        >
          {isAyahPlaying ? "⏸" : "▶"}
        </button>
      </div>

      <div className="ayah-translation">
        {ayah.bosnian_tokens.map((t) => (
          <span key={t.token_id}>
            <BosnianTokenSpan
              token={t}
              isHighlighted={activeTokenIds.has(t.token_id)}
              onTokenClick={onTokenClick}
            />{" "}
          </span>
        ))}
      </div>

      <div className="ayah-arabic" dir="rtl" lang="ar">
        {ayah.words.map((w) => (
          <span key={w.word_id}>
            <ArabicWord
              word={w}
              isHighlighted={activeWordId === w.word_id}
              onWordClick={onWordClick}
            />{" "}
          </span>
        ))}
        <AyahEndMark number={ayah.ayah_number} />
      </div>
    </div>
  );
}
