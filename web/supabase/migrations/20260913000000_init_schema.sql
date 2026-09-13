-- Kur'an riječ po riječ — osnovna šema.
--
-- Boja se čuva DIREKTNO po segmentu/tokenu (qac_css_class + qac_hex_color),
-- bez posredničke color_keys tabele — NALOG-V13 poglavlje 5 traži direktno
-- preslikavanje QAC boje, ne ponovno izvođenje boje preko zasebne legende.
--
-- Svi identifikatori (word_id, segment_id, token_id) su stabilni stringovi
-- iz pipeline-a (npr. 'S001-A001-W001'), ne generisani serial/uuid — isti
-- ključevi kao u Excel izvorima, radi lakšeg poravnanja i ponovnog uvoza.

create table surahs (
  id smallint primary key,
  name_bs text not null,
  name_arabic text not null,
  revelation_type text not null check (revelation_type in ('meccan', 'medinan')),
  ayah_count smallint not null
);

create table ayahs (
  surah_id smallint not null references surahs (id),
  ayah_number smallint not null,
  text_uthmani text not null,
  mehanovic_text text,
  primary key (surah_id, ayah_number)
);

create table words (
  word_id text primary key,
  surah_id smallint not null,
  ayah_number smallint not null,
  position smallint not null,
  text_uthmani text not null,
  transliteration text,
  gloss text,
  foreign key (surah_id, ayah_number) references ayahs (surah_id, ayah_number)
);
create index words_ayah_idx on words (surah_id, ayah_number);

create table word_segments (
  segment_id text primary key,
  word_id text not null references words (word_id),
  segment_order smallint not null,
  segment_text text not null,
  qac_tag text not null,
  qac_full_description text,
  qac_css_class text not null,
  qac_hex_color text not null,
  lemma text,
  root text,
  expression_status text not null
);
create index word_segments_word_idx on word_segments (word_id);

create table bosnian_tokens (
  token_id text primary key,
  surah_id smallint not null,
  ayah_number smallint not null,
  position smallint not null,
  display_text text not null,
  qac_css_class text not null,
  qac_hex_color text not null,
  mapping_status text not null,
  foreign key (surah_id, ayah_number) references ayahs (surah_id, ayah_number)
);
create index bosnian_tokens_ayah_idx on bosnian_tokens (surah_id, ayah_number);

-- Many-to-many veza segment <-> token (NALOG-V13 poglavlje 9: jedan
-- segment može imati više tokena, jedan token može pokrivati više
-- segmenata izraza).
create table token_segment_links (
  id bigint generated always as identity primary key,
  segment_id text not null references word_segments (segment_id),
  token_id text not null references bosnian_tokens (token_id),
  unique (segment_id, token_id)
);
create index token_segment_links_segment_idx on token_segment_links (segment_id);
create index token_segment_links_token_idx on token_segment_links (token_id);

-- Poruke sa Contact forme. Bez korisničkih naloga — anonimni javni unos.
create table contact_messages (
  id bigint generated always as identity primary key,
  name text not null,
  email text not null,
  message text not null,
  created_at timestamptz not null default now()
);

-- RLS: sadržaj je javan za čitanje; contact_messages je javan za upis
-- (anonimna forma) ali NE za čitanje (da niko ne vidi tuđe poruke).
alter table surahs enable row level security;
alter table ayahs enable row level security;
alter table words enable row level security;
alter table word_segments enable row level security;
alter table bosnian_tokens enable row level security;
alter table token_segment_links enable row level security;
alter table contact_messages enable row level security;

create policy "surahs_public_read" on surahs for select using (true);
create policy "ayahs_public_read" on ayahs for select using (true);
create policy "words_public_read" on words for select using (true);
create policy "word_segments_public_read" on word_segments for select using (true);
create policy "bosnian_tokens_public_read" on bosnian_tokens for select using (true);
create policy "token_segment_links_public_read" on token_segment_links for select using (true);

create policy "contact_messages_public_insert" on contact_messages for insert with check (true);
