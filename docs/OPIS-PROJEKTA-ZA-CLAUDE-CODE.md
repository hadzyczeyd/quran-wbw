# Kur'an riječ po riječ — opis projekta

Ovaj dokument daj Claude Codeu na početku rada. Opisuje šta se gradi,
kako je već bilo izgrađeno jednom, i koje su zamke već otkrivene i
riješene. Nemoj ga skraćivati; dio o zamkama je najvredniji.

Uz njega ide i `NALOG-V13`, koji uređuje **izradu podataka** (QAC
morfologija, boje, poravnanje, revizija). Ovaj dokument uređuje
**aplikaciju**. Kad se sukobe, pogledaj poglavlje 12.

---

## 0. Kako razgovarati sa mnom

- Nisam programer. Ovo mi je prvi projekt ove vrste.
- Objasni **šta radiš i zašto**, kratko, prije nego uradiš.
- Kad tražiš da nešto pokrenem, daj **tačnu komandu** i reci u kojem
  folderu se pokreće.
- Kad nešto pukne, objasni uzrok prostim jezikom, ne samo ispravku.
- Radim na **Windowsu, PowerShell**. Komande prilagodi tome.
- Commituj u Git nakon svakog koraka koji radi.

---

## 1. Šta aplikacija radi

Web aplikacija za učenje kur'anskog arapskog kroz bosanski jezik.

Korisnik otvori suru i vidi arapski tekst riječ po riječ, svaka riječ
obojena prema svojoj gramatičkoj ulozi. Ispod je bosanski prijevod.

- **Klik na arapsku riječ** → čuje se izgovor te riječi i u prijevodu
  se istaknu svi bosanski dijelovi koji joj odgovaraju.
- **Klik na bosanski dio** → istakne se cijela arapska riječ kojoj
  pripada.
- **Dugme uz ajet** → prava recitacija cijelog ajeta, u komadu.
- **Dva sloja prijevoda**, prebacivo globalno i po pojedinom ajetu:
  - *Mehanović* — objavljeni prijevod, proza, bez boja i bez klikanja
  - *Riječ po riječ* — prati arapski red riječi, obojen, klikabilan

Ciljna publika su govornici bosanskog koji uče arapski. Boja je
sredstvo učenja: gramatika se usvaja usput, bez tabela napamet.

---

## 2. Tehnički stack

| Sloj | Izbor |
|---|---|
| Frontend | Next.js (App Router), React, TypeScript |
| Stil | čisti CSS s varijablama, bez Tailwind klasa u komponentama |
| Baza | Supabase PostgreSQL, lokalno preko Dockera |
| Offline (planirano) | IndexedDB preko Dexie.js |
| Service worker (planirano) | Serwist, ne `next-pwa` |
| Data pipeline | Python, upravljan sa `uv` |
| Hosting (planirano) | Vercel + Supabase cloud |
| Mobile (kasnije) | Capacitor nad istim web kodom |

Arhitektura mora biti **web-first**. Nikakva mobile-only zavisnost u
osnovnoj logici.

Fontovi preko `next/font/google`:
- **Amiri Quran** za arapski (jedina debljina 400)
- **Montserrat** za sav latinični tekst

---

## 3. Struktura foldera

```
quran-wbw/
├── web/                          Next.js aplikacija
│   ├── src/app/                  rute
│   │   ├── page.tsx              početna
│   │   └── sura/[id]/page.tsx    čitač
│   ├── src/components/
│   ├── src/lib/supabase.ts       klijent, tipovi, dohvat
│   ├── src/styles/
│   │   ├── tokens.css            JEDINO mjesto gdje žive hex boje
│   │   ├── base.css              okvir, zaglavlje, podnožje
│   │   ├── home.css
│   │   └── reader.css
│   ├── public/audio/             lokalni audio
│   └── supabase/migrations/      SQL migracije
├── data-pipeline/
│   ├── sources/                  sirovi izvori (u .gitignore)
│   ├── scripts/                  Python skripte
│   ├── reports/                  izvještaji o provjerama
│   └── output/
└── docs/
```

**Važno:** Supabase CLI se instalira kao lokalna zavisnost u `web/` i
tamo očekuje folder `supabase/`. Migracije **moraju** biti u
`web/supabase/migrations/`, ne u korijenu projekta.

---

## 4. Izvori podataka

### 4.1 Arapski tekst i korijeni

- **al-quran.fr** → `tadabbur_corpus_essentiel.sqlite`, verzija
  `v_2026-08-13`, 36 MB
- Licenca **CC0**, komercijalna upotreba dozvoljena
- Tabele: `arabic_soura`, `arabic_words` (77.878 redova), `arabic_phrase`,
  `readings`, `root_knowledge`, `translations`
- `arabic_words` kolone: `id, id_phrase, soura, verse, word, root,
  root_pure, prefix, suffix, is_particle`
- **Nema POS oznaka** (samo `is_particle` 0/1), nema `word_position`
  (izvodi se iz redoslijeda `id`), nema morfoloških segmenata
- `text_hafs` je uthmani pravopis s alef waslom `ٱ` i nadrednim alifom `ٰ`
- Prijevodi u ovoj bazi (en, es, fr, id, it, ru) idu **po frazi**, ne po
  ajetu, i nisu upotrebljivi

### 4.2 Morfologija

- **Quranic Arabic Corpus v0.4** → `quranic-corpus-morphology-0.4.txt`,
  6,3 MB, 128.276 redova
- Copyright 2011 Kais Dukes, GNU GPL; arapski tekst iz Tanzil projekta,
  CC BY-ND 3.0
- Uslovi: original se **ne mijenja**, atribucija i link na
  `corpus.quran.com` moraju biti vidljivi u aplikaciji
- Zaglavlje je 56 redova, kolone na redu 56, podaci od reda 57
- Kolone razdvojene tabulatorom: `LOCATION  FORM  TAG  FEATURES`
- `LOCATION` = `(sura:ajet:riječ:segment)` — direktno upotrebljiv ključ
- `FORM` je Buckwalter transliteracija, ne arapsko pismo
- `FEATURES` nosi `POS:`, `LEM:`, `ROOT:` i gramatička svojstva
- 128.219 segmenata, **77.429 riječi**, 6236 ajeta, 114 sura
- Maksimalno 5 segmenata po riječi
- 44 različite POS oznake

### 4.3 Bosanski prijevod

- **QuranEnc** → `bosnian_mihanovich_v1.1.0-csv.1.csv`, 873 KB
- Prevodilac Muhamed Mehanović, verzija `v1.1.0-csv.1`, ažurirano
  2019-12-21
- CSV: 11 redova zaglavlja, pa kolone `id, sura, aya, translation,
  footnotes`
- 6236 ajeta, 114 sura, 0 fusnota, 0 praznih prijevoda
- **Uslov:** zaglavlje traži da se informacije o prijevodu ne uklanjaju.
  Atribucija na quranenc.com mora ostati vidljiva.
- Formalna licenca nije navedena u fajlu — provjeriti prije javnog
  objavljivanja

### 4.4 Audio po riječi

- **Hugging Face**, dataset `zaibihassan/Quranic-Word-By-Word-Audio-Data`
- Licenca **Apache 2.0**, traži link nazad na repozitorij
- 155.090 fajlova, dva recitatora: `muallim` i `mujawwad`
- Format `.opus`, 16 kHz mono
- Naming: `muallim/001/001_001_002.opus` = sura 1, ajet 1, riječ 2
- Uz svaku suru ide `.pb` fajl (Protocol Buffer) s timing podacima
- **Skidati samo po suri**, `--include "muallim/001/*"`. Skidanje cijelog
  dataseta odjednom udari u rate limit (HTTP 429) i traje danima.
- CLI se zove `hf`, ne više `huggingface-cli`

### 4.5 Recitacija po ajetu

- **everyayah.com**, `https://everyayah.com/data/Husary_128kbps/SSSAAA.mp3`
- Npr. `001002.mp3` = sura 1, ajet 2. Fajl `001000.mp3` je bismilla.
- Licencu provjeriti u `000_license.html` kod recitatora
- Ovo je **jedan fajl po ajetu**, pušta se cijeli, bez ikakvih timinga

---

## 5. Zamke koje su već otkrivene

Ovo je najvažnije poglavlje. Svaka od ovih stvari je otkrivena kroz
grešku i košta dan rada ako se ponovi.

### 5.1 Bismilla

- **al-quran.fr** uključuje bismillu kao prve 4 riječi ajeta 1 **svake**
  sure osim 9.
- **QAC i audio dataset je NE uključuju**, osim u suri 1 gdje bismilla
  jeste ajet 1.
- Razlika: 112 sura × 4 riječi = 448 riječi.
- **Pipeline mora preskočiti prve 4 riječi iz al-quran.fr baze za svaku
  suru osim 1 i 9.** Bez toga su sve pozicije riječi pomjerene za četiri
  i audio svira pogrešne riječi.

### 5.2 Jedino nesistematično odstupanje

- `37:130`: al-quran.fr ima 4 riječi, audio dataset 3. Radi se o
  إِلْ يَاسِينَ, koje se negdje piše kao dvije riječi, negdje kao jedna.
- To je **jedina** takva razlika u cijelom Kur'anu.

### 5.3 Ligatura لله

- لله tvori jedan spojeni glif u fontu.
- Ako se لِ i لَّهِ oboje kao dva odvojena segmenta, browser **cijelu
  ligaturu oboji bojom prvog segmenta**, pa لِلَّهِ ispadne sivo umjesto
  ljubičasto.
- Rješenje: ta dva segmenta se spajaju u jedan, boje se bojom osnove.
- Ovo je ograničenje prikaza teksta, ne pojednostavljivanje.

### 5.4 Određeni član

- QAC ٱل tretira kao zaseban DET segment.
- Ako se oboji sivo, riječ ispadne dvobojna na način koji ne odgovara
  legendi („određeni član ostaje spojen i preuzima boju nosive riječi").
- Rješenje: DET segment se spaja sa sljedećim i preuzima njegovu boju.

### 5.5 Arapska riječ se NIKAD ne razdvaja na ekranu

- Riječ je **jedan** HTML element. Segmenti su samo obojeni rasponi
  unutar nje, bez razmaka i bez reza, da se slova normalno spajaju.
- Podjela poslova:

| Ponašanje | Nivo |
|---|---|
| Prikaz teksta | riječ |
| Klik | riječ |
| Audio | riječ |
| Isticanje | riječ |
| Boja | **segment** |

- Klik na bosanski token ističe **cijelu** arapsku riječ, nikad dio.
- Boju token uzima od svog segmenta, ali isticanje ide na riječ.

### 5.6 Isticanje ne smije uništiti boju

- Za isticanje koristiti pozadinu, podvlaku, obrub ili debljinu.
- **Nikad ne mijenjati `color`** teksta.
- Provjereno dobro rješenje: pozadina izvedena iz `currentColor`, npr.
  `color-mix(in srgb, currentColor 14%, transparent)`. Tako zelena riječ
  dobije blagu zelenu podlogu i boja ostaje čitljiva.

### 5.7 QUL timinzi ne odgovaraju snimku

- QUL (qul.tarteel.ai) resurs 316, Husary sura po sura sa segmentima,
  ima u sqlite bazi **dvije adrese po suri** i **ista vremena za obje**.
- Adresa `khalil_al_husary/murattal` na CDN-u **ne postoji** (NoSuchKey).
- Adresa `husary/muallim` postoji, ali vremena joj **ne odgovaraju** —
  samo bismilla se poklapa, dalje sve odlazi u stranu.
- Zato je za recitaciju ajeta uzet everyayah.com, jedan fajl po ajetu.
- Ako se ikad vraćaš na QUL, **obavezno provjeri adresu HTTP zahtjevom
  prije upisa** i provjeri sinhronizaciju sluhom.

### 5.8 Segmenti u QUL bazi nisu JSON

- Zapis je Ruby: `[[1,0,630],[4,2640,5000,{"waqaf"=>true}]]`.
- `json.loads` to ne čita. Koristiti regex ili zamijeniti `=>` sa `:`.

### 5.9 Rezanje uthmani teksta na segmente

- Excel fajlovi nose arapski u imlaei pravopisu (`مَالِكِ`), a prikaz
  mora biti uthmani (`مَٰلِكِ`).
- Rješenje: uzeti uthmani riječ iz al-quran.fr baze i **izrezati je** na
  onoliko dijelova koliko ima segmenata, tražeći granice po
  **suglasničkom kosturu** (bez dijakritike, uz izjednačavanje alifa
  `ٱ إ أ آ` → `ا`).
- Skripta mora provjeriti da spojeni dijelovi daju **tačno** original, i
  prijaviti riječ ako ne daju.

### 5.10 Interpunkcija

- Mehanovićev prijevod se čuva **tačno kako je objavljen**, sa svim
  znakovima, i ne tokenizira se.
- Prijevod riječ po riječ **nema interpunkciju**; znakovi se skidaju s
  tokena, a riječi se odvajaju jednim razmakom.
- Ako se interpunkcija ikad izvodi poređenjem s originalnim tekstom,
  čitač se mora pomjeriti preko svakog znaka **tačno jednom**, inače isti
  zarez bude dodijeljen dva puta (bilo je tačno to).

### 5.11 Excel formati se mijenjaju kroz verzije

Do sada su viđena dva:

**Stari** (Fatiha, En-Nas) — dva fajla:
- `app_ready`: list `Segmenti` s kolonama `location, segment_id,
  segment_za_prikaz, corpus_tag, kategorija_bs, boja, hex,
  bosanski_oslonac`
- `obojeni`: jedan list, redovi `Ajet N:M`, `Arapski — boje`,
  `Mehanović — original`, `Bosanski — prati arapski`, boje kao boja fonta

**Noviji (V9/V10)** — jedan fajl je dovoljan:
- `Segmenti`: `segment_id, word_id, surah, ayah, word_index,
  segment_index, arapska_rijec, arapska_jedinica, qac_tag,
  qac_morfologija, morfologija_bs, kategorija, boja, ...`
- `Poravnanje`: `link_id, segment_id, bosnian_unit_id, surah, ayah,
  word_index, segment_index, redoslijed_bosanske_jedinice,
  arapska_jedinica, bosanska_jedinica, kategorija, boja,
  status_poravnanja, ...`
- `Prijevod_Mehanovic`: `mehanovic_original`, ponekad i
  `obojeni_tokeni_app` (V9 ima, V10 nema — **ne oslanjati se na nju**)
- `Vizuelne_grupe`, `Legenda`, `Izvori`

**Pravila za čitanje Excela:**
- Prepoznaj format po sadržaju, ne po imenu fajla.
- Redoslijed i tekst bosanskih tokena gradi iz lista `Poravnanje`
  (`redoslijed_bosanske_jedinice`), jer je on prisutan u svim verzijama.
- Redovi s praznim `word_index` su **crni umetnuti tokeni** bez arapskog
  ekvivalenta, ne greška.
- Jedna bosanska riječ može imati **više** redova u `Poravnanju`, jer se
  veže za više arapskih segmenata. To je many-to-many i mora tako i u
  bazu.
- Pročitaj sve Excele **jednom** i napravi indeks. Ranija verzija ih je
  otvarala za svaku suru posebno, 448 puta, i bila neupotrebljivo spora.

### 5.12 Kodiranje CSV-a na Windowsu

- Excel na našim Windowsima snima CSV u **Windows-1250**, ne UTF-8.
- Svaka skripta koja čita CSV koji korisnik može urediti mora probati
  redom `utf-8-sig, utf-8, cp1250, cp1252, latin-1`.
- Ispis Pythona u fajl uvijek s `encoding="utf-8"`, jer preusmjeravanje
  kroz PowerShell lomi arapska i naša slova.

---

## 6. Šema baze

Trinaest tabela plus `ayah_audio`. Ključna načela:

- Stabilni identifikatori: `'1:2:3'` za riječ, `'1:2:3:1'` za segment.
- **Nikad se ne spaja po arapskom pravopisu**, samo po tim ključevima.
- Download status **ne živi u Postgresu**, on je lokalni (IndexedDB).

```
color_keys(key, label_bs, hex)
surahs(id, name_ar, name_translit, name_bs, revelation_type,
       ayah_count, has_basmala)
ayahs(surah_id, ayah_number, text_uthmani)
words(location PK, surah_id, ayah_number, word_position,
      text_uthmani, root, lemma, corpus_tags)
word_segments(segment_location PK, word_location, segment_position,
      segment_text, corpus_tag, category_bs, color_key)
reciters(id, name, style, source_url, license)
audio_packages(surah_id, reciter_id, version, audio_url, audio_bytes,
      audio_sha256, timings_sha256, duration_ms, word_count, source)
word_timings(reciter_id, word_location, start_ms, end_ms,
      source_start_ms, source_end_ms)
ayah_audio(surah_id, ayah_number, reciter_id, audio_url, source,
      audio_bytes, audio_sha256)
translations(id, language, translator, version, source_url,
      attribution, kind)          kind: 'published' | 'literal'
translation_ayahs(translation_id, surah_id, ayah_number, text)
bosnian_tokens(id, translation_id, surah_id, ayah_number,
      token_position, display_text, is_translation_only,
      has_direct_arabic_counterpart, color_key,
      color_source_segment_location, prefix_punct, suffix_punct)
token_word_links(token_id, word_location, confidence,
      manual_review_status, mapping_provenance)
source_attributions(id, label, url, license, note)
```

Ograničenje koje se pokazalo korisnim: `bosnian_tokens` ima CHECK koji
odbija upis ako je token označen kao translation-only a nije crn ili ima
izvor boje. Baza tako sama hvata greške pipelinea.

RLS uključen na svim tabelama, politika samo za čitanje.

---

## 7. Boje

Definišu se **samo** u `web/src/styles/tokens.css`. Nigdje u kodu se ne
piše hex. Primjenjuju se preko atributa `data-color` na elementu.

| Ključ | Kategorija | Hex |
|---|---|---|
| `divine` | Allahova imena i svojstva | `#6B2D8E` |
| `verb` | Glagoli | `#A92F28` |
| `noun` | Imenice i glagolske imenice | `#1F6B4D` |
| `pronoun` | Zamjenice | `#1B5A94` |
| `particle` | Čestice i prijedlozi | `#8A8A93` |
| `negation` | Negacije | `#A9600F` |
| `translation` | Bosanske riječi bez arapskog parnjaka | `#000000` |

Prve verzije su koristile materijalne boje na punoj zasićenosti
(`#7B1FA2`, `#C62828`, `#2E7D32`, `#1565C0`, `#808080`, `#EF6C00`) i
međusobno su se nadglasavale. Nove su spuštene na približno istu
percipiranu tamnoću. Crna ostaje čista `#000000`.

Boja tokena se uzima **iz arapskog segmenta**, ne iz Excela s obojenim
ćelijama. Obojeni Excel odlučuje samo šta je crno.

---

## 8. Audio arhitektura

Dva izvora zvuka, korisnik **ne bira** između njih:

| Radnja | Izvor |
|---|---|
| Klik na riječ | izolovani snimak riječi (`muallim`), iz spojenog fajla po suri |
| Dugme uz ajet | everyayah.com, jedan mp3 po ajetu, pušta se cijeli |

**Spajanje word clipova** u jedan fajl po suri radi ffmpeg concat, a
`start_ms`/`end_ms` se računaju iz stvarnih trajanja clipova pomoću
`mutagen`. Timinzi su tako savršeno tačni jer se izvode iz fajlova koji
se stvarno reproduciraju.

**Reprodukcija raspona:** jedan `<audio>` element, `currentTime` na
početak, i `requestAnimationFrame` petlja koja pauzira na kraju.
`timeupdate` nije dovoljno precizan. Brzi uzastopni klikovi se rukuju
tako da se prethodna reprodukcija uvijek prekine prije nove.

**Udaljeni fajl:** prije postavljanja `currentTime` treba sačekati
`loadedmetadata`, inače postavka ne uspije.

---

## 9. Aplikacija, stanje na kraju prethodnog pokušaja

### Rute
- `/` — početna: bismilla u bojama, kratko objašnjenje, legenda sedam
  boja s primjerima, pretraga i mreža od 114 sura. Sure bez podataka su
  blijede i neklikabilne, uz brojač `N / 114`.
- `/sura/[id]` — čitač.

### Raspored čitača
- Lijepljeno zaglavlje preko cijele širine, s izborom sure, prekidačem
  prijevoda i kontrolama veličine teksta.
- Sadržaj ide do 96rem, razmaci se skaliraju sa širinom prozora.
- Iznad 62rem: tri kolone — broj ajeta i dugme za reprodukciju u uskom
  žlijebu, prijevod u sredini, arapski desno. Ispod toga se slaže jedno
  ispod drugog.
- Oznaka kraja ajeta: `U+06DD` plus istočnoarapske cifre. Kur'anski font
  to crta kao ukrasni krug s brojem. Zadeblja se sa
  `-webkit-text-stroke`, jer Amiri Quran ima samo jednu debljinu.

### Šta radi
- prikaz, boje po segmentima, klik i audio po riječi
- bidirekcijsko isticanje u oba smjera
- recitacija cijelog ajeta
- dva sloja prijevoda, globalni prekidač i prekidač po ajetu
- skaliranje teksta
- bosanski nazivi sura

### Šta NE radi i tek treba
- **offline režim** — service worker, Dexie, download po suri s
  provjerom prije nego se sura označi kao dostupna offline
- **deploy** na Vercel i Supabase cloud
- **ljubičasta lista lema** — razlikovanje Allahovih svojstava od običnih
  pridjeva nije mehaničko (رَحِيم se u 9:128 odnosi na Poslanika, رَبّ se
  koristi i za obične gospodare). Riješiti prije nego se boje puste na
  cijeli Kur'an.

---

## 10. Offline zahtjevi (nije započeto)

Bez interneta mora raditi, nakon što je jednom keširano: arapski tekst,
metapodaci sura i ajeta, tokenizacija, segmenti, POS, boje, bosanski
prijevod, poravnanja, prethodno skinuti audio paketi, download status.

Audio se skida **po suri**, ne unaprijed sav.

Sura se smije označiti kao dostupna offline **tek nakon** što:
1. je kompletan paket skinut,
2. su fajlovi uspješno raspakovani,
3. timing metapodaci odgovaraju očekivanoj verziji paketa,
4. je lokalni cache metadata uspješno ažuriran,
5. test čitanje potvrdi da keširani audio postoji i dostupan je.

**Prekinuti ili korumpirani download se nikada ne smije prikazati kao
gotov.**

---

## 11. Pravila rada s podacima

Ova pravila su spasila projekt više puta:

- **Ne pretpostavljaj format iz naziva.** Skini izvor, ispiši strukturu,
  pa tek onda piši kod.
- **Skripta staje umjesto da tiho upiše nešto pogrešno.** Svaka import
  skripta prvo provjeri da se broj riječi poklapa između Excela, corpus
  baze i QAC morfologije, pa tek onda piše u bazu.
- **Prijavi svako odstupanje**, ne progutaj ga. Poruke tipa
  „N tokena nema vezu, upisani su kao crni" su korisne.
- **Import je ponovljiv.** Briše samo svoju suru i upisuje je nanovo.
- Sirovi izvori i generisani output **ne idu u Git**. U repo ide samo
  pipeline koji ih reproducira.

---

## 12. Odnos prema NALOGU V13

`NALOG-V13` uređuje izradu podataka i on je mjerodavan za morfologiju,
boje i poravnanje. Ali dvije njegove odredbe se sudaraju s onim što
browser stvarno može:

1. **Zabrana spajanja segmenata** (poglavlje 24) ne može se ispoštovati
   za ligaturu لله i za određeni član, jer se ligatura u fontu oboji
   bojom prvog segmenta. To je ograničenje prikaza, ne pojednostavljenje.
2. **Boja iz QAC CSS klase** (poglavlje 5) znači čitanje web prikaza s
   corpus.quran.com za svaku riječ. Fajl koji se skine s njihove
   stranice ima tagove i morfologiju, ali **nema boje**.

Kad naiđeš na ovo, **stani i pitaj me**, nemoj sam birati.

---

## 13. Obavezne atribucije u aplikaciji

1. **Quranic Arabic Corpus**, uz link na `http://corpus.quran.com`
2. **Tanzil.info** za arapski tekst (CC BY-ND 3.0)
3. **quranenc.com** i Muhamed Mehanović za prijevod
4. **zaibihassan/Quranic-Word-By-Word-Audio-Data** (Apache 2.0), uz link
   na repozitorij
5. **everyayah.com** za recitaciju
6. **al-quran.fr** (CC0)

---

## 14. Provjereni brojevi

Koristi ih kao kontrolne vrijednosti:

- 114 sura, 6236 ajeta
- 77.429 riječi (QAC i audio dataset)
- 77.878 riječi u al-quran.fr bazi — razlika je bismilla plus 37:130
- 128.219 segmenata u QAC-u
- Sura 1: riječi po ajetu 4, 4, 2, 3, 4, 3, 9 — ukupno 29
- Sura 114: 4, 2, 2, 4, 5, 3 — ukupno 20, bez bismille
- Fatiha, spojeni audio muallim: oko 56,5 sekundi
