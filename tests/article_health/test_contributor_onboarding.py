"""Contributor onboarding instructions must match executable project requirements."""

import json
import os
import subprocess
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[2]


def test_onboarding_node_requirement_matches_package_engine():
    package = json.loads((REPO_ROOT / "package.json").read_text(encoding="utf-8"))
    minimum = package["engines"]["node"].removeprefix(">=")
    bootstrap = (REPO_ROOT / "public" / "start.sh").read_text(encoding="utf-8")
    contributing = (REPO_ROOT / "CONTRIBUTING.md").read_text(encoding="utf-8")

    assert f'MIN_NODE_VERSION="{minimum}"' in bootstrap
    assert f"Node.js {minimum.removesuffix('.0')}+" in contributing


def test_article_template_passes_frontmatter_validator(tmp_path):
    contributing = (REPO_ROOT / "CONTRIBUTING.md").read_text(encoding="utf-8")
    template_section = contributing.split("### 文章結構範本", 1)[1]
    article_template = template_section.split("```markdown", 1)[1].split("```", 1)[0]

    article_path = tmp_path / "knowledge" / "Culture" / "contributor-template.md"
    article_path.parent.mkdir(parents=True)
    article_path.write_text(article_template.strip() + "\n", encoding="utf-8")

    env = os.environ.copy()
    env["TWMD_VALIDATE_FILES"] = "knowledge/Culture/contributor-template.md"
    result = subprocess.run(
        [
            "node",
            str(REPO_ROOT / "scripts" / "core" / "test-frontmatter.mjs"),
            "--strict",
        ],
        cwd=tmp_path,
        env=env,
        capture_output=True,
        text=True,
        check=False,
    )

    assert result.returncode == 0, result.stdout + result.stderr
