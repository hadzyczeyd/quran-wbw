# Ciljana revizija dosljednosti zamjenica (dopuna THIRD, CP7)

Pročitaj `scripts/v131/prompts/COMMON.md` (posebno pravila za subjektni PRON sufiks / 55.9 i povratne zamjenice) i u
`sources/NALOG_V13.1_tekst.txt` sekcije 46.2, 46.3, 55.5–55.9.

ULAZ: `runs/<RUN>/cp7_third/CONSISTENCY_INPUT.json` — trenutno stanje mastera po ajetu (arapski ajet, Mehanovićev prijevod,
tokeni s id/tekstom/statusom, segmenti s id/oznakom/targets/target_text/napomenom).

Zadatak: pregledaj CIJELU suru isključivo za ova dva pravila dosljednosti i za svaki PRON segment koji je UNEXPRESSED presudi:
1. Samostalna subjektna zamjenica (هُوَ، هُمْ، أَنتَ، أَنتُمْ، نَحْنُ، أَنَا، هِيَ …) ili subjektni sufiks: ako ga u prijevodu nosi
   zaseban površinski token — eksplicitna zamjenica ("on", "oni", "vi", "mi", "ja") ili pomoćni glagol/kopula koja u toj
   rečenici izražava baš to lice ("su", "smo", "ste", "je", "ćete" …) i trenutno je inserted ili vezan samo za drugi segment —
   PRON se veže na taj token (55.9). Kopula koja pripada drugom subjektu ili glagolski oblik koji već nosi lice drugog segmenta
   ne dolazi u obzir. Ako lice postoji samo u glagolskoj fleksiji, PRON smije ostati UNEXPRESSED — ne mijenjaj.
2. Povratna (resumptivna) zamjenica u relativnoj rečenici ili uz istaknutu temu (npr. لَهُ، لَهُمْ، فِيهِ، بِهِ iza ٱلَّذِى/مَن/مَا
   ili iza imenice-teme): ako njenu ulogu nosi padežni/posvojni oblik relativnog izraza ili teme ("kojima", "Čija", "onima",
   "Onome", "čemu", "zulumćarima" …) — tj. oblik koji kodira upravo odnos te zamjenice s njenim prijedlogom — veže se na taj
   token (dosljedno 89:8, 85:9, 85:11). Ako bosanski relativ samo stoji u nominativu/akuzativu kao vlastiti argument, a arapska
   zamjenica je čisto ponavljanje, smije ostati UNEXPRESSED — ne mijenjaj.
3. Eksplicitna bosanska zamjenica ("On", "on", "ti", "Ti", "Mi", "mi", "oni" …) koja je trenutno INSERTED, a izražava lice
   sadržano u glagolskom (V) segmentu iste rečenice koji nema zaseban PRON segment za to lice (prefiks imperfekta y-/t-/n-/ʾ-,
   ili 3. l. jd. m. perfekta) → dodaj je u targets tog V segmenta (zadrži postojeće ciljeve), dosljedno 80:18, 81:23, 48:10.
   Ako zamjenica pripada imenskoj rečenici bez glagola, vokativu, ili je već izražena PRON segmentom drugdje → ne mijenjaj.
- Ništa drugo ne mijenjaj; postojeći ciljevi drugih segmenata ostaju; tokene ne dijeli osim ako je podjela već postojala.

IZLAZ: `runs/<RUN>/cp7_third/CONSISTENCY_FIXES.json`:
{"<segment id>": {"kind": "LINK", "targets": [[token_id, null], ...], "semantic_role": "...", "evidence_type": "PRONOUN_CONTEXT",
  "bosnian_target_phrase": "...", "rule": "dosljednost zamjenica (55.9 / povratne zamjenice)", "note": "konkretan osnov na bosanskom"}}
Upiši SAMO segmente koje stvarno treba promijeniti (prazan objekat {} ako nema ničega). Targets moraju biti tokeni istog ajeta,
redom kako stoje u prijevodu.
Ne mijenjaj nijedan drugi fajl. Odgovori u manje od 80 riječi: koji segmenti su promijenjeni i zašto.
