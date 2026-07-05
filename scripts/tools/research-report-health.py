#!/usr/bin/env python3
"""research-report-health.py — Stage 1 SSOT 研究報告品質閘門

對標研究所論文標準：一份 depth-article 的 research report 必須是 SSOT —
記錄完整搜尋軌跡（方法論）+ 多語系/一手/學術來源多樣性 + 每個 claim 的信度標記 +
完整參考文獻。這支工具把 REWRITE-PIPELINE Stage 1 的搜尋配額從「aspirational 規則」
儀器化成「可量測的 hard gate」(REFLEXES #15)。

誕生背景（2026-06-04 深度研究-設計研究院 session）：
量測 226 份歷史 research report 發現 57% 英文/國際/學術來源 = 0、42% distinct 來源 ≤ 10，
且 v6.3 多 agent 編排「合成 clean fact-pack」把 agent 原始搜尋軌跡丟掉（違反 Step 1.7
「不摘要」）。哲宇 directive：Stage 0 20+ / Stage 1 80+ / 全部寫回 report 當 SSOT / 對標論文。

stdlib-only，可接 CI gate。

用法:
  python3 scripts/tools/research-report-health.py reports/research/2026-06/{slug}.md
  python3 scripts/tools/research-report-health.py {file} --tier=depth   # 預設
  python3 scripts/tools/research-report-health.py {file} --tier=standard
  python3 scripts/tools/research-report-health.py {file} --json
退出碼: 0 = PASS, 1 = FAIL (hard 未過), 2 = 檔案問題
"""
import argparse
import json
import re
import sys
from pathlib import Path

# ── 來源分類 heuristics ──────────────────────────────────────────────
EN_HINTS = (
    "en.wikipedia.org", "dezeen", "bbc.", "reuters", "theguardian", "nytimes",
    "scholar.google", "jstor", "wdo.org", "designboom", "cnn.", "apnews",
    "sciencedirect", "springer", "nature.com", "taipeitimes", "taiwan-panorama",
    "focustaiwan", "researchgate", "academia.edu", "ieee", "acm.org", "arxiv",
    "/en/", "thediplomat", "aljazeera", "economist", "ft.com", "wsj.com",
    "japantimes", "koreaherald", "scmp.com",
    # 2026-06-12 justfont EVOLVE 補：科技/設計題常見英文媒體與國際組織（原漏）
    "qz.com", "appleinsider", "goldthread", "atypi.org", "en.morisawa", "blog.adobe",
    # 2026-06-14 造山者 EVOLVE 補：紀錄片/半導體/外交題常見英文媒體・智庫・學術・英文官方頻道（原漏）
    "cinemaescapist", "aparc.fsi", "hoover.org", "fpri.org", "sagepub", "gasiantimes",
    "jsis.washington", "taiwanplus", "/english/", "larb.org", "fsi.stanford",
)
# 一手 = 官方 / 政府 / 學術原始來源
# 註：.org.tw 多為財團法人 / 官方機構 / 協會官網（tdri.org.tw / goldenpin.org.tw /
#     *.design.org.tw 等），算一手；.com.tw 太廣（含 chinatimes 等媒體）故不納入。
PRIMARY_HINTS = (
    ".gov.tw", ".gov/", "gov.tw", ".edu.tw", ".edu/", "edu.tw", "sinica.edu",
    ".org.tw",  # 財團法人 / 官方機構 / 協會官網（2026-06-04 v2 實驗補：原漏 tdri.org.tw 等）
    "ndltd.ncl", "airitilibrary", "stat.gov", "ly.gov.tw", "president.gov",
    "ey.gov", "moc.gov", "moe.gov", "drnh.gov", "scholar.google", "jstor",
    "law.moj", "mops.twse", "gcis.nat", "data.gov", "nmth", "npm.gov",
    "ith.sinica", "drnh", "twreporter",  # 報導者 = 深度一手調查
    # 2026-06-12 justfont EVOLVE 補（原漏，通用性站得住）：官方 source repo＝一手 artifact；
    # 群募平台專案頁＝募資原始數據；國際專業協會官網＝一手
    "github.com", "flyingv.cc", "wabay.tw", "zeczec.com", "atypi.org",
)
# 信度標記 pattern
CONFIDENCE_RE = re.compile(
    r"高信度|高信心|高可信|single[_\s-]?source|單一來源|未驗證|unverified|"
    r"high_confidence|待驗|必驗|交叉(驗證|比對)|verbatim|逐字|信度[:：]|confidence"
)
# 搜尋日誌 / 方法論 section
SEARCHLOG_RE = re.compile(
    r"##+\s*.*(搜尋(日誌|紀錄|記錄|log)|方法論|search\s*log|探索搜尋|query|查詢紀錄|"
    r"研究方法|搜尋軌跡|methodology)",
    re.IGNORECASE,
)
# 信心程度三層系統（v6.5 — 12 範本 #1 共通 pattern）
VERIF_TIERS = (
    re.compile(r"high_confidence|高信度|高可信"),
    re.compile(r"single_source|單一來源"),
    re.compile(r"unverified|未驗證|搜尋.{0,6}未(找到|獲)"),
)
# negative findings（搜了沒找到也要記）
NEGATIVE_RE = re.compile(
    r"未找到|未獲|查無|搜尋.{0,8}(未|無)|no data found|未發布|未公開|找不到|無法(取得|查證|驗證)"
)
# 反例 / 不能說的話 / 不採信清單 section（護欄前置）
COUNTEREX_RE = re.compile(
    r"##+\s*.*(反例|不能說|不採信|必驗反例|可能陷阱|red[_\s-]?flag|護欄|不可寫|風險)",
    re.IGNORECASE,
)
URL_RE = re.compile(r"https?://[^\s\)\]\>\"'，。、；]+")

# ── §8 raw 密度 + ephemeral pointer（v2 — 2026-07-05 柯智棠健檢）────────────
# 誕生背景：柯智棠 EVOLVE orchestrator 把 4 agent 完整回報（~56KB 逐條軌跡）壓成
# 6KB 主題摘要存 session scratchpad（ephemeral），report §8 只留 9 行 pointer +
# 「commit 時 raw 隨 session 記錄留存」幻覺 policy — 本 gate v1 照樣 PASS（行數只 warn、
# §8 密度無檢查）。同病例：蘇打綠（及時救回）、台灣醫療與全民健保（5 份 raw 永久蒸發，
# report 自稱「永久存放於 /private/tmp」）。存 /tmp = 倒數計時的刪除佇列，不是落檔。
# 兩個合法 pattern：(1) §8 inline raw（楊德昌型）(2) §8 pointer 到 repo 內 sibling raw
# 檔（金曲獎-R1..R4 / 陳嫺靜-research-1..4 型）— 有效密度 = inline 行數 + 指向存在
# repo 檔的行數合計。指向 tmp / scratchpad = HARD FAIL（無論密度）。
S8_HEAD_RE = re.compile(r"^## 8[\.\s、]")
S8_END_RE = re.compile(r"^## (9|1[0-9])[\.\s、]")
EPHEMERAL_RE = re.compile(r"/private/tmp/claude|/tmp/claude-|scratchpad/")
S8_MDLINK_RE = re.compile(r"\(([^)\s]+\.md)\)")
S8_TICKPATH_RE = re.compile(r"`([^`\s]+\.md)`")

# ── Stage 0 觀點成型 exit gate 三件套（v7.3 — 哲宇 anti-drift 儀器化）─────────
# 抓「persona-only」drift：跑了 persona 但跳過 0.6.1 六核心問題 + 0.6.4 ≥20 探索搜尋。
VIEWPOINT_RE = re.compile(r"##+\s*.*觀點成型")
# 2026-06-14 p0-legion 校準（REFLEXES #66 gate dogfood）：原 regex 只認「20 路 persona」相鄰
# 或「persona 切入點」，漏掉 pipeline 自己的詞彙「入射角」（REWRITE Step 0.6.1-bis「撐開研究入射角」）
# + 合成報告常用的 `**personaAngles（20 路原文）**` bold marker。三者皆 legit persona section。
PERSONA_RE = re.compile(r"(##+\s*.*(20\s*路\s*persona|persona\s*(切入點|入射角))|personaAngles)", re.IGNORECASE)
FRONTMATTER_VP_RE = re.compile(r"^viewpoint_formed:\s*true", re.MULTILINE)
# 六核心問題落檔結構標記（記憶/多元面貌/想法感受/歷史脈絡/社會關聯/類型 → §觀點成型 sub-sections）
SIXQ_MARKERS = (
    re.compile(r"記憶\s*anchor|對台灣人的記憶"),
    re.compile(r"多元面貌|多元不同面貌"),
    re.compile(r"歷史脈絡"),
    re.compile(r"切入點清單"),
    re.compile(r"研究方向"),
    re.compile(r"核心矛盾候選|預期核心矛盾"),
)

TIERS = {
    # tier: (min_distinct, min_en, min_primary, min_confidence, min_lines, min_s8)
    "depth": (25, 5, 5, 8, 300, 120),
    "standard": (15, 3, 3, 4, 150, 50),
    "hub": (5, 1, 1, 0, 0, 0),
}


def analyze_s8(txt: str, report_path: Path):
    """§8 raw 有效密度 = inline 行數 + 指向存在的 repo 內 .md 檔行數合計。
    回傳 (s8_inline_lines, s8_effective_lines, ephemeral_hits, missing_pointers)。"""
    lines = txt.split("\n")
    start = end = None
    for i, l in enumerate(lines):
        if S8_HEAD_RE.match(l):
            start = i
        elif start is not None and S8_END_RE.match(l):
            end = i
            break
    if start is None:
        return 0, 0, len(EPHEMERAL_RE.findall(txt)), 0
    s8_lines = lines[start:(end or len(lines))]
    s8_txt = "\n".join(s8_lines)
    inline = len(s8_lines)
    # pointer 解析：markdown link（sibling 相對）+ backtick path（repo-root 或 sibling 相對）
    pointers = set(S8_MDLINK_RE.findall(s8_txt)) | set(S8_TICKPATH_RE.findall(s8_txt))
    effective = inline
    missing = 0
    repo_root = Path(__file__).resolve().parents[2]
    for ptr in pointers:
        if ptr.startswith("http"):
            continue
        cand = (repo_root / ptr) if ptr.startswith("reports/") else (report_path.parent / ptr)
        try:
            cand = cand.resolve()
            if cand.is_file() and repo_root in cand.parents:
                effective += cand.read_text(encoding="utf-8", errors="ignore").count("\n") + 1
            else:
                missing += 1
        except OSError:
            missing += 1
    ephemeral = len(EPHEMERAL_RE.findall(txt))
    return inline, effective, ephemeral, missing


def analyze(path: Path):
    txt = path.read_text(encoding="utf-8", errors="ignore")
    lines = txt.count("\n") + 1
    urls = [u.rstrip(".,;)。，、）]") for u in URL_RE.findall(txt)]
    distinct = sorted(set(urls))
    en = [u for u in distinct if any(h in u.lower() for h in EN_HINTS)]
    primary = [u for u in distinct if any(h in u.lower() for h in PRIMARY_HINTS)]
    confidence = len(CONFIDENCE_RE.findall(txt))
    has_searchlog = bool(SEARCHLOG_RE.search(txt))
    verif_tiers = sum(1 for r in VERIF_TIERS if r.search(txt))  # 0-3
    has_negative = bool(NEGATIVE_RE.search(txt))
    has_counterex = bool(COUNTEREX_RE.search(txt))
    # Stage 0 觀點成型 三件套 signals
    has_viewpoint = bool(VIEWPOINT_RE.search(txt))
    has_persona = bool(PERSONA_RE.search(txt))
    viewpoint_formed = bool(FRONTMATTER_VP_RE.search(txt))
    sixq = sum(1 for r in SIXQ_MARKERS if r.search(txt))
    # §8 raw 密度 + ephemeral pointer (v2)
    s8_inline, s8_effective, ephemeral, s8_missing = analyze_s8(txt, path)
    # domain diversity
    domains = set()
    for u in distinct:
        m = re.match(r"https?://([^/]+)", u)
        if m:
            domains.add(m.group(1).lower().lstrip("www."))
    return dict(
        s8_inline=s8_inline,
        s8_effective=s8_effective,
        ephemeral=ephemeral,
        s8_missing=s8_missing,
        lines=lines,
        distinct=len(distinct),
        en=len(en),
        primary=len(primary),
        domains=len(domains),
        confidence=confidence,
        has_searchlog=has_searchlog,
        verif_tiers=verif_tiers,
        has_negative=has_negative,
        has_counterex=has_counterex,
        has_viewpoint=has_viewpoint,
        has_persona=has_persona,
        viewpoint_formed=viewpoint_formed,
        sixq=sixq,
    )


def grade(metrics, tier):
    md, me, mp, mc, ml, ms8 = TIERS[tier]
    results = []
    hard_fail = 0
    warn = 0

    def simple(name, got, need, sev):
        nonlocal hard_fail, warn
        ok = got >= need
        if not ok:
            if sev == "hard":
                hard_fail += 1
            else:
                warn += 1
        results.append((name, got, f"≥ {need}", sev, ok))

    def floor_then_target(name, got, target):
        # 0 = HARD（egregious — 對應 57% 報告英文/一手來源 = 0 的系統性問題）；
        # 0 < got < target = WARN（nudge 不強迫塞 token 來源，避免懲罰正當的本土/兩岸題目）。
        nonlocal hard_fail, warn
        if got == 0:
            hard_fail += 1
            results.append((name, got, "≥ 1 (0=fail)", "hard", False))
        elif got < target:
            warn += 1
            results.append((name, got, f"理想 ≥ {target}", "warn", False))
        else:
            results.append((name, got, f"≥ {target}", "warn", True))

    simple("distinct 來源數", metrics["distinct"], md, "hard")
    floor_then_target("英文/國際/學術來源", metrics["en"], me)
    floor_then_target("一手/官方/學術來源", metrics["primary"], mp)
    simple("搜尋日誌/方法論 section",
           1 if metrics["has_searchlog"] else 0, 1, "hard")
    simple("信度三層系統 (high/single/unverified)", metrics["verif_tiers"], 2, "hard")
    simple("信度標記數", metrics["confidence"], mc, "warn")
    simple("negative findings 紀錄 (搜了沒找到)",
           1 if metrics["has_negative"] else 0, 1, "warn")
    simple("反例/不採信/護欄 section",
           1 if metrics["has_counterex"] else 0, 1, "warn")
    simple("報告行數 (SSOT 厚度)", metrics["lines"], ml, "warn")
    # v2: §8 raw 有效密度（inline + 指向存在的 repo 檔行數合計）— 摘要化 = Stage 1 未完成
    if ms8 > 0:
        simple("§8 raw 有效密度 (inline+repo pointer 行數)", metrics["s8_effective"], ms8, "hard")
    # v2: raw pointer 指向 ephemeral storage（/tmp / scratchpad）= 無論密度直接 fail
    if metrics["ephemeral"] > 0:
        hard_fail += 1
        results.append(("raw pointer 指向 ephemeral (tmp/scratchpad) — 存 /tmp = 倒數計時刪除佇列",
                        metrics["ephemeral"], "= 0", "hard", False))
    if metrics["s8_missing"] > 0:
        warn += 1
        results.append(("§8 pointer 指向不存在的檔", metrics["s8_missing"], "= 0", "warn", False))
    return results, hard_fail, warn


def grade_stage0(m):
    """Stage 0 觀點成型 exit gate — 三件套全到才進 Stage 1（哲宇 anti-drift 儀器化）。
    核心：抓 persona-only drift —— 跑了 persona 卻跳過 0.6.1 六核心問題 + 0.6.4 ≥20 探索搜尋。
    ≥10 distinct 來源是「≥20 探索真的發生」的 proxy（persona-only 只發散問題 → ~0 來源）。"""
    results = []
    hard = 0

    def chk(name, ok, detail):
        nonlocal hard
        if not ok:
            hard += 1
        results.append((name, ok, detail))

    chk("§觀點成型 section", m["has_viewpoint"], "缺 `## 觀點成型`")
    chk("frontmatter viewpoint_formed: true", m["viewpoint_formed"], "缺 `viewpoint_formed: true`")
    chk("六核心問題落檔結構 (≥4/6)", m["sixq"] >= 4, f"只有 {m['sixq']}/6 結構標記 (記憶/多元/脈絡/切入點/方向/矛盾)")
    chk("§20 路 persona 切入點", m["has_persona"], "缺 persona 切入點 section")
    chk("搜尋日誌/探索紀錄 section", m["has_searchlog"], "缺 `### 探索搜尋紀錄`")
    chk("≥20 探索搜尋 (distinct 來源 ≥10 proxy)", m["distinct"] >= 10,
        f"只有 {m['distinct']} distinct 來源 — persona-only？≥20 探索本該留 ≥10 來源")
    return results, hard


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("report")
    ap.add_argument("--tier", default="depth", choices=list(TIERS))
    ap.add_argument("--stage", choices=["0", "1"], default="1",
                    help="0 = Stage 0 觀點成型 exit gate (三件套 anti-drift); 1 = Stage 1 SSOT gate (預設)")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    p = Path(args.report)
    if not p.exists():
        print(f"❌ 找不到 research report: {p}", file=sys.stderr)
        sys.exit(2)

    m = analyze(p)

    # ── Stage 0 觀點成型 exit gate（哲宇 anti-drift：persona ≠ Stage 0 全部）──
    if args.stage == "0":
        results, hard_fail = grade_stage0(m)
        if args.json:
            print(json.dumps(dict(file=str(p), stage=0, metrics=m,
                                  hard_fail=hard_fail, passed=(hard_fail == 0)),
                             ensure_ascii=False, indent=2))
            sys.exit(0 if hard_fail == 0 else 1)
        print(f"🔬 research-report-health [Stage 0 觀點成型 exit gate]  {p}")
        for name, ok, detail in results:
            print(f"   {'✅' if ok else '🔴'} {name}" + ("" if ok else f"  — {detail}"))
        verdict = "PASS" if hard_fail == 0 else "FAIL"
        print(f"\n   Summary: hard_fail={hard_fail}  → {verdict}")
        if hard_fail:
            print("   ⛔ Stage 0 三件套未齊 = 不進 Stage 1。六核心問題 + ≥20 探索 + persona 缺一不可"
                  "（persona-only 不算 Stage 0 做完）。")
        sys.exit(0 if hard_fail == 0 else 1)

    results, hard_fail, warn = grade(m, args.tier)

    if args.json:
        print(json.dumps(
            dict(file=str(p), tier=args.tier, metrics=m,
                 hard_fail=hard_fail, warn=warn,
                 passed=(hard_fail == 0)),
            ensure_ascii=False, indent=2))
        sys.exit(0 if hard_fail == 0 else 1)

    print(f"🔬 research-report-health  {p}  (tier={args.tier})")
    print(f"   來源域名多樣性: {m['domains']} domains / {m['distinct']} URLs")
    for name, got, need, sev, ok in results:
        icon = "✅" if ok else ("🔴" if sev == "hard" else "⚠️ ")
        bar = "" if ok else f"  (需 {need})"
        print(f"   {icon} {name}: {got}{bar}")
    verdict = "PASS" if hard_fail == 0 else "FAIL"
    print(f"\n   Summary: hard_fail={hard_fail} warn={warn}  → {verdict}")
    if hard_fail:
        print("   ⛔ Stage 1 不過 = 不進 Stage 2。回去補搜尋 + 把原始搜尋軌跡寫回報告 (SSOT)。")
    sys.exit(0 if hard_fail == 0 else 1)


if __name__ == "__main__":
    main()
