"use client";

import { useEffect, useRef, useState } from "react";
import type { RootPanelCard, RootPanelData } from "@/lib/rootPanel";

export interface RootSelection {
  ayahNumber: number;
  position: number;
}

interface RootPanelProps {
  panel: RootPanelData;
  selection: RootSelection | null;
  /** Zatvaranje ploče na mobitelu (gasi i isticanje riječi). */
  onClose: () => void;
}

/** Bosanska množina: 1 imenica, 2–4 imenice, 5+ imenica (11–14 uvijek treći oblik). */
function plural(n: number, one: string, few: string, many: string) {
  const d = n % 10;
  const dd = n % 100;
  if (d === 1 && dd !== 11) return one;
  if (d >= 2 && d <= 4 && (dd < 12 || dd > 14)) return few;
  return many;
}

function ArabicExample({ card }: { card: RootPanelCard }) {
  const chars = Array.from(card.ar);
  const [start, end] = card.hl;
  return (
    <p className="rp-ar" dir="rtl" lang="ar">
      {card.ell[0] && "… "}
      {chars.slice(0, start).join("")}
      <mark className="rp-target">{chars.slice(start, end).join("")}</mark>
      {chars.slice(end).join("")}
      {card.ell[1] && " …"}
    </p>
  );
}

function Card({ card }: { card: RootPanelCard }) {
  return (
    <li className="rp-card">
      <div className="rp-form">
        <span className="rp-form-ar" dir="rtl" lang="ar">
          {card.form}
        </span>
        <span className="rp-meaning">{card.meaning}</span>
      </div>
      <div className="rp-example">
        <span className="rp-ref" dir="ltr">
          {card.ref}
        </span>
        <ArabicExample card={card} />
        <p className="rp-bs" lang="bs" dir="ltr">
          {card.ell[2] && "…"}
          {card.bs}
          {card.ell[3] && "…"}
        </p>
      </div>
    </li>
  );
}

function Section({ title, cards }: { title: string; cards: RootPanelCard[] }) {
  return (
    <section className="rp-section">
      <h3 className="rp-section-title">{title}</h3>
      {cards.length === 0 ? (
        <p className="rp-empty">Nema potvrđenih primjera</p>
      ) : (
        <ul className="rp-cards">
          {cards.map((c) => (
            <Card key={c.id} card={c} />
          ))}
        </ul>
      )}
    </section>
  );
}

/**
 * Panel korijena. Klik na imenicu ili glagol u ajetu prikazuje njen QAC
 * korijen, različite imenice i glagolske oblike, svaki s jednim
 * provjerenim kur'anskim primjerom.
 *
 * Širi ekran: sticky desna kolona. Uski ekran: ploča koja izlazi odozdo
 * (prvo do pola ekrana da riječ ostane vidljiva iznad nje; povlačenje
 * nagore je širi, nadolje zatvara).
 */
export function RootPanel({ panel, selection, onClose }: RootPanelProps) {
  const rootBw = selection
    ? panel.words[`${selection.ayahNumber}:${selection.position}`]
    : undefined;
  const root = rootBw ? panel.roots[rootBw] : undefined;
  const [expanded, setExpanded] = useState(false);
  const dragStart = useRef<number | null>(null);
  const bodyRef = useRef<HTMLDivElement>(null);

  // Nova riječ: ploča se vraća na pola ekrana, sadržaj na vrh.
  const selKey = selection ? `${selection.ayahNumber}:${selection.position}` : "";
  const [prevKey, setPrevKey] = useState(selKey);
  if (prevKey !== selKey) {
    setPrevKey(selKey);
    setExpanded(false);
  }
  useEffect(() => {
    bodyRef.current?.scrollTo({ top: 0 });
  }, [selKey]);

  // Kartica koja bi samo ponovila kliknutu riječ u istom ajetu privremeno se izostavlja (nalog V7, 6).
  const here = selection ? `${panel.surah}:${selection.ayahNumber}` : "";
  const notHere = (c: RootPanelCard) =>
    !(selection && c.ref === here && c.w === selection.position);
  const nouns = root ? root.nouns.filter(notHere) : [];
  const verbs = root ? root.verbs.filter(notHere) : [];

  function onTouchStart(e: React.TouchEvent) {
    dragStart.current = e.touches[0].clientY;
  }

  function onTouchEnd(e: React.TouchEvent) {
    if (dragStart.current === null) return;
    const dy = e.changedTouches[0].clientY - dragStart.current;
    dragStart.current = null;
    if (dy < -40) setExpanded(true);
    else if (dy > 40) {
      if (expanded) setExpanded(false);
      else onClose();
    }
  }

  return (
    <aside
      className={`root-panel${root ? " has-root" : ""}${expanded ? " is-expanded" : ""}`}
      aria-label="Korijen riječi"
      onClick={(e) => e.stopPropagation()}
    >
      <div
        className="rp-sheet-top"
        onTouchStart={onTouchStart}
        onTouchEnd={onTouchEnd}
      >
        <button
          type="button"
          className="rp-handle"
          onClick={() => setExpanded((v) => !v)}
          aria-label={expanded ? "Smanji ploču" : "Proširi ploču"}
        />
        <button
          type="button"
          className="rp-close"
          onClick={onClose}
          aria-label="Zatvori"
        >
          ×
        </button>
      </div>

      <div className="rp-body" ref={bodyRef}>
        {!selection && (
          <p className="rp-hint">
            Kliknite na imenicu ili glagol u ajetu da vidite njen korijen i
            srodne riječi.
          </p>
        )}
        {selection && !root && (
          <p className="rp-hint">
            Korijen se prikazuje samo za imenice i glagole.
          </p>
        )}
        {root && (
          <>
            <h2
              className="rp-head"
              onTouchStart={onTouchStart}
              onTouchEnd={onTouchEnd}
            >
              <span dir="ltr">Korijen:</span>{" "}
              <bdi className="rp-root" dir="rtl" lang="ar">
                {root.display}
              </bdi>
              <span className="rp-counts" dir="ltr">
                {nouns.length}{" "}
                {plural(nouns.length, "imenica", "imenice", "imenica")} ·{" "}
                {verbs.length}{" "}
                {plural(verbs.length, "glagol", "glagola", "glagola")}
              </span>
            </h2>
            <Section title="Imenice" cards={nouns} />
            <Section title="Glagoli" cards={verbs} />
          </>
        )}
      </div>
    </aside>
  );
}
