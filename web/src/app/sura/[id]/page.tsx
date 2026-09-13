import "@/styles/reader.css";
import { SuraReader } from "@/components/SuraReader";
import type { SurahData } from "@/lib/types";

// Privremeno: čita se iz JSON fixture-a generisanog pipeline skriptom.
// Kad Supabase baza bude spremna (OPIS poglavlje 6), ovo se zamjenjuje
// dohvatom iz baze po surah_id.
async function loadSurahData(id: string): Promise<SurahData | null> {
  try {
    const mod = await import(`@/lib/fixtures/${id}.json`);
    return mod.default as SurahData;
  } catch {
    return null;
  }
}

export default async function SuraPage({
  params,
}: {
  params: Promise<{ id: string }>;
}) {
  const { id } = await params;
  const data = await loadSurahData(id);

  if (data === null) {
    return (
      <main className="page-shell" style={{ paddingBlock: "3rem" }}>
        <p>
          Sura {id} još nema uvezene podatke. Pogledaj početnu stranicu za
          spisak sura koje su trenutno dostupne kao privremeni prikaz, dok se
          ne postavi Supabase baza za sve.
        </p>
      </main>
    );
  }

  return (
    <main className="page-shell">
      <SuraReader data={data} />
    </main>
  );
}
