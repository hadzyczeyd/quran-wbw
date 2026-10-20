"use client";

import { useLayoutEffect, useRef, useState } from "react";
import type { RootFamily } from "@/lib/rootFamilies";

// Boje oznaka grupa prate legendu (QAC): imenica sky, glagol seagreen, pridjev purple.
const GROUPS: { key: "imenice" | "glagoli" | "pridjevi"; label: string; qacClass: string }[] = [
  { key: "imenice", label: "Imenice", qacClass: "segSky" },
  { key: "glagoli", label: "Glagoli", qacClass: "segSeagreen" },
  { key: "pridjevi", label: "Pridjevi", qacClass: "segPurple" },
];

/** Oblačić iznad arapske riječi: korijen i riječi istog korijena. */
export function RootTooltip({ family }: { family: RootFamily }) {
  const ref = useRef<HTMLSpanElement>(null);
  const [pos, setPos] = useState({ shift: 0, below: false });

  // Ne smije izaći preko ruba ekrana niti ispod sticky zaglavlja (mobilni):
  // pomjeri ga vodoravno, a ako nema mjesta iznad riječi, prikaži ga ispod.
  useLayoutEffect(() => {
    const el = ref.current;
    if (!el) return;
    const r = el.getBoundingClientRect();
    const margin = 8;
    const header = document.querySelector(".site-header")?.getBoundingClientRect().bottom ?? 0;
    const vw = document.documentElement.clientWidth;
    let shift = 0;
    if (r.left < margin) shift = margin - r.left;
    else if (r.right > vw - margin) shift = vw - margin - r.right;
    setPos({ shift, below: r.top < header + margin });
  }, []);

  const groups = GROUPS.filter((g) => family[g.key].length > 0);

  return (
    <span
      ref={ref}
      className={`root-tooltip${pos.below ? " is-below" : ""}`}
      role="tooltip"
      dir="ltr"
      style={{ transform: `translateX(calc(-50% + ${pos.shift}px))`, ["--arrow-shift" as string]: `${-pos.shift}px` }}
      onClick={(e) => e.stopPropagation()}
    >
      <span className="rt-head">
        <span className="rt-label">Korijen</span>
        <span className="rt-root" dir="rtl" lang="ar">
          {[...family.root].map((ch, i) => (
            <span key={i} className="rt-letter">
              {ch}
            </span>
          ))}
        </span>
      </span>
      {groups.length > 0 && (
        <span className="rt-body">
          {groups.map((g) => (
            <span key={g.key} className="rt-row">
              <span className="rt-tag" data-qac-class={g.qacClass}>
                {g.label}
              </span>
              <span className="rt-chips" dir="rtl" lang="ar">
                {family[g.key].map((w) => (
                  <span key={w} className="rt-chip">
                    {w}
                  </span>
                ))}
              </span>
            </span>
          ))}
        </span>
      )}
    </span>
  );
}
