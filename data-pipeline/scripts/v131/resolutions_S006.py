# -*- coding: utf-8 -*-
"""CP4 razrješenja za suru 6."""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from resolve_common import P_NARROW, P_UNEXP, run  # noqa: E402

INS = P_NARROW + "; Mehanovićeva objašnjavajuća dopuna/pojačivač bez arapskog segmenta ostaje inserted (COMMON)"
LAW = "la- odgovora law uz 'opet' nije zasebno izraženo (dosljedno 30:58, 8:23)"
NIJEN = "in … illā 'nije ništa drugo do': NEG → 'nije ništa', illā → 'drugo do' (dosljedno 25:4, 37:15, 74:24)"
REPP = "ponovljeni bosanski prijedlog pred koordiniranim članom nosi isti arapski prijedlog (COMMON, 'na na', 57:1)"
REPN = "imenica nosi samo svoj leksički dio; ponovljeni prijedlog nosi arapski prijedlog (REPP)"
BAYN = "ponovljeni bayna: bosanski ne ponavlja 'između' (dosljedno 17:96 'između mene i vas', 17:45)"
SIRK = INS + ": 'u obožavanju' (dosljedno 9:31, 10:18, 13:16); 'druge/Njemu' su sadržaj glagola širk"
LAWTARA = "law tarā → law 'da', glagol 'ti je vidjeti' (dosljedno 32:12; 'je' kao 'si' u 8:50 'si vidio')"
LAYTA = "layta → 'Da … je da'; ponovljeno 'da' pred koordiniranim glagolima nosi layta, wa samo veznik (dosljedno 19:23, 33:66)"
LIQA = ("kaḏḏaba/āmana bi-liqāʾ → bi- nosi dopunsko 'da' (kao amara bi- 7:28, 9:67), liqāʾ 'će … stati' "
        "(nema zamjenice, pomoćni uz glagolski izraz), 'pred' kodira padež imenice (P_GOV)")
SVI = "subjektni sufiks → pomoćni 'će'; 'svi' je Mehanovićev pojačivač (inserted, dosljedno 10:4, 18:50, 43:85)"
HUMF = "samostalno hum bez zamjenice u prijevodu → fused na nosioca lica (dosljedno 13:10 HUWAF)"
NEMA = "lā/lam … li- 'nema' → negacija 'ne-' [0,2], posvojno '-ma' [2,4] (dosljedno 'nemoj' ne|moj, 3:8)"
LAYSA = "laysa li- 'neće imati' → laysa 'ni ne-' (kao lan 'ne-' u 'neće'), -hum '-će' (lice), li- 'imati' (dosljedno S009 kāna + li-)"
LREQ = P_UNEXP + ": prijedlog traži samo arapski glagol; bosanski glagol uzima direktni objekat (COMMON)"
BAAD = "baʿd → 'već', iḏ → veznik okolnosti 'a' (dosljedno 3:8, 3:80 'nakon' | 'što')"
KADH = "ka-ḏālika 'Isto tako/Tako isto': oba segmenta nose 'tako', 'isto' je pojačivač (dosljedno 25:31, 29:47, 18:19)"
DA = "dopunsko 'da' bez arapskog veznika ide glagolu dopunske rečenice (COMMON, 3:52)"
BIGH = "bi-ġayri 'ne (znajući)' → bi- dijeli 'ne' s ġayr (dosljedno 28:50)"
KANAF = "kāna + imperfekt/predikat preveden bez pomoćnog → kāna fused na glagol (većinska praksa završenih sura)"
RESR = "resumptivni -hi nosi relativ 'čijem/čemu'; mā samo 'ono/onome' (dosljedno 24:61)"
RESD = "resumptivni -hi uz istaknuti ḏālikum dijeli 'to' teme (COMMON: tema ispred, dosljedno 9:100)"
CORR = "korelativno 'i … i' za jedan wa: svi tokeni korelacije nose taj wa (COMMON 43:64)"
PARTN = "imenica/particip preveden glagolom: pomoćni nosi ime inna/anna ili zamjenicu koja ga već ima (COMMON, S009 PARTN)"
EMPHN = "zakletveno la- i -nna dijele 'sigurno' (dosljedno 7:16, 7:23, 7:149)"
KHALID = "ḫālidīn kao ḥāl → 'ćete vječno ostati' (pomoćni uz glagolski izraz; posvojni -kum druge fraze ga ne nosi, dosljedno 3:136, 9:72)"
LIKULL = "li-kulli + imenica → dativ imenice nosi li- (dosljedno 25:31 'svakom vjerovjesniku')"
ILLAMA = "illā mā šāʾa → 'osim ako ne' / mā 'drukčije' / 'odredi' (dosljedno 11:107)"

D0 = {
    "007-W009-S01": ("E1", LAW), "009-W004-S01": ("E1", LAW), "009-W006-S02": ("E1", LAW), "028-W011-S01": ("E1", LAW),
    "007-W012-S01": ("E2", NIJEN), "007-W014-S01": ("E2", NIJEN),
    "011-W010-S02": ("E2", "mukaḏḏibīn → cijeli relativni izraz s objektom 'poslanike' (dosljedno 16:36, 3:137)"),
    "012-W004-S01": ("E2", REPP), "012-W006-S03": ("E2", REPN),
    "017-W007-S01": ("E2", "li- uz kāšif izražen akuzativom 'je' (dosljedno 10:107)"),
    "019-W010-S02": ("E1", BAYN), "058-W011-S02": ("E1", BAYN),
    "022-W007-S01": ("E1", SIRK), "041-W012-S01": ("E1", SIRK), "064-W010-S01": ("E1", SIRK), "081-W008-S01": ("E1", SIRK),
    "088-W011-S01": ("E1", SIRK), "094-W021-S01": ("E1", SIRK), "148-W003-S01": ("E1", SIRK), "151-W009-S01": ("E1", SIRK),
    "025-W012-S01": ("E2", "āḏān sadržane u 'gluhim' (dosljedno 17:46, 18:57)"),
    "027-W001-S02": ("E2", LAWTARA), "027-W002-S01": ("E2", LAWTARA), "030-W001-S02": ("E2", LAWTARA),
    "030-W002-S01": ("E2", LAWTARA), "093-W023-S02": ("E2", LAWTARA), "093-W024-S01": ("E2", LAWTARA),
    "027-W008-S02": ("E1", LAYTA), "027-W010-S01": ("E1", LAYTA), "027-W014-S01": ("E1", LAYTA),
    "028-W011-S02": ("E2", "ʿāda li- → 'bi nastavili raditi' (vraćanje radnji je leksički sadržaj glagola)"),
    "030-W007-S01": ("E1", INS + ": 'ih' (nema arapskog objekta)"),
    "031-W005-S01": ("E2", LIQA), "031-W005-S02": ("E2", LIQA), "031-W006-S01": ("E2", LIQA),
    "154-W015-S01": ("E2", LIQA), "154-W015-S02": ("E2", LIQA), "154-W016-S01": ("E2", LIQA),
    "031-W010-S02": ("E1", "as-sāʿa → Mehanovićev termin 'Čas oživljenja' (većinska praksa)"),
    "040-W009-S02": ("E2", "as-sāʿa → 'Čas'; 'sudnji' je dopuna (dosljedno 'Doći će Čas sudnji')"),
    "031-W015-S01": ("E2", INS + ": 'sve'"),
    "031-W018-S02": ("E1", HUMF), "048-W014-S01": ("E1", HUMF), "092-W019-S02": ("E1", HUMF),
    "031-W023-S01": ("E2", P_UNEXP + ": INC alā nije zasebno izražen (većinska praksa)"),
    "036-W006-S02": ("E2", "resumptivni -hum dijeli izraz istaknute teme 'umrle' (COMMON, dosljedno 24:3)"),
    "036-W010-S02": ("E1", SVI), "038-W022-S02": ("E1", SVI),
    "048-W005-S01": ("E1", INS + ": 'zato'"),
    "048-W010-S02": ("E2", "lā → 'ne'; negativna konkordancija 'ničega' ide imenici ḫawf (COMMON, dosljedno 3:170 'nikakva straha')"),
    "048-W011-S01": ("E2", "ḫawf → 'neka se ničega boje' (konkordancija na vlastitom segmentu imenice)"),
    "051-W009-S01": ("E2", LAYSA), "051-W010-S01": ("E1", LAYSA), "051-W010-S02": ("E2", LAYSA),
    "070-W017-S01": ("E2", LAYSA), "070-W018-S01": ("E1", LAYSA), "070-W018-S02": ("E2", LAYSA),
    "052-W002-S01": ("E1", INS + ": 'od sebe'"),
    "052-W011-S01": ("E2", "ʿalā obaveze izražen glagolom odgovornosti 'odgovarati' (dosljedno 6:69 ʿalā → 'imati')"),
    "052-W019-S01": ("E2", "ʿalā obaveze izražen glagolom odgovornosti 'odgovarati'"),
    "053-W003-S02": ("E1", P_UNEXP + ": posvojni -hum uz baʿḍ nije izražen (većinska praksa, 8:37, 9:67)"),
    "112-W010-S02": ("E1", P_UNEXP + ": posvojni -hum uz baʿḍ nije izražen (većinska praksa)"),
    "053-W005-S03": ("E1", "subjektni sufiks → pomoćni 'bi'; 'nevjernici' je Mehanovićeva eksplikacija (inserted)"),
    "053-W010-S01": ("E1", P_UNEXP + ": min u min bayni (COMMON min qabli)"),
    "054-W008-S01": ("E2", "ʿalaykum → 'alej-' [0,4] | '-kum' (stvarna granica, dosljedno 7:46)"),
    "054-W008-S02": ("E2", "ʿalaykum → '-kum' [4,8] (dosljedno 7:46)"),
    "055-W005-S01": ("E2", INS + ": 'kojim idu'"),
    "059-W010-S01": ("E2", REPP), "059-W012-S03": ("E2", REPN),
    "061-W011-S01": ("E1", "aḥad → 'nekom'; 'od' kodira partitiv zamjenice (dosljedno 49:12, 63:10)"),
    "061-W011-S02": ("E1", "-kum → 'od vas' (dosljedno 49:12, 63:10)"),
    "063-W015-S01": ("E2", EMPHN), "077-W015-S01": ("E2", EMPHN),
    "065-W019-S02": ("E1", "posvojni -kum uz baʿḍ → lice glagola 'iskusite' (dosljedno 7:24, 29:25)"),
    "066-W009-S02": ("E1", INS + ": 'da Uputu dam'"),
    "068-W004-S01": ("E1", INS + ": 'i rugaju se' (objašnjenje, ne dublet)"),
    "068-W019-S01": ("E1", "baʿd → 'nakon što' (veznik koji uvodi preoblikovani maṣdar, dosljedno 24:33)"),
    "068-W020-S02": ("E1", "ḏikrā → 'se sjetiš,' ('što' nosi baʿda)"),
    "069-W012-S01": ("E1", INS + ": 'toga'"),
    "070-W002-S01": ("E1", "ponovljeni relativ 'koje' koordinirane relativne rečenice nosi isti REL (COMMON)"),
    "071-W018-S02": ("E1", "ponovljeni relativ 'koga' nosi isti REL (COMMON)"),
    "070-W026-S01": ("E1", "taʿdil kulla ʿadlin sažeto u 'otkupnina' (fused glagol + apsolutni objekat)"),
    "071-W011-S01": ("E1", DA), "071-W011-S02": ("E1", DA),
    "071-W014-S01": ("E2", BAAD), "071-W015-S01": ("E2", BAAD),
    "071-W023-S01": ("E1", INS + ": 'pa'"),
    "071-W035-S01": ("UNEXP", P_UNEXP + ": DET predikata nije istiġrāq; 'istinska' je Mehanovićev dodatak (dosljedno 8:2, 24:62)"),
    "071-W035-S02": ("E2", "hudā → 'uputa,'; 'istinska' inserted (dosljedno 8:2)"),
    "073-W019-S01": ("E2", "ʿālim → 'zna'; 'On' je eksplicitni subjekat bez arapske zamjenice (inserted, dosljedno 13:9 'On je')"),
    "092-W005-S01": ("E2", "muṣaddiq → 'potvrđuje'; 'ona' inserted (dosljedno 13:9)"),
    "095-W010-S02": ("E2", "muḫrij → 'Taj Koji izvodi'; 'On je' bez arapske zamjenice inserted (dosljedno 13:9)"),
    "096-W001-S01": ("E2", "fāliq → 'Taj Koji čini da sviće'; 'On je' inserted (dosljedno 13:9)"),
    "074-W010-S01": ("E1", DA),
    "080-W014-S01": ("E2", "illā → 'osim'; 'što se bojim' je Mehanovićeva dopuna"),
    "081-W022-S02": ("E2", "eksplicitna zamjenica 'vi' nosi subjektni sufiks (COMMON)"),
    "082-W008-S02": ("E2", PARTN + ": -hum → 'će'"),
    "082-W009-S02": ("E2", PARTN + ": amn → 'bit … sigurni:'"),
    "083-W002-S01": ("E1", INS + ": 'čvrst'"),
    "085-W005-S01": ("E1", INS + ": 'oni'"),
    "091-W005-S01": ("E2", "apsolutni objekat qadr dijeli glagol 'poznaju' (dosljedno 22:74)"),
    "094-W008-S03": ("E2", "-tum sadržan u glagolskom prilogu 'napustivši' (fused)"),
    "094-W011-S01": ("E2", "idiom taraka warāʾa ẓuhūrikum sadržan u 'napustivši' (fused)"),
    "094-W012-S01": ("E2", "idiom 'iza leđa' sadržan u 'napustivši' (fused)"),
    "094-W012-S02": ("E2", "idiom 'iza leđa vaših' sadržan u 'napustivši' (fused)"),
    "094-W026-S01": ("E1", LREQ), "104-W014-S01": ("E1", LREQ), "107-W008-S01": ("E1", LREQ),
    "137-W011-S01": ("E1", LREQ), "153-W010-S01": ("E1", LREQ),
    "094-W029-S01": ("E1", INS + ": 'tako'"),
    "099-W027-S01": ("E2", INS + ": 'zasađeni'"),
    "099-W031-S01": ("E2", CORR), "141-W015-S01": ("E2", CORR),
    "099-W037-S01": ("E1", INS + ": 'tek'"),
    "100-W001-S02": ("E1", "jaʿala → 'drže da'; kopula 'su' bez arapskog segmenta (inserted)"),
    "100-W010-S01": ("E1", BIGH), "108-W011-S01": ("E1", BIGH), "140-W007-S01": ("E1", BIGH), "144-W033-S01": ("E1", BIGH),
    "100-W015-S01": ("E1", INS + ": 'Ga'"),
    "101-W008-S02": ("E1", NEMA), "101-W009-S01": ("E1", NEMA), "101-W010-S01": ("E1", NEMA), "101-W010-S02": ("E1", NEMA),
    "163-W001-S01": ("E1", NEMA), "163-W003-S01": ("E1", NEMA),
    "104-W007-S01": ("E1", INS + ": 'ih'"),
    "104-W008-S02": ("E2", "li-nafsihi → li- 'u korist', nafs 'svoju' (dosljedno 27:40, 41:46)"),
    "104-W008-S03": ("E2", "li-nafsihi → nafs 'svoju' (dosljedno 27:40, 41:46)"),
    "104-W010-S01": ("E1", "izostavljeni ponovljeni predikat 'slijep' dijeli glagol; 'na to' inserted"),
    "105-W005-S01": ("E1", INS + ": 'to'"),
    "107-W007-S01": ("E2", DA + ": 'da nadzireš'"), "107-W009-S01": ("E2", DA + ": 'da nadzireš'"),
    "107-W010-S02": ("E1", "NEG nosi samo 'niti'; kopula 'si' inserted (COMMON: NEG samo 'ne/ni')"),
    "108-W013-S01": ("E1", "ka- → poredbeno 'Kao … tako'"), "108-W013-S02": ("E1", "ḏālika → deiktično 'njima'; 'i' inserted"),
    "108-W015-S01": ("E1", LIKULL), "112-W003-S01": ("E1", LIKULL),
    "109-W005-S01": ("E2", P_UNEXP + ": pripremno la- uz in (zakletveni sadržaj 'da' nosi la- odgovora, COMMON 12:35)"),
    "109-W008-S01": ("E2", "zakletveno la- odgovora → 'da' (COMMON, 12:35, 12:66)"),
    "110-W005-S01": ("E2", "negativna konkordancija 'ni' bez vlastitog segmenta ide NEG-u (COMMON 36:21)"),
    "111-W012-S01": ("E1", "qubulan → 'pred' (fused s ʿalā 'pred njih')"),
    "111-W015-S03": ({"targets_from": "E1", "drop": ["bi"], "add": ["oni,"]},
                     "mā kānū li-yuʾminū: -ū glagola dijeli eksplicitno 'oni' (dosljedno 10:13, 10:74, 7:101)"),
    "113-W008-S02": ("E1", "drugo li- koordiniranog glagola dijeli zajedničko 'da' (kao zajednički pomoćni)"),
    "114-W014-S01": ("E2", INS + ": 'dobro'"),
    "118-W002-S02": ("E1", RESR), "119-W005-S02": ("E1", RESR), "121-W003-S02": ("E1", RESR), "164-W026-S02": ("E1", RESR),
    "119-W002-S02": ("E1", "mā lakum → 'zašto'; -kum → lice glagola 'jedete' (dosljedno 14:12)"),
    "121-W020-S01": ("E1", P_UNEXP + ": la- uz inna; 'sigurno' nosi inna (COMMON, dosljedno 7:60)"),
    "122-W023-S01": ("E1", KANAF), "138-W025-S01": ("E1", KANAF), "140-W019-S01": ("E1", KANAF), "156-W011-S01": ("E1", KANAF),
    "139-W013-S01": ("E1", KANAF + "; 'plod' inserted"),
    "123-W001-S02": ({"targets_from": "E1", "drop": ["Isto"]}, KADH),
    "123-W001-S03": ({"targets_from": "E1", "drop": ["Isto"]}, KADH),
    "129-W001-S02": ({"targets_from": "E1", "drop": ["isto"]}, KADH),
    "129-W001-S03": ({"targets_from": "E1", "drop": ["isto"]}, KADH),
    "137-W001-S02": ({"targets_from": "E1", "drop": ["isto"]}, KADH),
    "137-W001-S03": ({"targets_from": "E1", "drop": ["isto"]}, KADH),
    "124-W019-S01": ("E1", "ponovljeno 'će' uz izostavljeni ponovljeni glagol nosi isti sa-"),
    "124-W020-S01": ("E2", "allaḏīna ajramū sažeto u imenicu 'Prestupnike': REL dijeli imenicu (dosljedno 16:118, 22:17, 83:29)"),
    "146-W002-S01": ("E2", "allaḏīna hādū → 'Jevrejima': REL dijeli imenicu (dosljedno 16:118, 22:17, 62:6)"),
    "146-W011-S01": ("E1", "izostavljeni ponovljeni ḥarramnā dijeli token prethodnog glagola"),
    "146-W011-S02": ("E1", "sufiks izostavljenog ponovljenog glagola → zajednički 'smo'"),
    "125-W001-S02": ("E1", "pogodbeno-relativno man → 'Onome koga' (relativni izraz)"),
    "125-W009-S02": ("E1", "man → 'onome kome' (relativni izraz)"),
    "125-W024-S02": ("E1", "dublet 'gnusoba - šejtan' za jedno rijs; crtica unutar dubleta dio je izraza (COMMON)"),
    "127-W006-S02": ("E1", "samostalno huwa + buduća kopula imenske rečenice: 'će' ide zamjenici (COMMON 40:6)"),
    "128-W002-S02": ("E1", P_UNEXP + ": objektni -hum nije izražen; 'sve' nosi jamīʿ"),
    "128-W025-S02": ("E2", KHALID), "128-W026-S01": ("E2", KHALID),
    "128-W028-S01": ("E1", ILLAMA), "128-W029-S01": ("E1", ILLAMA), "128-W030-S01": ("E1", ILLAMA),
    "130-W007-S01": ("E1", INS + ": 'redova'"),
    "130-W024-S01": ("E2", "anfus → 'sami … sebe' (dosljedno 9:42, 9:70)"),
    "132-W003-S01": ("E1", "min → 'prema'; 'već' inserted"), "132-W003-S02": ("E1", "mā → 'tome kako'"),
    "135-W004-S01": ("E1", P_UNEXP + ": ʿalā u ʿalā makānatikum (dosljedno 11:93, 11:121)"),
    "135-W005-S01": ("E1", "makāna → 'sve što možeš' (dosljedno 11:93)"),
    "135-W006-S02": ("E1", PARTN + ": ime inna -ī → 'ću, ja;'"), "135-W007-S01": ("E1", PARTN + ": ʿāmil → 'činit'"),
    "135-W013-S01": ("E1", "ʿāqiba → 'kraj'"), "135-W014-S02": ("E1", "ad-dār (lijepo boravište) → 'sretan'"),
    "136-W012-S01": ("E1", P_UNEXP + ": bi- u bi-zaʿmihim preoblikovan u 'tvrde oni'"),
    "138-W011-S01": ("E1", P_UNEXP + ": bi- u bi-zaʿmihim (dosljedno 6:136)"),
    "136-W016-S01": ("E1", "kāna + li- → kāna 'je', li- 'namijenjeno' (dosljedno S009)"),
    "136-W017-S01": ("E1", "li- → 'namijenjeno' (kāna + li-)"),
    "136-W023-S01": ("E1", "kāna + li- → kāna 'je'"), "136-W024-S01": ("E1", "li- → 'određeno za'"),
    "136-W030-S01": ("E2", P_UNEXP + ": mā u sāʾa mā; 'Kako ružno' nosi sāʾa (dosljedno 16:59)"),
    "138-W015-S02": ("E2", "anʿām → 'stoke'; egzistencijalno 'Ima' inserted (dosljedno 3:75, 9:49)"),
    "139-W018-S02": ("E1", INS + ": 'Allah' (3MS bez zamjenice)"),
    "141-W006-S02": ("E2", "ġayr → 'ne-' [0,2] u 'nepoduprte' (stvarna granica)"),
    "141-W007-S01": ("E2", "maʿrūš → '-poduprte' [2,11]"),
    "143-W002-S01": ("E1", INS + ": 'životinja'"),
    "145-W011-S02": ("E2", "objektni -hu → 'ma šta' (ono što se jede)"),
    "145-W012-S01": ("E2", "illā → 'drugo osim'"),
    "145-W029-S02": ("E2", "resumptivni -hi → relativ 'što' (COMMON)"),
    "145-W030-S02": ("E2", "man → 'li ko'; pomoćni 'bude' pripada glagolu koji gradi"),
    "145-W031-S01": ("E2", "pomoćni 'bude' pripada glagolu 'primoran' koji gradi (COMMON)"),
    "145-W033-S01": ("E1", INS + ": 'to'"), "145-W035-S01": ("E1", INS + ": 'u tome'"),
    "148-W009-S01": ("E1", "drugo 'ni' korelacije nosi wa + NEG (COMMON 93:3)"),
    "151-W003-S01": ("E1", DA + "; 'vam' inserted"),
    "151-W036-S01": ("E2", "illā bi-l-ḥaqq → illā 'osim', bi- 'kada to zahtijeva', ḥaqq 'pravda' (dosljedno 25:68)"),
    "151-W037-S01": ("E2", "bi- → 'kada to … zahtijeva' (dosljedno 25:68 'kad se na to ima')"),
    "151-W037-S03": ("E2", "ḥaqq → 'pravda' (dosljedno 25:68 'pravo')"),
    "151-W040-S02": ("E2", RESD), "152-W033-S02": ("E2", RESD), "153-W015-S02": ("E2", RESD),
    "154-W008-S01": ("E2", INS + ": 'prema njoj'"),
    "157-W002-S01": ("E2", DA + "; 'ne' inserted (ponavlja an iz 6:156)"),
    "157-W004-S02": ("E2", "ime anna -nā dijeli 'nama' istog referenta (dosljedno S009 12/120)"),
    "157-W011-S02": ("E2", "qad → 'eto' (dosljedno 3:143, 8:19)"),
    "157-W018-S01": ("E1", INS + ": 'i'"),
    "158-W005-S02": ("E1", "ponovljeno 'im' uz izostavljeni objekat drugog glagola nosi isti sufiks"),
    "158-W011-S01": ("E1", "izostavljeni treći yaʾtiya dijeli token 'dođe'"),
    "158-W023-S01": ("E2", PARTN + ": 'će' nosi -hā, īmān samo 'to što … tada vjerovati'"),
    "158-W032-S02": ("E2", "fī īmānihā → 'kao vjernik' (posjednik sadržan u imenici, fused)"),
    "159-W009-S01": ("E2", "fī šayʾin → 'ništa' (fused, kao iscrpni min)"),
    "159-W013-S01": ("E1", "ilā → dativ 'Allahu'; 'predat' inserted"),
}
D = {"S006-A" + k[:3] + "-" + k[4:]: v for k, v in D0.items()}
D.update({
    "S006-A071-B063": ("INS", "'istinska' — Mehanovićev pridjev bez arapskog segmenta (dosljedno 8:2 'Pravi')"),
    "S006-A123-B001": ("INS", "'Isto' — pojačivač u 'Isto tako' (dosljedno 25:31)"),
    "S006-A129-B002": ("INS", "'isto' — pojačivač u 'Tako isto' (dosljedno 29:47)"),
    "S006-A137-B004": ("INS", "'isto' — pojačivač u 'isto tako' (dosljedno 18:19)"),
})

if __name__ == "__main__":
    run("S006_El-Enam", D)
