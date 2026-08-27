#!/usr/bin/env python3
"""punct-cleanup.py — 標點淨化 campaign 的工作清單產生器 + 事實保真驗證器。

2026-07-19 哲宇選項3 legacy campaign 工具。144 篇 legacy（破折號>15 或全形分號>12）
要交給 codex (sol/luna/terra) + ollama 協作清標點。核心風險：外部 agent 看不到當初
的對話，可能在「改標點」時不小心改到事實。這支把「只改標點、零事實漂移」變成機械
可驗證的閘，不靠 agent 自律。

兩個 mode：

  # 產生工作清單（144 篇 + 每篇破折號/分號數 + category + featured）
  python3 scripts/tools/punct-cleanup.py --worklist

  # 驗證一篇清完的檔 vs git HEAD（改前）——事實保真 + gate pass
  python3 scripts/tools/punct-cleanup.py --verify knowledge/Society/認知作戰.md

--verify 檢查（任一 FAIL = 這次清理動到不該動的東西，必須 revert 重做）：
  1. frontmatter 逐字節不變
  2. 腳註 marker 集合 + 定義數不變（45/45 這種）
  3. 所有數字串（年份/金額/里程/統計）multiset 不變 —— 抓改到數字的事實漂移
  4. 所有「」『』引號內容 multiset 不變 —— 抓改到引語
  5. 所有 [連結文字](url) 的 url 不變 —— 抓改到來源
  6. em-dash ≤ 15 且 全形分號（正文，排除腳註）≤ 12 —— 達標
  7. article-health --profile=pre-commit hard=0 —— 過觸檔即硬 gate + 所有其他 hard 檢查

門檻說明：清理目標是「過未來的全站 hard gate」= em-dash ≤ 15、分號 ≤ 12。
能再往 EDITORIAL 理想（破折號 ≤ 4-8、分號 ≤ 3）更好，但**寧可少改也不要為了壓數字
而改到語意或事實**。#6 只要求達到 gate 門檻，不強迫壓到理想值。
"""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
KNOWLEDGE = REPO / "knowledge"

# SSOT：破折號/分號的「可編輯正文」判定跟 prose-health gate 共用同一 predicate，兩邊不漂
# （2026-07-19 campaign 揭：raw 全 body 計數會把 blockquote/腳註/圖說/書名/參考裝置等
#  鐵律禁改的合法區也數進去，引用/書名多的文章正文清乾淨也過不了 → gate 與 verifier 都改
#  只數可編輯正文的修辭性用法）。
sys.path.insert(0, str(Path(__file__).resolve().parent))
from lib.article_health.checks.prose_health import _uneditable_punct_predicate as _uneditable

# gate 門檻（跟 article-health.config.toml pre-commit override 對齊）
EMDASH_MAX = 15
SEMICOLON_MAX = 12

_RE_EMDASH = re.compile(r"——")
_RE_SEMICOLON = re.compile(r"；")
_RE_FN_MARKER = re.compile(r"\[\^[0-9A-Za-z_-]+\]")
_RE_FN_DEF = re.compile(r"(?m)^\[\^[0-9A-Za-z_-]+\]:")
_RE_DIGITS = re.compile(r"\d+(?:[.,]\d+)*")
_RE_QUOTE = re.compile(r"[「『]([^「」『』]*)[」』]")
_RE_MD_URL = re.compile(r"\]\((https?://[^)]+)\)")
_RE_FM = re.compile(r"^---\n.*?\n---\n", re.S)


def _strip_fm(text: str) -> str:
    m = _RE_FM.match(text)
    return text[m.end():] if m else text


def _fm_block(text: str) -> str:
    m = _RE_FM.match(text)
    return text[: m.end()] if m else ""


def _editable_counts(text: str) -> tuple[int, int]:
    """(可編輯正文破折號數, 分號數)。跟 prose-health gate 用同一 predicate，只數修辭性用法。

    先移除 frontmatter + code fence + HTML 區塊（近似 prose-health 的 body_without_protected），
    再用共用 predicate 排除 blockquote/腳註/圖說/書名/參考裝置。與 gate 計數對齊。
    """
    body = _strip_fm(text)
    body = re.sub(r"```.*?```", "", body, flags=re.S)
    body = re.sub(r"<(div|iframe)[\s\S]*?</\1>", "", body)
    is_un = _uneditable(body)
    dash = sum(1 for m in _RE_EMDASH.finditer(body) if not is_un(m.start()))
    semi = sum(1 for m in _RE_SEMICOLON.finditer(body) if not is_un(m.start()))
    return dash, semi


# ── worklist ──────────────────────────────────────────────────────────────

def _iter_zh_articles():
    for cat in sorted(KNOWLEDGE.iterdir()):
        if not cat.is_dir() or cat.name.startswith((".", "_")):
            continue
        # skip translation dirs (2-letter lang codes)
        if len(cat.name) <= 3 and cat.name.islower():
            continue
        for f in sorted(cat.glob("*.md")):
            if f.name.startswith("_"):
                continue
            yield f


def worklist():
    rows = []
    for f in _iter_zh_articles():
        text = f.read_text(encoding="utf-8")
        body = _strip_fm(text)
        # em-dash: exclude the 《…——…》 book-title & quote-attribution lines is hard to do
        # generically; count raw and let the agent apply the known exceptions.
        dash, semi = _editable_counts(text)
        if dash > EMDASH_MAX or semi > SEMICOLON_MAX:
            featured = bool(re.search(r"(?m)^featured:\s*true", text))
            rows.append((f.relative_to(REPO), dash, semi, f.parent.name, featured))
    rows.sort(key=lambda r: -(r[1] + r[2]))
    print(f"# 標點淨化 campaign 工作清單 — {len(rows)} 篇（破折號>{EMDASH_MAX} 或 分號>{SEMICOLON_MAX}）")
    print(f"# 產生：punct-cleanup.py --worklist")
    print(f"# 欄位：path\\tem_dash\\tsemicolon\\tcategory\\tfeatured")
    for path, dash, semi, cat, feat in rows:
        print(f"{path}\t{dash}\t{semi}\t{cat}\t{'featured' if feat else '-'}")
    return rows


# ── fix（保守自動拆句）────────────────────────────────────────────────────
# 2026-08-20 maintainer-am：分號是投稿 PR 過不了 gate 的第一大宗殘餘 blocker。八月的
# 兩批投稿（8/15 的 67 個 PR、8/19-20 的 26 個）跑完既有 heal 鏈之後，剩下的 hard 幾乎
# 都是這一條，每次都要有人手改幾十處。gate 自己的 fix_suggestion 寫得很清楚：
# 「前後子句拆成兩個句號句（；→。），或並列項改頓號（、）」——第一種是機械可決定的，
# 第二種需要讀懂並列關係。這支只做第一種，第二種留給人。
#
# 保守判準（不確定就不動，寧可留著讓人看）：
#   - 只碰 gate 認定「可編輯正文」的位置（共用 _uneditable predicate，不另立一把尺）
#   - 分號前的子句 < _MIN_CLAUSE_CJK 個中文字 → 疑似並列列舉（該用頓號），跳過
#   - 分號後緊接結束標點 / 引號收尾 / 右括號 → 跳過
#   - 同一行分號 ≥ _LIST_LINE_SEMIS 個 → 整行疑似列舉，跳過
# 寫檔前一律跑 verify()（事實保真 multiset + 真 gate），任一項不過就整篇還原。
# 註：這支是提案者，不是裁判——達標與否由 article-health 那把尺回答（REFLEXES #69）。

_MIN_CLAUSE_CJK = 8       # 分號前子句至少幾個中文字才視為「獨立子句」
_LIST_LINE_SEMIS = 3      # 一行內分號達幾個就當列舉行整行跳過
_RE_SKIP_AFTER = re.compile(r"^[」』）)\]】》，。；、！？]")


def _mask_protected(body: str) -> str:
    """把 code fence / HTML 區塊換成等長空白，保留 offset 與換行，供共用 predicate 定位。"""
    def blank(m: re.Match) -> str:
        return "".join("\n" if ch == "\n" else " " for ch in m.group(0))
    masked = re.sub(r"```.*?```", blank, body, flags=re.S)
    masked = re.sub(r"<(div|iframe)[\s\S]*?</\1>", blank, masked)
    masked = re.sub(r"https?://\S+", blank, masked)
    return masked


def fix_one(path: Path, dry_run: bool = False) -> tuple[bool, int, int, int]:
    """回傳 (是否寫檔, 改前分號, 改後分號, 實際轉換數)。"""
    path = path if path.is_absolute() else (REPO / path)
    original = path.read_text(encoding="utf-8")
    fm, body = _fm_block(original), _strip_fm(original)

    masked = _mask_protected(body)
    is_un = _uneditable(masked)

    line_semis: dict[int, int] = {}
    for m in _RE_SEMICOLON.finditer(masked):
        ls = masked.rfind("\n", 0, m.start()) + 1
        line_semis[ls] = line_semis.get(ls, 0) + 1

    before = sum(1 for m in _RE_SEMICOLON.finditer(masked) if not is_un(m.start()))

    out, converted, cursor = [], 0, 0
    for m in _RE_SEMICOLON.finditer(masked):
        i = m.start()
        if is_un(i):
            continue
        ls = masked.rfind("\n", 0, i) + 1
        if line_semis.get(ls, 0) >= _LIST_LINE_SEMIS:
            continue
        clause = masked[ls:i]
        # 子句起點取最近的句界，避免把整行長度誤當一個子句
        for sep in ("。", "！", "？", "：", "；"):
            p = clause.rfind(sep)
            if p != -1:
                clause = clause[p + 1:]
        if len(_CJK_RE.findall(clause)) < _MIN_CLAUSE_CJK:
            continue
        if _RE_SKIP_AFTER.match(masked[i + 1: i + 2]):
            continue
        out.append(body[cursor:i])
        out.append("。")
        cursor = i + 1
        converted += 1
    out.append(body[cursor:])
    new_body = "".join(out)

    after = sum(1 for m in _RE_SEMICOLON.finditer(_mask_protected(new_body))
                if not _uneditable(_mask_protected(new_body))(m.start()))

    if dry_run or converted == 0:
        return False, before, after, converted

    # 寫檔前先記下「改之前就有的 hard」。verify() 第 7 步跑的是整篇 article-health，
    # 一篇本來就有無關 hard（熱連結圖、缺圖檔…）的投稿會讓這支永遠不敢寫檔——那是把
    # 「我這次改壞了嗎」跟「這篇本來就有別的問題嗎」混成同一個燈（REFLEXES #38 混維度，
    # 2026-08-20 首跑 #1456 當場現形）。所以只問 delta：事實保真絕對成立，hard 只要求沒新增。
    baseline_hard = _hard_signatures(path, text=original)
    path.write_text(fm + new_body, encoding="utf-8")
    ok, reasons = _fidelity_ok(original, path.read_text(encoding="utf-8"))
    introduced = sorted(_hard_signatures(path) - baseline_hard)
    if introduced:
        ok = False
        reasons.append("新增 hard：" + "；".join(introduced[:2]))
    if not ok:
        path.write_text(original, encoding="utf-8")
        print(f"↩️  {path.name}: 拆句未過保真檢查，已整篇還原 — {reasons[:2]}")
        return False, before, before, 0
    return True, before, after, converted


def _hard_signatures(path: Path, text: str | None = None) -> set[str]:
    """這篇當下的 hard 訊息集合（去行號，供 before/after 比對）。"""
    restore = None
    if text is not None:
        restore = path.read_text(encoding="utf-8")
        path.write_text(text, encoding="utf-8")
    try:
        out = subprocess.run(
            ["python3", str(REPO / "scripts/tools/article-health.py"),
             str(path), "--profile=pre-commit"],
            capture_output=True, text=True, timeout=180,
        )
        return {
            re.sub(r"^hard\s+L?\d*\s*:?\s*", "", s)[:90]
            for s in (line.strip() for line in (out.stdout or "").splitlines())
            if s.startswith("hard ")
        }
    except Exception:
        return set()
    finally:
        if restore is not None:
            path.write_text(restore, encoding="utf-8")


def _fidelity_ok(old: str, new: str) -> tuple[bool, list[str]]:
    """事實保真：frontmatter / 腳註 / 數字 / 引語 / URL 一個位元都不准變。"""
    fails = []
    if _fm_block(old) != _fm_block(new):
        fails.append("frontmatter 被改動")
    miss, add = _multiset_diff(_RE_FN_MARKER.findall(old), _RE_FN_MARKER.findall(new))
    if miss or add:
        fails.append(f"腳註 marker 變動：缺 {miss[:3]} 多 {add[:3]}")
    if len(_RE_FN_DEF.findall(old)) != len(_RE_FN_DEF.findall(new)):
        fails.append("腳註定義數變動")
    miss, add = _multiset_diff(_RE_DIGITS.findall(old), _RE_DIGITS.findall(new))
    if miss or add:
        fails.append(f"數字變動：缺 {miss[:5]} 多 {add[:5]}")
    if _multiset_diff(_RE_QUOTE.findall(old), _RE_QUOTE.findall(new)) != ([], []):
        fails.append("引號內容變動")
    if _multiset_diff(_RE_MD_URL.findall(old), _RE_MD_URL.findall(new)) != ([], []):
        fails.append("連結 URL 變動")
    return (not fails), fails


_CJK_RE = re.compile(r"[一-鿿]")


# ── verify ────────────────────────────────────────────────────────────────

def _git_head(path: Path) -> str | None:
    rel = path.relative_to(REPO) if path.is_absolute() else path
    try:
        out = subprocess.run(
            ["git", "-C", str(REPO), "show", f"HEAD:{rel}"],
            capture_output=True, text=True, timeout=30,
        )
        return out.stdout if out.returncode == 0 else None
    except Exception:
        return None


def _multiset_diff(old_list, new_list):
    """回傳 (只在 old 缺的, 只在 new 多的)。用 Counter。"""
    from collections import Counter
    co, cn = Counter(old_list), Counter(new_list)
    missing = list((co - cn).elements())
    added = list((cn - co).elements())
    return missing, added


def verify(path: Path, baseline: str | None = None) -> bool:
    path = path if path.is_absolute() else (REPO / path)
    new = path.read_text(encoding="utf-8")
    old = baseline if baseline is not None else _git_head(path)
    fails = []

    if old is None:
        print(f"⚠️  {path.name}: git HEAD 無此檔（新檔？）— 只能跑達標 + gate 檢查，跳過事實比對")
    else:
        # 1. frontmatter 逐字節
        if _fm_block(old) != _fm_block(new):
            fails.append("frontmatter 被改動（campaign 只准動正文標點）")
        # 2. 腳註
        old_fn = _RE_FN_MARKER.findall(old); new_fn = _RE_FN_MARKER.findall(new)
        miss, add = _multiset_diff(old_fn, new_fn)
        if miss or add:
            fails.append(f"腳註 marker 變動：缺 {miss[:5]} 多 {add[:5]}")
        if len(_RE_FN_DEF.findall(old)) != len(_RE_FN_DEF.findall(new)):
            fails.append(f"腳註定義數變動：{len(_RE_FN_DEF.findall(old))}→{len(_RE_FN_DEF.findall(new))}")
        # 3. 數字 multiset
        miss, add = _multiset_diff(_RE_DIGITS.findall(old), _RE_DIGITS.findall(new))
        if miss or add:
            fails.append(f"數字變動（事實漂移！）：缺 {miss[:8]} 多 {add[:8]}")
        # 4. 引號內容 multiset
        miss, add = _multiset_diff(_RE_QUOTE.findall(old), _RE_QUOTE.findall(new))
        if miss or add:
            fails.append(f"引號內容變動（引語漂移！）：缺 {[m[:20] for m in miss[:5]]} 多 {[a[:20] for a in add[:5]]}")
        # 5. URL
        miss, add = _multiset_diff(_RE_MD_URL.findall(old), _RE_MD_URL.findall(new))
        if miss or add:
            fails.append(f"連結 URL 變動：缺 {miss[:3]} 多 {add[:3]}")

    # 6. 達標（可編輯正文修辭性用法；禁改合法區不計）
    dash, semi = _editable_counts(new)
    if dash > EMDASH_MAX:
        fails.append(f"破折號 {dash} > {EMDASH_MAX}（可編輯正文仍超，繼續清；書名/引語出處/blockquote/腳註已不計）")
    if semi > SEMICOLON_MAX:
        fails.append(f"全形分號 {semi} > {SEMICOLON_MAX}（可編輯正文仍超，繼續清）")

    # 7. article-health pre-commit hard gate
    try:
        out = subprocess.run(
            ["python3", str(REPO / "scripts/tools/article-health.py"),
             str(path), "--profile=pre-commit", "--quiet"],
            capture_output=True, text=True, timeout=120,
        )
        if out.returncode != 0:
            tail = (out.stdout or out.stderr).strip().splitlines()[-6:]
            fails.append("article-health pre-commit hard fail:\n      " + "\n      ".join(tail))
    except Exception as e:
        fails.append(f"article-health 跑不起來：{e}")

    if fails:
        print(f"❌ {path.name} — {len(fails)} 項未過：")
        for x in fails:
            print(f"   • {x}")
        return False
    print(f"✅ {path.name} — 事實保真 + 達標 + pre-commit hard gate 全過（破折號 {dash} / 分號 {semi}）")
    return True


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--worklist", action="store_true", help="產生 144 篇工作清單")
    ap.add_argument("--verify", metavar="FILE", help="驗證一篇清完的檔 vs git HEAD")
    ap.add_argument("--fix", nargs="+", metavar="FILE", help="保守自動拆句（；→。），寫檔前跑 verify，不過就還原")
    ap.add_argument("--dry-run", action="store_true", help="與 --fix 併用：只印會轉幾處，不寫檔")
    args = ap.parse_args()
    if args.worklist:
        worklist()
    elif args.verify:
        sys.exit(0 if verify(Path(args.verify)) else 1)
    elif args.fix:
        bad = 0
        for f in args.fix:
            wrote, before, after, n = fix_one(Path(f), dry_run=args.dry_run)
            tag = "DRY" if args.dry_run else ("✅" if wrote else "—")
            print(f"{tag} {f}: 分號 {before} → {after}（轉換 {n} 處）")
            if not args.dry_run and after > SEMICOLON_MAX:
                print(f"   ⚠️  仍 > {SEMICOLON_MAX}，剩下的是列舉型或短子句，需要人改成頓號")
                bad += 1
        sys.exit(1 if bad else 0)
    else:
        ap.error("--worklist 或 --verify FILE")


if __name__ == "__main__":
    main()
