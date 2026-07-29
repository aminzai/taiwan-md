from pathlib import Path

from lib.article_health.checks import ai_residue
from lib.article_health.loader import load_target
from lib.article_health.types import Severity


def _write_article(tmp_path: Path, body: str) -> Path:
    path = tmp_path / "knowledge" / "Culture" / "sample.md"
    path.parent.mkdir(parents=True)
    path.write_text(
        "---\ntitle: sample\ndescription: sample\n---\n\n" + body,
        encoding="utf-8",
    )
    return path


def test_whole_body_markdown_fence_is_hard_failure(tmp_path):
    target = load_target(
        _write_article(tmp_path, "```markdown\n# 標題\n\n正文內容。\n```")
    )
    violations = list(ai_residue.check(target, {}))
    assert len(violations) == 1
    assert violations[0].severity == Severity.HARD
    assert "整篇正文" in violations[0].message


def test_embedded_markdown_example_remains_allowed(tmp_path):
    target = load_target(
        _write_article(
            tmp_path,
            "# 正文\n\n這是教學範例：\n\n```markdown\n## 範例\n```\n\n正文繼續。",
        )
    )
    assert list(ai_residue.check(target, {})) == []


def test_non_markdown_whole_body_code_sample_remains_allowed(tmp_path):
    target = load_target(_write_article(tmp_path, "```python\nprint('ok')\n```"))
    assert list(ai_residue.check(target, {})) == []
