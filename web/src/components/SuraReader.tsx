"use client";

import { useMemo, useRef, useState } from "react";
import type { BosnianToken, QacWord, SurahData } from "@/lib/types";
import { ayahAudioUrl, wordAudioUrl } from "@/lib/audio";
import { AyahRow } from "./AyahRow";

interface SuraReaderProps {
  data: SurahData;
}

type PlayingState = { kind: "ayah"; ayahNumber: number } | { kind: "word"; wordId: string } | null;

/**
 * Isticanje je GLOBALNO za cijelu suru — u svakom trenutku može biti
 * istaknuta samo jedna riječ (i njen bosanski par), nikad više ajeta
 * odjednom. Isto važi za zvuk: jedan zajednički <audio> element, klik
 * na bilo šta prekida prethodnu reprodukciju prije nove.
 */
export function SuraReader({ data }: SuraReaderProps) {
  const audioRef = useRef<HTMLAudioElement | null>(null);
  const [activeWordId, setActiveWordId] = useState<string | null>(null);
  const [activeTokenIds, setActiveTokenIds] = useState<Set<string>>(new Set());
  const [playing, setPlaying] = useState<PlayingState>(null);

  // word_id -> { ayahNumber, word } — za povratnu vezu token -> riječ i audio.
  const wordIndex = useMemo(() => {
    const map = new Map<string, { ayahNumber: number; word: QacWord }>();
    for (const ayah of data.ayat) {
      for (const w of ayah.words) {
        map.set(w.word_id, { ayahNumber: ayah.ayah_number, word: w });
      }
    }
    return map;
  }, [data.ayat]);

  const segmentToWord = useMemo(() => {
    const map = new Map<string, string>();
    for (const ayah of data.ayat) {
      for (const w of ayah.words) {
        for (const s of w.segments) map.set(s.segment_id, w.word_id);
      }
    }
    return map;
  }, [data.ayat]);

  function getAudio(): HTMLAudioElement {
    if (audioRef.current === null) {
      audioRef.current = new Audio();
      audioRef.current.addEventListener("ended", () => setPlaying(null));
    }
    return audioRef.current;
  }

  function playWord(word: QacWord, ayahNumber: number) {
    const audio = getAudio();
    audio.pause();
    audio.src = wordAudioUrl(data.surah_id, ayahNumber, word.position);
    audio.play().catch(() => setPlaying(null));
    setPlaying({ kind: "word", wordId: word.word_id });
  }

  function clearHighlight() {
    setActiveWordId(null);
    setActiveTokenIds(new Set());
  }

  function handleWordClick(word: QacWord, ayahNumber: number) {
    if (activeWordId === word.word_id) {
      // Ponovni klik na već istaknutu riječ gasi isticanje.
      clearHighlight();
      return;
    }

    const tokenIds = new Set<string>();
    for (const seg of word.segments) {
      for (const tid of seg.linked_token_ids) tokenIds.add(tid);
    }
    setActiveTokenIds(tokenIds);
    setActiveWordId(word.word_id);
    playWord(word, ayahNumber);
  }

  function handleTokenClick(token: BosnianToken) {
    if (activeTokenIds.has(token.token_id) && activeTokenIds.size === 1) {
      clearHighlight();
      return;
    }

    // Bosanska riječ nema svoju boju niti audio — vodi na svoj arapski
    // segment i odatle na cijelu riječ (i njen izgovor).
    let firstWordId: string | null = null;
    for (const segId of token.linked_segment_ids) {
      const wid = segmentToWord.get(segId);
      if (wid) {
        firstWordId = wid;
        break;
      }
    }
    setActiveTokenIds(new Set([token.token_id]));
    setActiveWordId(firstWordId);

    if (firstWordId) {
      const entry = wordIndex.get(firstWordId);
      if (entry) playWord(entry.word, entry.ayahNumber);
    }
  }

  function handlePlayAyah(ayahNumber: number) {
    const audio = getAudio();

    if (playing?.kind === "ayah" && playing.ayahNumber === ayahNumber) {
      audio.pause();
      audio.currentTime = 0;
      setPlaying(null);
      return;
    }

    audio.pause();
    audio.src = ayahAudioUrl(data.surah_id, ayahNumber);
    audio.play().catch(() => setPlaying(null));
    setPlaying({ kind: "ayah", ayahNumber });
  }

  return (
    <div className="sura-reader" onClick={clearHighlight}>
      {data.ayat.map((ayah) => (
        <AyahRow
          key={ayah.ayah_number}
          ayah={ayah}
          activeWordId={activeWordId}
          activeTokenIds={activeTokenIds}
          onWordClick={(word) => handleWordClick(word, ayah.ayah_number)}
          onTokenClick={handleTokenClick}
          onPlayAyah={handlePlayAyah}
          isAyahPlaying={playing?.kind === "ayah" && playing.ayahNumber === ayah.ayah_number}
        />
      ))}
    </div>
  );
}
