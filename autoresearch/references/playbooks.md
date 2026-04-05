# Playbooks

Use the smallest playbook that fits the task.

## Optimize

Use when the user wants measurable improvement.

Setup:

- define the metric and direction
- define the writable scope
- define verify and optional guard
- set a bounded budget unless the user asked for unattended autonomy

Loop:

- baseline first
- test one improvement idea per iteration
- keep only verified wins

Examples:

- speed up a benchmark
- reduce bundle size
- improve test coverage
- reduce p95 latency

## Debug

Use when the user wants root-cause analysis.

Setup:

- symptom
- scope
- reproduction or failing output if available
- budget

Loop:

- collect evidence
- form one falsifiable hypothesis
- test it
- record confirmed bugs and disproven hypotheses separately

Output:

- confirmed findings with file and line references
- open questions
- optional handoff to `fix`

## Fix

Use when the code is already broken and the goal is to reduce failures.

Setup:

- target failure class: tests, types, lint, build, runtime
- scope
- verify command
- optional guard

Loop:

- detect the current error set
- pick the highest-value fix
- verify the error count decreases
- keep only fixes that move the broken state forward

## Audit

Use for security or quality review.

Setup:

- scope
- audit type: security, reliability, correctness, readiness
- budget
- whether fixes are in scope or the task is read-only

Loop:

- examine one attack surface or risk vector at a time
- require evidence for every finding
- prioritize externally reachable or high-impact issues first

Output:

- severity-ranked findings
- residual risks
- optional remediation queue

## Docs

Use to create or refresh project documentation.

Setup:

- mode: init, update, check, summarize
- scope
- target docs if specified

Loop:

- scout the codebase
- draft or update only the docs that match the repo
- validate doc claims against source files
- avoid generic boilerplate

## Design

Use for architecture or strategy questions without a single numeric metric.

Setup:

- decision statement
- constraints
- evaluation criteria
- whether the user wants local role simulation or explicit subagents

Loop:

- generate competing options
- critique each option against the criteria
- synthesize a recommendation
- preserve meaningful disagreement

Output:

- recommendation
- tradeoffs
- conditions that would change the decision

## Plan

When the user wants autoresearch but the setup contract is incomplete, run a short plan pass before any other playbook:

1. infer defaults from the repo
2. ask for the missing setup fields
3. dry-run verification if applicable
4. restate the working contract
5. begin the chosen playbook
