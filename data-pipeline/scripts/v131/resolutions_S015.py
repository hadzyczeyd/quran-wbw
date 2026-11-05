# -*- coding: utf-8 -*-
"""CP4 razrješenja za suru 15."""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from resolve_common import P_AUX, P_NARROW, P_UNEXP, run  # noqa: E402

BI = P_UNEXP + ": bi- uz ǧāʾa/atā/asrā; bosanski glagol uzima direktni objekat (dosljedno 26:30, 31:16, 34:9)"
RECT = P_UNEXP + ": prijedlog traži samo arapska rekcija; bosanski glagol uzima akuzativni objekat (COMMON)"
MI = "subjektni sufiks → eksplicitna zamjenica 'Mi'; pomoćni 'smo/ćemo' pripada glagolskom obliku (COMMON)"
COORD = "drugi koordinirani glagol nosi samo svoj token; njegov subjektni sufiks → zajednički pomoćni (dosljedno 30:9, 26:73)"
EMPH = P_UNEXP + ": emfatičko la- uz inna nema zaseban token (COMMON)"
ALSO = "wa → 'a'; 'i' sa značenjem 'također' ostaje inserted (COMMON)"
SEPPRON = "ime inna/anna → eksplicitno 'Ja'; samostalna zamjenica anā → kopula 'sam' koja nosi njeno lice (COMMON, dosljedno 26:44)"
AUXV = P_AUX + ": 'si' gradi perfekt i nosi subjektni sufiks -ta"

D = {
    "S015-A007-W004-S01": ("E2", BI),
    "S015-A008-W008-S01": ("E2", "iḏan → 'tada'; 'da ih pošaljemo,' je Mehanovićeva objašnjavajuća dopuna (inserted)"),
    "S015-A016-W002-S02": ("E1", MI),
    "S015-A016-W006-S03": ("E2", COORD),
    "S015-A019-W003-S03": ("E2", COORD),
    "S015-A019-W006-S03": ("E2", COORD),
    "S015-A020-W005-S01": ("E1", ALSO),
    "S015-A022-W009-S02": ("E1", "NEG mā → 'ni-' u 'niste' (granica ni|ste, COMMON)"),
    "S015-A022-W011-S01": ("E1", RECT),
    "S015-A022-W012-S02": ("E1", "ḫāzinīn → '-ste u stanju zadržati.' (predikatski izraz; '-ste' je ostatak tokena 'niste')"),
    "S015-A023-W002-S01": ("E1", EMPH),
    "S015-A026-W002-S02": ("E1", MI),
    "S015-A032-W004-S02": ("E2", "mā laka (šta ti je) → idiom 'zašto'; -ka je dio idioma"),
    "S015-A033-W006-S01": ("E2", AUXV),
    "S015-A038-W003-S02": ("E1", P_UNEXP + ": yawm al-waqt sažeto u 'Dana … određenog'; 'već' je pojačivač (inserted)"),
    "S015-A039-W004-S01": ("E2", AUXV),
    "S015-A039-W005-S02": ("E1", P_NARROW + ": 'poroke' je objašnjavajuća dopuna objekta (inserted)"),
    "S015-A042-W003-S01": ("E1", "laysa → 'ne-' u 'nećeš' (granica ne|ćeš)"),
    "S015-A042-W004-S01": ("E1", "posvojno li-ka → '-ćeš imati'"),
    "S015-A042-W005-S01": ("E1", "ponovljeni prijedlog 'nad' pred izuzetim nosi isti ʿalā (dosljedno 57:1)"),
    "S015-A042-W008-S01": ("E1", "REL man → 'onima koji'"),
    "S015-A047-W001-S03": ("E1", MI),
    "S015-A049-W003-S02": ("E2", SEPPRON),
    "S015-A049-W004-S01": ("E2", SEPPRON),
    "S015-A052-W004-S03": ("E2", COORD),
    "S015-A055-W003-S01": ("E1", P_UNEXP + ": bi- (s istinom) nema zasebnog tokena"),
    "S015-A055-W003-S03": ("E1", "ḥaqq → 'će se doista obistiniti\",'; 'koja' se odnosi na 'vijest' (inserted)"),
    "S015-A063-W004-S01": ("E2", BI),
    "S015-A064-W002-S01": ("E2", BI),
    "S015-A065-W002-S01": ("E2", BI),
    "S015-A066-W001-S03": ("E1", MI),
    "S015-A074-W001-S03": ("E1", MI),
    "S015-A076-W002-S01": ("E1", EMPH),
    "S015-A081-W001-S03": ("E1", MI),
    "S015-A082-W006-S01": ("E1", P_NARROW + ": āminīn → 'sigurni,'; 'vjerujući da su' je objašnjavajuća dopuna (inserted)"),
    "S015-A084-W001-S02": ("E2", "negativna konkordancija bez vlastitog segmenta ('ni … kakve') → NEG (COMMON)"),
    "S015-A084-W002-S01": ("E2", "aġnā → 'bijaše … od … koristi'"),
    "S015-A085-W002-S02": ("E1", MI),
    "S015-A085-W010-S02": ("E2", P_NARROW + ": sāʿa → 'Čas'; 'oživljenja' je objašnjavajuća dopuna (inserted)"),
    "S015-A085-W011-S01": ("E1", EMPH),
    "S015-A087-W002-S02": ("E1", MI),
    "S015-A087-W006-S01": ("E1", ALSO),
    "S015-A088-W007-S01": ("E1", RECT),
    "S015-A089-W002-S01": ("E2", P_UNEXP + ": inna nema zasebnog tokena"),
    "S015-A089-W002-S02": ("E2", SEPPRON),
    "S015-A089-W003-S01": ("E2", SEPPRON),
    "S015-A089-W004-S01": ("E1", "DET al- normalno unexpressed (COMMON)"),
    "S015-A097-W001-S02": ("E1", P_UNEXP + ": zakletveno la- u la-qad nema zaseban token (COMMON)"),
    "S015-A098-W002-S02": ("E1", "ḥamd → glagolski 'hvali'"),
    "S015-A098-W003-S01": ("E1", "rabb → 'Gospodara' i 'Ga,' (objekat oba glagola: veličaj Gospodara … hvali Ga)"),
    "S015-A089-B005": ("INS", "'samo' je Mehanovićevo isticanje isključivosti (ḍamīr al-faṣl + određeni predikat) bez zasebnog segmenta"),
}

if __name__ == "__main__":
    run("S015_El-Hidzr", D)
