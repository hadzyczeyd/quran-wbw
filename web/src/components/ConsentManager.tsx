"use client";

import Link from "next/link";
import { usePathname } from "next/navigation";
import { useEffect, useRef, useState, useSyncExternalStore } from "react";
import {
  OPEN_SETTINGS_EVENT,
  getConsent,
  getIds,
  isTrackingExcluded,
  setConsent,
  subscribeConsent,
} from "@/lib/consent";

const LOCAL_HOST_RE = /^(localhost|127\.0\.0\.1|\[::1\]|.+\.localhost)$/;

/**
 * Traka za pristanak na statistiku + slanje pregleda stranica.
 * Ništa se ne šalje i ne pohranjuje (osim samog izbora) prije pristanka.
 * Ne broje se: lokalni razvoj, automatizovani preglednici i uređaji na
 * kojima se admin prijavio (vidi AdminGuard).
 */
export function ConsentManager() {
  const pathname = usePathname();
  // "ssr" dok se ne pročita localStorage u pregledniku (bez hydration razlike).
  const stored = useSyncExternalStore(subscribeConsent, () => getConsent() ?? "none", () => "ssr");
  const consent = stored === "granted" || stored === "denied" ? stored : null;
  const [settingsOpen, setSettingsOpen] = useState(false);
  const lastSent = useRef<string | null>(null);

  useEffect(() => {
    const onOpen = () => setSettingsOpen(true);
    window.addEventListener(OPEN_SETTINGS_EVENT, onOpen);
    return () => window.removeEventListener(OPEN_SETTINGS_EVENT, onOpen);
  }, []);

  useEffect(() => {
    if (consent !== "granted" || !pathname) return;
    if (pathname.startsWith("/admin") || pathname.startsWith("/login")) return;
    if (isTrackingExcluded() || navigator.webdriver) return;
    if (LOCAL_HOST_RE.test(location.hostname)) return;
    if (lastSent.current === pathname) return;
    lastSent.current = pathname;

    const [visitorId, sessionId, firstInSession] = getIds();
    const utmSource = new URLSearchParams(location.search).get("utm_source");
    fetch("/api/track", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      keepalive: true,
      body: JSON.stringify({
        visitorId,
        sessionId,
        firstInSession,
        path: pathname,
        referrer: firstInSession ? document.referrer : "",
        utmSource,
      }),
    }).catch(() => {});
  }, [consent, pathname]);

  function choose(value: "granted" | "denied") {
    setConsent(value);
    setSettingsOpen(false);
  }

  if (stored === "ssr" || (stored !== "none" && !settingsOpen)) return null;

  return (
    <div className="consent-banner" role="dialog" aria-live="polite" aria-label="Postavke kolačića">
      <p>
        Uz vaš pristanak bilježimo anonimnu statistiku posjeta (koje stranice se otvaraju, iz koje države
        i s kojeg uređaja ili aplikacije), da bismo znali kako se stranica koristi. Ne koristimo oglase niti
        dijelimo podatke s trećim stranama. Više u{" "}
        <Link href="/privatnost">politici privatnosti</Link>.
      </p>
      <div className="consent-actions">
        <button type="button" className="consent-btn" onClick={() => choose("denied")}>
          Odbijam
        </button>
        <button type="button" className="consent-btn" onClick={() => choose("granted")}>
          Prihvatam
        </button>
      </div>
      {consent !== null && (
        <p className="consent-current">
          Trenutni izbor: {consent === "granted" ? "statistika dozvoljena" : "statistika odbijena"}.
        </p>
      )}
    </div>
  );
}

export function ConsentSettingsLink() {
  return (
    <button
      type="button"
      className="site-footer-link"
      onClick={() => window.dispatchEvent(new Event(OPEN_SETTINGS_EVENT))}
    >
      Postavke kolačića
    </button>
  );
}
