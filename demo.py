"""
Customer Journey Demo
=====================
Simulates a lead going from a Facebook ad all the way through to enrollment
in the backend program, showing how the profile gets built through conversation.

Run:  python demo.py
"""
from datetime import datetime
from models import Lead, Customer, JourneyStage
from journey import advance_stage, is_qualified, qualification_score
from qualification import QUESTIONS, record_answer, log_message
from crm import print_summary, suggest_next_action


def section(title: str):
    print(f"\n[{title}]")


def run():
    # ── STEP 1: New lead arrives from Facebook ────────────────────────────────
    section("STEP 1 — New lead from Facebook ad")

    lead = Lead(
        name="Sarah Johnson",
        phone="+60123456789",
        facebook_id="fb_sarah_001",
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
        "Hi Sarah! I saw you were interested in our program. "
        "I'd love to learn more about what you're looking for. Do you have a few minutes?")
    log_message(customer, "inbound", "Yes, I'm interested! What do you need to know?")

    print(f"  Next action  : {suggest_next_action(customer)}")


    # ── STEP 3: Qualification conversation ────────────────────────────────────
    section("STEP 3 — Qualification conversation")

    advance_stage(customer, JourneyStage.QUALIFYING)

    # Simulate the back-and-forth for each question
    conversation = [
        ("profession",        "I'm a nurse, working rotating shifts at a hospital."),
        ("challenge",         "I've been struggling with my weight for years. "
                              "Shift work makes it hard to eat consistently and I have no energy left to exercise."),
        ("challenge_urgency", "It's pretty urgent — my doctor actually told me I need to address it right away."),
        ("goal",              "I want to lose 15kg and have consistent energy throughout my shifts."),
        ("goal_timeline",     "I'd love to see real results within 3 months."),
        ("tried_before",      "Yes — I've tried a few diets before but nothing stuck because of my crazy schedule."),
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
    print(f"  Next action  : {suggest_next_action(customer)}")


    # ── STEP 5: Invite to trial class ─────────────────────────────────────────
    section("STEP 5 — Trial class invite")

    advance_stage(customer, JourneyStage.TRIAL_INVITED)
    customer.trial_invited_at = datetime.now()
    log_message(customer, "outbound",
        "Sarah, based on what you shared — especially around shift work and energy — "
        "I think our program would be a great fit. "
        "I'd love to invite you to a FREE trial class this Saturday at 10am. Can you make it?")
    log_message(customer, "inbound", "Yes! I'll be there for sure.")

    print(f"  Next action  : {suggest_next_action(customer)}")


    # ── STEP 6: Trial attended ────────────────────────────────────────────────
    section("STEP 6 — Sarah attends the trial class")

    advance_stage(customer, JourneyStage.TRIAL_ATTENDED)
    customer.trial_attended_at = datetime.now()
    log_message(customer, "outbound",
        "Sarah! So glad you joined us today. How did you feel about the session? "
        "I'd love to share more about how our full program can help you hit your 15kg goal.")
    log_message(customer, "inbound", "It was amazing! I really felt it. Tell me more about the full program.")

    print(f"  Next action  : {suggest_next_action(customer)}")


    # ── STEP 7: Invite to backend program ─────────────────────────────────────
    section("STEP 7 — Backend program invite")

    advance_stage(customer, JourneyStage.BACKEND_INVITED)
    customer.backend_invited_at = datetime.now()
    log_message(customer, "outbound",
        "Our program is built for busy people like you — flexible around shift schedules, "
        "sustainable nutrition, and consistent energy. We'll build a custom plan for you. "
        "Ready to get started?")
    log_message(customer, "inbound", "I'm in! How do I sign up?")

    print(f"  Next action  : {suggest_next_action(customer)}")


    # ── STEP 8: Enrolled ──────────────────────────────────────────────────────
    section("STEP 8 — Enrolled!")

    advance_stage(customer, JourneyStage.ENROLLED)
    customer.enrolled_at = datetime.now()
    log_message(customer, "outbound",
        "Welcome to the program, Sarah! Here's everything you need to get started...")

    print(f"  Next action  : {suggest_next_action(customer)}")


    # ── Final CRM summary ─────────────────────────────────────────────────────
    print_summary(customer)


if __name__ == "__main__":
    run()
