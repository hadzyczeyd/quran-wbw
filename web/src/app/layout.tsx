import type { Metadata, Viewport } from "next";
import Link from "next/link";
import Script from "next/script";
import { Analytics } from "@vercel/analytics/next";
import { Amiri_Quran, Atkinson_Hyperlegible_Next } from "next/font/google";
import { SiteHeader, TabBar } from "@/components/SiteNav";
import { ConsentManager, ConsentSettingsLink } from "@/components/ConsentManager";
import { ServiceWorkerRegister } from "@/components/ServiceWorkerRegister";
import { PREFS_SCRIPT } from "@/lib/prefs";
import "@/styles/tokens.css";
import "@/styles/base.css";

const amiriQuran = Amiri_Quran({
  subsets: ["arabic"],
  weight: "400",
  variable: "--font-amiri-quran",
  display: "swap",
});

// Jedno latinično pismo za sučelje i prijevod — pravljeno za čitljivost (razlikuje slične znakove).
const atkinson = Atkinson_Hyperlegible_Next({
  subsets: ["latin", "latin-ext"],
  variable: "--font-atkinson",
  display: "swap",
  // Next nema metrike za ovaj font (upozorenje pri buildu); rezervni je sistemski sans.
  adjustFontFallback: false,
  fallback: ["system-ui", "sans-serif"],
});

export const metadata: Metadata = {
  title: "Kur'an riječ po riječ",
  description:
    "Učenje kur'anskog arapskog kroz bosanski jezik — riječ po riječ, obojeno prema gramatičkoj ulozi.",
  applicationName: "Kur'an riječ po riječ",
  appleWebApp: { capable: true, title: "Riječ po riječ", statusBarStyle: "default" },
  icons: {
    icon: [{ url: "/icons/any-32.png", sizes: "32x32", type: "image/png" }],
    apple: [{ url: "/icons/apple-180.png", sizes: "180x180" }],
  },
  formatDetection: { telephone: false },
};

export const viewport: Viewport = {
  width: "device-width",
  initialScale: 1,
  viewportFit: "cover",
  themeColor: [
    { media: "(prefers-color-scheme: light)", color: "#f7f6f3" },
    { media: "(prefers-color-scheme: dark)", color: "#131210" },
  ],
};

const currentYear = new Date().getFullYear();

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="bs" className={`${amiriQuran.variable} ${atkinson.variable}`} suppressHydrationWarning>
      <body>
        {/* Tema i veličina teksta prije prvog iscrtavanja (bez bljeska). */}
        <Script id="postavke-prikaza" strategy="beforeInteractive">
          {PREFS_SCRIPT}
        </Script>
        <a href="#sadrzaj" className="skip-link">
          Preskoči na sadržaj
        </a>
        <SiteHeader />

        <div id="sadrzaj" className="page">
          {children}
        </div>

        <footer className="site-footer">
          <div className="shell site-footer-inner">
            <p className="site-footer-support">
              Smatrate li stranicu korisnom - podijelite je s drugima! Donaciju posvetite ne nama, nego:{" "}
              <a href="https://zagazu.ba" target="_blank" rel="noopener noreferrer">
                zagazu.ba
              </a>
              .
            </p>
            <nav className="site-footer-links" aria-label="Podnožje">
              <Link href="/o-aplikaciji">O aplikaciji</Link>
              <Link href="/izvori">Izvori</Link>
              <Link href="/contact">Kontakt</Link>
              <Link href="/privatnost">Privatnost</Link>
              <ConsentSettingsLink />
            </nav>
            <p className="site-footer-copy">
              © {currentYear}{" "}
              <a href="https://z-one.dev" target="_blank" rel="noopener noreferrer">
                Zejd Hadžić
              </a>
            </p>
          </div>
        </footer>

        <TabBar />
        <ConsentManager />
        <ServiceWorkerRegister />

        {/* Vercel Web Analytics postoji samo na Vercelu; na Hostingeru bi /_vercel/insights bio 404. */}
        {process.env.VERCEL === "1" && <Analytics />}
      </body>
    </html>
  );
}
