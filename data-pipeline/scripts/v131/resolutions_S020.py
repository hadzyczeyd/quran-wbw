# -*- coding: utf-8 -*-
"""CP4 razrješenja za suru 20."""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from resolve_common import P_AUX, P_GOV, P_NARROW, P_UNEXP, run  # noqa: E402

COORDV = "drugi koordinirani glagol nosi samo svoj token; zajednički pomoćni ostaje uz prvi (dosljedno 30:9, 15:19, 19:30)"
MI = "subjektni sufiks → samo eksplicitna zamjenica; pomoćni pripada glagolskom obliku (COMMON, dosljedno 23:12, 15:16)"
SEPPRON = "ime inna → eksplicitna zamjenica; samostalna zamjenica → kopula koja nosi njeno lice (dosljedno 15:49, 26:44)"
AFTERINNA = "iza inna zamjenica nosi ime; sufiks glagola → pomoćni, a bez pomoćnog fused na glagol (COMMON, dosljedno 70:6, 19:83)"
BI = P_UNEXP + ": bi- uz ǧāʾa/atā/asrā/ḏahaba; bosanski glagol uzima direktni objekat (dosljedno 26:30, 15:7)"
INS = P_NARROW + "; pojačivač/neodređenost/dopuna bez arapskog segmenta ostaje inserted (COMMON)"
FADA = "fa sababiyya → 'pa'; 'da' konjunktiva pripada glagolu (dosljedno 26:102)"
LALLA = "laʿalla bez zamjenice → 'da'; sufiks → 'bi', glagol 'bi …' (dosljedno 30:46, 35:12)"
NEBILI = "laʿallahu … 'ne bi li': laʿalla → 'ne … li', -hu i glagol → 'bi' (dosljedno 46:27, 30:41)"
SUBJ = P_UNEXP + ": prijedlog li- s korisnikom preoblikovanim u subjekat nije izražen (dosljedno 19:62, 26:155)"
OMIT = ("SOURCE_TRANSLATION_OMISSION: izvorni Mehanovićev tekst 20:129 („I da nije prije izrečene riječi Gospodara tvoga, kazna bi već bila "
        "neminovna.“) ne sadrži „wa-ajalun musammā“ (i roka određenog); tekst se ne mijenja, veza se ne izmišlja (dosljedno 60:12)")

D = {
    "S020-A010-W004-S02": ("E1", COORDV),
    "S020-A010-W006-S01": ("E1", INS + ": 'tu'"),
    "S020-A010-W013-S02": ("E2", INS + ": 'nekakvu'"),
    "S020-A012-W001-S02": ("E1", SEPPRON),
    "S020-A012-W002-S01": ("E1", SEPPRON),
    "S020-A014-W001-S02": ("E1", SEPPRON),
    "S020-A014-W002-S01": ("E1", SEPPRON),
    "S020-A016-W001-S01": ("E1", "fa → 'zato'; 'I' bez arapskog segmenta (inserted)"),
    "S020-A016-W001-S02": ("E1", "zabrana lā → 'ne'"),
    "S020-A016-W002-S01": ("E1", P_AUX + ": jusiv 'neka … odvrati'"),
    "S020-A016-W003-S02": ("E2", "-hā → 'njeg'; 'u' pripada Mehanovićevoj dopuni 'vjerovanja u'"),
    "S020-A016-W010-S01": ("E2", FADA),
    "S020-A016-W010-S02": ("E2", FADA),
    "S020-A021-W005-S02": ("E1", P_AUX + "; eksplicitno 'Mi' nosi lice prefiksa (COMMON)"),
    "S020-A021-W006-S01": ("E1", "sīra → Mehanovićeva relativna preoblika 'u ono što je … bila.'"),
    "S020-A021-W006-S02": ("E1", "-hā → subjekat preoblike 'bila.'"),
    "S020-A022-W005-S01": ("E1", "taxruj → 'će se ukazati'; ponovljeno 'ruka' bez segmenta (inserted)"),
    "S020-A028-W001-S02": ("E1", "subjektni sufiks bez zamjenice → pomoćni 'bi' (COMMON 55.9)"),
    "S020-A035-W002-S01": ("E1", "kāna bez pomoćnog → fused na glagol 'uviđaš.\"' (COMMON)"),
    "S020-A035-W002-S02": ("E1", AFTERINNA),
    "S020-A035-W004-S01": ("E1", "baṣīr → glagolsko 'uviđaš.\"'; 'sve' je pojačivač (inserted)"),
    "S020-A037-W002-S02": ("E2", "subjektni sufiks → pomoćni 'smo'; 'Svoju' je dopuna (inserted)"),
    "S020-A040-W004-S02": ("E1", COORDV),
    "S020-A040-W010-S03": ("E2", MI),
    "S020-A040-W015-S01": ("E1", "ʿayn u idiomu qurrat al-ʿayn → 'se raduje'"),
    "S020-A040-W018-S03": ("E2", MI),
    "S020-A040-W020-S03": ("E2", MI),
    "S020-A040-W025-S03": ("E2", MI),
    "S020-A044-W005-S01": ("E2", NEBILI),
    "S020-A044-W005-S02": ("E2", NEBILI),
    "S020-A044-W006-S01": ("E2", NEBILI),
    "S020-A047-W006-S02": ("E2", INS + ": 'da idu'"),
    "S020-A047-W014-S01": ("E1", BI),
    "S020-A051-W003-S01": ("E1", "bāl u idiomu mā bālu → 'je'"),
    "S020-A051-W004-S02": ("E1", P_GOV + ": 's narodima'"),
    "S020-A056-W002-S02": ("E2", MI),
    "S020-A058-W002-S01": ("E1", BI),
    "S020-A061-W010-S01": ("E2", FADA),
    "S020-A061-W010-S02": ("E2", FADA + "; eksplicitno 'On' nosi lice prefiksa"),
    "S020-A062-W004-S02": ("E2", "asarra → 'tiho su'; 'šaptali.' nosi najwā"),
    "S020-A063-W012-S01": ("E1", BI),
    "S020-A065-W005-S01": ("E2", "tulqiya → 'hoćeš ti … baciti?\"' ('baciti' zajedničko za oba člana alternative)"),
    "S020-A068-W004-S02": ("E1", SEPPRON),
    "S020-A068-W005-S01": ("E1", SEPPRON),
    "S020-A068-W006-S02": ("E2", "predikat preveden glagolski: 'ćeš … pobijediti!' ('će' dijeli predikat, dosljedno 31:5, 26:44)"),
    "S020-A069-W007-S02": ("E2", MI),
    "S020-A069-W008-S01": ("E2", "inna → 'jer'; 'samo' je pojačivač (inserted)"),
    "S020-A069-W009-S02": ("E2", MI),
    "S020-A071-W002-S02": ("E2", MI),
    "S020-A073-W002-S02": ("E1", AFTERINNA),
    "S020-A073-W008-S02": ("E2", MI),
    "S020-A077-W007-S01": ("E1", BI),
    "S020-A078-W008-S01": ("E2", "ponovljeni ġašiya (naglasna tautologija) nosi isti izraz 'se … sručilo;'"),
    "S020-A078-W008-S02": ("E2", "ponovljeni -hum nosi isti izraz 'na njih'"),
    "S020-A080-W004-S02": ("E2", MI),
    "S020-A082-W002-S01": ("E1", P_UNEXP + ": emfatičko la- uz inna nema zaseban token (COMMON)"),
    "S020-A083-W002-S01": ("E1", P_AUX + ": 'si … požurio,'"),
    "S020-A088-W005-S01": ("E1", P_UNEXP + ": posvojno la- preoblikovano u glagol 'mukalo'"),
    "S020-A088-W007-S03": ("E2", MI),
    "S020-A089-W003-S02": ("E1", "NEG lā → 'ne'; 'ni' nosi vlastiti segment qawl (COMMON, 36:30)"),
    "S020-A089-W006-S01": ("E1", "qawl → 'ni riječi' (negativna konkordancija na vlastitom segmentu)"),
    "S020-A090-W009-S02": ("E2", MI),
    "S020-A092-W007-S01": ("E1", P_AUX + ": 'su zalutali,'; 'da' bez segmenta (inserted)"),
    "S020-A093-W001-S01": ("E2", P_UNEXP + ": an u allā nije izražen; 'pa' je Mehanovićev veznik"),
    "S020-A094-W017-S01": ("E1", "tarqub → 'nisi'[2,4] 'postupio'"),
    "S020-A094-W018-S01": ("E1", "qawl → 'onako kako sam … rekao.\"'"),
    "S020-A096-W002-S02": ("E2", MI),
    "S020-A096-W006-S02": ("E1", "resumptivna -hi → akuzativni relativ 'što' (COMMON: oblik relativa)"),
    "S020-A097-W004-S01": ("E2", SUBJ),
    "S020-A103-W006-S01": ("E1", INS + ": 'dana.'"),
    "S020-A110-W003-S01": ("E1", "mā bayna aydīhim → parafraza 'su radili' (pomoćni uz glagolski oblik)"),
    "S020-A110-W004-S01": ("E1", "aydī u idiomu bayna aydī → 'su radili'"),
    "S020-A113-W002-S03": ("E1", P_UNEXP + ": objektni -hu nije zasebno izražen; 'Kur'an' nosi qurʾānan"),
    "S020-A113-W009-S01": ("E2", LALLA + "; ponovljeno 'da' nosi isti laʿalla"),
    "S020-A113-W010-S01": ("E2", LALLA),
    "S020-A113-W012-S01": ("E2", "'bi … pobudio.' (pomoćni uz glagol)"),
    "S020-A113-W013-S01": ("E2", P_UNEXP + ": li- uz yuḥdiṯu; bosanski glagol uzima akuzativni objekat 'ih'"),
    "S020-A117-W012-S01": ("E2", FADA + ": 'pa onda'"),
    "S020-A117-W012-S02": ("E2", FADA),
    "S020-A118-W002-S02": ("E2", "-ka (tebi) preoblikovano u subjekat → lični pomoćni '-ćeš' (dosljedno 19:15)"),
    "S020-A121-W007-S02": ("E2", "subjektni sufiks infinitivne dopune → finitni 'počeše' (dosljedno 26:73 'mogu')"),
    "S020-A127-W003-S01": ("E1", "REL man → 'one koji'; 'sve' je pojačivač (inserted, dosljedno 23:84)"),
    "S020-A130-W007-S01": ("E1", "rabb → 'Gospodara' i 'Ga,' (dosljedno 15:98)"),
    "S020-A130-W019-S01": ("E2", LALLA),
    "S020-A130-W020-S01": ("E2", LALLA),
    "S020-A132-W012-S01": ("E1", "lām pripadanja → 'za … sljeduje.'"),
    "S020-A133-W001-S03": ("E1", "subjektni sufiks bez zamjenice i pomoćnog → fused 'govore:'; 'Nevjernici' je dopuna (inserted)"),
    "S020-A133-W004-S01": ("E1", BI),
    "S020-A133-W004-S02": ("E2", INS + ": 'kakav'"),
    "S020-A134-W004-S02": ("E2", INS + ": 'kakvom'"),
    "S020-A134-W019-S02": ("E1", COORDV),
    "S020-A135-W005-S03": ("E2", "FUT sa- nosi 'ćete'; glagol 'saznati'"),
    "S020-A135-W011-S01": ("E2", INS + ": 'i sam'"),
    "S020-A129-W008-S01": ("UNEXP", OMIT),
    "S020-A129-W008-S02": ("UNEXP", OMIT),
    "S020-A129-W009-S01": ("UNEXP", OMIT),
}

if __name__ == "__main__":
    run("S020_Ta-ha", D)
