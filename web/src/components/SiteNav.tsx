"use client";

import Link from "next/link";
import { usePathname } from "next/navigation";
import { useEffect, useRef, useState } from "react";

const NAV_LINKS = [
  { href: "/", label: "Početna" },
  { href: "/sure", label: "Sure" },
  { href: "/o-aplikaciji", label: "O aplikaciji" },
  { href: "/izvori", label: "Izvori" },
  { href: "/contact", label: "Kontakt" },
];

/**
 * Hamburger meni kao klijentska komponenta (ne checkbox-hack) — treba
 * mu JS da se zatvori na klik van menija, na klik na link (Next.js
 * Link ne reloada stranicu, pa bi checkbox ostao "checked" preko
 * navigacije) i da ikona animira u X dok je otvoren.
 */
export function SiteNav() {
  const [open, setOpen] = useState(false);
  const buttonRef = useRef<HTMLButtonElement>(null);
  const navRef = useRef<HTMLElement>(null);
  const pathname = usePathname();

  useEffect(() => {
    setOpen(false);
  }, [pathname]);

  useEffect(() => {
    if (!open) return;

    function onDocumentClick(e: MouseEvent) {
      const target = e.target as Node;
      if (buttonRef.current?.contains(target)) return;
      if (navRef.current?.contains(target)) return;
      setOpen(false);
    }

    document.addEventListener("click", onDocumentClick);
    return () => document.removeEventListener("click", onDocumentClick);
  }, [open]);

  return (
    <>
      <button
        type="button"
        ref={buttonRef}
        className={`nav-toggle-button${open ? " is-open" : ""}`}
        aria-label={open ? "Zatvori meni" : "Meni"}
        aria-expanded={open}
        onClick={() => setOpen((v) => !v)}
      >
        <svg viewBox="0 0 24 24" width="22" height="22" aria-hidden="true">
          <path
            className="nav-toggle-line nav-toggle-line-top"
            d="M3 6h18"
            stroke="currentColor"
            strokeWidth="2"
            strokeLinecap="round"
          />
          <path
            className="nav-toggle-line nav-toggle-line-middle"
            d="M3 12h18"
            stroke="currentColor"
            strokeWidth="2"
            strokeLinecap="round"
          />
          <path
            className="nav-toggle-line nav-toggle-line-bottom"
            d="M3 18h18"
            stroke="currentColor"
            strokeWidth="2"
            strokeLinecap="round"
          />
        </svg>
      </button>

      <nav ref={navRef} className={`site-nav${open ? " is-open" : ""}`}>
        {NAV_LINKS.map((link) => (
          <Link key={link.href} href={link.href} onClick={() => setOpen(false)}>
            {link.label}
          </Link>
        ))}
      </nav>
    </>
  );
}
