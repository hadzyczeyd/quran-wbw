# -*- coding: utf-8 -*-
"""CP4 razrješenja za suru 18."""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from resolve_common import P_AUX, P_FUNC, P_GOV, P_NARROW, P_UNEXP, run  # noqa: E402

INS = P_NARROW + "; Mehanovićeva objašnjavajuća dopuna/pojačivač bez arapskog segmenta ostaje inserted (COMMON)"
MINDUNI = "min dūni → 'pored/mimo/osim' + 'drugi' (dūn = 'osim/drugi'), fused s min"
PART = P_UNEXP + ": partitivni min uz imenicu bez genitiva nije izražen (dosljedno 37:52, 39:8)"
ELID = P_UNEXP + ": ponovljeni bayna nije ponovljen; jedno 'između' nosi prvi (dosljedno 25:10, 17:45)"
OBJV = "objekat sadržan u značenju glagola pripada glagolskom izrazu (dosljedno 17:7, 23:59)"
JUSS = "jusiv 3. lica: 'neka … glagol' na glagol, NEG 'ne' (+ 'ništa' bez segmenta) (dosljedno 17:33, 20:16)"
COP = "kopula 'biti/će … biti' uz particip/pridjev bez arapskog segmenta ostaje inserted (dosljedno 23:35, 26:52)"
IMPL = "Mehanović eksplicira imenicu sadržanu u pridjevu/elativu ('vrt', 'grijeh') → pripada tom segmentu"
CONDREL = "uslovni man preveden relativnim izrazom 'onoga/onome ko' → cijeli izraz (COMMON: REL → stvarni bosanski relativni izraz)"
OMIT = "SOURCE_TRANSLATION_OMISSION: izvorni Mehanovićev tekst ne prevodi "

D = {
    "S018-A002-W002-S01": ("E2", "namjerni li- → 'da'; ponovljeno 'da' za koordinirani glagol nosi isti li- (COMMON)"),
    "S018-A002-W007-S02": ("E2", "koordinirani glagol nosi samo 'obraduje.'; 'da' nosi li-"),
    "S018-A004-W001-S02": ("E1", "subjunktiv koordiniran s li- iz 18:2 → 'da upozori' ('da' gradi oblik u ovom ajetu)"),
    "S018-A005-W002-S01": ("E1", "posvojni li- (lahum ʿilm) preoblikovan u glagol 'znaju,' (dosljedno 15:42, 25:2)"),
    "S018-A006-W003-S02": ("E2", "-ka u nafsaka dio idioma 'svisnuti,' (povratni objekat sadržan u glagolu)"),
    "S018-A011-W002-S01": ("E2", "ʿalā u idiomu ḍaraba ʿalā l-āḏān → 'dubokim snom'"),
    "S018-A014-W014-S01": ("E2", MINDUNI),
    "S018-A015-W005-S01": ("E2", MINDUNI),
    "S018-A016-W013-S01": ("E2", PART),
    "S018-A018-W006-S01": ("E2", "ḏāta (strana) → 'na … stranu,'"),
    "S018-A018-W011-S01": ("E1", COP + ": 'je ležao' je Mehanovićev predikat (inserted)"),
    "S018-A019-W035-S02": ("E1", JUSS),
    "S018-A019-W036-S01": ("E1", JUSS),
    "S018-A020-W003-S02": ("E1", "iza inna 'oni' nosi ime; sufiks glagola fused na 'doznaju' (COMMON, dosljedno 19:83)"),
    "S018-A021-W002-S01": ("E2", "kauzativ aʿṯarnā → 'smo, učinili da … saznaju,' ('oni' inserted)"),
    "S018-A021-W027-S01": ("E1", "ġalaba → 'se … najviše držalo'"),
    "S018-A021-W028-S01": ("E1", "ʿalā → 'do' (držati do)"),
    "S018-A022-W028-S01": ("E2", "Mehanovićev dublet 'površno i lijepo,' (COMMON: dublet jedne riječi)"),
    "S018-A025-W007-S02": ("E2", INS + ": 'k tome'"),
    "S018-A026-W016-S01": ("E2", MINDUNI),
    "S018-A026-W017-S01": ("E1", "partitivni min uz negaciju → genitiv 'zaštitnika' (" + P_FUNC + ", dosljedno 30:29)"),
    "S018-A028-W002-S02": ("E2", "-ka u nafsaka dio izraza 'Budi strpljiv'"),
    "S018-A028-W009-S01": ("E1", "yurīdūna → imenski 'u želji'"),
    "S018-A028-W010-S01": ("E1", P_GOV + ": 'za Licem'"),
    "S018-A028-W015-S01": ("E1", "turīdu → imenski 'iz želje'"),
    "S018-A028-W016-S01": ("E1", P_GOV + ": 'za sjajem'"),
    "S018-A031-W011-S01": ("E2", PART + "; instrumental traži glagol 'kititi se'"),
    "S018-A031-W021-S01": ("E1", COP),
    "S018-A034-W001-S02": ("E1", "kāna → pomoćni 'je'"),
    "S018-A040-W005-S01": ("E2", IMPL + ": 'bolji vrt'"),
    "S018-A040-W007-S01": ("E2", "janna u min jannatika elidirana → 'tvoga'"),
    "S018-A043-W002-S01": ("E1", "kāna → '-je' u 'nije'"),
    "S018-A043-W003-S02": ("E2", "-hu (posjednik) bez zamjenice → pomoćni '-je' u 'nije' (COMMON 55.9)"),
    "S018-A044-W009-S01": ("E1", INS + ": 'čini da … sve'"),
    "S018-A045-W014-S01": ("E2", P_UNEXP + ": fa- nema tokena; 'ipak' je Mehanovićev prilog"),
    "S018-A047-W005-S02": ("E1", INS + ": 'površina'"),
    "S018-A048-W001-S02": ("E1", P_AUX + ": pasiv 'bit će … poredani:'"),
    "S018-A048-W004-S01": ("E1", "ṣaff → 'u redove'"),
    "S018-A048-W016-S01": ("E1", INS + ": 'za oživljavanje'"),
    "S018-A049-W015-S01": ("E2", IMPL + ": 'mali … grijeh'"),
    "S018-A049-W017-S01": ("E2", IMPL + ": 'veliki grijeh'"),
    "S018-A055-W012-S01": ("E1", "an → 'to što … da' i ponovljeno 'što … da' za koordinirani glagol"),
    "S018-A055-W014-S01": ("E1", "sunna → 'kazna … pravilo'; 'koja je bila' bez segmenta (inserted)"),
    "S018-A059-W005-S02": ("E2", "subjektni sufiks → pomoćni 'su'; 'stanovnici njihovi' je Mehanovićev subjekat (inserted)"),
    "S018-A061-W004-S01": ("E1", P_UNEXP + ": bayn nije izražen; recipročnost nosi 'sastaju'"),
    "S018-A064-W008-S02": ("E1", P_UNEXP + ": posvojni -humā nije zasebno izražen"),
    "S018-A065-W003-S01": ("E1", "partitivni min uz neodređenost → 'jednoga' (COMMON)"),
    "S018-A069-W006-S01": ("E1", COP),
    "S018-A070-W009-S01": ("E2", "uḥdiṯa → 'ja … prvi … kažem.\"'"),
    "S018-A073-W004-S01": ("E1", "uzročno bi- → 'što' (fused s mā)"),
    "S018-A073-W007-S02": ("E2", P_UNEXP + ": objektni -nī nije zasebno izražen"),
    "S018-A074-W011-S01": ("E1", P_UNEXP + ": bi- (u zamjenu) nije izražen"),
    "S018-A074-W011-S02": ("E1", "ġayr → 'nije … ubilo!'"),
    "S018-A074-W012-S01": ("E1", "negativna konkordancija na vlastitom segmentu: nafs → 'nikoga' (COMMON)"),
    "S018-A078-W005-S02": ("E1", ELID),
    "S018-A081-W006-S01": ("E2", P_UNEXP + ": min poređenja nije izražen"),
    "S018-A082-W026-S03": ("E1", "-hu → 'to'; 'Sve' je pojačivač (inserted)"),
    "S018-A083-W004-S01": ("E2", "DET al- u imenu Ḏū l-Qarnayn unexpressed (COMMON)"),
    "S018-A084-W008-S01": ("E2", "kull → 'sve'; 'što želi' je dopuna (inserted)"),
    "S018-A086-W006-S02": ("E2", "objektni -hā preoblikovan u subjekat 'zalazi' (fused)"),
    "S018-A086-W019-S01": ("E1", OBJV + ": 'ćeš … ih kazniš'"),
    "S018-A087-W003-S01": ("E2", CONDREL),
    "S018-A088-W002-S01": ("E2", CONDREL),
    "S018-A092-W003-S01": ("E1", OBJV + ": sabab sadržan u 'pođe.'"),
    "S018-A094-W003-S01": ("E2", "DET al- u imenu Ḏū l-Qarnayn unexpressed (COMMON)"),
    "S018-A094-W018-S02": ("E1", ELID),
    "S018-A095-W011-S02": ("E1", ELID),
    "S018-A098-W011-S01": ("E1", "dakkāʾ → 'sa zemljom … sravniti,'"),
    "S018-A098-W012-S02": ("E1", "kāna → 'će'"),
    "S018-A098-W015-S01": ("E1", "ḥaqq → 'se sigurno ispuniti.\"'"),
    "S018-A101-W004-S01": ("E1", "fī bez bosanskog prijedloga → instrumental 'koprenom'"),
    "S018-A104-W010-S01": ("E2", "yuḥsinūna → 'dobro'; kopula 'je' inserted"),
    "S018-A105-W009-S02": ("E2", "NEG lā → 'ne-' u 'nećemo'; 'ni' nosi vlastiti segment wazn (COMMON)"),
    "S018-A105-W014-S01": ("E2", "negativna konkordancija na vlastitom segmentu: wazn → 'ni vagu'"),
    "S018-A106-W006-S02": ("E2", P_AUX + ": 'su se … rugali.' (dosljedno 23:110)"),
    "S018-A106-W009-S01": ("E2", "huzuw → leksički sadržaj 'rugali.' (dosljedno 23:110)"),
    "S018-A109-W010-S01": ("E1", "qabla → suprotno 'ali ne' (Mehanovićeva preoblika)"),
    "S018-A109-W012-S01": ("E1", P_UNEXP + ": drugi tanfada elidiran ('ali ne i riječi')"),
    "S018-A109-W018-S01": ("E1", OBJV + ": 'ga proširili'"),
    "S018-A110-W005-S01": ("E1", "miṯl → 'kao'; 'i' bez segmenta (inserted)"),
    "S018-A110-W013-S01": ("E1", "kāna + imperfekt bez pomoćnog → fused na 'nada' (dosljedno 29:5)"),
    "S018-A110-W020-S02": ("E1", JUSS),
    "S018-A110-W021-S01": ("E1", JUSS),
    # Mehanovićevi propusti (tekst se ne mijenja; dokumentovano u cp4/DOCUMENTED_EXCEPTIONS.json)
    "S018-A026-W008-S02": ("UNEXP", OMIT + "„as-samāwāti“ (ġaybu s-samāwāti wa-l-arḍi → „ono što je čulima nedokučivo“); veza se ne izmišlja"),
    "S018-A026-W009-S03": ("UNEXP", OMIT + "„al-arḍi“ (vidi 18:26 W008); veza se ne izmišlja"),
    "S018-A086-W015-S02": ("UNEXP", OMIT + "vokativ „yā ḏā l-qarnayni“ (O Zulkarnejne); veza se ne izmišlja"),
    "S018-A086-W016-S02": ("UNEXP", OMIT + "„al-qarnayni“ u vokativu; veza se ne izmišlja"),
}

if __name__ == "__main__":
    run("S018_El-Kehf", D)
