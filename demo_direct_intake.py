"""
Direct-Intake Funnel Demo
=========================
Simulates a hot lead who qualifies with high urgency and a strong score,
so instead of being routed through the free trial class, they're offered
a direct invite to join the backend program right away.

Run:  python demo_direct_intake.py
"""
from datetime import datetime
from models import Lead, Customer, JourneyStage
from journey import advance_stage, is_qualified, qualification_score, recommend_offer
from qualification import QUESTIONS, record_answer, log_message
from crm import print_summary, suggest_next_action


def section(title: str):
    print(f"\n[{title}]")


def run():
    # ── STEP 1: New lead arrives from Facebook ────────────────────────────────
    section("STEP 1 — New lead from Facebook ad")

    lead = Lead(
        name="Marcus Tan",
        phone="+60129876543",
        facebook_id="fb_marcus_002",
        ad_campaign="Weight Loss Challenge — Jan 2026",
    )
    customer = Customer(lead=lead)
    log_message(customer, "inbound", "Clicked Facebook ad and submitted lead form.", channel="facebook")

    print(f"  Lead created : {lead.name}")
    print(f"  Campaign     : {lead.ad_campaign}")
    print(f"  Next action  : {suggest_next_action(customer)}")


    # ── STEP 2: First contact via CRM ─────────────────────────────────────────
    section("STEP 2 — Initial outreach")

    advance_stage(customer, JourneyStage.CONTACTED)
    log_message(customer, "outbound",
        "Hi Marcus! I saw you were interested in our program. "
        "I'd love to learn more about what you're looking for. Do you have a few minutes?")
    log_message(customer, "inbound", "Yes, let's talk — I need help now.")

    print(f"  Next action  : {suggest_next_action(customer)}")


    # ── STEP 3: Qualification conversation ────────────────────────────────────
    section("STEP 3 — Qualification conversation")

    advance_stage(customer, JourneyStage.QUALIFYING)

    # A high-urgency, high-intent conversation — the signals that qualify
    # this lead for the direct-intake offer instead of the trial funnel.
    conversation = [
        ("profession",        "I'm a small business owner, on my feet all day."),
        ("challenge",         "My doctor flagged my blood pressure and told me I need to "
                              "lose weight now or go on medication."),
        ("challenge_urgency", "Very urgent — I need to start immediately, this can't wait."),
        ("goal",              "I want to lose 20kg and get my blood pressure under control."),
        ("goal_timeline",     "I need to show real progress within 6 weeks for my next checkup."),
        ("tried_before",      "Yes, I've tried a few things before but never stuck with it."),
    ]

    for key, answer in conversation:
        question_text = next(q["question"] for q in QUESTIONS if q["key"] == key)
        log_message(customer, "outbound", question_text)
        log_message(customer, "inbound", answer)
        record_answer(customer, key, answer)
        print(f"  Q: {question_text}")
        print(f"  A: {answer}\n")

    print(f"  Qualified    : {is_qualified(customer)}")
    print(f"  Score        : {qualification_score(customer)}/100")


    # ── STEP 4: Mark as qualified ─────────────────────────────────────────────
    section("STEP 4 — Profile complete → Qualified")

    advance_stage(customer, JourneyStage.QUALIFIED)
    offer = recommend_offer(customer)
    print(f"  Recommended offer : {offer}")
    print(f"  Next action        : {suggest_next_action(customer)}")


    # ── STEP 5: Invite straight to intake (skip the trial) ────────────────────
    section("STEP 5 — Direct intake invite")

    advance_stage(customer, JourneyStage.INTAKE_INVITED)
    customer.backend_invited_at = datetime.now()
    log_message(customer, "outbound",
        "Marcus, given what your doctor told you, I don't want you to wait for a trial class. "
        "Let's get you started in the full program right away — we'll build your plan around "
        "getting your blood pressure down fast. Ready to join now?")
    log_message(customer, "inbound", "Yes, let's do it. Sign me up.")

    print(f"  Next action  : {suggest_next_action(customer)}")


    # ── STEP 6: Enrolled ──────────────────────────────────────────────────────
    section("STEP 6 — Enrolled!")

    advance_stage(customer, JourneyStage.ENROLLED)
    customer.enrolled_at = datetime.now()
    log_message(customer, "outbound",
        "Welcome to the program, Marcus! Here's everything you need to get started...")

    print(f"  Next action  : {suggest_next_action(customer)}")


    # ── Final CRM summary ─────────────────────────────────────────────────────
    print_summary(customer)


if __name__ == "__main__":
    run()
