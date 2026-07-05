#!/usr/bin/env python3
"""agent-report-health.py — 委派 agent 分部報告收件品質閘門（receipt gate）

姊妹儀器 research-report-health.py 驗「組裝後的主 report SSOT」；本儀器驗更上游的
「單一 agent 回來的分部報告」——orchestrator 收到 task-notification 落檔後、開始任何
合成之前跑。回答三個問題：**這份是不是壓縮過的摘要？存放位置合不合法？結構完不完整？**

誕生背景（2026-07-05 柯智棠健檢，哲宇 directive「儀器化分部報告品質硬門檻 + 通知呼叫
session 疑慮/為什麼/思考方向」）：柯智棠 EVOLVE 的 4 隻研究 agent 各回 ~20KB 逐條軌跡，
orchestrator 收到後壓成 ~6KB 主題摘要存 scratchpad，report §8 蒸發，gate v1 照樣 PASS。
同病三例（柯智棠救回 / 蘇打綠救回 / 台灣醫療 5 份 raw 永久遺失）。斷點在收件那 30 秒，
所以閘門也要站在收件那 30 秒。

閾值校準（2026-07-05 真實 corpus dogfood，REFLEXES #66）：
  該攔（orchestrator 壓縮版 aggregate ×4）: 5-6KB / 軌跡 2-9 行 / 宣稱 28-61 次搜尋
  該過（agent 真 final message ×8）:       14-38KB / 軌跡 13-62 行
  → 體積分界 8KB、軌跡分界 10 行，兩側都有 ≥2x margin

輸出 = 給呼叫 session 的疑慮通知：每條疑慮附「為什麼」+「可能的思考方向」。
stdlib-only。

用法:
  python3 scripts/tools/agent-report-health.py reports/research/2026-07/{slug}-research-A.md
  python3 scripts/tools/agent-report-health.py {file} --claimed 60     # prompt 給的搜尋配額 / agent 宣稱數
  python3 scripts/tools/agent-report-health.py {file} --min-kb 8 --min-trail 10
  python3 scripts/tools/agent-report-health.py {file} --json
退出碼: 0 = PASS, 1 = FAIL (hard 疑慮), 2 = 檔案問題, 3 = CONCERN (僅 warn 疑慮)
"""
import argparse
import json
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]

# ── 訊號 regex ───────────────────────────────────────────────────────
TRAIL_SECTION_RE = re.compile(
    r"#+\s*.*(搜尋(軌跡|紀錄|記錄|日誌)|軌跡|search\s*(log|trail)|query\s*log|逐條)", re.IGNORECASE)
TRAIL_LINE_RE = re.compile(r"^\s*(\d+[\.、]|-)\s")
CLAIMED_RE = re.compile(r"(\d+)\s*(?:次搜尋|次 web|searches|search(?:es)?\b|queries)", re.IGNORECASE)
EPHEMERAL_RE = re.compile(r"/private/tmp/claude|/tmp/claude-|scratchpad/")
URL_RE = re.compile(r"https?://[^\s\)\]\>\"'，。、；]+")
BARE_DOMAIN_RE = re.compile(r"\b[a-z0-9][a-z0-9-]*(?:\.[a-z0-9-]+)+\.(?:tw|com|org|net|cn|jp|kr|io|cc|news)\b")
EXPECTED_SECTIONS = (
    ("搜尋軌跡/紀錄", TRAIL_SECTION_RE),
    ("Findings", re.compile(r"#+\s*.*findings|#+\s*.*發現", re.IGNORECASE)),
    ("引語庫", re.compile(r"#+\s*.*(引語|verbatim|quote)", re.IGNORECASE)),
    ("negative findings", re.compile(r"#+\s*.*(negative|沒找到|查無)", re.IGNORECASE)),
    ("質地素材", re.compile(r"#+\s*.*(質地|素材|texture|給 writer)", re.IGNORECASE)),
)


def analyze(path: Path):
    txt = path.read_text(encoding="utf-8", errors="ignore")
    lines = txt.split("\n")
    size_kb = len(txt.encode("utf-8")) / 1024
    trail_lines = sum(1 for l in lines if TRAIL_LINE_RE.match(l)
                      and ("→" in l or "query" in l.lower()))
    has_trail_section = bool(TRAIL_SECTION_RE.search(txt))
    claimed_m = CLAIMED_RE.search(txt)
    claimed = int(claimed_m.group(1)) if claimed_m else None
    ephemeral = len(EPHEMERAL_RE.findall(txt))
    urls = len(set(URL_RE.findall(txt)) | set(BARE_DOMAIN_RE.findall(txt)))
    sections = [name for name, r in EXPECTED_SECTIONS if r.search(txt)]
    # 存放位置
    try:
        resolved = path.resolve()
        in_repo = REPO_ROOT in resolved.parents or resolved == REPO_ROOT
        path_ephemeral = bool(EPHEMERAL_RE.search(str(resolved))) or str(resolved).startswith(("/tmp/", "/private/tmp/", "/var/folders/"))
    except OSError:
        in_repo, path_ephemeral = False, True
    return dict(
        size_kb=round(size_kb, 1), trail_lines=trail_lines,
        has_trail_section=has_trail_section, claimed=claimed,
        ephemeral_refs=ephemeral, urls=urls,
        sections=sections, sections_count=len(sections),
        in_repo=in_repo, path_ephemeral=path_ephemeral,
        path=str(path),
    )


def grade(m, min_kb: float, min_trail: int, claimed_override):
    """回傳 concerns list。每條: (check, severity hard|warn, got, expect, why, directions[])"""
    concerns = []
    claimed = claimed_override or m["claimed"]

    if m["path_ephemeral"] or not m["in_repo"]:
        concerns.append((
            "存放位置在 repo 外（tmp / scratchpad / 其他）", "hard",
            m["path"], "repo 內（如 reports/research/{YYYY-MM}/）",
            "tmp 與 scratchpad 是倒數計時的刪除佇列。台灣醫療與全民健保的 5 份 raw 寫著「永久存放於 /tmp」，一個月後全數蒸發、無法救回",
            ["立即把檔案移入 reports/research/{YYYY-MM}/ 並納入 commit",
             "如果內容來自 task-notification，直接把 <result> verbatim 寫到 repo 路徑",
             "檢查同 session 其他 agent 的落檔位置是否同病"],
        ))
    if m["size_kb"] < min_kb:
        concerns.append((
            f"體積 {m['size_kb']}KB 低於分界 {min_kb}KB", "hard",
            f"{m['size_kb']}KB", f"≥ {min_kb}KB",
            "研究 agent 真實 final message 實測 14-38KB；orchestrator 壓縮版 aggregate 實測 5-6KB。體積落在壓縮版級距 = 這份極可能已被摘要過（柯智棠病）",
            ["回頭找 task-notification 的 <result> 原文比對長度——如果原文更長，這份是收件後壓縮版，用原文覆蓋",
             "如果 notification 也這麼短，檢查 subagent transcript（output_file symlink）撈完整 final message",
             "如果 agent 真的只回這麼少，用 SendMessage 要求 agent 補完整逐條軌跡",
             "窄子題 agent 的合法短回報可用 --min-kb 調低，但先排除前三種可能"],
        ))
    if not m["has_trail_section"]:
        concerns.append((
            "缺「搜尋軌跡」section", "hard",
            "無", "五段回報結構第一段",
            "逐條 query→發現→URL 是分部報告的骨架；缺席通常是被重新組織成主題式摘要的簽名（壓縮的第一個犧牲品就是軌跡）",
            ["確認 spawn prompt 是否要求五段結構——沒要求就是 prompt 退化，補 Step 1.8-bis 模板",
             "從 notification / subagent transcript 找原始軌跡",
             "要求 agent 重報：只補「§X 搜尋軌跡（逐條）」段即可"],
        ))
    if m["trail_lines"] < min_trail:
        concerns.append((
            f"逐條軌跡 {m['trail_lines']} 行低於分界 {min_trail} 行", "hard",
            str(m["trail_lines"]), f"≥ {min_trail}",
            "真實 final message 實測 13-62 行軌跡；壓縮版實測 2-9 行。軌跡行數是「壓縮與否」最直接的尺",
            ["同上——先驗 notification / transcript 是否有更完整版本",
             "對照宣稱搜尋數：宣稱高而軌跡少 = 壓縮或截斷的鐵證"],
        ))
    if claimed and m["trail_lines"] < claimed * 0.5:
        concerns.append((
            f"宣稱 {claimed} 次搜尋但軌跡只記錄 {m['trail_lines']} 行（{round(m['trail_lines']/claimed*100)}%）", "warn",
            f"{m['trail_lines']}/{claimed}", "≥ 50%",
            "宣稱數與記錄數的落差是三種病的共同症狀：agent 自行摘要、orchestrator 收件後壓縮、通知截斷。柯智棠 aggregate 宣稱 60 次只留 9 行（15%）",
            ["用 subagent transcript 實數 tool calls 當外部尺（REFLEXES #69），別信宣稱數",
             "落差確認後按體積/軌跡的 directions 救援"],
        ))
    if m["sections_count"] < 4:
        concerns.append((
            f"五段回報結構只偵測到 {m['sections_count']}/5（{('、'.join(m['sections']) or '無')}）", "warn",
            f"{m['sections_count']}/5", "≥ 4/5",
            "缺段可能是壓縮（negative findings 與質地素材最常被吃掉），也可能是 agent 沒照模板",
            ["對照 Step 1.8-bis 五段模板檢查缺哪段、去 notification 原文找",
             "negative findings 缺席特別危險——「搜了沒找到」的紀錄防止下輪重搜與幻覺補洞"],
        ))
    if m["ephemeral_refs"] > 0:
        concerns.append((
            f"內文引用 ephemeral 路徑 {m['ephemeral_refs']} 處", "warn",
            str(m["ephemeral_refs"]), "0",
            "分部報告內再指向 tmp/scratchpad = 又一層會蒸發的依賴",
            ["把被指向的內容也 verbatim 收進 repo，或改指 repo 內路徑"],
        ))
    if m["urls"] < 5:
        concerns.append((
            f"來源 URL/網域僅 {m['urls']} 個", "warn",
            str(m["urls"]), "≥ 5",
            "研究型分部報告每條軌跡都該帶來源；來源稀少可能是壓縮掉了，也可能該 agent 任務本來就非搜尋型（如 persona 發散）",
            ["非搜尋型 agent（persona / writer / verifier 回報）本檢查可忽略",
             "搜尋型 agent 來源少 → 回 notification 原文找被刪的 URL"],
        ))
    return concerns


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("report")
    ap.add_argument("--claimed", type=int, default=None,
                    help="prompt 配額 / agent 宣稱的搜尋數（不給則從內文 parse）")
    ap.add_argument("--min-kb", type=float, default=8.0)
    ap.add_argument("--min-trail", type=int, default=10)
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    p = Path(args.report)
    if not p.is_file():
        print(f"❌ 找不到分部報告: {p}", file=sys.stderr)
        sys.exit(2)

    m = analyze(p)
    concerns = grade(m, args.min_kb, args.min_trail, args.claimed)
    hard = sum(1 for c in concerns if c[1] == "hard")
    warn = sum(1 for c in concerns if c[1] == "warn")
    verdict = "FAIL" if hard else ("CONCERN" if warn else "PASS")

    if args.json:
        print(json.dumps(dict(
            file=str(p), metrics=m, verdict=verdict, hard=hard, warn=warn,
            concerns=[dict(check=c, severity=s, got=g, expect=e, why=w, directions=d)
                      for c, s, g, e, w, d in concerns]),
            ensure_ascii=False, indent=2))
        sys.exit(0 if verdict == "PASS" else (1 if verdict == "FAIL" else 3))

    print(f"🔬 agent-report-health  {p}")
    print(f"   {m['size_kb']}KB / 軌跡 {m['trail_lines']} 行 / 來源 {m['urls']} / "
          f"結構 {m['sections_count']}/5 / 宣稱搜尋 {args.claimed or m['claimed'] or '—'}")
    if not concerns:
        print("   ✅ 無疑慮：體積、軌跡密度、結構、存放位置皆在真實 final message 級距")
    for check, sev, got, expect, why, directions in concerns:
        icon = "🔴" if sev == "hard" else "⚠️ "
        print(f"\n   {icon} [{check}]")
        print(f"      為什麼：{why}")
        print(f"      思考方向：")
        for i, d in enumerate(directions, 1):
            print(f"        ({i}) {d}")
    print(f"\n   Verdict: {verdict}  (hard={hard} warn={warn})")
    if verdict == "FAIL":
        print("   ⛔ 收件不合格 = 不准開始合成 §6 / 不進 Stage 2。先照思考方向救回 raw。")
    elif verdict == "CONCERN":
        print("   🟡 可續行，但每條疑慮需在 orchestrator 回報裡明示處置（採信 / 救援 / 忽略理由）。")
    sys.exit(0 if verdict == "PASS" else (1 if verdict == "FAIL" else 3))


if __name__ == "__main__":
    main()
