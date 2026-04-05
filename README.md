# Codex Autoresearch

Codex-native skill inspired directly by [karpathy/autoresearch](https://github.com/karpathy/autoresearch) and adapted from [uditgoenka/autoresearch](https://github.com/uditgoenka/autoresearch).

This repo is not a line-by-line port of the Claude plugin. It is a smaller Codex-first skill built around the parts that matter most in the original autoresearch idea:

- hard scope control
- one mechanical metric
- baseline first
- one focused experiment at a time
- explicit keep or revert decisions
- optional git memory
- bounded loops by default in Codex

## Why This Version Exists

Karpathy's original project is powerful because it is narrow: one file, one metric, one fixed experiment loop.

The Claude adaptation generalized that idea into a large command suite. For Codex, the ideal skill is leaner. It should teach an operating model, not ship a large slash-command framework with thousands of lines of workflow prose.

This repo keeps the core loop and a few compact playbooks:

- `optimize`
- `debug`
- `fix`
- `audit`
- `docs`
- `design`

## Repo Layout

```text
autoresearch/
  SKILL.md
  agents/openai.yaml
  references/
    core-loop.md
    logging.md
    playbooks.md
```

## Install

With Codex's built-in skill installer:

```powershell
py -3 "$env:CODEX_HOME\\skills\\.system\\skill-installer\\scripts\\install-skill-from-github.py" --repo avelev99/codex-autoresearch --path autoresearch
```

Manual install:

```powershell
Copy-Item -Recurse .\autoresearch "$env:CODEX_HOME\\skills\\autoresearch"
```

If `CODEX_HOME` is unset, the default location is usually `~/.codex/skills/autoresearch`.

## Attribution

- Original project and concept: [karpathy/autoresearch](https://github.com/karpathy/autoresearch)
- Claude-oriented adaptation: [uditgoenka/autoresearch](https://github.com/uditgoenka/autoresearch)
- Upstream license: MIT, preserved in [LICENSE](LICENSE)
