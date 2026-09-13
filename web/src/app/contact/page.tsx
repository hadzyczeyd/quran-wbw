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
        Kur&apos;an riječ po riječ je lični, pasioni projekat — radim ga sam,
        u slobodno vrijeme, iz želje da učenje kur&apos;anskog arapskog bude
        dostupnije govornicima bosanskog jezika. Ako imaš pitanje, primjedbu
        na prijevod ili boju, ili samo želiš reći da ti se sviđa — javi se.
      </p>

      <p>
        Email:{" "}
        <a href="mailto:hadziczejd2008@gmail.com">hadziczejd2008@gmail.com</a>
      </p>

      <section>
        <h2>Pošalji poruku</h2>
        <ContactForm />
      </section>
    </main>
  );
}
