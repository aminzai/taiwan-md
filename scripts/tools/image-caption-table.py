#!/usr/bin/env python3
"""image-caption-table.py — 把一篇文章的每張圖列成「看圖對照表」。

REWRITE-STAGE-3-VERIFY Step 3.6.3「看圖一列」的必經表：每張本地圖一列，
印出 alt、緊接其後的斜體圖說、解析後的本地檔案路徑（存不存在）。
驗證站拿這張表逐列用 Read 打開圖片，alt 與圖說裡的每個可見原子對著畫面核。

為什麼要有這張表（2026-09-19，三篇同日現形 vc=3）：
  金鐘獎 v1「後台手持獎座、身穿西裝」（照片是台上、露肩禮服）、
  低薪「館前路志清大樓、中央自動門」（門楣寫松江路 207 號、旋轉門）、
  油價「加油機上的價格」（畫面是路邊招牌）——三篇走完冷讀與主編仍上線，
  因為所有席位讀的都是文字。`image-alt` 只查有沒有 alt、`image-health` 只查
  檔案存不存在；沒有任何一步把「照片本身」放到驗證者面前。這支工具不做判斷
  （判斷是看圖的人的事），只保證每張圖都有一列、每列都有能直接 Read 的路徑。

用法：
  python3 scripts/tools/image-caption-table.py knowledge/Society/誰算低薪.md
  python3 scripts/tools/image-caption-table.py A.md B.md --json

輸出：markdown 表（預設）或 JSON。外部熱連結（Wikimedia 等）也列，但路徑欄
標 (remote)；找不到的本地檔標 ❌，退出碼 2（讓 pipeline 能 fail-loud）。
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
PUBLIC = REPO / "public"

_RE_IMAGE = re.compile(r"!\[([^\]]*)\]\(([^)\n]+)\)")
_RE_CAPTION = re.compile(r"^\s*(?:_|\*)(.+?)(?:_|\*)\s*$")
_RE_H2 = re.compile(r"^## ")
_SOURCE_SECTIONS = ("## 圖片來源", "## 參考資料", "## 延伸閱讀", "## 資料來源")


def _split_frontmatter(text: str) -> tuple[int, str]:
    """回 (body 起始行號 offset, body)。"""
    if text.startswith("---"):
        end = text.find("\n---", 3)
        if end >= 0:
            head = text[: end + 4]
            return head.count("\n"), text[end + 4 :]
    return 0, text


def _caption_after(lines: list[str], idx: int) -> str:
    """圖片那行之後、下一個非空行若是整行斜體，就是圖說。"""
    j = idx + 1
    while j < len(lines) and not lines[j].strip():
        j += 1
    if j < len(lines):
        m = _RE_CAPTION.match(lines[j])
        if m:
            return m.group(1).strip()
    return ""


def _resolve(src: str) -> tuple[str, bool | None]:
    """回 (顯示路徑, 是否存在)。remote 回 None。"""
    src = src.split(" ")[0].strip()
    if src.startswith(("http://", "https://", "//")):
        return src, None
    rel = src.lstrip("/")
    p = PUBLIC / rel
    return str(p.relative_to(REPO)), p.exists()


def table_for(path: Path) -> list[dict]:
    text = path.read_text(encoding="utf-8")
    pad, body = _split_frontmatter(text)
    lines = body.split("\n")
    rows: list[dict] = []
    in_source_section = False
    for i, line in enumerate(lines):
        if _RE_H2.match(line):
            in_source_section = line.strip().startswith(_SOURCE_SECTIONS)
        if in_source_section:
            continue
        for m in _RE_IMAGE.finditer(line):
            alt, src = m.group(1).strip(), m.group(2).strip()
            disp, exists = _resolve(src)
            rows.append(
                {
                    "n": len(rows) + 1,
                    "line": pad + i + 1,
                    "alt": alt,
                    "caption": _caption_after(lines, i),
                    "path": disp,
                    "exists": exists,
                }
            )
    return rows


def _md(article: Path, rows: list[dict]) -> str:
    out = [f"### 看圖對照表 — {article}", ""]
    if not rows:
        out.append("（正文沒有內文圖）")
        return "\n".join(out)
    out += [
        "| # | 行 | alt | 圖說 | 本地路徑（用 Read 打開） |",
        "| --- | --- | --- | --- | --- |",
    ]
    for r in rows:
        if r["exists"] is None:
            p = f"{r['path']} (remote)"
        elif r["exists"]:
            p = r["path"]
        else:
            p = f"❌ {r['path']}（檔案不存在）"
        alt = r["alt"].replace("|", "\\|")
        cap = (r["caption"] or "—").replace("|", "\\|")
        out.append(f"| {r['n']} | L{r['line']} | {alt} | {cap} | {p} |")
    out.append("")
    out.append(
        f"共 {len(rows)} 張。每列：Read 打開路徑那張圖，alt 與圖說裡的地點、門牌、"
        "衣著、動作、招牌數字、物件種類逐項對畫面；畫面上看不到的一律不寫。"
    )
    return "\n".join(out)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("articles", nargs="+")
    ap.add_argument("--json", action="store_true", help="輸出 JSON 而非 markdown 表")
    args = ap.parse_args()

    rc = 0
    result = {}
    for a in args.articles:
        p = Path(a)
        if not p.exists():
            print(f"❌ 找不到檔案：{a}", file=sys.stderr)
            rc = 2
            continue
        rows = table_for(p)
        result[a] = rows
        if any(r["exists"] is False for r in rows):
            rc = 2
        if not args.json:
            print(_md(p, rows))
            print()
    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    return rc


if __name__ == "__main__":
    sys.exit(main())
