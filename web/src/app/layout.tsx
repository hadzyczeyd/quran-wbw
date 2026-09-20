import type { Metadata } from "next";
import Link from "next/link";
import { Analytics } from "@vercel/analytics/next";
import { Amiri_Quran, Montserrat } from "next/font/google";
import { SiteNav } from "@/components/SiteNav";
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

            <SiteNav />
          </div>
        </header>

        {children}

        <footer className="site-footer">
          <p>© {currentYear} Zejd Hadžić. Sva prava zadržana.</p>
        </footer>

        <Analytics />
      </body>
    </html>
  );
}
