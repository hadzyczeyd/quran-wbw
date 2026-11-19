"use client";

import type { ClientWord } from "@/lib/types";

interface ArabicWordProps {
  word: ClientWord;
  isHighlighted: boolean;
  onWordClick: (word: ClientWord) => void;
}

/**
 * Arapska riječ je JEDAN HTML element (OPIS zamka 5.5). Segmenti su
 * samo obojeni rasponi unutar nje, bez razmaka i bez reza, da se
 * slova normalno spajaju u fontu. Spajanje za prikaz (لله ligatura)
 * radi server (lib/clientSurah.ts).
 */
export function ArabicWord({ word, isHighlighted, onWordClick }: ArabicWordProps) {
  return (
    <span
      className={`arabic-word${isHighlighted ? " is-highlighted-word" : ""}`}
      data-word-id={word.id}
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
      {word.parts.map((p, i) => (
        <span key={i} data-qac-class={p.c}>
          {p.t}
        </span>
      ))}
    </span>
  );
}
