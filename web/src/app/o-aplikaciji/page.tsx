import type { Metadata } from "next";
import "@/styles/about.css";
import { APP_INFO_SECTIONS } from "@/lib/appInfoContent";

export const metadata: Metadata = {
  title: "O aplikaciji — Kur'an riječ po riječ",
  description: "Namjena, uputstvo za korištenje i napomene o aplikaciji Kur'an riječ po riječ.",
};

export default function OAplikacijiPage() {
  return (
    <main className="page-shell about-page">
      <h1>O aplikaciji</h1>
      {APP_INFO_SECTIONS.map((section, i) => (
        <section key={section.title}>
          {i > 0 && <h2>{section.title}</h2>}
          {section.body}
        </section>
      ))}
    </main>
  );
}
