"use client";

import { mergeSegmentsForDisplay } from "@/lib/segments";
import type { QacWord } from "@/lib/types";

interface ArabicWordProps {
  word: QacWord;
  isHighlighted: boolean;
  onWordClick: (word: QacWord) => void;
}

/**
 * Arapska riječ je JEDAN HTML element (OPIS zamka 5.5). Segmenti su
 * samo obojeni rasponi unutar nje, bez razmaka i bez reza, da se
 * slova normalno spajaju u fontu.
 */
export function ArabicWord({ word, isHighlighted, onWordClick }: ArabicWordProps) {
  const displaySegments = mergeSegmentsForDisplay(word.segments);

  return (
    <span
      className={`arabic-word${isHighlighted ? " is-highlighted-word" : ""}`}
      onClick={(e) => {
        e.stopPropagation();
        onWordClick(word);
      }}
      role="button"
      tabIndex={0}
      title={word.gloss ?? undefined}
      onKeyDown={(e) => {
        if (e.key === "Enter" || e.key === " ") onWordClick(word);
      }}
    >
      {displaySegments.map((seg) => (
        <span key={seg.key} data-qac-class={seg.cssClass}>
          {seg.text}
        </span>
      ))}
    </span>
  );
}
