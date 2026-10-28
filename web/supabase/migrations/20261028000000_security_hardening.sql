-- Sigurnosno učvršćivanje (2026-10-28).
--
-- 1. Javne uloge (anon/authenticated) dobijaju samo ono što aplikaciji treba:
--    sadržaj Kur'ana samo za čitanje, blog čitanje + upis (RLS i dalje pušta
--    samo admina), contact_messages nimalo direktno. RLS je već bio uključen;
--    ovo je druga linija odbrane (npr. TRUNCATE ne prolazi kroz RLS).
-- 2. Kontakt poruke idu isključivo kroz submit_contact_message(): provjera
--    dužine i formata + ograničenje broja poruka (zaštita od spama).
-- 3. Funkcijama fiksiran search_path (Supabase linter 0011).
--
-- Skripta se može bezbjedno pokrenuti više puta.

-- 1. Prava nad tabelama
revoke all on table
  public.surahs, public.ayahs, public.words, public.word_segments,
  public.bosnian_tokens, public.token_segment_links
from anon, authenticated;
grant select on table
  public.surahs, public.ayahs, public.words, public.word_segments,
  public.bosnian_tokens, public.token_segment_links
to anon, authenticated;

revoke all on table public.blog_posts from anon, authenticated;
grant select on table public.blog_posts to anon;
grant select, insert, update, delete on table public.blog_posts to authenticated;

revoke all on table public.contact_messages from anon, authenticated;
drop policy if exists "contact_messages_public_insert" on public.contact_messages;

-- 2. Kontakt forma
alter table public.contact_messages
  drop constraint if exists contact_messages_name_len,
  drop constraint if exists contact_messages_email_fmt,
  drop constraint if exists contact_messages_message_len;
alter table public.contact_messages
  add constraint contact_messages_name_len check (char_length(name) between 1 and 100),
  add constraint contact_messages_email_fmt check (
    char_length(email) <= 254 and email ~ '^[^@[:space:]]+@[^@[:space:]]+[.][^@[:space:]]+$'
  ),
  add constraint contact_messages_message_len check (char_length(message) between 1 and 5000);

create index if not exists contact_messages_created_idx on public.contact_messages (created_at);
create index if not exists contact_messages_email_created_idx on public.contact_messages (lower(email), created_at);

create or replace function public.submit_contact_message(p_name text, p_email text, p_message text)
returns void
language plpgsql
security definer
set search_path = ''
as $$
declare
  v_name text := btrim(coalesce(p_name, ''));
  v_email text := lower(btrim(coalesce(p_email, '')));
  v_message text := btrim(coalesce(p_message, ''));
begin
  if v_name = '' or v_email = '' or v_message = '' then
    raise exception 'invalid_input' using errcode = '22023';
  end if;

  -- Najviše 5 poruka sa iste adrese na sat i 60 ukupno na sat.
  if (select count(*) from public.contact_messages
      where lower(email) = v_email and created_at > now() - interval '1 hour') >= 5
     or (select count(*) from public.contact_messages
         where created_at > now() - interval '1 hour') >= 60 then
    raise exception 'rate_limited' using errcode = 'P0429';
  end if;

  insert into public.contact_messages (name, email, message)
  values (v_name, v_email, v_message);
end;
$$;

revoke all on function public.submit_contact_message(text, text, text) from public;
grant execute on function public.submit_contact_message(text, text, text) to anon, authenticated;

-- 3. search_path
alter function public.is_blog_admin() set search_path = '';
alter function public.blog_set_updated_at() set search_path = '';
