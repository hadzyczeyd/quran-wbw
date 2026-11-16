"use client";

import { useState, useSyncExternalStore } from "react";
import { clearInstallPrompt, getInstallPrompt, subscribeInstallPrompt } from "@/lib/installPrompt";
import { Icon } from "./Icon";

const subscribeNoop = () => () => {};

/**
 * Instalacija aplikacije na početni ekran. Chrome/Edge/Android nude
 * beforeinstallprompt (dugme); iOS Safari nema API, pa se pokaže uputstvo.
 */
export function InstallApp() {
  const promptEvent = useSyncExternalStore(subscribeInstallPrompt, getInstallPrompt, () => null);
  const [installed, setInstalled] = useState(false);
  const standalone = useSyncExternalStore(
    subscribeNoop,
    () => window.matchMedia("(display-mode: standalone)").matches,
    () => false,
  );
  const isIOS = useSyncExternalStore(subscribeNoop, () => /iPad|iPhone|iPod/.test(navigator.userAgent), () => false);

  if (standalone || installed) {
    return <p className="install-status">Aplikacija je instalirana na ovom uređaju.</p>;
  }

  if (promptEvent) {
    return (
      <button
        type="button"
        className="btn btn-primary"
        onClick={async () => {
          await promptEvent.prompt();
          const { outcome } = await promptEvent.userChoice;
          if (outcome === "accepted") setInstalled(true);
          clearInstallPrompt();
        }}
      >
        <Icon name="download" size={18} />
        Instaliraj aplikaciju
      </button>
    );
  }

  if (isIOS) {
    return (
      <p className="install-status">
        Na iPhoneu: u Safariju dodirnite <strong>Dijeli</strong>, zatim <strong>Dodaj na početni ekran</strong>.
      </p>
    );
  }

  return (
    <p className="install-status">
      U meniju preglednika izaberite <strong>Instaliraj aplikaciju</strong> ili{" "}
      <strong>Dodaj na početni ekran</strong>.
    </p>
  );
}
