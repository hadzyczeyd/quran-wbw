-- Statistika posjeta (samo uz pristanak posjetioca na stranici).
--
-- Šta se čuva: slučajni anonimni ID uređaja i sesije (UUID iz preglednika),
-- stranica, izvor dolaska (domen preporučioca / utm_source), država
-- (iz Vercel zaglavlja, IP adresa se NE čuva), tip uređaja, preglednik,
-- operativni sistem i aplikacija (in-app preglednik, npr. Facebook).
-- Upis ide isključivo kroz record_page_view(), čitanje samo za admina kroz
-- analytics_summary(). Podaci stariji od 13 mjeseci se brišu.
--
-- Skripta se može bezbjedno pokrenuti više puta.

create table if not exists public.page_views (
  id bigint generated always as identity primary key,
  created_at timestamptz not null default now(),
  visitor_id uuid not null,
  session_id uuid not null,
  path text not null,
  source text not null,
  referrer_host text,
  country text,
  device text,
  browser text,
  os text,
  in_app text,
  constraint page_views_path_len check (char_length(path) between 1 and 300),
  constraint page_views_source_len check (char_length(source) between 1 and 60),
  constraint page_views_ref_len check (referrer_host is null or char_length(referrer_host) <= 200),
  constraint page_views_country_fmt check (country is null or country ~ '^[A-Z]{2}$'),
  constraint page_views_device_val check (device is null or device in ('mobile', 'tablet', 'desktop')),
  constraint page_views_browser_len check (browser is null or char_length(browser) <= 40),
  constraint page_views_os_len check (os is null or char_length(os) <= 40),
  constraint page_views_in_app_len check (in_app is null or char_length(in_app) <= 40)
);

create index if not exists page_views_created_at_idx on public.page_views (created_at);
create index if not exists page_views_visitor_idx on public.page_views (visitor_id, created_at);

alter table public.page_views enable row level security;
revoke all on table public.page_views from anon, authenticated;

-- Upis jednog pregleda stranice (poziva ga /api/track na serveru).
create or replace function public.record_page_view(
  p_visitor_id uuid,
  p_session_id uuid,
  p_path text,
  p_source text,
  p_referrer_host text,
  p_country text,
  p_device text,
  p_browser text,
  p_os text,
  p_in_app text
)
returns void
language plpgsql
security definer
set search_path = ''
as $$
begin
  if p_visitor_id is null or p_session_id is null or coalesce(p_path, '') = '' then
    raise exception 'invalid_input' using errcode = '22023';
  end if;

  -- Zaštita od zloupotrebe: najviše 300 pregleda po uređaju na sat.
  if (select count(*) from public.page_views
      where visitor_id = p_visitor_id and created_at > now() - interval '1 hour') >= 300 then
    return;
  end if;

  insert into public.page_views
    (visitor_id, session_id, path, source, referrer_host, country, device, browser, os, in_app)
  values (
    p_visitor_id, p_session_id, left(p_path, 300), left(coalesce(nullif(p_source, ''), 'Direktno'), 60),
    nullif(left(p_referrer_host, 200), ''), nullif(upper(p_country), ''), nullif(p_device, ''),
    nullif(left(p_browser, 40), ''), nullif(left(p_os, 40), ''), nullif(left(p_in_app, 40), '')
  );
end;
$$;

revoke all on function public.record_page_view(uuid, uuid, text, text, text, text, text, text, text, text) from public;
grant execute on function public.record_page_view(uuid, uuid, text, text, text, text, text, text, text, text) to anon, authenticated;

-- Pregled statistike za admina (zadnjih p_days dana).
create or replace function public.analytics_summary(p_days int default 30)
returns jsonb
language plpgsql
security definer
set search_path = ''
as $$
declare
  v_days int := least(greatest(coalesce(p_days, 30), 1), 400);
  v_from timestamptz := date_trunc('day', now()) - make_interval(days => v_days - 1);
  v_result jsonb;
begin
  if not public.is_blog_admin() then
    raise exception 'forbidden' using errcode = '42501';
  end if;

  -- Rok čuvanja: 13 mjeseci.
  delete from public.page_views where created_at < now() - interval '395 days';

  with v as (
    select * from public.page_views where created_at >= v_from
  ),
  first_views as (
    select distinct on (session_id) * from v order by session_id, created_at
  )
  select jsonb_build_object(
    'from', v_from,
    'days', v_days,
    'totals', (select jsonb_build_object(
        'visitors', count(distinct visitor_id),
        'sessions', count(distinct session_id),
        'views', count(*)) from v),
    'today', (select jsonb_build_object(
        'visitors', count(distinct visitor_id),
        'views', count(*)) from v where created_at >= date_trunc('day', now())),
    'daily', (select coalesce(jsonb_agg(d order by d.day), '[]'::jsonb) from (
        select to_char(date_trunc('day', created_at), 'YYYY-MM-DD') as day,
               count(distinct visitor_id) as visitors, count(*) as views
        from v group by 1) d),
    'countries', (select coalesce(jsonb_agg(c order by c.visitors desc), '[]'::jsonb) from (
        select coalesce(country, '??') as key, count(distinct visitor_id) as visitors
        from v group by 1 order by 2 desc limit 30) c),
    'sources', (select coalesce(jsonb_agg(s order by s.sessions desc), '[]'::jsonb) from (
        select source as key, count(*) as sessions
        from first_views group by 1 order by 2 desc limit 30) s),
    'apps', (select coalesce(jsonb_agg(a order by a.visitors desc), '[]'::jsonb) from (
        select coalesce(in_app, 'Preglednik') as key, count(distinct visitor_id) as visitors
        from v group by 1 order by 2 desc limit 20) a),
    'devices', (select coalesce(jsonb_agg(x order by x.visitors desc), '[]'::jsonb) from (
        select coalesce(device, 'nepoznato') as key, count(distinct visitor_id) as visitors
        from v group by 1 order by 2 desc) x),
    'browsers', (select coalesce(jsonb_agg(x order by x.visitors desc), '[]'::jsonb) from (
        select coalesce(browser, 'nepoznato') as key, count(distinct visitor_id) as visitors
        from v group by 1 order by 2 desc limit 15) x),
    'os', (select coalesce(jsonb_agg(x order by x.visitors desc), '[]'::jsonb) from (
        select coalesce(os, 'nepoznato') as key, count(distinct visitor_id) as visitors
        from v group by 1 order by 2 desc limit 15) x),
    'pages', (select coalesce(jsonb_agg(p order by p.views desc), '[]'::jsonb) from (
        select path as key, count(*) as views, count(distinct visitor_id) as visitors
        from v group by 1 order by 2 desc limit 30) p)
  ) into v_result;

  return v_result;
end;
$$;

revoke all on function public.analytics_summary(int) from public;
grant execute on function public.analytics_summary(int) to authenticated;
