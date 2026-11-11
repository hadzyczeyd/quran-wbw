#!/bin/bash
# Tok panela korijena za jednu suru (nalog V7).
#   bash scripts/roots/run_sura.sh pre  N   → APP (generator) → VERIFIED → SHORT → EXCERPT_TODO_N
#   bash scripts/roots/run_sura.sh post N   → EXCERPTS_N (bazen) → FINAL → web/src/data/rootPanel/S<NNN>.json
set -e
cd "$(dirname "$0")/../.."
R=sources/root_panel; N=$2
if [ "$1" = pre ]; then
  uv run scripts/roots/gen_root_panel.py app $N
  uv run scripts/roots/verify_root_panel.py $R/SURA_${N}_ROOT_PANEL_APP.json $R/SURA_${N}_ROOT_PANEL_VERIFIED.json
  uv run scripts/roots/prefer_short.py $R/SURA_${N}_ROOT_PANEL_VERIFIED.json $R/SURA_${N}_ROOT_PANEL_SHORT.json
  uv run scripts/roots/excerpts.py todo $R/SURA_${N}_ROOT_PANEL_SHORT.json $R/EXCERPT_TODO_${N}.json
else
  uv run scripts/roots/swap_gloss.py apply $N
  uv run scripts/roots/excerpt_pool.py split $N
  uv run scripts/roots/excerpts.py apply $R/SURA_${N}_ROOT_PANEL_SHORT.json $R/EXCERPTS_${N}.json $R/SURA_${N}_ROOT_PANEL_FINAL.json
  uv run scripts/roots/build_app_root_panel.py $R/SURA_${N}_ROOT_PANEL_FINAL.json $N
fi
