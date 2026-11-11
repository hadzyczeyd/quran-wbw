# -*- coding: utf-8 -*-
"""
Generator ROOT_PANEL_V7 APP JSON-a (nalog GLAVNI_NALOG_ROOT_PANEL_FINAL_V7) — zamjenjuje ranije ChatGPT isporuke.
Izlaz ide u isti tok kao ranije: verify_root_panel → prefer_short → excerpts/pool → build_app_root_panel.

  uv run scripts/roots/gen_root_panel.py todo <sure...>    → sources/root_panel/GLOSS_TODO.json (kartice bez kratkog značenja)
  uv run scripts/roots/gen_root_panel.py app  <sura>       → sources/root_panel/SURA_<n>_ROOT_PANEL_APP.json

Izvori (odjeljak 3): QAC Dictionary stranica korijena (keš sources/root_panel/dict, fetch_dict.py) daje kandidate;
QAC morphology 0.4 potvrđuje ROOT/POS/LEM i lokacije; Tanzil Uthmani i Mehanović v1.1.0 daju tekst 1:1.
Korijeni iz već objavljenih panela (SURA_*_ROOT_PANEL_SHORT.json) preuzimaju se kakvi jesu, radi dosljednosti
između sura; novi korijeni grade se iz Dictionary + morphology, a kratko značenje dolazi iz GLOSS_DB.json.

Grupe (odjeljak 5): imenica = ROOT+N+LEM; glagol = ROOT+V+vidljivi oblik (stem + subjektni nastavak + energetično -n),
bez prefiksa i objektnih zamjenica, uz normalizaciju samo za poređenje ({→A, tiho slovo s @, ^, sjedišta hamze).
Primjer grupe: najprije oblik bez prefiksa i objektne zamjenice, zatim najkraći ajet, zatim niža referenca.
"""
import collections
import glob
import hashlib
import html as htmlmod
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(__file__))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "v131"))
from common import QAC_MORPH, load_mehanovic_surah, load_uthmani_surah  # noqa: E402
from fetch_dict import path_of, url_of  # noqa: E402
from verify_root_panel import words_with_spans  # noqa: E402

sys.stdout.reconfigure(encoding="utf-8")
D = os.path.join(os.path.dirname(__file__), "..", "..", "sources", "root_panel")
GLOSS_DB = os.path.join(D, "GLOSS_DB.json")
# paneli isporučeni prije generatora (ChatGPT po nalogu V7); samo oni su izvor "objavljenih" korijena
PUBLISHED = {1, *range(70, 115)}
MERGED = {(2, 181): 3, (13, 37): 8, (8, 6): 4, (37, 130): 3}  # QAC riječ koja pokriva dvije Uthmani riječi
BW2AR = dict(zip("'>&<}AbptvjHxd*rzs$SDTZEg_fqklmnhwYyFNKaui~o`{", "ءأؤإئابةتثجحخدذرزسشصضطظعغـفقكلمنهوىيًٌٍَُِّْٰٱ"))

# ---------------------------------------------------------------- izvori
_uth, _meh, _morph, _words = {}, {}, None, None


def verse(s, a):
    if s not in _uth:
        _uth[s] = load_uthmani_surah(s)
        _meh[s] = load_mehanovic_surah(s)
    return _uth[s][a]["ayah_text"], _meh[s][a]["text"]


def morph():
    """(s,a,w) → lista segmenata {loc,bw,pos,features,root,lemma}."""
    global _words
    if _words is None:
        _words = collections.defaultdict(list)
        for line in open(QAC_MORPH, encoding="utf-8"):
            m = re.match(r"\((\d+):(\d+):(\d+):(\d+)\)\t(\S*)\t(\S+)\t(\S+)", line)
            if not m:
                continue
            loc = tuple(int(x) for x in m.groups()[:4])
            f = m[7]
            root = re.search(r"ROOT:([^|]+)", f)
            lem = re.search(r"LEM:([^|]+)", f)
            _words[loc[:3]].append({"loc": list(loc), "bw": m[5], "pos": m[6], "features": f,
                                    "root": root[1] if root else None, "lemma": lem[1] if lem else None})
    return _words


def stem_of(segs, root=None):
    for g in segs:
        if g["pos"] in ("N", "V") and g["root"] and "STEM" in g["features"] and (root is None or g["root"] == root):
            return g
    return None


def uth_spans(s, a):
    """Raspon Uthmani riječi za svaku QAC riječ (1-based)."""
    text, _ = verse(s, a)
    ws = words_with_spans(text)
    mw = MERGED.get((s, a))
    out = {}
    j = 0
    w = 1
    while j < len(ws):
        if w == mw:
            out[w] = (ws[j][0], ws[j + 1][1], text[ws[j][0]:ws[j + 1][1]])
            j += 2
        else:
            out[w] = ws[j]
            j += 1
        w += 1
    return text, out


# ---------------------------------------------------------------- Dictionary
def parse_dict(root):
    p = path_of(root)
    if not os.path.exists(p):
        raise SystemExit(f"nema Dictionary stranice za {root} (fetch_dict.py)")
    t = open(p, encoding="utf-8").read()
    head = re.search(r'Quran Dictionary - <span class="ax">([^<]+)</span>', t)
    rows = re.findall(r'<td class="c1"><span class="l">\((\d+):(\d+):(\d+)\)</span> <i class="ab">([^<]*)</i></td>'
                      r'<td class="c2"><a [^>]*>([^<]*)</a></td>', t)
    cands = [{"loc": [int(s), int(a), int(w)], "transliteration": htmlmod.unescape(tr), "gloss_en": htmlmod.unescape(g),
              "line": i + 1} for i, (s, a, w, tr, g) in enumerate(rows)]
    return (htmlmod.unescape(head[1]).strip() if head else None), cands


def root_display(root):
    return " ".join("أ" if ch == "A" else BW2AR.get(ch, ch) for ch in root)


# ---------------------------------------------------------------- grupe
def norm_key(bw, features="", weak=False):
    bw = re.sub(r".@", "", bw)          # tiho slovo
    for a, b in (("{", "A"), ("^", ""), ("[", ""), ("_", ""), ("#", "'"), (",", ""), ("Y`", "A"), ("`", "A"), ("aAA", "aA")):
        bw = bw.replace(a, b)
    bw = re.sub(r"[>&<}']", "'", bw)  # sjedišta hamze
    bw = re.sub(r"^([nl])~", lambda m: m.group(1), bw)   # početna geminacija iz sandhija
    bw = re.sub(r"^t~", "At~", bw)                      # VIII bez hamzat al-wasl
    bw = re.sub(r"iY$", "iy", bw)
    bw = re.sub(r"aY$", "aA", bw)
    bw = re.sub(r"[FNK]$", "", bw)
    bw = re.sub(r"o$", "", bw)         # završni sukun
    f = features.split("|")
    if ("MOOD:JUS" in f or "IMPV" in f) and not weak:
        bw = re.sub(r"(?<=[^aiuA])[iu]$", "", bw)   # vezni vokal (liaison)
    elif "PERF" in f and "3FS" in f:
        bw = re.sub(r"ti$", "t", bw)
    elif "PERF" in f and "2MP" in f:
        bw = re.sub(r"umu$", "um", bw)
    if "PERF" in f:
        bw = re.sub(r"aw[ui]$", "aw", bw)
    return bw


def subj_parts(segs, stem):
    """Subjektni nastavak i energetično -n koji pripadaju glagolskoj fleksiji (ne objektne zamjenice)."""
    i = segs.index(stem)
    pgn = next((x for x in stem["features"].split("|") if re.fullmatch(r"[123][MF]?[SDP]", x)), None)
    out = []
    for g in segs[i + 1:]:
        f = g["features"]
        if "EMPH" in f:
            out.append(g["bw"])
            continue
        m = re.match(r"SUFFIX\|PRON:(\S+)", f)
        if m and not out and pgn and m[1] == pgn and not re.match(r"[hk]", g["bw"]) and g["bw"] not in ("niY", "niy"):
            out.append(g["bw"])
            continue
        break
    return out


def is_bare(segs, stem):
    """Bez prefiksa i bez objektne zamjenice — najjednostavniji vidljivi oblik."""
    i = segs.index(stem)
    if i > 0:
        return False
    rest = segs[i + 1:]
    subj = subj_parts(segs, stem)
    return len(rest) == len(subj)


def group_key(root, segs, stem):
    if stem["pos"] == "N":
        return f"{root}|N|{stem['lemma']}"
    return f"{root}|V|{norm_key(stem['bw'] + ''.join(subj_parts(segs, stem)), stem['features'], root[-1] in "wy")}"


def build_root(root, current_sura=None):
    header, cands = parse_dict(root)
    words = morph()
    groups = collections.defaultdict(list)
    seen = set()
    for c in cands:
        s, a, w = c["loc"]
        segs = words.get((s, a, w))
        if not segs:
            continue
        stem = stem_of(segs, root)
        if not stem or (s, a, w) in seen:
            continue
        seen.add((s, a, w))
        groups[(stem["pos"], group_key(root, segs, stem))].append((c, segs, stem))
    nv = {k for k, v in words.items() if stem_of(v, root)}
    missing = sorted(nv - seen)
    out = {"root_bw": root, "root_display": root_display(root), "root_dir": "rtl", "dictionary_url": url_of(root),
           "nouns": [], "verbs": [],
           "dictionary_evidence": {"header": header, "lines_retrieved": len(cands),
                                   "candidates": [{"loc": c["loc"], "transliteration": c["transliteration"],
                                                   "gloss_en": c["gloss_en"], "line": c["line"]} for c in cands],
                                   "morphology_coverage": {"dictionary_candidates": len(cands), "nv_segments": len(nv),
                                                           "missing_dictionary": [list(x) for x in missing]}}}
    # izbor
    for (pos, gk), items in groups.items():
        alts = []
        for c, segs, stem in items:
            s, a, w = c["loc"]
            if (s, a) in MERGED:
                continue
            text, sp = uth_spans(s, a)
            st, en, word = sp[w]
            alts.append({"qac_location": stem["loc"], "qac_word_index": w, "features": stem["features"],
                         "lemma": stem["lemma"], "ayah_ref": f"{s}:{a}", "highlight_word": word,
                         "highlight_word_index": w, "highlight_span": {"start": st, "end": en},
                         "gloss_en": c["gloss_en"], "_bare": is_bare(segs, stem),
                         "_len": len(words_with_spans(text)), "_ord": (s, a, w)})
        if not alts:
            continue

        def score(x):
            return (not x["_bare"], x["_len"], x["_ord"])
        alts.sort(key=score)
        best = alts[0]
        s, a = best["_ord"][:2]
        text, meh = verse(s, a)
        card = {"root_bw": root, "pos": pos, "lemma": best["lemma"], "frequency": len(items),
                "qac_location": best["qac_location"], "features": best["features"], "form": best["highlight_word"],
                "meaning_en": best["gloss_en"], "ayah_ref": best["ayah_ref"], "arabic": text, "bosnian": meh,
                "highlight_word": best["highlight_word"], "highlight_word_index": best["highlight_word_index"],
                "highlight_span": best["highlight_span"],
                "alternatives": [{k: v for k, v in x.items() if not k.startswith("_")} for x in alts],
                "group_key": gk, "arabic_dir": "rtl", "bosnian_dir": "ltr", "reference_dir": "ltr",
                "source_ref": best["ayah_ref"], "is_excerpt": False,
                "lemma_links": sorted({x["lemma"] for x in alts}),
                "morphology_links": sorted({x["features"] for x in alts})}
        card["gloss_key"] = f"{gk}|{card['form']}"
        out["nouns" if pos == "N" else "verbs"].append(card)
    # vidljivi duplikati unutar sekcije: spoji u grupu veće učestalosti
    for sec in ("nouns", "verbs"):
        byform = {}
        for c in sorted(out[sec], key=lambda c: -c["frequency"]):
            if c["form"] in byform:
                k = byform[c["form"]]
                k["alternatives"] += c["alternatives"]
                k["frequency"] += c["frequency"]
                k["lemma_links"] = sorted(set(k["lemma_links"]) | set(c["lemma_links"]))
                k["morphology_links"] = sorted(set(k["morphology_links"]) | set(c["morphology_links"]))
                k.setdefault("merged_group_keys", []).append(c["group_key"])
            else:
                byform[c["form"]] = c
        # redoslijed: učestalost, zatim niža referenca
        out[sec] = sorted(byform.values(), key=lambda c: (-c["frequency"], tuple(c["qac_location"][:3])))
    return out


# ---------------------------------------------------------------- objavljeni korijeni
def published_roots():
    """root_bw → (sura, objekt korijena) iz već objavljenih panela; najčešća varijanta."""
    by = collections.defaultdict(list)
    for f in glob.glob(os.path.join(D, "SURA_*_ROOT_PANEL_SHORT.json")):
        n = int(re.search(r"SURA_(\d+)_", os.path.basename(f))[1])
        if n not in PUBLISHED:
            continue  # SHORT generisanih sura nije izvor (inače bi se zamjene konteksta jedne sure prenosile u druge)
        for r in json.load(open(f, encoding="utf-8"))["roots"]:
            sig = json.dumps([(c["group_key"], c["form"], c["ayah_ref"]) for c in r["nouns"] + r["verbs"]])
            by[r["root_bw"]].append((sig, n, r))
    out = {}
    for root, lst in by.items():
        common = collections.Counter(s for s, _, _ in lst).most_common(1)[0][0]
        out[root] = next((n, r) for s, n, r in lst if s == common)
    return out


def sura_roots(n):
    roots = []
    for (s, a, w), segs in sorted(morph().items()):
        if s == n:
            st = stem_of(segs)
            if st and st["root"] not in roots:
                roots.append(st["root"])
    return roots


def parse_suras(args):
    s = []
    for x in args:
        if "-" in x:
            p, q = x.split("-")
            s += list(range(int(p), int(q) + 1))
        else:
            s.append(int(x))
    return s


def load_gloss():
    return json.load(open(GLOSS_DB, encoding="utf-8")) if os.path.exists(GLOSS_DB) else {}


def todo(suras):
    pub = published_roots()
    gloss = load_gloss()
    items = {}
    roots = []
    for n in suras:
        for r in sura_roots(n):
            if r not in pub and r not in roots:
                roots.append(r)
    for r in roots:
        obj = build_root(r)
        for sec in ("nouns", "verbs"):
            for c in obj[sec]:
                k = c["gloss_key"]
                if k in gloss or k in items:
                    continue
                full = c["arabic"]
                st, en = c["highlight_span"]["start"], c["highlight_span"]["end"]
                items[k] = {"key": k, "root": r, "root_display": obj["root_display"], "pos": c["pos"],
                            "lemma": c["lemma"], "features": c["features"], "form": c["form"], "ref": c["ayah_ref"],
                            "gloss_en": c["meaning_en"],
                            "arabic_marked": full[:st] + "[[" + full[st:en] + "]]" + full[en:],
                            "bosnian": c["bosnian"]}
    out = os.path.join(D, "GLOSS_TODO.json")
    json.dump(list(items.values()), open(out, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"novih korijena {len(roots)}; kartica bez značenja {len(items)} → {out}")


def app(n):
    pub = published_roots()
    gloss = load_gloss()
    words = morph()
    uth = load_uthmani_surah(n)
    clickable = set()
    verses = []
    for a in sorted(uth):
        text, meh = verse(n, a)
        _, sp = uth_spans(n, a)
        ws = []
        for w in sorted(sp):
            segs = words.get((n, a, w), [])
            stem = stem_of(segs)
            st, en, word = sp[w]
            item = {"qac_location": [n, a, w], "word": word, "start": st, "end": en, "word_index": w,
                    "qac_word_index": w, "segments": segs, "clickable": bool(stem)}
            if stem:
                item["root_bw"] = stem["root"]
                item["stem_qac_location"] = stem["loc"]
                clickable.add((n, a, w))
            ws.append(item)
        verses.append({"sura": n, "ayah": a, "arabic": text, "bosnian": meh, "ref": f"{n}:{a}", "words": ws})
    roots, miss_gloss, swapped = [], [], 0
    for r in sura_roots(n):
        if r in pub:
            obj = json.loads(json.dumps(pub[r][1]))
            src = f"objavljeni panel sure {pub[r][0]}"
        else:
            obj = build_root(r)
            src = "Dictionary + morphology (gen_root_panel)"
        obj["source"] = src
        for sec in ("nouns", "verbs"):
            for c in obj[sec]:
                h = hashlib.sha1(f"{c['group_key']}|{c['form']}".encode("utf-8")).hexdigest()[:10]
                c["id"] = f"S{n}-{r}-{h}"
                if "gloss_key" in c:
                    if c["gloss_key"] not in gloss:
                        miss_gloss.append(c["gloss_key"])
                        continue
                    c["meaning_bs"] = gloss[c["gloss_key"]]
                # dupli aktuelni kontekst (odjeljak 6): isti oblik u istom ajetu/riječi ove sure → drugi kandidat
                loc = tuple(c["qac_location"][:3])
                # isto i za primjer iz ajeta gdje QAC spaja dvije Uthmani riječi (indeks se ne bi slagao)
                if loc in clickable or loc[:2] in MERGED:
                    for alt in sorted(c["alternatives"], key=lambda x: (len(words_with_spans(verse(*x["qac_location"][:2])[0])),
                                                                        tuple(x["qac_location"][:3]))):
                        s, a, w = alt["qac_location"][:3]
                        if (s, a, w) in clickable or (s, a) in MERGED:
                            continue
                        # raspon i indeks računaj iz izvora (alternative u objavljenim panelima nisu pouzdane)
                        _, sp = uth_spans(s, a)
                        stem = stem_of(words.get((s, a, w), []), r)
                        if w not in sp or sp[w][2] != c["form"] or not stem:
                            continue
                        text, meh = verse(s, a)
                        for k in ("arabic_full", "bosnian_full", "excerpt_arabic", "excerpt_bosnian",
                                  "highlight_display_span", "qa_status"):
                            c.pop(k, None)
                        c["is_excerpt"] = False
                        c["highlight_word"] = c["form"]
                        c.update({"qac_location": stem["loc"], "features": stem["features"], "lemma": stem["lemma"],
                                  "ayah_ref": f"{s}:{a}", "source_ref": f"{s}:{a}", "arabic": text, "bosnian": meh,
                                  "highlight_word_index": w, "highlight_span": {"start": sp[w][0], "end": sp[w][1]},
                                  "meaning_en": alt.get("gloss_en", c.get("meaning_en"))})
                        swapped += 1
                        break
        roots.append(obj)
    if miss_gloss:
        raise SystemExit(f"nedostaje kratko značenje za {len(miss_gloss)} kartica (prvo {miss_gloss[:3]})")
    first = next(w for v in verses for w in v["words"] if w["clickable"])
    d = {"schema_version": "ROOT_PANEL_V7", "protocol": "GLAVNI_NALOG_ROOT_PANEL_FINAL_V7",
         "surah": {"number": n, "ayah_count": len(uth)},
         "source_lock": [{"file": "quranic-corpus-morphology-0.4.txt"}, {"file": "quran-uthmani.txt (Tanzil)"},
                         {"file": "bosnian_mihanovich_v1.1.0"}, {"file": "QAC Dictionary (corpus.quran.com), keš sources/root_panel/dict"}],
         "text_rules": {"root_dir": "rtl", "arabic_dir": "rtl", "bosnian_dir": "ltr", "reference_dir": "ltr",
                        "storage_order": "logical Unicode; never reverse", "span_unit": "Unicode code points",
                        "span_interval": "[start,end)", "highlight_word_index": "QAC whole-word index"},
         "default_selection": {"surah": n, "ayah": first["qac_location"][1], "word_index": first["qac_word_index"],
                               "root_bw": first["root_bw"], "stem_qac_location": first["stem_qac_location"]},
         "roots": roots, "surah_verses": verses}
    out = os.path.join(D, f"SURA_{n}_ROOT_PANEL_APP.json")
    json.dump(d, open(out, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    nc = sum(len(r["nouns"]) + len(r["verbs"]) for r in roots)
    print(f"{out}: {len(roots)} korijena ({sum(1 for r in roots if r['source'].startswith('obj'))} iz objavljenih), "
          f"{nc} kartica, klikova {len(clickable)}, zamijenjen dupli kontekst {swapped}")


if __name__ == "__main__":
    cmd = sys.argv[1]
    if cmd == "todo":
        todo(parse_suras(sys.argv[2:]))
    elif cmd == "app":
        app(int(sys.argv[2]))
