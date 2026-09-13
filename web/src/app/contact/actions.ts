"use server";

import { supabase } from "@/lib/supabase";

export interface ContactFormState {
  status: "idle" | "success" | "error";
  message?: string;
}

export async function submitContactMessage(
  _prevState: ContactFormState,
  formData: FormData
): Promise<ContactFormState> {
  const name = String(formData.get("name") ?? "").trim();
  const email = String(formData.get("email") ?? "").trim();
  const message = String(formData.get("message") ?? "").trim();

  if (!name || !email || !message) {
    return { status: "error", message: "Sva polja su obavezna." };
  }
  if (!email.includes("@")) {
    return { status: "error", message: "Unesi ispravnu email adresu." };
  }

  const { error } = await supabase.from("contact_messages").insert({ name, email, message });

  if (error) {
    return { status: "error", message: "Nešto je pošlo po zlu, pokušaj ponovo." };
  }

  return { status: "success", message: "Hvala! Poruka je poslana." };
}
