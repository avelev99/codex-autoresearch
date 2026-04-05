# Core Loop

This is the shared loop protocol behind every autoresearch mode.

## Preconditions

Resolve the setup contract first:

- goal
- scope
- metric
- direction
- verify
- budget

Optional but useful:

- guard
- git policy
- artifact policy

If runtime, sample size, or evaluation window affects the metric, keep that budget stable enough that iterations remain comparable.

If the run is expected to span many iterations or outlive the current chat, create a durable run folder first. The recommended scaffold is `.autoresearch/<tag>/` with `contract.md`, `results.tsv`, `notes.md`, and `summary.md`. Use `scripts/init_run.py` when you want this structure deterministically.

If the repo is dirty, do not assume commit-based iteration is safe. Either work without git memory or ask the user how they want to handle local changes.

Treat the run contract as stable during a loop. If the contract changes materially, restate the baseline before continuing.

## Review

Before each iteration:

1. Read the current version of the in-scope files.
2. Read the latest verification output or experiment notes.
3. If git memory is enabled, inspect recent history and the last kept diff.
4. Decide what single change or hypothesis should be tested next.

## Change

Prefer one focused change per iteration:

- one optimization idea
- one bug hypothesis
- one fix step
- one audit vector
- one doc refresh pass on a coherent slice

If a task truly requires a coupled change, keep the coupling explicit and explain why it is a single experiment.

## Verify

Verification must be mechanical.

Good:

- benchmark value
- failing test count
- type error count
- lint error count
- coverage percentage
- exact output diff
- presence or absence of a security finding

Bad:

- "looks cleaner"
- "feels faster"
- "probably fixed"

Use the fastest trustworthy check. Prefer a short command over a slow full-suite gate when the shorter check still answers the experiment question.

## Decide

After verification:

- keep when the metric improved or the hypothesis was confirmed
- revert or discard when the metric worsened or the hypothesis was disproven
- rework only when the idea is still promising and the failure mode is clear
- stop and surface the blocker when verification is unreliable or the environment is broken

Simplicity rule:

- if two options perform the same, keep the simpler one
- if an improvement is tiny and the complexity cost is large, default to discard

## Stop Conditions

Default Codex stop conditions:

- requested iteration budget reached
- target metric achieved
- no trustworthy next experiment
- repeated flat results with no stronger hypothesis

Only run indefinitely when the user explicitly asked for unattended autonomy.

## Git Memory

Use git as memory only when it is safe and wanted.

When enabled:

1. commit the candidate
2. verify
3. keep the commit if it wins
4. revert the commit if it loses
5. read recent history before choosing the next step

When disabled:

- keep a short experiment log in the response or a local artifact
- do not fabricate commit-based memory

## Subagents

Use subagents only when explicitly authorized. Good delegation targets:

- upstream research
- repo audits
- disjoint file groups
- alternative design proposals

Do not require subagents for the core loop.
