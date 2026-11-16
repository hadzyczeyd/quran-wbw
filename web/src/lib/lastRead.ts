/** Zadnje mjesto čitanja (sura + ajet) — samo na ovom uređaju, u localStorage. */
export interface LastRead {
  surah: number;
  ayah: number;
}

const KEY = "rpr-last-read";
const EVENT = "rpr-last-read-change";
let cachedRaw: string | null | undefined;
let cachedValue: LastRead | null = null;

export function getLastRead(): LastRead | null {
  let raw: string | null = null;
  try {
    raw = localStorage.getItem(KEY);
  } catch {
    return null;
  }
  if (raw === cachedRaw) return cachedValue;
  cachedRaw = raw;
  try {
    const v = raw ? JSON.parse(raw) : null;
    cachedValue =
      v && Number.isInteger(v.surah) && Number.isInteger(v.ayah) ? { surah: v.surah, ayah: v.ayah } : null;
  } catch {
    cachedValue = null;
  }
  return cachedValue;
}

export function setLastRead(value: LastRead) {
  try {
    localStorage.setItem(KEY, JSON.stringify(value));
  } catch {
    return;
  }
  window.dispatchEvent(new Event(EVENT));
}

export function subscribeLastRead(cb: () => void) {
  window.addEventListener(EVENT, cb);
  window.addEventListener("storage", cb);
  return () => {
    window.removeEventListener(EVENT, cb);
    window.removeEventListener("storage", cb);
  };
}
