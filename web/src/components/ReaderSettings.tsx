"use client";

import { useSyncExternalStore } from "react";
import { getServerPrefs, readPrefs, setPref, subscribePrefs, type Size } from "@/lib/prefs";
import { Icon } from "./Icon";
import { ThemePicker } from "./ThemeToggle";

const SIZES: { value: Size; label: string; aria: string }[] = [
  { value: "s", label: "A", aria: "Mala" },
  { value: "m", label: "A", aria: "Srednja" },
  { value: "l", label: "A", aria: "Velika" },
  { value: "xl", label: "A", aria: "Najveća" },
];

function SizePicker({ label, value, onChange }: { label: string; value: Size; onChange: (s: Size) => void }) {
  return (
    <div className="segmented size-picker" role="radiogroup" aria-label={label}>
      {SIZES.map((s, i) => (
        <button
          key={s.value}
          type="button"
          role="radio"
          aria-checked={value === s.value}
          aria-label={s.aria}
          onClick={() => onChange(s.value)}
          style={{ fontSize: `${0.8 + i * 0.15}rem` }}
        >
          {s.label}
        </button>
      ))}
    </div>
  );
}

export const SETTINGS_POPOVER_ID = "postavke-citaca";

/** Postavke čitača kao ploča (popover): tema, veličina teksta, prijevod, boje. */
export function ReaderSettings() {
  const prefs = useSyncExternalStore(subscribePrefs, readPrefs, getServerPrefs);
  return (
    <div id={SETTINGS_POPOVER_ID} popover="auto" className="sheet" aria-labelledby="postavke-naslov">
      <div className="sheet-head">
        <h2 id="postavke-naslov">Prikaz</h2>
        <button
          type="button"
          className="icon-btn"
          popoverTarget={SETTINGS_POPOVER_ID}
          popoverTargetAction="hide"
          aria-label="Zatvori"
        >
          <Icon name="close" />
        </button>
      </div>
      <div className="sheet-body">
        <span className="field-label">Tema</span>
        <ThemePicker />

        <span className="field-label">Veličina arapskog teksta</span>
        <SizePicker label="Veličina arapskog teksta" value={prefs.arSize} onChange={(v) => setPref("arSize", v)} />

        <span className="field-label">Veličina prijevoda</span>
        <SizePicker label="Veličina prijevoda" value={prefs.trSize} onChange={(v) => setPref("trSize", v)} />

        <div className="settings-switches">
          <label className="switch">
            <span>Prikaži bosanski prijevod</span>
            <input
              type="checkbox"
              role="switch"
              checked={prefs.translation === "on"}
              onChange={(e) => setPref("translation", e.target.checked ? "on" : "off")}
            />
          </label>
          <label className="switch mobile-only">
            <span>
              Korijen riječi pri dodiru
              <span className="switch-hint">Traka na dnu ekrana s korijenom i srodnim riječima</span>
            </span>
            <input
              type="checkbox"
              role="switch"
              checked={prefs.roots === "on"}
              onChange={(e) => setPref("roots", e.target.checked ? "on" : "off")}
            />
          </label>
          <label className="switch">
            <span>Boje gramatike</span>
            <input
              type="checkbox"
              role="switch"
              checked={prefs.colors === "on"}
              onChange={(e) => setPref("colors", e.target.checked ? "on" : "off")}
            />
          </label>
        </div>
      </div>
    </div>
  );
}
