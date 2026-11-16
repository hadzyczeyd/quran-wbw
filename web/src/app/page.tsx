import Link from "next/link";
import "@/styles/home.css";
import { Bismillah } from "@/components/Bismillah";
import { ContinueReading } from "@/components/ContinueReading";
import { SurahGrid } from "@/components/SurahGrid";
import { getAvailableSurahIds } from "@/lib/availableSurahs";

// Statično; lista dostupnih sura se osvježava najkasnije minut nakon uvoza nove sure.
export const revalidate = 60;

export default async function Home() {
  const availableSurahIds = await getAvailableSurahIds();

  return (
    <main className="shell home">
      <section className="hero">
        <Bismillah />
        <h1 className="hero-title">Kur&apos;an riječ po riječ</h1>
        <p className="hero-lede">
          Svaka arapska riječ obojena je prema gramatičkoj ulozi i povezana s bosanskim prijevodom.
          Dodirnite riječ da čujete izgovor i vidite njen korijen.
        </p>
        <ContinueReading />
      </section>

      <p className="note home-note">
        Aplikacija je u razvoju. Ako primijetite grešku, javite nam sa imenom sure i brojem ajeta
        putem <Link href="/contact">kontakt forme</Link>.
      </p>

      <SurahGrid availableSurahIds={availableSurahIds} />
    </main>
  );
}
