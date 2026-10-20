"use client";

import { useLayoutEffect, useRef, useState } from "react";
import type { RootFamily } from "@/lib/rootFamilies";

const GROUPS: { key: "imenice" | "glagoli" | "pridjevi"; label: string }[] = [
  { key: "imenice", label: "Imenice" },
  { key: "glagoli", label: "Glagoli" },
  { key: "pridjevi", label: "Pridjevi" },
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

  return (
    <span
      ref={ref}
      className={`root-tooltip${pos.below ? " is-below" : ""}`}
      role="tooltip"
      style={{ transform: `translateX(calc(-50% + ${pos.shift}px))`, ["--arrow-shift" as string]: `${-pos.shift}px` }}
      onClick={(e) => e.stopPropagation()}
    >
      <span className="root-tooltip-label">Korijen</span>
      <span className="root-tooltip-root" dir="rtl" lang="ar">
        {[...family.root].join(" ")}
      </span>
      {GROUPS.filter((g) => family[g.key].length > 0).map((g) => (
        <span key={g.key} className="root-tooltip-group">
          <span className="root-tooltip-group-label">{g.label}</span>
          <span className="root-tooltip-words" dir="rtl" lang="ar">
            {family[g.key].join("  ·  ")}
          </span>
        </span>
      ))}
    </span>
  );
}
