from models import Customer, JourneyStage
from journey import qualification_score, is_qualified, recommend_offer
from qualification import missing_profile_fields


def suggest_next_action(customer: Customer) -> str:
    """
    Based on the current journey stage and profile completeness,
    return the recommended next action for the sales/CRM team.
    """
    stage = customer.stage
    profile = customer.profile
    score = qualification_score(customer)

    if stage == JourneyStage.NEW_LEAD:
        return "Send initial contact message — introduce yourself and ask how you can help."

    elif stage == JourneyStage.CONTACTED:
        return "Start qualification — ask about their biggest challenge first."

    elif stage == JourneyStage.QUALIFYING:
        missing = missing_profile_fields(customer)
        if missing:
            return f"Still gathering info — ask about: {', '.join(missing)}."
        return "Profile complete — mark as QUALIFIED and prepare trial invite."

    elif stage == JourneyStage.QUALIFIED:
        if score < 50:
            return f"Score {score}/100 — nurture further before making an offer."
        if recommend_offer(customer) == "direct_intake":
            return f"Score {score}/100, high urgency — skip the trial and invite them to join intake directly."
        return f"Score {score}/100 — invite to the free trial class now."

    elif stage == JourneyStage.INTAKE_INVITED:
        return "Follow up to confirm they're joining. Address objections and get them enrolled directly."

    elif stage == JourneyStage.TRIAL_INVITED:
        return "Follow up to confirm attendance. Handle any objections or reschedule if needed."

    elif stage == JourneyStage.TRIAL_ATTENDED:
        return "Check in post-trial. Share what the backend program offers and invite them to join."

    elif stage == JourneyStage.TRIAL_NO_SHOW:
        return "Reach out — ask what came up and offer to reschedule the trial."

    elif stage == JourneyStage.BACKEND_INVITED:
        return "Follow up on their decision. Address objections and guide them to enroll."

    elif stage == JourneyStage.ENROLLED:
        return "Welcome them! Send onboarding details for the backend program."

    elif stage == JourneyStage.DROPPED:
        return "Re-engagement: check in after 2 weeks with a fresh message."

    return "No action required."


def print_summary(customer: Customer):
    """Print a clean CRM-style summary of a customer's journey and profile."""
    lead = customer.lead
    profile = customer.profile
    score = qualification_score(customer)

    print(f"\n{'='*55}")
    print(f"  {lead.name.upper()}")
    print(f"  Stage : {customer.stage.value.replace('_', ' ').title()}")
    print(f"  Score : {score}/100  |  Qualified: {'Yes' if is_qualified(customer) else 'No'}")
    print(f"  Source: Facebook — {lead.ad_campaign or 'Unknown campaign'}")
    print(f"{'─'*55}")

    if profile.profession:
        print(f"  Role      : {profile.profession}")

    if profile.challenges:
        print(f"  Challenges:")
        for c in profile.challenges:
            print(f"    • {c.description}")
            print(f"      Urgency: {c.urgency.value}")

    if profile.goals:
        print(f"  Goals:")
        for g in profile.goals:
            timeline = f"  (target: {g.timeline})" if g.timeline else ""
            print(f"    • {g.description}{timeline}")

    if profile.has_tried_before is not None:
        print(f"  Tried before : {'Yes' if profile.has_tried_before else 'No'}")

    if profile.notes.strip():
        print(f"  Notes : {profile.notes.strip()}")

    print(f"\n  Journey path:")
    for stage, ts in customer.stage_history:
        print(f"    {ts.strftime('%Y-%m-%d %H:%M')}  →  {stage.value}")

    print(f"\n  Messages logged : {len(customer.communications)}")
    print(f"\n  Next action: {suggest_next_action(customer)}")
    print(f"{'='*55}\n")
