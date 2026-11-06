# -*- coding: utf-8 -*-
"""CP4 razrješenja za suru 12."""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from resolve_common import P_NARROW, P_UNEXP, run  # noqa: E402

INS = P_NARROW + "; Mehanovićeva objašnjavajuća dopuna/pojačivač bez arapskog segmenta ostaje inserted (COMMON)"
OBJV = "objekat sadržan u značenju glagola pripada glagolskom izrazu (dosljedno 16:1, 11:20)"
RECT = P_UNEXP + ": prijedlog traži samo arapska rekcija; bosanski glagol uzima dativ/direktni objekat (COMMON)"
INNA0 = "ime inna/laʿalla bez eksplicitne zamjenice → pomoćni koji nosi lice ili fused na glagol (dosljedno 11:7)"
DAV = "'da/kako' dopune bez arapskog veznika ide uz glagol (perifraza/stanje, dosljedno 16:59, 16:78)"
NAFS = "nafs u idiomu rāwada ʿan nafsihi sadržan je u 'zavoditi' (fused s glagolom)"
AUXV = "pomoćni glagol pripada glagolskom obliku koji gradi (COMMON)"
SEVEN = INS + ": ponovljeni broj 'sedam'"
RESUMP = "resumptivna zamjenica → padežni oblik relativnog izraza (COMMON)"
LIV = "posvojni li- preoblikovan u glagol 'pripada' (COMMON); 'Allahu/Njemu' nosi imenica/zamjenica"
LIPOSS = P_UNEXP + ": posvojni li- preoblikovan u posvojnu zamjenicu (pripadnost nosi -kum/-hu)"
REPP = "ponovljeni bosanski prijedlog/veznik ispred koordiniranog člana nosi isti arapski segment (COMMON: 'na na')"
REPDA = "an → 'da'; ponovljeno 'da' pred koordiniranim glagolom nosi isti an; ekspletivno 'ne' u 'neće' ide glagolu (dosljedno 16:45)"
COORDPRON = "sufiks koordiniranog glagola → zajednička eksplicitna zamjenica (COMMON)"
DOUBLET = "Mehanović daje dvostruki prijevod ('Sve znaniji od znanijeg ima, a Sveznajući je iznad svakog'): oba dijela pripadaju istom segmentu"

D = {
    "S012-A002-W001-S02": ("E2", INNA0),
    "S012-A004-W006-S02": ("E2", INNA0 + ": 'sam'"),
    "S012-A004-W013-S01": ("E2", AUXV + "; 'u snu' je dopuna (inserted)"),
    "S012-A004-W015-S01": ("E1", DAV + ": 'kako … se pokloniše.\"'"),
    "S012-A009-W008-S01": ("E2", "wajh u idiomu sadržan u 'okrenuti,' (fused)"),
    "S012-A010-W016-S01": ("E1", OBJV + ": 'nešto učiniti,'"),
    "S012-A011-W004-S01": ("E1", "idiom mā laka → 'zašto' (oba člana idioma dijele izraz)"),
    "S012-A012-W004-S01": ("E1", DAV + ": 'da se zabavi'"),
    "S012-A013-W002-S02": ("E2", INNA0 + ": 'mi,'"),
    "S012-A017-W003-S02": ("E2", INNA0 + ": 'smo'"),
    "S012-A017-W005-S01": ("E1", DAV + ": 'da se nadmećemo,'"),
    "S012-A021-W013-S01": ("E1", "nattaḫiḏahu → 'posiniti!\"'; 'možemo' nosi ʿasā"),
    "S012-A023-W019-S01": ("E2", "idiom aḥsana maṯwāya → 'lijepo pazi' (maṯwā fused s glagolom)"),
    "S012-A025-W015-S01": ("E1", "arāda → 'je htio'"),
    "S012-A025-W017-S01": ("E1", "sūʾ kao objekat namjere → 'zlo učiniti\",'"),
    "S012-A026-W005-S01": ("E2", NAFS),
    "S012-A028-W004-S01": ("E1", DAV + ": 'da je … razderana,'"),
    "S012-A028-W010-S02": ("E2", "-kunna → 'vaših - ženskih' (crtica unutar izraza pripada izrazu, COMMON)"),
    "S012-A030-W010-S01": ("E2", NAFS),
    "S012-A030-W012-S01": ("E2", "šaġafahā ḥubban → 'u njega se ludo zaljubila!' ('se' dio povratnog glagola)"),
    "S012-A030-W012-S02": ("E2", "objektni -hā preoblikovan u subjekat 'zaljubila!' (fused, dosljedno 18:86)"),
    "S012-A032-W004-S01": ("E1", AUXV + ": 'ste … korile\",'"),
    "S012-A032-W009-S01": ("E2", NAFS),
    "S012-A035-W009-S02": ("E1", DAV + ": 'da … smjeste u tamnicu.'"),
    "S012-A036-W009-S01": ("E1", DAV + ": 'da cijedim'"),
    "S012-A036-W015-S01": ("E1", DAV + ": '\"kako … nosim'"),
    "S012-A036-W024-S02": ("E2", INNA0 + ": fused 'vidimo'"),
    "S012-A037-W002-S01": ("E2", "lā → 'ne-' u 'neće'; 'Ništa' nosi vlastiti segment ṭaʿām (COMMON)"),
    "S012-A037-W004-S01": ("E2", "neodređeno ṭaʿām pod negacijom → '\"Ništa od onoga' (negativna zamjenica na imenici, COMMON)"),
    "S012-A037-W008-S02": ("E2", "taʾwīl → upitno 'što'"),
    "S012-A037-W011-S01": ("E2", "an yaʾtiyakumā → 'ćete dobiti\",'"),
    "S012-A037-W011-S02": ("E2", "objektni -kumā preoblikovan u subjekat → pomoćni 'ćete'"),
    "S012-A040-W007-S01": ("E1", AUXV + ": 'ste … nadjenuli'"),
    "S012-A040-W019-S01": ("E2", LIV),
    "S012-A042-W002-S02": ("E2", "allaḏī → 'onome … kojeg'"),
    "S012-A042-W004-S02": ("E2", RESUMP + ": 'za kojeg'"),
    "S012-A043-W003-S02": ("E2", INNA0 + ": 'sam'"),
    "S012-A043-W008-S01": ("E1", DAV + ": 'kako … pojede'"),
    "S012-A043-W014-S02": ("E1", SEVEN),
    "S012-A045-W007-S01": ("E2", INS + ": 'toliko'"),
    "S012-A046-W015-S02": ("E1", SEVEN),
    "S012-A046-W017-S01": ("E2", "laʿalla → 'da' (COMMON); 'pa' bez segmenta (inserted)"),
    "S012-A046-W017-S02": ("E2", INNA0 + ": fused 'vratim'"),
    "S012-A047-W008-S04": ("E2", RESUMP + ": 'ono'"),
    "S012-A048-W005-S01": ("E1", P_UNEXP + ": ḏālika u min baʿdi ḏālika nije izražen ('poslije' nosi baʿd)"),
    "S012-A050-W015-S01": ("E1", "DET al- nije istighrāq → UNEXPRESSED; pokazno 'onim' inserted (COMMON)"),
    "S012-A051-W008-S01": ("E2", NAFS),
    "S012-A051-W026-S01": ("E2", NAFS),
    "S012-A054-W005-S01": ("E1", "astaḫliṣ (uzeti isključivo za sebe) → 'uzet ću … svitu\",'"),
    "S012-A054-W006-S02": ("E1", "nafs u li-nafsī → povratno-posvojno 'svoju'"),
    "S012-A059-W007-S01": ("E1", LIPOSS),
    "S012-A059-W012-S02": ("E2", INNA0 + ": fused 'dajem'"),
    "S012-A062-W013-S02": ("E2", "ime laʿalla -hum → 'će' (COMMON)"),
    "S012-A063-W013-S01": ("E1", DAV + ": 'da bismo dobili mjeru'"),
    "S012-A064-W003-S01": ("E1", DAV + ": deliberativno 'da … povjerim'"),
    "S012-A065-W006-S01": ("E1", DAV + ": 'da su … vraćene'"),
    "S012-A065-W022-S01": ("E1", "genitiv baʿīr (tovar kamile) → opisna rečenica 'koji kamila može ponijeti;'"),
    "S012-A067-W022-S01": ("E2", LIV),
    "S012-A068-W003-S01": ("E1", P_UNEXP + ": min u min ḥayṯu nije izražen (kao min qabli/baʿdi)"),
    "S012-A068-W004-S01": ("E1", "ḥayṯu → 'onako kako'"),
    "S012-A068-W009-S01": ("E2", "kāna + imperfekt: '-je' u 'nije' nosi kāna; glagol samo 'pomoglo' (COMMON)"),
    "S012-A068-W010-S01": ("E2", RECT),
    "S012-A068-W011-S01": ("E2", P_UNEXP + ": min Allāhi nije zasebno izražen; 'da budu pošteđeni' je dopuna (inserted)"),
    "S012-A068-W018-S01": ("E1", P_UNEXP + ": nafs (u duši) nije zasebno izražen ('želja Jakubova')"),
    "S012-A071-W002-S03": ("E1", COORDPRON + ": 'Oni'"),
    "S012-A072-W009-S01": ("E1", "genitiv baʿīr (tovar kamile) → opisna rečenica 'koji kamila može ponijeti.' (dosljedno 12:65)"),
    "S012-A076-W029-S01": ("E2", P_UNEXP + ": wa na početku rečenice nema bosanskog veznika"),
    "S012-A076-W029-S02": ("E1", DOUBLET + ": fawqa → 'od … iznad'"),
    "S012-A076-W030-S01": ("E1", DOUBLET + ": kull → 'Sve … svakog.'"),
    "S012-A076-W033-S01": ("E1", DOUBLET + ": ʿalīm → 'znaniji … Sveznajući'"),
    "S012-A077-W007-S01": ("E1", LIPOSS),
    "S012-A077-W017-S01": ("E1", "qāla (u sebi) → 'pomisli u sebi,'"),
    "S012-A080-W005-S01": ("E1", DAV + ": ḥāl najiyyan → 'da se posavjetuju.'"),
    "S012-A080-W013-S01": ("E2", AUXV + ": 'ste se … zakleli,'"),
    "S012-A085-W010-S01": ("E2", "drugi takūna nosi samo svoj token; kāna fused s predikatom 'umrijeti!\"' (COMMON)"),
    "S012-A086-W008-S02": ({"targets_from": "E1", "add": ["mi"]}, "aʿlamu → 'mi … da znam' (1. l. jd. preoblikovano u 'mi'; 'da' ide glagolu)"),
    "S012-A086-W009-S01": ("E2", "min Allāhi → preoblika 'je dao' (izvor znanja)"),
    "S012-A089-W002-S01": ("E2", "upitni hal → '\"A … li\",'"),
    "S012-A092-W002-S01": ("E1", "lā negacije vrste → egzistencijalno 'neće biti' (dosljedno 23:101)"),
    "S012-A094-W007-S01": ("E1", P_UNEXP + ": emfatičko la- dijeli pojačivač s inna → UNEXPRESSED (dosljedno 11:31, 11:79)"),
    "S012-A094-W011-S01": ("E2", "an → 'da'"),
    "S012-A094-W012-S01": ("E2", "tufannidūni → 'recite … omatuhio.\"'"),
    "S012-A099-W014-S01": ("E1", INS + ": 'od svega,'"),
    "S012-A100-W007-S01": ("E2", "sujjadan sadržan u 'nakloniše,' (fused); 'se' nosi glagol"),
    "S012-A100-W036-S02": ("UNEXP", P_UNEXP + ": ponovljeni bayna nije ponovljen; jedno 'između' nosi prvi (dosljedno 18:78)"),
    "S012-A101-W006-S03": ("E1", COORDPRON + ": 'Ti'"),
    "S012-A101-W015-S01": ("E2", REPP),
    "S012-A101-W017-S03": ("E2", REPP),
    "S012-A102-W010-S01": ("E2", "iḏ → 'kada'"),
    "S012-A102-W013-S01": ("E2", "wa stanja → 'i kada' (Mehanović okolnost daje vremenskom rečenicom)"),
    "S012-A102-W014-S01": ("E1", AUXV + ": 'su spletke smislili.'"),
    "S012-A105-W001-S02": ("E2", "kaʾayyin → 'koliko'; 'ima' bez segmenta (inserted)"),
    "S012-A105-W004-S01": ("E2", REPP),
    "S012-A105-W006-S03": ("E2", REPP),
    "S012-A107-W002-S01": ("E2", REPDA),
    "S012-A107-W003-S01": ("E2", REPDA),
    "S012-A107-W009-S01": ("E2", REPDA),
    "S012-A109-W010-S01": ("E1", "ahl → 'koji su … bili' (iz naselja)"),
    "S012-A109-W011-S02": ("E1", "qurā → 'naseljenih mjesta'"),
    "S012-A110-W003-S01": ("E2", INS + ": 'gotovo'"),
}

if __name__ == "__main__":
    run("S012_Jusuf", D)
