import "@/styles/home.css";
import { Bismillah } from "@/components/Bismillah";
import { ColorLegend } from "@/components/ColorLegend";
import { SurahGrid } from "@/components/SurahGrid";
import { getAvailableSurahIds } from "@/lib/availableSurahs";

export default async function Home() {
  const availableSurahIds = await getAvailableSurahIds();

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

      <section className="legend-section">
        <input type="checkbox" id="legend-toggle" className="legend-toggle-checkbox" />
        <label htmlFor="legend-toggle" className="section-heading legend-toggle-label">
          Legenda boja
        </label>
        <ColorLegend />
      </section>

      <SurahGrid availableSurahIds={availableSurahIds} />
    </main>
  );
}
