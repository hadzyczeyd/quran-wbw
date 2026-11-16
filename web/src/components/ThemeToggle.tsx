"use client";

import { useSyncExternalStore } from "react";
import { getServerPrefs, readPrefs, setPref, subscribePrefs, type Theme } from "@/lib/prefs";
import { Icon } from "./Icon";

function useEffectiveDark(theme: Theme) {
  const systemDark = useSyncExternalStore(
    (cb) => {
      const mq = window.matchMedia("(prefers-color-scheme: dark)");
      mq.addEventListener("change", cb);
      return () => mq.removeEventListener("change", cb);
    },
    () => window.matchMedia("(prefers-color-scheme: dark)").matches,
    () => false,
  );
  return theme === "dark" || (theme === "system" && systemDark);
}

/** Brzi prekidač svijetla/tamna tema u zaglavlju (detaljniji izbor, uklj. "sistem", je u postavkama). */
export function ThemeToggle() {
  const prefs = useSyncExternalStore(subscribePrefs, readPrefs, getServerPrefs);
  const dark = useEffectiveDark(prefs.theme);
  return (
    <button
      type="button"
      className="icon-btn"
      aria-label={dark ? "Uključi svijetlu temu" : "Uključi tamnu temu"}
      onClick={() => setPref("theme", dark ? "light" : "dark")}
    >
      <Icon name={dark ? "sun" : "moon"} />
    </button>
  );
}

const THEMES: { value: Theme; label: string }[] = [
  { value: "system", label: "Kao uređaj" },
  { value: "light", label: "Svijetla" },
  { value: "dark", label: "Tamna" },
];

/** Segmentni izbor teme (postavke čitača, stranica Više). */
export function ThemePicker() {
  const prefs = useSyncExternalStore(subscribePrefs, readPrefs, getServerPrefs);
  return (
    <div className="segmented" role="radiogroup" aria-label="Tema">
      {THEMES.map((t) => (
        <button
          key={t.value}
          type="button"
          role="radio"
          aria-checked={prefs.theme === t.value}
          onClick={() => setPref("theme", t.value)}
        >
          {t.label}
        </button>
      ))}
    </div>
  );
}
