# -*- coding: utf-8 -*-
"""
Čitanje QAC DIRECT V13.1 "REVIDIRANA" APP_READY fajlova (oktobar 2026).

Ovi fajlovi dolaze u više varijanti zaglavlja (različita imena kolona,
neki imaju naslovne redove iznad zaglavlja), pa se kolone traže po
listi sinonima. Iz njih se gradi isti oblik redova koji baza već koristi:
- CSS klase "sky" -> "segSky" (frontend selektori ostaju isti),
- korijen/lema iz QAC morfologije (quranic-corpus-morphology-0.4.txt)
  prevedeni iz Buckwaltera u arapsko pismo, kao u ranijim podacima,
- boja bosanskog tokena izvodi se iz povezanih segmenata: jedna boja ->
  ta boja; više različitih -> MAPPED_FUSED_MULTI_SEGMENT (neutralno, bez
  dominantne boje, V13.1 pravilo 8.4); bez veza -> inserted_no_arabic_segment,
- tokeni bez razmaka među sobom (npr. riječ + interpunkcija) spajaju se u
  jedan prikazni token prema razmacima u Mehanovićevom originalu.
"""
import unicodedata

KNOWN_CLASSES = {
    "segSeagreen", "segSky", "segBlue", "segPurple", "segGray", "segMetal", "segRust", "segNavy",
    "segRed", "segRose", "segOrange", "segGold", "segBrown", "segGreen", "segPink",
}
FUSED_CLASS = "fused"
FUSED_STATUS = "MAPPED_FUSED_MULTI_SEGMENT"
INSERTED = "inserted_no_arabic_segment"

BUCKWALTER = {
    "'": "ء", "|": "آ", ">": "أ", "&": "ؤ", "<": "إ", "}": "ئ", "A": "ا", "b": "ب", "p": "ة",
    "t": "ت", "v": "ث", "j": "ج", "H": "ح", "x": "خ", "d": "د", "*": "ذ", "r": "ر", "z": "ز",
    "s": "س", "$": "ش", "S": "ص", "D": "ض", "T": "ط", "Z": "ظ", "E": "ع", "g": "غ", "_": "ـ",
    "f": "ف", "q": "ق", "k": "ك", "l": "ل", "m": "م", "n": "ن", "h": "ه", "w": "و", "Y": "ى",
    "y": "ي", "F": "ً", "N": "ٌ", "K": "ٍ", "a": "َ", "u": "ُ", "i": "ِ", "~": "ّ", "o": "ْ",
    "`": "ٰ", "{": "ٱ", "^": "ٓ", "#": "ٔ", ":": "ۜ", "@": "۟", '"': "۠", "[": "ۢ", ";": "ۭ",
    ",": "ۥ", ".": "ۦ", "!": "ۨ", "-": "۪", "+": "۫", "%": "۬", "]": "ۭ",
}


def bw_to_arabic(text):
    return "".join(BUCKWALTER.get(ch, ch) for ch in text)


def load_morphology(path):
    """(sura, ajet, riječ, segment) lokacija -> {'root': 'ا ل ه', 'lemma': 'ٱللَّه'}"""
    out = {}
    with open(path, encoding="utf-8") as f:
        for line in f:
            if not line.startswith("("):
                continue
            loc, _form, _tag, feats = line.rstrip("\n").split("\t")
            root = lemma = None
            for part in feats.split("|"):
                if part.startswith("ROOT:"):
                    root = " ".join(bw_to_arabic(part[5:]))
                elif part.startswith("LEM:"):
                    lemma = bw_to_arabic(part[4:])
            out[loc.strip("()")] = {"root": root, "lemma": lemma}
    return out


def read_rows(wb, name):
    ws = wb[name]
    rows = list(ws.iter_rows(values_only=True))
    for i, r in enumerate(rows[:8]):
        if r and ("ayah_id" in r or "ayah" in r):
            header = r
            return [dict(zip(header, row)) for row in rows[i + 1:] if any(v is not None for v in row)]
    raise ValueError(f"List {name}: zaglavlje nije pronađeno")


def pick(row, *names):
    for n in names:
        if n in row and row[n] not in (None, ""):
            return row[n]
    return None


def is_revidirana(wb):
    ws = wb["Rijeci"]
    for r in ws.iter_rows(min_row=1, max_row=6, values_only=True):
        if r and "word_order" in r:
            return True
    return False


def normalize_class(c):
    if not c:
        return None
    c = str(c).strip()
    if c.startswith("seg"):
        return c
    return "seg" + c[:1].upper() + c[1:]


def _spacing(tokens, source):
    """Za svaki token: da li ispred njega u originalu stoji razmak. None ako rekonstrukcija ne uspije."""
    pos = 0
    gaps = []
    for t in tokens:
        j = pos
        while j < len(source) and source[j].isspace():
            j += 1
        if source[j:j + len(t)] != t:
            return None
        gaps.append(j > pos)
        pos = j + len(t)
    if source[pos:].strip():
        return None
    return gaps


def _base_len(text):
    return sum(1 for ch in text if not unicodedata.category(ch).startswith("M"))


def _split_by_letters(word_text, parts):
    """Dijeli tekst riječi na dijelove s istim brojem osnovnih slova kao `parts` (dijakritika ide uz slovo)."""
    out, pos = [], 0
    for part in parts:
        need, start = _base_len(part), pos
        while pos < len(word_text) and need:
            pos += 1
            while pos < len(word_text) and unicodedata.category(word_text[pos]).startswith("M"):
                pos += 1
            need -= 1
        out.append(word_text[start:pos])
    return out if pos == len(word_text) and all(out) else None


def apply_arabic(data, arabic):
    """
    Zamjenjuje arapski tekst riječi/segmenata provjerenim osmanskim tekstom
    (REVIDIRANA fajlovi imaju nepotpunu Buckwalter konverziju: obični sukun,
    bez pauzalnih znakova, ponegdje ostaci ASCII znakova). ID-ovi riječi su
    stabilni; ako se segmentacija promijenila, dosadašnji tekst segmenata
    te riječi dijeli se po broju osnovnih slova novih segmenata.
    """
    problems = []
    segs_by_word = {}
    for s in data["segments"]:
        segs_by_word.setdefault(s["word_id"], []).append(s)
    for w in data["words"]:
        text = arabic["words"].get(w["word_id"])
        if not text:
            problems.append(f"riječ {w['word_id']}: nema provjerenog arapskog teksta")
            continue
        w["text"] = text
        segs = sorted(segs_by_word.get(w["word_id"], []), key=lambda s: s["segment_order"])
        old = arabic["segments"].get(w["word_id"], {})
        if segs and all(s["segment_id"] in old for s in segs) and len(old) == len(segs):
            for s in segs:
                s["segment_text"] = old[s["segment_id"]]
            continue
        old_joined = "".join(old[k] for k in sorted(old))
        split = _split_by_letters(old_joined, [s["segment_text"] for s in segs])
        if split is None:
            problems.append(f"riječ {w['word_id']}: segmenti se ne mogu poravnati s tekstom {old_joined!r}")
            continue
        for s, part in zip(segs, split):
            s["segment_text"] = part
    return problems


def parse(wb, morph, arabic=None):
    """Vraća (data, problemi). data ima ključeve kao import_file očekuje."""
    problems = []
    rijeci = read_rows(wb, "Rijeci")
    segs_raw = read_rows(wb, "Segmenti")
    toks_raw = read_rows(wb, "Bosanski_tokeni")
    veze_raw = read_rows(wb, "Veze")
    prijevod_raw = read_rows(wb, "Prijevod_Mehanovic")

    surah_id = int(rijeci[0]["surah_id"])
    words = []
    for r in rijeci:
        words.append({
            "word_id": r["qac_word_id"],
            "ayah": int(r["ayah_id"]),
            "position": int(r["word_order"]),
            "text": r["arabic_word"],
            "transliteration": pick(r, "qac_transliteration", "transliteration"),
            "gloss": pick(r, "qac_word_gloss", "qac_gloss"),
        })
    word_ids = {w["word_id"] for w in words}

    segments = []
    for s in segs_raw:
        text = s.get("arabic_segment")
        if not text or text == "Ø":
            continue
        loc = (
            f"{surah_id}:{int(pick(s, 'ayah_id', 'ayah'))}:"
            f"{int(s['word_order'])}:{int(s['segment_order'])}"
        )
        m = morph.get(loc)
        if m is None:
            problems.append(f"segment {s['qac_segment_id']}: lokacija {loc!r} nije u QAC morfologiji")
            m = {"root": None, "lemma": None}
        css = normalize_class(s.get("qac_css_class"))
        if css not in KNOWN_CLASSES:
            problems.append(f"segment {s['qac_segment_id']}: nepoznata klasa {s.get('qac_css_class')!r}")
        if s["qac_word_id"] not in word_ids:
            problems.append(f"segment {s['qac_segment_id']}: nepostojeća riječ")
        segments.append({
            "segment_id": s["qac_segment_id"],
            "word_id": s["qac_word_id"],
            "segment_order": int(s["segment_order"]),
            "segment_text": text,
            "qac_tag": pick(s, "qac_tag", "tag"),
            "qac_full_description": pick(s, "qac_full_description", "features"),
            "qac_css_class": css,
            "qac_hex_color": s.get("qac_hex_color"),
            "lemma": m["lemma"],
            "root": m["root"],
        })
    seg_by_id = {s["segment_id"]: s for s in segments}

    tokens = sorted(
        (
            {
                "token_id": t["bosnian_token_id"],
                "ayah": int(t["ayah_id"]),
                "order": int(t["bosnian_token_order"]),
                "text": str(t["bosnian_original_token"]),
                "file_status": t.get("mapping_status"),
            }
            for t in toks_raw
        ),
        key=lambda t: (t["ayah"], t["order"]),
    )
    token_ids = {t["token_id"] for t in tokens}

    links = set()
    for v in veze_raw:
        sid, tid = v.get("qac_segment_id"), v.get("bosnian_token_id")
        if sid not in seg_by_id:
            continue
        if tid not in token_ids:
            problems.append(f"veza {sid} -> nepostojeći token {tid}")
            continue
        links.add((sid, tid))
    segs_of_token = {}
    for sid, tid in links:
        segs_of_token.setdefault(tid, []).append(sid)
    linked_segs = {sid for sid, _ in links}

    for s in segments:
        s["expression_status"] = (
            "EXPRESSED_IN_BOSNIAN" if s["segment_id"] in linked_segs
            else "QAC_SEGMENT_NOT_SEPARATELY_EXPRESSED_IN_BOSNIAN"
        )

    prijevod = {int(p["ayah_id"]): pick(p, "source_exact", "mehanovic_original") for p in prijevod_raw}

    # Boja tokena iz veza + spajanje interpunkcije po razmacima originala.
    out_tokens = []
    merged_into = {}
    fused_disagree = 0
    by_ayah = {}
    for t in tokens:
        by_ayah.setdefault(t["ayah"], []).append(t)
    for ayah, ts in by_ayah.items():
        source = prijevod.get(ayah) or ""
        gaps = _spacing([t["text"] for t in ts], source)
        if gaps is None:
            problems.append(f"ajet {ayah}: tokeni ne rekonstruišu Mehanovićev tekst")
            gaps = [True] * len(ts)
        # Prikazni token = niz izvornih tokena bez razmaka među njima
        # ("Reci" + ":" -> "Reci:", "Kur" + "'" + "an" -> "Kur'an"), kao u
        # ranijim podacima. Veze svih spojenih tokena prelaze na jedan ID.
        groups = []
        for i, t in enumerate(ts):
            if i > 0 and not gaps[i] and groups:
                groups[-1].append(t)
            else:
                groups.append([t])

        rows = []
        for group in groups:
            sids = sorted({s for t in group for s in segs_of_token.get(t["token_id"], [])})
            linked = [t for t in group if segs_of_token.get(t["token_id"])]
            keep = (linked or group)[0]
            for t in group:
                if t is not keep:
                    merged_into[t["token_id"]] = keep["token_id"]
            classes = {seg_by_id[s]["qac_css_class"] for s in sids}
            file_status = linked[0]["file_status"] if len(linked) == 1 else "MAPPED_ONE_TO_MANY"
            if not sids:
                css, hex_, status = INSERTED, "#000000", INSERTED
            elif len(classes) == 1:
                seg0 = seg_by_id[sids[0]]
                css, hex_ = seg0["qac_css_class"], seg0["qac_hex_color"]
                status = file_status if file_status != FUSED_STATUS else "MAPPED_ONE_TO_MANY"
            else:
                css, hex_, status = FUSED_CLASS, "#000000", FUSED_STATUS
            if (status == FUSED_STATUS) != (file_status == FUSED_STATUS):
                fused_disagree += 1
            rows.append({
                "token_id": keep["token_id"],
                "surah_id": surah_id,
                "ayah_number": ayah,
                "display_text": "".join(t["text"] for t in group),
                "qac_css_class": css,
                "qac_hex_color": hex_,
                "mapping_status": status,
            })
        for pos, r in enumerate(rows, start=1):
            r["position"] = pos
        shown = " ".join(r["display_text"] for r in rows)
        if shown != " ".join(source.split()):
            problems.append(f"ajet {ayah}: prikaz se razlikuje od originala: {shown!r}")
        out_tokens.extend(rows)

    links = {(sid, merged_into.get(tid, tid)) for sid, tid in links}
    kept_ids = {t["token_id"] for t in out_tokens}
    dangling = [tid for _, tid in links if tid not in kept_ids]
    if dangling:
        problems.append(f"{len(dangling)} veza pokazuje na nepostojeći prikazni token")

    ayahs = sorted({w["ayah"] for w in words})
    missing_tr = [a for a in ayahs if not prijevod.get(a)]
    if missing_tr:
        problems.append(f"ajeti bez prijevoda: {missing_tr[:5]}")

    data = {
        "surah_id": surah_id,
        "words": words,
        "segments": segments,
        "tokens": out_tokens,
        "links": sorted(links),
        "prijevod": prijevod,
        "stats": {"fused": sum(t["mapping_status"] == FUSED_STATUS for t in out_tokens),
                  "fused_status_disagree": fused_disagree},
    }
    if arabic is not None:
        problems += apply_arabic(data, arabic)
    return data, problems


def load_arabic_backup(folder):
    """Provjereni osmanski tekst iz JSON backupa baze (words.json + word_segments.json)."""
    import json
    import os

    with open(os.path.join(folder, "words.json"), encoding="utf-8") as f:
        words = {w["word_id"]: w["text_uthmani"] for w in json.load(f)}
    segments = {}
    with open(os.path.join(folder, "word_segments.json"), encoding="utf-8") as f:
        for s in json.load(f):
            segments.setdefault(s["word_id"], {})[s["segment_id"]] = s["segment_text"]
    return {"words": words, "segments": segments}
