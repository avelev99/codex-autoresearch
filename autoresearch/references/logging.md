# Logging

Persist results only when the user asked for artifacts or when a durable log materially helps the task.

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
