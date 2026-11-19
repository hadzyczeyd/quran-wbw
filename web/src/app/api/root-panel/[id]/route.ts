import type { RootPanelData } from "@/lib/rootPanel";

// Kartice panela korijena po suri, statično generisane pri buildu. Stranica
// sure nosi samo indeks klikabilnih riječi, a kartice preglednik dohvati
// odavde tek pri prvom kliku (sura 2 ima ~2 MB kartica).
//
// Bez ručnog gzipa: od Next 16.4.6 server (i Hostinger CDN) sam komprimuje
// ovaj odgovor, pa je ručni gzip bio dvostruk i preglednik nije mogao
// pročitati JSON (korijeni nisu radili ni na jednoj suri).
export const dynamicParams = false;

export async function generateStaticParams() {
  return Array.from({ length: 114 }, (_, i) => ({ id: String(i + 1) }));
}

export async function GET(_request: Request, { params }: { params: Promise<{ id: string }> }) {
  const { id } = await params;
  const mod = await import(`@/data/rootPanel/S${id.padStart(3, "0")}.json`);
  return new Response(JSON.stringify((mod.default as RootPanelData).roots), {
    headers: {
      "Content-Type": "application/json; charset=utf-8",
      "Cache-Control": "public, max-age=3600, stale-while-revalidate=86400",
    },
  });
}
