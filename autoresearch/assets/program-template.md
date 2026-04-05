# Autoresearch Run Contract

This file is the working contract for a single run.
Keep it short, explicit, and stable across iterations.

## Run Identity

- Run name:
- Date:
- Branch:
- Owner:
- Mode:

## Objective

- Goal:
- Why it matters:
- Success criterion:

## Scope

- Writable files:
- Read-only context:
- Out of scope:

## Metric

- Primary metric:
- Direction: `higher` or `lower`
- Baseline value:
- Target value:

## Verification

- Verify command:
- Guard command:
- Known failure modes:

## Loop Rules

- Read current state before each change.
- Make one focused change per iteration when practical.
- Verify after each change.
- Keep the change only if the metric improves and the guard passes.
- Revert or discard regressions.
- Stop when the goal is reached, the budget is spent, or the metric stops moving.

## Budget

- Iteration limit:
- Time limit:
- Human checkpoint:

## Logging

- Log format:
- Result file:
- Fields to record:
- Notes to keep:

## Handoff

- What the next iteration should know:
- What should not be repeated:
- Open risks:

## Run Notes

- Baseline:
- Iteration 1:
- Iteration 2:
- ...
