"""Contributor onboarding instructions must match executable project requirements."""

import json
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[2]


def test_onboarding_node_requirement_matches_package_engine():
    package = json.loads((REPO_ROOT / "package.json").read_text(encoding="utf-8"))
    minimum = package["engines"]["node"].removeprefix(">=")
    bootstrap = (REPO_ROOT / "public" / "start.sh").read_text(encoding="utf-8")
    contributing = (REPO_ROOT / "CONTRIBUTING.md").read_text(encoding="utf-8")

    assert f'MIN_NODE_VERSION="{minimum}"' in bootstrap
    assert f"Node.js {minimum.removesuffix('.0')}+" in contributing
