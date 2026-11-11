# Kratko značenje kartice panela korijena (nalog V7, odjeljak 8)

Ulaz: `sources/root_panel/GLOSS_TODO_<k>.json` — lista kartica. Svaka ima:
`key`, `root` / `root_display`, `pos` (N imenica ili V glagol), `lemma`, `features` (QAC), `form` (tačna arapska riječ
kartice), `ref` (primjer), `gloss_en` (engleska glosa QAC Dictionary za tu lokaciju), `arabic_marked` (cijeli ajet,
ciljna riječ u [[ ]]) i `bosnian` (Mehanovićev prijevod tog ajeta).

Izlaz: `sources/root_panel/GLOSS_DONE_<k>.json` = `{"<key>": "<kratko značenje>", ...}` za SVAKI key iz ulaza.
Provjera: `uv run scripts/roots/gloss_pool.py check <k>` mora završiti s "grešaka 0".

## Pravila
- Kratko značenje je bosanska leksička glosa prikazane riječi `form`, ne citat prijevoda ajeta. Obično 1–4 riječi,
  najviše 7. Bez navodnika, zagrada, arapskih slova i završne tačke.
- Značenje odgovara QAC zapisu (lema, POS, osobine) i kontekstu primjera. Mehanovićev prijevod koristi za izbor
  bosanske riječi i nijanse, ali glosa mora opisati upravo tu arapsku riječ.
- Imenica: osnovno značenje u odgovarajućem obliku ("znanje", "svjetovi", "Sveznajući", "čuvari"); particip
  aktivni/pasivni kao imenica ("oni koji se vraćaju", "Onaj koji zna"); glagolska imenica ("izvođenje", "izlazak").
  Ako riječ ima priključenu zamjenicu, uključi je ("tvoj naum", "njihov povratak", "iza njih"). Određeni član se ne prevodi.
- Glagol: sačuvaj lice, broj, vrijeme ili zapovjedni oblik, aktiv/pasiv: "izveo je", "izveli smo", "zahvaljujete",
  "čuvajte", "bit ćete vraćeni", "neka spuste" (jusiv s li-/bez), "da saznate" (subjunktiv s li-/an), "sigurno ću
  napuniti" (zakletveno la- + -nna). Priključena objektna zamjenica ulazi u glosu ("izvest će vas", "obratio im se").
  Prefiks wa-/fa- prevedi samo ako je dio prikazane riječi i nosi smisao ("i zahvaljujte", "pa da ga umnogostruči").
- Imperfekt bez sa-/sawfa prevedi prezentom osim kad kontekst jasno traži futur ("bit će" uz yakūnu u opisu Sudnjeg dana).
- Glagolske forme (II, IV, X…) prevedi njihovim značenjem (II/IV kauzativ, V/VI refleksiv/recipročnost, VII/VIII
  refleksiv, X traženje), uz kontekst.
- Bez tefsirskog objašnjenja. Allahova imena i svojstva velikim slovom kao kod Mehanovića ("Sveznajući", "Milostivi").
- Ista lema u različitim karticama smije dobiti različitu glosu samo ako se oblik stvarno razlikuje (lice, broj,
  zamjenica, prefiks).

Radi jednako pažljivo do kraja dijela; za svaku karticu stvarno pogledaj riječ u ajetu i prijevod. Pomoćne skripte
drži samo u scratchpadu. Ne mijenjaj druge fajlove.
