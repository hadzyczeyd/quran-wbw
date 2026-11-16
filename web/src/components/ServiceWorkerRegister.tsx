"use client";

import { useEffect } from "react";
import { captureInstallPrompt } from "@/lib/installPrompt";
import { syncThemeColor } from "@/lib/prefs";

/**
 * Registruje public/sw.js samo u produkciji (u razvoju bi keš smetao HMR-u),
 * hvata ponudu za instalaciju i usklađuje boju statusne trake s temom.
 */
export function ServiceWorkerRegister() {
  useEffect(() => {
    captureInstallPrompt();
    if (document.documentElement.hasAttribute("data-theme")) syncThemeColor();
    if (process.env.NODE_ENV !== "production" || !("serviceWorker" in navigator)) return;
    navigator.serviceWorker.register("/sw.js", { scope: "/", updateViaCache: "none" }).catch(() => {});
  }, []);
  return null;
}
