/**
 * Pristanak na statistiku i isključivanje vlastitih posjeta (klijent).
 * Sve je u localStorage-u ovog preglednika; ništa se ne šalje dok posjetilac
 * izričito ne pristane.
 */

export const CONSENT_KEY = "kr_consent"; // "granted" | "denied"
export const NO_TRACK_KEY = "kr_no_track"; // "1" = ne broji ovaj uređaj (admin), "0" = broji
export const VISITOR_KEY = "kr_vid";
export const SESSION_KEY = "kr_sid";
export const OPEN_SETTINGS_EVENT = "kr-open-consent";
const CHANGE_EVENT = "kr-consent-change";

/** Za useSyncExternalStore: obavijest o promjeni izbora (i iz drugih kartica). */
export function subscribeConsent(callback: () => void) {
  window.addEventListener(CHANGE_EVENT, callback);
  window.addEventListener("storage", callback);
  return () => {
    window.removeEventListener(CHANGE_EVENT, callback);
    window.removeEventListener("storage", callback);
  };
}

function notify() {
  window.dispatchEvent(new Event(CHANGE_EVENT));
}

export type Consent = "granted" | "denied" | null;

function read(key: string, storage: "local" | "session" = "local"): string | null {
  try {
    return (storage === "local" ? localStorage : sessionStorage).getItem(key);
  } catch {
    return null;
  }
}

function write(key: string, value: string | null, storage: "local" | "session" = "local") {
  try {
    const s = storage === "local" ? localStorage : sessionStorage;
    if (value === null) s.removeItem(key);
    else s.setItem(key, value);
  } catch {
    /* privatni način / blokirana pohrana */
  }
}

export function getConsent(): Consent {
  const v = read(CONSENT_KEY);
  return v === "granted" || v === "denied" ? v : null;
}

export function setConsent(value: "granted" | "denied") {
  write(CONSENT_KEY, value);
  if (value === "denied") {
    write(VISITOR_KEY, null);
    write(SESSION_KEY, null, "session");
  }
  notify();
}

export function isTrackingExcluded(): boolean {
  return read(NO_TRACK_KEY) === "1";
}

export function setTrackingExcluded(excluded: boolean) {
  write(NO_TRACK_KEY, excluded ? "1" : "0");
  notify();
}

/** Pri prvoj admin prijavi na uređaju isključi ga iz statistike (izbor "0" se poštuje). */
export function excludeAdminDeviceByDefault() {
  if (read(NO_TRACK_KEY) === null) write(NO_TRACK_KEY, "1");
}

/** Vraća [visitorId, sessionId, prvi pregled u sesiji?]. */
export function getIds(): [string, string, boolean] {
  let vid = read(VISITOR_KEY);
  if (!vid) {
    vid = crypto.randomUUID();
    write(VISITOR_KEY, vid);
  }
  let sid = read(SESSION_KEY, "session");
  const first = !sid;
  if (!sid) {
    sid = crypto.randomUUID();
    write(SESSION_KEY, sid, "session");
  }
  return [vid, sid, first];
}

export function openConsentSettings() {
  window.dispatchEvent(new Event(OPEN_SETTINGS_EVENT));
}
