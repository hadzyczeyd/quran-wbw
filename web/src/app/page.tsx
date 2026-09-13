import "@/styles/home.css";
import { Bismillah } from "@/components/Bismillah";
import { SurahGrid } from "@/components/SurahGrid";
import { QAC_LEGEND } from "@/lib/legend";

export default function Home() {
  return (
    <main className="page-shell">
      <section className="home-hero">
        <Bismillah />
        <p className="home-lede">
          Kur&apos;an riječ po riječ — arapski tekst obojen prema gramatičkoj
          ulozi svakog segmenta, direktno preslikan iz Quranic Arabic
          Corpusa, uz bosanski prijevod koji prati isti redoslijed riječi.
          Klikni riječ da čuješ izgovor i vidiš njen bosanski dio.
        </p>
      </section>

      <section aria-labelledby="legend-heading">
        <h2 id="legend-heading" style={{ fontSize: "1rem", color: "var(--color-text-muted)" }}>
          Legenda boja (QAC — Quranic Arabic Corpus)
        </h2>
        <div className="legend-grid">
          {QAC_LEGEND.map((entry) => (
            <div className="legend-item" key={entry.cssClass}>
              <span className="legend-swatch" data-qac-class={entry.cssClass}>
                ع
              </span>
              <span className="legend-label">
                {entry.label} <em>({entry.tags.join(", ")})</em>
              </span>
            </div>
          ))}
        </div>
      </section>

      <SurahGrid />
    </main>
  );
}
