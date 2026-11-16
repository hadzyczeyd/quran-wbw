import { QAC_LEGEND } from "@/lib/legend";

/** Legenda QAC boja — u čitaču (ploča/popover) i na stranici O aplikaciji. */
export function ColorLegend({ wide = false }: { wide?: boolean }) {
  return (
    <ul className={`legend-list${wide ? " is-wide" : ""}`}>
      {QAC_LEGEND.map((entry) => (
        <li className="legend-item" key={entry.cssClass}>
          <span className="legend-dot" data-qac-class={entry.cssClass} aria-hidden="true" />
          <span className="legend-label">{entry.label}</span>
        </li>
      ))}
      <li className="legend-item">
        <span className="legend-fused-sample" aria-hidden="true">
          <span className="fused-marker" data-qac-class="segRed" />
          <span className="fused-marker" data-qac-class="segSeagreen" />
        </span>
        <span className="legend-label">bosanska riječ nosi više arapskih dijelova (tačke su njihove boje)</span>
      </li>
    </ul>
  );
}
