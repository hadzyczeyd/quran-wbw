# FIRST (CP5) / SECOND (CP6) / THIRD (CP7)

Pročitaj `scripts/v131/prompts/COMMON.md`, `scripts/v131/review.py` (docstring = format izlaza), `scripts/v131/MAPPING_SPEC.md` i
`sources/NALOG_V13.1_tekst.txt` (sekcije 8, 8.1–8.4, 12, 13 (FIRST) / 14 (SECOND) / 15 (THIRD), 16, 17.1, 46.2, 46.3, cijela 55).

- FIRST = obavezni PUNI semantički audit 100% segmenata, tokena i veza; po ajetu i `translation_completeness` PASS/FAIL + napomena.
- SECOND = NEZAVISNO ciljano ponovno čitanje iz izvora rizičnih/promijenjenih redova; napomene počinju "SEMANTIC_RECHECK:".
- THIRD = završni SEMANTIC_EXCEPTION_RECHECK svih rizičnih/ikad promijenjenih/ikad neusklađenih redova; napomene počinju
  "SEMANTIC_EXCEPTION_RECHECK:".
Svaki red sudi sam iz izvora. SECOND/THIRD ne čitaju `cp5_first/`, `cp6_second/`, `entry_1/`, `entry_2/`, `cp4/` ni `*_SUPERSEDED_*`.
FIRST ne čita `entry_1/`, `entry_2/`, `cp4/`.

ULAZ: svaki `runs/<RUN>/<DIR>/packets/Bxxx.json`. IZLAZ: `runs/<RUN>/<DIR>/Bxxx.json` s `"phase": "<PHASE>"`, jedan unos po SVAKOM
navedenom id-u (segment, token, veza), PASS/FAIL i konkretna bosanska napomena s osnovom. Ispravi samo ono što je dokazivo pogrešno:
FAIL + `correction` (kind LINK ili UNEXPRESSED, targets [[token_id, null ili [start,end]], ...], semantic_role, evidence_type iz
dozvoljene liste, bosnian_target_phrase, note) i FAIL pogođenih redova tokena/veza. Nakon svakog batch-a:
`uv run scripts/v131/review.py check <RUN> <PHASE> Bxxx`; nastavi tek nakon PASS. (<DIR> = cp5_first / cp6_second / cp7_third.)

Odgovori u manje od 60 riječi: broj FAIL, ispravljeni id-evi s kratkim razlogom.
