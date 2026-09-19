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

const currentYear = new Date().getFullYear();

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="bs" className={`${amiriQuran.variable} ${montserrat.variable}`}>
      <body>
        <header className="site-header">
          <div className="page-shell site-header-inner">
            <Link href="/" className="site-brand">
              {/* eslint-disable-next-line @next/next/no-img-element */}
              <img src="/favicon.ico" alt="" width={24} height={24} className="site-brand-logo" />
              <span>
                <span className="site-brand-accent">Kur&apos;an</span> riječ po riječ
              </span>
            </Link>

            <input type="checkbox" id="nav-toggle" className="nav-toggle-checkbox" />
            <label htmlFor="nav-toggle" className="nav-toggle-button" aria-label="Meni">
              <svg viewBox="0 0 24 24" width="22" height="22" aria-hidden="true">
                <path d="M3 6h18M3 12h18M3 18h18" stroke="currentColor" strokeWidth="2" strokeLinecap="round" />
              </svg>
            </label>

            <nav className="site-nav">
              <Link href="/">Početna</Link>
              <Link href="/sure">Sure</Link>
              <Link href="/o-aplikaciji">O aplikaciji</Link>
              <Link href="/izvori">Izvori</Link>
              <Link href="/contact">Kontakt</Link>
            </nav>
          </div>
        </header>

        {children}

        <footer className="site-footer">
          <p>© {currentYear} Z Solutions. Sva prava zadržana.</p>
        </footer>
      </body>
    </html>
  );
}
