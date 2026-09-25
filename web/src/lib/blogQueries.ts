import { cache } from "react";
import type { BlogPost, BlogPostSummary } from "./blog";
import { supabase } from "./supabase";

// Samo za server komponente (koristi React cache()).

export async function getPublishedPosts(): Promise<BlogPostSummary[]> {
  const { data, error } = await supabase
    .from("blog_posts")
    .select("id, slug, title, excerpt, published, created_at")
    .eq("published", true)
    .order("created_at", { ascending: false });
  if (error || !data) return [];
  return data;
}

// cache(): generateMetadata i sama stranica traže isti članak u istom
// zahtjevu — jedan upit umjesto dva.
export const getPublishedPost = cache(async (slug: string): Promise<BlogPost | null> => {
  const { data, error } = await supabase
    .from("blog_posts")
    .select("*")
    .eq("slug", slug)
    .eq("published", true)
    .maybeSingle();
  if (error || !data) return null;
  return data;
});
