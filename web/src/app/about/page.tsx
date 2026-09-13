import type { Metadata } from "next";
import "@/styles/about.css";

export const metadata: Metadata = {
  title: "O projektu — Kur'an riječ po riječ",
  description: "Izvori, licence i zahvale za Kur'an riječ po riječ.",
};

export default function AboutPage() {
  return (
    <main className="page-shell about-page">
      <h1>O projektu</h1>
      <p className="about-lede">
        Kur&apos;an riječ po riječ je lični, pasioni projekat — web aplikacija
        za učenje kur&apos;anskog arapskog kroz bosanski jezik. Svaka arapska
        riječ je obojena prema svojoj gramatičkoj ulozi, direktno preslikano
        iz Quranic Arabic Corpusa (corpus.quran.com), uz bosanski prijevod
        koji prati isti redoslijed riječi. Cilj je da se gramatika usvaja
        usput, kroz boju i zvuk, a ne napamet iz tabela.
      </p>

      <section>
        <h2>Izvori i licence</h2>
        <dl className="about-credits">
          <dt>Arapski tekst i morfologija</dt>
          <dd>
            <a href="https://corpus.quran.com" target="_blank" rel="noreferrer">
              Quranic Arabic Corpus
            </a>{" "}
            (Kais Dukes) — segmentacija, gramatičke oznake i boje po
            segmentu, preuzeto direktno bez preklasifikacije.
          </dd>

          <dt>Izvorni kur&apos;anski tekst</dt>
          <dd>
            <a href="https://tanzil.net" target="_blank" rel="noreferrer">
              Tanzil.info
            </a>{" "}
            (CC BY-ND 3.0) i{" "}
            <a href="https://al-quran.fr" target="_blank" rel="noreferrer">
              al-quran.fr
            </a>{" "}
            (CC0).
          </dd>

          <dt>Bosanski prijevod</dt>
          <dd>
            Muhamed Mehanović, objavljeno na{" "}
            <a href="https://quranenc.com" target="_blank" rel="noreferrer">
              QuranEnc.com
            </a>
            . Prijevod se čuva tačno kako je objavljen, bez izmjena.
          </dd>

          <dt>Recitacija cijelog ajeta</dt>
          <dd>
            <a href="https://everyayah.com" target="_blank" rel="noreferrer">
              everyayah.com
            </a>{" "}
            — Mahmoud Khalil Al-Husary.
          </dd>

          <dt>Izgovor pojedinačne riječi</dt>
          <dd>
            Tafsir Center for Quranic Studies, uz ljubaznu dozvolu preko{" "}
            <a href="https://quran.foundation" target="_blank" rel="noreferrer">
              Quran Foundation
            </a>{" "}
            (Quran.com) Content API-ja. Samo streaming — ne čuva se trajno.
          </dd>

          <dt>Fontovi</dt>
          <dd>
            Amiri Quran (Khaled Hosny) za arapski tekst, Montserrat (Julieta
            Ulanovsky) za bosanski — oba preko Google Fonts, slobodne
            licence.
          </dd>
        </dl>
      </section>

      <section>
        <h2>Napomena</h2>
        <p>
          Sav kur&apos;anski sadržaj prikazan je u svom izvornom obliku, bez
          izmjena. Ako primijetiš grešku u prijevodu, boji ili vezi između
          arapske i bosanske riječi,{" "}
          <a href="/contact">javi na Contact stranici</a>.
        </p>
      </section>
    </main>
  );
}
