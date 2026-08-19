# autonomous-dev-team

This project is a dynamic multi-agent system where AI agents collaboratively build a Flask REST API — defining requirements, designing architecture, writing code, and iteratively testing and reviewing it through structured feedback loops and dynamic routing until the code passes all checks.

## What this skill does
* dev-orchestrator — acts as the entry point and coordinator of the full pipeline, owns the shared state object, manages workflows, and produces the final codebase or failure report.
* product-owner — turns the task description into a formal requirements doc, produces user stories, acceptance criteria, and edge cases to test.
* architect — reads the requirements doc and produces a structured architecture doc detailing file structure, endpoint definitions, and the data model.
* coder — reads the architecture doc and writes the full working Python Flask code; during loops, reads review comments and test results to fix only flagged issues, producing complete updated code.
* qa-tester — reads the coder's output, writes and mentally executes test cases, and produces a strict structured verdict on pass/fail status with identified issues.
* code-reviewer — reviews code for structure, readability, REST conventions, and error handling, reads the qa-tester's verdict, and produces a strict structured verdict on approve/reject status with comments.
