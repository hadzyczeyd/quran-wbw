"use client";

import type { ClientToken } from "@/lib/types";

interface BosnianTokenSpanProps {
  token: ClientToken;
  isHighlighted: boolean;
  onTokenClick: (token: ClientToken) => void;
}

export function BosnianTokenSpan({ token, isHighlighted, onTokenClick }: BosnianTokenSpanProps) {
  const clickable = token.word !== null;
  const fused = token.fused.length > 0;

  return (
    <span
      className={`bosnian-token${fused ? " is-fused" : ""}${isHighlighted ? " is-highlighted" : ""}`}
      data-qac-class={token.c}
      onClick={
        clickable
          ? (e) => {
              e.stopPropagation();
              onTokenClick(token);
            }
          : undefined
      }
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
      {token.t}
      {fused && (
        <span className="fused-markers" aria-hidden="true">
          {token.fused.map((m, i) => (
            <span key={i} className="fused-marker" data-qac-class={m.c} title={m.tag} />
          ))}
        </span>
      )}
    </span>
  );
}
