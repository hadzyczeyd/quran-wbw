# Aplikacija u trgovinama (Play Store, Microsoft Store, App Store)

Sajt je od ove verzije **PWA** (progresivna web aplikacija):

- `web/src/app/manifest.ts` — naziv, ikone, boje, prečice
- `web/public/icons/` — ikone (192/512, "maskable" za Android, 180 za iPhone)
- `web/public/sw.js` — service worker: otvarane sure rade bez interneta, `/offline` kad stranica nije sačuvana
- stranica **Više** ima dugme *Instaliraj aplikaciju* (Chrome/Edge/Android) i uputstvo za iPhone

Korisnici je već sada mogu instalirati direktno sa sajta. Za objavu u trgovinama PWA se "pakuje" — kod ostaje isti, svaka promjena na sajtu odmah je i u aplikaciji (nema ponovnog slanja na pregled osim kad se mijenja ikona/naziv).

## 1. Google Play (preporučeno, najjednostavnije)

Android aplikacija je *Trusted Web Activity* (TWA): Chrome prikazuje sajt preko cijelog ekrana, bez adresne trake.

1. Otvori <https://www.pwabuilder.com>, upiši `https://kuran-rijecporijec.com` i pokreni provjeru.
2. **Package for stores → Android → Google Play**. Package ID npr. `com.kuranrijecporijec.app`. Sačuvaj *signing key* koji PWABuilder napravi (bez njega se aplikacija više ne može ažurirati).
3. U preuzetom paketu je `assetlinks.json`. Kopiraj ga u `web/public/.well-known/assetlinks.json`, commit i push (deploy). Bez toga Android prikazuje adresnu traku.
4. Napravi Google Play Developer nalog (jednokratna taksa, trenutno 25 USD), nova aplikacija → upload `.aab` fajla iz paketa → popuni opis, snimke ekrana, politiku privatnosti (`/privatnost`), upitnik o sadržaju.
5. Novi lični nalozi moraju prvo proći zatvoreno testiranje (trenutno 12 testera, 14 dana) prije javne objave.

## 2. Microsoft Store (Windows)

PWABuilder → **Windows** paket → upload u Partner Center. Individualni developerski nalog — provjeri trenutne uslove na <https://storedeveloper.microsoft.com>.

## 3. Apple App Store (iPhone/iPad)

- Treba Apple Developer Program (99 USD godišnje) i Mac s Xcodeom za build (PWABuilder → **iOS** pravi Xcode projekat).
- Apple odbija aplikacije koje su "samo sajt u okviru" (smjernica 4.2). Ovdje u prilog idu rad bez interneta, audio, postavke prikaza i panel korijena, ali odobrenje nije zagarantovano.
- Do tada: na iPhoneu u Safariju *Dijeli → Dodaj na početni ekran* daje gotovo isti doživljaj (puni ekran, ikona, offline).

## Nakon promjena

- Promjena ikone/naziva: ažurirati `manifest.ts` i ikone, za Play Store napraviti novi paket s **istim** signing keyem i povećanom verzijom.
- Promjena `sw.js` logike: povećati `VERSION` u `sw.js` da se stari keš obriše.
