#!/usr/bin/env python3
"""translation-wikilink-stock.py — 譯文裡殘留的 [[wikilink]] 存量：分三類，只機械改寫第一類。

為什麼要這支（2026-09-28 巴別塔渦流第二十四輪）：譯文不該留 [[wikilink]]。三條翻譯引擎從
2026-09-22 起在送模型前用 `cross_link_localizer.resolve_wikilinks()` 把它收回工具端（該語言有
目標的譯文 → markdown 連結，沒有 → 純文字），那之前落地的譯文還留著 940 個。站上文章頁把
wikilink 一律轉成粗體（`src/utils/article-render.ts` 的 resolveWikilinks，不產生連結），所以：
  - 沒有顯示字、目標是 zh 條目名的，越南文頁面上出現粗體的「濁水溪公社」——讀者看到中文
    （2026-09-28 線上實測 /vi/music/taiwan-music-festival-culture/）
  - 拿英文名當目標的（`[[Jody Chiang]]`）對不到任何條目，pre-commit 的 wikilink-target hard
    閘門會擋下之後任何碰到這篇的 commit（渦流第二十三輪對齊標題層級時撞上）

三類：
  A 顯示字不含漢字、該語言有目標的譯文 → 交給 resolve_wikilinks 改成 [顯示字](/lang/cat/slug/)。
    這就是引擎現在對每篇新譯文做的事，不需要判斷；--apply 只動這一類
  B 顯示字不含漢字、目標對不到（多半是英文名當目標）→ 要照 zh 同位置的 wikilink 找回條目，不動
  C 顯示字含漢字 → 要替它找該語言的名字（模型或名字表），不動

判斷一律交給 cross_link_localizer（has_cjk、resolve_wikilinks），這裡不另寫一份：同一件事兩套
判準會分歧（BABEL-VORTEX-LOOP §儀器化第 1 條）。程式碼區塊裡的不算，frontmatter 不碰。

用法：
  python3 translation-wikilink-stock.py              # 全庫盤點（dry-run），各語 A/B/C
  python3 translation-wikilink-stock.py <譯文...>     # 指定檔案（dry-run，列出每一處）
  python3 translation-wikilink-stock.py --apply ...  # 只改 A 類；不帶檔案＝全庫
"""
from __future__ import annotations

import re
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import cross_link_localizer as X  # noqa: E402
from langs import ALL_TRANSLATION_LANGS  # noqa: E402

REPO = Path(__file__).resolve().parents[3]
KNOWLEDGE = REPO / "knowledge"
FM = re.compile(r"^---\n.*?\n---\n", re.S)


def rewrite(body: str, lang: str, index: X.LocalizerIndex) -> tuple[str, Counter, list[tuple[str, str]]]:
    """回傳 (只改了 A 類的正文, 各類計數, [(類別, 原文)])。"""
    counts: Counter = Counter()
    seen: list[tuple[str, str]] = []

    def _sub(m: re.Match) -> str:
        label = (m.group(2) or m.group(1)).strip()
        if X.has_cjk(label):
            kind, new = "C", m.group(0)
        else:
            out, linked, _ = X.resolve_wikilinks(m.group(0), lang, index)
            kind, new = ("A", out) if linked else ("B", m.group(0))
        counts[kind] += 1
        seen.append((kind, m.group(0)))
        return new

    lines, fence = body.split("\n"), False
    for i, line in enumerate(lines):
        if line.lstrip().startswith("```"):
            fence = not fence
        elif not fence and "[[" in line:
            lines[i] = X.WIKILINK_RE.sub(_sub, line)
    return "\n".join(lines), counts, seen


def main() -> int:
    args = [a for a in sys.argv[1:] if a != "--apply"]
    apply = "--apply" in sys.argv
    files = ([Path(a) if Path(a).is_absolute() else REPO / a for a in args] if args else
             [p for L in ALL_TRANSLATION_LANGS for p in sorted((KNOWLEDGE / L).rglob("*.md"))
              if not p.name.startswith("_")])
    index = X.load_index()
    per_lang: dict[str, Counter] = {}
    files_with: dict[str, set] = {"A": set(), "B": set(), "C": set()}
    for p in files:
        lang = p.relative_to(KNOWLEDGE).parts[0]
        if lang not in X.LANGS:
            continue
        text = p.read_text(encoding="utf-8")
        m = FM.match(text)
        head, body = (text[:m.end()], text[m.end():]) if m else ("", text)
        new_body, counts, seen = rewrite(body, lang, index)
        per_lang.setdefault(lang, Counter()).update(counts)
        for kind in counts:
            files_with[kind].add(p)
        if args:
            for kind, raw in seen:
                print(f"{kind}  {p.relative_to(REPO)}  {raw}")
        if apply and counts["A"]:
            p.write_text(head + new_body, encoding="utf-8")
            print(f"fixed {p.relative_to(REPO)}  — {counts['A']} 個改成連結")
    for lang in sorted(per_lang):
        c = per_lang[lang]
        print(f"{lang}: A {c['A']}  B {c['B']}  C {c['C']}")
    total = sum(per_lang.values(), Counter())
    print(f"\n{'已改' if apply else '可改'} A 類 {total['A']} 處／{len(files_with['A'])} 篇；"
          f"留給對照工具的 B 類 {total['B']} 處／{len(files_with['B'])} 篇；"
          f"讀者看到中文的 C 類 {total['C']} 處／{len(files_with['C'])} 篇")
    return 0


if __name__ == "__main__":
    sys.exit(main())
