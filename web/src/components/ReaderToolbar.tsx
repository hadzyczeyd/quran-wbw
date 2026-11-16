"use client";

import Link from "next/link";
import { useState } from "react";
import { ColorLegend } from "./ColorLegend";
import { Icon } from "./Icon";
import { ReaderSettings, SETTINGS_POPOVER_ID } from "./ReaderSettings";

const LEGEND_ID = "legenda-boja";
const JUMP_ID = "skok-na-ajet";

interface ReaderToolbarProps {
  surahId: number;
  surahName: string;
  ayahCount: number;
  currentAyah: number;
  onJump: (ayah: number) => void;
}

/**
 * Traka čitača ispod zaglavlja: povratak na listu, gdje se nalazimo (sura i
 * ajet, dodir otvara skok na ajet), legenda boja i postavke prikaza.
 */
export function ReaderToolbar({ surahId, surahName, ayahCount, currentAyah, onJump }: ReaderToolbarProps) {
  const [jumpValue, setJumpValue] = useState("");

  function submitJump(e: React.FormEvent) {
    e.preventDefault();
    const n = Number(jumpValue);
    if (!Number.isInteger(n) || n < 1 || n > ayahCount) return;
    document.getElementById(JUMP_ID)?.hidePopover();
    setJumpValue("");
    onJump(n);
  }

  return (
    <>
      <div className="reader-toolbar">
        <div className="reader-toolbar-inner">
          <Link href="/sure" className="icon-btn" aria-label="Sve sure">
            <Icon name="chevronLeft" />
          </Link>
          <button type="button" className="reader-where" popoverTarget={JUMP_ID}>
            <span className="reader-where-name">
              {surahId}. {surahName}
            </span>
            <span className="reader-where-ayah">
              Ajet {currentAyah} od {ayahCount}
            </span>
          </button>
          <div className="reader-toolbar-actions">
            <button type="button" className="icon-btn legend-btn" popoverTarget={LEGEND_ID} aria-label="Legenda boja">
              <Icon name="palette" />
            </button>
            <button type="button" className="icon-btn" popoverTarget={SETTINGS_POPOVER_ID} aria-label="Postavke prikaza">
              <Icon name="type" />
            </button>
          </div>
        </div>
      </div>

      <div id={LEGEND_ID} popover="auto" className="sheet" aria-labelledby="legenda-naslov">
        <div className="sheet-head">
          <h2 id="legenda-naslov">Legenda boja</h2>
          <button type="button" className="icon-btn" popoverTarget={LEGEND_ID} popoverTargetAction="hide" aria-label="Zatvori">
            <Icon name="close" />
          </button>
        </div>
        <div className="sheet-body">
          <ColorLegend />
        </div>
      </div>

      <div id={JUMP_ID} popover="auto" className="sheet" aria-labelledby="skok-naslov">
        <div className="sheet-head">
          <h2 id="skok-naslov">Idi na ajet</h2>
          <button type="button" className="icon-btn" popoverTarget={JUMP_ID} popoverTargetAction="hide" aria-label="Zatvori">
            <Icon name="close" />
          </button>
        </div>
        <form className="sheet-body jump-form" onSubmit={submitJump}>
          <label className="field-label" htmlFor="skok-broj">
            Broj ajeta (1–{ayahCount})
          </label>
          <div className="jump-row">
            <input
              id="skok-broj"
              type="number"
              inputMode="numeric"
              min={1}
              max={ayahCount}
              required
              value={jumpValue}
              onChange={(e) => setJumpValue(e.target.value)}
              className="input"
            />
            <button type="submit" className="btn btn-primary">
              Idi
            </button>
          </div>
        </form>
      </div>

      <ReaderSettings />
    </>
  );
}
