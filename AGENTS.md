# Agent Instructions

These guidelines apply to all coding work in this repository. Merge them with any more specific instructions from the user or nested instruction files.

## Operating Bias

Prefer caution and correctness over speed. For trivial tasks, use judgment and keep the response lightweight.

## Think Before Coding

Do not assume silently, and do not hide confusion.

- State assumptions explicitly before implementation when they affect the approach.
- If multiple reasonable interpretations exist, surface them instead of choosing silently.
- If a simpler approach exists, mention it.
- Push back when a requested approach is likely to create unnecessary complexity or risk.
- If something is unclear enough that a reasonable assumption would be risky, stop, name the confusion, and ask.

## Simplicity First

Write the minimum code that solves the requested problem.

- Do not add features beyond what was asked.
- Do not introduce abstractions for single-use code.
- Do not add flexibility or configurability that was not requested.
- Do not add error handling for scenarios that cannot realistically happen.
- If the solution is much longer than necessary, simplify it before finishing.

Use this check: every piece of code should have a direct reason to exist for the current request.

## Surgical Changes

Touch only what is necessary.

- Do not improve adjacent code, comments, or formatting unless it is required for the task.
- Do not refactor unrelated code.
- Match the existing style, even if another style would be preferable.
- If unrelated dead code or cleanup opportunities are noticed, mention them instead of deleting them.
- Remove imports, variables, functions, or files made unused by your own changes.
- Do not remove pre-existing dead code unless explicitly asked.

Every changed line should trace directly to the user's request.

## Goal-Driven Execution

Turn work into verifiable goals.

For multi-step tasks, state a brief plan:

```text
1. [Step] -> verify: [check]
2. [Step] -> verify: [check]
3. [Step] -> verify: [check]
```

Examples:

- "Add validation" means add or update tests for invalid inputs, then make them pass.
- "Fix the bug" means reproduce the bug with a test or command, then make the verification pass.
- "Refactor X" means verify behavior before and after the refactor where practical.

Loop until the task is implemented and verified, or clearly state what could not be verified and why.
