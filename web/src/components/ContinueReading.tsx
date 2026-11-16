"use client";

import Link from "next/link";
import { useSyncExternalStore } from "react";
import { getLastRead, subscribeLastRead } from "@/lib/lastRead";
import { SURAHS } from "@/lib/surahs";
import { Icon } from "./Icon";

/** Glavna radnja na početnoj: nastavak zadnjeg čitanja, ili početak od El-Fatihe. */
export function ContinueReading() {
  const last = useSyncExternalStore(subscribeLastRead, getLastRead, () => null);
  const surah = last ? SURAHS.find((s) => s.id === last.surah) : undefined;

  if (!last || !surah) {
    return (
      <div className="hero-actions">
        <Link href="/sura/1" className="btn btn-primary">
          Počni čitati
        </Link>
        <Link href="/o-aplikaciji" className="btn btn-secondary">
          Kako koristiti
        </Link>
      </div>
    );
  }

  return (
    <Link href={`/sura/${surah.id}#ajet-${last.ayah}`} className="continue-card">
      <span className="continue-icon" aria-hidden="true">
        <Icon name="book" size={22} />
      </span>
      <span className="continue-text">
        <span className="continue-label">Nastavi čitati</span>
        <span className="continue-title">
          {surah.nameBs}, ajet {last.ayah}
        </span>
      </span>
      <Icon name="chevronRight" />
    </Link>
  );
}
