import { createClient } from "@supabase/supabase-js";

/**
 * Javni klijent — koristi "anon" ključ, ograničen RLS politikama (samo
 * čitanje sadržaja, samo upis na contact_messages). Bezbjedan za browser
 * i server komponente podjednako.
 */
export const supabase = createClient(
  process.env.NEXT_PUBLIC_SUPABASE_URL!,
  process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY!
);
