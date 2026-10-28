import sanitize from "sanitize-html";

/**
 * Sadržaj članka prije prikaza — samo oznake koje TipTap editor (PostEditor)
 * stvarno proizvodi. Upis je već ograničen na admina (RLS), ovo je druga
 * linija odbrane: ni ukradena sesija ni ručno umetnut HTML ne mogu ubaciti
 * skriptu, iframe ili javascript: link na javnu stranicu.
 */
export function sanitizeBlogHtml(html: string): string {
  return sanitize(html, {
    allowedTags: [
      "p", "br", "h2", "h3", "h4", "strong", "b", "em", "i", "u", "s", "code", "pre",
      "blockquote", "hr", "ul", "ol", "li", "a", "img", "span",
      "table", "colgroup", "col", "thead", "tbody", "tr", "th", "td",
    ],
    allowedAttributes: {
      a: ["href", "target", "rel"],
      img: ["src", "alt", "title", "width", "height", "loading"],
      th: ["colspan", "rowspan", "colwidth"],
      td: ["colspan", "rowspan", "colwidth"],
      col: ["span", "style"],
      table: ["style"],
      ol: ["start"],
    },
    allowedStyles: {
      "*": { "min-width": [/^\d+(\.\d+)?px$/], width: [/^\d+(\.\d+)?(px|%)$/] },
    },
    allowedSchemes: ["https", "http", "mailto"],
    allowedSchemesByTag: { img: ["https"] },
    allowProtocolRelative: false,
    transformTags: {
      a: (tagName, attribs) => ({
        tagName,
        attribs: { ...attribs, target: "_blank", rel: "noopener noreferrer nofollow" },
      }),
    },
  });
}
