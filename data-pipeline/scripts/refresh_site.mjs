// Odmah osvježi stranice sura na sajtu nakon ručne izmjene u bazi.
//   node data-pipeline/scripts/refresh_site.mjs 107 110 114
// Čita SUPABASE_SERVICE_ROLE_KEY iz web/.env.local; ključ ide samo na vlastiti sajt (HTTPS).
import { readFileSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const SITE = process.env.SITE_URL ?? "https://kuran-rijecporijec.com";
const envPath = join(dirname(fileURLToPath(import.meta.url)), "..", "..", "web", ".env.local");
const env = Object.fromEntries(
  readFileSync(envPath, "utf8").split(/\r?\n/).filter((l) => /^\w+=/.test(l))
    .map((l) => [l.slice(0, l.indexOf("=")), l.slice(l.indexOf("=") + 1).replace(/^"|"$/g, "")]),
);
const suras = process.argv.slice(2).map(Number).filter((n) => n >= 1 && n <= 114);
if (!suras.length) {
  console.error("Upotreba: node refresh_site.mjs <broj sure> [...]");
  process.exit(1);
}
const paths = suras.map((n) => `/sura/${n}`);
const r = await fetch(`${SITE}/api/revalidate`, {
  method: "POST",
  headers: { "Content-Type": "application/json", Authorization: `Bearer ${env.SUPABASE_SERVICE_ROLE_KEY}` },
  body: JSON.stringify({ paths }),
});
const body = await r.json().catch(() => ({}));
if (!r.ok) {
  console.error(`Greška ${r.status}:`, body);
  process.exit(1);
}
// Prva posjeta iscrta stranicu iznova (da je i sljedeći posjetilac odmah dobije svježu).
for (const p of body.revalidated) {
  const res = await fetch(SITE + p);
  console.log(`${p}: osvježeno (${res.status}, ${res.headers.get("x-nextjs-cache") ?? "-"})`);
}
