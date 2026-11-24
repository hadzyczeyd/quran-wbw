import { revalidatePath } from "next/cache";
import { createClient } from "@supabase/supabase-js";

/**
 * Trenutno osvježavanje statičnih stranica nakon ručne izmjene podataka u bazi
 * (npr. ispravka veza u jednoj suri), umjesto čekanja do sat vremena (revalidate).
 *
 * POST /api/revalidate  { "paths": ["/sura/107"] }
 * Authorization: Bearer <Supabase service role ključ>
 *
 * Ključ se ne čuva na serveru: provjerava se tako što se s njim pozove Supabase
 * admin API, što uspijeva samo sa service role ključem. Bez ispravnog ključa → 401.
 */
const ALLOWED = /^\/(sura\/([1-9]\d?|10\d|11[0-4])|sure)?$/;

export async function POST(request: Request) {
  const key = request.headers.get("authorization")?.replace(/^Bearer\s+/i, "") ?? "";
  const url = process.env.NEXT_PUBLIC_SUPABASE_URL;
  if (!key || !url) return Response.json({ error: "unauthorized" }, { status: 401 });

  const admin = createClient(url, key, { auth: { persistSession: false, autoRefreshToken: false } });
  const { error } = await admin.auth.admin.listUsers({ page: 1, perPage: 1 });
  if (error) return Response.json({ error: "unauthorized" }, { status: 401 });

  let paths: unknown;
  try {
    ({ paths } = await request.json());
  } catch {
    return Response.json({ error: "body: { paths: string[] }" }, { status: 400 });
  }
  if (!Array.isArray(paths) || paths.length === 0 || paths.length > 120) {
    return Response.json({ error: "paths: 1–120 putanja" }, { status: 400 });
  }
  const done: string[] = [];
  for (const p of paths) {
    if (typeof p === "string" && ALLOWED.test(p)) {
      revalidatePath(p);
      done.push(p);
    }
  }
  return Response.json({ revalidated: done });
}
