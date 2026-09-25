"use client";

import { useEffect, useRef, useState } from "react";

const SITE_NAME = "Kur'an riječ po riječ";

function getShareData() {
  const url = typeof window !== "undefined" ? window.location.href : "";
  const title = typeof document !== "undefined" ? document.title : SITE_NAME;
  return { url, title };
}

type ShareTarget = "email" | "viber" | "whatsapp" | "messenger" | "facebook";

function shareUrlFor(target: ShareTarget, url: string, title: string): string {
  const encodedUrl = encodeURIComponent(url);
  const encodedText = encodeURIComponent(`${title} — ${url}`);

  switch (target) {
    case "email":
      return `mailto:?subject=${encodeURIComponent(title)}&body=${encodedText}`;
    case "viber":
      return `viber://forward?text=${encodedText}`;
    case "whatsapp":
      return `https://wa.me/?text=${encodedText}`;
    case "messenger":
      return `fb-messenger://share/?link=${encodedUrl}`;
    case "facebook":
      return `https://www.facebook.com/sharer/sharer.php?u=${encodedUrl}`;
  }
}

/** Dijeljenje trenutne stranice — dropdown sa nekoliko servisa i kopiranjem linka. */
export function ShareMenu() {
  const [open, setOpen] = useState(false);
  const [copied, setCopied] = useState(false);
  const wrapperRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    if (!open) return;

    function onDocumentClick(e: MouseEvent) {
      if (wrapperRef.current && !wrapperRef.current.contains(e.target as Node)) {
        setOpen(false);
      }
    }

    document.addEventListener("click", onDocumentClick);
    return () => document.removeEventListener("click", onDocumentClick);
  }, [open]);

  function openShareLink(target: ShareTarget) {
    const { url, title } = getShareData();
    window.open(shareUrlFor(target, url, title), "_blank", "noopener,noreferrer");
    setOpen(false);
  }

  async function handleCopy() {
    const { url } = getShareData();
    try {
      await navigator.clipboard.writeText(url);
      setCopied(true);
      setTimeout(() => setCopied(false), 2000);
    } catch {
      // Clipboard API nedostupna (npr. stariji browser) — nema fallbacka,
      // ostale opcije dijeljenja i dalje rade.
    }
  }

  // Instagram nema URL za dijeljenje linka (za razliku od ostalih), pa se
  // link kopira u clipboard i otvara se Instagram poruke — korisnik ga samo
  // zalijepi. window.open ide prvi, sinhrono, da ga popup blocker ne odsiječe.
  function handleInstagram() {
    const { url } = getShareData();
    window.open("https://www.instagram.com/direct/inbox/", "_blank", "noopener,noreferrer");
    navigator.clipboard?.writeText(url).catch(() => {});
    setOpen(false);
  }

  return (
    <div className="share-wrapper" ref={wrapperRef}>
      <button
        type="button"
        className="share-toggle"
        aria-label="Podijeli"
        aria-expanded={open}
        onClick={() => {
          setCopied(false);
          setOpen((v) => !v);
        }}
      >
        <svg viewBox="0 0 24 24" width="18" height="18" aria-hidden="true">
          <path d="M12 15.5V4" fill="none" stroke="currentColor" strokeWidth="1.8" strokeLinecap="round" />
          <path
            d="M7.5 8 12 3.5 16.5 8"
            fill="none"
            stroke="currentColor"
            strokeWidth="1.8"
            strokeLinecap="round"
            strokeLinejoin="round"
          />
          <path
            d="M5 12.5v5.7a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2v-5.7"
            fill="none"
            stroke="currentColor"
            strokeWidth="1.8"
            strokeLinecap="round"
            strokeLinejoin="round"
          />
        </svg>
        Podijeli
      </button>

      {open && (
        <div className="share-menu" role="menu">
          <button type="button" className="share-option" role="menuitem" onClick={() => openShareLink("email")}>
            <span className="share-option-icon" style={{ background: "#6f6a5f" }}>
              <svg viewBox="0 0 24 24" width="15" height="15" aria-hidden="true">
                <rect x="3" y="5" width="18" height="14" rx="2" fill="none" stroke="white" strokeWidth="1.6" />
                <path d="M4 6.5 12 13 20 6.5" fill="none" stroke="white" strokeWidth="1.6" strokeLinecap="round" strokeLinejoin="round" />
              </svg>
            </span>
            Email
          </button>

          <button type="button" className="share-option" role="menuitem" onClick={() => openShareLink("viber")}>
            <span className="share-option-icon" style={{ background: "#7360f2" }}>
              <svg viewBox="0 0 24 24" width="15" height="15" aria-hidden="true">
                <path
                  d="M12 4.5c-4.4 0-7.5 2.7-7.5 7.4 0 2.9 1.5 5.1 3.9 6.3l-.5 3.3 3.4-2c.2 0 .5.02.7.02 4.4 0 7.5-2.7 7.5-7.6S16.4 4.5 12 4.5Z"
                  fill="none"
                  stroke="white"
                  strokeWidth="1.5"
                  strokeLinejoin="round"
                />
                <path d="M9 10.5c0 3 2 5 5 5" fill="none" stroke="white" strokeWidth="1.4" strokeLinecap="round" />
              </svg>
            </span>
            Viber
          </button>

          <button type="button" className="share-option" role="menuitem" onClick={() => openShareLink("whatsapp")}>
            <span className="share-option-icon" style={{ background: "#25d366" }}>
              <svg viewBox="0 0 24 24" width="15" height="15" aria-hidden="true">
                <path
                  d="M12 4.5a7.5 7.5 0 0 0-6.4 11.4L4.5 19.5l3.7-1.1A7.5 7.5 0 1 0 12 4.5Z"
                  fill="none"
                  stroke="white"
                  strokeWidth="1.5"
                  strokeLinejoin="round"
                />
                <path
                  d="M9.2 9.6c.3-.8.6-.8.9-.8h.5c.2 0 .4 0 .5.4.2.5.6 1.5.6 1.6.1.1.1.3 0 .4-.2.3-.3.4-.5.6-.2.2-.4.4-.2.7.3.5.9 1.2 1.6 1.7.7.5 1 .5 1.3.4.2-.1.6-.6.7-.8.1-.2.3-.2.5-.1.2.1 1.4.6 1.6.7.2.1.3.2.4.3 0 .2 0 .8-.3 1.2-.3.5-1.4 1-2 1-1.5 0-3.2-.9-4.4-2.1-1.2-1.2-2.1-2.9-2.1-4.5 0-.7.2-1.3.5-1.7Z"
                  fill="white"
                />
              </svg>
            </span>
            WhatsApp
          </button>

          <button type="button" className="share-option" role="menuitem" onClick={() => openShareLink("messenger")}>
            <span className="share-option-icon" style={{ background: "#0084ff" }}>
              <svg viewBox="0 0 24 24" width="15" height="15" aria-hidden="true">
                <path
                  d="M12 4.5c-4.4 0-7.7 3-7.7 7.4 0 2.4 1 4.5 2.7 5.9v3l2.5-1.4c.8.2 1.6.4 2.5.4 4.4 0 7.7-3 7.7-7.4S16.4 4.5 12 4.5Z"
                  fill="none"
                  stroke="white"
                  strokeWidth="1.5"
                  strokeLinejoin="round"
                />
                <path d="M6.8 13.6 10.4 10l2 2.1 3.7-2.1-3.6 3.9-2-2.1-3.7 2.1Z" fill="white" strokeLinejoin="round" />
              </svg>
            </span>
            Messenger
          </button>

          <button type="button" className="share-option" role="menuitem" onClick={() => openShareLink("facebook")}>
            <span className="share-option-icon" style={{ background: "#1877f2" }}>
              <svg viewBox="0 0 24 24" width="15" height="15" aria-hidden="true">
                <path
                  d="M14 9h2V6.2c-.3 0-1.4-.1-2.6-.1-2.6 0-4.4 1.6-4.4 4.5V13H6.5v3h2.5v7h3.1v-7h2.5l.4-3H12v-2.1c0-.9.2-1.5 1.5-1.5H14Z"
                  fill="white"
                />
              </svg>
            </span>
            Facebook
          </button>

          <button type="button" className="share-option" role="menuitem" onClick={handleInstagram}>
            <span
              className="share-option-icon"
              style={{
                background:
                  "linear-gradient(45deg, #f09433 0%, #e6683c 25%, #dc2743 50%, #cc2366 75%, #bc1888 100%)",
              }}
            >
              <svg viewBox="0 0 24 24" width="15" height="15" aria-hidden="true">
                <rect x="5" y="5" width="14" height="14" rx="4" fill="none" stroke="white" strokeWidth="1.6" />
                <circle cx="12" cy="12" r="3.2" fill="none" stroke="white" strokeWidth="1.6" />
                <circle cx="16.2" cy="7.8" r="0.9" fill="white" />
              </svg>
            </span>
            Instagram
          </button>

          <button type="button" className="share-option" role="menuitem" onClick={handleCopy}>
            <span className="share-option-icon" style={{ background: "var(--color-gold)" }}>
              <svg viewBox="0 0 24 24" width="15" height="15" aria-hidden="true">
                {copied ? (
                  <path d="M5 12.5 9.5 17 19 7" fill="none" stroke="white" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" />
                ) : (
                  <>
                    <path d="M9.5 14.5 14.5 9.5" stroke="white" strokeWidth="1.6" strokeLinecap="round" />
                    <path
                      d="M11 7.5l1.3-1.3a3 3 0 0 1 4.3 4.3L15.2 12"
                      fill="none"
                      stroke="white"
                      strokeWidth="1.6"
                      strokeLinecap="round"
                    />
                    <path
                      d="M13 16.5l-1.3 1.3a3 3 0 0 1-4.3-4.3L8.8 12"
                      fill="none"
                      stroke="white"
                      strokeWidth="1.6"
                      strokeLinecap="round"
                    />
                  </>
                )}
              </svg>
            </span>
            {copied ? "Kopirano!" : "Kopiraj link"}
          </button>
        </div>
      )}
    </div>
  );
}
