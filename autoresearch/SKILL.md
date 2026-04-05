---
name: autoresearch
description: Metric-driven autonomous iteration for Codex. Use when the user wants Codex to set up a constrained experiment loop, improve a measurable metric, run repeated debug or fix passes, perform a scoped security or quality audit, keep iterating on a bounded file set, or reason through a design decision using explicit verification and keep-or-revert mechanics.
---

# Autoresearch

Autoresearch is a Codex operating model derived from Karpathy's `program.md`, not a literal slash-command system.

The core idea is simple:

1. Constrain the scope hard enough that Codex can understand it.
2. Choose one mechanical success criterion.
3. Make one focused change.
4. Verify.
5. Keep or revert.
6. Repeat.

## When To Use This Skill

Use this skill when the user wants:

- metric-driven optimization
- a bounded experiment loop
- autonomous debugging with a hypothesis queue
- iterative fixing until errors drop to zero
- a scoped security or quality audit with evidence
- documentation updates validated against code
- structured comparison of competing technical options

Do not use this skill for casual one-shot edits that do not benefit from iteration, metrics, or explicit keep-or-revert decisions.

## Codex Translation

Translate the original Claude-oriented material into Codex-native behavior:

- Treat slash-command examples as aliases for plain-language requests.
- Ask direct plain-text questions only for the missing fields that materially affect execution.
- Inspect the repo for defaults before asking.
- Use subagents only when the user explicitly asked for subagents, delegation, or parallel agent work.
- Default to bounded loops unless the user explicitly asks for indefinite or overnight autonomy.

## Shared Invariants

- Humans set direction; Codex executes the experiment loop.
- Read all in-scope files before changing them.
- Keep the writable scope intentionally small, ideally one file or one subsystem when possible.
- Prefer one primary metric, not a scoreboard.
- Try to keep iteration cost roughly comparable across experiments when the task allows it.
- Use the fastest verification that is still trustworthy.
- Establish a baseline before the first change.
- Make one meaningful change per iteration when practical.
- Preserve user work. Never wipe unrelated changes.
- If git is part of the workflow, prefer reversible operations and use history as memory.
- If git is not part of the workflow, keep the experiment log in the response or a local artifact only when useful.

## Setup Contract

Before starting a loop, resolve these fields:

| Field | Meaning |
|---|---|
| `goal` | What should improve |
| `scope` | Files Codex may modify |
| `read_only` | Files or paths Codex may inspect but not change |
| `metric` | Single mechanical criterion |
| `direction` | Higher or lower is better |
| `verify` | Exact command or procedure that produces the metric |
| `guard` | Optional command that must keep passing |
| `budget` | Iteration count, time limit, or explicit stop rule |
| `git_policy` | Whether commit-based memory is required, optional, or disabled |
| `artifact_policy` | Whether to create logs, reports, or result files |

If any critical field is missing, inspect the repo first, then ask the smallest direct question set needed to unblock execution.

## Default Execution Modes

Pick the lightest mode that fits the task, then load the matching playbook from `references/playbooks.md`.

| Mode | Use For |
|---|---|
| `optimize` | Improve a measured metric |
| `debug` | Investigate failures with explicit hypotheses |
| `fix` | Reduce error count until a broken state is repaired |
| `audit` | Security or quality review with evidence-backed findings |
| `docs` | Generate or refresh documentation and verify it against code |
| `design` | Compare options and converge on a reasoned recommendation |

If the user simply says "run autoresearch," use `optimize` when a metric already exists, otherwise start with `plan` inside the optimize playbook.

## Loop Rules

Load `references/core-loop.md` for the detailed protocol. In every mode:

1. Review current state, recent changes, and prior experiment notes.
2. Choose the next best change or hypothesis.
3. Apply one focused step.
4. Verify mechanically.
5. Keep, revert, or rework.
6. Record the outcome if durable logging is enabled.
7. Continue until the budget or stop condition is reached.

Default stop behavior for Codex:

- Stop at the requested iteration count.
- Stop when the goal is achieved.
- Stop when verification is no longer trustworthy.
- Stop when returns clearly flatten and report why.

Do not assume an infinite unattended loop unless the user explicitly asked for that operating mode.

## Git Memory

If the repo is clean and the user wants commit-based iteration:

- commit each candidate before verification
- keep winning commits
- revert losing commits instead of destroying history
- read recent git history before the next iteration

If the working tree is already dirty or the user did not ask for commit-based iteration, do not force git commits. Use a lighter-weight experiment log instead.

## Subagents

If the user explicitly asks for subagents:

- delegate research, repo audit, or disjoint implementation tasks
- keep ownership boundaries clear
- integrate the final design in the main thread

If the user does not explicitly ask for subagents:

- simulate perspectives locally
- avoid hidden dependency on delegation

## Reference Files

Load only what is needed:

- `references/core-loop.md` for the shared loop protocol
- `references/playbooks.md` for mode-specific setup and execution
- `references/logging.md` for experiment logs and result artifacts

## Safety

- Reject subjective metrics for optimize or fix loops.
- Ask before destructive or production-facing actions.
- If the task turns into a review, prioritize findings and risks over narration.
- If verification cannot be made trustworthy, say so clearly and stop.
