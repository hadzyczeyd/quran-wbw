/**
 * beforeinstallprompt stiže jednom, rano (često prije nego korisnik otvori
 * stranicu "Više"), pa se hvata globalno (ServiceWorkerRegister) i čuva ovdje.
 */
export interface BeforeInstallPromptEvent extends Event {
  prompt: () => Promise<void>;
  userChoice: Promise<{ outcome: "accepted" | "dismissed" }>;
}

let deferred: BeforeInstallPromptEvent | null = null;
const listeners = new Set<() => void>();

export function captureInstallPrompt() {
  window.addEventListener("beforeinstallprompt", (e) => {
    e.preventDefault();
    deferred = e as BeforeInstallPromptEvent;
    listeners.forEach((l) => l());
  });
  window.addEventListener("appinstalled", () => {
    deferred = null;
    listeners.forEach((l) => l());
  });
}

export function getInstallPrompt() {
  return deferred;
}

export function clearInstallPrompt() {
  deferred = null;
  listeners.forEach((l) => l());
}

export function subscribeInstallPrompt(cb: () => void) {
  listeners.add(cb);
  return () => listeners.delete(cb);
}
