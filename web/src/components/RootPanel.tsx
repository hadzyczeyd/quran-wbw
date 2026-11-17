"use client";

import { useEffect, useRef, useState } from "react";
import type { RootPanelCard, RootPanelIndex, RootPanelRoot } from "@/lib/rootPanel";
import { loadRootPanelRoots } from "@/lib/rootPanelClient";
import { Icon } from "./Icon";

export interface RootSelection {
  ayahNumber: number;
  position: number;
}

interface RootPanelProps {
  /** null = sura nema podatke o korijenima; panel tada samo objašnjava čitanje i boje. */
  panel: RootPanelIndex | null;
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
  const rootBw =
    selection && panel ? panel.words[`${selection.ayahNumber}:${selection.position}`] : undefined;
  // Kartice se učitavaju tek pri prvom kliku na imenicu ili glagol.
  const [roots, setRoots] = useState<Record<string, RootPanelRoot> | null>(null);
  const [loadFailed, setLoadFailed] = useState(false);
  const needRoots = rootBw !== undefined && roots === null;
  const surah = panel?.surah ?? 0;
  useEffect(() => {
    if (!needRoots || !surah) return;
    let alive = true;
    loadRootPanelRoots(surah).then(
      (r) => alive && setRoots(r),
      () => alive && setLoadFailed(true),
    );
    return () => {
      alive = false;
    };
  }, [needRoots, surah, selection?.ayahNumber, selection?.position]);
  const root = rootBw && roots ? roots[rootBw] : undefined;
  const [expanded, setExpanded] = useState(false);
  const dragStart = useRef<number | null>(null);
  const bodyRef = useRef<HTMLDivElement>(null);

  // Nova riječ: ploča se vraća na kompaktnu traku, sadržaj na vrh.
  const selKey = selection
    ? `${selection.ayahNumber}:${selection.position}`
    : "";
  const [prevKey, setPrevKey] = useState(selKey);
  if (prevKey !== selKey) {
    setPrevKey(selKey);
    setExpanded(false);
    setLoadFailed(false);
  }
  useEffect(() => {
    bodyRef.current?.scrollTo({ top: 0 });
  }, [selKey]);

  // Kartica koja bi samo ponovila kliknutu riječ u istom ajetu privremeno se izostavlja (nalog V7, 6).
  const here = selection ? `${surah}:${selection.ayahNumber}` : "";
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
      className={`root-panel${rootBw ? " has-root" : ""}${expanded ? " is-expanded" : ""}`}
      aria-label="Korijen riječi"
      onClick={(e) => e.stopPropagation()}
    >
      {/* Mobitel: kompaktna traka (korijen + broj riječi); dodir ili povlačenje nagore otvara kartice. */}
      <div className="rp-peek" onTouchStart={onTouchStart} onTouchEnd={onTouchEnd}>
        <button
          type="button"
          className="rp-peek-main"
          onClick={() => setExpanded((v) => !v)}
          aria-expanded={expanded}
          aria-controls="rp-kartice"
        >
          <span className="rp-peek-label">Korijen</span>
          <bdi className="rp-peek-root" dir="rtl" lang="ar">
            {root?.display ?? "…"}
          </bdi>
          <span className="rp-peek-counts">
            {root ? (
              <>
                <span>
                  {nouns.length}&nbsp;{plural(nouns.length, "imenica", "imenice", "imenica")},
                </span>{" "}
                <span>
                  {verbs.length}&nbsp;{plural(verbs.length, "glagol", "glagola", "glagola")}
                </span>
              </>
            ) : loadFailed
                ? "Nije učitano"
                : "Učitavanje…"}
          </span>
          <Icon name={expanded ? "chevronDown" : "chevronUp"} size={18} />
        </button>
        <button type="button" className="icon-btn" onClick={onClose} aria-label="Zatvori korijen">
          <Icon name="close" size={18} />
        </button>
      </div>

      <div className="rp-body" ref={bodyRef} id="rp-kartice">
        {!selection && (
          <div className="rp-intro">
            <h2 className="rp-intro-title">Korijen riječi</h2>
            <p className="rp-hint">
              {panel
                ? "Dodirnite imenicu ili glagol u ajetu da ovdje vidite njen korijen i srodne riječi iz Kur’ana, svaku s primjerom."
                : "Za ovu suru korijeni još nisu pripremljeni. Dodirom na riječ čujete izgovor i vidite njen bosanski par."}
            </p>
          </div>
        )}
        {rootBw && !roots && (
          <p className="rp-hint" role="status">
            {loadFailed
              ? "Korijen se nije mogao učitati. Provjerite vezu i kliknite riječ ponovo."
              : "Učitavanje korijena…"}
          </p>
        )}
        {selection && !rootBw && (
          <p className="rp-hint">
            Korijen se prikazuje samo za imenice i glagole.
          </p>
        )}
        {root && (
          <>
            <h2 className="rp-head">
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
            {nouns.length + verbs.length === 0 ? (
              // Jedini primjer korijena je upravo kliknuta riječ (izostavljena po nalogu V7, 6).
              <p className="rp-hint">
                Imenice i glagoli ovog korijena javljaju se u Kur&apos;anu samo na
                ovom mjestu.
              </p>
            ) : (
              <>
                <Section title="Imenice" cards={nouns} />
                <Section title="Glagoli" cards={verbs} />
              </>
            )}
          </>
        )}
      </div>
    </aside>
  );
}
