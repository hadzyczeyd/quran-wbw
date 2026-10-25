# Ciljana revizija dosljednosti (dopuna THIRD, CP7)

Pročitaj `scripts/v131/prompts/COMMON.md` (posebno pravilo "relativna preoblika BEZ REL segmenta") i u
`sources/NALOG_V13.1_tekst.txt` sekcije 46.2, 46.3, 55.5–55.9.

ULAZ: `runs/<RUN>/cp7_third/CONSISTENCY_INPUT.json` — trenutno stanje mastera po ajetu (arapski ajet, Mehanovićev prijevod,
tokeni s id/tekstom/statusom, segmenti s id/oznakom/targets/target_text/napomenom).

Zadatak: pregledaj CIJELU suru isključivo za pravila dosljednosti iz COMMON.md (relativna preoblika bez REL segmenta i
korelativno "i … i"):
- N/ADJ segment (particip, imenica, pridjev) koji Mehanović prevodi relativnom preoblikom ("onaj koji …", "oni koji su …",
  "onih koje …", "Onaj Koji …", "onoga ko …") i nema svoj REL segment → cijeli izraz (uključujući "onaj/oni/onih/onoga" i
  "koji/ko/koje") mora biti target tog N/ADJ segmenta;
- V segment čijoj opisnoj rečenici Mehanović dodaje "koji/koja/koje" (bez REL segmenta) → "koji/koja/koje" NE smije biti target
  glagola (ostaje inserted); glagol zadržava svoj glagolski izraz;
- korelativno "i … i" / "i … a i" kojim Mehanović prevodi jedan arapski wa → svi tokeni korelacije (i prvo "i") su targets
  tog wa segmenta; "i" koje je samo Mehanovićev pojačivač bez korelacije ostaje inserted;
- ništa drugo ne mijenjaj; "koji" koji pripada stvarnom REL segmentu ostaje na REL-u; ne diraj poddijelove tokena osim ako su
  direktno u pitanju.

IZLAZ: `runs/<RUN>/cp7_third/CONSISTENCY_FIXES.json`:
{"<segment id>": {"kind": "LINK", "targets": [[token_id, null], ...], "semantic_role": "...", "evidence_type": "PHRASE_CONTEXT",
  "bosnian_target_phrase": "...", "note": "konkretan osnov na bosanskom"}}
Upiši SAMO segmente koje stvarno treba promijeniti (prazan objekat {} ako nema ničega). Targets moraju biti tokeni istog ajeta,
redom kako stoje u prijevodu, i moraju zadržati sve postojeće ciljeve koji nisu predmet pravila.
Ne mijenjaj nijedan drugi fajl. Odgovori u manje od 60 riječi: koji segmenti su promijenjeni i zašto.
