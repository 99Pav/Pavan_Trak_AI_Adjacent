"""GitHubAgent: produces mocked responses for GitHub-related queries."""

import logging
import re

logger = logging.getLogger(__name__)


class GitHubAgent:
    """A mock agent that answers GitHub-related questions.

    The agent does not perform any real API calls. It inspects the query
    to pick a sensible mock response (pull requests, repositories,
    commits, ...) and returns it as plain text.
    """

    name = "GitHubAgent"

    def __init__(self):
        self._pull_requests = [
            "#128  Add retry logic to the HTTP client   (open, by pavan)",
            "#131  Fix flaky test in test_router        (open, by aiden)",
            "#134  Bump requests from 2.31.0 to 2.32.3  (open, dependabot)",
        ]
        self._repositories = [
            "query-router      (private, main)",
            "py-utils          (public,  main)",
            "ml-experiments    (private, dev)",
        ]
        self._commits = [
            "a1b2c3d  Refactor QueryRouter to use keyword scoring   (2 hours ago)",
            "e4f5g6h  Add LinearAgent mock responses                (yesterday)",
            "i7j8k9l  Initial project structure                      (3 days ago)",
        ]

    def _has(self, query, *words):
        """Return True if any of the words appears as a whole word."""

        for word in words:
            if re.search(r"\b" + re.escape(word) + r"\b", query):
                return True
        return False

    def _pull_request_response(self):
        lines = ["Here are your open pull requests:"]
        lines.extend("  - " + pr for pr in self._pull_requests)
        return "\n".join(lines)

    def _repository_response(self):
        lines = ["Here are your GitHub repositories:"]
        lines.extend("  - " + repo for repo in self._repositories)
        return "\n".join(lines)

    def _commit_response(self):
        lines = ["Recent commits on the default branch:"]
        lines.extend("  - " + commit for commit in self._commits)
        return "\n".join(lines)

    def _branch_response(self):
        return (
            "Branches in query-router:\n"
            "  - main (default)\n"
            "  - develop\n"
            "  - feature/query-router"
        )

    def handle(self, query):
        """Return a mocked GitHub response for the given query."""

        logger.debug("GitHubAgent received query: %s", query)
        text = query.lower()

        if self._has(text, "pull request", "pull requests", "pr", "prs"):
            response = self._pull_request_response()
        elif self._has(text, "repo", "repos", "repository", "repositories"):
            response = self._repository_response()
        elif self._has(text, "commit", "commits"):
            response = self._commit_response()
        elif self._has(text, "branch", "branches"):
            response = self._branch_response()
        else:
            response = (
                "This is a mocked GitHub response. "
                "You can ask about pull requests, repositories, "
                "commits or branches."
            )

        logger.debug("GitHubAgent produced a mock response")
        return response
