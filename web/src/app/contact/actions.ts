"use server";

import { supabase } from "@/lib/supabase";

export interface ContactFormState {
  status: "idle" | "success" | "error";
  message?: string;
}

const EMAIL_RE = /^[^@\s]+@[^@\s]+\.[^@\s]+$/;

export async function submitContactMessage(
  _prevState: ContactFormState,
  formData: FormData
): Promise<ContactFormState> {
  const name = String(formData.get("name") ?? "").trim();
  const email = String(formData.get("email") ?? "").trim();
  const message = String(formData.get("message") ?? "").trim();

  // Skriveno polje koje čovjek ne vidi — popunjavaju ga samo botovi.
  if (String(formData.get("website") ?? "") !== "") {
    return { status: "success", message: "Hvala! Poruka je poslana." };
  }

  if (!name || !email || !message) {
    return { status: "error", message: "Sva polja su obavezna." };
  }
  if (!EMAIL_RE.test(email) || email.length > 254) {
    return { status: "error", message: "Unesi ispravnu email adresu." };
  }
  if (name.length > 100 || message.length > 5000) {
    return { status: "error", message: "Poruka je preduga." };
  }

  // Upis samo kroz funkciju u bazi (provjera + ograničenje broja poruka).
  const { error } = await supabase.rpc("submit_contact_message", {
    p_name: name,
    p_email: email,
    p_message: message,
  });

  if (error) {
    if (error.message.includes("rate_limited")) {
      return { status: "error", message: "Previše poruka u kratkom roku, pokušaj ponovo kasnije." };
    }
    return { status: "error", message: "Nešto je pošlo po zlu, pokušaj ponovo." };
  }

  return { status: "success", message: "Hvala! Poruka je poslana." };
}
