"use client";

import { useRef } from "react";
import { ColorLegend } from "./ColorLegend";

/**
 * Floating dugme za legendu boja — vidljivo samo na uskom ekranu (od
 * 75rem preuzima sticky bočna traka, vidi reader.css). Otvara popup
 * (<dialog>) sa istom kompaktnom legendom.
 */
export function MobileLegendButton() {
  const dialogRef = useRef<HTMLDialogElement>(null);

  return (
    <>
      <button
        type="button"
        className="legend-fab"
        onClick={() => dialogRef.current?.showModal()}
        aria-label="Prikaži legendu boja"
      >
        <span className="legend-dot" data-qac-class="segPurple" />
        Legenda
      </button>

      <dialog
        ref={dialogRef}
        className="legend-fab-dialog"
        onClick={(e) => {
          if (e.target === dialogRef.current) dialogRef.current?.close();
        }}
      >
        <button
          type="button"
          className="app-info-dialog-close"
          onClick={() => dialogRef.current?.close()}
          aria-label="Zatvori"
        >
          ×
        </button>
        <h2 className="legend-sidebar-heading">Legenda boja</h2>
        <ColorLegend compact />
      </dialog>
    </>
  );
}
