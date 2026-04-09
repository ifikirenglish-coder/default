from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from typing import Optional
import uuid


class JourneyStage(Enum):
    NEW_LEAD        = "new_lead"         # Came in from Facebook ad
    CONTACTED       = "contacted"        # First CRM message sent
    QUALIFYING      = "qualifying"       # In conversation — gathering challenges/goals
    QUALIFIED       = "qualified"        # Profile complete, ready for trial offer
    TRIAL_INVITED   = "trial_invited"    # Invited to free trial class
    TRIAL_ATTENDED  = "trial_attended"   # Showed up to trial
    TRIAL_NO_SHOW   = "trial_no_show"    # Missed the trial
    BACKEND_INVITED = "backend_invited"  # Invited to join the main (backend) program
    ENROLLED        = "enrolled"         # Signed up for backend program
    DROPPED         = "dropped"          # Unresponsive or disqualified


class Urgency(Enum):
    LOW    = "low"
    MEDIUM = "medium"
    HIGH   = "high"


@dataclass
class Challenge:
    description: str
    urgency: Urgency = Urgency.MEDIUM


@dataclass
class Goal:
    description: str
    timeline: Optional[str] = None   # e.g. "3 months", "by end of year"
    priority: int = 1                # 1 = most important


@dataclass
class QualificationProfile:
    profession: Optional[str] = None
    industry: Optional[str] = None
    challenges: list = field(default_factory=list)   # list[Challenge]
    goals: list = field(default_factory=list)        # list[Goal]
    has_tried_before: Optional[bool] = None
    notes: str = ""


@dataclass
class Communication:
    id: str = field(default_factory=lambda: str(uuid.uuid4())[:8])
    timestamp: datetime = field(default_factory=datetime.now)
    direction: str = "outbound"      # "outbound" | "inbound"
    channel: str = "crm"             # "crm" | "facebook" | "email" | "phone"
    message: str = ""
    stage_at_time: Optional[object] = None  # JourneyStage


@dataclass
class Lead:
    id: str = field(default_factory=lambda: str(uuid.uuid4())[:8])
    name: str = ""
    phone: Optional[str] = None
    email: Optional[str] = None
    facebook_id: Optional[str] = None
    ad_campaign: Optional[str] = None
    created_at: datetime = field(default_factory=datetime.now)


@dataclass
class Customer:
    lead: Lead
    stage: JourneyStage = JourneyStage.NEW_LEAD
    profile: QualificationProfile = field(default_factory=QualificationProfile)
    communications: list = field(default_factory=list)   # list[Communication]
    stage_history: list = field(default_factory=list)    # list[tuple[JourneyStage, datetime]]

    # Key timestamps
    trial_invited_at: Optional[datetime] = None
    trial_attended_at: Optional[datetime] = None
    backend_invited_at: Optional[datetime] = None
    enrolled_at: Optional[datetime] = None

    def __post_init__(self):
        self.stage_history.append((self.stage, datetime.now()))
