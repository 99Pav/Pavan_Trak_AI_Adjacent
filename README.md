# GitHub & Linear Agent Router

A simple, modular Python query router that understands a user's intent and
delegates the query to the appropriate mock agent — **GitHubAgent** or
**LinearAgent**. Unsupported queries return a fixed fallback message.

## Overview

The router inspects each user query for intent keywords and chooses one of the
two agents. Each agent then returns a **mocked** response (no real API calls are
made). This is an "AI-adjacent" exercise: the intelligence is implemented with
plain Python classes, conditional logic, and regular expressions instead of an
LLM or LangChain.

## Objectives

- Accept a user query from the command line.
- Detect the intent of the query (GitHub, Linear, or unsupported).
- Route the query to the correct agent.
- Return the agent's mocked response.
- Return `"I cannot answer this question."` for unsupported queries.
- Keep routing logic separate from agent logic.

## Technologies Used

- Python 3.6+ (standard library only: `logging`, `re`, `unittest`)
- No third-party packages, no API keys, no AI models required

## Project Structure

```
query-router/
├── agents/
│   ├── __init__.py
│   ├── github_agent.py     # GitHubAgent implementation
│   └── linear_agent.py     # LinearAgent implementation
├── router/
│   ├── __init__.py
│   └── query_router.py     # QueryRouter + routing rules
├── tests/
│   ├── __init__.py
│   └── test_router.py      # Unit tests
├── main.py                 # CLI entry point
├── README.md
├── requirements.txt
└── PROJECT_STEPS.md
```

## Agent Architecture

```
                 +----------------+
   user query -> |  QueryRouter   |
                 +--------+-------+
                          |  detect_intent()
          +---------------+----------------+
          |                                |
   GitHub intent                    Linear intent
          |                                |
  +-------v--------+              +--------v-------+
  |  GitHubAgent   |              |  LinearAgent   |
  +----------------+              +----------------+
   mocked PRs / repos /            mocked issues /
   commits / branches              tasks / assignments
```

- **GitHubAgent** — handles pull requests, repositories, commits and branches.
- **LinearAgent** — handles issues, tasks and assigned items.
- **QueryRouter** — owns all routing decisions. It never builds a response
  itself; it only selects an agent and forwards the query.

Both agents expose a single public method, `handle(query)`, and can be used
independently of the router.

## Routing Logic

The router lowercases the query and counts how many keywords from each agent's
keyword list appear as **whole words** (using `\b` word boundaries, so `pr`
does not match `project`).

| Intent      | Keywords (examples)                                                     |
| ----------- | ----------------------------------------------------------------------- |
| `github`    | github, git, pull request(s), pr, prs, repo(s), commit(s), branch(es)... |
| `linear`    | linear, issue(s), task(s), ticket(s), assigned, backlog, sprint...       |

Decision rules:

1. If the query is empty/whitespace → `"Please enter a valid, non-empty query."`
2. If neither keyword set matches → `"I cannot answer this question."`
3. Otherwise the intent with the higher keyword count wins (ties go to GitHub),
   and the query is forwarded to that agent.

## Setup

Prerequisites:

- Python 3.6 or newer (the spec targets 3.10+; this project is verified on
  3.6.3 and has no version-specific features that break on 3.10+).
- No third-party packages, API keys, or network access are required.

Steps (Windows PowerShell):

```powershell
# 1. Go to the project folder
 

 

# 2. Install dependencies (none required — stdlib only)
pip install -r requirements.txt
```

If `Activate.ps1` is blocked by execution policy, either run
`Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass` for the session,
or skip activation and call the interpreter directly (see below).

## How to Run

With the virtual environment activated:

```powershell
python main.py
```

 

## Example Inputs and Outputs

```
Ask a question> Show my open pull requests
Agent   : GitHubAgent
Response:
Here are your open pull requests:
  - #128  Add retry logic to the HTTP client   (open, by pavan)
  ...

Ask a question> What issues are assigned to me?
Agent   : LinearAgent
Response:
These Linear items are assigned to you:
  - ENG-101  Query router misroutes unsupported queries
  ...

Ask a question> What's the weather today?
Agent   : None
Response:
I cannot answer this question.
```

## Testing

The tests use the built-in `unittest` module, so no installation is needed.

```bash
# from the query-router folder
python -m unittest discover -s tests -v
```

The suite covers GitHub routing, Linear routing, unsupported queries, empty
input, the `pr` vs `project` word-boundary case, and direct (router-free) use
of each agent.

## Assumptions and Limitations

**Assumptions**

- The user runs the app from the `query-router` folder so that the `agents`
  and `router` packages are importable.
- Queries are written in English and use ordinary GitHub/Linear vocabulary.
- Mock data is static and hard-coded; it is meant to illustrate routing, not
  to reflect a real account.

**Limitations**

- All responses are **mocked**; no real GitHub or Linear API is contacted and
  no authentication is performed.
- Routing is **keyword-based**, so it can misclassify unusual phrasing. When a
  query contains keywords for both agents, the higher keyword count wins and
  ties default to GitHub.
- Matching is case-insensitive and uses whole words, so `pr` does not match
  `project`; however it is still a simple rule set, not real language
  understanding (no LLM/LangChain is used).
- There is no memory or conversation state between queries — each query is
  handled independently.
- Logging is written to `stderr` at INFO level; set the level to DEBUG to also
  see agent-level messages.
- Only a CLI is provided; there is no web or API interface.
- Not designed for concurrency or multi-user use.
