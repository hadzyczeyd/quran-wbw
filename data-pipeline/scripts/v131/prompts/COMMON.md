# Zajedničko za sve V13.1 agente

Radni folder: `C:\Users\haris\OneDrive\Desktop\wbw app\data-pipeline` (Windows; Bash s POSIX putanjama
`/c/Users/haris/OneDrive/Desktop/wbw app/data-pipeline`; Python preko `uv run`).
Aplikacija veže svaki arapski QAC morfološki segment za tačne tokene NEPROMIJENJENOG bosanskog prijevoda
Muhameda Mehanovića koji nose njegovo značenje/funkciju u cijelom ajetu.

Pravila (protokol `sources/NALOG_V13.1_tekst.txt` je autoritet):
- tokeni se nikad ne mijenjaju, ne dijele i ne spajaju; svaki segment zasebno; sadržajni segment → najuži dokazivi ekvivalent;
- Mehanovićeve čisto objašnjavajuće dopune ostaju inserted, ali token koji izražava dio vlastitog leksičkog značenja
  arapske riječi (npr. objekt/publika sadržani u samom glagolu: وَقَبَ → "razastre tmine", ٱنْحَرْ → "kurban kolji") se veže;
- bosanski prijedlog koji kodira padež imenice pripada toj imenici; ako zasebnog prijedloga nema, padežni oblik imenice nosi
  arapski prijedlog (bi- uz a'ūḏu → "Gospodaru"); ali pridjev/riječ koja samo slaže s drugom riječju ne nosi prijedlog;
- arapski prijedlog koji traži samo arapski glagol, a bosanski glagol uzima direktni objekat → unexpressed;
- DET al- normalno unexpressed s pojedinačnim razlogom; kopula/pomoćni glagol imenske rečenice bez arapskog segmenta → inserted;
- NEG token dobija NEG segment, glagol svoj uski token; negirani oblici ("nije/neće/nisu") se dijele ni-/ne- vs. ostatak
  `part` rasponima samo na stvarnoj unutrašnjoj granici koja pokriva cijeli token; ekspletivno "ne" (uz "dok", glagole straha) nije NEG;
- pomoćni glagol pripada glagolskom obliku koji gradi; REL → stvarni bosanski relativni izraz (ponovljeni "koji" istog REL-a u istom ajetu
  nose taj REL); povratne (resumptivne) zamjenice smiju biti unexpressed;
- relativna preoblika BEZ REL segmenta (jedinstveno pravilo za sve sure):
  * imenica/particip/pridjev (N/ADJ) preveden kao "onaj koji …", "oni koji su …", "onih koje …", "Onaj Koji …" → cijeli izraz,
    uključujući "onaj/oni/onih" i "koji/ko/koje", pripada tom N/ADJ segmentu (particip znači "onaj koji radi X");
  * glagol (V) u opisnoj rečenici kojoj Mehanović dodaje "koji/koja/koje" → glagol ide na svoj glagolski izraz, a "koji/koja/koje"
    ostaje inserted (glagol sam ne znači "koji");
- emfatičko la- uz inna, zakletveno la- u la-qad: unexpressed ako ga ne nosi zaseban token;
- subjektni PRON sufiks (55.9): ako ga nosi zaseban površinski token (eksplicitna zamjenica "oni"/"vi", pomoćni glagol "smo"/"ćete"),
  veže se na taj token; ako je lice samo u glagolskoj fleksiji, dozvoljeno je i vezati ga na glagolski token (fused) i dokumentovati
  da nije zasebno izražen — ali dosljedno unutar sure; nikad na semantički nepovezan token;
- restriktivno مَا/لَا … إِلَّا ("samo", "baš"): presudi iz konteksta nosi li restriktivni token i NEG; ne izmišljaj vezu;
- korelativno "i … i" / "i … a i" kojim Mehanović prevodi jedan arapski wa: svi tokeni korelacije nose taj wa
  (npr. 43:64 "i moj i vaš", 43:84 "i na nebu … a i na Zemlji"); ne ostavljaj prvo "i" inserted;
- negativna korelacija "ni … ni" za lā/mā … wa-lā/wa-mā: prvo "ni" ide na PRVI NEG segment (zajedno s "ne"/"ni-" ako ga ima),
  a drugo "ni" na wa + drugi NEG (dosljedno 93:3 "nije te ni napustio ni omrznuo");
- nema cross-word kontaminacije; jedan token smije nositi više segmenata (navedi ga za svaki);
- rizične veze (REL/funkcijske/one-to-many) trebaju konkretnu napomenu; engleski gloss je samo pomoć.

Izolacija: koristi samo navedene ulaze, protokol, `scripts/v131/MAPPING_SPEC.md`, `scripts/v131/review.py` i validatore.
Nikad ne otvaraj druge runove, Excel fajlove, web aplikaciju/bazu ni internet. Ne mijenjaj nijedan drugi fajl.
Batch-eve radi i provjeravaj JEDAN PO JEDAN (napiši batch → pokreni provjeru → tek nakon PASS sljedeći).
Ako si prekinut, nastavi od prvog batch-a koji nema PASS u manifestu.
