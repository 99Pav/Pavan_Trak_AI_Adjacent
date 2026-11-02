"""Command-line interface for the GitHub & Linear query router.

Run with:  python main.py
"""

import logging
import sys

from router.query_router import QueryRouter

BANNER = """
==========================================================
  GitHub & Linear Agent Router
  Type a question and I will route it to the right agent.
  Commands: 'help' for examples, 'exit' (or 'quit') to stop.
==========================================================
"""

HELP_TEXT = """
Example queries:
  - Show my open pull requests          -> GitHubAgent
  - List my GitHub repositories         -> GitHubAgent
  - Show recent commits                 -> GitHubAgent
  - What issues are assigned to me?     -> LinearAgent
  - Show my pending tasks               -> LinearAgent
  - List my open Linear issues          -> LinearAgent
  - What's the weather today?           -> I cannot answer this question.
"""

EXIT_COMMANDS = {"exit", "quit", "q"}


def configure_logging(level=logging.INFO):
    """Send logs to stderr so they do not interfere with the CLI output."""

    logging.basicConfig(
        level=level,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
        stream=sys.stderr,
    )


def print_result(result):
    """Print the routed agent and its response."""

    print("")
    print("Agent   : {0}".format(result.agent_name))
    print("Response:")
    print(result.response)
    print("")


def run():
    """Start the interactive CLI loop."""

    configure_logging()
    router = QueryRouter()

    print(BANNER)
    while True:
        try:
            query = input("Ask a question> ")
        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye!")
            break

        if query.strip().lower() in EXIT_COMMANDS:
            print("Goodbye!")
            break

        if query.strip().lower() == "help":
            print(HELP_TEXT)
            continue

        result = router.route(query)
        print_result(result)


if __name__ == "__main__":
    run()
