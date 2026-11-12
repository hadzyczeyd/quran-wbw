import type { RootPanelRoot } from "./rootPanel";

const cache = new Map<number, Promise<Record<string, RootPanelRoot>>>();

/**
 * Kartice korijena sure, učitane u pregledniku tek kad zatrebaju (prvi klik
 * na imenicu ili glagol) — stranica sure ostaje lagana. Neuspjelo učitavanje se ponovi na sljedeći klik.
 */
export function loadRootPanelRoots(surahId: number): Promise<Record<string, RootPanelRoot>> {
  let p = cache.get(surahId);
  if (!p) {
    p = fetch(`/api/root-panel/${surahId}`).then((r) => {
      if (!r.ok) throw new Error(`root-panel ${r.status}`);
      return r.json() as Promise<Record<string, RootPanelRoot>>;
    });
    p.catch(() => cache.delete(surahId));
    cache.set(surahId, p);
  }
  return p;
}
