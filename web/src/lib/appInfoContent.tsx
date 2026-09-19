// Sadržaj "O aplikaciji" — dijele ga kompaktne dropdown kartice na
// početnoj (AppInfoSection) i puna tekstualna stranica /o-aplikaciji.
export interface AppInfoSection {
  title: string;
  body: React.ReactNode;
}

export const APP_INFO_SECTIONS: AppInfoSection[] = [
  {
    title: "O aplikaciji",
    body: (
      <>
        <p>
          Svjesni vlastite manjkavosti, kao i upozorenja islamskih učenjaka
          na neispravnost doslovnog prevođenja kur’anskog teksta, ovu smo
          aplikaciju namijenili svima koji, pored prijevoda značenja
          cijelih ajeta, žele upoznati i značenja pojedinačnih kur’anskih
          riječi. Više o tome možete pogledati u{" "}
          <a
            href="https://www.youtube.com/watch?v=C3F1AvBia-8&list=PLFbK0HhGQsKyejX8pdSHo-Qvck_fXJ1eU&index=14"
            target="_blank"
            rel="noreferrer"
          >
            ovom videu
          </a>
          .
        </p>
        <p>
          Aplikacija koristi originalni arapski tekst Kur’ana i
          neizmijenjeni bosanski prijevod značenja mr. Muhameda
          Mehanovića.
        </p>
        <p>
          Veći razmak između arapskih riječi omogućava njihovo lakše
          raspoznavanje. Redovnim korištenjem aplikacije korisnik može
          lakše prepoznavati bojom označene vrste riječi, povezivati
          arapske riječi s njihovim značenjima i jednostavnije ih pamtiti.
        </p>
      </>
    ),
  },
  {
    title: "Kako koristiti aplikaciju",
    body: (
      <ul>
        <li>Arapske riječi i njihovi dijelovi označeni su bojama prema legendi.</li>
        <li>
          Povezane bosanske riječi prikazane su istom bojom kao
          odgovarajući dio arapske riječi.
        </li>
        <li>Mehanovićev prijevod značenja prenesen je bez izmjena.</li>
        <li>Bosanske riječi koje nemaju zaseban arapski dio su crne.</li>
        <li>
          Ako neki arapski dio nije zasebno izražen u bosanskom prijevodu,
          nije povezan niti istaknut.
        </li>
        <li>
          Klikom na arapsku riječ označavaju se sve povezane riječi u
          bosanskom prijevodu.
        </li>
        <li>
          Klikom na pojedinačni dio arapske riječi označava se samo
          njegov bosanski ekvivalent.
        </li>
        <li>
          Na ovaj način korisnik može jasnije uočiti vezu između arapskog
          teksta, njegovih gramatičkih dijelova i prijevoda značenja na
          bosanskom jeziku.
        </li>
        <li>Klikom na arapsku riječ pušta se audio snimak izgovora te riječi.</li>
        <li>
          Klikom na dugme &quot;play&quot; pušta se audio snimak učenja
          cijelog ajeta.
        </li>
      </ul>
    ),
  },
  {
    title: "Važna napomena",
    body: (
      <>
        <p>
          Cilj aplikacije jeste približiti značenja pojedinačnih
          kur’anskih riječi. Zato je treba posmatrati prvenstveno kao
          pomoćni rječnik kur’anskih izraza, a ne kao doslovni prijevod
          Kur’ana niti kao zamjenu za tefsir.
        </p>
        <p>
          Prijevod značenja cijelog ajeta potpunije prenosi njegov smisao,
          dok se za podrobnije i ispravnije razumijevanje uvijek treba
          vratiti pouzdanim tefsirima.
        </p>
        <p>
          Savršenstvo pripada samo Allahu, dok je manjkavost svojstvena
          čovjeku. Zbog toga smo zahvalni na svakoj povratnoj informaciji,
          konstruktivnoj kritici i ukazivanju na moguće greške ili
          propuste.
        </p>
      </>
    ),
  },
  {
    title: "Autorska prava",
    body: (
      <>
        <p>
          Sva prava su zadržana. Nijedan dio ovog sadržaja ne smije se
          koristiti u komercijalne svrhe niti ponovo objavljivati,
          umnožavati ili distribuirati u bilo kojem obliku, uključujući
          štampanje, fotokopiranje, pohranjivanje u elektronske baze
          podataka i objavljivanje na internetu, bez prethodnog pisanog
          odobrenja autora.
        </p>
        <p>
          Dozvoljeno je dijeljenje poveznice na web-stranicu i korištenje
          sadržaja za lične potrebe.
        </p>
      </>
    ),
  },
];
