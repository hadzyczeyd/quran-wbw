"use client";

import type { BosnianToken } from "@/lib/types";

interface BosnianTokenSpanProps {
  token: BosnianToken;
  isHighlighted: boolean;
  onTokenClick: (token: BosnianToken) => void;
}

export function BosnianTokenSpan({ token, isHighlighted, onTokenClick }: BosnianTokenSpanProps) {
  const clickable = token.linked_segment_ids.length > 0;

  return (
    <span
      className={`bosnian-token${isHighlighted ? " is-highlighted" : ""}`}
      data-qac-class={token.css_class}
      onClick={clickable ? () => onTokenClick(token) : undefined}
      role={clickable ? "button" : undefined}
      tabIndex={clickable ? 0 : undefined}
      onKeyDown={
        clickable
          ? (e) => {
              if (e.key === "Enter" || e.key === " ") onTokenClick(token);
            }
          : undefined
      }
    >
      {token.text}
    </span>
  );
}
