import "@/styles/reader.css";
import { notFound } from "next/navigation";
import { ColorLegend } from "@/components/ColorLegend";
import { MobileLegendButton } from "@/components/MobileLegendButton";
import { SuraOpeningHeader } from "@/components/SuraOpeningHeader";
import { SurahInfoSidebar } from "@/components/SurahInfoSidebar";
import { SuraReader } from "@/components/SuraReader";
import { getAvailableSurahIds } from "@/lib/availableSurahs";
import { loadSurahFromSupabase } from "@/lib/loadSurah";
import { juzStartsInSurah } from "@/lib/quranMeta";
import { getRootPanel } from "@/lib/rootPanel";
import { SURAHS } from "@/lib/surahs";

// Sure se generišu statično pri buildu i serviraju s CDN-a (klik na karticu
// je trenutan, a Link ih unaprijed dohvati). Nakon novog uvoza u bazu
// stranica se osvježi u pozadini najkasnije za sat — korisnik nikad ne čeka.
export const revalidate = 3600;

export async function generateStaticParams() {
  const ids = await getAvailableSurahIds();
  return [...ids].map((id) => ({ id: String(id) }));
}

export default async function SuraPage({
  params,
}: {
  params: Promise<{ id: string }>;
}) {
  const { id } = await params;
  const surahId = Number(id);
  if (!/^\d{1,3}$/.test(id) || surahId < 1 || surahId > 114) notFound();
  const data = await loadSurahFromSupabase(surahId);

  if (data === null) {
    return (
      <main className="page-shell" style={{ paddingBlock: "3rem" }}>
        <p>
          Sura {id} još nema uvezene podatke u bazi. Pogledaj početnu stranicu
          za spisak sura koje su trenutno dostupne.
        </p>
      </main>
    );
  }

  const surahMeta = SURAHS.find((s) => s.id === surahId) ?? null;

  return (
    <main className="page-shell reader-layout">
      <div className="reader-left-column">
        {surahMeta && <SurahInfoSidebar surah={surahMeta} />}
        <aside className="legend-sidebar" aria-label="Legenda boja">
          <h2 className="legend-sidebar-heading">Legenda boja</h2>
          <ColorLegend compact />
        </aside>
      </div>
      <SuraReader
        data={data}
        rootPanel={await getRootPanel(surahId)}
        juzStarts={juzStartsInSurah(surahId)}
        header={surahMeta && <SuraOpeningHeader surah={surahMeta} />}
      />
      <MobileLegendButton />
    </main>
  );
}
