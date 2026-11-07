import type { Metadata } from "next";
import Link from "next/link";
import { ConsentSettingsLink } from "@/components/ConsentManager";
import "@/styles/about.css";

export const metadata: Metadata = {
  title: "Privatnost — Kur'an riječ po riječ",
  description: "Kako Kur'an riječ po riječ postupa s podacima posjetilaca i kolačićima.",
};

// Tekst o hostingu prati platformu na kojoj je stranica izgrađena (Vercel ili Hostinger).
const onVercel = process.env.VERCEL === "1";

export default function PrivatnostPage() {
  return (
    <main className="page-shell about-page">
      <h1>Politika privatnosti</h1>
      <p className="about-lede">
        Stranicu možete koristiti bez ikakvog pristanka. Statistiku posjeta bilježimo samo ako je izričito
        dozvolite.
      </p>

      <section>
        <h2>Ko je odgovoran</h2>
        <p>
          Za obradu podataka na ovoj stranici odgovoran je Zejd Hadžić. Za sva pitanja o privatnosti i
          zahtjeve u vezi s vašim podacima koristite <Link href="/contact">Kontakt stranicu</Link>.
        </p>
      </section>

      <section>
        <h2>Statistika posjeta (samo uz pristanak)</h2>
        <p>
          Ako kliknete „Prihvatam“, u vašem pregledniku (localStorage) se pohranjuje slučajni anonimni
          identifikator uređaja i sesije, a pri otvaranju stranica bilježimo:
        </p>
        <ul>
          <li>koju stranicu ste otvorili i vrijeme posjete;</li>
          <li>odakle ste došli (npr. Google, Facebook ili direktno) i eventualni utm_source u linku;</li>
          <li>državu, određenu iz IP adrese u trenutku posjete — samu IP adresu ne pohranjujemo;</li>
          <li>vrstu uređaja (mobitel, tablet, računar), preglednik, operativni sistem i aplikaciju iz koje je
            stranica otvorena (npr. Facebook ili Instagram preglednik).</li>
        </ul>
        <p>
          Ne bilježimo ime, email, IP adresu ni precizniju lokaciju i ne pravimo profile posjetilaca.
          Podatke vidi samo administrator stranice, ne prodajemo ih i ne dijelimo s oglašivačima. Svrha je
          isključivo da znamo koliko se stranica koristi i odakle posjetioci dolaze.
        </p>
        <p>
          Pravni osnov je vaš pristanak. Možete ga povući u svakom trenutku preko „Postavke kolačića“ u dnu
          stranice (<ConsentSettingsLink />); tada se identifikator briše iz vašeg preglednika i ništa se više
          ne bilježi. Zapisi se automatski brišu nakon 13 mjeseci.
        </p>
      </section>

      <section>
        <h2>Bez pristanka</h2>
        <p>
          Ako kliknete „Odbijam“ ili ne izaberete ništa, statistika se ne bilježi. Pohranjuje se samo vaš
          izbor, kako vas ne bismo stalno pitali. Prijava administratora koristi tehnički neophodnu pohranu
          Supabase sesije, i to samo na stranici za prijavu.
        </p>
        {onVercel ? (
          <p>
            Hosting (Vercel) vodi agregatnu statistiku bez kolačića i bez praćenja pojedinaca (Vercel Web
            Analytics), uz uobičajene sigurnosne zapise servera.
          </p>
        ) : (
          <p>Hosting (Hostinger) vodi samo uobičajene sigurnosne zapise servera.</p>
        )}
      </section>

      <section>
        <h2>Gdje se podaci čuvaju</h2>
        <p>
          Statistika se čuva u bazi podataka kod pružaoca Supabase, a stranica radi na{" "}
          {onVercel ? "Vercel serverima u Frankfurtu" : "serverima pružaoca Hostinger"}. Oba pružaoca obrađuju podatke samo za potrebe rada ove stranice.
        </p>
      </section>

      <section>
        <h2>Vaša prava</h2>
        <p>
          U skladu sa Zakonom o zaštiti ličnih podataka Bosne i Hercegovine i, za posjetioce iz Evropske
          unije, Općom uredbom o zaštiti podataka (GDPR), imate pravo na pristup, ispravku i brisanje podataka,
          ograničenje obrade, prigovor i povlačenje pristanka, kao i pravo na pritužbu Agenciji za zaštitu
          ličnih podataka BiH ili nadzornom tijelu u svojoj državi. Budući da su zapisi anonimni, za zahtjev
          koji se odnosi na vaš uređaj navedite identifikator iz preglednika ili jednostavno povucite pristanak.
        </p>
      </section>
    </main>
  );
}
