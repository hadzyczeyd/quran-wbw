import "@/styles/reader.css";
import { ColorLegend } from "@/components/ColorLegend";
import { MobileLegendButton } from "@/components/MobileLegendButton";
import { SuraOpeningHeader } from "@/components/SuraOpeningHeader";
import { SurahInfoSidebar } from "@/components/SurahInfoSidebar";
import { SuraReader } from "@/components/SuraReader";
import { loadSurahFromSupabase } from "@/lib/loadSurah";
import { SURAHS } from "@/lib/surahs";

export default async function SuraPage({
  params,
}: {
  params: Promise<{ id: string }>;
}) {
  const { id } = await params;
  const surahId = Number(id);
  const data = Number.isInteger(surahId) ? await loadSurahFromSupabase(surahId) : null;

  if (data === null) {
    return (
      <main className="page-shell" style={{ paddingBlock: "3rem" }}>
        <p>
          Sura {id} još nema uvezene podatke u bazi. Pogledaj početnu
          stranicu za spisak sura koje su trenutno dostupne.
        </p>
      </main>
    );
  }

  const surahMeta = SURAHS.find((s) => s.id === surahId) ?? null;

  return (
    <main className="page-shell reader-layout">
      {surahMeta && <SurahInfoSidebar surah={surahMeta} />}
      <div className="sura-main-column">
        {surahMeta && <SuraOpeningHeader surah={surahMeta} />}
        <SuraReader data={data} />
      </div>
      <aside className="legend-sidebar" aria-label="Legenda boja">
        <h2 className="legend-sidebar-heading">Legenda boja</h2>
        <ColorLegend compact />
      </aside>
      <MobileLegendButton />
    </main>
  );
}
