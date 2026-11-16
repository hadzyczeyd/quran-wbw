import "@/styles/reader.css";

/** Kostur čitača dok se sura (ako nije unaprijed dohvaćena) učitava — zauzima isto mjesto kao sadržaj. */
export default function Loading() {
  return (
    <main className="reader" aria-busy="true" aria-label="Učitavanje sure">
      <div className="reader-toolbar">
        <div className="reader-toolbar-inner" />
      </div>
      <div className="reader-columns">
        <div className="reader-main">
          <div className="skeleton-block is-title" />
          {[0, 1, 2].map((i) => (
            <div key={i} className="skeleton-ayah">
              <div className="skeleton-block is-ar" />
              <div className="skeleton-block is-ar short" />
              <div className="skeleton-block is-tr" />
            </div>
          ))}
        </div>
      </div>
    </main>
  );
}
