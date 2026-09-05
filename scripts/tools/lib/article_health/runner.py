"""article_health.runner — orchestrates checks against a target."""

from __future__ import annotations
from typing import Any

from .config import Config, ProfileConfig
from .registry import discover_checks, get_check
from .types import (
    CheckResult,
    FileTarget,
    HealthReport,
    Severity,
    Violation,
)


def resolve_applies_to(
    mod: Any,
    config: Config,
    profile: ProfileConfig | None,
) -> list[str]:
    """這支 check 要跑哪些語言 —— 語言範圍的唯一解析點。

    優先序：profile 的 options_override > checks.<name>.options > 模組常數 > ["*"]。
    沒有任何 config 時回傳模組自己宣告的 APPLIES_TO，所以預設行為不變。

    語言範圍原本寫死在模組常數裡，同一份清單又在各 check 的路徑排除函式裡抄一次
    （issue #1264 的「兩道尺」）。放到 config 之後，要放寬或依 profile 分流是設定
    改動而不是程式改動，也不必再動兩個地方。
    """
    override = _resolve_options(config, profile, mod.CHECK_NAME).get("applies_to")
    if override is not None:
        return list(override)
    return list(getattr(mod, "APPLIES_TO", ["*"]))


def _select_checks(
    profile: ProfileConfig | None,
    config: Config,
    target: FileTarget,
) -> list[Any]:
    """Resolve which check modules to run for this target + profile."""
    discover_checks()
    from .registry import _REGISTRY  # type: ignore[attr-defined]

    if profile is None or profile.checks is None:
        candidates = list(_REGISTRY.values())
    else:
        candidates = [_REGISTRY[c] for c in profile.checks if c in _REGISTRY]

    selected = []
    for mod in candidates:
        # Respect APPLIES_TO lang filter (config-overridable, single resolution point)
        applies = resolve_applies_to(mod, config, profile)
        if "*" not in applies and target.lang not in applies:
            continue
        # Respect global checks.X.enabled
        cfg = config.get_check_config(mod.CHECK_NAME)
        if not cfg.enabled:
            continue
        selected.append(mod)
    return selected


def explain_empty_selection(
    target: FileTarget,
    config: Config,
    profile: ProfileConfig | None,
    check_name: str | None = None,
) -> str:
    """Diagnose why a report came back with zero results, for CLI messaging.

    Read-only diagnostic — re-derives which cause applies without touching
    `_select_checks` / `resolve_applies_to`'s actual filtering logic (that
    behavior is OBSERVER-QUEUE #27 已拍板的設計, not up for change here).

    2026-09-05 bug: `article-health.py` printed the same hardcoded
    "(no checks ran — Phase 1 has empty registry)" line for every empty
    selection — a leftover from the 2026-05-04 SSOT Phase 1 era when the
    registry really was empty. Years later with 25+ plugins live, the line
    kept firing for `--check=seo-meta --profile=ci-deploy` on an `en` file
    (seo-meta's APPLIES_TO = ["zh-TW"], not overridden by ci-deploy) —
    indistinguishable from an actual misconfiguration. This distinguishes:
      (a) 語言範圍排除（設計如此，APPLIES_TO / options.applies_to 排除了
          這個檔案的語言）
      (b) check 被 config `enabled=false`（真的沒有 check 可跑）
      (c) `--check=<name>` 沒註冊，或已註冊但不在這個 profile 的
          checks 清單裡（真的沒有 check 可跑）
    """
    discover_checks()
    from .registry import _REGISTRY  # type: ignore[attr-defined]

    if not _REGISTRY:
        return (
            "⚠️  registry 是空的：一個 plugin 都沒被 discover 到——"
            "檢查 scripts/tools/lib/article_health/checks/ 底下的檔案是否存在、"
            "import 有沒有炸掉。這才是 2026-05-04 Phase 1 的原始情境，"
            "現在（25+ plugins 應該都在）不該再發生。"
        )

    profile_name = profile.name if profile is not None else None
    if profile is None or profile.checks is None:
        profile_check_names: set[str] = set(_REGISTRY.keys())
    else:
        profile_check_names = set(profile.checks)

    if check_name:
        if check_name not in _REGISTRY:
            return (
                f"⚠️  check「{check_name}」沒有註冊在 registry 裡"
                "（名字打錯，或這個 plugin 還沒進目前的 checkout——"
                "真的沒有 check 可跑）。"
            )
        if check_name not in profile_check_names:
            scope = f"profile「{profile_name}」" if profile_name else "目前指定的 profile"
            return (
                f"ℹ️  check「{check_name}」已註冊，但 {scope} 的 checks 清單沒有列它，"
                "所以這次沒有東西可跑（真的沒有 check 可跑：profile 沒列這個 check，"
                "不是這個檔案本身的問題）。"
            )
        mod = _REGISTRY[check_name]
        applies = resolve_applies_to(mod, config, profile)
        if "*" not in applies and target.lang not in applies:
            return (
                f"⊘ check「{check_name}」的語言範圍是 {applies}，"
                f"不含這個檔案的語言「{target.lang}」——這是設計如此的語言範圍排除，"
                "不是錯誤（語言範圍的唯一解析點是 resolve_applies_to；"
                "要放寬請改 config 的 applies_to，不是回報 bug）。"
            )
        cfg = config.get_check_config(check_name)
        if not cfg.enabled:
            return (
                f"⊘ check「{check_name}」目前被 config 設成 enabled=false，"
                "所以沒有跑（真的沒有 check 可跑：check 被 disable）。"
            )
        return (
            f"⚠️  check「{check_name}」照理該被選中卻沒有出現在結果裡——"
            "不屬於上述任何已知成因，這是異常，麻煩回報。"
        )

    # No --check given: the whole profile came back empty for this target.
    if profile is not None and profile.checks == []:
        return (
            f"ℹ️  profile「{profile_name}」的 checks 清單明列為空，"
            "所以這個檔案沒有任何 check 可跑（真的沒有 check 可跑：profile 空清單）。"
        )
    lang_excluded = []
    disabled = []
    for name in sorted(profile_check_names):
        mod = _REGISTRY.get(name)
        if mod is None:
            continue
        applies = resolve_applies_to(mod, config, profile)
        if "*" not in applies and target.lang not in applies:
            lang_excluded.append(name)
            continue
        cfg = config.get_check_config(name)
        if not cfg.enabled:
            disabled.append(name)
    parts = []
    if lang_excluded:
        parts.append(
            f"語言範圍排除，設計如此：{', '.join(lang_excluded)} 都不含"
            f"這個檔案的語言「{target.lang}」"
        )
    if disabled:
        parts.append(f"被 config disable，真的沒有 check 可跑：{', '.join(disabled)}")
    if not parts:
        return (
            "⚠️  沒有找到已知成因（可能是 profile.checks 列的名字都不在 registry 裡），"
            "麻煩回報。"
        )
    return "⊘ 這個檔案沒有任何 check 跑，成因：" + "；".join(parts) + "。"


def _resolve_severity(
    plugin_default: Severity,
    config: Config,
    profile: ProfileConfig | None,
    check_name: str,
) -> Severity:
    """Profile severity override > config severity override > plugin default."""
    if profile is not None and check_name in profile.severity_overrides:
        return profile.severity_overrides[check_name]
    cfg = config.get_check_config(check_name)
    if cfg.severity is not None:
        return cfg.severity
    return plugin_default


def _resolve_options(
    config: Config,
    profile: ProfileConfig | None,
    check_name: str,
) -> dict[str, Any]:
    base = dict(config.get_check_config(check_name).options)
    if profile and check_name in profile.options_overrides:
        base.update(profile.options_overrides[check_name])
    return base


def run_checks(
    target: FileTarget,
    config: Config,
    profile_name: str | None = None,
    check_name: str | None = None,
) -> HealthReport:
    """Run checks against a single target. Returns aggregate HealthReport.

    Args:
      target: prepared FileTarget
      config: parsed Config
      profile_name: name of profile to use (selects subset of checks).
                    If None, runs all enabled checks.
      check_name: if set, run ONLY this check (overrides profile.checks).
    """
    profile = config.get_profile(profile_name) if profile_name else None
    selected = _select_checks(profile, config, target)
    if check_name:
        selected = [m for m in selected if m.CHECK_NAME == check_name]

    report = HealthReport(target=target, results=[])
    for mod in selected:
        resolved_severity = _resolve_severity(
            mod.DEFAULT_SEVERITY, config, profile, mod.CHECK_NAME
        )
        options = _resolve_options(config, profile, mod.CHECK_NAME)

        violations: list[Violation] = []
        try:
            for v in mod.check(target, options):
                # Severity precedence (per design 2026-05-04 SSOT Phase 3):
                # 1. Plugin-yielded severity that DIFFERS from the plugin's
                #    DEFAULT_SEVERITY → authoritative. Lets a single check
                #    yield mixed HARD/WARN violations (e.g. frontmatter-title:
                #    halfwidth punct = HARD, vague adjective = WARN).
                # 2. If plugin yielded the default, profile/config can
                #    override it (resolved_severity).
                # 3. Plugin's DEFAULT_SEVERITY → fallback (already in v).
                if v.severity == mod.DEFAULT_SEVERITY:
                    v.severity = resolved_severity
                violations.append(v)
        except Exception as e:
            violations.append(
                Violation(
                    check=mod.CHECK_NAME,
                    severity=Severity.WARN,
                    message=f"check execution error: {e}",
                )
            )

        result = CheckResult(
            check=mod.CHECK_NAME,
            passed=all(v.severity != Severity.HARD for v in violations),
            violations=violations,
        )
        report.results.append(result)

    return report
