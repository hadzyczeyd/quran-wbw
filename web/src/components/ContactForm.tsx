"use client";

import { useActionState } from "react";
import { submitContactMessage, type ContactFormState } from "@/app/contact/actions";

const initialState: ContactFormState = { status: "idle" };

export function ContactForm() {
  const [state, formAction, pending] = useActionState(submitContactMessage, initialState);

  return (
    <form action={formAction} className="contact-form">
      <label>
        Ime
        <input type="text" name="name" required maxLength={100} />
      </label>
      <label>
        Email
        <input type="email" name="email" required maxLength={200} />
      </label>
      {/* Mamac za botove: skriven od ljudi i čitača ekrana. */}
      <div className="contact-hp" aria-hidden="true">
        <label>
          Web stranica
          <input type="text" name="website" tabIndex={-1} autoComplete="off" />
        </label>
      </div>
      <label>
        Poruka
        <textarea name="message" required rows={5} maxLength={2000} />
      </label>

      {state.status !== "idle" && (
        <p className={`contact-status ${state.status}`} aria-live="polite">
          {state.message}
        </p>
      )}

      <button type="submit" className="contact-submit" disabled={pending}>
        {pending ? "Šaljem…" : "Pošalji"}
      </button>
    </form>
  );
}
