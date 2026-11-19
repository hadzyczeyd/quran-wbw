import type { RootPanelRoot } from "./rootPanel";

const cache = new Map<number, Promise<Record<string, RootPanelRoot>>>();

/**
 * Tijelo odgovora kao JSON. Ako je odgovor ipak (dvostruko) gzipovan —
 * stari keš preglednika/service workera iz verzije s ručnim gzipom —
 * raspakuje se ovdje umjesto da korijeni ne rade.
 */
async function readJson(r: Response): Promise<Record<string, RootPanelRoot>> {
  const buf = new Uint8Array(await r.arrayBuffer());
  if (buf[0] === 0x1f && buf[1] === 0x8b && typeof DecompressionStream !== "undefined") {
    const stream = new Blob([buf]).stream().pipeThrough(new DecompressionStream("gzip"));
    return JSON.parse(await new Response(stream).text());
  }
  return JSON.parse(new TextDecoder().decode(buf));
}

/**
 * Kartice korijena sure, učitane u pregledniku tek kad zatrebaju (prvi klik
 * na imenicu ili glagol) — stranica sure ostaje lagana. Neuspjelo učitavanje se ponovi na sljedeći klik.
 */
export function loadRootPanelRoots(surahId: number): Promise<Record<string, RootPanelRoot>> {
  let p = cache.get(surahId);
  if (!p) {
    p = fetch(`/api/root-panel/${surahId}`).then((r) => {
      if (!r.ok) throw new Error(`root-panel ${r.status}`);
      return readJson(r);
    });
    p.catch(() => cache.delete(surahId));
    cache.set(surahId, p);
  }
  return p;
}
