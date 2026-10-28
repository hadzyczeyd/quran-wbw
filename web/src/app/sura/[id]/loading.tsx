import "@/styles/reader.css";

/** Trenutni odziv na klik dok se sura (ako nije unaprijed dohvaćena) učitava. */
export default function Loading() {
  return (
    <main className="page-shell reader-layout" aria-busy="true">
      <div className="reader-left-column" />
      <div className="sura-main-column">
        <p className="sura-loading">Učitavanje sure…</p>
      </div>
    </main>
  );
}
