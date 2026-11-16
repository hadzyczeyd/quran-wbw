import "@/styles/reader.css";
import type { Metadata } from "next";
import Link from "next/link";
import { notFound } from "next/navigation";
import { SuraOpeningHeader } from "@/components/SuraOpeningHeader";
import { SuraPager } from "@/components/SuraPager";
import { SuraReader } from "@/components/SuraReader";
import { getAvailableSurahIds } from "@/lib/availableSurahs";
import { loadSurahFromSupabase } from "@/lib/loadSurah";
import { juzStartsInSurah } from "@/lib/quranMeta";
import { getRootPanelIndex } from "@/lib/rootPanel";
import { SURAHS } from "@/lib/surahs";

// Sure se generišu statično pri buildu i serviraju s CDN-a (klik na karticu
// je trenutan, a Link ih unaprijed dohvati). Nakon novog uvoza u bazu
// stranica se osvježi u pozadini najkasnije za sat — korisnik nikad ne čeka.
export const revalidate = 3600;

export async function generateStaticParams() {
  const ids = await getAvailableSurahIds();
  return [...ids].map((id) => ({ id: String(id) }));
}

export async function generateMetadata({ params }: { params: Promise<{ id: string }> }): Promise<Metadata> {
  const { id } = await params;
  const surah = SURAHS.find((s) => s.id === Number(id));
  if (!surah) return {};
  return {
    title: `${surah.id}. ${surah.nameBs} — Kur'an riječ po riječ`,
    description: `Sura ${surah.nameBs} (${surah.nameArabic}) riječ po riječ: arapski tekst obojen po gramatici, bosanski prijevod i izgovor svake riječi.`,
  };
}

export default async function SuraPage({ params }: { params: Promise<{ id: string }> }) {
  const { id } = await params;
  const surahId = Number(id);
  if (!/^\d{1,3}$/.test(id) || surahId < 1 || surahId > 114) notFound();

  const [data, rootPanel] = await Promise.all([loadSurahFromSupabase(surahId), getRootPanelIndex(surahId)]);
  const surahMeta = SURAHS.find((s) => s.id === surahId)!;

  if (data === null) {
    return (
      <main className="shell empty-state">
        <h1>{surahMeta.nameBs}</h1>
        <p>Ova sura još nije uvezena. Pogledajte listu sura koje su trenutno dostupne.</p>
        <Link href="/sure" className="btn btn-primary">
          Sve sure
        </Link>
      </main>
    );
  }

  return (
    <main className="reader">
      <SuraReader
        data={data}
        surahName={surahMeta.nameBs}
        rootPanel={rootPanel}
        juzStarts={juzStartsInSurah(surahId)}
        header={<SuraOpeningHeader surah={surahMeta} />}
        footer={<SuraPager surahId={surahId} />}
      />
    </main>
  );
}
