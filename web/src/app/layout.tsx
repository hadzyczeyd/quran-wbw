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
          <div
            className="page-shell"
            style={{
              padding: "0.9rem 0",
              display: "flex",
              justifyContent: "space-between",
              alignItems: "center",
              gap: "1rem",
            }}
          >
            <Link href="/" style={{ fontWeight: 700, textDecoration: "none" }}>
              Kur&apos;an riječ po riječ
            </Link>
            <nav style={{ display: "flex", gap: "1.2rem", fontSize: "0.9rem" }}>
              <Link href="/about" style={{ textDecoration: "none" }}>
                O projektu
              </Link>
              <Link href="/contact" style={{ textDecoration: "none" }}>
                Kontakt
              </Link>
            </nav>
          </div>
        </header>

        {children}

        <footer className="site-footer">
          <p>
            Kur&apos;anski tekst, prijevod i audio prikazani su iz izvora
            navedenih na <Link href="/about">stranici O projektu</Link>, bez
            izmjena.
          </p>
        </footer>
      </body>
    </html>
  );
}
