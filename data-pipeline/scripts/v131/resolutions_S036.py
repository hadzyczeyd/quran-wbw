# -*- coding: utf-8 -*-
"""CP4 razrješenja za suru 36."""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from resolve_common import P_AUX, P_NARROW, P_UNEXP, run  # noqa: E402

DA = P_NARROW + ": 'da' je bosanski uvod modalne dopune (inserted; dosljedno 48:15)"
NEK = P_NARROW + ": neodređenost imenice ('jedan', 'neko') je Mehanovićeva dopuna (inserted)"
CONC = "negativna konkordancija: 'ni-' u odričnoj zamjenici i 'ne-/ni-' glagola nose NEG (stvarne granice; dosljedno 46:13, 46:26)"
EMIN = "naglasni min (ikakav) uz negaciju → 'jedan' u 'nijedan' (granica ni|jedan)"
AUXP = "subjektni sufiks bez eksplicitne zamjenice nosi pomoćni glagol (dosljedno 44:41, 44:58, 48:4)"
WHOLE = "odrične zamjenice (niko, nijedan, nikome) se ne dijele: pripadaju imenici/min koju prevode, NEG nosi 'ne/ni-' glagola (dosljedno svim ranijim surama)"
DANAS = "deiktično al- u al-yawma → 'Danas' (fused s imenicom; dosljedno 40:16, 43:68)"

D = {
    "S036-A009-W009-S02": ("E1", P_NARROW + ": aġšaynā → 'koprenu stavili'; 'na oči' je Mehanovićeva dopuna"),
    "S036-A012-W008-S02": ("E2", "āṯār (ono što iza ostane) → relativna preoblika 'tragove koje iza … ostave;' (COMMON)"),
    "S036-A020-W005-S01": ("E1", NEK),
    "S036-A022-W002-S02": ("E2", P_UNEXP + ": -ya u idiomu mā liya ('Zašto') nije zasebno izražen"),
    "S036-A022-W004-S01": ("E2", DA),
    "S036-A023-W001-S02": ("E2", DA),
    "S036-A023-W008-S02": ("E1", NEK),
    "S036-A023-W010-S01": ("E1", "tuġni → '-će biti od koristi' ('od' je dio glagolskog idioma 'biti od koristi')"),
    "S036-A023-W013-S01": ("E1", "šayʾan u negaciji → 'ni … kakve'"),
    "S036-A026-W005-S02": ("E1", "layta → 'Kad … samo'; 'bi' pripada glagolu (potencijal)"),
    "S036-A026-W007-S01": ("E1", P_AUX + ": yaʿlamu → 'bi … znao'"),
    "S036-A026-W007-S02": ("E1", AUXP),
    "S036-A027-W001-S01": ("E2", "bi- → 'za' [0,2] u 'zašto' (stvarna granica za|što; dosljedno 45:35 'zato')"),
    "S036-A027-W001-S02": ("E2", "mā → 'što' [2,5] u 'zašto'"),
    "S036-A030-W002-S01": ("E1", P_UNEXP + ": ʿalā; pridjev 'ljudske' samo slaže (COMMON)"),
    "S036-A030-W004-S01": ("E1", WHOLE),
    "S036-A030-W006-S01": ("E1", WHOLE),
    "S036-A032-W006-S01": ("E1", P_AUX + ": muḥḍarūn → 'bit će … dovedeni.'"),
    "S036-A036-W005-S02": ("E2", P_UNEXP + ": -hā u kullahā nije zasebno izražen (dosljedno 48:28)"),
    "S036-A041-W001-S01": ("E1", "aditivno wa → 'i'"),
    "S036-A043-W004-S02": ("E1", WHOLE),
    "S036-A043-W005-S01": ("E1", WHOLE),
    "S036-A043-W009-S02": ("E1", AUXP),
    "S036-A046-W001-S02": ("E1", WHOLE),
    "S036-A046-W003-S01": ("E1", WHOLE),
    "S036-A047-W013-S02": ("E2", DA),
    "S036-A048-W006-S01": ("E1", P_UNEXP + ": kopulativno kāna nije zasebno izraženo (dosljedno 84:15)"),
    "S036-A049-W008-S02": ("E1", AUXP),
    "S036-A054-W001-S02": ("E2", DANAS),
    "S036-A054-W002-S01": ("E1", WHOLE),
    "S036-A054-W004-S01": ("E1", WHOLE),
    "S036-A059-W002-S01": ("E2", DANAS),
    "S036-A064-W001-S02": ("E2", "subjektni -ū imperativa razloženog na 'uđite … trpite' → oba glagolska tokena"),
    "S036-A064-W002-S01": ("E2", DANAS),
    "S036-A065-W001-S01": ("E2", DANAS),
    "S036-A066-W003-S03": ("E1", AUXP),
    "S036-A066-W006-S03": ("E1", AUXP),
    "S036-A066-W009-S02": ("E1", AUXP),
    "S036-A067-W005-S02": ("E2", "posvojno -him → 'su' (3. l. mn. u relativnoj dopuni); 'na kome' je Mehanovićeva dopuna"),
    "S036-A067-W007-S02": ("E1", AUXP),
    "S036-A067-W010-S02": ("E1", AUXP + "; zajednički 'bi'"),
    "S036-A069-W011-S01": ("E2", P_UNEXP + ": wa nije preveden veznikom (apozicija s crticom)"),
    "S036-A072-W003-S01": ("E2", P_UNEXP + ": fa nije preveden veznikom (crtica)"),
    "S036-A074-W001-S02": ("E1", "ittaḫaḏū → 'prihvataju'; 'kao' kodira drugi objekat i pripada imenici"),
    "S036-A074-W005-S01": ("E1", "ālihatan → 'kao bogove'"),
    "S036-A074-W007-S01": ("E1", P_AUX + ": yunṣarūn → 'bi … potpomognuti bili;'"),
    "S036-A076-W001-S02": ("E1", "zabranjujuće lā uz jusiv 3. lica → 'nek … ne'"),
    "S036-A076-W002-S01": ("E1", "yaḥzun → 'žaloste'"),
    "S036-A078-W005-S01": ("E1", "maṣdar ḫalq preoblikovan u rečenicu 'kako je stvoren,' (dosljedno 49:17)"),
}

if __name__ == "__main__":
    run("S036_Ja-Sin", D)
