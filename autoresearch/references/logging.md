# Logging

Persist results only when the user asked for artifacts or when a durable log materially helps the task.

If you need a ready-made scaffold, start from `assets/results.tsv`.

## Git Modes

Use the lightest git mode that still preserves learning:

- `none`: no commits, keep memory in the response or a local log
- `kept-only`: commit only winning states
- `per-experiment`: commit each experiment and revert losers

Only use `per-experiment` when the user explicitly wants durable experiment history or long unattended runs.

## Minimal Log Schema

Use a TSV when you need a durable experiment log:

```tsv
iteration	status	metric	description
0	baseline	12.4	initial state
1	keep	11.8	reduce query fan-out
2	discard	12.6	add cache in wrong layer
3	crash	0.0	invalid config variant
```

Recommended extra columns when useful:

- `commit`
- `guard`
- `artifact`
- `scope`
- `notes`

## Status Values

- `baseline`
- `keep`
- `discard`
- `crash`
- `blocked`

## Branching

If commit-based memory is enabled, prefer a dedicated branch with a short descriptive tag, for example:

```text
codex/autoresearch-2026-04-05-auth-latency
```

Do not create a branch just to satisfy the pattern. If the user wants the work on the current branch, respect that.

## What To Log

Log:

- the metric or outcome
- whether the step was kept
- the shortest description that will help the next iteration

Do not log:

- verbose chat transcripts
- every shell command unless the task is forensic
- large blobs of raw output that can be regenerated

## Artifact Policy

Prefer chat-only summaries for short tasks.

Create files only when:

- the loop has many iterations
- the user asked for a report
- future iterations benefit from durable memory
- another tool or workflow will consume the artifact

Do not commit logs by default unless the user asked for versioned experiment history.

If you want a ready-made folder structure instead of manual files, use `scripts/init_run.py` to scaffold `.autoresearch/<tag>/`.

Recommended run folder when artifacts are needed:

```text
.autoresearch/<tag>/
  contract.md
  results.tsv
  notes.md
  summary.md
```

Use `scripts/init_run.py --tag <name> --path <repo-root>` to scaffold this structure.
