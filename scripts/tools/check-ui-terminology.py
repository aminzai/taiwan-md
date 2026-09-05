#!/usr/bin/env python3
"""check-ui-terminology.py — UI 字串層用語校正閘門（WARN-only）。

背景：讀者 issue #1440 指出站上選單「數據」該用台灣通用譯法「資料」。
docs/editorial/TERMINOLOGY.md §Layer 1「A 類：一律替換」table 早就列了這條規則
（數據 → 資料，分歧類型 B），但那張表只守 knowledge/ 文章（透過
scripts/tools/lib/article_health/checks/terminology.py，且該 plugin 實際
讀的是 data/terminology/*.yaml 的 opt-in `detection:` 區塊 —— 數據.yaml 本身
沒有 detection 區塊，所以連文章層都沒被真的掃到）。src/i18n/**/*.ts 這層則
完全沒有任何用語校正閘門在看。

OBSERVER-QUEUE #31（2026-09-05 哲宇拍板選 A）：把「數據」區段品牌改成「資料」
之外，順便把這道 UI 字串閘門補上——但只做 WARN，不做 hard gate（既有 12 個
案例其實正確用法，例如「投票數據」「PM2.5 監測數據」，自動判斷會有誤判，
需要人眼看一次）。

資料源（單一 SSOT，不重複造字表）：直接 parse
docs/editorial/TERMINOLOGY.md 的「### A 類：一律替換」table，取
分歧類型 == 'B' 的列（跟站上原本「數據 → 資料 tier B」的說法對齊）。
表格本身如果加新行，這支腳本下次跑就自動吃到，不用兩邊維護。

用法：
    python3 scripts/tools/check-ui-terminology.py            # 人類可讀報告
    python3 scripts/tools/check-ui-terminology.py --json     # 機器可讀

Exit code 永遠是 0 —— 這是 WARN-only 工具，不擋 commit / CI，只負責把清單
攤出來讓人看。
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
TERMINOLOGY_MD = REPO_ROOT / "docs" / "editorial" / "TERMINOLOGY.md"
I18N_DIR = REPO_ROOT / "src" / "i18n"

if sys.stdout.encoding and sys.stdout.encoding.lower() not in ("utf-8", "utf8"):
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")


@dataclass
class Term:
    china: str  # 完整原始欄位（可能含括號說明，如「移動（形容手機）」）
    base: str  # 拿掉括號說明後、真正拿去比對的字串
    taiwan: str
    tier: str
    # 只在特定複合詞才判定命中的字（用來壓「移動」這種同時是常用動詞的雜訊）
    compounds: tuple[str, ...] = field(default_factory=tuple)


# ── 已知安全重疊：C 字串本身就是「正確台灣用語」但剛好包含某個 china term 當
# 子字串。純子字串比對會把這些也炸出來，必須排除，否則第一次跑就被當噪音關掉。
#   - 數據機（modem）：data/terminology/數據機.yaml 的 display.taiwan 本身就是
#     「數據機」——這是台灣正確用語，不是「數據」的誤用。
#   - 演算法：display.taiwan 是「演算法」，尾三字剛好是 china term「算法」。
#   - 預算法／決算法：法律名稱（《預算法》《決算法》），首二／尾二字剛好組出
#     「算法」——跟「演算法/algorithm」語意上完全無關，是 budget.ts 這種預算
#     類頁面的高頻污染源（2026-09-05 首跑：14 處「算法」命中裡 11 處是這個）。
_KNOWN_SAFE_SUBSTRINGS: dict[str, list[str]] = {
    "數據": ["數據機"],
    "算法": ["演算法", "預算法", "決算法"],
}

# 「移動（形容手機）」：裸字「移動」本身是通用動詞（移動位置），台灣中文一樣
# 常用，裸字比對雜訊過大。只在下列「形容手機/裝置」的複合詞命中時才算。
_MOBILE_COMPOUNDS = (
    "移動端",
    "移動裝置",
    "移動網路",
    "移動通訊",
    "移動支付",
    "移動版",
    "移動優先",
    "移動電話",
    "移動上網",
)

_TABLE_ROW_RE = re.compile(
    r"^\|\s*(?P<china>[^|]+?)\s*\|\s*(?P<taiwan>[^|]+?)\s*\|\s*(?P<tier>[ABC])\s*\|\s*$"
)


def load_tier_b_terms() -> list[Term]:
    """Parse TERMINOLOGY.md 的「A 類：一律替換」table，取分歧類型 == B 的列。"""
    text = TERMINOLOGY_MD.read_text(encoding="utf-8")
    lines = text.splitlines()

    try:
        start = next(i for i, l in enumerate(lines) if l.strip() == "### A 類：一律替換")
    except StopIteration:
        raise SystemExit(
            f"找不到 TERMINOLOGY.md 的「### A 類：一律替換」標題 — 文件結構可能改了，"
            f"這支腳本的 parser 需要跟著更新（{TERMINOLOGY_MD}）"
        )

    terms: list[Term] = []
    for line in lines[start + 1 :]:
        stripped = line.strip()
        if stripped.startswith("###"):
            break  # 下一個章節，table 結束
        if not stripped.startswith("|"):
            continue
        if set(stripped.replace("|", "").strip()) <= {"-", " "}:
            continue  # 分隔列 |---|---|---|
        m = _TABLE_ROW_RE.match(stripped)
        if not m:
            continue
        china_raw = m.group("china")
        taiwan = m.group("taiwan")
        tier = m.group("tier")
        if china_raw in ("中國用語",):  # header row 保險
            continue
        if tier != "B":
            continue
        base = re.sub(r"（[^）]*）", "", china_raw).strip()
        base = base.split("/")[0].strip()  # 「博主/博客」型不在 B 但保留寫法一致
        compounds: tuple[str, ...] = ()
        if base == "移動":
            compounds = _MOBILE_COMPOUNDS
        terms.append(Term(china=china_raw, base=base, taiwan=taiwan, tier=tier, compounds=compounds))
    if not terms:
        raise SystemExit("TERMINOLOGY.md table parse 出來是空的 — parser 壞了，先別信任這支腳本的結果")
    return terms


def _strip_string_aware_brace_span(text: str, open_idx: int) -> int:
    """從 text[open_idx] == '{' 開始，回傳對應 '}' 的 index（跳過字串/註解內的括號）。"""
    depth = 0
    i = open_idx
    n = len(text)
    in_str: str | None = None  # None / "'" / '"' / '`'
    in_line_comment = False
    in_block_comment = False
    while i < n:
        c = text[i]
        nxt = text[i + 1] if i + 1 < n else ""
        if in_line_comment:
            if c == "\n":
                in_line_comment = False
        elif in_block_comment:
            if c == "*" and nxt == "/":
                in_block_comment = False
                i += 1
        elif in_str:
            if c == "\\":
                i += 1  # 跳過跳脫字元的下一個字
            elif c == in_str:
                in_str = None
        else:
            if c == "/" and nxt == "/":
                in_line_comment = True
                i += 1
            elif c == "/" and nxt == "*":
                in_block_comment = True
                i += 1
            elif c in ("'", '"', "`"):
                in_str = c
            elif c == "{":
                depth += 1
            elif c == "}":
                depth -= 1
                if depth == 0:
                    return i
        i += 1
    return n - 1  # 沒找到收尾括號（不該發生，容錯回傳檔尾）


_ZH_TW_BLOCK_RE = re.compile(r"['\"]zh-TW['\"]\s*:\s*\{")


def find_zh_tw_blocks(text: str) -> list[tuple[int, int]]:
    """回傳 (block_start, block_end) 的清單（含頭尾大括號），可能有多個。"""
    spans = []
    for m in _ZH_TW_BLOCK_RE.finditer(text):
        open_idx = text.index("{", m.end() - 1)
        close_idx = _strip_string_aware_brace_span(text, open_idx)
        spans.append((open_idx, close_idx))
    return spans


_KEY_BEFORE_RE = re.compile(r"['\"]([\w.\-]+)['\"]\s*:")


def nearest_key(text: str, pos: int) -> str:
    """往回找離 pos 最近的 `'key.name':` 當上下文標示（找不到回傳 '?'）。"""
    window_start = max(0, pos - 400)
    window = text[window_start:pos]
    matches = list(_KEY_BEFORE_RE.finditer(window))
    if not matches:
        return "?"
    return matches[-1].group(1)


@dataclass
class Hit:
    file: str
    line: int
    key: str
    china: str
    taiwan: str
    tier: str
    context: str


def scan_file(path: Path, terms: list[Term]) -> list[Hit]:
    text = path.read_text(encoding="utf-8")
    hits: list[Hit] = []
    for block_start, block_end in find_zh_tw_blocks(text):
        block = text[block_start : block_end + 1]
        for term in terms:
            needles = term.compounds if term.compounds else (term.base,)
            safe_subs = _KNOWN_SAFE_SUBSTRINGS.get(term.base, [])
            for needle in needles:
                for m in re.finditer(re.escape(needle), block):
                    abs_pos = block_start + m.start()
                    # 已知安全重疊（如 數據機 / 演算法）跳過
                    skip = False
                    for safe in safe_subs:
                        # 檢查這個 needle 是否落在某個安全字串內
                        idx = block.find(safe)
                        while idx != -1:
                            if idx <= m.start() < idx + len(safe):
                                skip = True
                                break
                            idx = block.find(safe, idx + 1)
                        if skip:
                            break
                    if skip:
                        continue
                    line_no = text.count("\n", 0, abs_pos) + 1
                    key = nearest_key(text, abs_pos)
                    ctx_start = max(0, m.start() - 12)
                    ctx_end = min(len(block), m.end() + 12)
                    context = block[ctx_start:ctx_end].replace("\n", " ")
                    hits.append(
                        Hit(
                            file=str(path.relative_to(REPO_ROOT)),
                            line=line_no,
                            key=key,
                            china=needle,
                            taiwan=term.taiwan,
                            tier=term.tier,
                            context=context,
                        )
                    )
    return hits


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--json", action="store_true", help="輸出機器可讀 JSON")
    parser.add_argument(
        "--path",
        default=str(I18N_DIR),
        help=f"掃描目錄（預設 {I18N_DIR.relative_to(REPO_ROOT)}）",
    )
    args = parser.parse_args()

    terms = load_tier_b_terms()
    scan_root = Path(args.path)
    files = sorted(scan_root.rglob("*.ts"))

    all_hits: list[Hit] = []
    for f in files:
        all_hits.extend(scan_file(f, terms))

    if args.json:
        print(
            json.dumps(
                {
                    "tool": "check-ui-terminology",
                    "severity": "WARN",
                    "terms_checked": [t.base for t in terms],
                    "hit_count": len(all_hits),
                    "hits": [h.__dict__ for h in all_hits],
                },
                ensure_ascii=False,
                indent=2,
            )
        )
        return 0

    print("🧬 check-ui-terminology — UI 字串用語校正閘門（WARN-only，不擋 commit/CI）")
    print(f"   資料源：docs/editorial/TERMINOLOGY.md §A 類：一律替換（分歧類型 B，{len(terms)} 詞）")
    print(f"   掃描範圍：{scan_root.relative_to(REPO_ROOT)}/**/*.ts 的 zh-TW 字串區塊")
    print()

    if not all_hits:
        print("✅ 沒有命中 — 目前沒有 tier B 中國用語殘留在 UI zh-TW 字串。")
        return 0

    by_file: dict[str, list[Hit]] = {}
    for h in all_hits:
        by_file.setdefault(h.file, []).append(h)

    for file, hits in by_file.items():
        print(f"⚠️  {file} ({len(hits)} 處)")
        for h in sorted(hits, key=lambda x: x.line):
            print(
                f"   L{h.line:<5} key={h.key:<40} 「{h.china}」→「{h.taiwan}」  …{h.context}…"
            )
        print()

    print(f"總計：{len(all_hits)} 處 WARN（人工判斷是否需要改；不是每一處都是誤用，語境決定）")
    print("   本工具只列出，不自動改字——「投票數據」「PM2.5 監測數據」這類指數值本身的用法是正確的。")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
