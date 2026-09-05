"""Tests for explain_empty_selection() — the empty-selection CLI message.

2026-09-05 bug: `article-health.py` printed one hardcoded line —
"(no checks ran — Phase 1 has empty registry)" — for EVERY empty
`_select_checks()` result, whether the cause was a designed language-scope
exclusion (e.g. `seo-meta` APPLIES_TO=["zh-TW"] on an `en` file) or an
actual misconfiguration. That line is a 2026-05-04 SSOT Phase 1 leftover
from when the registry really was empty; with 25+ plugins live it now reads
as "the tool is broken" for the (very common, by-design) language-scope
case. See `explain_empty_selection()` in `lib/article_health/runner.py`.

These tests cover the three causes named in the bug report:
  (a) 語言範圍排除（設計如此）— APPLIES_TO / options.applies_to excludes
      this file's lang
  (b) check 被 config `enabled=false`
  (c) `--check=<name>` known to the registry but not listed in the active
      profile's `checks`

Unit-level tests (a)/(b)/(c) use synthetic plugins injected into the
registry (same pattern as test_runner.py) so they don't depend on which
real plugins happen to be registered. A subprocess-level integration test
also pins the exact real-world repro from the bug report (`seo-meta` on an
`en` file under `ci-deploy`) plus the still-untouched typo'd `--check` path,
so a regression on the literal reported command is caught even if the
synthetic-plugin unit tests keep passing.
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path
from typing import Any, Iterator

from lib.article_health import registry
from lib.article_health.config import CheckConfig, Config, ProfileConfig
from lib.article_health.loader import load_target
from lib.article_health.runner import explain_empty_selection
from lib.article_health.types import FileTarget, Severity, Violation

_REPO_ROOT = Path(__file__).resolve().parents[2]


def _make_target(tmp_path, lang: str = "zh-TW", content: str = "test\n") -> FileTarget:
    if lang == "zh-TW":
        f = tmp_path / "knowledge" / "Nature" / "x.md"
    else:
        f = tmp_path / "knowledge" / lang / "Nature" / "x.md"
    f.parent.mkdir(parents=True, exist_ok=True)
    f.write_text(content, encoding="utf-8")
    return load_target(f)


def _register_synthetic_plugin(
    check_name: str, applies_to: list[str] | None = None
):
    """Inject a fake plugin module into the registry for testing."""

    class FakeMod:
        CHECK_NAME = check_name
        DIMENSION = "test"
        DEFAULT_SEVERITY = Severity.WARN
        EDITORIAL_REF = "test"

    if applies_to is not None:
        FakeMod.APPLIES_TO = applies_to

    def check(target: FileTarget, config: dict[str, Any]) -> Iterator[Violation]:
        return iter(())

    FakeMod.check = staticmethod(check)

    registry._REGISTRY[check_name] = FakeMod()
    registry._DISCOVERED = True
    return FakeMod


# ── (a) 語言範圍排除（設計如此）───────────────────────────────────────────────


def test_lang_scope_exclusion_message_is_design_not_error(tmp_path):
    registry.reset_registry()
    _register_synthetic_plugin("zh-only", applies_to=["zh-TW"])
    target_en = _make_target(tmp_path, lang="en")
    cfg = Config()

    msg = explain_empty_selection(target_en, cfg, profile=None, check_name="zh-only")

    assert "語言範圍" in msg
    assert "設計如此" in msg
    assert "不是錯誤" in msg
    # Must NOT be mistaken for the "genuinely nothing runnable" bucket.
    assert "真的沒有 check 可跑" not in msg


def test_lang_scope_exclusion_names_the_actual_lang(tmp_path):
    registry.reset_registry()
    _register_synthetic_plugin("zh-only", applies_to=["zh-TW"])
    target_en = _make_target(tmp_path, lang="en")
    cfg = Config()

    msg = explain_empty_selection(target_en, cfg, profile=None, check_name="zh-only")

    assert "en" in msg
    assert "zh-only" in msg


# ── (b) check 被 config enabled=false ─────────────────────────────────────


def test_disabled_check_message_says_genuinely_nothing_ran(tmp_path):
    registry.reset_registry()
    _register_synthetic_plugin("toggle-me")
    target = _make_target(tmp_path)
    cfg = Config()
    cfg.checks["toggle-me"] = CheckConfig(enabled=False)

    msg = explain_empty_selection(target, cfg, profile=None, check_name="toggle-me")

    assert "disable" in msg or "停用" in msg
    assert "真的沒有 check 可跑" in msg
    # Must NOT be mislabeled as the designed lang-exclusion case.
    assert "語言範圍" not in msg


# ── (c) --check=<name> 已註冊但不在這個 profile 的 checks 清單裡 ──────────


def test_check_not_in_profile_scope_message(tmp_path):
    registry.reset_registry()
    _register_synthetic_plugin("test-a")
    _register_synthetic_plugin("test-b")
    target = _make_target(tmp_path)
    cfg = Config()
    profile = ProfileConfig(name="only-a", checks=["test-a"])

    msg = explain_empty_selection(
        target, cfg, profile=profile, check_name="test-b"
    )

    assert "test-b" in msg
    assert "only-a" in msg
    assert "真的沒有 check 可跑" in msg
    assert "profile" in msg
    assert "語言範圍" not in msg


def test_check_not_in_profile_scope_distinct_from_lang_exclusion(tmp_path):
    """(a) and (c) must not collapse into the same wording — a reader should
    be able to tell "this profile doesn't run that check" apart from "this
    check doesn't apply to this file's language" without cross-referencing
    config."""
    registry.reset_registry()
    _register_synthetic_plugin("test-a")
    _register_synthetic_plugin("zh-only", applies_to=["zh-TW"])
    target_en = _make_target(tmp_path, lang="en")
    cfg = Config()
    profile = ProfileConfig(name="only-a", checks=["test-a"])

    msg_scope = explain_empty_selection(
        target_en, cfg, profile=profile, check_name="zh-only"
    )
    msg_lang = explain_empty_selection(
        _make_target(tmp_path, lang="en", content="y\n"),
        cfg,
        profile=None,
        check_name="zh-only",
    )

    assert msg_scope != msg_lang
    assert "profile" in msg_scope and "語言範圍" not in msg_scope
    assert "語言範圍" in msg_lang and "設計如此" in msg_lang


# ── Integration: pin the literal repro commands from the bug report ──────


def _run_cli(*args: str) -> subprocess.CompletedProcess:
    return subprocess.run(
        [sys.executable, "scripts/tools/article-health.py", *args],
        cwd=str(_REPO_ROOT),
        capture_output=True,
        text=True,
        timeout=30,
    )


def test_cli_seo_meta_en_ci_deploy_reports_lang_exclusion():
    """The exact repro from the bug report: seo-meta's APPLIES_TO=["zh-TW"]
    excludes `en` files, and ci-deploy doesn't override that — this is
    designed behavior, not a broken tool."""
    target = "knowledge/en/Geography/44-south-village.md"
    if not (_REPO_ROOT / target).exists():
        import pytest

        pytest.skip(f"fixture article missing: {target}")

    proc = _run_cli(target, "--check=seo-meta", "--profile=ci-deploy")

    assert proc.returncode == 0
    assert "Phase 1 has empty registry" not in proc.stdout
    assert "語言範圍" in proc.stdout
    assert "設計如此" in proc.stdout
    assert "seo-meta" in proc.stdout


def test_cli_unknown_check_name_still_hard_errors():
    """--list-checks' sibling guard (main(), unrelated to
    explain_empty_selection) must be untouched: an unregistered --check
    name still exits 2 with the known-checks list, not a soft empty-report."""
    target = "knowledge/en/Geography/44-south-village.md"
    if not (_REPO_ROOT / target).exists():
        import pytest

        pytest.skip(f"fixture article missing: {target}")

    proc = _run_cli(target, "--check=not-a-check", "--profile=ci-deploy")

    assert proc.returncode == 2
    assert "未知的 check 名稱" in proc.stderr
    assert "Phase 1 has empty registry" not in proc.stdout
