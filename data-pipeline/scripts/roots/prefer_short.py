# -*- coding: utf-8 -*-
"""
Prednost kraćim ajetima: za svaku karticu među Dictionary alternativama s ISTOM vidljivom riječju (isti
oblik, ista klitika → kratko značenje ostaje tačno) bira se najkraći ajet. Rasponi se računaju iz QAC
indeksa riječi u zaključanom Uthmani tekstu (bez traženja prvog jednakog stringa).

  uv run scripts/roots/prefer_short.py <VERIFIED.json> <SHORT.json> [prag_riječi]
Ispis: koliko kartica je promijenjeno i koliko ih je i dalje duže od praga (kandidati za izvod).
"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from verify_root_panel import verse, words_with_spans  # noqa: E402

sys.stdout.reconfigure(encoding="utf-8")


def main():
    src, dst = sys.argv[1], sys.argv[2]
    limit = int(sys.argv[3]) if len(sys.argv) > 3 else 12
    d = json.load(open(src, encoding="utf-8"))
    changed, long_cards = 0, []
    for root in d["roots"]:
        for sec in ("nouns", "verbs"):
            for c in root[sec]:
                best = None
                for alt in c["alternatives"]:
                    if alt["highlight_word"] != c["form"]:
                        continue
                    s, a, w = alt["qac_location"][:3]
                    u, meh = verse(s, a)
                    ws = words_with_spans(u["ayah_text"])
                    if w > len(ws) or ws[w - 1][2] != c["form"]:
                        continue
                    cand = (len(ws), (s, a), alt, u["ayah_text"], meh, ws[w - 1])
                    if best is None or cand[:2] < best[:2]:
                        best = cand
                cur = len(words_with_spans(c["arabic_full"]))
                if best and best[0] < cur:
                    n_words, ref, alt, full, meh, (st, en, _) = best
                    c.update({"qac_location": alt["qac_location"], "features": alt["features"], "lemma": alt["lemma"],
                              "ayah_ref": alt["ayah_ref"], "source_ref": alt["ayah_ref"], "arabic": full, "arabic_full": full,
                              "bosnian": meh, "bosnian_full": meh, "highlight_word": c["form"],
                              "highlight_word_index": alt["qac_location"][2], "highlight_span": {"start": st, "end": en},
                              "meaning_en": alt.get("gloss_en", c.get("meaning_en"))})
                    changed += 1
                    cur = n_words
                if cur > limit:
                    long_cards.append(c["id"])
    json.dump(d, open(dst, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"promijenjeno na kraći ajet: {changed}; i dalje duže od {limit} riječi: {len(long_cards)}")


if __name__ == "__main__":
    main()
