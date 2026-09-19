import type { Metadata } from "next";
import "@/styles/about.css";
import { ContactForm } from "@/components/ContactForm";

export const metadata: Metadata = {
  title: "Kontakt — Kur'an riječ po riječ",
  description: "Kontakt i pitanja o projektu Kur'an riječ po riječ.",
};

export default function ContactPage() {
  return (
    <main className="page-shell about-page">
      <h1>Kontakt</h1>
      <p className="about-lede">
        Savršenstvo pripada samo Allahu, dok je manjkavost svojstvena
        čovjeku — zbog toga smo zahvalni na svakoj povratnoj informaciji,
        primjedbi na prijevod ili boju, te ukazivanju na moguće greške ili
        propuste.
      </p>

      <p>
        Email: <a href="mailto:hadziczejd2008@gmail.com">hadziczejd2008@gmail.com</a>
      </p>

      <section>
        <h2>Pošaljite poruku</h2>
        <ContactForm />
      </section>
    </main>
  );
}
