from datetime import datetime
from models import Customer, JourneyStage, Urgency


# Which stage transitions are allowed
VALID_TRANSITIONS = {
    JourneyStage.NEW_LEAD:        [JourneyStage.CONTACTED,       JourneyStage.DROPPED],
    JourneyStage.CONTACTED:       [JourneyStage.QUALIFYING,      JourneyStage.DROPPED],
    JourneyStage.QUALIFYING:      [JourneyStage.QUALIFIED,       JourneyStage.DROPPED],
    JourneyStage.QUALIFIED:       [JourneyStage.TRIAL_INVITED,   JourneyStage.INTAKE_INVITED, JourneyStage.DROPPED],
    JourneyStage.TRIAL_INVITED:   [JourneyStage.TRIAL_ATTENDED,  JourneyStage.TRIAL_NO_SHOW, JourneyStage.DROPPED],
    JourneyStage.TRIAL_ATTENDED:  [JourneyStage.BACKEND_INVITED, JourneyStage.DROPPED],
    JourneyStage.TRIAL_NO_SHOW:   [JourneyStage.TRIAL_INVITED,   JourneyStage.DROPPED],  # can re-invite
    JourneyStage.BACKEND_INVITED: [JourneyStage.ENROLLED,        JourneyStage.DROPPED],
    JourneyStage.INTAKE_INVITED:  [JourneyStage.ENROLLED,        JourneyStage.DROPPED],  # skips the trial entirely
    JourneyStage.ENROLLED:        [],
    JourneyStage.DROPPED:         [JourneyStage.CONTACTED],  # re-engagement possible
}

# Qualified leads at or above this score, with at least one high-urgency
# challenge, are strong enough to skip the trial and be pitched straight
# into the backend program.
DIRECT_INTAKE_SCORE_THRESHOLD = 70


def advance_stage(customer: Customer, to_stage: JourneyStage) -> bool:
    allowed = VALID_TRANSITIONS.get(customer.stage, [])
    if to_stage not in allowed:
        print(f"  [!] Cannot move from {customer.stage.value} → {to_stage.value}")
        return False
    customer.stage = to_stage
    customer.stage_history.append((to_stage, datetime.now()))
    return True


def is_qualified(customer: Customer) -> bool:
    """Minimum bar: at least one challenge and one goal captured."""
    p = customer.profile
    return len(p.challenges) > 0 and len(p.goals) > 0


def qualification_score(customer: Customer) -> int:
    """
    0–100 score based on profile completeness and signal strength.
    Higher score = warmer lead, more likely to convert.
    """
    score = 0
    p = customer.profile

    if p.challenges:
        score += 20
        if any(c.urgency == Urgency.HIGH for c in p.challenges):
            score += 20   # High urgency = strong buying signal

    if p.goals:
        score += 20
        if any(g.timeline for g in p.goals):
            score += 10   # Has a deadline = more motivated

    if p.profession:
        score += 15       # We know who they are

    if p.has_tried_before:
        score += 15       # Actively seeking solutions = higher intent

    return min(score, 100)


def recommend_offer(customer: Customer) -> str:
    """
    Decide how to make the offer to a qualified lead:
      - "direct_intake": skip the trial and invite them straight into the
        backend program — reserved for hot leads (high score + high urgency).
      - "trial": route them through the free trial class first.
    """
    score = qualification_score(customer)
    high_urgency = any(c.urgency == Urgency.HIGH for c in customer.profile.challenges)

    if score >= DIRECT_INTAKE_SCORE_THRESHOLD and high_urgency:
        return "direct_intake"
    return "trial"
