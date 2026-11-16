import type { Metadata } from "next";
import Link from "next/link";

export const metadata: Metadata = {
  title: "Bez interneta — Kur'an riječ po riječ",
  robots: { index: false },
};

/** Prikazuje ga service worker kad nema mreže, a tražena stranica nije ranije otvarana. */
export default function OfflinePage() {
  return (
    <main className="shell empty-state">
      <h1>Nema internet veze</h1>
      <p>
        Ova stranica još nije sačuvana na uređaju. Sure koje ste već otvarali rade i bez interneta.
      </p>
      <Link href="/sure" className="btn btn-primary">
        Otvori listu sura
      </Link>
    </main>
  );
}
