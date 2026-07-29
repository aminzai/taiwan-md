#!/usr/bin/env python3
"""Remove an AI-added Markdown fence only when it wraps an article's whole body.

Default mode is read-only.  ``--apply`` rewrites exact candidates and leaves
embedded code examples untouched.  This pairs with article-health's hard gate:
the gate prevents recurrence; this tool safely heals historical instances.
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path


REPO = Path(__file__).resolve().parents[3]
KNOWLEDGE = REPO / "knowledge"
WRAPPER = re.compile(
    r"\A(?P<prefix>---\n[\s\S]*?\n---\n)(?P<space>\s*)"
    r"```(?:markdown|md)\s*\n(?P<body>[\s\S]*?)\n```\s*\Z",
    re.IGNORECASE,
)


def candidates() -> list[tuple[Path, re.Match[str]]]:
    found = []
    for path in sorted(KNOWLEDGE.glob("*/*/*.md")):
        match = WRAPPER.fullmatch(path.read_text(encoding="utf-8"))
        if match:
            found.append((path, match))
    return found


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--apply", action="store_true")
    parser.add_argument("--limit", type=int, default=0)
    args = parser.parse_args()

    found = candidates()
    selected = found[: args.limit or None]
    print(f"whole-body Markdown wrappers: {len(found)}; selected: {len(selected)}")
    for path, match in selected:
        rel = path.relative_to(REPO)
        print(f"  {'fix' if args.apply else 'would fix'} {rel}")
        if args.apply:
            path.write_text(
                match.group("prefix") + "\n" + match.group("body").rstrip() + "\n",
                encoding="utf-8",
            )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
