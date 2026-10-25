# -*- coding: utf-8 -*-
"""
Provjera i normalizacija ROOT_PANEL_V7 JSON-a (izvor: ChatGPT isporuka) prema zaključanim izvorima
pipeline-a: QAC morphology 0.4, Tanzil Uthmani 1.1 (bez basmala prefiksa u 1. ajetu), Mehanović v1.1.0.

  uv run scripts/roots/verify_root_panel.py <ulazni APP.json> <izlazni APP.json>

Svaka kartica mora proći: QAC lokacija ima isti ROOT/POS/LEM; arapski tekst je 1:1 cijeli ajet ili
kontinuirani izvod; raspon bojenja daje tačno ciljnu riječ; indeks cijele riječi odgovara QAC riječi;
bosanski tekst je 1:1 Mehanović ili kontinuirani izvod. Basmala koju Tanzil prefiksira 1. ajetu se uklanja
i rasponi se pomjeraju (ista pravila kao V13.1 snapshot).
"""
import json
import os
import re
import sys
from collections import defaultdict

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "v131"))
from common import QAC_MORPH, load_mehanovic_surah, load_uthmani_surah  # noqa: E402

sys.stdout.reconfigure(encoding="utf-8")

_uth, _meh = {}, {}


def verse(s, a):
    if s not in _uth:
        _uth[s] = load_uthmani_surah(s)
        _meh[s] = load_mehanovic_surah(s)
    return _uth[s][a], _meh[s][a]["text"]


def load_morph():
    m = {}
    with open(QAC_MORPH, encoding="utf-8") as f:
        for line in f:
            mm = re.match(r"\((\d+):(\d+):(\d+):(\d+)\)\t(\S*)\t(\S+)\t(\S+)", line)
            if mm:
                loc = tuple(int(x) for x in mm.groups()[:4])
                feats = mm.group(7).split("|")
                root = next((x[5:] for x in feats if x.startswith("ROOT:")), None)
                lem = next((x[4:] for x in feats if x.startswith("LEM:")), None)
                m[loc] = {"pos": mm.group(6), "root": root, "lemma": lem, "features": mm.group(7)}
    return m


def words_with_spans(text):
    """Leksičke riječi (bez samostalnih pauza) s rasponima u kodnim tačkama."""
    out = []
    for mm in re.finditer(r"\S+", text):
        if any(c.isalpha() for c in mm.group(0)):
            out.append((mm.start(), mm.end(), mm.group(0)))
    return out


def norm_bs(t):
    return re.sub(r"\s+", " ", t.replace("…", "")).strip()


def main():
    src, dst = sys.argv[1], sys.argv[2]
    d = json.load(open(src, encoding="utf-8"))
    morph = load_morph()
    problems = defaultdict(list)
    fixed = defaultdict(int)
    n = 0
    for root in d["roots"]:
        for sec, pos in (("nouns", "N"), ("verbs", "V")):
            seen_forms = set()
            for c in root[sec]:
                n += 1
                cid = c["id"]
                loc = tuple(c["qac_location"])
                m = morph.get(loc)
                if not m or m["root"] != root["root_bw"] or m["pos"] != pos or m["lemma"] != c["lemma"]:
                    problems[cid].append(f"QAC {loc}: {m} ≠ root={root['root_bw']} pos={pos} lem={c['lemma']}")
                s, a = loc[0], loc[1]
                u, meh = verse(s, a)
                full = u["ayah_text"]
                ar = c["arabic"]
                st, en = c["highlight_span"]["start"], c["highlight_span"]["end"]
                if ar != full and u["rule"] and ar == u["raw_line_text"]:
                    shift = len(u["raw_line_text"]) - len(full)
                    ar, st, en = full, st - shift, en - shift
                    fixed["basmala_stripped"] += 1
                if ar == full:
                    off = 0
                elif full.count(ar) == 1:
                    off = full.index(ar)
                else:
                    problems[cid].append(f"arapski nije 1:1 Uthmani {s}:{a}")
                    continue
                if ar[st:en] != c["highlight_word"] or c["highlight_word"] != c["form"]:
                    problems[cid].append(f"raspon {st}:{en}='{ar[st:en]}' ≠ '{c['highlight_word']}' / form '{c['form']}'")
                ws = words_with_spans(full)
                idx = [i for i, (a0, a1, _) in enumerate(ws, 1) if a0 == st + off and a1 == en + off]
                if idx != [loc[2]]:
                    problems[cid].append(f"indeks riječi {idx} ≠ QAC riječ {loc[2]}")
                if norm_bs(c["bosnian"]) != norm_bs(meh) and norm_bs(c["bosnian"]) not in norm_bs(meh):
                    problems[cid].append("bosanski nije 1:1 Mehanović")
                key = (c["form"], c.get("group_key"))
                if c["form"] in seen_forms:
                    problems[cid].append(f"dupli vidljivi oblik {c['form']}")
                seen_forms.add(c["form"])
                c["arabic"], c["highlight_span"] = ar, {"start": st, "end": en}
                c["highlight_word_index"] = loc[2]
                c["arabic_full"], c["bosnian_full"] = full, meh
                c["bosnian"] = c["bosnian"] if norm_bs(c["bosnian"]) != norm_bs(meh) else meh
    # Riječi aktuelne sure: indeksi po QAC riječi (bez basmale).
    for v in d["surah_verses"]:
        u, meh = verse(v["sura"], v["ayah"])
        if v["arabic"] != u["ayah_text"]:
            if u["rule"] and v["arabic"] == u["raw_line_text"]:
                shift = len(u["raw_line_text"]) - len(u["ayah_text"])
                v["arabic"] = u["ayah_text"]
                for w in v["words"]:
                    w["start"] -= shift
                    w["end"] -= shift
                    w["word_index"] = w["qac_word_index"]
                fixed["surah_verse_basmala_stripped"] += 1
            else:
                problems[v["ref"]].append("ajet sure nije 1:1 Uthmani")
        for w in v["words"]:
            if v["arabic"][w["start"]:w["end"]] != w["word"]:
                problems[v["ref"]].append(f"riječ {w['word']} raspon pogrešan")
            if w.get("clickable"):
                sl = tuple(w["stem_qac_location"])
                m = morph.get(sl)
                if not m or m["root"] != w["root_bw"] or m["pos"] not in ("N", "V"):
                    problems[v["ref"]].append(f"klik {w['word']}: {m}")
    # Obuhvat: svaka N lema i svaka V lema korijena ima bar jednu karticu.
    for root in d["roots"]:
        have = {("N", c["lemma"]) for c in root["nouns"]} | {("V", c["lemma"]) for c in root["verbs"]}
        need = {(m["pos"], m["lemma"]) for m in morph.values() if m["root"] == root["root_bw"] and m["pos"] in ("N", "V")}
        miss = need - have
        if miss:
            problems[root["root_bw"]].append(f"nedostaju leme: {sorted(miss)}")
    json.dump(d, open(dst, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"kartica {n}; ispravke {dict(fixed)}; problemi {sum(len(v) for v in problems.values())}")
    for k, v in list(problems.items())[:40]:
        print(" ", k, "|", "; ".join(v))


if __name__ == "__main__":
    main()
