// Ručna ispravka jednog ajeta u bazi prema opisu (spec JSON) — tokeni, tekst, veze, boje.
//   node data-pipeline/scripts/manual/apply_ayah.mjs spec.json
// spec: { "surah": 92, "ayah": 19, "text": "…", "tokens": [ { "id": "S092-A019-B001", "text": "ne", "segs": ["S092-A019-W001-S02"] }, … ] }
// Boja i status se izvode: bez segmenta = crno (inserted); segmenti različitih boja = spojeni ("fused");
// inače boja segmenta, ONE_TO_MANY ako segment nosi više tokena. Postojeći token zadržava status ako mu se veze ne mijenjaju.
import { readFileSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";
import { createRequire } from "node:module";

const webDir = join(dirname(fileURLToPath(import.meta.url)), "..", "..", "..", "web");
const require = createRequire(join(webDir, "package.json"));
const { createClient } = require("@supabase/supabase-js");
const env = Object.fromEntries(readFileSync(join(webDir, ".env.local"), "utf8").split(/\r?\n/).filter((l) => /^\w+=/.test(l)).map((l) => [l.slice(0, l.indexOf("=")), l.slice(l.indexOf("=") + 1).replace(/^"|"$/g, "")]));
const sb = createClient(env.NEXT_PUBLIC_SUPABASE_URL, env.SUPABASE_SERVICE_ROLE_KEY, { auth: { persistSession: false } });
const ok = (r, what) => { if (r.error) throw new Error(`${what}: ${r.error.message}`); return r.data; };

const spec = JSON.parse(readFileSync(process.argv[2], "utf8"));
const { surah, ayah } = spec;
const pre = `S${String(surah).padStart(3, "0")}-A${String(ayah).padStart(3, "0")}-`;

const oldTokens = ok(await sb.from("bosnian_tokens").select("*").eq("surah_id", surah).eq("ayah_number", ayah), "tokeni");
const oldLinks = ok(await sb.from("token_segment_links").select("segment_id, token_id").like("token_id", `${pre}%`), "veze");
const segs = ok(await sb.from("word_segments").select("segment_id, qac_css_class, qac_hex_color, expression_status").like("segment_id", `${pre}%`), "segmenti");
const segById = new Map(segs.map((s) => [s.segment_id, s]));
for (const t of spec.tokens) for (const s of t.segs) if (!segById.has(s)) throw new Error(`nepoznat segment ${s}`);

const oldSegsOf = (id) => oldLinks.filter((l) => l.token_id === id).map((l) => l.segment_id).sort().join(",");
const tokensPerSeg = new Map();
for (const t of spec.tokens) for (const s of t.segs) tokensPerSeg.set(s, (tokensPerSeg.get(s) ?? 0) + 1);
const oldById = new Map(oldTokens.map((t) => [t.token_id, t]));

const rows = spec.tokens.map((t, i) => {
  const old = oldById.get(t.id);
  let css, hex, status;
  const classes = [...new Set(t.segs.map((s) => segById.get(s).qac_css_class))];
  if (t.segs.length === 0) [css, hex, status] = ["inserted_no_arabic_segment", "#000000", "inserted_no_arabic_segment"];
  else if (classes.length > 1) [css, hex, status] = ["fused", "#000000", "MAPPED_FUSED_MULTI_SEGMENT"];
  else {
    const seg = segById.get(t.segs[0]);
    css = seg.qac_css_class;
    hex = seg.qac_hex_color;
    status = t.segs.some((s) => tokensPerSeg.get(s) > 1) ? "MAPPED_ONE_TO_MANY" : "MAPPED_ONE_TO_ONE";
  }
  if (old && oldSegsOf(t.id) === [...t.segs].sort().join(",") && old.qac_css_class === css) status = old.mapping_status;
  return { token_id: t.id, surah_id: surah, ayah_number: ayah, position: i + 1, display_text: t.text, qac_css_class: css, qac_hex_color: hex, mapping_status: status };
});

// 1) veze ajeta van, 2) tokeni (privremene pozicije da se izbjegnu sudari), 3) veze nazad, 4) status segmenata, 5) tekst ajeta
ok(await sb.from("token_segment_links").delete().like("token_id", `${pre}%`), "brisanje veza");
const keep = new Set(rows.map((r) => r.token_id));
const gone = oldTokens.filter((t) => !keep.has(t.token_id)).map((t) => t.token_id);
if (gone.length) ok(await sb.from("bosnian_tokens").delete().in("token_id", gone), "brisanje tokena");
for (const r of rows) if (oldById.has(r.token_id)) ok(await sb.from("bosnian_tokens").update({ position: 1000 + r.position }).eq("token_id", r.token_id), "pozicija");
ok(await sb.from("bosnian_tokens").upsert(rows, { onConflict: "token_id" }), "tokeni");
const links = spec.tokens.flatMap((t) => t.segs.map((s) => ({ segment_id: s, token_id: t.id })));
if (links.length) ok(await sb.from("token_segment_links").insert(links), "veze");
for (const s of segs) {
  const want = tokensPerSeg.has(s.segment_id) ? "EXPRESSED_IN_BOSNIAN" : "QAC_SEGMENT_NOT_SEPARATELY_EXPRESSED_IN_BOSNIAN";
  if (s.expression_status !== want) ok(await sb.from("word_segments").update({ expression_status: want }).eq("segment_id", s.segment_id), "segment");
}
if (spec.text) ok(await sb.from("ayahs").update({ mehanovic_text: spec.text }).eq("surah_id", surah).eq("ayah_number", ayah), "tekst");

const check = ok(await sb.from("bosnian_tokens").select("position, display_text, qac_css_class").eq("surah_id", surah).eq("ayah_number", ayah).order("position"), "provjera");
console.log(`${surah}:${ayah}: ` + check.map((t) => `${t.display_text}=${t.qac_css_class.replace(/^seg/, "").replace("inserted_no_arabic_segment", "crno")}`).join("  "));
