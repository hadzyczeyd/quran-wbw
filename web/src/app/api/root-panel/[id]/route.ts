import { gzipSync } from "node:zlib";
import type { RootPanelData } from "@/lib/rootPanel";

// Kartice panela korijena po suri, statično generisane pri buildu. Stranica
// sure nosi samo indeks klikabilnih riječi, a kartice preglednik dohvati
// odavde tek pri prvom kliku (sura 2 ima ~1,8 MB kartica).
export const dynamicParams = false;

export async function generateStaticParams() {
  return Array.from({ length: 114 }, (_, i) => ({ id: String(i + 1) }));
}

export async function GET(_request: Request, { params }: { params: Promise<{ id: string }> }) {
  const { id } = await params;
  const mod = await import(`@/data/rootPanel/S${id.padStart(3, "0")}.json`);
  // Next ne komprimuje statično generisane odgovore route handlera, pa se
  // gzip radi ovdje (2,3 MB → ~0,3 MB za suru 2); fetch ga uvijek prihvata.
  const json = JSON.stringify((mod.default as RootPanelData).roots);
  // Dev server sam komprimuje odgovore — ručni gzip bi tamo bio dvostruk (neparsiran JSON).
  if (process.env.NODE_ENV !== "production") {
    return new Response(json, { headers: { "Content-Type": "application/json; charset=utf-8" } });
  }
  const body = gzipSync(json, { level: 9 });
  return new Response(body, {
    headers: {
      "Content-Type": "application/json; charset=utf-8",
      "Content-Encoding": "gzip",
      Vary: "Accept-Encoding",
      "Cache-Control": "public, max-age=3600, stale-while-revalidate=86400",
    },
  });
}
