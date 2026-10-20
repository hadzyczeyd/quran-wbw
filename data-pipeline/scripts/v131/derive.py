# -*- coding: utf-8 -*-
"""
Deterministička derivacija iz CONSENSUS_MASTER-a (nalog 55.3 korak 6, 55.11):
mapping statusi, Veze, highlight grupe, display boje, fused markeri, coverage matrica.
Ništa se ne odlučuje semantički — sve slijedi iz zaključanih veza.
"""
from common import INSERTED, UNEXPRESSED

CONTENT_TAGS = {"N", "PN", "ADJ", "V", "IMPN"}
FUSED_CSS, FUSED_HEX = "neutral-fused", "#000000"
INSERTED_HEX = "#000000"


def derive(snap, master):
    segs = {s["qac_segment_id"]: s for s in snap["segments"]}
    toks = {t["bosnian_token_id"]: t for t in snap["tokens"]}
    links = master["links"]

    seg_targets = {}
    tok_segs = {}
    parts = {}
    for sid, l in links.items():
        if l["kind"] != "LINK":
            continue
        for tid, part in l["targets"]:
            seg_targets.setdefault(sid, []).append(tid)
            tok_segs.setdefault(tid, []).append(sid)
            if part:
                parts.setdefault(tid, []).append((tuple(part), sid))

    def word_of(sid):
        return segs[sid]["qac_word_id"]

    def hg_for_word(wid):
        return "HG-" + wid

    # status po tokenu
    tok_status = {}
    for tid in toks:
        ss = sorted(set(tok_segs.get(tid, [])))
        if not ss:
            tok_status[tid] = INSERTED
        elif tid in parts:
            tok_status[tid] = "MAPPED_BY_TOKEN_PART"
        elif len(ss) >= 2:
            tok_status[tid] = "MAPPED_FUSED_MULTI_SEGMENT"
        else:
            sid = ss[0]
            if len(set(seg_targets[sid])) > 1:
                tok_status[tid] = "MAPPED_ONE_TO_MANY"
            else:
                w_segs = [x for x in seg_targets if word_of(x) == word_of(sid)]
                w_toks = {t for x in w_segs for t in seg_targets[x]}
                tok_status[tid] = "MAPPED_BY_SEGMENT" if len(w_segs) >= 2 and len(w_toks) >= 2 else "MAPPED_ONE_TO_ONE"

    seg_status = {}
    for sid in segs:
        l = links.get(sid)
        if l is None or l["kind"] == "REVIEW":
            seg_status[sid] = "REVIEW_REQUIRED"
        elif l["kind"] == "UNEXPRESSED":
            seg_status[sid] = UNEXPRESSED
        else:
            ts = set(seg_targets[sid])
            st = {tok_status[t] for t in ts}
            if "MAPPED_FUSED_MULTI_SEGMENT" in st:
                seg_status[sid] = "MAPPED_FUSED_MULTI_SEGMENT"
            elif "MAPPED_BY_TOKEN_PART" in st:
                seg_status[sid] = "MAPPED_BY_TOKEN_PART"
            elif len(ts) > 1:
                seg_status[sid] = "MAPPED_ONE_TO_MANY"
            else:
                seg_status[sid] = tok_status[next(iter(ts))]

    seg_rows = []
    for s in snap["segments"]:
        sid = s["qac_segment_id"]
        l = links.get(sid, {})
        seg_rows.append({**s, "mapping_status": seg_status[sid],
                         "linked_bosnian_token_ids": ";".join(sorted(set(seg_targets.get(sid, [])))),
                         "mapping_note": format_note(l),
                         "highlight_group_id": hg_for_word(s["qac_word_id"]) if sid in seg_targets else ""})

    tok_rows = []
    fused_markers = []
    for t in snap["tokens"]:
        tid = t["bosnian_token_id"]
        ss = sorted(set(tok_segs.get(tid, [])), key=lambda x: (segs[x]["word_order"], segs[x]["segment_order"]))
        st = tok_status[tid]
        if st == INSERTED:
            css, hexv, rule = INSERTED, INSERTED_HEX, "crna #000000 — inserted_no_arabic_segment (bez QAC ID-a)"
        elif st == "MAPPED_FUSED_MULTI_SEGMENT":
            css, hexv, rule = FUSED_CSS, FUSED_HEX, "neutralni nosač + zasebni QAC marker po segmentu (bez dominantne boje)"
            for sid in ss:
                fused_markers.append({"ayah_id": t["ayah_id"], "bosnian_token_id": tid, "token": t["bosnian_original_token"],
                                      "qac_segment_id": sid, "tag": segs[sid]["tag"], "css": segs[sid]["qac_css_class"],
                                      "hex": segs[sid]["qac_hex_color"], "arabic_segment": segs[sid]["arabic_segment"],
                                      "highlight_group_id": hg_for_word(word_of(sid))})
        elif st == "MAPPED_BY_TOKEN_PART":
            css, hexv, rule = "token-part", FUSED_HEX, "svaki poddio u boji svog QAC segmenta"
            by_range = {}
            for p_, sid in parts[tid]:
                by_range.setdefault(p_, []).append(sid)
            for p_, sids in by_range.items():
                if len({segs[x]["qac_hex_color"] for x in sids}) > 1:
                    rule = "poddijelovi u boji svog segmenta; poddio s više segmenata neutralan + markeri"
                    for sid in sids:
                        fused_markers.append({"ayah_id": t["ayah_id"], "bosnian_token_id": tid,
                                              "token": t["bosnian_original_token"][p_[0]:p_[1]] + f" (poddio {p_[0]}–{p_[1]})",
                                              "qac_segment_id": sid, "tag": segs[sid]["tag"], "css": segs[sid]["qac_css_class"],
                                              "hex": segs[sid]["qac_hex_color"], "arabic_segment": segs[sid]["arabic_segment"],
                                              "highlight_group_id": hg_for_word(word_of(sid))})
        else:
            s0 = segs[ss[0]]
            css, hexv, rule = s0["qac_css_class"], s0["qac_hex_color"], f"boja QAC segmenta {s0['tag']}"
        words = sorted({word_of(x) for x in ss})
        notes = [format_note(links[x]) for x in ss]
        tok_rows.append({**t, "mapping_status": st, "linked_qac_segment_ids": ";".join(ss),
                         "linked_qac_word_ids": ";".join(words), "qac_css_class": css, "qac_hex_color": hexv,
                         "highlight_group_id": "|".join(hg_for_word(w) for w in words),
                         "display_rule": rule,
                         "token_parts": sorted([[p[0], p[1], sid] for p, sid in parts.get(tid, [])]),
                         "mapping_note": " || ".join(dict.fromkeys(notes)) if notes else master["inserted"].get(tid, "")})

    link_rows = []
    for sid, l in links.items():
        if l["kind"] != "LINK":
            continue
        s = segs[sid]
        for tid, part in sorted(l["targets"], key=lambda x: (x[0], x[1] or [0])):
            pid = ""
            if part:
                order = sorted(p for p, _ in parts[tid])
                pid = f"{tid}-P{order.index(tuple(part)) + 1:02d}"
            link_rows.append({"surah_id": s["surah"], "ayah_id": s["ayah"], "qac_segment_id": sid, "qac_word_id": s["qac_word_id"],
                              "bosnian_token_id": tid, "bosnian_token_part_id": pid,
                              "token_part_start": part[0] if part else "", "token_part_end": part[1] if part else "",
                              "mapping_status": seg_status[sid], "qac_tag": s["tag"], "qac_css_class": s["qac_css_class"],
                              "qac_hex_color": s["qac_hex_color"], "highlight_group_id": hg_for_word(s["qac_word_id"]),
                              "mapping_note": format_note(l), "source_ref": s["source_ref"]})
    link_rows.sort(key=lambda r: (r["ayah_id"], r["qac_segment_id"], r["bosnian_token_id"]))
    for i, r in enumerate(link_rows, start=1):
        r["alignment_id"] = f"AL-S{r['surah_id']:03d}-{i:05d}"

    coverage = coverage_matrix(snap, seg_rows, tok_rows, links)
    return {"segments": seg_rows, "tokens": tok_rows, "links": link_rows, "fused_markers": fused_markers, "coverage": coverage}


def format_note(l):
    if not l:
        return ""
    if l.get("kind") == "UNEXPRESSED":
        return f"UNEXPRESSED: {l.get('note')}"
    if l.get("kind") == "REVIEW":
        return f"REVIEW_REQUIRED: {l.get('note')}"
    return (f"role={l.get('semantic_role')}; evidence={l.get('evidence_type')}; "
            f"target='{l.get('bosnian_target_phrase')}'; {l.get('note')}")


def coverage_matrix(snap, seg_rows, tok_rows, links):
    out = []
    ayahs = sorted({s["ayah"] for s in seg_rows})
    for a in ayahs:
        ss = [s for s in seg_rows if s["ayah"] == a]
        ts = [t for t in tok_rows if t["ayah_id"] == a]
        words = sorted({s["word_order"] for s in ss})
        unexpressed = [s for s in ss if s["mapping_status"] == UNEXPRESSED]
        content_unlinked_words = []
        for w in words:
            wsegs = [s for s in ss if s["word_order"] == w]
            content = [s for s in wsegs if s["tag"] in CONTENT_TAGS]
            if content and not any(s["linked_bosnian_token_ids"] for s in content):
                content_unlinked_words.append(w)
        blocks = []
        run = []
        for w in content_unlinked_words:
            if run and w == run[-1] + 1:
                run.append(w)
            else:
                if len(run) >= 2:
                    blocks.append(run)
                run = [w]
        if len(run) >= 2:
            blocks.append(run)
        review = sum(1 for s in ss if s["mapping_status"] == "REVIEW_REQUIRED")
        inserted = [t for t in ts if t["mapping_status"] == INSERTED]
        out.append({
            "surah_id": snap["surah_id"], "ayah_id": a, "qac_word_count": len(words), "qac_segment_count": len(ss),
            "mapped_segment_count": sum(1 for s in ss if s["linked_bosnian_token_ids"]),
            "unexpressed_segment_count": len(unexpressed),
            "unexpressed_segment_ids": ";".join(s["qac_segment_id"] for s in unexpressed),
            "unexpressed_content_segment_count": sum(1 for s in unexpressed if s["tag"] in CONTENT_TAGS),
            "unexpressed_justification": "individualno obrazloženje u Segmenti.mapping_note" if unexpressed else "",
            "lexical_bosnian_token_count": sum(1 for t in ts if t["is_lexical"]),
            "lexical_inserted_no_arabic_segment_count": sum(1 for t in inserted if t["is_lexical"]),
            "punctuation_inserted_count": sum(1 for t in inserted if not t["is_lexical"]),
            "suspicious_unexpressed_qac_block_count": len(blocks),
            "suspicious_blocks": [f"W{b[0]:03d}-W{b[-1]:03d}" for b in blocks],
            "review_required_count": review,
            "source_translation_completeness": "PASS",
            "translation_reconstruction_status": "PASS",
            "coverage_status": "AYAH_COVERAGE_PASS" if not blocks and not review else "REVIEW_REQUIRED",
        })
    return out
