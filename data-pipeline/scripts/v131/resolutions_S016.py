# -*- coding: utf-8 -*-
"""CP4 razrješenja za suru 16."""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from resolve_common import P_NARROW, P_UNEXP, run  # noqa: E402

INS = P_NARROW + "; Mehanovićeva objašnjavajuća dopuna/pojačivač bez arapskog segmenta ostaje inserted (COMMON)"
OBJV = "objekat sadržan u značenju glagola pripada glagolskom izrazu (dosljedno 17:7, 18:86)"
RECT = P_UNEXP + ": prijedlog traži samo arapska rekcija; bosanski glagol uzima direktni objekat (COMMON)"
BIV = P_UNEXP + ": bi- uz jāʾa/atā sadržan je u bosanskom glagolu 'dovesti/donijeti' (COMMON)"
PART = P_UNEXP + ": partitivni/objašnjavajući min uz imenicu u jednini nije izražen (COMMON)"
REPP = "ponovljeni bosanski prijedlog/veznik ispred koordiniranog člana nosi isti arapski segment (COMMON: 'na na')"
REPDA = "namjerni li-/an → 'da'; ponovljeno 'da' za koordinirani glagol nosi isti segment, glagol samo svoj token (COMMON)"
LAALLA = "laʿalla → 'da'; 'bi/biste' nose -kum/-hum i -ūna te glagol (COMMON)"
DETY = "DET al- u al-yawma ('danas/sada') nije istighrāq → UNEXPRESSED (COMMON)"
YAWM = "yawm + rečenica → 'na Dan kada' (s 'kada', COMMON)"
SECAUX = "sufiks drugog koordiniranog glagola → zajednički pomoćni (COMMON)"
DOUBLET = "Mehanovićev dublet jednog glagola ('prisjećaju i pouku uzimaju') je jedan izraz; sufiks fused na cijeli dublet"
NAFS = "anfus → povratno-naglasno 'sami sebi' (nafs nosi i 'sebi' i 'sami', dosljedno 39:15, 51:21)"
HUM = P_UNEXP + ": samostalno hum bez zamjenice i pomoćnog glagola (dosljedno 42:39, 51:18, 107:6)"
POSS = P_UNEXP + ": posvojni -hum uz ajr nije zasebno izražen"
NEMA = "'nema' = ne|ma: negacija 'ne-', posjedovni/glagolski dio '-ma' (stvarna granica, dosljedno 67:20)"
OMIT = "SOURCE_TRANSLATION_OMISSION: izvorni Mehanovićev tekst ne prevodi stavak „wa-qalbuhu muṭmaʾinnun bi-l-īmāni“ (a srce mu je smireno u vjerovanju) u 16:106; veza se ne izmišlja — "

D = {
    "S016-A001-W009-S01": ("E1", OBJV + ": 'Mu pridružuju!'"),
    "S016-A003-W007-S01": ("E1", OBJV + ": 'Mu pridružuju.'"),
    "S016-A006-W005-S01": ("E1", OBJV + ": 'je … vraćate'"),
    "S016-A006-W007-S01": ("E1", OBJV + ": 'je … izgonite.'"),
    "S016-A007-W010-S02": ("E2", "idiom šiqq al-anfus → 'velike muke' (oba člana idioma dijele izraz)"),
    "S016-A009-W003-S01": ("E2", "qaṣd 'usmjerenost ka' → 'vodi … Pravi' ('Ka Allahu vodi … Pravi put')"),
    "S016-A013-W013-S02": ("E2", DOUBLET),
    "S016-A014-W005-S01": ("E2", REPDA),
    "S016-A014-W009-S02": ("E2", REPDA),
    "S016-A014-W016-S01": ("E1", RECT),
    "S016-A014-W020-S02": ("E1", LAALLA),
    "S016-A015-W007-S01": ("E1", RECT),
    "S016-A017-W007-S02": ("E2", DOUBLET),
    "S016-A023-W008-S01": ("E2", "jedan wa preveden korelacijom 'i … a i'; svi tokeni korelacije nose taj wa (dosljedno 43:84)"),
    "S016-A024-W003-S01": ("E1", RECT),
    "S016-A025-W014-S01": ("E2", "relativni mā → 'koji'; 'teret' pripada glagolu wazara"),
    "S016-A025-W015-S01": ("E2", OBJV + ": wizr sadržan u yazirūna → 'teret … će nositi!'"),
    "S016-A027-W018-S01": ("E1", DETY),
    "S016-A033-W004-S01": ("E2", REPDA),
    "S016-A033-W008-S01": ("E2", REPDA),
    "S016-A033-W021-S01": ("E1", NAFS),
    "S016-A034-W006-S01": ("E1", RECT),
    "S016-A034-W007-S01": ("E1", "REL → stvarni bosanski relativni izraz 'ono čemu' (COMMON)"),
    "S016-A036-W003-S01": ("E2", "fī kulli → dativ 'svakom'; padež upravljane imenice kull nosi fī"),
    "S016-A037-W014-S01": ("E1", "'niko' nosi partitivni min (genitiv/neodređenost, COMMON); nāṣirīn → 'će … pomoći.'"),
    "S016-A038-W012-S01": ("E1", "waʿdan ʿalayhi (obećanje koje On ispunjava) → posvojno 'Njegovo' (fused s -hi)"),
    "S016-A038-W013-S01": ("E1", "ḥaqqan → 'doista će se ispuniti,'"),
    "S016-A040-W005-S03": ("E2", "resumptivni -hu → izraz na koji se odnosi ('nešto', COMMON)"),
    "S016-A041-W016-S01": ("E1", "law željnog uslova → 'kad … samo' (kad bi samo)"),
    "S016-A043-W002-S01": ("E1", INS + ": 'kao poslanike'"),
    "S016-A044-W011-S02": ("E1", LAALLA),
    "S016-A045-W001-S03": ("E1", "amina → 'su sigurni'; ekspletivno 'ne-' u 'neće' pripada futurskom obliku glagola"),
    "S016-A045-W005-S01": ("E2", REPDA),
    "S016-A045-W006-S01": ("E1", "yaḫsifa → 'neće … utjerati,' (ekspletivno 'ne' nije arapski NEG; cijeli futurski oblik)"),
    "S016-A045-W008-S01": ("E1", RECT),
    "S016-A045-W011-S01": ({"targets_from": "E1", "drop": ["da"]}, "yaʾtiya → 'neće, … doći,'; ponovljeno 'da' nosi an (COMMON)"),
    "S016-A046-W002-S01": ("E1", "subjunktiv koordiniran s an iz 16:45 → 'da … neće … kazniti,' ('da' gradi oblik u ovom ajetu, dosljedno 18:4)"),
    "S016-A046-W007-S02": ("E1", "fa-mā hum bi-muʿjizīna → 'pa da … -će umaći,'; 'da' ide uz glagolski izraz (COMMON fa)"),
    "S016-A047-W002-S01": ("E1", "subjunktiv koordiniran s an iz 16:45 → 'da … neće, … kažnjavati?' (dosljedno 18:4)"),
    "S016-A047-W003-S01": ({"targets_from": "E2", "drop": ["su"]}, "ʿalā stanja → 'dok … u'; kopula 'su' bez segmenta ostaje inserted (COMMON)"),
    "S016-A047-W004-S01": ("E2", "taḫawwuf → 'strahu,'; 'u' nosi ʿalā"),
    "S016-A048-W007-S01": ("E1", PART),
    "S016-A049-W006-S02": ("E1", P_UNEXP + ": drugi mā nije ponovljen; obuhvatnost nosi prvo 'sve'"),
    "S016-A049-W009-S01": ("E1", PART),
    "S016-A052-W003-S01": ("E2", REPP),
    "S016-A052-W005-S03": ("E2", REPP),
    "S016-A052-W006-S02": ("E1", "posvojni li- preoblikovan u 'Njemu treba' (COMMON: li- → glagol je vezan)"),
    "S016-A052-W007-S02": ("E1", "dīn → 'poslušan biti.'"),
    "S016-A052-W011-S01": ("E1", "modalno 'da' u perifrazi ide uz glagol (COMMON)"),
    "S016-A053-W010-S01": ("E1", "DET al- nije istighrāq → UNEXPRESSED; neodređenik 'kakva' ide na imenicu (COMMON)"),
    "S016-A053-W010-S02": ("E1", "neodređenik 'kakva' → imenica (COMMON)"),
    "S016-A055-W005-S02": ("E2", "FUT sawfa → 'ćete' (COMMON); 'zbilja,' je pojačivač (inserted)"),
    "S016-A058-W007-S01": ("E1", "muswadd → 'smrkne,'; 'se' nosi ẓalla"),
    "S016-A059-W009-S02": ("E1", "deliberativno 'da' u perifrazi ide uz glagol (COMMON)"),
    "S016-A059-W013-S01": ("E1", "deliberativno 'da' u perifrazi ide uz glagol (COMMON)"),
    "S016-A061-W023-S02": ("E2", SECAUX + ": 'mogu'"),
    "S016-A062-W017-S01": ("E1", "kopula uz particip: 'će … biti' i 'u nju' bez segmenta (inserted, COMMON)"),
    "S016-A063-W014-S01": ("E1", DETY),
    "S016-A066-W007-S01": ("E2", "partitivni min u mimmā nije izražen ('ono što')"),
    "S016-A066-W008-S01": ("E2", "fī buṭūnihi → 'iz … utrobe' (Mehanović daje izvor)"),
    "S016-A066-W010-S01": ("E1", "min bayni → 'između' (fused s bayn, kao min dūni); 'što nastaje' je dopuna (inserted)"),
    "S016-A068-W006-S01": ("E1", "ittaḫaḏa (VIII, 'uzeti sebi') → 'Pravi sebi'"),
    "S016-A073-W010-S01": ("E2", REPP),
    "S016-A073-W012-S03": ("E2", REPP),
    "S016-A074-W001-S02": ("E2", "lā zabrane → 'ne'; 'ništa' nosi vlastiti segment amṯāl (COMMON)"),
    "S016-A074-W004-S02": ("E2", "al-amṯāla (objekat) → 'ništa'; poređenje nosi ḍaraba"),
    "S016-A075-W006-S01": ("E2", NEMA),
    "S016-A075-W007-S01": ("E2", NEMA),
    "S016-A076-W019-S01": ("E1", BIV),
    "S016-A078-W007-S01": ("E1", "ḥāl bez veznika → 'dok … znate,' ('dok' izražava stanje glagolske rečenice)"),
    "S016-A078-W014-S01": ("E1", LAALLA),
    "S016-A081-W024-S01": ("E1", LAALLA),
    "S016-A084-W001-S02": ("E1", YAWM),
    "S016-A085-W007-S01": ("E1", "yuḫaffafu → 'olakšanja … -će imati.' (drugi koordinirani glagol nosi samo svoj token)"),
    "S016-A086-W006-S01": ("E2", "granica tokena 'će:\"Gospodaru' ide prije navodnika: 'će:' | '\"Gospodaru'"),
    "S016-A086-W006-S02": ("E2", "subjektni sufiks → pomoćni 'će:' (granica prije navodnika)"),
    "S016-A086-W007-S01": ("E2", "rabb → '\"Gospodaru' (granica prije navodnika)"),
    "S016-A089-W001-S02": ("E1", YAWM),
    "S016-A089-W011-S01": ("E1", BIV),
    "S016-A090-W016-S01": ("E2", "laʿalla 'ne … li'; glagol uključuje 'bi' (COMMON)"),
    "S016-A091-W012-S02": ("E2", SECAUX + ": 'ste'"),
    "S016-A092-W007-S01": ("E2", "min baʿdi → 'kad … već' (vremensko 'nakon')"),
    "S016-A092-W008-S01": ("E2", OBJV + ": 'bi je … bila čvrsto oprela,'"),
    "S016-A092-W017-S01": ("E2", "zamjenica razdvajanja hiya → kopula 'je' (COMMON)"),
    "S016-A094-W006-S01": ("E1", "fa sababiyya → 'pa'; 'da' ide uz glagol (COMMON)"),
    "S016-A094-W006-S02": ("E1", "fa sababiyya: 'da posrne' (COMMON)"),
    "S016-A094-W009-S01": ("E2", "masdar ṯubūt → 'stabilna bila,'; 'je' nosi subjektni -hā"),
    "S016-A094-W009-S02": ("E2", "subjektni -hā bez zamjenice → pomoćni 'je' (COMMON)"),
    "S016-A094-W010-S02": ("E1", "koordinirani subjunktiv pod fa → 'da … iskusite' (COMMON)"),
    "S016-A095-W003-S02": ("E2", "ʿahd → 'obavezu'; genitivni odnos nosi 'datu Allahu'"),
    "S016-A095-W004-S01": ("E2", "genitiv ʿahdi llāhi → 'datu Allahu'"),
    "S016-A095-W006-S01": ("E1", "pridjev qalīl → relativna preoblika 'što malo'"),
    "S016-A096-W011-S02": ("E1", POSS),
    "S016-A097-W014-S02": ("E1", POSS),
    "S016-A099-W002-S01": ({"targets_from": "E2", "add": ["nikakve"]}, NEMA + "; 'nikakve' bez vlastitog segmenta → negacija (dosljedno 39:28)"),
    "S016-A099-W003-S01": ("E2", NEMA),
    "S016-A099-W004-S01": ("E1", "sulṭān → 'moći'; 'nikakve' nosi negacija"),
    "S016-A100-W007-S01": ("E1", HUM),
    "S016-A102-W003-S01": ("E1", INS + ": 'Džibril,' (Mehanovićevo imenovanje)"),
    "S016-A103-W008-S01": ("E2", "lisān → 'Jezik'; drugo 'jezik' ide uz aʿjamī"),
    "S016-A103-W012-S01": ("E2", "Mehanović eksplicira imenicu sadržanu u pridjevu → 'jezik … nearapa,' (dosljedno 18:40)"),
    "S016-A106-W006-S01": ("E2", OBJV + ": 'je u Njega vjerovao'"),
    "S016-A106-W007-S01": ("E2", "illā → isključenje 'ne i'"),
    "S016-A107-W002-S01": ("E1", "uzročno bi- → 'što' (dosljedno 18:73); 'zato' nosi ḏālika"),
    "S016-A110-W011-S02": ("E2", SECAUX + ": 'su'"),
    "S016-A110-W012-S03": ("E2", SECAUX + ": 'su'"),
    "S016-A111-W001-S01": ("E1", YAWM + "; ponovljeni relativ 'u kome' odnosi se na isti Dan"),
    "S016-A112-W009-S01": ("E1", "rizq → 'hrana'"),
    "S016-A112-W010-S01": ("E1", "raġad 'obilno i ugodno' → 'u izobilju … ukusna'"),
    "S016-A112-W024-S02": ({"targets_from": "E1", "drop": ["stanovnici", "njegovi"], "add": ["su"]},
                           "kāna + imperfekt: -ūna ide na zajednički 'su' (COMMON); 'stanovnici njegovi' je Mehanovićev subjekat (inserted, dosljedno 18:59)"),
    "S016-A112-B044": ("INS", "'stanovnici' je Mehanovićev eksplicitni subjekat bez arapskog segmenta (COMMON)"),
    "S016-A115-W020-S01": ("E2", "Allāh → Mehanovićevo 'Gospodar tvoj' (cijeli izraz)"),
    "S016-A116-W004-S01": ("E1", P_UNEXP + ": taṣifu nije zasebno izražen; 'govorite' nosi taqūlū"),
    "S016-A117-W003-S01": ("E1", INS + ": 'onda'"),
    "S016-A118-W014-S01": ("E1", NAFS),
    "S016-A121-W004-S03": ("E2", "objektni sufiks drugog koordiniranog glagola → zajednička zamjenica 'njega' (COMMON)"),
    "S016-A125-W005-S01": ("E2", "jedan bi- pred koordiniranim imenicama → 'mudro' i instrumental 'savjetom'"),
    "S016-A127-W003-S01": ("E2", "kopula uz pridjev: 'ćeš' nosi oblik, 'biti' inserted (COMMON)"),
    "S016-A127-W005-S01": ("E2", "bi- sredstva → 'uz … pomoć.'"),
    "S016-A128-W007-S01": ("E1", HUM),
    # Mehanovićev propust (tekst se ne mijenja; dokumentovano u cp4/DOCUMENTED_EXCEPTIONS.json)
    "S016-A106-W010-S01": ("UNEXP", OMIT + "wa stanja"),
    "S016-A106-W010-S02": ("UNEXP", OMIT + "qalb"),
    "S016-A106-W010-S03": ("UNEXP", OMIT + "-hu"),
    "S016-A106-W011-S01": ("UNEXP", OMIT + "muṭmaʾinn"),
    "S016-A106-W012-S01": ("UNEXP", OMIT + "bi-"),
    "S016-A106-W012-S02": ("UNEXP", OMIT + "al-"),
    "S016-A106-W012-S03": ("UNEXP", OMIT + "īmān"),
}

if __name__ == "__main__":
    run("S016_En-Nahl", D)
