// PRIVREMENO (selidba na Hostinger): samo imena zaglavlja, bez vrijednosti; vrijednost samo za
// zaglavlja čije ime sliči državi i koja imaju tačno 2 slova. Briše se nakon provjere.
export const dynamic = "force-dynamic";

export function GET(request: Request) {
  const names: string[] = [];
  const country: Record<string, string> = {};
  request.headers.forEach((value, name) => {
    names.push(name);
    if (/country|geo|region/i.test(name) && /^[A-Za-z]{2}$/.test(value)) country[name] = value;
  });
  return Response.json({ names: names.sort(), country });
}
