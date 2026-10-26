# -*- coding: utf-8 -*-
"""CP4 razrješenja za suru 37."""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from resolve_common import P_AUX, P_NARROW, P_UNEXP, run  # noqa: E402

AUXP = "subjektni sufiks drugog glagola nosi zajednički pomoćni glagol ili eksplicitnu zamjenicu (dosljedno 84:25, 46:20)"
COP = P_NARROW + ": particip imenskog predikata → sam particip; buduća kopula 'će/ćemo … biti' je inserted (dosljedno 36:32)"
NEK = P_NARROW + ": neodređenost ('jedan/jednog/jedne/jedno') je Mehanovićeva dopuna (inserted; dosljedno 36:20)"
BI = P_UNEXP + ": bi- uz ǧāʾa/atā; bosanski glagol uzima direktni objekat"
BAAD = P_UNEXP + ": -hum u baʿḍuhum nije zasebno izražen (dosljedno 45:19)"
OBJ = P_NARROW + ": dodani objekat ('Ga', 'ga', 'mu', 'ih') je Mehanovićeva dopuna (inserted; dosljedno 46:15)"
HATTA = "ḥattā ḥīn → akuzativ trajanja 'neko vrijeme' (fused; dosljedno 51:43)"
SAWF = "sawfa nosi 'će'; glagol svoj leksički token"

D = {
    "S037-A015-W002-S01": ("E1", "NEG in → 'nije' + konkordancija 'ništa' (dosljedno 87:6)"),
    "S037-A015-W004-S01": ("E1", "restriktivno illā → 'drugo do'"),
    "S037-A016-W007-S02": ("E1", COP),
    "S037-A021-W007-S02": ("E2", AUXP),
    "S037-A022-W007-S02": ("E2", AUXP),
    "S037-A024-W003-S01": ("E1", COP),
    "S037-A025-W001-S01": ("E2", P_NARROW + ": mā → '\"Šta'; 'zašto' je Mehanovićevo razlaganje (inserted)"),
    "S037-A027-W002-S02": ("E2", BAAD),
    "S037-A028-W004-S02": ("E2", AUXP),
    "S037-A030-W002-S01": ("E2", "kāna → pomoćni dio 'smo' [2,5] u 'nismo'; 'imali,' nosi posvojni la-"),
    "S037-A031-W005-S01": ("E1", "inna → 'doista,'; 'da' je bosanski uvod sadržaja (inserted)"),
    "S037-A035-W010-S02": ("E2", AUXP),
    "S037-A036-W005-S02": ("E2", NEK),
    "S037-A037-W003-S01": ("E2", BI),
    "S037-A037-W004-S02": ("E2", P_AUX + ": ṣaddaqa → 'je iskrenost potvrdio.'"),
    "S037-A039-W006-S02": ("E2", AUXP),
    "S037-A045-W002-S01": ("E2", P_UNEXP + ": ʿalā bezličnog pasiva; bosanski lični pasiv bez prijedloga"),
    "S037-A045-W002-S02": ("E2", "-him postaje subjekat bosanskog pasiva; lice nosi pomoćni 'će'"),
    "S037-A050-W002-S02": ("E2", BAAD),
    "S037-A051-W005-S01": ("E2", "kāna → pomoćni 'sam'; '\"Imao' nosi posvojni li-"),
    "S037-A051-W007-S01": ("E2", NEK),
    "S037-A052-W003-S02": ("E2", P_UNEXP + ": partitivni min nije izražen (muṣaddiqīn → lični glagol)"),
    "S037-A053-W006-S02": ("E1", "inna → 'doista,'; 'da' je bosanski uvod sadržaja (inserted)"),
    "S037-A054-W004-S01": ("E1", "particip muṭṭaliʿūn preoblikovan u rečenicu '\"Hoćete da pogledate?\",' (cijela preoblika; dosljedno 49:17)"),
    "S037-A055-W002-S02": ("E1", "raʾā → 'ugledati.'; zajednički 'će' ostaje uz prvi glagol (dosljedno 46:16)"),
    "S037-A059-W001-S01": ("E1", P_UNEXP + ": izuzetak illā preoblikovan u potvrdnu rečenicu; nema tokena"),
    "S037-A059-W002-S01": ("E2", P_AUX + ": maṣdar mawta glagolizovan → 'smo umrli' (dosljedno 49:17)"),
    "S037-A072-W004-S01": ("E2", "relativna preoblika participa 'one koji su … upozoravali;'; 'ih' je dodani objekat (inserted)"),
    "S037-A075-W005-S02": ("E1", "particip mujībūn → 'smo se … odazvali:'; 'Mi' ostaje inserted (imenska rečenica bez glagolskog segmenta, COMMON)"),
    "S037-A083-W002-S01": ("E1", "min (pripadnost) → poredbeno 'kao'"),
    "S037-A083-W003-S01": ("E1", "šīʿa → 'Iste vjere'"),
    "S037-A090-W003-S01": ("E2", OBJ),
    "S037-A095-W002-S01": ("E2", "a- → '\"Kako'"),
    "S037-A095-W002-S02": ("E2", "taʿbudūna → modalno 'možete obožavati'"),
    "S037-A102-W002-S01": ("E1", "balaġa → 'on odraste toliko da' (eksplicitno 'on' nosi lice glagola)"),
    "S037-A102-W004-S02": ("E1", "saʿy → 'poče u poslu pomagati,'"),
    "S037-A102-W013-S02": ("E2", P_UNEXP + ": imperativ unẓur nije zasebno preveden ('misliš' nosi tarā)"),
    "S037-A102-W021-S02": ("E2", P_AUX + ": taǧidu → 'vidjet ćeš,'"),
    "S037-A105-W002-S01": ("E1", P_NARROW + ": ṣaddaqta → 'si … obistiniti'; 'odlučio' je Mehanovićeva dopuna"),
    "S037-A127-W003-S02": ("E1", COP),
    "S037-A128-W004-S02": ("E2", "relativna preoblika ADJ 'oni … koji su Mu bili odani.' (COMMON)"),
    "S037-A145-W002-S03": ("E2", NEK),
    "S037-A146-W005-S01": ("E2", NEK),
    "S037-A151-W004-S02": ("E2", P_UNEXP + ": posvojno -him nema zaseban token"),
    "S037-A156-W001-S01": ("E1", "am → 'Ili, možda,' (dosljedno 46:4)"),
    "S037-A157-W002-S01": ("E2", BI),
    "S037-A157-W004-S01": ("E2", P_UNEXP + ": kāna u kuntum nije zasebno izraženo (dosljedno 36:48)"),
    "S037-A158-W010-S02": ("E1", COP),
    "S037-A159-W004-S01": ("E2", OBJ),
    "S037-A161-W002-S01": ("E1", "wa → drugo 'ni'; prvo 'ni' ostaje inserted jer NEG je u 37:162 (veza ne prelazi ajet)"),
    "S037-A162-W004-S02": ("E2", "fātinīn → 'možete … u zabludu zavesti,'; konkordancijsko 'nikoga' ide na NEG"),
    "S037-A167-W003-S02": ("E1", "yaqūlu → 'govorili:'; 'su' nosi kāna"),
    "S037-A167-W003-S03": ("E2", AUXP),
    "S037-A170-W004-S01": ("E1", SAWF),
    "S037-A172-W003-S02": ("E1", COP),
    "S037-A174-W003-S01": ("E1", HATTA),
    "S037-A175-W003-S01": ("E1", SAWF),
    "S037-A177-W004-S02": ("E1", "glagol pokude sāʾa → 'zlo … osvanut će'"),
    "S037-A177-W005-S01": ("E1", "ṣabāḥ → 'jutro'"),
    "S037-A178-W003-S01": ("E1", HATTA),
    "S037-A179-W003-S01": ("E1", SAWF),
    "S037-A180-W006-S01": ("E2", OBJ),
}

if __name__ == "__main__":
    run("S037_Es-Saffat", D)
