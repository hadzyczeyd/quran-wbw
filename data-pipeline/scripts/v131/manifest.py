# -*- coding: utf-8 -*-
"""Evidentira validan checkpoint u RUN_MANIFEST (nakon reopen/hash provjere artefakta).

Upotreba: uv run scripts/v131/manifest.py <RUN> <CP> <artifact_rel_path> <STATUS> [batch]
"""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from common import RUNS, atomic_write_json, load_json, now, sha256_file  # noqa: E402


def record(run, cp, rel, status, batch=None, extra=None):
    run_dir = os.path.join(RUNS, run)
    path = os.path.join(run_dir, "RUN_MANIFEST.json")
    m = load_json(path)
    art = os.path.join(run_dir, rel)
    load_json(art) if art.endswith(".json") else open(art, "rb").read()
    h = sha256_file(art)
    parent = m["checkpoints"][-1]["sha256"] if m["checkpoints"] else None
    m["checkpoint_seq"] = len(m["checkpoints"]) + 1
    m["checkpoints"].append({"seq": m["checkpoint_seq"], "checkpoint": cp, "batch": batch, "artifact_path": rel, "sha256": h,
                             "parent_checkpoint_hash": parent, "status": status, "timestamp": now(), **({"extra": extra} if extra else {})})
    m["current_checkpoint"] = cp
    m["last_valid_micro_checkpoint"] = f"{cp}:{batch or 'ALL'}"
    m["batch_retry_count"] = 0
    atomic_write_json(path, m)
    print(f"{cp} {status} {rel} {h[:16]}")


if __name__ == "__main__":
    a = sys.argv
    record(a[1], a[2], a[3], a[4], a[5] if len(a) > 5 else None)
