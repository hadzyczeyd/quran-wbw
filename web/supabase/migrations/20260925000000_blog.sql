-- Blog: članci i slike.
--
-- Čitanje: svi vide OBJAVLJENE članke. Pisanje (članci + slike): samo jedan
-- admin nalog, prepoznat po email-u u is_blog_admin(). Nalog se kreira ručno
-- u Supabase dashboardu (Authentication > Users) sa ISTIM email-om kao dolje —
-- šifra se nigdje ne upisuje u kod ni u ovu datoteku.
--
-- Skripta se može bezbjedno pokrenuti više puta.

create or replace function public.is_blog_admin()
returns boolean
language sql
stable
as $$
  select coalesce(auth.jwt() ->> 'email', '') = 'ehaadmin@kuran-rijecporijec.com'
$$;

create table if not exists public.blog_posts (
  id uuid primary key default gen_random_uuid(),
  slug text not null unique,
  title text not null,
  content text not null default '',
  excerpt text not null default '',
  published boolean not null default true,
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now()
);

create index if not exists blog_posts_published_created_idx
  on public.blog_posts (published, created_at desc);

create or replace function public.blog_set_updated_at()
returns trigger
language plpgsql
as $$
begin
  new.updated_at = now();
  return new;
end;
$$;

drop trigger if exists blog_posts_set_updated_at on public.blog_posts;
create trigger blog_posts_set_updated_at
  before update on public.blog_posts
  for each row execute function public.blog_set_updated_at();

alter table public.blog_posts enable row level security;

drop policy if exists "Objavljeni clanci su javni" on public.blog_posts;
create policy "Objavljeni clanci su javni" on public.blog_posts
  for select using (published or public.is_blog_admin());

drop policy if exists "Admin dodaje clanke" on public.blog_posts;
create policy "Admin dodaje clanke" on public.blog_posts
  for insert to authenticated with check (public.is_blog_admin());

drop policy if exists "Admin mijenja clanke" on public.blog_posts;
create policy "Admin mijenja clanke" on public.blog_posts
  for update to authenticated
  using (public.is_blog_admin()) with check (public.is_blog_admin());

drop policy if exists "Admin brise clanke" on public.blog_posts;
create policy "Admin brise clanke" on public.blog_posts
  for delete to authenticated using (public.is_blog_admin());

-- Slike u člancima: javni bucket (čitanje preko javnog URL-a), upis/brisanje
-- samo admin, do 5 MB, samo slike.
insert into storage.buckets (id, name, public, file_size_limit, allowed_mime_types)
values (
  'blog-images', 'blog-images', true, 5242880,
  array['image/jpeg', 'image/png', 'image/webp', 'image/gif']
)
on conflict (id) do update set
  public = excluded.public,
  file_size_limit = excluded.file_size_limit,
  allowed_mime_types = excluded.allowed_mime_types;

drop policy if exists "Admin otprema slike bloga" on storage.objects;
create policy "Admin otprema slike bloga" on storage.objects
  for insert to authenticated
  with check (bucket_id = 'blog-images' and public.is_blog_admin());

drop policy if exists "Admin brise slike bloga" on storage.objects;
create policy "Admin brise slike bloga" on storage.objects
  for delete to authenticated
  using (bucket_id = 'blog-images' and public.is_blog_admin());
