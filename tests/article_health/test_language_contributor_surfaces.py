"""Contributor-facing language lists must follow the enabled registry."""

import re
import subprocess
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[2]
REGISTRY = REPO_ROOT / "src" / "config" / "languages.mjs"


def _registry_codes() -> set[str]:
    text = REGISTRY.read_text(encoding="utf-8")
    entries = re.findall(r"\{\s*code:\s*'([\w-]+)'.*?enabled:\s*(true|false)", text, re.S)
    return {code for code, _ in entries if code != "zh-TW"}


def _enabled_translation_codes() -> set[str]:
    text = REGISTRY.read_text(encoding="utf-8")
    entries = re.findall(r"\{\s*code:\s*'([\w-]+)'.*?enabled:\s*(true|false)", text, re.S)
    return {code for code, enabled in entries if enabled == "true" and code != "zh-TW"}


def _qa_wired_translation_codes() -> set[str]:
    """語言碼要不要被譯文 QA 接線認得，看的是有沒有內容，不是 registry 的 enabled 旗標。

    一個語言以 scaffold（enabled: false）進註冊表之後，投稿的譯文會比上線決定早
    幾個月進 knowledge/<code>/，而那段空窗正是它最需要被守的時候——那批內容將來
    會一次全部進站，是唯一一批從未經過閘門的。判準與
    scripts/tools/check-language-registry-sync.sh 的「譯文 QA 接線必須覆蓋每個有
    內容的語言」同源，兩邊必須是同一把尺（LESSONS `scaffold-window-has-no-qa`）。
    """
    return _enabled_translation_codes() | {
        code for code in _registry_codes() if (REPO_ROOT / "knowledge" / code).is_dir()
    }


def test_translation_workflow_paths_cover_every_language_with_content():
    text = (REPO_ROOT / ".github" / "workflows" / "translation-check.yml").read_text(
        encoding="utf-8"
    )
    paths = set(re.findall(r"knowledge/([a-z]{2})/\*\*", text))
    assert paths == _qa_wired_translation_codes()


def test_translation_submission_options_match_enabled_registry():
    text = (REPO_ROOT / ".github" / "ISSUE_TEMPLATE" / "translation.yml").read_text(
        encoding="utf-8"
    )
    options = set(re.findall(r"^\s+- .*\(([a-z]{2})\)$", text, re.M))
    assert options == _enabled_translation_codes()


def test_i18n_page_triggers_match_enabled_registry():
    text = (REPO_ROOT / ".github" / "workflows" / "i18n-smoke-test.yml").read_text(
        encoding="utf-8"
    )
    paths = set(re.findall(r"src/pages/([a-z]{2})/\*\*", text))
    assert paths == _enabled_translation_codes()


def test_language_registry_mirrors_match_every_field():
    result = subprocess.run(
        ["node", "scripts/tools/compare-language-registries.mjs"],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
        check=False,
    )
    assert result.returncode == 0, result.stdout + result.stderr


def test_current_build_and_review_tools_use_the_language_registry():
    expected_imports = {
        "scripts/core/test-frontmatter.mjs": "ALL_LANGUAGE_CODES",
        "scripts/core/build-latest.mjs": "ENABLED_LANGUAGE_CODES",
        "scripts/core/generate-contributors-data.js": "ALL_LANGUAGE_CODES",
        "scripts/tools/generate-dashboard-analytics.py": "ENABLED_TRANSLATION_LANGS",
        "scripts/tools/monitor-404.py": "ENABLED_TRANSLATION_LANGS",
        "scripts/tools/check-slug-consistency.py": "ALL_TRANSLATION_LANGS",
        "scripts/tools/review-pr.sh": "ALL_LANGUAGE_CODES",
        "scripts/tools/bulk-pr-analyze.sh": "ALL_LANGUAGE_CODES",
        "scripts/tools/terminology-prose-fix.py": "TRANSLATION_LANGS",
        "scripts/tools/lang-sync/sync-on-update.py": "ENABLED_TRANSLATION_LANGS",
        "scripts/tools/lang-sync/prioritize-batch.py": "ALL_TRANSLATION_LANGS",
        ".husky/pre-commit": "ALL_LANGUAGE_CODES",
        ".github/workflows/pr-review.yml": "ALL_LANGUAGE_CODES",
    }
    for relative_path, symbol in expected_imports.items():
        source = (REPO_ROOT / relative_path).read_text(encoding="utf-8")
        assert symbol in source, f"{relative_path} 未使用語言 registry 的 {symbol}"


def test_localized_article_route_errors_name_the_right_language():
    for code in _enabled_translation_codes():
        route = REPO_ROOT / "src" / "pages" / code / "[category]" / "[slug].astro"
        assert route.exists(), f"缺少 {code} article route"
        source = route.read_text(encoding="utf-8")
        assert f"[{code} getStaticPaths]" in source
