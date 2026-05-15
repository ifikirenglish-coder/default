# Perfect Webinar Funnel — Communication Plan

A comprehensive, channel-by-channel plan covering **Email**, **WhatsApp**, and **Landing Pages** mapped to the Perfect Webinar Funnel (Monday → Sunday).

---

## 1. Timeline Overview

| Day | Phase | Goal | Primary Channels |
|---|---|---|---|
| **Mon** | Registration + Indoctrination Day 1 | Capture lead, deliver Video 1 | Landing Page, Email, WhatsApp |
| **Tue** | Indoctrination Day 2 | Deliver Video 2, build belief | Email, WhatsApp |
| **Wed** | Indoctrination Day 3 | Deliver Video 3, pre-frame webinar | Email, WhatsApp |
| **Thu** | Live Webinar | Run live event, drive Buy | Landing Page (live room), Email, WhatsApp |
| **Fri** | Replay Day 1 | Drive replay views, first buy push | Landing Page (replay), Email, WhatsApp |
| **Sat** | Replay Day 2 / Repitch | Re-pitch, handle objections | Email, WhatsApp |
| **Sun** | Cart Close | Urgency & scarcity, close cart | Email, WhatsApp, Landing Page (countdown) |

Psychological arc across the week: **Emotion → Logic → Urgency & Scarcity**.

---

## 2. Landing Pages

### 2.1 Headline / Registration Page (Mon entry)
- **Purpose:** Convert cold traffic into registrants.
- **Above the fold:**
  - Curiosity-driven headline (the "big promise")
  - Sub-headline naming target audience + outcome
  - Date/time of live webinar (with timezone auto-detect)
  - CTA: "Save My Free Seat"
- **Below the fold:**
  - 3 bullet "secrets you'll learn"
  - Host bio + social proof (logos, testimonials)
  - FAQ + footer
- **Form fields:** Name, Email, WhatsApp number (with explicit opt-in checkbox), Timezone.
- **Tech:** Pixel + UTM capture, server-side event for conversion API.

### 2.2 Thank You Page
- **Purpose:** Confirm registration, set expectations, hand off to Video 1.
- **Sections:**
  - "You're in" confirmation + calendar add (Google/Apple/Outlook)
  - "Add the host on WhatsApp" deep link (`https://wa.me/<number>?text=...`)
  - Embedded Video 1 (Indoctrination) with autoplay-muted + CTA
  - "What to do before the webinar" — homework / pre-call asset

### 2.3 Indoctrination Pages (Mon/Tue/Wed)
- 3 unique URLs, one per video, gated only by tracking link from email/WhatsApp.
- Each page:
  - Embedded video
  - Single sub-CTA (book a call, take a quiz, join WhatsApp group)
  - Comment / reply prompt to drive engagement signal

### 2.4 Live Webinar Room (Thu)
- Hosted on Zoom / GoToWebinar / WebinarJam.
- Branded waiting room with countdown.
- Chat moderated for objection capture (feed objections into Sun email sequence).

### 2.5 Replay Page (Fri–Sat)
- Same video for 48 hours, then expires.
- Visible countdown to cart close.
- "Buy Now" button anchored sticky on scroll.
- Cart link opens checkout in new tab.

### 2.6 Sales / Repitch Page (Fri–Sun)
- Long-form sales letter mirroring webinar stack:
  - Hero offer + price
  - Stack visualization (each component + value)
  - Bonus stack
  - Guarantee
  - FAQ from chat objections
  - Countdown to cart close
- Exit-intent popup: "Watch the replay one more time" → replay page.

### 2.7 Checkout & Order Confirmation
- 1-step checkout, mobile-first.
- Order bump + 1-click upsell.
- Confirmation page: onboarding next-steps, WhatsApp community invite, calendar for kickoff.

---

## 3. Email Sequence

> Convention: **[Type] — Subject line — Send time (registrant local)**. CTA always points to a single, tracked URL.

### Monday — Registration & Video 1
1. **[Welcome] — "You're in. Here's what to do next." — T+5 min**
   - Confirms registration, links Thank You page, calendar add, WhatsApp opt-in nudge.
2. **[Indoctrination 1] — "The story that changed everything…" — 6:00 PM**
   - Frames the *origin story* (Emotion). CTA → Video 1.

### Tuesday — Video 2
3. **[Indoctrination 2] — "The #1 mistake most [audience] make" — 10:00 AM**
   - Vehicle / mechanism reveal (Logic begins). CTA → Video 2.
4. **[Soft objection] — "But what about [common objection]?" — 7:00 PM**
   - Pre-handles objection raised in past cohorts.

### Wednesday — Video 3 + Pre-frame
5. **[Indoctrination 3] — "What you'll walk away with tomorrow" — 9:00 AM**
   - Outcome + transformation. CTA → Video 3.
6. **[Pre-frame] — "Tomorrow. Bring a notebook." — 6:00 PM**
   - Sets webinar expectations: length, what to prepare, no-multitasking ask.

### Thursday — Live Webinar Day
7. **[Day-of] — "We go live in 6 hours" — Webinar − 6h**
8. **[1 hour reminder] — "Doors open in 60 minutes" — Webinar − 1h**
9. **[Going live] — "We're live — join now" — Webinar − 5 min** (plain text, urgent tone)
10. **[Post-webinar replay] — "Replay is up (48h only)" — Webinar + 2h**

### Friday — Replay + First Pitch
11. **[Replay push] — "Did you catch it?" — 9:00 AM** → Replay page.
12. **[Stack recap] — "Here's exactly what's inside [Offer]" — 4:00 PM** → Sales page.

### Saturday — Repitch + Objections
13. **[Case study] — "How [Customer] got [Result] in [Time]" — 10:00 AM**
14. **[Objection 1] — "Is this for me if [objection]?" — 3:00 PM**
15. **[Objection 2] — "What if it doesn't work?" — 7:00 PM** (guarantee focus)

### Sunday — Cart Close (matches the three icons on page 14)
16. **① [Objections] — "Buy Now / Watch Replay / Questions?" — 9:00 AM**
    - Three-button email, mirroring the framework's three options.
17. **② [Urgency & Scarcity] — "Closes tonight at midnight" — 3:00 PM**
    - Countdown timer (live image), bonuses expiring.
18. **③ [Cart Close] — "Final call — closing in 1 hour" — 11:00 PM**
    - Plain text, short, single link.

### Post-Sunday
- **Non-buyers:** Move into long-term nurture sequence; re-invite to next cohort.
- **Buyers:** Onboarding sequence (Day 0 / 1 / 3 / 7).

---

## 4. WhatsApp Sequence

> WhatsApp **complements** email — shorter, more conversational, higher open rate. Send only to registrants who explicitly opted in. Use a verified Business account with template messages for pre-event broadcasts and session messages once a conversation is open.

### Rules of engagement
- Cap broadcasts to **1–2 per day** to avoid spam reports.
- Always include opt-out: "Reply STOP to unsubscribe."
- Personalize with `{{first_name}}` and `{{webinar_time_local}}`.
- Use rich media: 15–30s host videos, single image cards, voice notes (Sat/Sun).

### Schedule

| # | Day / Time | Type | Message (template) |
|---|---|---|---|
| W1 | Mon, T+10 min | Template — Confirmation | "Hi {{first_name}}, you're confirmed for {{webinar_title}} on {{date}}. Save this number so you don't miss reminders. — {{host}}" |
| W2 | Mon, 6:05 PM | Template — Video 1 | "Video 1 is live. 12 min. Watch here 👉 {{link}}" |
| W3 | Tue, 10:05 AM | Template — Video 2 | "Today's drop: the #1 mistake most {{audience}} make. {{link}}" |
| W4 | Wed, 9:05 AM | Template — Video 3 | "Final video before tomorrow's live session: {{link}}" |
| W5 | Wed, 7:00 PM | Voice note | 30-sec personal voice note from host: what to prepare. |
| W6 | Thu, Webinar − 3h | Template — Reminder | "We go live in 3 hours. Add to calendar 👉 {{calendar_link}}" |
| W7 | Thu, Webinar − 15min | Template — Going live | "Doors open. Click to join 👉 {{room_link}}" |
| W8 | Thu, Webinar + 90 min | Template — Replay | "Missed it? Replay is up for 48h: {{replay_link}}" |
| W9 | Fri, 10:00 AM | Template — Stack | Image card of stack + "Full details: {{sales_link}}" |
| W10 | Sat, 11:00 AM | Voice note | Host answers top 2 objections from webinar chat. |
| W11 | Sat, 6:00 PM | Template — Case study | Short video testimonial + {{sales_link}} |
| W12 | Sun, 10:00 AM | Template — Cart open | "Cart closes tonight at midnight. Three options 👇 ① Buy ② Replay ③ Ask me anything" |
| W13 | Sun, 5:00 PM | Template — Urgency | Countdown image + "6 hours left. {{checkout_link}}" |
| W14 | Sun, 11:30 PM | Template — Final | "30 min to go. After tonight, the bonuses are gone. {{checkout_link}}" |

### 1:1 Conversational Layer
- Anyone who **replies** to a broadcast is moved into a **human / sales** queue.
- Sales rep uses a playbook keyed off `qualification_score` (from `qualification.py`) — high-urgency replies get a same-hour call invite; lower scores get nurture.
- Capture objections raised in chat → feed Sunday emails W12/W13 copy.

---

## 5. Channel Orchestration Rules

1. **Single source of truth:** CRM (extends current `models.Customer` + `JourneyStage`). Every send writes a touchpoint event.
2. **Suppression logic:**
   - If a contact **buys**, immediately remove from email + WhatsApp sales sequences and enrol in onboarding.
   - If a contact **opens replay** but doesn't buy, prioritize Saturday case study email + WhatsApp voice note.
   - If a contact **clicks checkout but doesn't pay**, trigger abandoned-cart sequence (E + WA, 1h, 6h, 24h).
3. **Frequency caps:** Max 3 email + 2 WhatsApp messages per day across all sequences.
4. **Quiet hours:** No sends 10 PM – 8 AM registrant local time, except Sunday cart-close final.
5. **Stage mapping (re-using your `JourneyStage` enum):**
   - `NEW_LEAD` → registration email + WA confirm
   - `CONTACTED` → indoctrination 1–3
   - `QUALIFYING` → pre-frame + reminders
   - `TRIAL_INVITED` → webinar reminders
   - `TRIAL_ATTENDED` / `TRIAL_NO_SHOW` → branch to replay vs. re-invite
   - `BACKEND_INVITED` → Fri–Sun pitch / repitch / close
   - `ENROLLED` → onboarding sequence
   - `DROPPED` → long-term nurture

---

## 6. Tracking & KPIs

| Metric | Target |
|---|---|
| Registration page conversion | ≥ 35% from warm, ≥ 15% from cold |
| WhatsApp opt-in rate at registration | ≥ 60% |
| Email open rate (pre-webinar) | ≥ 45% |
| WhatsApp read rate | ≥ 80% |
| Show-up rate (live) | 30–40% of registrants |
| Replay watch rate | 40–55% of no-shows |
| Webinar → buyer conversion | 5% (6-fig), 10% (7-fig), 15% (8-fig) — per page 14 |
| Cart abandon recovery | ≥ 15% of started checkouts |

UTM scheme: `utm_source={email|whatsapp|page}&utm_medium={broadcast|template}&utm_campaign={cohort_id}&utm_content={message_id}`.

---

## 7. Asset Checklist

**Landing Pages (7):** Registration · Thank You · Indoctrination ×3 · Replay · Sales/Repitch · Checkout · Confirmation.

**Emails (18):** see Section 3.

**WhatsApp templates (14):** see Section 4 — submit for Meta approval ≥ 5 business days before launch.

**Creative:** Host headshots, 3 indoctrination videos (8–15 min), 1 webinar deck, 1 stack image, 3 testimonial videos, 1 countdown gif, 1 voice note script.

**Compliance:** Privacy policy, GDPR/PDPA consent on form, explicit WhatsApp opt-in, STOP keyword handling, unsubscribe links in every email.

---

## 8. Launch Runbook (T-minus)

- **T-14 days:** Submit WhatsApp templates, finalize landing pages, run pixel tests.
- **T-10 days:** Begin paid traffic to Registration page.
- **T-7 days:** First registrants enter Monday cohort.
- **T-1 day:** Tech rehearsal of live room + backup link.
- **T-0 (Thu):** Live webinar.
- **T+3 days (Sun midnight):** Cart close, switch traffic to next cohort's Registration page.
