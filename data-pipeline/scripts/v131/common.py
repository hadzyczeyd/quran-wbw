# -*- coding: utf-8 -*-
"""QAC DIRECT V13.1 — zajednički deterministički sloj (izvori, color master, tokenizer, hash, atomski zapis)."""
import hashlib
import json
import os
import re
import sys
import unicodedata
from datetime import datetime, timezone

sys.stdout.reconfigure(encoding="utf-8")

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
SOURCES = os.path.join(ROOT, "sources")
RUNS = os.path.join(ROOT, "runs")

QAC_MORPH = os.path.join(SOURCES, "quranic-corpus-morphology-0.4.txt")
UTHMANI = os.path.join(SOURCES, "quran-uthmani.txt")
MEHANOVIC_XLSX = os.path.join(SOURCES, "bosnian_mihanovich_v1.1.0-excel.1.xlsx")
COLOR_DIR = os.path.join(SOURCES, "qac_color_source")
API_MORPH = os.path.join(COLOR_DIR, "api", "morphology-api.txt")
WBW = os.path.join(COLOR_DIR, "api", "word-by-word.txt")

QAC_COMMIT = "ee7218ad8e68fe50486c0541e434d91a5998e5f7"
API_COMMIT = "17a9062416eccc332111ef3e84f74072d709e187"
PINNED_BLOBS = {
    "color-service.ts": "da03f0eaa6e054ef287cd6fdb9c119ef56327a16",
    "styles.scss": "b232f90fb36a3e348298706115e9b58a3ef0b18e",
    "pronoun-type.ts": "37c8751419181b3d5541b2144dbd099d2b32f9d3",
    "PartOfSpeech.java": "494e0bc2fd1fc9eeecc90f49c419a6f166f789ce",
}
PROTOCOL_DOC = "QAC_DIRECT_V13.1_LARGE_SURAH_UTHMANI_SEMANTIC_MAPPING_GUARDS_47_3_03-10-2026.docx"

PROFILES = {
    "bosnian_tokenizer_profile": "WHITESPACE_PRESERVE_PUNCT_V1",
    "alignment_profile": "QAC_SEGMENT_CONTEXTUAL_V2",
    "output_schema_profile": "V13_1_CANONICAL_SCHEMA",
    "source_profile": "V13_SOURCE_MASTER_LOCK",
    "semantic_mapping_profile": "SEMANTIC_FIRST_ROLE_ROOT_V1",
}

INSERTED = "inserted_no_arabic_segment"
UNEXPRESSED = "QAC_SEGMENT_NOT_SEPARATELY_EXPRESSED_IN_BOSNIAN"


def now():
    return datetime.now(timezone.utc).isoformat()


def sha256_bytes(b):
    return hashlib.sha256(b).hexdigest()


def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def git_blob_sha(path):
    data = open(path, "rb").read()
    return hashlib.sha1(b"blob %d\0" % len(data) + data).hexdigest()


def canonical_json(obj):
    return json.dumps(obj, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def atomic_write_json(path, obj):
    """candidate → close → reopen → strukturna provjera → SHA-256 (V13 4.6)."""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    tmp = path + ".candidate"
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(obj, f, ensure_ascii=False, indent=1, sort_keys=True)
    with open(tmp, encoding="utf-8") as f:
        reopened = json.load(f)
    if canonical_json(reopened) != canonical_json(obj):
        raise RuntimeError(f"reopen mismatch: {path}")
    os.replace(tmp, path)
    return sha256_file(path)


def load_json(path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)


# ---------------------------------------------------------------- Buckwalter

BUCKWALTER = {
    "'": "ء", "|": "آ", ">": "أ", "&": "ؤ", "<": "إ", "}": "ئ",
    "A": "ا", "b": "ب", "p": "ة", "t": "ت", "v": "ث", "j": "ج",
    "H": "ح", "x": "خ", "d": "د", "*": "ذ", "r": "ر", "z": "ز",
    "s": "س", "$": "ش", "S": "ص", "D": "ض", "T": "ط", "Z": "ظ",
    "E": "ع", "g": "غ", "_": "ـ", "f": "ف", "q": "ق", "k": "ك",
    "l": "ل", "m": "م", "n": "ن", "h": "ه", "w": "و", "Y": "ى",
    "y": "ي", "F": "ً", "N": "ٌ", "K": "ٍ", "a": "َ", "u": "ُ",
    "i": "ِ", "~": "ّ", "o": "ْ", "^": "ٓ", "#": "ٔ", "`": "ٰ",
    "{": "ٱ", ":": "ۜ", "@": "۟", '"': "۠", "[": "ۢ", ";": "ۣ",
    ",": "ۥ", ".": "ۦ", "!": "ۨ", "-": "۪", "+": "۫", "%": "۬",
    "]": "ۭ",
}


def bw_to_arabic(text):
    """Tanzil/QAC Buckwalter (extended) → Unicode; koristi se samo za QAC segmentni surface-form."""
    return "".join(BUCKWALTER.get(ch, ch) for ch in text)


# ---------------------------------------------------------------- QAC morphology

def load_qac_surah(surah):
    """QAC 0.4 zapisi jedne sure, raw linije + parsirani segmenti."""
    raw, segs = [], []
    prefix = f"({surah}:"
    with open(QAC_MORPH, encoding="utf-8") as f:
        for line in f:
            if not line.startswith(prefix):
                continue
            line = line.rstrip("\n")
            raw.append(line)
            loc, form, tag, feats = line.split("\t")
            s, a, w, g = map(int, loc.strip("()").split(":"))
            parts = feats.split("|")
            seg_type = parts[0]
            lemma = next((p[4:] for p in parts if p.startswith("LEM:")), None)
            root = next((p[5:] for p in parts if p.startswith("ROOT:")), None)
            segs.append({
                "surah": s, "ayah": a, "word": w, "segment": g,
                "qac_location": f"{s}:{a}:{w}:{g}",
                "form_bw": form, "form_ar": bw_to_arabic(form),
                "tag": tag, "features": feats, "segment_type": seg_type,
                "lemma_bw": lemma, "root_bw": root,
                "raw_line": line,
            })
    return raw, segs


def api_lines_by_word():
    """QAC API morphology.txt (pinned commit): jedan red po QAC riječi u kanonskom redoslijedu 0.4."""
    words = []
    seen = set()
    with open(QAC_MORPH, encoding="utf-8") as f:
        for line in f:
            if line.startswith("("):
                s, a, w, _ = map(int, line.split("\t")[0].strip("()").split(":"))
                if (s, a, w) not in seen:
                    seen.add((s, a, w))
                    words.append((s, a, w))
    api = open(API_MORPH, encoding="utf-8").read().split("\n")
    if api and api[-1] == "":
        api = api[:-1]
    wbw = open(WBW, encoding="utf-8").read().split("\n")
    if wbw and wbw[-1] == "":
        wbw = wbw[:-1]
    if not (len(words) == len(api) == len(wbw)):
        raise RuntimeError(f"API/WBW poravnanje: {len(words)} {len(api)} {len(wbw)}")
    return {k: (api[i], wbw[i]) for i, k in enumerate(words)}


def assign_pronoun_types(segs, api_map):
    """
    QAC ColorService čita segment.pronounType. U pinned QAC API (TsvReader/Segmenter)
    subjektni sufiks nema vlastitu morfologiju (izveden iz konjugacije glagola), dok su
    eksplicitni PRON sufiksi objekti: prvi = obj, drugi = obj2. U 0.4 datasetu svi
    sufiksi imaju PRON zapis, pa se broj eksplicitnih (objektnih) sufiksa čita iz API
    reda iste riječi; preostali (raniji) PRON sufiksi riječi su subjektni.
    """
    by_word = {}
    for s in segs:
        by_word.setdefault((s["surah"], s["ayah"], s["word"]), []).append(s)
    problems = []
    for key, ws in by_word.items():
        api_line, _ = api_map[key]
        tokens = api_line.split(" ")
        stem_is_pron = "POS:PRON" in tokens
        explicit = sum(1 for t in tokens if t.startswith("PRON:"))
        suffix_prons = [s for s in ws if s["tag"] == "PRON" and s["segment_type"] == "SUFFIX"]
        if explicit > len(suffix_prons):
            problems.append(f"{key}: API eksplicitnih PRON {explicit} > 0.4 sufiksa {len(suffix_prons)}")
        n_subj = len(suffix_prons) - explicit
        for i, s in enumerate(suffix_prons):
            if i < n_subj:
                s["pronoun_type"] = "subj"
            else:
                s["pronoun_type"] = "obj" if i == n_subj else "obj2"
        for s in ws:
            if s["tag"] == "PRON" and s["segment_type"] != "SUFFIX":
                # Samostalna zamjenica (STEM): ColorService default grana → nema pronounType.
                s["pronoun_type"] = None
            s.setdefault("pronoun_type", None)
            s["api_line"] = api_line
        _ = stem_is_pron
    return problems


# ---------------------------------------------------------------- QAC COLOR MASTER

def build_color_master():
    """Izvodi QAC_COLOR_MASTER iz pinned color-service.ts + styles.scss + PartOfSpeech.java."""
    files = {}
    for name, blob in PINNED_BLOBS.items():
        path = os.path.join(COLOR_DIR, name)
        actual = git_blob_sha(path)
        files[name] = {"path": path, "expected_blob": blob, "actual_blob": actual, "match": actual == blob}
    cs = open(os.path.join(COLOR_DIR, "color-service.ts"), encoding="utf-8").read()
    block = cs.split("posTagColors")[1].split("]);")[0]
    pos_map = dict(re.findall(r"\['([A-Z]+)',\s*'([a-z]+)'\]", block))
    scss = open(os.path.join(COLOR_DIR, "styles.scss"), encoding="utf-8").read()
    hex_by_class = {c: h.upper() for c, h in re.findall(r"\.([a-z]+)\s*\{\s*color:\s*(#[0-9a-fA-F]{6})", scss)}
    pos_java = open(os.path.join(COLOR_DIR, "PartOfSpeech.java"), encoding="utf-8").read()
    repertoire = re.findall(r'\w+\("([A-Z]+)"\)', pos_java)

    rows = []
    def add(tag, variant, rule, css):
        hexv = hex_by_class[css]
        r, g, b = (int(hexv[i:i + 2], 16) for i in (1, 3, 5))
        rows.append({
            "row_id": f"QCM-{len(rows) + 1:03d}", "qac_tag": tag, "variant": variant,
            "color_rule": rule, "css_class": css, "rgb": f"{r},{g},{b}", "hex": hexv,
            "excel_argb": "FF" + hexv[1:],
            "source_ref": f"kaisdukes/quranic-corpus@{QAC_COMMIT}:src/theme/color-service.ts + styles.scss",
        })
    for tag in repertoire:
        if tag in pos_map:
            add(tag, None, "explicit posTagColors map", pos_map[tag])
        elif tag == "PRON":
            add("PRON", "subj", "PRON special: pronounType=subj", "sky")
            add("PRON", "obj2", "PRON special: pronounType=obj2", "orange")
            add("PRON", "obj", "PRON special: otherwise (obj/default)", "metal")
        else:
            add(tag, None, "ColorService source fallback", "pink")
    master = {
        "qac_commit": QAC_COMMIT, "api_commit": API_COMMIT, "files": files,
        "palette": hex_by_class, "repertoire": repertoire, "rows": rows,
    }
    master["master_hash"] = sha256_bytes(canonical_json(rows).encode("utf-8"))
    return master


def color_for(seg, master):
    tag = seg["tag"]
    for r in master["rows"]:
        if r["qac_tag"] != tag:
            continue
        if tag == "PRON":
            want = seg.get("pronoun_type")
            want = want if want in ("subj", "obj2") else "obj"
            if r["variant"] != want:
                continue
        return r
    return None


# ---------------------------------------------------------------- Uthmani

def load_uthmani_surah(surah):
    out = {}
    raw = {}
    basmala = None
    with open(UTHMANI, encoding="utf-8") as f:
        for line in f:
            line = line.rstrip("\n")
            if not line or line.startswith("#"):
                continue
            s, a, t = line.split("|", 2)
            if (int(s), int(a)) == (1, 1):
                basmala = t + " "
            if int(s) == surah:
                raw[int(a)] = t
    for a, t in raw.items():
        rule = None
        text = t
        # Prefiks se uzima iz istog izvora (1:1), ne iz memorije.
        if a == 1 and surah not in (1, 9) and basmala and t.startswith(basmala):
            BASMALA_PREFIX = basmala
            # Tanzil export uključuje basmalu kao prefiks 1. ajeta; ona nije dio ajeta u Mushafu.
            text = t[len(BASMALA_PREFIX):]
            rule = "TANZIL_BASMALA_PREFIX_EXCLUDED"
        out[a] = {"raw_line_text": t, "ayah_text": text, "rule": rule}
    return out


def is_word_token(tok):
    return any(unicodedata.category(c).startswith("L") for c in tok)


# ---------------------------------------------------------------- Mehanović + tokenizer

def load_mehanovic_surah(surah):
    import openpyxl
    wb = openpyxl.load_workbook(MEHANOVIC_XLSX, read_only=True)
    ws = wb.worksheets[0]
    out = {}
    header_seen = False
    for r in ws.iter_rows(values_only=True):
        if not header_seen:
            if r and r[0] == "id":
                header_seen = True
            continue
        if r[1] == surah:
            out[int(r[2])] = {"id": r[0], "text": r[3], "footnotes": r[4]}
    wb.close()
    return out


def tokenize(text):
    """WHITESPACE_PRESERVE_PUNCT_V1: maksimalni ne-whitespace nizovi; gap_before = tačan izvorni whitespace."""
    toks = []
    for m in re.finditer(r"\S+", text):
        start = m.start()
        prev_end = toks[-1]["span_end"] if toks else 0
        toks.append({"text": m.group(0), "gap_before": text[prev_end:start],
                     "span_start": start, "span_end": m.end(),
                     "is_lexical": any(unicodedata.category(c).startswith(("L", "N")) for c in m.group(0))})
    return toks


def reconstruct(toks, text):
    rebuilt = "".join(t["gap_before"] + t["text"] for t in toks)
    trailing = text[len(rebuilt):]
    return rebuilt + trailing == text and not trailing.strip()


def word_id(s, a, w):
    return f"S{s:03d}-A{a:03d}-W{w:03d}"


def seg_id(s, a, w, g):
    return f"S{s:03d}-A{a:03d}-W{w:03d}-S{g:02d}"


def tok_id(s, a, t):
    return f"S{s:03d}-A{a:03d}-B{t:03d}"
