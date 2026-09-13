// Sije `surahs` tabelu direktno iz src/lib/surahs.ts, da metapodaci
// postoje na jednom mjestu (nema dupliranja 114 redova u Pythonu).
//
// Upotreba: npx tsx scripts/seed-surahs.ts
import { config } from "dotenv";
import { createClient } from "@supabase/supabase-js";
import { SURAHS } from "../src/lib/surahs";

config({ path: ".env.local" });

const url = process.env.NEXT_PUBLIC_SUPABASE_URL;
const key = process.env.SUPABASE_SERVICE_ROLE_KEY;

if (!url || !key) {
  console.error("GREŠKA: NEXT_PUBLIC_SUPABASE_URL / SUPABASE_SERVICE_ROLE_KEY nedostaju u .env.local");
  process.exit(1);
}

const supabase = createClient(url, key);

async function main() {
  const rows = SURAHS.map((s) => ({
    id: s.id,
    name_bs: s.nameBs,
    name_arabic: s.nameArabic,
    revelation_type: s.revelationType,
    ayah_count: s.ayahCount,
  }));

  const { error } = await supabase.from("surahs").upsert(rows, { onConflict: "id" });
  if (error) {
    console.error("GREŠKA:", error.message);
    process.exit(1);
  }
  console.log(`OK: upisano ${rows.length} sura u tabelu surahs.`);
}

main();
