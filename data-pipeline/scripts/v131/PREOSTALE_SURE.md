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
| 7 | 25 El-Furkan | 77 | 893 | 11.6 | u radu |
| 8 | 27 En-Neml | 93 | 1151 | 12.4 | |
| 9 | 17 El-Isra | 111 | 1556 | 14.0 | |
| 10 | 29 El-Ankebut | 69 | 976 | 14.1 | |
| 11 | 18 El-Kehf | 110 | 1579 | 14.4 | |
| 12 | 16 En-Nahl | 128 | 1844 | 14.4 | |
| 13 | 11 Hud | 123 | 1917 | 15.6 | |
| 14 | 12 Jusuf | 111 | 1777 | 16.0 | |
| 15 | 14 Ibrahim | 52 | 830 | 16.0 | |
| 16 | 7 El-A'raf | 206 | 3320 | 16.1 | |
| 17 | 28 El-Kasas | 88 | 1430 | 16.2 | |
| 18 | 22 El-Hadždž | 78 | 1274 | 16.3 | |
| 19 | 8 El-Enfal | 75 | 1233 | 16.4 | |
| 20 | 10 Junus | 109 | 1833 | 16.8 | |
| 21 | 3 Alu Imran | 200 | 3481 | 17.4 | |
| 22 | 6 El-En'am | 165 | 3050 | 18.5 | |
| 23 | 9 Et-Tevba | 129 | 2498 | 19.4 | |
| 24 | 13 Er-Ra'd | 43 | 853 | 19.8 | |
| 25 | 24 En-Nur | 64 | 1316 | 20.6 | |
| 26 | 4 En-Nisa | 176 | 3747 | 21.3 | |
| 27 | 2 El-Bekara | 286 | 6116 | 21.4 | |
| 28 | 5 El-Maida | 120 | 2804 | 23.4 | |

Status: "u radu" → "gotovo (commit …)". Bilješke o konvencijama/greškama izvora po suri ispod.

## Bilješke
- 26: 26:220 greška izvora (Mehanović „Silni i Milostivi“ umjesto as-samīʿ al-ʿalīm) → DOCUMENTED_EXCEPTIONS (SOURCE_TRANSLATION_MISMATCH), QA 90 redova.
- DONE 2026-11-05 dosljednost: ka-ḏālika „Eto, tako“ — većina (42:3, 42:7, 44:54, 47:3, 40:34, 40:74, 54:35) DEM → 'Eto,'; 30:28, 30:59, 37:80, 37:110, 37:121, 37:131 imaju 'Eto,' inserted → ispravljeno (CONSISTENCY_FIXES; i 40:34, 40:74, 54:35 'tako' skinut s DEM), reimportovano.
- DONE 2026-11-05: crtica '-' ne nosi fa-/wa- (15:3, 15:22, 30:16, 30:39, 30:44×2 → UNEXPRESSED), reimportovano.
- DONE 2026-11-05: 'da' u 'neće da' ide uz glagol (većina: 23:74, 34:8, 36:35, 41:52, 57:24) → ispravljeno 26:3 i 26:190, reimportovano.
- 20: 20:129 propust izvora (Mehanović bez „wa-ajalun musammā“) → DOCUMENTED_EXCEPTIONS (SOURCE_TRANSLATION_OMISSION), QA 90 redova.
- TODO (nakon 21): subḥāna — optativno 'neka je/si' pripada subḥāna, obična kopula 'je' inserted; provjeriti/ispraviti 30:40 ('Čist je' — kopula vezana) i 34:41 ('Uzvišen neka' — 'si/je' nevezano); ostali objavljeni već dosljedni.
- 21: 21:67 u izvoru duplikat 21:66 → odobrena zamjena prijevodom Besima Korkuta (scripts/v131/MEHANOVIC_OVERRIDES.json, napomena na /izvori).
