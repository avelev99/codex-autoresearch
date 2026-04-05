# Autoresearch Modes

Autoresearch is a loop discipline, not a command zoo.

## Shared Rules

All modes follow the same core principles:

- Constrain scope hard.
- Use one mechanical metric.
- Establish a baseline before changing anything.
- Make one meaningful change at a time when practical.
- Verify mechanically.
- Keep, revert, or rework based on the metric.
- Log what happened so the next iteration has memory.

## Mode Guide

| Mode | Use When | Output |
|---|---|---|
| `plan` | The user has a goal but the metric, scope, or verify command is unclear | A ready-to-run run contract |
| `optimize` / `loop` | The user wants repeated improvement on a measurable metric | Baseline, iteration plan, and keep/revert loop |
| `debug` | Something is failing and the goal is root cause, not guesswork | Hypotheses, tests, evidence, and a lead queue |
| `fix` | The code is broken and the goal is to reduce the failure count | Ordered repairs until the failure set shrinks or clears |
| `security` | The user wants an audit, threat review, or vulnerability hunt | Evidence-backed findings and coverage gaps |
| `ship` | The user wants readiness checks, a dry run, or a release | Checklist, gate status, and ship/verify steps |
| `scenario` | The user wants edge cases, abuse cases, or test scenarios | Concrete situations and derived cases |
| `predict` | The user wants multiple expert angles before acting | Ranked findings, disagreements, and handoff notes |
| `learn` | The user wants docs generated, refreshed, or checked | Coverage map, doc updates, and validation results |
| `reason` | The user wants a technical decision refined through critique | Candidates, critiques, synthesis, and recommendation |

## What Matters Most By Mode

### `plan`

- Translate a vague objective into a measurable contract.
- Prefer a metric the repo can actually produce.
- If the verify command cannot be dry-run, the plan is not ready.

### `optimize` / `loop`

- Start with a baseline.
- Keep iteration cost comparable.
- Track whether the metric improved, regressed, or stayed flat.
- Stop when the goal is met, the budget is exhausted, or returns flatten.

### `debug`

- Start from the symptom and work backward.
- Test the most specific, falsifiable hypothesis first.
- Record disproven hypotheses so you do not repeat them.

### `fix`

- Prioritize blockers before cleanup.
- Use the narrowest change that reduces errors.
- Use a guard command when one fix could break another area.

### `security`

- Default to read-only.
- Map attack surface before hunting.
- Require file:line evidence for any finding.

### `ship`

- Check readiness before delivery.
- Dry-run if the action is irreversible.
- Verify the shipped result after the action.

### `scenario`

- Prefer concrete actors and actions over abstract possibilities.
- Expand across happy path, failure path, abuse, scale, timing, and recovery.

### `predict`

- Simulate distinct roles and preserve disagreement where it matters.
- Rank findings before chaining to a follow-on mode.

### `learn`

- Scan the repo first.
- Update only docs that the repo actually needs.
- Validate claims against code or config.

### `reason`

- Compare options, do not just summarize them.
- Make criteria explicit.
- Separate the strongest argument from the safest argument.

## What To Avoid

- Infinite loops by default.
- Subjective metrics.
- Large writable scopes when a smaller scope will do.
- Hidden dependencies on special UI tools or command frameworks.
- Carrying forward command-suite complexity that does not improve the loop.
