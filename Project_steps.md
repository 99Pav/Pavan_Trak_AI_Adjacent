# Python Project –  Track – Aiden / AI-Adjacent

## Project: GitHub & Linear Agent Router

### 1. Project Objective

Build a simple AI-adjacent query router using Python that understands user queries and routes them to the appropriate agent based on intent.

The project will contain two mock agents:

- GitHubAgent
- LinearAgent

If a query does not match either agent, the system should return:

"I cannot answer this question."

---

### 2. Understand the Project Requirements

Before starting development, understand what each component should do.

**GitHubAgent**

- Handle GitHub-related queries.
- Identify pull request requests.
- Handle repository-related questions.
- Return mocked GitHub responses.

**LinearAgent**

- Handle Linear-related queries.
- Identify issue-related questions.
- Handle assigned task requests.
- Return mocked Linear responses.

**Query Router**

- Accept user input.
- Understand the intent of the query.
- Identify the correct agent.
- Forward the query to that agent.
- Return the agent's response.

---

### 3. Development Environment Setup

Tasks:

- Install Python (3.10 or above).
- Install Visual Studio Code.
- Install the Python extension in VS Code.
- Create a dedicated project folder.
- Set up a Python virtual environment.
- Activate the virtual environment.
- Verify the Python installation.

Expected result: A working Python development environment.

---

### 4. Project Structure Design

Plan the following folder structure:

query-router/

- agents/
  - github_agent.py
  - linear_agent.py
- router/
  - query_router.py
- tests/
  - test_router.py
- main.py
- README.md
- requirements.txt
- PROJECT_STEPS.md

Purpose of each file:

- agents/: Contains individual agent implementations.
- github_agent.py: Handles GitHub queries.
- linear_agent.py: Handles Linear queries.
- router/: Contains query-routing logic.
- query_router.py: Decides which agent handles the query.
- tests/: Contains unit tests.
- main.py: Application entry point.
- README.md: Project documentation.
- requirements.txt: Project dependencies.

---

### 5. Design the Agent Architecture

Before implementation, understand the responsibilities of each component.

**Component 1: GitHubAgent**

- Receive GitHub-related queries.
- Process the request.
- Return a mock response.

**Component 2: LinearAgent**

- Receive Linear-related queries.
- Process the request.
- Return a mock response.

**Component 3: QueryRouter**

- Receive the user's question.
- Analyze keywords and intent.
- Select the appropriate agent.
- Forward the question.
- Return the response.

---

### 6. Define Query Routing Rules

Prepare example queries and expected routing decisions.

| User Query                      | Expected Agent |
| ------------------------------- | -------------- |
| Show my open pull requests      | GitHubAgent    |
| List my GitHub repositories     | GitHubAgent    |
| Show recent commits             | GitHubAgent    |
| What issues are assigned to me? | LinearAgent    |
| Show my pending tasks           | LinearAgent    |
| List my open Linear issues      | LinearAgent    |
| What's the weather today?       | Not Supported  |

Expected behavior:

- GitHub queries → GitHubAgent
- Linear queries → LinearAgent
- Unsupported queries → "I cannot answer this question."

---

### 7. Implement the Agents

Development tasks:

**GitHubAgent**

- Create the agent class.
- Define its query-handling responsibility.
- Add mock responses.
- Test GitHub-related requests.

**LinearAgent**

- Create the agent class.
- Define its query-handling responsibility.
- Add mock responses.
- Test Linear-related requests.

Keep the two agents independent of the routing logic.

---

### 8. Implement Query Routing

Development tasks:

- Create the QueryRouter component.
- Accept user questions.
- Identify the query intent.
- Route GitHub queries to GitHubAgent.
- Route Linear queries to LinearAgent.
- Handle unsupported queries.
- Return the appropriate response.

Important: Routing logic should remain separate from agent logic.

---

### 9. Build the Command-Line Interface (CLI)

Create a simple terminal-based interface.

Expected user experience:

1. Start the application.
2. Display a welcome message.
3. Ask the user to enter a query.
4. Process the query.
5. Display the selected agent and response.
6. Allow the user to enter another query.
7. Provide an exit option.

---

### 10. Testing

Test the following scenarios:

| Test Case                    | Expected Result                |
| ---------------------------- | ------------------------------ |
| GitHub pull request query    | GitHubAgent                    |
| GitHub repository query      | GitHubAgent                    |
| Linear assigned issues query | LinearAgent                    |
| Linear task query            | LinearAgent                    |
| Weather query                | Unsupported response           |
| Empty input                  | Appropriate validation message |

Optional:

- Write 1–2 unit tests.
- Test the router independently.
- Check that unsupported queries are handled correctly.

---

### 11. Add Logging

Add simple logs to understand routing decisions.

Examples:

- Received user query.
- Identified GitHub intent.
- Routing to GitHubAgent.
- Identified Linear intent.
- Routing to LinearAgent.
- Unsupported query detected.

---

### 12. Prepare README Documentation

The README should include:

1. Project title.
2. Project overview.
3. Project objectives.
4. Technologies used.
5. Project folder structure.
6. Agent architecture.
7. Routing logic explanation.
8. Installation instructions.
9. How to run the application.
10. Example inputs and outputs.
11. Testing instructions.
12. Assumptions and limitations.

---

### 13. Final Project Validation

Before submission, verify:

- [ ] Python environment works.
- [ ] Project folder structure is organized.
- [ ] GitHubAgent works independently.
- [ ] LinearAgent works independently.
- [ ] QueryRouter routes correctly.
- [ ] Unsupported queries return the expected message.
- [ ] CLI works correctly.
- [ ] Unit tests pass.
- [ ] Logging works.
- [ ] README is complete.
- [ ] No real API integration is required.

---

### 14. Final Deliverables

Submit the following:

1. Complete Python source code.
2. GitHubAgent implementation.
3. LinearAgent implementation.
4. QueryRouter implementation.
5. CLI application.
6. Unit tests.
7. README.md.
8. requirements.txt.

### Recommended Development Order

| Phase | Task                                    |
| ----- | --------------------------------------- |
| Day 1 | Environment setup and project structure |
| Day 2 | Understand and implement GitHubAgent    |
| Day 3 | Understand and implement LinearAgent    |
| Day 4 | Implement query-routing logic           |
| Day 5 | Build CLI and test scenarios            |
| Day 6 | Add logging and unit tests              |
| Day 7 | Complete README and final validation    |

**Final Goal:** Build a simple, modular Python query router that correctly identifies user intent and delegates queries to GitHubAgent or LinearAgent.
