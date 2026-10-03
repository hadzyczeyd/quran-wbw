"use client";

import type { BosnianToken } from "@/lib/types";

interface BosnianTokenSpanProps {
  token: BosnianToken;
  isHighlighted: boolean;
  onTokenClick: (token: BosnianToken) => void;
}

export function BosnianTokenSpan({ token, isHighlighted, onTokenClick }: BosnianTokenSpanProps) {
  const clickable = token.linked_segment_ids.length > 0;
  const fused = token.fused_markers.length > 0;

  return (
    <span
      className={`bosnian-token${fused ? " is-fused" : ""}${isHighlighted ? " is-highlighted" : ""}`}
      data-qac-class={token.css_class}
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
      {token.text}
      {fused && (
        <span className="fused-markers" aria-hidden="true">
          {token.fused_markers.map((m) => (
            <span key={m.segment_id} className="fused-marker" data-qac-class={m.css_class} title={m.tag} />
          ))}
        </span>
      )}
    </span>
  );
}
