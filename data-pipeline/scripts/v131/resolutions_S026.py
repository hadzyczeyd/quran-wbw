# -*- coding: utf-8 -*-
"""CP4 razrješenja za suru 26."""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from resolve_common import P_AUX, P_GOV, P_NARROW, P_UNEXP, run  # noqa: E402

PART = P_UNEXP + ": partitivni min nije izražen, jednina/predikat nosi imenicu (dosljedno 37:52, 39:8)"
BI = P_UNEXP + ": bi- uz ǧāʾa/atā/nazala; bosanski glagol uzima direktni objekat (dosljedno 31:16, 34:9)"
RECT = P_UNEXP + ": prijedlog traži samo arapska rekcija; bosanski glagol uzima akuzativni objekat (COMMON)"
INS = P_NARROW + "; pojačivač/neodređenost bez arapskog segmenta ostaje inserted (COMMON)"
KADH = "ka-ḏālika: DEM → 'Eto,', ka- → 'tako' (dosljedno 42:3, 44:54, 47:3)"
SEPPRON = "samostalna zamjenica između imena i predikata → kopula koja nosi njeno lice; subjektni sufiks → eksplicitna zamjenica (COMMON)"
AFTERPRON = "zamjenica nosi samostalno hum / ime inna; sufiks glagola ide na pomoćni ili glagol (dosljedno 39:25, 70:6)"
NECEDA = "kāna → 'će' iz 'neće'; 'da' u Mehanovićevom 'neće da' nema arapskog segmenta (inserted)"
COP = "kopula imenske rečenice bez arapskog segmenta ostaje inserted; particip nosi samo svoj token (COMMON)"
NAKAD = "yawma → 'na Dan kad(a)': 'kad' uvodi rečenicu u iḍāfi (dosljedno 40:16, 40:51, 41:47, 57:12)"
KADHDHABU = P_NARROW + ": kaḏḏabū → idiom 'u laž utjeruju'; 'su nastavili da' je Mehanovićevo aspektno proširenje (inserted)"
MISMATCH = "SOURCE_TRANSLATION_MISMATCH: Mehanovićev tekst 26:220 ima „Silni i Milostivi“ (refren 26:9 itd.) umjesto "

D = {
    "S026-A003-W005-S01": ("E2", NECEDA),
    "S026-A014-W003-S01": ("E2", P_NARROW + ": ḏanb → 'zlodjela'; 'optužbu za' je objašnjavajuća dopuna (inserted)"),
    "S026-A019-W006-S01": ("E2", PART),
    "S026-A021-W010-S01": ("E2", PART),
    "S026-A022-W001-S02": ("E1", P_UNEXP + ": tilka nije zasebno izražen; 'to što' je bosanski oblik maṣdarskog an"),
    "S026-A022-W005-S01": ("E1", "maṣdarsko an → 'to što'"),
    "S026-A029-W004-S01": ("E2", INS + ": 'nekoga'"),
    "S026-A030-W004-S01": ("E1", BI),
    "S026-A031-W003-S01": ("E1", BI),
    "S026-A037-W002-S01": ("E1", BI),
    "S026-A040-W005-S02": ("E1", SEPPRON),
    "S026-A040-W006-S01": ("E1", SEPPRON),
    "S026-A041-W005-S01": ("E2", RECT),
    "S026-A041-W010-S02": ("E1", SEPPRON),
    "S026-A041-W011-S01": ("E1", SEPPRON),
    "S026-A044-W007-S02": ("E1", "ime inna -nā → eksplicitno 'mi' (COMMON)"),
    "S026-A044-W008-S02": ("E1", "samostalno naḥnu → 'ćemo' (predikat preveden glagolski, dosljedno 31:5, 32:10, 34:7)"),
    "S026-A049-W010-S01": ("E1", "allaḏī: relativna rečenica preoblikovana u samostalnu, relativni subjekat nosi 'on'"),
    "S026-A049-W011-S01": ("E1", P_AUX + ": 'je … naučio'; 'on' nosi allaḏī"),
    "S026-A052-W008-S01": ("E2", COP + ": 'bit' inserted, 'ćete' nosi -kum"),
    "S026-A055-W002-S01": ("E2", RECT),
    "S026-A058-W001-S01": ("E2", P_UNEXP + ": wa- nema tokena; ponovljeno 'iz' kodira padež imenice"),
    "S026-A058-W001-S02": ("E2", P_GOV),
    "S026-A059-W001-S02": ("E1", KADH),
    "S026-A061-W002-S01": ("E2", "recipročni VI tarāʾā → 'jedni druge ugledaše,'"),
    "S026-A061-W003-S02": ("E2", P_UNEXP + ": jamʿān (dvije skupine) Mehanović ne imenuje; 'jedni druge' nosi recipročni glagol"),
    "S026-A070-W003-S01": ("E2", RECT),
    "S026-A070-W005-S01": ("E2", "upitno mā → 'Šta'; 'to' je pojačivač (inserted)"),
    "S026-A073-W002-S01": ("E1", "glagol nosi samo svoj token; 'mogu' je zajednički finitni oblik"),
    "S026-A073-W004-S02": ("E1", "subjektni sufiksi oba koordinirana glagola → zajednički finitni 'mogu' (kao zajednički pomoćni)"),
    "S026-A074-W003-S01": ("E2", P_NARROW + ": 'kako' uvodi dopunu bez arapskog segmenta (inserted)"),
    "S026-A079-W002-S01": ("E1", "huwa u relativnoj rečenici: ulogu nosi nominativni relativ 'Koji' (COMMON: resumptivna → oblik relativa)"),
    "S026-A087-W003-S01": ("E1", NAKAD),
    "S026-A088-W001-S01": ("E1", NAKAD),
    "S026-A096-W002-S01": ("E2", P_UNEXP + ": okolnosno wa nema tokena; glagolski prilog nosi glagol"),
    "S026-A096-W004-S02": ("E2", AFTERPRON + "; bez pomoćnog → fused na 'svađajući'"),
    "S026-A100-W001-S02": ("E1", "korelacija 'ni … ni': prvo 'ni' na prvi NEG (COMMON, 93:3)"),
    "S026-A100-W003-S01": ("E1", P_UNEXP + ": 'ni' pripada korelaciji"),
    "S026-A102-W002-S01": ("E1", "anna → 'da' (da se povratimo)"),
    "S026-A102-W004-S01": ("E1", "karra → glagolski 'se povratimo,'; 'da' nosi anna"),
    "S026-A102-W005-S01": ("E1", "fa sababiyya → 'pa'"),
    "S026-A102-W005-S02": ("E1", "konjunktiv nakūna → 'da postanemo' ('da' gradi oblik)"),
    "S026-A102-W006-S01": ("E2", PART),
    "S026-A111-W003-S01": ("E2", RECT),
    "S026-A112-W004-S01": ("E1", RECT),
    "S026-A116-W007-S01": ("E2", PART),
    "S026-A118-W008-S01": ("E2", PART),
    "S026-A128-W005-S02": ("E2", "subjektni sufiks bez zamjenice i pomoćnog → fused na glagolski token (COMMON 55.9)"),
    "S026-A136-W008-S01": ("E2", PART),
    "S026-A139-W001-S02": ("E2", KADHDHABU),
    "S026-A146-W002-S01": ("E1", "fī mā hāhunā sažeto u mjesni prilog 'ovdje'"),
    "S026-A146-W004-S01": ("E1", P_UNEXP + ": čestica hā- nema bosanski ekvivalent"),
    "S026-A148-W001-S01": ("E2", P_UNEXP + ": wa- nema tokena; ponovljeno 'u' kodira padež imenice"),
    "S026-A148-W001-S02": ("E2", P_GOV),
    "S026-A149-W005-S01": ("E1", INS + ": 'vrlo'"),
    "S026-A153-W004-S01": ("E2", PART),
    "S026-A154-W007-S01": ("E1", BI),
    "S026-A154-W007-S02": ("E2", INS + ": 'jedno'"),
    "S026-A155-W004-S01": ("E1", P_UNEXP + ": posvojno la- preoblikovano u subjekat 'ona'"),
    "S026-A155-W006-S02": ("E1", P_UNEXP + ": posvojno la- preoblikovano u subjekat 'vi'"),
    "S026-A157-W002-S01": ("E1", "fa → 'i potom'"),
    "S026-A157-W002-S02": ("E1", "aṣbaḥa (sestra kāna) bez zasebnog tokena → fused na glagolski izraz"),
    "S026-A165-W004-S02": ("E2", "ʿālamīn → 'svjetova' (dosljedno 1:2, 37:182); 'svih' je pojačivač (inserted)"),
    "S026-A167-W007-S01": ("E2", PART),
    "S026-A171-W004-S02": ("E1", "ġābirīn → 'je ostala … onima koji su kaznu iskusili'; 'koja' se odnosi na 'starice' (inserted)"),
    "S026-A182-W001-S02": ("E1", "zinū → 'mjerite,'; 'mjerom' je Mehanovićeva etimološka dopuna (inserted)"),
    "S026-A182-W003-S02": ("E2", "mustaqīm → 'ispravnom'"),
    "S026-A185-W004-S01": ("E2", PART),
    "S026-A186-W008-S02": ("E2", PART),
    "S026-A188-W004-S01": ("E1", RECT),
    "S026-A189-W001-S02": ("E2", KADHDHABU),
    "S026-A189-W009-S01": ("E2", INS + ": 'jednog'"),
    "S026-A190-W006-S01": ("E2", NECEDA),
    "S026-A193-W002-S01": ("E1", BI),
    "S026-A194-W004-S01": ("E2", PART),
    "S026-A200-W001-S02": ("E1", KADH),
    "S026-A202-W005-S02": ("E2", AFTERPRON),
    "S026-A206-W005-S01": ("E1", P_NARROW + ": 'kao prijetnja' je objašnjavajuća dopuna (inserted)"),
    "S026-A210-W003-S01": ("E1", BI),
    "S026-A211-W003-S01": ("E1", P_UNEXP + ": la- (njima ne priliči) preoblikovano u subjekat 'oni'"),
    "S026-A212-W001-S01": ("E2", P_UNEXP + ": inna nema zasebnog tokena"),
    "S026-A212-W004-S01": ("E2", "emfatičko la- na predikatu → pojačivač 'potpuno'"),
    "S026-A212-W004-S02": ("E2", COP),
    "S026-A215-W002-S02": ("E2", P_UNEXP + ": posvojni -ka u idiomu 'spusti krilo' nije zasebno izražen"),
    "S026-A215-W005-S01": ("E2", PART),
    "S026-A218-W004-S01": ("E2", P_NARROW + ": 'na namazu' je objašnjavajuća dopuna (inserted)"),
    "S026-A221-W001-S01": ("E1", "hal (ponuda) → 'Hoćete li'"),
    "S026-A221-W002-S01": ("E1", "'da obavijestim' ('da' gradi bosanski oblik)"),
    "S026-A225-W007-S02": ("E2", AFTERPRON),
    "S026-A227-W017-S01": ("E2", "ayya → 'kakvo'"),
    "S026-A227-W018-S01": ("E2", P_GOV + ": 'u … mjesto'"),
    # 26:220 — greška izvornog teksta; tekst se ne mijenja, dokumentovano u cp4/DOCUMENTED_EXCEPTIONS.json
    "S026-A220-W003-S02": ("UNEXP", MISMATCH + "as-samīʿ („Onaj Koji sve čuje“); veza se ne izmišlja"),
    "S026-A220-W004-S02": ("UNEXP", MISMATCH + "al-ʿalīm („Onaj Koji sve zna“); veza se ne izmišlja"),
    "S026-A220-B007": ("INS", "'Silni' ne odgovara arapskom as-samīʿ (greška izvornog teksta, cp4/DOCUMENTED_EXCEPTIONS.json)"),
    "S026-A220-B009": ("INS", "'Milostivi' ne odgovara arapskom al-ʿalīm (greška izvornog teksta, cp4/DOCUMENTED_EXCEPTIONS.json)"),
    "S026-A182-B005": ("INS", "'mjerom' je Mehanovićeva etimološka dopuna bez arapskog segmenta"),
}

if __name__ == "__main__":
    run("S026_Es-Suara", D)
