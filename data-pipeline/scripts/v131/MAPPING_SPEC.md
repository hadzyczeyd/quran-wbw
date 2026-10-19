# QAC DIRECT V13.1 — specifikacija semantičkog unosa (Entry 1 / Entry 2)

Ovo je tehnički format za CP2/CP3. Sadržajna pravila su iz naloga
(`data-pipeline/sources/NALOG_V13.1_tekst.txt`), koji je obavezan i ima
prednost. Prije rada pročitaj u nalogu najmanje odjeljke 2, 7, 8, 8.1–8.4,
9, 12, 16, 24, 46.1–46.3 i 55 (cijeli).

## Ulaz
`runs/<RUN>/cp1/batch_inputs/Bxxx.json` — za svaki ajet: puni Uthmani ajet,
neizmijenjen Mehanovićev tekst, QAC riječi sa segmentima (tag, features,
pronoun_type, lemma/root u Buckwalteru, QAC CSS klasa), QAC engleska
word-by-word glosa (samo pomoć za razumijevanje, nije izlazni podatak) i
bosanski tokeni sa stabilnim ID-ovima (WHITESPACE_PRESERVE_PUNCT_V1 —
interpunkcija je dio tokena; ništa ne odvajaj i ne mijenjaj).

## Izlaz (jedan JSON po batchu)
`runs/<RUN>/<entry_dir>/Bxxx.json`:

```json
{
  "batch_id": "B001",
  "entry": "ENTRY_1",
  "ayahs": [
    {
      "ayah_id": 2,
      "segment_links": [
        {
          "qac_segment_id": "S040-A002-W001-S01",
          "targets": [{"bosnian_token_id": "S040-A002-B001", "part": null}],
          "semantic_role": "kratko: funkcija/značenje segmenta u ajetu",
          "evidence_type": "DIRECT_LEXICAL",
          "bosnian_target_phrase": "Objavljivanje",
          "note": "konkretan razlog veze"
        }
      ],
      "unexpressed_segments": [
        {"qac_segment_id": "...", "reason": "individualno obrazloženje zašto funkcija/sadržaj nije izražen ni u širem izrazu"}
      ],
      "inserted_tokens": [
        {"bosnian_token_id": "...", "reason": "zašto token ne prenosi nijedan QAC segment (provjeren cijeli ajet)"}
      ],
      "review_required": [
        {"id": "segment ili token ID", "reason": "zašto veza nije dokaziva"}
      ]
    }
  ]
}
```

Pravila formata (validator ih provjerava):
- Svaki QAC segment ajeta pojavljuje se tačno jednom: ili u `segment_links`,
  ili u `unexpressed_segments`, ili u `review_required`.
- Svaki bosanski token ajeta mora biti target bar jedne veze ili biti u
  `inserted_tokens` (ili `review_required`).
- `targets` smiju sadržavati samo tokene istog ajeta.
- `part` je `null` ili `[start, end]` (0-based, end-exclusive, Unicode
  codepoint raspon unutar tokena) — samo za MAPPED_BY_TOKEN_PART, kada u
  tokenu postoji stvarna dokaziva unutrašnja granica. Svi poddijelovi jednog
  tokena moraju bez preklapanja i praznina pokriti cijeli token.
- `evidence_type` ∈ DIRECT_LEXICAL, PHRASE_CONTEXT, RELATIVE_CLAUSE_ROLE,
  LEXICALIZED_NEGATION, PRONOUN_CONTEXT, GOVERNED_PHRASE, IDIOMATIC_Mehanovic,
  FUNCTION_CONTEXT.
- Za REL, NEG, PRON, funkcijske segmente, cross-word i one-to-many veze
  `note` mora navesti konkretan kontekstualni osnov i, kod realne
  dvosmislenosti, zašto susjedni kandidat nije izabran (nalog 55.12).
  Generičko „kontekst ajeta“ nije dovoljno.

Statusi (ONE_TO_ONE, ONE_TO_MANY, BY_SEGMENT, BY_TOKEN_PART,
FUSED_MULTI_SEGMENT, inserted…) se NE upisuju ručno — deterministički se
izvode iz veza. Ti odlučuješ samo veze segment ↔ token(i) i obrazloženja.
Ako jedan token nosi više segmenata, samo navedi isti token kao target kod
svakog od tih segmenata; fused/markeri se izvode automatski.

## Postupak po batchu (mikro-checkpoint)
1. Pročitaj ulazni `Bxxx.json` (samo snapshot — ne otvaraj tuđe entry
   direktorije, stare Excel fajlove ni bazu aplikacije).
2. Za svaki ajet: SEMANTIC-FIRST redoslijed iz naloga 55.3; mapiraj svaki
   segment zasebno (46.2); poštuj REL / NEG / PRON / cross-word guardove (55.6–55.10).
3. Zapiši `runs/<RUN>/<entry_dir>/Bxxx.json`.
4. Pokreni validator:
   `uv run scripts/v131/entry_checkpoint.py <RUN> <entry_dir> Bxxx`
   On provjerava format i potpunost, atomski hashira batch i upisuje
   mikro-checkpoint u `<entry_dir>/ENTRY_MANIFEST.json`. Ako javi grešku,
   ispravi samo taj batch i ponovi validator.
5. Tek nakon PASS-a pređi na sljedeći batch.
