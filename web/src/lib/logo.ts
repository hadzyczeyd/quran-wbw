/**
 * Logo (otvoreni Mushaf na rahli) kao vektor — precrtan iz originalnog
 * favicon.ico (128 px) da bude oštar u svakoj veličini (zaglavlje, PWA ikone).
 * Koordinate su za viewBox 0 0 128 128; crta se lijeva polovina, desna je
 * njen odraz (LOGO_MIRROR).
 */
export const LOGO_HALF_PATHS = [
  // korica (lijevi rub i donja ivica)
  "M28 30.6 L31.6 30.6 L22.8 60.3 L64 79.4 L64 83.2 L19.4 63.8 L19.4 58.3 Z",
  // stranica
  "M33.8 30.6 C42 33 52 34.3 61.6 42.3 L61.6 76.6 C57.5 72.2 45.5 66.4 25.6 58.2 Z",
  // noga rahle
  "M64 78.6 L41 84.6 C38.5 86.8 36.5 88.6 34 89.8 L29.5 91.8 C27.6 92.8 27 94.6 27.3 96.4 C27.6 98.2 28.6 98.8 30 98.6 L40.5 93.4 L64 83.4 Z",
  // gornji krak rahle
  "M38.4 76.8 L41.6 76.8 L47.5 80 L47 84 L38.5 80.6 Z",
  // spoj ispod knjige
  "M46 75 L64 81 L64 84 L46 87.5 Z",
];

export const LOGO_MIRROR = "translate(128 0) scale(-1 1)";

/** Originalna zlatna boja logotipa. */
export const LOGO_GOLD = "#b8912e";

/** Kompletan SVG kao string (za generisanje PNG ikona). */
export function logoSvg(color: string, size: number) {
  const half = LOGO_HALF_PATHS.map((d) => `<path d="${d}"/>`).join("");
  return `<svg xmlns="http://www.w3.org/2000/svg" width="${size}" height="${size}" viewBox="0 0 128 128"><g fill="${color}">${half}<g transform="${LOGO_MIRROR}">${half}</g></g></svg>`;
}
