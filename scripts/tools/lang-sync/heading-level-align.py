#!/usr/bin/env python3
"""heading-level-align.py — 譯文的標題層級對齊 zh：標題數一樣、只是層級不同時，照 zh 的層級改回來。

為什麼要這支（2026-09-28 巴別塔渦流第二十三輪）：44 篇譯文的標題數跟 zh 完全一樣，層級卻不一樣——
最常見是把 zh 的 ### 升成 ##（ja〈台灣維基百科〉zh 九個 ### 全被譯成 ##），站上的目次因此多出一堆頂層
章節，verify 的章節數比對也跟著報差異。內容沒錯，錯的只是每行開頭幾個井字號，所以這件事不需要模型。

判準刻意保守，三道都要過才動：
  1. 兩邊（## 到 ###### 、程式碼區塊外）標題數一樣
  2. 每個標題在全文的相對位置差不到 0.2——標題數碰巧一樣、實際對不上的篇（例如譯文少一節又多一節）擋在這裡
  3. 只改標題行開頭的井字號數量，標題文字與其他行一個字元都不動

用法：
  python3 heading-level-align.py              # 全庫盤點（dry-run）
  python3 heading-level-align.py <譯文...>     # 指定檔案（dry-run）
  python3 heading-level-align.py --apply ...  # 落地；--apply 不帶檔案＝全庫
標題數不一樣的譯文（全庫約 550 篇）不在這支範圍，要重譯才對得齊。
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[3]
KNOWLEDGE = REPO / "knowledge"
sys.path.insert(0, str(Path(__file__).resolve().parent))
from langs import ALL_TRANSLATION_LANGS  # noqa: E402

SRC = re.compile(r"^translatedFrom:\s*['\"]?([^'\"\n]+)", re.M)
HEADING = re.compile(r"^(#{2,6})( \S.*)$")
MAX_POSITION_GAP = 0.2


def split_fm(text: str) -> tuple[str, str]:
    m = re.match(r"^---\n.*?\n---\n", text, re.S)
    return (text[:m.end()], text[m.end():]) if m else ("", text)


def headings(body: str) -> list[tuple[int, int, float]]:
    """(行號, 層級, 在全文的相對位置)，程式碼區塊裡的井字號不算。"""
    lines, out, fence, pos = body.split("\n"), [], False, 0
    total = max(1, len(body))
    for i, line in enumerate(lines):
        if line.lstrip().startswith("```"):
            fence = not fence
        elif not fence:
            m = HEADING.match(line)
            if m:
                out.append((i, len(m.group(1)), pos / total))
        pos += len(line) + 1
    return out


def align(zh_text: str, tr_text: str) -> tuple[str | None, str]:
    """回傳 (改好的譯文, 說明)；不該動時第一個值是 None。"""
    _, zb = split_fm(zh_text)
    tfm, tb = split_fm(tr_text)
    zh_h, tr_h = headings(zb), headings(tb)
    if [h[1] for h in zh_h] == [h[1] for h in tr_h]:
        return None, "same"
    if len(zh_h) != len(tr_h):
        return None, f"heading count differs ({len(zh_h)} vs {len(tr_h)})"
    gap = max(abs(z[2] - t[2]) for z, t in zip(zh_h, tr_h))
    if gap > MAX_POSITION_GAP:
        return None, f"positions do not line up (max gap {gap:.2f})"
    lines = tb.split("\n")
    changed = 0
    for (_, zl, _), (ti, tl, _) in zip(zh_h, tr_h):
        if zl != tl:
            lines[ti] = "#" * zl + HEADING.match(lines[ti]).group(2)
            changed += 1
    return tfm + "\n".join(lines), f"{changed}/{len(tr_h)} headings realigned"


def main() -> int:
    args = [a for a in sys.argv[1:] if a != "--apply"]
    apply = "--apply" in sys.argv
    files = ([Path(a) if Path(a).is_absolute() else REPO / a for a in args] if args else
             [p for L in ALL_TRANSLATION_LANGS for p in sorted((KNOWLEDGE / L).rglob("*.md"))
              if not p.name.startswith("_")])
    fixed = skipped = 0
    for p in files:
        t = p.read_text(encoding="utf-8")
        m = SRC.search(t)
        zp = KNOWLEDGE / m.group(1).strip() if m else None
        if not zp or not zp.exists():
            continue
        new, note = align(zp.read_text(encoding="utf-8"), t)
        if new is None:
            if note != "same" and args:
                print(f"skip  {p.relative_to(REPO)}  — {note}")
            skipped += note != "same"
            continue
        fixed += 1
        print(f"{'fixed' if apply else 'would'} {p.relative_to(REPO)}  — {note}")
        if apply:
            p.write_text(new, encoding="utf-8")
    print(f"\n{'已對齊' if apply else '可對齊'} {fixed} 篇；標題數或位置對不上而略過 {skipped} 篇")
    return 0


if __name__ == "__main__":
    sys.exit(main())
