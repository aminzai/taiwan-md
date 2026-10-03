#!/usr/bin/env python3
"""策展人筆記密度盤點 — 量 EDITORIAL §四 密度上限與 §十 最低使用量各自蓋住多少條目。

**這支是尺，不是閘門。** 它沒有接 pre-commit、沒有接 CI、沒有 pass/fail 門檻，
因為它要量的那兩條規則目前互相矛盾，而「要留哪一條」是 OBSERVER-QUEUE #74
在等的決定（EDITORIAL 要不要分成事實層硬閘門與美學層預設）。先量再改，
拍板之前不該有東西拿這兩條規則去擋任何人的 commit（REFLEXES #66 門檻要用
真實產出校準、#99 尺先驗再用）。

量的是哪兩條（canonical: docs/editorial/EDITORIAL.md）：

  §四 密度規則：1500 字以下 0-1 個；1500-3000 字 1-2 個；3000+ 字 2-4 個。寧少勿多。
  §十 富文本最低使用量：B 級至少 1 個 📝 策展人筆記 callout。「不強制 = 不存在」。

§四 容許 0 個（「寧少勿多」），§十 把 0 這個出口關掉——同一份 canonical 的兩端
對同一篇文章可以同時判它太多與太少。這支尺把兩個族群分開報，讓那個矛盾有數字。

誕生：2026-10-03 twmd-maintainer-am。Discussion #1757（kwt-klure）抽樣 24 篇近期
條目，量到策展人筆記是「可逐篇插入的零件」裡收斂最明顯的一個（88% 的文章有、
平均 2.75 則、4 篇超過文件自訂上限）。本尺把那份抽樣放大到全庫，因為 §四 這條
規則寫進 canonical 之後從來沒有任何儀器看過它（34 個 article-health check 裡
沒有一個量筆記密度；prose-health 只把筆記當排除區，不量它的量）。

用法：
    python3 scripts/tools/curator-note-density.py                 # 全庫報告
    python3 scripts/tools/curator-note-density.py --json          # 機器可讀
    python3 scripts/tools/curator-note-density.py --top 20        # 超標前 N 篇
    python3 scripts/tools/curator-note-density.py knowledge/Society/馬英九迷因.md
"""

import argparse
import json
import pathlib
import re
import sys
from collections import Counter

REPO = pathlib.Path(__file__).resolve().parents[2]
KNOWLEDGE = REPO / "knowledge"

# 譯文目錄不算：§四／§十 是中文母稿的編輯規則，譯文的筆記數由母稿決定
# （語言清單刻意不寫死——凡是 knowledge/ 下兩字母以內的目錄即視為語言目錄，
#  新語言出生時這支尺不需要改，per §神經迴路「新語言出生時感知系統不會自動更新」）
NON_ZH_DIR = re.compile(r"^[a-z]{2}(-[A-Za-z]{2,4})?$|^all$")

# 一行「開啟一則策展人筆記」的條件：標記詞之前只有 blockquote／標題／強調／emoji
# 標記與空白。這樣寫才能同時收下庫內實際出現的 12 種變體（`> **📝 策展人筆記`、
# `📝 **策展人筆記**`、`## 策展人筆記`、`> 🎙️ **策展人筆記` …），又不會把正文
# 裡順口提到「策展人筆記」的句子算成一則（全庫 3 例，已抽驗）。
NOTE_LINE = re.compile(r"^[\s>#*_\-]*(?:[\U0001F300-\U0001FAFF☀-➿️]\s*)*[\s>#*_]*策展人筆記")
CJK = re.compile(r"[一-鿿]")


def density_cap(cjk_chars: int) -> int:
    """EDITORIAL §四 密度規則的上限。"""
    if cjk_chars < 1500:
        return 1
    if cjk_chars <= 3000:
        return 2
    return 4


def count_notes(body: str) -> int:
    return sum(1 for line in body.splitlines() if NOTE_LINE.match(line))


def strip_frontmatter(text: str) -> str:
    if text.startswith("---"):
        parts = text.split("---", 2)
        if len(parts) == 3:
            return parts[2]
    return text


def zh_articles():
    for path in sorted(KNOWLEDGE.glob("*/*.md")):
        if NON_ZH_DIR.match(path.parts[-2]):
            continue
        if path.name.startswith("_"):
            continue
        yield path


def measure(path: pathlib.Path) -> dict:
    body = strip_frontmatter(path.read_text(encoding="utf-8", errors="replace"))
    chars = len(CJK.findall(body))
    notes = count_notes(body)
    cap = density_cap(chars)
    return {
        "path": str(path.relative_to(REPO)),
        "cjk_chars": chars,
        "notes": notes,
        "cap": cap,
        "over_by": max(0, notes - cap),
        "over_cap": notes > cap,          # §四 判太多
        "below_minimum": notes == 0,      # §十 判太少（B 級至少 1）
    }


def main() -> int:
    ap = argparse.ArgumentParser(description="策展人筆記密度盤點（尺，非閘門）")
    ap.add_argument("files", nargs="*", help="指定檔案；省略 = 全庫 zh 條目")
    ap.add_argument("--json", action="store_true", help="輸出 JSON")
    ap.add_argument("--top", type=int, default=10, help="超標排行顯示幾篇（預設 10）")
    args = ap.parse_args()

    if args.files:
        paths = [pathlib.Path(f).resolve() for f in args.files]
        missing = [p for p in paths if not p.is_file()]
        if missing:
            print(f"找不到：{', '.join(str(p) for p in missing)}", file=sys.stderr)
            return 2
    else:
        paths = list(zh_articles())

    rows = [measure(p) for p in paths]
    if not rows:
        print("沒有可量的條目", file=sys.stderr)
        return 2

    over = [r for r in rows if r["over_cap"]]
    zero = [r for r in rows if r["below_minimum"]]
    total = len(rows)

    if args.json:
        print(json.dumps({
            "total": total,
            "over_cap": len(over),
            "below_minimum": len(zero),
            "mean_notes": round(sum(r["notes"] for r in rows) / total, 2),
            "distribution": dict(sorted(Counter(r["notes"] for r in rows).items())),
            "rows": rows,
        }, ensure_ascii=False, indent=2))
        return 0

    print("════════ 策展人筆記密度盤點（尺，非閘門）════════")
    print(f"  zh 條目                     : {total}")
    print(f"  §四 超過密度上限            : {len(over)}  ({100 * len(over) / total:.1f}%)")
    print(f"  §十 一則都沒有（B 級最低）  : {len(zero)}  ({100 * len(zero) / total:.1f}%)")
    print(f"  平均每篇                    : {sum(r['notes'] for r in rows) / total:.2f} 則")
    print()
    dist = sorted(Counter(r["notes"] for r in rows).items())
    print("  筆記數分布：" + "  ".join(f"{n}則×{c}" for n, c in dist))
    print()
    if over:
        print(f"  超標最多的 {min(args.top, len(over))} 篇（筆記/上限・字數）：")
        for r in sorted(over, key=lambda r: -r["over_by"])[:args.top]:
            print(f"    {r['notes']:3d}/{r['cap']}  {r['cjk_chars']:6d}字  {r['path']}")
        print()
    print("  ⚠️ 這兩個族群是同一份 canonical 的兩端：§四 容許 0 則（寧少勿多），")
    print("     §十 要求 B 級至少 1 則（不強制 = 不存在）。要留哪一條是")
    print("     OBSERVER-QUEUE #74 在等的決定，本尺只量不裁。")
    return 0


if __name__ == "__main__":
    sys.exit(main())
