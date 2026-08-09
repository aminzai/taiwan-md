#!/usr/bin/env python3
"""restore-html-blocks.py — 把譯文整段掉的區塊級 HTML 放回原位。

## 這支在補哪個洞

嵌入影片是一段純結構的 HTML：

    <div class="video-embed" style="…">
      <iframe src="https://www.youtube.com/embed/…" title="悲情城市 4K 數位修復版預告" …></iframe>
    </div>

裡面沒有一個字需要翻譯——`title` 是影片的中文原名，讀者要拿它去找原片，規範
明寫不動。但因為它「看起來不像正文」，寫檔的人很容易整段跳過：2026-08-09 委派
批次裡 `Art/台灣電影.md` 的 5 段影片全部消失，72 條腳註與 12 個章節卻一條不差。

掉了不會靜默：`verify-translation.py` 的 URL 多重集會少 5 條而硬失敗。問題是
**發現之後沒有修的辦法**——重派一隻 agent 去翻 85KB 的長文只為了補 5 段不用翻
的 HTML，是拿最貴的資源做最機械的事。這支就是那把機械的鑷子。

全庫 82/905 篇中文原稿含區塊級 HTML（約 9%），這不是單篇的意外。

## 錨點為什麼是「後面那句圖說的序號」

譯文的字句跟原稿對不上（那正是翻譯），所以不能用文字比對定位。第一版用
`(第 K 個標題, 標題後第 N 個區塊)`，實測差一格：中文原稿的圖片與圖說之間
沒有空行、算作同一塊，譯文卻用空行隔開變成兩塊，區塊序號整段被推移。這種
「排版習慣差異」在每一篇譯文上都可能不同，用區塊序號當錨等於把錨綁在流沙上。

穩的錨是**斜體圖說的序號**：影片區塊在本庫的固定寫法是「區塊 + 一句
`_……_` 圖說」，而圖說是譯文一定會保留、也一定 1:1 對應的東西（它是正文的
一部分，寫檔的人不會跳過）。所以錨點取「這段 HTML 後面那句圖說，是全文第
幾句圖說」，插在那句之前。實測 5 段影片全部落回原位。

沒有圖說跟在後面的 HTML 區塊（表格、details）才退回標題＋區塊序號。兩種錨都
失準時整支拒做（exit 2），不猜——插錯位置比缺一段更難發現，寧可留給人。

用法：
    python3 restore-html-blocks.py <zh原稿> <譯文> [--apply] [--quiet]

Exit: 0 = 無缺漏或已修復；1 = 有缺漏（未加 --apply）；2 = 無法錨定，需人工。
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

HEADING = re.compile(r"^#{1,6}\s")
# 區塊級 HTML：整段以 `<` 開頭的塊。行內的 `<br>`、`<sup>` 不算——它們住在段落
# 裡，跟著段落一起被翻譯，不會整段消失。
HTML_BLOCK = re.compile(r"^\s*<(div|figure|iframe|table|video|blockquote|details)\b", re.I)


def _split(text: str) -> tuple[str, list[str]]:
    """切出 frontmatter 與正文區塊（以空行分段）。"""
    fm = ""
    body = text
    if text.startswith("---"):
        parts = text.split("---", 2)
        if len(parts) == 3:
            fm = "---" + parts[1] + "---"
            body = parts[2]
    return fm, [b for b in re.split(r"\n\s*\n", body)]


def _signature(block: str) -> str:
    """區塊的身分證：優先用裡面的網址，沒有就用去空白的全文。

    用網址當簽章，是因為譯文若真的保留了這段 HTML，屬性順序與縮排可能被
    重新排版，但 src 不會變。
    """
    urls = re.findall(r'(?:src|href)="([^"]+)"', block)
    return "|".join(urls) if urls else re.sub(r"\s+", "", block)


def _is_caption(s: str) -> bool:
    """一句獨立的斜體圖說：`_……_` 自成一塊。"""
    s = s.strip()
    return len(s) > 2 and s.startswith("_") and s.endswith("_") and "\n" not in s


def _anchors(blocks: list[str]) -> list[tuple[int, int, int, str]]:
    """回傳 [(標題序號, 標題後第幾塊, 後隨圖說的序號, 區塊內容)]，只收 HTML 區塊。

    後隨圖說序號 = 這段 HTML 緊接著的那句圖說是全文第幾句；沒有圖說跟在後面
    就是 -1（退回標題錨）。
    """
    out, h_idx, since, cap_n = [], -1, 0, 0
    real = [b for b in blocks if b.strip()]
    for i, b in enumerate(real):
        s = b.strip()
        if HEADING.match(s):
            h_idx += 1
            since = 0
            continue
        since += 1
        if _is_caption(s):
            cap_n += 1
            continue
        if HTML_BLOCK.match(s):
            nxt = real[i + 1].strip() if i + 1 < len(real) else ""
            # cap_n 是「這段之前已經數到幾句圖說」，後隨的那句是下一句，故 +1。
            out.append((h_idx, since, cap_n + 1 if _is_caption(nxt) else -1, b))
    return out


def _heading_count(blocks: list[str]) -> int:
    return sum(1 for b in blocks if HEADING.match(b.strip()))


def restore(zh_path: Path, tgt_path: Path, apply: bool, quiet: bool) -> int:
    zh_fm, zh_blocks = _split(zh_path.read_text(encoding="utf-8"))
    tgt_text = tgt_path.read_text(encoding="utf-8")
    tgt_fm, tgt_blocks = _split(tgt_text)

    wanted = _anchors(zh_blocks)
    if not wanted:
        if not quiet:
            print(f"✅ {tgt_path.name} — 原稿無區塊級 HTML")
        return 0

    have = {_signature(b) for *_, b in _anchors(tgt_blocks)}
    missing = [a for a in wanted if _signature(a[-1]) not in have]
    if not missing:
        if not quiet:
            print(f"✅ {tgt_path.name} — {len(wanted)} 段 HTML 區塊全在")
        return 0

    if not apply:
        print(f"❌ {tgt_path.name} — 缺 {len(missing)}/{len(wanted)} 段區塊級 HTML")
        for h, n, c, b in missing[:5]:
            where = f"第 {c} 句圖說前" if c > 0 else f"第 {h + 1} 個標題後第 {n} 塊"
            print(f"     {where}：{_signature(b)[:70]}")
        return 1

    zh_h, tgt_h = _heading_count(zh_blocks), _heading_count(tgt_blocks)
    if zh_h != tgt_h:
        print(
            f"⛔ {tgt_path.name} — 標題數 {tgt_h} ≠ 原稿 {zh_h}，錨點不可信，拒絕插入。"
            "\n   先讓章節數對上（重譯或補章節），再跑這支。"
        )
        return 2

    tgt_real = [b.strip() for b in tgt_blocks if b.strip()]
    zh_caps = sum(1 for b in zh_blocks if _is_caption(b))
    tgt_caps = sum(1 for b in tgt_real if _is_caption(b))
    # 由後往前插，避免前面的插入把後面的序號推掉。
    inserted, degraded = 0, 0
    for h_target, n_target, cap_target, block in sorted(
        missing, key=lambda x: (-x[0], -x[1])
    ):
        pos = None
        if cap_target > 0 and zh_caps == tgt_caps:
            seen = 0
            for i, s in enumerate(tgt_real):
                if _is_caption(s):
                    seen += 1
                    if seen == cap_target:
                        pos = i
                        break
        if pos is None:
            h_idx, since = -1, 0
            for i, s in enumerate(tgt_real):
                if HEADING.match(s):
                    h_idx += 1
                    since = 0
                    continue
                since += 1
                if h_idx == h_target and since == n_target:
                    pos = i
                    break
            degraded += 1
        if pos is None:
            print(f"⛔ {tgt_path.name} — {_signature(block)[:50]} 兩種錨都定不出位置，未插入")
            return 2
        tgt_real.insert(pos, block.strip())
        inserted += 1
    if degraded and not quiet:
        print(f"   ⚠️ {degraded} 段沒有圖說可錨，改用標題＋區塊序號（位置請人工確認）")
    tgt_blocks = tgt_real

    out = (tgt_fm + "\n\n" if tgt_fm else "") + "\n\n".join(
        b.strip() for b in tgt_blocks if b.strip()
    ) + "\n"
    tgt_path.write_text(out, encoding="utf-8")
    if not quiet:
        print(f"🔧 {tgt_path.name} — 補回 {inserted} 段區塊級 HTML")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("zh")
    ap.add_argument("target")
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--quiet", action="store_true")
    a = ap.parse_args()
    return restore(Path(a.zh), Path(a.target), a.apply, a.quiet)


if __name__ == "__main__":
    sys.exit(main())
