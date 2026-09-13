import type { Metadata } from "next";
import Link from "next/link";
import { Amiri_Quran, Montserrat } from "next/font/google";
import "@/styles/tokens.css";
import "@/styles/base.css";

const amiriQuran = Amiri_Quran({
  subsets: ["arabic"],
  weight: "400",
  variable: "--font-amiri-quran",
  display: "swap",
});

const montserrat = Montserrat({
  subsets: ["latin", "latin-ext"],
  variable: "--font-montserrat",
  display: "swap",
});

export const metadata: Metadata = {
  title: "Kur'an riječ po riječ",
  description:
    "Učenje kur'anskog arapskog kroz bosanski jezik — riječ po riječ, obojeno prema gramatičkoj ulozi.",
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="bs" className={`${amiriQuran.variable} ${montserrat.variable}`}>
      <body>
        <header className="site-header">
          <div className="page-shell" style={{ padding: "0.9rem 0" }}>
            <Link href="/" style={{ fontWeight: 700, textDecoration: "none" }}>
              Kur&apos;an riječ po riječ
            </Link>
          </div>
        </header>

        {children}

        <footer className="site-footer">
          <p>
            Arapski tekst i morfologija:{" "}
            <a href="https://corpus.quran.com" target="_blank" rel="noreferrer">
              Quranic Arabic Corpus
            </a>{" "}
            (Kais Dukes) i{" "}
            <a href="https://tanzil.net" target="_blank" rel="noreferrer">
              Tanzil.info
            </a>{" "}
            (CC BY-ND 3.0). Bosanski prijevod: Muhamed Mehanović,{" "}
            <a href="https://quranenc.com" target="_blank" rel="noreferrer">
              QuranEnc
            </a>
            . Audio po riječi: Tafsir Center for Quranic Studies, uz ljubaznu
            dozvolu preko{" "}
            <a href="https://quran.foundation" target="_blank" rel="noreferrer">
              Quran Foundation
            </a>{" "}
            (Quran.com) Content API-ja. Recitacija ajeta:{" "}
            <a href="https://everyayah.com" target="_blank" rel="noreferrer">
              everyayah.com
            </a>
            . Izvor arapskog teksta u bazi:{" "}
            <a href="https://al-quran.fr" target="_blank" rel="noreferrer">
              al-quran.fr
            </a>{" "}
            (CC0).
          </p>
        </footer>
      </body>
    </html>
  );
}
