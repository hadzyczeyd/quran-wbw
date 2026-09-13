import "@/styles/reader.css";
import { ColorLegend } from "@/components/ColorLegend";
import { SuraReader } from "@/components/SuraReader";
import { loadSurahFromSupabase } from "@/lib/loadSurah";

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

  return (
    <main className="page-shell reader-layout">
      <SuraReader data={data} />
      <aside className="legend-sidebar" aria-label="Legenda boja">
        <h2 className="legend-sidebar-heading">Legenda boja</h2>
        <ColorLegend compact />
      </aside>
    </main>
  );
}
