import type { Metadata } from "next";
import "@/styles/home.css";
import { SurahGrid } from "@/components/SurahGrid";
import { getAvailableSurahIds } from "@/lib/availableSurahs";

// Statično; lista dostupnih sura se osvježava najkasnije minut nakon uvoza nove sure.
export const revalidate = 60;

export const metadata: Metadata = {
  title: "Sure — Kur'an riječ po riječ",
  description: "Spisak svih 114 sura, pretraga i otvaranje čitača.",
};

export default async function SurePage() {
  const availableSurahIds = await getAvailableSurahIds();

  return (
    <main className="page-shell" style={{ paddingBlock: "2rem" }}>
      <SurahGrid availableSurahIds={availableSurahIds} />
    </main>
  );
}
