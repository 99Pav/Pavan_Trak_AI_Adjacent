"""QueryRouter: inspects a user query and forwards it to the right agent.

The routing logic lives here and nowhere else. The router only knows about
keywords/intent; it delegates the actual answer to the agents. This keeps
routing concerns separate from agent concerns.
"""

import logging
import re

from agents.github_agent import GitHubAgent
from agents.linear_agent import LinearAgent

logger = logging.getLogger(__name__)


class RouteResult:
    """The outcome of routing a single query."""

    def __init__(self, agent_name, response, is_supported=True):
        self.agent_name = agent_name
        self.response = response
        self.is_supported = is_supported

    def __repr__(self):
        return "RouteResult(agent_name={0!r}, is_supported={1!r})".format(
            self.agent_name, self.is_supported
        )


class QueryRouter:
    """Routes a query to GitHubAgent, LinearAgent or an unsupported response."""

    UNSUPPORTED_RESPONSE = "I cannot answer this question."
    EMPTY_RESPONSE = "Please enter a valid, non-empty query."
    UNSUPPORTED_AGENT = "None"

    # Keywords that indicate a GitHub-related intent.
    GITHUB_KEYWORDS = [
        "github",
        "git",
        "pull request",
        "pull requests",
        "pr",
        "prs",
        "repo",
        "repos",
        "repository",
        "repositories",
        "commit",
        "commits",
        "branch",
        "branches",
        "merge",
        "fork",
        "clone",
        "gist",
    ]

    # Keywords that indicate a Linear-related intent.
    LINEAR_KEYWORDS = [
        "linear",
        "issue",
        "issues",
        "task",
        "tasks",
        "ticket",
        "tickets",
        "backlog",
        "sprint",
        "milestone",
        "cycle",
        "assigned",
        "assignee",
    ]

    def __init__(self, github_agent=None, linear_agent=None):
        self.github_agent = github_agent if github_agent is not None else GitHubAgent()
        self.linear_agent = linear_agent if linear_agent is not None else LinearAgent()

    @staticmethod
    def _count_matches(query, keywords):
        """Return the number of keywords that appear in the query.

        Matching uses whole-word boundaries so that e.g. "pr" does not
        match "project".
        """

        count = 0
        for keyword in keywords:
            if re.search(r"\b" + re.escape(keyword) + r"\b", query):
                count += 1
        return count

    def detect_intent(self, query):
        """Return the detected intent name: 'github', 'linear' or 'unsupported'."""

        text = query.lower().strip()
        github_score = self._count_matches(text, self.GITHUB_KEYWORDS)
        linear_score = self._count_matches(text, self.LINEAR_KEYWORDS)

        logger.debug(
            "Intent scores for %r -> github=%d, linear=%d",
            query, github_score, linear_score,
        )

        if github_score == 0 and linear_score == 0:
            return "unsupported"
        if github_score >= linear_score:
            return "github"
        return "linear"

    def route(self, query):
        """Route *query* and return a RouteResult."""

        logger.info("Received user query: %r", query)

        if query is None or not query.strip():
            logger.warning("Empty query received")
            return RouteResult(self.UNSUPPORTED_AGENT, self.EMPTY_RESPONSE, False)

        intent = self.detect_intent(query)

        if intent == "github":
            logger.info("Identified GitHub intent. Routing to GitHubAgent.")
            return RouteResult(self.github_agent.name, self.github_agent.handle(query), True)

        if intent == "linear":
            logger.info("Identified Linear intent. Routing to LinearAgent.")
            return RouteResult(self.linear_agent.name, self.linear_agent.handle(query), True)

        logger.info("Unsupported query detected.")
        return RouteResult(self.UNSUPPORTED_AGENT, self.UNSUPPORTED_RESPONSE, False)
