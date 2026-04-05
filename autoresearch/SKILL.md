---
name: autoresearch
description: Autonomous goal-directed iteration for metric-driven improvement, debugging, fixing failing tests or builds, security auditing, shipping readiness, scenario exploration, multi-perspective code analysis, codebase documentation, and design-decision reasoning. Use when the user asks to run autoresearch, keep iterating until done, improve a measurable metric, hunt bugs, fix errors, audit for vulnerabilities, generate edge cases, analyze code from multiple expert angles, document a codebase, or reason through a technical decision.
---

# Autoresearch for Codex

Use this skill as an operating mode inside Codex, not as a literal slash-command plugin.

## Translation Layer

The bundled source material came from a Claude-style command package. Translate it before acting:

- Treat `/autoresearch` and `/autoresearch:*` as mode names or natural-language requests, not literal commands.
- Treat `AskUserQuestion` as asking the user directly in concise plain text after inspecting the repo for smart defaults.
- Treat mentions of `Claude Code`, `claude -p`, plugin installation, or `.claude/` paths as legacy source wording. Prefer Codex-native behavior and the current workspace.
- Treat chained slash-command flows as sequential modes in the same conversation.
- Do not depend on hidden UI question tools, batched forms, or command registries.
- Do not use subagents unless the user explicitly asks for subagents, delegation, or parallel agent work. If the user has not granted that, simulate multiple perspectives locally in a structured single-agent analysis.

## Shared Operating Rules

- Read the relevant files before proposing or making changes.
- Prefer mechanical metrics, reproducible checks, and explicit baselines.
- When iterating, change one meaningful idea at a time when practical so causality stays clear.
- Keep iteration notes concise. Persist logs or output directories only if the user asked for artifacts or the task materially benefits from durable logs.
- Do not auto-commit every experiment. Use commit-based iteration only when the user asked for it or when it is clearly part of the requested workflow.
- If critical context is missing, inspect the repo first, then ask the minimum number of direct questions needed to unblock the next step.
- If the user asks for autonomy, continue through implementation and verification; do not stop at a plan unless the missing context is genuinely blocking.

## Mode Selection

Map the user request to one of these modes:

| Mode | Use For | Reference |
|---|---|---|
| `plan` | Define goal, scope, metric, direction, and verify command before an optimization loop | `references/plan-workflow.md` |
| `loop` | Improve a measurable metric iteratively | `references/autonomous-loop-protocol.md` |
| `debug` | Investigate bugs or failures with hypotheses and evidence | `references/debug-workflow.md` |
| `fix` | Reduce error count until tests, types, lint, or build pass | `references/fix-workflow.md` |
| `security` | Perform a threat-focused audit and report evidence-backed findings | `references/security-workflow.md` |
| `ship` | Check readiness, dry-run, and execute a release or delivery workflow | `references/ship-workflow.md` |
| `scenario` | Generate use cases, edge cases, failure modes, or test scenarios | `references/scenario-workflow.md` |
| `predict` | Analyze code from several expert perspectives before acting | `references/predict-workflow.md` |
| `learn` | Generate, update, or validate project documentation | `references/learn-workflow.md` |
| `reason` | Refine a subjective technical decision through structured critique | `references/reason-workflow.md` |

If the user says "run autoresearch" without enough detail:

- Use `plan` first when goal, metric, direction, or verify command are missing.
- Use `loop` directly only when goal, scope, metric, direction, and verify command are already clear.

## Context Gathering

Before running any mode:

1. Inspect the repo for likely defaults, constraints, and available verification commands.
2. Infer what can be answered locally without asking the user.
3. Ask direct plain-text questions only for the missing pieces that materially change execution.

Question style for Codex:

- Keep questions short.
- Ask for the smallest missing set, not a full questionnaire.
- Prefer one concise grouped message over a long wizard.
- If the user already implied a reasonable default, proceed with that default and state the assumption.

## Mode Guidance

### `plan`

Use when the task needs a reliable optimization setup.

- Produce a concrete configuration with goal, scope, metric, direction, verify command, and optional guard.
- Dry-run the verify command before accepting it.
- Reject subjective or non-repeatable metrics.
- If the user wants to proceed immediately, transition into `loop`.

### `loop`

Use when a metric and verification method already exist.

- Establish a baseline first.
- Iterate on focused changes.
- Re-run the metric after each change.
- Keep the best known state and discard regressions.
- If the user gave an iteration bound, stop after that bound and summarize results.
- If the user asked to "keep going" or "iterate until done," continue until the goal is reached, diminishing returns are clear, or the user interrupts.

### `debug`

Use for failures, regressions, unexplained behavior, or root-cause analysis.

- Start with symptoms, failing outputs, and reproduction evidence.
- Form explicit hypotheses and test them.
- Separate confirmed bugs from disproven hypotheses.
- Prefer evidence-backed findings with file and line references.
- Transition to `fix` if the user wants repairs after diagnosis.

### `fix`

Use when the code is already known to be broken and the goal is to reduce the failure count.

- Detect the failing domains first: tests, types, lint, build, runtime.
- Prioritize high-signal blockers before cosmetic issues.
- Verify that the error count decreases after each fix.
- Use a guard command when reducing one failure class could regress another.

### `security`

Use for code audits, attack-surface review, or vulnerability hunting.

- Default to read-only unless the user explicitly asks for remediation.
- Require code evidence for every finding.
- Prioritize externally reachable, high-impact paths first.
- Use STRIDE and OWASP as coverage frameworks, not as a substitute for evidence.

### `ship`

Use for release readiness, deployment, PR creation, or any final delivery workflow.

- Identify what is being shipped and the destination.
- Build a checklist from the actual repo state.
- Dry-run where possible before irreversible actions.
- Verify the shipped state after the action.

### `scenario`

Use for edge cases, use-case generation, or failure-mode exploration.

- Start from a concrete actor plus action if possible.
- Expand across success paths, errors, abuse paths, timing issues, data variation, integrations, and recovery.
- Prefer concrete situations over abstract advice.

### `predict`

Use for multi-perspective analysis before debugging, fixing, shipping, or auditing.

- Simulate distinct reviewer roles locally unless the user explicitly asked for subagents.
- Keep the perspectives independent in structure: for example architecture, security, performance, reliability, and devil's advocate.
- Synthesize shared findings and preserve meaningful disagreement.
- If the user requested a follow-on mode, hand off the ranked findings into that mode.

### `learn`

Use for documentation generation, refresh, or staleness checks.

- Scout the codebase first.
- Detect whether this is an initialization, update, check, or summary request.
- Generate only the documentation that matches the repo and the user's scope.
- Validate doc claims against the code before finalizing.
- Do the work locally unless the user explicitly asked for delegation.

### `reason`

Use for design decisions, architectural tradeoffs, argument refinement, or other subjective technical questions.

- Structure the reasoning as competing candidate views plus critique.
- Keep judge criteria explicit.
- Simulate multiple roles locally unless the user explicitly asked for subagents.
- Converge on a recommendation, then state the tradeoffs and open risks.

## Reference Usage

Load only the reference file for the active mode. When reading a reference:

- Apply the translation layer above before following any step.
- Ignore legacy assumptions about special question tools or slash-command execution.
- Keep the workflow substance; translate the interface mechanics.

Useful references:

- `references/core-principles.md` for the general autoresearch mindset.
- `references/results-logging.md` when a durable iteration log would materially help.
- `references/autonomous-loop-protocol.md` for detailed loop behavior in metric-driven work.

## Safety and Escalation

- If verification is impossible because the project lacks a runnable metric or the environment is broken, stop and explain the blocker clearly.
- If a workflow would require destructive or high-risk actions, ask the user before proceeding.
- If the task becomes primarily a review, prioritize findings, risks, regressions, and missing tests over summaries.
