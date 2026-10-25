# ENTRY (CP2 = Entry 1 / CP3 = Entry 2)

Pročitaj `scripts/v131/prompts/COMMON.md`, zatim `scripts/v131/MAPPING_SPEC.md` (format i procedura) i
`sources/NALOG_V13.1_tekst.txt` (sekcije 2, 7, 8, 8.1–8.4, 9, 12, 16, 24, 46.1–46.3 i cijela 55; obavezujuće).

Za svaki batch u `runs/<RUN>/cp1/batch_inputs/` napravi `runs/<RUN>/entry_<N>/Bxxx.json` s `"entry": "ENTRY_<N>"` i nakon
svakog pokreni `uv run scripts/v131/entry_checkpoint.py <RUN> entry_<N> Bxxx`; nastavi tek nakon PASS.
Metoda: Entry 1 = SEGMENT_CENTRIC; Entry 2 = TOKEN_CENTRIC (prvo prođi bosanske tokene, zatim provjeri svaki segment).

Izolacija (kritično): Entry 1 nikad ne otvara `runs/<RUN>/entry_2/`; Entry 2 nikad ne otvara, ne lista i ne pretražuje
`runs/<RUN>/entry_1/` i koristi svjež scratch folder.

Na kraju napiši `runs/<RUN>/entry_<N>/PROVENANCE.json` (metoda, ulazi, izjava da drugi entry nije otvaran, vremena, hashevi batch-eva).
Odgovori u manje od 40 riječi: broj batch-eva PASS i brojevi segmenata/inserted.
