import "@/styles/home.css";
import { AppInfoSection } from "@/components/AppInfoSection";
import { Bismillah } from "@/components/Bismillah";
import { ColorLegend } from "@/components/ColorLegend";
import { DevStatusBanner } from "@/components/DevStatusBanner";
import { SurahGrid } from "@/components/SurahGrid";
import { getAvailableSurahIds } from "@/lib/availableSurahs";

export default async function Home() {
  const availableSurahIds = await getAvailableSurahIds();

  return (
    <main className="page-shell">
      <section className="home-hero">
        <Bismillah />
        <h1 className="home-title">Kur&apos;an riječ po riječ</h1>
        <p className="home-lede">
          Arapski tekst obojen prema gramatičkoj ulozi svake riječi, uz
          bosanski prijevod i izgovor na dodir.
        </p>
        <DevStatusBanner />
      </section>

      <AppInfoSection />

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
