"""
Thinkific API client.

Authentication requires two values from your Thinkific admin panel
(Settings → API):
    THINKIFIC_API_KEY   – your API key
    THINKIFIC_SUBDOMAIN – your school subdomain (e.g. "myschool" for myschool.thinkific.com)

Pass them explicitly to ThinkificClient, or set the environment variables
and call ThinkificClient.from_env().
"""

import os
import urllib.request
import urllib.error
import json
from typing import Optional

from models import Customer, JourneyStage


_BASE_URL = "https://api.thinkific.com/api/public/v1"


class ThinkificError(Exception):
    """Raised when the Thinkific API returns an error response."""


class ThinkificClient:
    def __init__(self, api_key: str, subdomain: str):
        self.api_key = api_key
        self.subdomain = subdomain

    @classmethod
    def from_env(cls) -> "ThinkificClient":
        api_key = os.environ.get("THINKIFIC_API_KEY", "")
        subdomain = os.environ.get("THINKIFIC_SUBDOMAIN", "")
        if not api_key or not subdomain:
            raise EnvironmentError(
                "Set THINKIFIC_API_KEY and THINKIFIC_SUBDOMAIN environment variables."
            )
        return cls(api_key, subdomain)

    # ------------------------------------------------------------------
    # Internal helpers
    # ------------------------------------------------------------------

    def _headers(self) -> dict:
        return {
            "X-Auth-API-Key": self.api_key,
            "X-Auth-Subdomain": self.subdomain,
            "Content-Type": "application/json",
        }

    def _request(self, method: str, path: str, body: Optional[dict] = None) -> dict:
        url = f"{_BASE_URL}/{path.lstrip('/')}"
        data = json.dumps(body).encode() if body else None
        req = urllib.request.Request(url, data=data, headers=self._headers(), method=method)
        try:
            with urllib.request.urlopen(req) as resp:
                return json.loads(resp.read().decode())
        except urllib.error.HTTPError as exc:
            detail = exc.read().decode()
            raise ThinkificError(f"Thinkific {exc.code} on {method} {url}: {detail}") from exc

    def _get(self, path: str) -> dict:
        return self._request("GET", path)

    def _post(self, path: str, body: dict) -> dict:
        return self._request("POST", path, body)

    # ------------------------------------------------------------------
    # Users
    # ------------------------------------------------------------------

    def get_users(self, page: int = 1, limit: int = 25) -> dict:
        """Return a paginated list of school users."""
        return self._get(f"users?page={page}&limit={limit}")

    def get_user_by_email(self, email: str) -> Optional[dict]:
        """Look up a single user by email. Returns None if not found."""
        result = self._get(f"users?query[email]={urllib.request.quote(email)}")
        items = result.get("items", [])
        return items[0] if items else None

    def create_user(self, first_name: str, last_name: str, email: str) -> dict:
        """Create a new Thinkific user and return the created record."""
        return self._post("users", {
            "first_name": first_name,
            "last_name": last_name,
            "email": email,
        })

    def get_or_create_user(self, first_name: str, last_name: str, email: str) -> dict:
        """Return the existing user for *email*, or create one if absent."""
        user = self.get_user_by_email(email)
        if user:
            return user
        return self.create_user(first_name, last_name, email)

    # ------------------------------------------------------------------
    # Courses
    # ------------------------------------------------------------------

    def get_courses(self, page: int = 1, limit: int = 25) -> dict:
        """Return a paginated list of courses in the school."""
        return self._get(f"courses?page={page}&limit={limit}")

    def get_course(self, course_id: int) -> dict:
        """Return a single course by ID."""
        return self._get(f"courses/{course_id}")

    # ------------------------------------------------------------------
    # Enrollments
    # ------------------------------------------------------------------

    def get_enrollments(self, page: int = 1, limit: int = 25) -> dict:
        """Return a paginated list of all enrollments."""
        return self._get(f"enrollments?page={page}&limit={limit}")

    def enroll_user(self, user_id: int, course_id: int, *, activated: bool = True) -> dict:
        """Enroll *user_id* in *course_id*. Returns the created enrollment record."""
        return self._post("enrollments", {
            "user_id": user_id,
            "course_id": course_id,
            "activated": activated,
        })

    # ------------------------------------------------------------------
    # CRM bridge
    # ------------------------------------------------------------------

    def enroll_customer(self, customer: Customer, course_id: int) -> dict:
        """
        Enroll a CRM Customer in a Thinkific course.

        The customer must have an email address on their lead record.
        If no Thinkific account exists yet for that email, one is created
        automatically.

        Returns the Thinkific enrollment record.
        Raises ThinkificError on any API failure.
        """
        lead = customer.lead

        if not lead.email:
            raise ValueError(f"Customer {lead.name!r} has no email address — cannot enroll.")

        name_parts = lead.name.strip().split(" ", 1)
        first_name = name_parts[0]
        last_name = name_parts[1] if len(name_parts) > 1 else ""

        user = self.get_or_create_user(first_name, last_name, lead.email)
        enrollment = self.enroll_user(user["id"], course_id)

        if customer.stage != JourneyStage.ENROLLED:
            print(
                f"[thinkific] Note: customer stage is {customer.stage.value!r}, "
                "not 'enrolled' — enrolling anyway."
            )

        print(
            f"[thinkific] Enrolled {lead.email} (user_id={user['id']}) "
            f"in course {course_id}. Enrollment id: {enrollment.get('id')}."
        )
        return enrollment
