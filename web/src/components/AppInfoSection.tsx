"use client";

import { useRef, useState } from "react";
import Link from "next/link";
import { APP_INFO_SECTIONS } from "@/lib/appInfoContent";

// Autorska prava ostaje samo na /o-aplikaciji — ne zauzima mjesto u
// kompaktnim karticama na početnoj.
const HOME_CARDS = APP_INFO_SECTIONS.filter((s) => s.title !== "Autorska prava");

export function AppInfoSection() {
  const dialogRef = useRef<HTMLDialogElement>(null);
  const [activeIndex, setActiveIndex] = useState<number | null>(null);

  function openCard(i: number) {
    setActiveIndex(i);
    dialogRef.current?.showModal();
  }

  const active = activeIndex !== null ? HOME_CARDS[activeIndex] : null;

  return (
    <section className="app-info">
      <div className="app-info-track">
        {HOME_CARDS.map((card, i) => (
          <button
            type="button"
            className="app-info-card"
            key={card.title}
            onClick={() => openCard(i)}
          >
            {card.title}
            <span className="app-info-card-chevron" aria-hidden="true">
              ›
            </span>
          </button>
        ))}
      </div>
      <p className="app-info-full-link">
        <Link href="/o-aplikaciji">Pročitaj sve na jednoj stranici →</Link>
      </p>

      <dialog
        ref={dialogRef}
        className="app-info-dialog"
        onClick={(e) => {
          if (e.target === dialogRef.current) dialogRef.current?.close();
        }}
      >
        {active && (
          <>
            <button
              type="button"
              className="app-info-dialog-close"
              onClick={() => dialogRef.current?.close()}
              aria-label="Zatvori"
            >
              ×
            </button>
            <h2>{active.title}</h2>
            {active.body}
          </>
        )}
      </dialog>
    </section>
  );
}
