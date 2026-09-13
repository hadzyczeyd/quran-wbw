// Standardni popis 114 sura — broj, bosanski naziv (uobičajena
// transliteracija, ista konvencija kao nazivi Excel fajlova u pipeline-u),
// arapski naziv, mjesto objave i broj ajeta. Ovo je opšte poznata
// kur'anska metapodataka, nezavisna od QAC pipeline-a; kasnije zamjenjuje
// `surahs` tabelu iz Supabase baze.
//
// Mekka/Medina razvrstavanje prati uobičajenu konvenciju štampanih
// mushafa (npr. King Fahd Complex) — kod par ajeta postoji manja
// naučna nesuglasica oko tačnog mjesta objave, ali ovo je najrašireniji
// standard.

export type RevelationType = "meccan" | "medinan";

export interface SurahMeta {
  id: number;
  nameBs: string;
  nameArabic: string;
  revelationType: RevelationType;
  ayahCount: number;
}

const MEDINAN_IDS = new Set([
  2, 3, 4, 5, 8, 9, 22, 24, 33, 47, 48, 49, 57, 58, 59, 60, 61, 62, 63, 64,
  65, 66, 76, 98, 99, 110,
]);

function meta(
  id: number,
  nameBs: string,
  nameArabic: string,
  ayahCount: number
): SurahMeta {
  return {
    id,
    nameBs,
    nameArabic,
    ayahCount,
    revelationType: MEDINAN_IDS.has(id) ? "medinan" : "meccan",
  };
}

export const SURAHS: SurahMeta[] = [
  meta(1, "El-Fatiha", "الفاتحة", 7),
  meta(2, "El-Bekara", "البقرة", 286),
  meta(3, "Alu Imran", "آل عمران", 200),
  meta(4, "En-Nisa", "النساء", 176),
  meta(5, "El-Maida", "المائدة", 120),
  meta(6, "El-En'am", "الأنعام", 165),
  meta(7, "El-A'raf", "الأعراف", 206),
  meta(8, "El-Enfal", "الأنفال", 75),
  meta(9, "Et-Tevba", "التوبة", 129),
  meta(10, "Junus", "يونس", 109),
  meta(11, "Hud", "هود", 123),
  meta(12, "Jusuf", "يوسف", 111),
  meta(13, "Er-Ra'd", "الرعد", 43),
  meta(14, "Ibrahim", "ابراهيم", 52),
  meta(15, "El-Hidžr", "الحجر", 99),
  meta(16, "En-Nahl", "النحل", 128),
  meta(17, "El-Isra", "الإسراء", 111),
  meta(18, "El-Kehf", "الكهف", 110),
  meta(19, "Merjem", "مريم", 98),
  meta(20, "Ta-ha", "طه", 135),
  meta(21, "El-Enbija", "الأنبياء", 112),
  meta(22, "El-Hadždž", "الحج", 78),
  meta(23, "El-Mu'minun", "المؤمنون", 118),
  meta(24, "En-Nur", "النور", 64),
  meta(25, "El-Furkan", "الفرقان", 77),
  meta(26, "Eš-Šu'ara", "الشعراء", 227),
  meta(27, "En-Neml", "النمل", 93),
  meta(28, "El-Kasas", "القصص", 88),
  meta(29, "El-Ankebut", "العنكبوت", 69),
  meta(30, "Er-Rum", "الروم", 60),
  meta(31, "Lukman", "لقمان", 34),
  meta(32, "Es-Sedžda", "السجدة", 30),
  meta(33, "El-Ahzab", "الأحزاب", 73),
  meta(34, "Sebe'", "سبإ", 54),
  meta(35, "Fatir", "فاطر", 45),
  meta(36, "Ja-sin", "يس", 83),
  meta(37, "Es-Saffat", "الصافات", 182),
  meta(38, "Sad", "ص", 88),
  meta(39, "Ez-Zumer", "الزمر", 75),
  meta(40, "Gafir", "غافر", 85),
  meta(41, "Fussilet", "فصلت", 54),
  meta(42, "Eš-Šura", "الشورى", 53),
  meta(43, "Ez-Zuhruf", "الزخرف", 89),
  meta(44, "Ed-Duhan", "الدخان", 59),
  meta(45, "El-Džasija", "الجاثية", 37),
  meta(46, "El-Ahkaf", "الأحقاف", 35),
  meta(47, "Muhammed", "محمد", 38),
  meta(48, "El-Feth", "الفتح", 29),
  meta(49, "El-Hudžurat", "الحجرات", 18),
  meta(50, "Kaf", "ق", 45),
  meta(51, "Ez-Zarijat", "الذاريات", 60),
  meta(52, "Et-Tur", "الطور", 49),
  meta(53, "En-Nedžm", "النجم", 62),
  meta(54, "El-Kamer", "القمر", 55),
  meta(55, "Er-Rahman", "الرحمن", 78),
  meta(56, "El-Vakia", "الواقعة", 96),
  meta(57, "El-Hadid", "الحديد", 29),
  meta(58, "El-Mudžadela", "المجادلة", 22),
  meta(59, "El-Hašr", "الحشر", 24),
  meta(60, "El-Mumtehina", "الممتحنة", 13),
  meta(61, "Es-Saff", "الصف", 14),
  meta(62, "El-Džumu'a", "الجمعة", 11),
  meta(63, "El-Munafikun", "المنافقون", 11),
  meta(64, "Et-Tegabun", "التغابن", 18),
  meta(65, "Et-Talak", "الطلاق", 12),
  meta(66, "Et-Tahrim", "التحريم", 12),
  meta(67, "El-Mulk", "الملك", 30),
  meta(68, "El-Kalem", "القلم", 52),
  meta(69, "El-Hakka", "الحاقة", 52),
  meta(70, "El-Mearidž", "المعارج", 44),
  meta(71, "Nuh", "نوح", 28),
  meta(72, "El-Džinn", "الجن", 28),
  meta(73, "El-Muzzemmil", "المزمل", 20),
  meta(74, "El-Muddessir", "المدثر", 56),
  meta(75, "El-Kijama", "القيامة", 40),
  meta(76, "El-Insan", "الانسان", 31),
  meta(77, "El-Murselat", "المرسلات", 50),
  meta(78, "En-Nebe", "النبإ", 40),
  meta(79, "En-Nazi'at", "النازعات", 46),
  meta(80, "Abese", "عبس", 42),
  meta(81, "Et-Tekvir", "التكوير", 29),
  meta(82, "El-Infitar", "الإنفطار", 19),
  meta(83, "El-Mutaffifin", "المطففين", 36),
  meta(84, "El-Inšikak", "الإنشقاق", 25),
  meta(85, "El-Burudž", "البروج", 22),
  meta(86, "Et-Tarik", "الطارق", 17),
  meta(87, "El-A'la", "الأعلى", 19),
  meta(88, "El-Gašija", "الغاشية", 26),
  meta(89, "El-Fedžr", "الفجر", 30),
  meta(90, "El-Beled", "البلد", 20),
  meta(91, "Eš-Šems", "الشمس", 15),
  meta(92, "El-Lejl", "الليل", 21),
  meta(93, "Ed-Duha", "الضحى", 11),
  meta(94, "Eš-Šerh", "الشرح", 8),
  meta(95, "Et-Tin", "التين", 8),
  meta(96, "El-Alek", "العلق", 19),
  meta(97, "El-Kadr", "القدر", 5),
  meta(98, "El-Bejjina", "البينة", 8),
  meta(99, "Ez-Zilzal", "الزلزلة", 8),
  meta(100, "El-Adijat", "العاديات", 11),
  meta(101, "El-Karia", "القارعة", 11),
  meta(102, "Et-Tekasur", "التكاثر", 8),
  meta(103, "El-Asr", "العصر", 3),
  meta(104, "El-Humeza", "الهمزة", 9),
  meta(105, "El-Fil", "الفيل", 5),
  meta(106, "Kurejš", "قريش", 4),
  meta(107, "El-Maun", "الماعون", 7),
  meta(108, "El-Kevser", "الكوثر", 3),
  meta(109, "El-Kafirun", "الكافرون", 6),
  meta(110, "En-Nasr", "النصر", 3),
  meta(111, "El-Leheb", "المسد", 5),
  meta(112, "El-Ihlas", "الإخلاص", 4),
  meta(113, "El-Felek", "الفلق", 5),
  meta(114, "En-Nas", "الناس", 6),
];
