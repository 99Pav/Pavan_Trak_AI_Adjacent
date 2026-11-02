"""Unit tests for the query router and the mock agents.

Run with:  python -m unittest discover -s tests -v
"""

import os
import sys
import unittest

# Make the project root importable when tests are run from the tests folder.
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from agents.github_agent import GitHubAgent
from agents.linear_agent import LinearAgent
from router.query_router import QueryRouter


class QueryRouterTestCase(unittest.TestCase):
    def setUp(self):
        self.router = QueryRouter()

    def test_routes_github_pull_request_query(self):
        result = self.router.route("Show my open pull requests")
        self.assertEqual(result.agent_name, "GitHubAgent")
        self.assertTrue(result.is_supported)

    def test_routes_github_repository_query(self):
        result = self.router.route("List my GitHub repositories")
        self.assertEqual(result.agent_name, "GitHubAgent")

    def test_routes_github_commit_query(self):
        result = self.router.route("Show recent commits")
        self.assertEqual(result.agent_name, "GitHubAgent")

    def test_routes_linear_assigned_issue_query(self):
        result = self.router.route("What issues are assigned to me?")
        self.assertEqual(result.agent_name, "LinearAgent")

    def test_routes_linear_task_query(self):
        result = self.router.route("Show my pending tasks")
        self.assertEqual(result.agent_name, "LinearAgent")

    def test_routes_linear_issue_query(self):
        result = self.router.route("List my open Linear issues")
        self.assertEqual(result.agent_name, "LinearAgent")

    def test_unsupported_query_returns_expected_message(self):
        result = self.router.route("What's the weather today?")
        self.assertFalse(result.is_supported)
        self.assertEqual(result.response, QueryRouter.UNSUPPORTED_RESPONSE)

    def test_empty_query_returns_validation_message(self):
        result = self.router.route("   ")
        self.assertFalse(result.is_supported)
        self.assertEqual(result.response, QueryRouter.EMPTY_RESPONSE)

    def test_pr_keyword_does_not_match_project(self):
        # "project" must not be treated as the GitHub keyword "pr".
        result = self.router.route("Tell me about my project")
        self.assertFalse(result.is_supported)

    def test_detect_intent(self):
        self.assertEqual(self.router.detect_intent("show commits"), "github")
        self.assertEqual(self.router.detect_intent("my pending tasks"), "linear")
        self.assertEqual(self.router.detect_intent("weather"), "unsupported")


class AgentsTestCase(unittest.TestCase):
    def test_github_agent_returns_text(self):
        agent = GitHubAgent()
        self.assertIn("pull request", agent.handle("show my pull requests").lower())

    def test_linear_agent_returns_text(self):
        agent = LinearAgent()
        self.assertIn("linear", agent.handle("open linear issues").lower())

    def test_agents_are_independent_of_router(self):
        # Agents can be used directly, without the router.
        self.assertEqual(GitHubAgent().name, "GitHubAgent")
        self.assertEqual(LinearAgent().name, "LinearAgent")


if __name__ == "__main__":
    unittest.main()
