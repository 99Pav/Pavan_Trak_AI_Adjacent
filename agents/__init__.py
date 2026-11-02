"""Mock agents used by the query router.

Each agent is responsible only for producing a response to a query it
understands. Agents know nothing about routing; the QueryRouter decides
which agent (if any) should handle a given query.
"""

from agents.github_agent import GitHubAgent
from agents.linear_agent import LinearAgent

__all__ = ["GitHubAgent", "LinearAgent"]
