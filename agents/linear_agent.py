"""LinearAgent: produces mocked responses for Linear-related queries."""

import logging
import re

logger = logging.getLogger(__name__)


class LinearAgent:
    """A mock agent that answers Linear-related questions.

    The agent does not perform any real API calls. It inspects the query
    to pick a sensible mock response (issues, tasks, assignments, ...)
    and returns it as plain text.
    """

    name = "LinearAgent"

    def __init__(self):
        self._issues = [
            "ENG-101  Query router misroutes unsupported queries  (In Progress, High)",
            "ENG-104  Add logging to QueryRouter                  (Todo, Medium)",
            "ENG-109  Write unit tests for GitHubAgent            (Todo, Low)",
        ]
        self._tasks = [
            "[ ] Implement LinearAgent mock responses",
            "[x] Design the project folder structure",
            "[ ] Document the routing rules in README",
        ]
        self._assigned = [
            "ENG-101  Query router misroutes unsupported queries",
            "ENG-118  Review the CLI welcome message",
        ]

    def _has(self, query, *words):
        """Return True if any of the words appears as a whole word."""

        for word in words:
            if re.search(r"\b" + re.escape(word) + r"\b", query):
                return True
        return False

    def _issue_response(self):
        lines = ["Here are your open Linear issues:"]
        lines.extend("  - " + issue for issue in self._issues)
        return "\n".join(lines)

    def _task_response(self):
        lines = ["Here are your pending tasks:"]
        lines.extend("  - " + task for task in self._tasks)
        return "\n".join(lines)

    def _assigned_response(self):
        lines = ["These Linear items are assigned to you:"]
        lines.extend("  - " + item for item in self._assigned)
        return "\n".join(lines)

    def handle(self, query):
        """Return a mocked Linear response for the given query."""

        logger.debug("LinearAgent received query: %s", query)
        text = query.lower()

        if self._has(text, "task", "tasks"):
            response = self._task_response()
        elif self._has(text, "assigned", "assign", "assignee"):
            response = self._assigned_response()
        elif self._has(text, "issue", "issues", "ticket", "tickets"):
            response = self._issue_response()
        else:
            response = (
                "This is a mocked Linear response. "
                "You can ask about issues, tasks or assigned items."
            )

        logger.debug("LinearAgent produced a mock response")
        return response
