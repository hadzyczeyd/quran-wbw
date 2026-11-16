import type { Metadata } from "next";
import Link from "next/link";
import "@/styles/about.css";
import { ConsentSettingsLink } from "@/components/ConsentManager";
import { Icon, type IconName } from "@/components/Icon";
import { InstallApp } from "@/components/InstallApp";
import { ShareMenu } from "@/components/ShareMenu";
import { ThemePicker } from "@/components/ThemeToggle";

export const metadata: Metadata = {
  title: "Više — Kur'an riječ po riječ",
  description: "Postavke, instalacija aplikacije, informacije o projektu i kontakt.",
};

const LINKS: { href: string; label: string; hint: string; icon: IconName }[] = [
  { href: "/o-aplikaciji", label: "O aplikaciji", hint: "Namjena i uputstvo za korištenje", icon: "info" },
  { href: "/izvori", label: "Izvori", hint: "Prijevod, gramatika, audio", icon: "sources" },
  { href: "/contact", label: "Kontakt", hint: "Prijavite grešku ili pošaljite pitanje", icon: "mail" },
  { href: "/privatnost", label: "Privatnost", hint: "Šta se bilježi i zašto", icon: "shield" },
];

/** Mobilni "Više" ekran (četvrta kartica donje trake). */
export default function VisePage() {
  return (
    <main className="shell more-page">
      <h1>Više</h1>

      <section className="more-group" aria-labelledby="more-app">
        <h2 id="more-app">Aplikacija</h2>
        <div className="more-card">
          <p className="more-text">
            Instalirajte stranicu kao aplikaciju: otvara se s početnog ekrana, preko cijelog ekrana, a
            otvarane sure rade i bez interneta.
          </p>
          <InstallApp />
        </div>
        <div className="more-card">
          <span className="field-label">Tema</span>
          <ThemePicker />
        </div>
      </section>

      <section className="more-group" aria-labelledby="more-info">
        <h2 id="more-info">Informacije</h2>
        <ul className="more-list">
          {LINKS.map((l) => (
            <li key={l.href}>
              <Link href={l.href} className="more-link">
                <Icon name={l.icon} />
                <span>
                  <span className="more-link-label">{l.label}</span>
                  <span className="more-link-hint">{l.hint}</span>
                </span>
                <Icon name="chevronRight" size={18} />
              </Link>
            </li>
          ))}
        </ul>
      </section>

      <section className="more-group more-row">
        <ShareMenu label="Podijeli stranicu" />
        <ConsentSettingsLink />
      </section>
    </main>
  );
}
