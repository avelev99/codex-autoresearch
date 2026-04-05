#!/usr/bin/env python3
"""Initialize a reusable autoresearch run folder from bundled templates."""

from __future__ import annotations

import argparse
import shutil
from pathlib import Path


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Initialize an autoresearch run folder.")
    parser.add_argument("--tag", required=True, help="Run tag, for example auth-latency-pass-1")
    parser.add_argument(
        "--path",
        default=".",
        help="Project root where .autoresearch/<tag> should be created (default: current directory)",
    )
    return parser


def write_if_missing(path: Path, content: str) -> None:
    if not path.exists():
        path.write_text(content, encoding="utf-8")


def copy_if_missing(src: Path, dest: Path) -> None:
    if not dest.exists():
        shutil.copyfile(src, dest)


def main() -> int:
    args = build_parser().parse_args()
    root = Path(args.path).resolve()
    run_dir = root / ".autoresearch" / args.tag
    skill_root = Path(__file__).resolve().parent.parent
    assets_dir = skill_root / "assets"
    run_dir.mkdir(parents=True, exist_ok=True)

    copy_if_missing(assets_dir / "program-template.md", run_dir / "contract.md")
    copy_if_missing(assets_dir / "results.tsv", run_dir / "results.tsv")
    write_if_missing(run_dir / "notes.md", "# Notes\n\n")
    write_if_missing(run_dir / "summary.md", "# Summary\n\n")

    print(run_dir)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
