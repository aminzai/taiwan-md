"""語言範圍的單一來源 —— APPLIES_TO 與各 check 自己的排除清單不准各說各話。

背景：issue #1264 追出來的「兩道尺」。擋住非中文的其實有兩層：

  1. `seo_meta.APPLIES_TO = ["zh-TW"]` —— registry 層過濾，今天真正生效的那道。
  2. `seo_meta._is_excluded_path()` 的前綴清單 —— 被第一道完全遮住，是死碼。

死碼那份停在五語年代（en/ja/ko/es/fr），站上現在有 12 語。放寬 APPLIES_TO 的
那一刻它就復活，而且覆蓋範圍剛好相反：後出生的 ar/ru/hi/id/pt/vi 被放行進來
（`_cjk_count()` 對西里爾與阿拉伯字母一律回 0，等於量了但沒量），實測過的
en/ja/ko/es/fr 反而繼續被擋。所以收斂成一道尺是任何門檻決定的共同前置。

本檔測三件事：
  - 各 check 的路徑排除吃 langs.py SSOT，不自己抄一份語言清單
  - APPLIES_TO 可由 config 覆寫，且**預設行為與今天完全相同**
  - 語言範圍只有一個解析點，runner 與 --fix 不各自實作
"""

from __future__ import annotations

import re
from pathlib import Path

import pytest

from lib.article_health import runner
from lib.article_health.checks import seo_meta
from lib.article_health.config import CheckConfig, Config, ProfileConfig
from lib.article_health.langs import TRANSLATION_LANGS

REPO_ROOT = Path(__file__).resolve().parents[2]
CHECKS_DIR = REPO_ROOT / "scripts" / "tools" / "lib" / "article_health"


# ─── 尺一：路徑排除必須吃 SSOT ────────────────────────────────────────────────


@pytest.mark.parametrize("lang", sorted(TRANSLATION_LANGS))
def test_seo_meta_excludes_every_translation_language(lang):
    """每一個翻譯語言都要被排除，不只五語年代那五個。

    這條在 APPLIES_TO 放寬之前是死碼路徑，但它決定放寬那天的覆蓋範圍。
    """
    assert seo_meta._is_excluded_path(f"knowledge/{lang}/foo.md") is True


def test_seo_meta_still_accepts_zh_tw():
    assert seo_meta._is_excluded_path("knowledge/Technology/台積電.md") is False


def test_seo_meta_accepts_windows_path_separators():
    """Windows 上 `str(Path(...))` 是反斜線，守衛不能因此把每一篇都當成非 knowledge。

    原本的 `"knowledge/" not in path` 對 `knowledge\\Technology\\台積電.md` 成立，
    於是 seo-meta 在 Windows 開發機上一篇都沒量過（Linux/CI 正常，所以沒人發現）。
    """
    assert seo_meta._is_excluded_path("knowledge\\Technology\\台積電.md") is False
    assert seo_meta._is_excluded_path("knowledge\\en\\foo.md") is True


def test_check_guard_follows_the_configured_scope():
    """守衛跟著解析後的 scope 走，不自己另訂一套語言政策。

    只放寬 APPLIES_TO 而守衛仍寫死「所有翻譯都擋」的話，config 旋鈕轉了不會動，
    等於兩道尺還在，只是換一種形狀。
    """
    scope = ["zh-TW", "en"]
    assert seo_meta._is_excluded_path("knowledge/en/foo.md", scope) is False
    # 沒被列進 scope 的語言照舊擋著
    assert seo_meta._is_excluded_path("knowledge/ja/foo.md", scope) is True
    # hub page 不因為 scope 放寬就進來
    assert seo_meta._is_excluded_path("knowledge/en/_index.md", scope) is True


def test_widening_scope_makes_the_check_actually_run(tmp_path):
    """端到端：config 放寬 scope 之後，en 文章真的會被 seo-meta 量到。"""
    from lib.article_health import registry
    from lib.article_health.loader import load_target
    from lib.article_health.runner import run_checks

    registry.reset_registry()
    registry.discover_checks()

    f = tmp_path / "knowledge" / "en" / "x.md"
    f.parent.mkdir(parents=True)
    f.write_text(
        "---\ntitle: 'T'\ndescription: 'D'\n---\n\nbody\n", encoding="utf-8"
    )
    target = load_target(f)

    def violations(report):
        return [v for r in report.results for v in r.violations]

    default_report = run_checks(target, Config(), check_name="seo-meta")
    assert violations(default_report) == [], "預設行為必須維持今天的 zh-TW only"

    widened = Config(checks={
        "seo-meta": CheckConfig(options={"applies_to": ["zh-TW", "en"]}),
    })
    widened_report = run_checks(target, widened, check_name="seo-meta")
    assert violations(widened_report), "放寬 scope 後 seo-meta 應該真的量到這個檔"


def test_no_check_hardcodes_language_path_prefixes():
    """寫死 `knowledge/en/` 這種路徑前綴清單，跟寫死 `"en", "ja"` 是同一個病。

    既有的 test_langs_ssot.test_no_check_hardcodes_the_five_language_world 掃的是
    `"en", "ja", "ko", "es"` 這種裸語言碼字面，所以 seo_meta 用的
    `("knowledge/en/", "knowledge/ja/", ...)` 形式整個溜過去了。補上這一面。
    """
    prefix_form = re.compile(
        r'knowledge/en/["\']\s*,\s*["\']knowledge/ja/'
    )
    offenders = []
    for py in sorted(CHECKS_DIR.rglob("*.py")):
        if py.name == "langs.py":
            continue
        code = "\n".join(
            ln for ln in py.read_text(encoding="utf-8").splitlines()
            if not ln.lstrip().startswith("#")
        )
        if prefix_form.search(code):
            offenders.append(py.relative_to(REPO_ROOT).as_posix())
    assert offenders == [], f"還有寫死語言路徑前綴的檔案：{offenders}"


# ─── 尺二：APPLIES_TO 可由 config 覆寫，預設不變 ─────────────────────────────


class _FakeMod:
    CHECK_NAME = "fake-check"
    APPLIES_TO = ["zh-TW"]


def test_resolve_applies_to_defaults_to_module_constant():
    """沒有任何 config 時，解析結果等同今天的模組常數。"""
    assert runner.resolve_applies_to(_FakeMod, Config(), None) == ["zh-TW"]


def test_resolve_applies_to_defaults_to_wildcard_when_module_is_silent():
    class NoAppliesTo:
        CHECK_NAME = "quiet-check"

    assert runner.resolve_applies_to(NoAppliesTo, Config(), None) == ["*"]


def test_check_options_can_widen_the_language_scope():
    config = Config(checks={
        "fake-check": CheckConfig(options={"applies_to": ["zh-TW", "en"]}),
    })
    assert runner.resolve_applies_to(_FakeMod, config, None) == ["zh-TW", "en"]


def test_profile_options_override_wins_over_check_options():
    """per-profile 控制是重點：pre-commit 嚴、ci-deploy 維持現狀之類的分流。"""
    config = Config(checks={
        "fake-check": CheckConfig(options={"applies_to": ["zh-TW", "en"]}),
    })
    profile = ProfileConfig(
        name="pre-commit",
        options_overrides={"fake-check": {"applies_to": ["zh-TW", "en", "ja"]}},
    )
    assert runner.resolve_applies_to(_FakeMod, config, profile) == [
        "zh-TW", "en", "ja",
    ]


def test_seo_meta_default_scope_is_unchanged():
    """預設行為 = 今天的 zh-TW only。這條是整個重構的安全網。"""
    assert runner.resolve_applies_to(seo_meta, Config(), None) == ["zh-TW"]


# ─── 尺三：解析點只有一個 ────────────────────────────────────────────────────


# ─── 尺四：非中文閾值按文字系統分組（OBSERVER-QUEUE #27 選 D，2026-09-05）────


def test_translation_thresholds_group_ja_ko_separately_from_default():
    """ja/ko（CJK/諺文）吃自己的組；其他語言（含未來新語言）落到 default 組。

    這是「按文字系統分門檻」的核心行為：ja/ko 貼 Google 慣例 (160/60)，
    拉丁與其他字母系統吃比較寬的現況門檻，兩組數字不該混在一起。
    """
    options = {
        "translation_thresholds": {
            "ja": {"title_max": 60, "desc_max": 160},
            "ko": {"title_max": 60, "desc_max": 160},
            "default": {"title_max": 120, "desc_max": 400},
        }
    }
    ja = seo_meta._resolve_translation_thresholds(options, "ja")
    ko = seo_meta._resolve_translation_thresholds(options, "ko")
    assert ja == {"title_max": 60, "desc_max": 160}
    assert ko == {"title_max": 60, "desc_max": 160}

    for lang in ("en", "es", "fr", "pt", "vi", "id", "de", "ar", "ru", "hi"):
        resolved = seo_meta._resolve_translation_thresholds(options, lang)
        assert resolved == {"title_max": 120, "desc_max": 400}, (
            f"{lang} 應該落到 default 組（拉丁與其他字母系統的現況門檻）"
        )

    # 站上還沒出生的語言也要吃 default，不是 None（fail-loud 只在 default
    # 本身缺席時才發生）。
    assert seo_meta._resolve_translation_thresholds(options, "zz-未來語言") == {
        "title_max": 120,
        "desc_max": 400,
    }


def test_translation_thresholds_fail_loud_without_default_group():
    """真的沒有任何吃得到的組時，check 要 fail-loud（yield WARN），不是靜默略過。"""
    assert seo_meta._resolve_translation_thresholds({}, "de") is None
    assert seo_meta._resolve_translation_thresholds(
        {"translation_thresholds": {"ja": {"title_max": 60, "desc_max": 160}}}, "de"
    ) is None


# ─── 尺五：profile 分流 —— pre-commit 開全語言、ci-deploy 維持 zh-TW only ────


def test_real_config_pre_commit_widens_seo_meta_to_all_languages():
    """吃真正的 article-health.config.toml（不是合成 Config），驗證 profile 分流。

    pre-commit 是新寫/改到的檔要守的那道（--staged），ci-deploy 是全站掃描
    （既有 700+ 篇非中文長譯文不該被這次改動標記）。兩者對 seo-meta 的
    applies_to 解析結果必須不同，否則「只守新改到的檔」這個設計等於沒生效。
    """
    from lib.article_health.config import load_config

    config = load_config(REPO_ROOT / "scripts" / "tools" / "article-health.config.toml")

    pre_commit = config.get_profile("pre-commit")
    ci_deploy = config.get_profile("ci-deploy")
    assert pre_commit is not None and ci_deploy is not None

    assert runner.resolve_applies_to(seo_meta, config, pre_commit) == ["*"]
    assert runner.resolve_applies_to(seo_meta, config, ci_deploy) == ["zh-TW"]


def test_real_config_has_ja_ko_and_default_translation_thresholds():
    """真正的 config 檔要有 ja/ko 專屬組 + default 組，且 default 涵蓋 de。"""
    from lib.article_health.config import load_config

    config = load_config(REPO_ROOT / "scripts" / "tools" / "article-health.config.toml")
    options = config.get_check_config("seo-meta").options
    table = options.get("translation_thresholds", {})

    assert "ja" in table and "ko" in table
    assert "default" in table
    for lang in ("ja", "ko"):
        assert table[lang]["desc_max"] == 160
        assert table[lang]["title_max"] == 60
    # default 組沒有幫 de 開專屬 entry —— 用同一份 default 接住，
    # 過期五語清單被拆掉之後這是「新語言自動被守」的驗證點。
    assert "de" not in table
    assert seo_meta._resolve_translation_thresholds(options, "de") == table["default"]


def test_de_is_not_shielded_by_the_retired_five_language_list(tmp_path):
    """過期五語清單（en/ja/ko/es/fr）拆掉之後，de 這種清單外語言不該被靜默放行。

    在放寬過的 scope 下，de 應該被視為 in-scope（不排除），量到就走 default
    門檻——而不是像舊 `_is_excluded_path` 死碼復活時那樣被反向放行不檢查。
    """
    scope = ["zh-TW", "*"]
    assert seo_meta._is_excluded_path("knowledge/de/foo.md", scope) is False

    from lib.article_health import registry
    from lib.article_health.config import CheckConfig, Config, ProfileConfig
    from lib.article_health.loader import load_target
    from lib.article_health.runner import run_checks

    registry.reset_registry()
    registry.discover_checks()

    f = tmp_path / "knowledge" / "de" / "x.md"
    f.parent.mkdir(parents=True)
    # description 刻意超過 default 組的 400 上限，確認真的被量到而不是漏檢。
    f.write_text(
        "---\ntitle: 'Ein kurzer Titel'\ndescription: '" + ("鑫" * 5) + "x" * 420 + "'\n---\n\nbody\n",
        encoding="utf-8",
    )
    target = load_target(f)

    widened = Config(
        checks={
            "seo-meta": CheckConfig(
                options={
                    "applies_to": ["zh-TW", "de"],
                    "translation_thresholds": {
                        "ja": {"title_max": 60, "desc_max": 160},
                        "ko": {"title_max": 60, "desc_max": 160},
                        "default": {"title_max": 120, "desc_max": 400},
                    },
                }
            ),
        }
    )
    report = run_checks(target, widened, check_name="seo-meta")
    violations = [v for r in report.results for v in r.violations]
    assert any("description 太長" in v.message for v in violations), (
        "de 檔在放寬 scope 後應該被 default 組量到並標記超長 description"
    )


def test_applies_to_is_enforced_in_exactly_one_place():
    """決定「這支 check 跑不跑這個語言」的 APPLIES_TO 讀取只准有一處。

    article-health.py 的 `--fix` 路徑原本自己抄了一份過濾
    （`"*" in getattr(m, "APPLIES_TO", ["*"]) or target.lang in m.APPLIES_TO`），
    跟 runner 那份是兩個獨立實作。加了 config 覆寫之後，只改一邊就是新的兩道尺。

    `registry.py` 那處不算：它把 APPLIES_TO 放進 `--list-checks` 的 metadata，是
    顯示模組宣告值，不參與任何選擇決策，而且 registry 這一層拿不到 config。
    """
    reader = re.compile(r'getattr\(\s*\w+\s*,\s*["\']APPLIES_TO["\']')
    sources = [p for p in CHECKS_DIR.rglob("*.py") if p.name != "registry.py"]
    sources.append(REPO_ROOT / "scripts" / "tools" / "article-health.py")

    hits = []
    for py in sorted(set(sources)):
        for lineno, line in enumerate(
            py.read_text(encoding="utf-8").splitlines(), start=1
        ):
            if line.lstrip().startswith("#"):
                continue
            if reader.search(line):
                hits.append(f"{py.relative_to(REPO_ROOT).as_posix()}:{lineno}")

    assert len(hits) == 1, (
        f"APPLIES_TO 的執行點應該只有一處，實際有 {len(hits)} 處：{hits}"
    )
    assert "runner.py" in hits[0], f"執行點跑到別的檔案去了：{hits[0]}"
