from datetime import datetime
from models import Customer, Challenge, Goal, Urgency, Communication


# Ordered qualification questions.
# Each maps to a profile field via its "key".
QUESTIONS = [
    {
        "key": "profession",
        "question": "What do you do for work, or what's your current role?",
        "maps_to": "profession",
    },
    {
        "key": "challenge",
        "question": "What's the biggest challenge you're facing right now that made you reach out?",
        "maps_to": "challenge",
    },
    {
        "key": "challenge_urgency",
        "question": "How urgent is this for you — is this something you need to solve right away, or more of a longer-term thing?",
        "maps_to": "urgency",
    },
    {
        "key": "goal",
        "question": "What does success look like for you? What do you want to achieve?",
        "maps_to": "goal",
    },
    {
        "key": "goal_timeline",
        "question": "Do you have a timeline in mind — when do you want to see results?",
        "maps_to": "goal_timeline",
    },
    {
        "key": "tried_before",
        "question": "Have you tried anything before to solve this? What happened?",
        "maps_to": "tried_before",
    },
]

_URGENCY_HIGH_KEYWORDS  = ["right away", "urgent", "asap", "immediately", "now", "critical"]
_URGENCY_LOW_KEYWORDS   = ["eventually", "someday", "no rush", "long term", "not urgent"]
_TRIED_YES_KEYWORDS     = ["yes", "tried", "used", "attempted", "before", "previously"]
_TRIED_NO_KEYWORDS      = ["no", "never", "first time", "haven't", "not yet"]


def record_answer(customer: Customer, key: str, answer: str):
    """Map a qualification answer onto the customer's profile."""
    p = customer.profile
    lower = answer.lower()

    if key == "profession":
        p.profession = answer

    elif key == "challenge":
        p.challenges.append(Challenge(description=answer))

    elif key == "challenge_urgency":
        if p.challenges:
            if any(kw in lower for kw in _URGENCY_HIGH_KEYWORDS):
                urgency = Urgency.HIGH
            elif any(kw in lower for kw in _URGENCY_LOW_KEYWORDS):
                urgency = Urgency.LOW
            else:
                urgency = Urgency.MEDIUM
            p.challenges[-1].urgency = urgency

    elif key == "goal":
        p.goals.append(Goal(description=answer))

    elif key == "goal_timeline":
        if p.goals:
            p.goals[-1].timeline = answer

    elif key == "tried_before":
        if any(kw in lower for kw in _TRIED_YES_KEYWORDS):
            p.has_tried_before = True
        elif any(kw in lower for kw in _TRIED_NO_KEYWORDS):
            p.has_tried_before = False
        if answer.strip():
            p.notes += f"\nPrevious attempts: {answer}"


def log_message(customer: Customer, direction: str, message: str, channel: str = "crm"):
    """Append a communication record to the customer's history."""
    comm = Communication(
        direction=direction,
        channel=channel,
        message=message,
        stage_at_time=customer.stage,
        timestamp=datetime.now(),
    )
    customer.communications.append(comm)
    return comm


def missing_profile_fields(customer: Customer) -> list:
    """Return a list of profile fields still not captured."""
    p = customer.profile
    missing = []
    if not p.challenges:
        missing.append("main challenge")
    if not p.goals:
        missing.append("goal")
    if not p.profession:
        missing.append("profession / role")
    return missing
