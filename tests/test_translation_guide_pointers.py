"""翻譯入口文件的指路必須指得到真的檔案。

誕生：2026-09-25 twmd-maintainer-am。`i18n/README.md` 畫了一棵有 8 個
`STYLE.md` 的目錄樹，其中 6 個從來沒有被建立過；而 12 個語言都有的
canonical 詞表 `docs/editorial/per-language/TRANSLATION-{lang}.md`，在
`i18n/README.md` 與 `docs/prompts/TRANSLATE_PROMPT.md` 兩份入口文件裡
一個字也沒被提到。送過 98 個 PR 的 aminzai 照著找 `i18n/id/STYLE.md`，
找不到，於是在 PR #1773 裡寫下「i18n/id/STYLE.md not yet exists」，
在沒有讀過印尼文主權詞表的情況下完成翻譯。

canonical 蓋了 12 個語言，入口還在描述 2 個語言的舊世界，中間沒有東西
在對賬（REFLEXES #91 建造與登記是兩個不同步的代謝 / #92 twin-artifact
缺重整器）。這支測試就是那個對賬。
"""

from __future__ import annotations

import json
import re
import subprocess
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parents[1]
PER_LANG_DIR = REPO / "docs/editorial/per-language"
ENTRY_DOCS = (
    REPO / "i18n/README.md",
    REPO / "docs/prompts/TRANSLATE_PROMPT.md",
)


def enabled_translation_langs() -> list[str]:
    """從 languages.mjs 這個 SSOT 取上線語言，不在測試裡寫死清單。"""
    script = (
        "import('file://%s').then(m=>{const L=m.LANGUAGES||m.default;"
        "console.log(JSON.stringify(L.filter(x=>x.enabled&&!x.isDefault)"
        ".map(x=>x.code)))})" % (REPO / "src/config/languages.mjs")
    )
    out = subprocess.run(
        ["node", "-e", script], capture_output=True, text=True, cwd=REPO, timeout=60
    )
    if out.returncode != 0:
        pytest.skip(f"languages.mjs 讀不到，node 說：{out.stderr.strip()[:200]}")
    langs = json.loads(out.stdout.strip().splitlines()[-1])
    assert langs, "語言登記表回空清單，SSOT 可能壞了"
    return langs


def test_every_enabled_language_has_canonical_wordlist() -> None:
    """每個上線語言都要有 canonical 詞表——它同時是品質閘門的資料源。"""
    missing = [
        lang
        for lang in enabled_translation_langs()
        if not (PER_LANG_DIR / f"TRANSLATION-{lang}.md").is_file()
    ]
    assert not missing, (
        "這些上線語言沒有 canonical 詞表："
        f"{missing}。新語言誕生要補 docs/editorial/per-language/TRANSLATION-<lang>.md，"
        "否則翻譯的人與閘門都沒有該語言的主權詞表可讀"
    )


@pytest.mark.parametrize("doc", ENTRY_DOCS, ids=lambda p: p.name)
def test_entry_doc_advertises_only_existing_style_guides(doc: Path) -> None:
    """入口文件提到的每個 i18n/{lang}/STYLE.md 都必須真的存在。

    這條防的是「畫一棵理想的目錄樹」：讀者照著找不到檔案，會得出
    「這個語言沒有指引」的結論，而不是去找別的地方。
    """
    text = doc.read_text(encoding="utf-8")
    # 兩種寫法都要抓：完整路徑 `i18n/ko/STYLE.md`，以及目錄樹裡的裸寫
    # `├── ko/STYLE.md`。原始缺陷正是後者——只抓前者的尺會漏掉造出這支
    # 測試的那個 bug 本身（REFLEXES #99 尺先驗再用）。
    referenced = set(
        re.findall(r"(?:i18n/)?([a-z]{2}(?:-[A-Za-z]{2,4})?)/STYLE\.md", text)
    )
    ghosts = sorted(
        lang for lang in referenced if not (REPO / f"i18n/{lang}/STYLE.md").is_file()
    )
    assert not ghosts, (
        f"{doc.relative_to(REPO)} 提到了不存在的 STYLE.md：{ghosts}。"
        "要嘛建立該檔案，要嘛不要在入口文件裡承諾它"
    )


@pytest.mark.parametrize("doc", ENTRY_DOCS, ids=lambda p: p.name)
def test_entry_doc_routes_to_canonical_wordlist(doc: Path) -> None:
    """兩份入口文件都要指得到 canonical 資料夾。

    STYLE.md 只有 2 個語言有，canonical 詞表 12 個語言都有。入口只講
    STYLE.md 的話，另外 10 個語言的譯者會走到空手而回。
    """
    text = doc.read_text(encoding="utf-8")
    assert "docs/editorial/per-language/" in text, (
        f"{doc.relative_to(REPO)} 沒有指向 docs/editorial/per-language/。"
        "讀這份文件的譯者會找不到自己語言的主權詞表"
    )
