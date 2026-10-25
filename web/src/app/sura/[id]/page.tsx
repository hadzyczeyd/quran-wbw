import "@/styles/reader.css";
import { ColorLegend } from "@/components/ColorLegend";
import { MobileLegendButton } from "@/components/MobileLegendButton";
import { SuraOpeningHeader } from "@/components/SuraOpeningHeader";
import { SurahInfoSidebar } from "@/components/SurahInfoSidebar";
import { SuraReader } from "@/components/SuraReader";
import { loadSurahFromSupabase } from "@/lib/loadSurah";
import { juzStartsInSurah } from "@/lib/quranMeta";
import { getRootPanel } from "@/lib/rootPanel";
import { SURAHS } from "@/lib/surahs";

export default async function SuraPage({
  params,
}: {
  params: Promise<{ id: string }>;
}) {
  const { id } = await params;
  const surahId = Number(id);
  const data = Number.isInteger(surahId)
    ? await loadSurahFromSupabase(surahId)
    : null;

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
