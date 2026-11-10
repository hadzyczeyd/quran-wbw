# Preostale sure 2–29 (V13.1)

Nalog korisnika (2026-11-05): uraditi sure 2–29, prvo one s kraćim ajetima
(redoslijed po prosječnom broju riječi po ajetu), jedna po jedna, punim V13.1 tokom.

| Red | Sura | Ajeta | Riječi | Riječi/ajet | Status |
|---|---|---|---|---|---|
| 1 | 26 Eš-Šu'ara | 227 | 1318 | 5.8 | gotovo (2026-11-05) |
| 2 | 15 El-Hidžr | 99 | 655 | 6.6 | gotovo (2026-11-05) |
| 3 | 23 El-Mu'minun | 118 | 1050 | 8.9 | gotovo (2026-11-05) |
| 4 | 19 Merjem | 98 | 961 | 9.8 | gotovo (2026-11-05) |
| 5 | 20 Ta-ha | 135 | 1335 | 9.9 | gotovo (2026-11-05) |
| 6 | 21 El-Enbija | 112 | 1169 | 10.4 | gotovo (2026-11-05) |
| 7 | 25 El-Furkan | 77 | 893 | 11.6 | gotovo (2026-11-05) |
| 8 | 27 En-Neml | 93 | 1151 | 12.4 | gotovo (2026-11-05) |
| 9 | 17 El-Isra | 111 | 1556 | 14.0 | gotovo (2026-11-05) |
| 10 | 29 El-Ankebut | 69 | 976 | 14.1 | gotovo (2026-11-05) |
| 11 | 18 El-Kehf | 110 | 1579 | 14.4 | gotovo (2026-11-06) |
| 12 | 16 En-Nahl | 128 | 1844 | 14.4 | gotovo (2026-11-06) |
| 13 | 11 Hud | 123 | 1917 | 15.6 | gotovo (2026-11-06) |
| 14 | 12 Jusuf | 111 | 1777 | 16.0 | gotovo (2026-11-06) |
| 15 | 14 Ibrahim | 52 | 830 | 16.0 | gotovo (2026-11-06) |
| 16 | 7 El-A'raf | 206 | 3320 | 16.1 | gotovo (2026-11-06) |
| 17 | 28 El-Kasas | 88 | 1430 | 16.2 | gotovo (2026-11-06) |
| 18 | 22 El-Hadždž | 78 | 1274 | 16.3 | gotovo (2026-11-06) |
| 19 | 8 El-Enfal | 75 | 1233 | 16.4 | gotovo (2026-11-06) |
| 20 | 10 Junus | 109 | 1833 | 16.8 | gotovo (2026-11-06) |
| 21 | 3 Alu Imran | 200 | 3481 | 17.4 | gotovo (2026-11-08) |
| 22 | 6 El-En'am | 165 | 3050 | 18.5 | gotovo (2026-11-10) |
| 23 | 9 Et-Tevba | 129 | 2498 | 19.4 | gotovo (2026-11-09) |
| 24 | 13 Er-Ra'd | 43 | 853 | 19.8 | gotovo (2026-11-09) |
| 25 | 24 En-Nur | 64 | 1316 | 20.6 | gotovo (2026-11-09) |
| 26 | 4 En-Nisa | 176 | 3747 | 21.3 | |
| 27 | 2 El-Bekara | 286 | 6116 | 21.4 | |
| 28 | 5 El-Maida | 120 | 2804 | 23.4 | gotovo (2026-11-10) |

Status: "u radu" → "gotovo (commit …)". Bilješke o konvencijama/greškama izvora po suri ispod.

## Bilješke
- 26: 26:220 greška izvora (Mehanović „Silni i Milostivi“ umjesto as-samīʿ al-ʿalīm) → DOCUMENTED_EXCEPTIONS (SOURCE_TRANSLATION_MISMATCH), QA 90 redova.
- DONE 2026-11-05 dosljednost: ka-ḏālika „Eto, tako“ — većina (42:3, 42:7, 44:54, 47:3, 40:34, 40:74, 54:35) DEM → 'Eto,'; 30:28, 30:59, 37:80, 37:110, 37:121, 37:131 imaju 'Eto,' inserted → ispravljeno (CONSISTENCY_FIXES; i 40:34, 40:74, 54:35 'tako' skinut s DEM), reimportovano.
- DONE 2026-11-05: crtica '-' ne nosi fa-/wa- (15:3, 15:22, 30:16, 30:39, 30:44×2 → UNEXPRESSED), reimportovano.
- DONE 2026-11-05: 'da' u 'neće da' ide uz glagol (većina: 23:74, 34:8, 36:35, 41:52, 57:24) → ispravljeno 26:3 i 26:190, reimportovano.
- 20: 20:129 propust izvora (Mehanović bez „wa-ajalun musammā“) → DOCUMENTED_EXCEPTIONS (SOURCE_TRANSLATION_OMISSION), QA 90 redova.
- DONE 2026-11-05: subḥāna — optativno 'neka je/si' pripada subḥāna, obična kopula 'je' inserted; 30:40 ispravljen ('je' inserted); 34:41 je ispravan ('si' nosi -ka); reimportovano.
- 21: 21:67 u izvoru duplikat 21:66 → odobrena zamjena prijevodom Besima Korkuta (scripts/v131/MEHANOVIC_OVERRIDES.json, napomena na /izvori).
- DONE 2026-11-05: neodređenici 'jedan/neki/kakav' uz neodređenu imenicu — većina objavljenih (≈50) ih veže na imenicu, ≈31 inserted (npr. 20:10 'nekakvu', 26:29 'nekoga', 26:154 'jedno', 26:189 'jednog', 21:111 'izvjesno'?) → 27 mjesta u 13 sura (20, 21, 25, 26, 30, 36, 37, 42, 48, 49, 54, 62, 77) vezano na imenicu, reimportovano; 'ikakav' uz negaciju (25:3, 72:21) i 'neka je' (37:109, 181) ostaju inserted.
- DONE 2026-11-06: laʿalla 'bi' uz glagol u 21:31 i 21:58 (laʿalla → samo 'da'); 46:23 'ste' je kopula ('ste vi narod'), ispravno.
- DONE 2026-11-05: al- iscrpnosti ('Sva/Svaka hvala', 'svi ljudi', 'svih svjetova') → DET (većina: 1:2, 34:1, 39:29/74/75, 40:65, 43:33); ispravljeno 15 mjesta u 17, 21, 26, 30, 35, 59, 62, 64, 66, 77; 'sve/svi' uz kull/jamīʿ ili kao objekat ('sve zna') ostaje kako jeste.
- 29: izvorni tipo 29:47 'Knjigu-i' (bez razmaka); 29:60 Mehanović ʿalīm prevodi 'Svevideći' (njegov izbor).
- 18: propusti izvora 18:26 (nebesa i Zemlja u ġaybu s-samāwāti wa-l-arḍ) i 18:86 (vokativ 'O Zulkarnejne') → DOCUMENTED_EXCEPTIONS (SOURCE_TRANSLATION_OMISSION), QA 90.
- 16: propust izvora 16:106 (wa-qalbuhu muṭmaʾinnun bi-l-īmān, W010–W012) → DOCUMENTED_EXCEPTIONS, QA 90. Konzistencija: iza samostalnog hum zamjenica nosi samo hum (16:16, 16:20, 16:72 → -ūna fused/pomoćni).
- DONE 2026-11-06: 63:7 W003-S02 (-ūna) s 'Oni' (hum) → fused 'govore:', reimportovano.
- DONE 2026-11-06: pravila li-/laʿalla/fa sababiyya/hum zapisana u COMMON.md; fa sababiyya → 'pa da' na fa (većina objavljenih: 17:22, 17:29, 33:32, 80:4) — 16:94 i 26:102 usklađeni, reimportovano.
- DONE 2026-11-06: 16:44 W012-S02 (-ūna od yatafakkarūn) je na 'oni', a ime laʿalla već nosi 'oni' → 'bi' (većina: 12:46, 20:113, 32:3, 32:21, 44:58), reimportovano.
- 28: propust izvora 28:50 (wa-man aḍallu mimmani ttabaʿa hawāhu, W009–W013; detektovani blok W012–W013) → DOCUMENTED_EXCEPTIONS (SOURCE_TRANSLATION_OMISSION), QA 90.
- 22: izvorni tipfeleri (samo prijavljeno): 22:37 'bogogojaznost', 22:40 'pomažuv -Allah', 22:54 'Kur 'an' (razmak), 22:64 '?' iza izjavne rečenice.
- DONE 2026-11-06: COMMON dopunjen — particip/imenica prevedena glagolom: pomoćni nosi zamjenicu/ime (SECOND u S022 je to prekršio, THIRD vratio); 22:71 'nikakav' na sulṭān (kao 7:33), reimportovano.
- 8: izvor (samo prijavljeno): 8:6 'naočigled svoj', 8:7 i 8:58 '-Allah' bez razmaka; QAC 0.4 u 8:43 W008 spaja glagol i -ka u S01.
- 10: izvor (samo prijavljeno): 10:58 'blagodarnosti' (faḍl), 10:64/108 razmaci uz crticu, 10:87/90 malo 'mi' za Allaha, 10:88 drugo rabbanā 'Gospodaru moj', 10:93 'Israllove'.
- DONE 2026-11-06: 7:125 ime inna 'Mi' nosi i 'ćemo' (particip munqalibūn samo leksički), dosljedno 10:20, 10:102; reimportovano.
- Pauza 2026-11-06 po nalogu korisnika; sljedeća: 3 Alu Imran.
- 3: izvor (samo prijavljeno): 3:19 'sviđa', 3:199 'svidjeti' (svodi/svesti), 3:41 'išaretorn', 3:81 'Potvrđujerno', 3:98 'Allahova ajete', interpunkcija 36/78/154, veliko 'A' iza zareza u 140; li-n-nās (110) i fī l-amr (159) nisu prevedeni (pojedinačno UNEXPRESSED, bez bloka).
- 3: pomoćni 'će' participa/imenice prevedene glagolom uz običnu imeničku subjekat-frazu ostaje uz glagolski izraz (185 'će okusiti' kao 21:35, 29:57; 198 'će ugostiti'); SECOND/THIRD su ga bili prebacili na subjekat → vraćeno kroz CONSISTENCY_FIXES.
- Pauza 2026-11-08 po nalogu korisnika (deploy nakon sure 3); sljedeća: 6 El-En'am.
- 13: izvor (samo prijavljeno): 13:33 bez negacije za lā yaʿlamu ('što on zna da postoji', NEG pojedinačno UNEXPRESSED) i malo 'on' za Allaha; 13:31 'rade-sve' bez razmaka; 13:16 neobični navodnici.
- 24: izvor (samo prijavljeno): 24:23 ʿaḏābun ʿaẓīm → 'patnja bolna'; neprevedeno (pojedinačno UNEXPRESSED): 24:13 ʿalayhi, 24:32 minkum, 24:54 innamā, 24:55 baʿd u min baʿdi ḫawfihim.
- 9: greška izvora 9:15 ('Onaj Koji sve čuje i mudar je' za ʿalīmun ḥakīm) i 9:98 ('Onaj Koji sve zna i mudar je' za samīʿun ʿalīm) → ʿalīm/samīʿ pojedinačno UNEXPRESSED, neodgovarajući tokeni inserted (kao 26:220, bez bloka). Ostalo (samo prijavljeno): 9:69 'bili poništena', 9:106 'AAllah', 9:118 'bilo im se stisnula', 9:124 navodnik/velika slova, 9:120 ḥawlahum 'u njegovoj blizini'; ʿasā neprevedeno 9:18/102, innamā 9:18/55/85/93.
- 9: COMMON potvrđeno: pomoćni pripada i glagolu koji gradi (38, 42, 83); ime inna/anna → zamjenica + kopula; amara bi- → bi- nosi 'da' (kao 7:28; u 3:21/110/114 'da se …' ostalo inserted — kandidat za usklađivanje).
- 6: greške izvora (samo prijavljeno): 63 'zahvalnil', 74 'očitaj', 161 'pravovjemika'; navodnici u 46, 80, 93, 128, 131.
  Konvencije: ka-ḏālika 'Isto tako' → oba na 'tako' ('isto' inserted); 'u obožavanju' uz ašraka inserted; law tarā → 'da' | 'ti je vidjeti';
  laysa lahum 'neće imati' → laysa 'ni ne-', -hum '-će', li- 'imati'; 'nema' (lā/lam … lahu) → ne|ma; bi-ġayri → 'ne' (bi- + ġayr).
  THIRD je negativnu konkordanciju ('nikakve sumnje' 12, 23, 81, 91, 119, 158) prebacio na NEG; vraćeno CONSISTENCY_FIXES (imenica s vlastitim segmentom nosi 'nikakav', praksa 30:5).
  6:17 li- uz kāšif → UNEXPRESSED (FIRST+SECOND+THIRD); 10:107 isti izraz ima li- → 'je' (kandidat za usklađivanje).
- 5: greške izvora (samo prijavljeno): tipfeleri 3 'žtrvenicima', 4 'sviđa' (svodi), 12 'lsrailovih', 14 'medu', 34 'opršta', 66 'lndžila', 72 'lsrailovi';
  108 'da se ne plaše' ('ne' bez arapske negacije, inserted); 117 'im' umjesto -nī; neprevedeno 11 i 12 ʿankum, 107 al-awlayān.
  Konvencije: zamjenica razdvajanja → kopula + 'baš' (9:10); inna + la- → inna 'jer/da' + 'doista', la- UNEXPRESSED; ḏālika bi- → 'zato' (fused);
  neponovljeni prijedlog (ʿalā/ʿan/bi-/bayna) → UNEXPRESSED; iscrpni min uz negiranu imenicu → token imenice.
