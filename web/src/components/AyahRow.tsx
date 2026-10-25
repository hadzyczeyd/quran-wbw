"use client";

import { normRoot, type RootFamilies } from "@/lib/rootFamilies";
import type { Ayah, BosnianToken, QacWord } from "@/lib/types";
import { ArabicWord } from "./ArabicWord";
import { AyahEndMark } from "./AyahEndMark";
import { BosnianTokenSpan } from "./BosnianTokenSpan";
import { PlayIcon } from "./PlayIcon";

interface AyahRowProps {
  ayah: Ayah;
  activeWordId: string | null;
  activeTokenIds: Set<string>;
  onWordClick: (word: QacWord) => void;
  onTokenClick: (token: BosnianToken) => void;
  onPlayAyah: (ayahNumber: number) => void;
  isAyahPlaying: boolean;
  rootFamilies?: RootFamilies | null;
  /** Broj džuza koji počinje ovim ajetom. */
  juzStart?: number;
}

function familyOf(word: QacWord, families: RootFamilies | null | undefined) {
  if (!families) return null;
  for (const s of word.segments) {
    if (s.root && s.root !== "QAC_NO_DATA") {
      const f = families[normRoot(s.root)];
      if (f) return f;
    }
  }
  return null;
}

export function AyahRow({
  ayah,
  activeWordId,
  activeTokenIds,
  onWordClick,
  onTokenClick,
  onPlayAyah,
  isAyahPlaying,
  rootFamilies,
  juzStart,
}: AyahRowProps) {
  return (
    <div className="ayah-row" id={`ajet-${ayah.ayah_number}`}>
      <div className="ayah-gutter">
        <span className="ayah-number">{ayah.ayah_number}</span>
        {juzStart && <span className="ayah-juz-badge">Džuz {juzStart}</span>}
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
          <PlayIcon playing={isAyahPlaying} />
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
              rootFamily={familyOf(w, rootFamilies)}
            />{" "}
          </span>
        ))}
        <AyahEndMark number={ayah.ayah_number} />
      </div>
    </div>
  );
}
