import { QAC_LEGEND } from "@/lib/legend";

interface ColorLegendProps {
  /** Sažetiji prikaz za bočnu traku u čitaču (manji razmaci, jedna kolona). */
  compact?: boolean;
}

export function ColorLegend({ compact = false }: ColorLegendProps) {
  return (
    <div className={compact ? "legend-sidebar-list" : "legend-grid"}>
      {QAC_LEGEND.map((entry) => (
        <div className="legend-item" key={entry.cssClass}>
          <span className="legend-dot" data-qac-class={entry.cssClass} />
          <span className="legend-label">{entry.label}</span>
        </div>
      ))}
      <div className="legend-item">
        <span className="legend-fused-sample" aria-hidden="true">
          <span className="fused-marker" data-qac-class="segRed" />
          <span className="fused-marker" data-qac-class="segSeagreen" />
        </span>
        <span className="legend-label">riječ nosi više dijelova (tačkice = njihove boje)</span>
      </div>
    </div>
  );
}
