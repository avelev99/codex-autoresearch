# Codex Autoresearch

Codex-native port of [uditgoenka/autoresearch](https://github.com/uditgoenka/autoresearch).

This repo packages the `autoresearch` skill for Codex with the workflow docs translated from the original Claude-oriented command model into Codex-native behavior:

- direct plain-text clarification instead of `AskUserQuestion`
- slash-command examples treated as legacy aliases
- Codex-first workflow guidance for planning, looping, debugging, fixing, security, shipping, scenario analysis, prediction, documentation, and reasoning
- no hard dependency on special command registries or Claude-specific tooling

## Install

If you already have Codex's built-in skill installer available:

```powershell
py -3 "$env:CODEX_HOME\\skills\\.system\\skill-installer\\scripts\\install-skill-from-github.py" --repo avelev99/codex-autoresearch --path autoresearch
```

Or copy the folder manually into your Codex skills directory:

```powershell
Copy-Item -Recurse .\autoresearch "$env:CODEX_HOME\\skills\\autoresearch"
```

If `CODEX_HOME` is unset, the default location is usually `~/.codex/skills/autoresearch`.

## Contents

```text
autoresearch/
  SKILL.md
  references/
```

## Attribution

- Original project: [uditgoenka/autoresearch](https://github.com/uditgoenka/autoresearch)
- Original license: MIT, preserved in [LICENSE](LICENSE)

This repo is a platform adaptation for Codex, not the upstream project.
