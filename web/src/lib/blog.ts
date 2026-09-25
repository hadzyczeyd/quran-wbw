export interface BlogPost {
  id: string;
  slug: string;
  title: string;
  content: string;
  excerpt: string;
  published: boolean;
  created_at: string;
  updated_at: string;
}

export type BlogPostSummary = Pick<
  BlogPost,
  "id" | "slug" | "title" | "excerpt" | "published" | "created_at"
>;

// Nalog admina u Supabase Auth traži email; forma za prijavu prima korisničko
// ime ("ehaadmin") i dodaje ovu domenu. Isti email je i u
// supabase/migrations/20260925000000_blog.sql (is_blog_admin).
const ADMIN_EMAIL_DOMAIN = "kuran-rijecporijec.com";

export function usernameToEmail(input: string): string {
  const value = input.trim().toLowerCase();
  return value.includes("@") ? value : `${value}@${ADMIN_EMAIL_DOMAIN}`;
}

const MONTHS = [
  "januar",
  "februar",
  "mart",
  "april",
  "maj",
  "juni",
  "juli",
  "august",
  "septembar",
  "oktobar",
  "novembar",
  "decembar",
];

export function formatBlogDate(iso: string): string {
  const d = new Date(iso);
  return `${d.getDate()}. ${MONTHS[d.getMonth()]} ${d.getFullYear()}.`;
}

/** "Šta je tefsir?" -> "sta-je-tefsir" (bez dijakritika, za URL). */
export function slugify(title: string): string {
  const slug = title
    .toLowerCase()
    .replace(/đ/g, "dj")
    .normalize("NFD")
    .replace(/[̀-ͯ]/g, "")
    .replace(/[^a-z0-9]+/g, "-")
    .replace(/^-+|-+$/g, "")
    .slice(0, 80)
    .replace(/-+$/g, "");
  return slug || "clanak";
}

/** Prva slika iz HTML sadržaja — za pregled linka pri dijeljenju (og:image). */
export function firstImageUrl(html: string): string | null {
  const match = html.match(/<img[^>]+src="([^"]+)"/i);
  return match ? match[1] : null;
}
