"""prose_health — consolidated prose quality checks.

Migrated from `scripts/tools/quality-scan.sh` (16 dims) +
`scripts/tools/check-manifesto-11.sh` (3 tiers) into a single SSOT plugin.

Canonical:
  - quality-scan: docs/editorial/EDITORIAL.md §quality-scan 偵測指標
  - manifesto-11: docs/semiont/MANIFESTO.md §11 書寫節制

Ports the most actionable dimensions:

quality-scan dims:
  1. bullet density           7. repeated bullet blocks    13. (THIN — deferred)
  2. year count               8. plastic phrases (5 variants + extras)
  3. URL count               8b. em-dash overuse
  4. hollow words             8c. 全形分號「；」density (2026-07-19 哲宇, scored)
  5. (prose lines — deferred) 8d. run-on 長句 / 辭藻湯 (2026-07-19, WARN-only)
  6. lastHumanReview          8e. 英文式短句開場 (2026-07-19, WARN-only)
                              9. textbook opening
                             10. formulaic ending
                             11. template H2

2026-07-19 哲宇 directive (高速公路.md live review) 新增三 dim + Tier1 一變體：
  - §8c 全形分號：繁中散文水印，翻譯腔。scored（只在 rewrite-stage-3 咬）。
  - §8d run-on 長句：≥62 字 + ≥8 停頓 = 沒呼吸的辭藻湯。WARN-only soft-launch。
  - §8e 英文式短句開場：≤8 字平述句（。結尾、無數字）+ 接長句 = topic-sentence 腔。
    排除設問（？）與具體場景句。WARN-only soft-launch。corpus 校準見
    reports/prose-instrument-upgrade-2026-07-19.md。**2026-08-19 v3 升計分**（≥3 處 +1、
    ≥6 處 +2）：第二帶判準從「句首定調詞」改為「宣告型謂語且無事件體標記」、量整段展開，
    哲宇同日兩次點名同一篇文章的英式開場而 v2 報 0，校準數字見常數區註解。
  - Tier1 補「強加對比收束句」：根本是兩件事 / 兩本帳 / 不同的語言（散文對位變體）。
                             12. (LIST-DUMP — deferred)
                             14. (QUALITY-DECAY — deferred)
                             15. (CHINA-TERM — deferred to terminology plugin)
                             16. citation desert

manifesto-11 tiers:
  Tier 1: 11 「不是X是Y」 對位句型 variants + em-dash density
  Tier 2: 30+ AI 抽象 metaphor 詞 + 「重」當抽象份量隱喻 (warn ≥ 2 total)
  Tier 3: 17 AI ritual 語 (warn ≥ 1 occurrence)

§盼望而不粉飾 §自稱 (2026-06-15 哲宇 directive — MANIFESTO §跟台灣的關係 §自稱):
  - 島嶼自稱密度: 「這座島 / 這個島嶼」當台灣的迴避稱呼 (balance not ban，ratio-based:
    島佔「島+台灣」國名指稱 > 1/4 且 ≥ 3，或完全不稱台灣才 WARN，不罰文學用法)。WARN 級。

  (PUA 體 / 媒體焦慮體 偵測器於 2026-06-15 evaluation 後移除：四 subagent + 全 corpus
   814 篇驗證顯示 92-100% 假陽性 — 抓到第三方/引用/腳註新聞標題/文章正在批判的詞/正向用法。
   PUA 與媒體焦慮是「對誰施壓 / 是否販賣恐懼」的語意判斷，不是句法特徵，regex 結構上做不到。
   改由 EDITORIAL §六 對照表 + §五 結尾判準句的人工判斷接管。)

Total score budget: ≤ 3 = pass (per QUALITY-CHECKLIST §四 + REWRITE-PIPELINE).
A "score" violation is yielded with the running total — the runner can
gate on this via profile.fail_on = "score-budget".

Budget is configurable per-profile via `options.score_budget` (int, default
3) — read by article-health.py's score-budget gate (scripts/tools/
article-health.py::_resolve_score_budget). 2026-07-16: added so profiles
whose文體 structurally trips other dims (e.g. `memory-diary`: checklist/
handoff lists trip LIST-DUMP/THIN, no footnotes required) can raise the
pass threshold without changing the default zh-TW knowledge/ budget of 3.

2026-09-05 哲宇拍板 OBSERVER-QUEUE #24 選 B（超越單純調高 budget）：
`options.exclude_dimensions` (list[str]) 讓 profile 整組關掉特定維度的
score 貢獻，而不是墊高 budget 讓灌水混過。目前支援排除的維度 id：
"no-url" (§3 URL count) / "LIST-DUMP" (§12) / "THIN" (§13) /
"citation-desert" (§16)。`memory-diary` profile 排除這四個「文章向」維度
（checklist/handoff 清單結構天生觸發，不是灌水），score_budget 因此收回
跟 knowledge/ 一致的預設 3——量錯維度用排除修正，不是挪高及格線讓單薄
內容也能過關。未設定 exclude_dimensions 的 profile（release-pr/ci-deploy/
pre-commit/dashboard）行為不變。

AI 痕跡 Tier 4 (speak-human-tw 轉譯, 2026-07-16 soft-launch):
  (a) 立場真空 (stance-vacuum)      (d) 時代帽子開場 (time-hat opening)
  (b) 價值上升詞密度 (value-inflation) (e) 假推論密度 (「這意味著」)
  (c) 罐頭結尾起手式 (canned-ending)   (f) 首先/其次/最後 三件套
  全部併入 score budget（跟 quality-scan §1-16 一致，不是另開 WARN-only
  bucket像 §11 Tier 1-3 / §自稱）。權重是初次校準值，非最終定案 — 見各
  常數旁註解。

Deferred to Phase 4b (need more structural parsing):
  - LIST-DUMP: bullet ratio per file half
  - THIN: prose lines per H2 section
  - QUALITY-DECAY: prose ratio front vs back
  - CHINA-TERM: requires data/terminology TSV files (separate plugin)
"""

from __future__ import annotations
import re
from typing import Any, Iterator

from ..types import FileTarget, Severity, Violation


CHECK_NAME = "prose-health"
DIMENSION = "prose-quality"
DEFAULT_SEVERITY = Severity.WARN
EDITORIAL_REF = "EDITORIAL.md §quality-scan + MANIFESTO.md §11"
APPLIES_TO = ["zh-TW"]


# ── Plastic phrases (quality-scan §8) ────────────────────────────────────────
_RE_PLASTIC = re.compile(
    r"不僅.{0,8}更是|不只.{0,8}也是|不是.{0,8}而是|"
    r"展現了.{0,8}的精神|展現.{0,8}的決心|體現了.{0,8}的精神|"
    r"扮演著.{0,10}角色|發揮著.{0,10}作用|見證了.{0,10}的歷程|"
    r"彰顯了|承載著.{0,10}的|不僅僅是.{0,10}更是|"
    r"既是.{0,8}也是.{0,8}更是|成為.{0,8}的重要.{0,6}|"
    r"為.{0,10}注入.{0,8}活力|為.{0,10}奠定.{0,8}基礎|"
    r"在.{0,10}上扮演.{0,8}角色|為.{0,10}提供了.{0,8}動力|"
    r"開啟了.{0,8}的新篇章|翻開.{0,8}的新頁|書寫.{0,8}的篇章|"
    r"譜寫.{0,8}的華章|綻放.{0,8}的光芒|閃耀.{0,8}的光輝"
)

# ── Hollow words (quality-scan §4) ───────────────────────────────────────────
_RE_HOLLOW = re.compile(
    r"重要的|顯著的|豐富的|完整的|多元的|"
    r"積極|蓬勃發展|逐步|逐漸|不斷|持續|"
    r"日益|進一步|全面|深入|大力|有效|顯著|穩步"
)

# ── Em-dash (manifesto-11 [9-10] / quality-scan §8b) ─────────────────────────
_RE_EMDASH = re.compile(r"——")

# ── 中文字元計數（開場短句 / 長句判定用）─────────────────────────────────────
_CJK_CHAR = re.compile(r"[一-鿿]")

# ── 全形分號「；」(quality-scan §8c，2026-07-19 哲宇 directive) ────────────────
# 繁中自然散文極少用全形分號。它是翻譯腔 / 學術腔的水印：作者把英文一個帶 ';' 的長句
# 直譯過來，或把「該用句號斷成兩句」「該用頓號列舉」的並列子句硬用；接起來，讀起來像
# 論文或法律條文而不像人話。自然中文做法：句號（。）斷句、頓號（、）列舉。合法殘餘
# （引用官方 / 法律原文、腳註分隔多來源）用「排除腳註行 + ≤3 免計」兜住，不追殺文學例外。
_RE_SEMICOLON = re.compile(r"；")

# ── 英文式超短句開場（歐化語法，2026-07-19 哲宇 directive）────────────────────
# 哲宇 anti-example：「協議並沒有收尾。自救會指控補償被打了六、七折…」——段落以一句
# 超短陳述（≤ 10 字）開頭，緊接一句長得多的句子。這是英文 topic-sentence / punchy
# lead 的腔調（先甩一句短的定調，再展開），中文自然行文會直接流進主題，不會孤立一個
# 四五字的短句當引子。判準刻意排除「整段只有一句短句」的電影感過場句（那是另一種手法，
# 不在此 detector 打擊範圍）——只抓「短開場 + 同段接長句」這個 English structure 指紋。
# 門檻經 2026-07-19 全 corpus 853 篇校準：初版 (≤10/≥15/2×) 誤報 58%（哲宇 anti-example
# 只是最極端一種，中文正常段落也常見中短句開頭）。收緊到 ≤8 字開場 + 後接 ≥28 字 + ≥3.5×
# 落差，把打擊面收到「真的甩一句超短定調再長篇展開」的英文 topic-sentence 指紋。
_ENGLISH_OPENER_MAX_CHARS = 8    # 開場句中文字數 ≤ 此值才算「超短」
_ENGLISH_OPENER_NEXT_MIN = 28    # 後接句中文字數 ≥ 此值（確保是「短→長」不是「短→中」）
_ENGLISH_OPENER_RATIO = 3.5      # 後接句 ≥ 開場句的幾倍

# 第二帶（2026-08-04 哲宇 directive「段落前面出現短句也應該檢查」）：9-14 字的段首
# 短句加「宣告型指紋」二次過濾才報——直接把門檻拉到 12 全站爆 1025 hits / 443 篇，
# 大量是健康的中文短句節奏（「他愣了三秒。」「他叫辯士。」）。round 2 病例的共同指紋
# 是宣告不是短：「這個頭銜在轉述裡長大過」（這個＋隱喻斷言）「從結果看，這是⋯」。
# 指紋 = 句首「這/那/真正/從結果/但」類定調詞（場景短句「博士之後他去了巴黎」放行）。
_ENGLISH_OPENER_BAND2_MAX = 15   # 第二帶上限（2026-08-19 14→15：「所以文章真正的本體是那份研究報告。」15 字）
_RE_OPENER_DECLARATIVE_LEAD = re.compile(
    r"^(?:這(?:個|些|種|是|一切|兩件事)?|那(?:個|些|種)?|真正|從結果|但|所謂)"
)
# 第二帶 v3（2026-08-19 哲宇 directive「文章裡面還是有很多英文短句在開頭殘留」，點名
# 「這些翻譯很多是在我家跑的。」「純粹之後才輪到後面那一段。」）：v2 的兩個門檻讓第二帶
# 名存實亡——(a) 句首定調詞清單太窄：「純粹之後⋯」「寫完之後⋯」「搬家日記是⋯」「維基百科上
# 也⋯」全是宣告句卻不以 這/那/真正 起頭；(b) 3.5× 落差對 12 字開場要後接 ≥42 字，正常展開
# 句 30-40 字永遠搆不到。實測：今天那篇改稿前 15 處人眼認定的英式開場，v2 報 0。
# v3 判準：宣告型 = 句首定調詞 **或**（謂語帶判斷／存在／能願／副詞定調：是/有/叫/可以/都/
# 也/很/一直/就/才/在⋯的/得到 **且** 不帶事件體標記 了/著/過/起來/出來/下去/進去/回來），
# 後接改量「段落剩餘 ≥40 字」（不只下一句），落差降到 1.5×。冒號收尾與含引號的開場句豁免
# （那是引語／列舉的引子，中文本來的寫法）。
# 校準（2026-08-19，983 篇 zh corpus）：v2 744 hits／403 篇 → v3 2,133 hits／650 篇；
# 新增命中抽樣 45 條人眼判：「市場太小是結構性問題。」「日本是他們的第二個家。」「語言也是
# 閃靈的聲音核心。」這類判斷句主題句佔絕大多數，場景句（「那天是他的最後一堂課。」）約
# 一成。今天那篇改稿前 15 處 v3 抓 11。放寬是刻意的：哲宇要的是嚴格執行，這條從 WARN-only
# 升為計分項（見 check() §8e）。
_ENGLISH_OPENER_BAND2_REST_MIN = 40   # 第二帶：段落剩餘中文字數 ≥ 此值
_ENGLISH_OPENER_BAND2_RATIO = 1.5     # 第二帶：下一句 ≥ 開場句的幾倍（放寬自 3.5）
_RE_OPENER_STATIVE = re.compile(r"(?:是|有|叫|可以|都|也|很|一直|就|才|在.{0,8}的|得到)")
_RE_OPENER_EVENT = re.compile(r"(?:了|著|過|起來|出來|下去|進去|回來)")

# ── 「是⋯的」cleft 長片語型（§歐化第 7 病動詞片語變體，2026-08-04 哲宇 directive）──
# 第 7 病 plugin 抓 curated 評價形容詞（「是隨便的」「是顯而易見的」）；哲宇 callout
# 「『腦神經外科』這四個字，是媒體多年轉述之間慢慢添上去的。」揭另一型：「是＋長動詞
# 片語＋的＋句末標點」的英文 cleft 直譯。短的「是他蓋的」是中文自然強調式，病的指紋
# 是「是」與「的」之間塞了長片語（資訊全部懸在判斷句裡）。中文紀實把動作句直接寫出來
# （「媒體多年轉述之間，慢慢把這四個字添了上去」）或讓「的」接名詞（「是⋯添上去的頭銜」）。
# 891 篇校準：minlen=10 → 129 hits、minlen=12 → 71 hits。⚠️ 出處交代型（「是徐賢修
# 拍板的」「是許皓甯在台上說的」）是合法強調句，句法上與 cleft 無法完全區分——本組是
# 意識層儀器（MANIFESTO §14：儀器篩選標記、判斷裁決），WARN-only 讓寫手看見，逐處人判。
# 含數字片語豁免（出處型常帶人名年份；同 §8e 場景句豁免邏輯）。
_RE_CLEFT_LONG_PREDICATE = re.compile(
    r"是[^。！？\n，、「」0-9０-９]{12,25}的[。！？]"
    # 「是從⋯V出來的」狀語型 cleft：門檻可低（6 字），出處交代型罕用「從」開頭
    # （2026-08-04 dogfood：自己的 diary 寫出「尺是從被照亮的地方長出來的。」10 字
    # 溜過 12 字門檻，哲宇 callout「diary 有一樣的問題」）
    r"|是從[^。！？\n，、「」0-9０-９]{6,22}的[。！？]"
)

# ── 英式段首宣告慣用式（§8e 的簽名檔補充，2026-08-03 round 2）─────────────────
# §8e 的長度門檻（≤8 字）與數字豁免讓三種 9-13 字的隱喻宣告句穿過：「這個頭銜在轉述裡
# 長大過。」（10 字）「真正的轉彎發生在 1987 年。」（數字豁免）「從結果看，這是他人生的
# 第一場賭。」（14 字）。一般形（任意短宣告句）語意判斷 regex 做不到——場景句「那是一個
# 耶誕夜。」跟宣告句句法相同；改抓具名慣用式：「真正的[轉X]發生在／出現在」全 corpus
# 878 篇有 9 篇在用，是跟「值得停下來看」（22 篇）同型的跨篇簽名檔——每篇單獨看是一句
# 過場，攤開看是模板。段首限定（MULTILINE ^）。
_RE_DECLARATIVE_OPENER_IDIOM = re.compile(
    r"^(?:真正的[^。！？\n]{1,8}(?:發生在|出現在|來自|集中發生在|在)"
    r"|(?:真正的)?(?:轉機|轉折|轉捩點|終局|轉彎|轉身)[^。！？\n]{0,6}?(?:出現在|發生在|在)[^。！？\n]{1,12}[。]"
    r"|最(?:深|大|難|重)的[^。！？\n]{1,8}(?:在|是)[^。！？\n]{1,12}[。]"  # 最高級宣告型（08-04 diary dogfood）
    r"|從結果(?:看|來看)[，,]\s*這是)",
    re.MULTILINE,
)

# ── 長句 / 華麗辭藻湯（quality-scan §8d，2026-07-19 哲宇 directive）────────────
# 哲宇：「有些段落切得太長，語感不順，看起來像是華麗的辭藻湯」。機械 proxy：單一句子
# （。！？之間）塞太多逗號 / 頓號 / 分號子句又太長 = 沒有呼吸的 run-on，讀起來像堆疊
# 修飾語的湯。soft-launch WARN，門檻抓得保守（同時超過長度 + 停頓數才報）避免誤殺
# 正常敘事長句。
# 門檻經 2026-07-19 corpus 校準：55字/7停頓誤報偏多（37%，多為正常敘事長句）。
# 收到 62字 + 8停頓，聚焦真正沒呼吸的辭藻湯。WARN-only（不計分）故寬鬆代價低，但仍收緊減噪。
_RUNON_MIN_CJK = 62       # 句子中文字數 ≥ 此值
_RUNON_MIN_PAUSES = 8     # 句內停頓（，、；）數 ≥ 此值

# 歐化「(不)是 X 的」判斷句 (余光中〈中文的常態與變態〉)：是/不是 + 評價形容詞 + 的 + 句末標點。
# 自然中文直接讓形容詞當謂語：「這個選址不隨便」優於「這個選址不是隨便的」。2026-06-07 哲宇
# directive 加入 (live review 複雜生活節「這個選址不是隨便的」)。curated 評價形容詞 list +
# 的後接標點 lookahead，避開合法的「是…的」(是我的 / 是紅色的 / 是教書的 / 是昨天來的)。
_EURO_DE_ADJ = (
    "隨便|必然|偶然|明顯|顯而易見|理所當然|合理|正確|錯誤|重要|必要|多餘|困難|容易|"
    "普遍|常見|罕見|獨特|特別|相同|一致|值得|危險|公平|刻意|足夠|充分|有限|徒勞|"
    "空洞|脆弱|致命|關鍵|根本|主觀|客觀|清楚|模糊|完整|完美|理想|樂觀|悲觀"
)
_RE_EURO_DE = re.compile(rf"不?是(?:{_EURO_DE_ADJ})的(?=[。，！？、；：」』）\s])")

# ── Manifesto §11 Tier 1: 不是X是Y 對位句型 變體 ───────────────────────────
# Tightened versions of patterns from check-manifesto-11.sh.
# 2026-05-09 brave-kirch: 加 antithesis-bare 抓最普遍的「不是 X，是 Y」
# (X 跟 Y 都不超過 30 字、結尾是純「是」不要求「而是 / 也是 / 更是」)。
# 哲宇 EDITORIAL v6.0 self-check 揭露 plugin 漏抓 16+ 處對位句型。
_TIER1_PATTERNS = [
    # 既有 11 patterns (require explicit antithesis tail)
    re.compile(r"不是.{0,30}[，,]\s*而是"),  # cross-comma
    re.compile(r"這不是.{0,15}是"),
    re.compile(r"不只是.{0,15}是"),
    re.compile(r"不再是.{0,15}是"),
    re.compile(r"不僅.{0,15}更是"),
    re.compile(r"不只.{0,15}也是"),
    re.compile(r"不是.{0,8}而是"),
    re.compile(r"不僅僅是.{0,10}更是"),
    re.compile(r"既是.{0,8}也是.{0,8}更是"),
    re.compile(r"從.{2,15}到.{2,15}[，,]\s*從.{2,15}到"),
    re.compile(r"與其說.{0,15}不如說"),
    # NEW (2026-05-09): bare antithesis 「不是 X，是 Y」 / 「不是 X 是 Y」
    # X 1-30 字 (no 是 inside to avoid match overlap); Y 1-30 字
    re.compile(r"不是[^是\n]{1,30}[，,]\s*是[^，,。\n]{1,30}"),  # 不是 X，是 Y
    # NEW: 「不只 X，更 Y」「不只是 X，也 Y」「並非 X，而是 Y」 系列
    re.compile(r"不只[^更也\n]{1,30}[，,]\s*更"),
    re.compile(r"不只是[^也還\n]{1,30}[，,]\s*(也|還)"),
    re.compile(r"並非[^而\n]{1,30}[，,]\s*而是"),
    re.compile(r"並不[^而是\n]{1,30}[，,]\s*而是"),
    # NEW (2026-08-03 round 2): 「不在 X，在 Y」變體——無「是」字所以既有 patterns 全漏。
    # 「差別不在錢，在他怎麼定義⋯」891 篇校準 9 hits（差別不在錢/算力/白/牛肉/數據、
    # 問題不在框架、關鍵不在財務崩盤⋯）。三題判準同 §11.1：讀者真的會預設「差別在錢」嗎？
    # 不會 = 稻草人前設 = 重寫成正面斷言。
    # ⚠️ 刻意不含「而在」尾（「重點不在於技術，而在於模式」是傳統中文學術修辭，891 篇
    # 39 hits 多為正當用法）——只抓省略「而」的壓縮口語型，那才是 AI 對位腔的指紋。
    re.compile(r"(?:差別|差異|問題|重點|關鍵)不在[^，。！？\n]{1,12}[，,]\s*在"),
]

# ── §11 Tier 1 補：強加對比的收束句（2026-07-19 哲宇 directive）───────────────
# 對位句型的散文變體：不是「不是 X 是 Y」的句型，而是段末 / 節末拿一個抽象對比當
# 結論——「（大眾直覺與官方統計）量的根本是兩件事」「（兩邊講的）根本是不同的語言」
# 「這條路的兩本帳，從來沒有攤開在同一頁上」。tell 是「根本是 …兩件事 / 兩回事 /
# 不同的 X」「兩本帳」「沒攤開在同一頁」這種把並列的兩者硬拗成「其實是兩種東西」的
# essay 收尾腔。跟「兩件事」裸詞不同（「這篇要做兩件事」「相隔半年的兩件事」是實指，
# 不抓）——只抓「根本是 / 其實是 + 兩件事 / 不同的」與「兩本帳 / 同一頁」高精度變體。
_RE_FORCED_CONTRAST_CLOSER = re.compile(
    r"(?:根本|其實|說到底|講的|量的|要的|問的)(?:是|上是|其實是)?[^，。！？\n]{0,10}"
    r"(?:兩件事|兩回事|兩碼事|不同的(?:語言|東西|世界|邏輯|事|概念))"
    r"|(?:兩|另一)本帳"  # 2026-08-03 round 2: 「還有另一本帳」= another ledger 英文隱喻直譯
    # 2026-08-04 EZWAY vc=2：「誰來把帳算完」「這筆帳是有人在問了」= settle the
    # account 直譯。中文「算帳」是報復或記帳，不當公共問責的隱喻用。896 篇校準
    # 0 hits（EZWAY 已修）。「秋後算帳」語序不同不誤中。
    r"|把帳算完"
    r"|(?:這|那)筆帳[^，。！？\n]{0,10}(?:有人[在]?問|沒人問|誰來問)"
    r"|(?:從來)?(?:沒有|沒|未曾|不曾)[^，。！？\n]{0,8}(?:攤開|放|擺)[^，。！？\n]{0,6}同一(?:頁|張|條|個)"
)

# ── Manifesto §11 Tier 2: AI 抽象 metaphor 詞 ────────────────────────────────
_TIER2_WORDS = [
    "重量", "縮影", "軌跡", "弧線", "DNA", "基因",
    "土壤", "養分", "血液", "縫隙", "皺褶", "肌理", "織就",
    "指紋", "神經末梢", "肌肉記憶", "基底", "底色",
    "張力", "光譜", "鏡子", "承載著", "形塑", "鬆動",
    "展演", "召喚", "凝視", "直面", "直擊",
    "鋪陳", "醞釀", "沈澱",
]

# ── §11 Tier 2 補：「重」當抽象份量隱喻 (2026-06-04 哲宇 callout) ──────────────
# AI 很愛把「意義/份量/重要性」寫成物理上的「重」(很重 / 最重的一刻 / 沉重 /
# 份量很重)。是 Tier 2 metaphor 的高頻變體，但「重量」靜態詞 catch 不到、又不能
# 用裸 substring「很重」(會誤殺「很重要/很重視/很重大」)。用 regex + 負向預看
# 排除常見複合詞，逐處 WARN + 計入 Tier 2 密度。口語替代：把抽象的「重」改成具體
# 後果或畫面 (「最重的一刻」→「最不敢忘的一刻」/ 直接寫那一刻發生什麼)。
_RE_WEIGHT_METAPHOR = re.compile(
    r"(?:很|最|更|太|格外|分外|這麼|那麼|如此|越來越|愈來愈|沉甸甸地?)重"
    r"(?!要|視|新|複|建|點|申|組|演|置|逢|疊|整|大|心|力|機|金|傷|病|罪|刑|兵|鎮"
    r"|工|劃|唱|奏|圍|彈|操|播|映|審|提|溫|現|生|用|返|犯|劑|物|量|罰|稅|賞|創)"
    r"|[沉沈]重(?!澱)"
    r"|份量|分量"
)

# ── Manifesto §11 Tier 3: AI ritual 語 ───────────────────────────────────────
_TIER3_PHRASES = [
    "在這個意義上", "從某種意義上", "就此而言", "換言之",
    "值得我們深思", "值得我們反思", "拭目以待", "不容忽視",
    "不可或缺", "不可磨滅", "影響深遠", "歷久彌新",
    "並非偶然", "耐人尋味", "不言而喻", "不可言說", "無以名狀",
]

# ── §後台洩漏 backstage leak (2026-08-03 哲宇 directive) ──────────────────────
# canonical: EDITORIAL §六 §後台洩漏。抓「作者的工作痕跡跑進成品」——句子本身有內容、
# 不空洞、不歐化，過得了前面所有關卡，壞在說話對象錯了（說給編輯/查核者/作者自己聽，
# 不是說給讀者聽）。全 WARN、不計 score（soft-launch，跟 §11 Tier 1-3 一致）。
#
# 四類裡只有 (b)(d) 有乾淨的句法指紋，(a)(c) 是語意判斷——依 PUA/媒體焦慮偵測器被移除
# 的教訓（語意判斷 regex 做不到，92-100% 假陽性），這裡只收最窄的字面指紋，其餘交給
# EDITORIAL §後台洩漏 的人眼判準（「這句話在跟誰說話」）。寧可漏抓不可哭狼（REFLEXES #24）。

# (a) 分析框架洩漏：用語法/文體術語描述真實人事物。
# 「兩件事的動詞不一樣，判斷是同一套」——沒有讀者在讀一個人的收藏時會想到「動詞」。
# 878 篇校準：初版含「變成」誤報 4/5（「把設計從展場名詞變成日常動詞」是有意識的修辭、
# 「化學名詞變成全民動作」的「名詞」是實指名稱、編輯教學文合法討論「主詞換成」）。
#
# ⚠️ 本類另有兩種形狀 regex 抓不到，交 EDITORIAL §後台洩漏 人眼判準（2026-08-03 實測）：
#   - 指涉語法回指（「前者可以等，後者必須動手」）：878 篇 38 hits，逐條看絕大多數是
#     正當對比——「前者是壓制，後者是收編」指涉的是文中已存在的兩個真實事物，而哲宇
#     callout 的那句指涉的是作者剛造出來的抽象對比。差別在指涉對象是文中實體還是作者
#     的論述動作，這是語意判斷。
#   - 對稱宣告（「這兩件事完全不同」）：同上，跟正當的比較句無法用句法區分。
# 硬收會複製 PUA／媒體焦慮偵測器被移除的錯誤（92-100% 假陽性）。寧可漏抓不可哭狼。
_RE_BACKSTAGE_GRAMMAR_META = re.compile(
    r"(?:動詞|受詞|句型|語法|修辭)(?:不一樣|不同|是同一|一樣)"
)

# (e) 指揮讀者注意力：作者跳出來告訴讀者「現在該注意這個」。
# 「這裡有一個細節值得停下來看」「這句話值得放在千億債務的旁邊一起讀」——好的散文
# 讓材料自己有份量，不需要導遊舉旗。
# 878 篇校準：裸抓「值得停下來」「值得記住」誤報 39 hits（跟「值得一提的是」同性質，
# 是中文常見過場語，論述文的正當結構）。收緊為只抓帶完整指揮動作的句式——要求作者
# 指定「停下來看什麼」或「跟什麼放一起讀」，那才是導遊舉旗而非過場。
_RE_BACKSTAGE_READER_DIRECTION = re.compile(
    r"值得(?:先)?(?:停下來(?:看|讀|想)|放在[^。！？\n]{0,14}一起(?:讀|看))"
    r"|(?:這裡|這邊)有(?:一個|一段|一條)[^。！？\n]{0,12}值得(?:停下來|放在|先)"
    r"|(?:先|請)記住(?:這|那)(?:一)?(?:句|點|個|段)[^。！？\n]{0,10}[，,。]"
    r"|讀到這裡[^。！？\n]{0,8}(?:可以|不妨|請)"
)

# (b) 寫作動機洩漏：段落開頭宣告「這一段要做什麼」。
# 「要說清楚回來的是什麼樣的公司。」——投影藍圖給寫手的指令被照抄進正文。
# 高精度：自然中文敘事不會這樣起手（這是簡報/論文的過場語）。
# 878 篇校準：初版含「值得一提的是」誤報 25/25（它是中文常見過場語，性質接近 §11 Tier 3
# ritual 語而非指令複讀，25 篇在用；全 flag 會製造噪音、哭狼）。移除該 pattern，只留
# 真正的「把寫作指令照抄進正文」——投影藍圖的全局功能描述被寫手當成句子。
_RE_BACKSTAGE_WRITING_INTENT = re.compile(
    r"(?:^|[。！？\n])\s*(?:"
    r"(?:要|先|得)(?:先)?說清楚[^。！？\n]{0,20}[。：]"
    r"|(?:這裡|這邊|此處)(?:必須|得|要)(?:先)?(?:交代|說明|補充)"
    r"|先(?:說|講|交代|處理)[^。！？\n]{0,12}[，,][^。！？\n]{0,6}再(?:說|講|回到|處理)"
    r"|這一(?:段|節)(?:要|想|得)(?:說|講|處理|回答)"
    r")"
)

# (c) 自我評價洩漏：作者稱讚自己的處理方式。
# 「這一段誠實的空白值得留著。」——「誠實」「值得留著」是作者在評自己有好好處理
# negative finding。窄化：只抓「指涉文章自身的名詞 + 值得/誠實」的搭配。
_RE_BACKSTAGE_SELF_PRAISE = re.compile(
    r"(?:誠實的(?:空白|留白|缺口|沉默))"
    r"|(?:這(?:一)?(?:段|節|句|處)[^。！？\n]{0,8}值得(?:留著|保留|留下|寫下來))"
    r"|(?:空白|缺口|沉默)[^。！？\n]{0,6}值得(?:留著|保留|留下)"
)

# (d) 查證過程洩漏：把「媒體轉述的分歧」攤在正文再分析一輪。
# 「這句話有兩個版本在流傳，另一家媒體的版本沒有『不用擔心』四個字。」
# 正文要嘛用認定版本的逐字、要嘛不用；分歧進腳註。
# 878 篇校準：初版裸抓「有兩個版本」誤報 9/10——作品版本（周蕙〈約定〉粵語/國語、
# 康士坦 MV 兩版）、民間傳說版本（連江媽祖）、史實爭議（珍奶起源春水堂 vs 翰林）、
# 災難統計分歧（南投 921 死亡數，且已用 ⚠️ callout 正當揭露）全部是正當內容。
# 真陽性的特徵是指涉「**一句話／說法**的媒體轉述版本」，不是作品或傳說的版本。
# 收緊為只抓明確指向媒體轉述分歧的三種寫法。
_RE_BACKSTAGE_VERIFICATION = re.compile(
    r"這(?:句話|段話|個說法)[^。！？\n]{0,10}(?:有|流傳著?)(?:兩|三|多|不只一)個版本"
    r"|另一(?:家|篇|份)(?:媒體|報導|報紙)[^。！？\n]{0,12}版本"
    r"|(?:各家|不同)(?:媒體|報導)[^。！？\n]{0,8}(?:說法|版本)(?:不一|有出入|有落差)"
    r"|無論哪(?:一)?個版本"
    # 「沒有一家媒體去交叉印證另一家」——查核員在描述自己的比對工作（2026-08-04
    # EZWAY 哲宇 callout）。896 篇校準 0 hits，高精度。正文只該給結論（三種算法
    # 對不起來），比對過程進腳註。
    r"|沒有一家媒體[^。！？\n]{0,14}(?:交叉印證|印證|核實|查證)"
)

# (f) 查無聲明：查證的「查無」結論用研究者視角的語言寫進正文（2026-08-03 round 2，
# 哲宇 13 段殘留裡的最大宗，5 例）。「中英文檔案裡找不到任何一件訴訟紀錄」「沒有銀行團
# 或監理機關的獨立版本可以對照」「沒有公開材料可以判斷」——這是查核員報告搜尋範圍與
# 信度分層的語言。兩例（黃崇仁 [^31][^40]）腳註裡早有同一句話，正文是重複求安心。
# 改法三徑：刪／降級進腳註或策展人筆記（後台的兩個合法的家）／視角翻轉（「我查不到」
# 改寫成「誰沒有說」）。canonical: EDITORIAL §後台洩漏 形狀七。
#
# ⚠️ 本組必須跳過 blockquote 與腳註定義行（_backstage_line_is_legit_backstage）：
# 策展人筆記與腳註正是查無聲明該住的地方——醫療法「找不到任何一份⋯」寫在 📝 筆記裡
# 是正確示範，罰它等於罰紀律的正確表達。
_RE_BACKSTAGE_NEGATIVE_EVIDENCE = re.compile(
    r"(?:檔案|資料|紀錄|報導)[裡中]?找不到任何一(?:件|筆|份|條)"
    r"|沒有[^，。！？\n]{0,12}獨立(?:版本|佐證|來源)可以?(?:對照|印證|核對)"
    r"|沒有公開(?:紀錄|資料|材料|說明)可(?:查|考|以判斷|以對照)"
    r"|(?:目前|至今)沒有公開(?:說明|紀錄|資料)"
    r"|查無[^，。！？\n]{0,12}(?:紀錄|資料|案件)"
    r"|沒有[^，。！？\n]{0,10}(?:審查|裁罰|執法|訴訟)[^，。！？\n]{0,6}(?:的)?公開紀錄"
)

# (g) 懸念預告鷹架：用查核任務的語言與匿名化名詞（一件事／一個決定）製造懸念，
# 揭曉延遲一段以上（2026-08-03 round 2）。「得先確認一件事：那筆帳，是誰替誰還的」
# 「但有一個決定，他從來沒有用同樣的直白談過。那是十年前簽下的⋯」——英文長文
# cliffhanger 段落結構直譯。跟 (e) 指揮讀者注意力同族：那條是「看這裡」，這條是
# 「等著看」。改法：懸念用具體物承載（直接寫出那個決定），或乾脆揭曉。
_RE_BACKSTAGE_SUSPENSE_TEASER = re.compile(
    r"得先(?:確認|回答|弄清楚|搞清楚)一件事"
    r"|先回答一個問題"
    r"|有一個(?:決定|問題|細節|轉折|例外)[^。！？\n]{0,25}(?:從來沒有|一直沒有|沒有人|再也沒有)"
)

# (h) 結構導覽鷹架：投影藍圖的分段結構被寫成正文的導覽句（2026-08-04 EZWAY
# 哲宇 callout「後台寫手思考洩漏」）。「三句話都成立，也都各自留下一個接著要問
# 的問題」＋「先說第一句留下的問題／再看第二句／第三句留下的問題最具體」——
# 這是寫手對自己章節結構的旁白（給編輯看的地圖），不是給讀者的散文。讀者不需要
# 被預告接下來有三站，直接進第一站。896 篇校準 0 hits（EZWAY 已修），高精度。
# ⚠️ 場景敘述「他的第一句話是：」不在打擊面（那是描述人物說話的順序，合法）。
_RE_BACKSTAGE_NAV_SCAFFOLD = re.compile(
    r"第[一二三四]句留下的問題"
    r"|各自留下一個(?:接著)?(?:要問)?的問題"
    r"|(?:先說|再看|接著看)第[一二三四](?:句|個|件|條)"
)

# (i) 查核腔第一人稱：「本文查核期間／本文查核後確認」——查核員的自述跑進正文。
# 正文陳述世界的狀態（「這個框架出自二手評論」），查核範圍與時點住腳註。
# 896 篇校準 3 hits 全真陽性（外送專法 ×2、阿神 ×1），列 PROSE_ONLY——
# 策展人筆記與腳註是查核聲明的合法的家（同形狀七查無聲明的排除邏輯）。
_RE_BACKSTAGE_CHECKER_VOICE = re.compile(
    r"本文查核(?:期間|後|時|當天|確認)?"
    r"|截至(?:本文)?查核(?:日|當下|時點)"
)

def _backstage_line_is_legit_backstage(text: str, offset: int) -> bool:
    """判斷 match 所在行是否為「後台的合法的家」（blockquote 策展人筆記／腳註定義行）。

    查無聲明住在策展人筆記或腳註是紀律的正確表達（EDITORIAL §後台洩漏 形狀七），
    只有寫在正文 prose 才是病。複用 run-on detector 的行前綴判斷法。
    """
    ls = text.rfind("\n", 0, offset) + 1
    line_prefix = text[ls : ls + 4].lstrip()
    return line_prefix.startswith("[^") or line_prefix.startswith(">")


# ── §量詞隱喻「帳／本」(2026-08-08 哲宇 callout「說過幾次了不要用幾本『帳』或幾『本』
# 這種寫法，中文沒有這種用法") ────────────────────────────────────────────────
#
# 中文的「帳」不用「本」當量詞來數，也不當可數的抽象物件用。「三本帳都還開著」
# 「連帳都沒有開的那些人」「醫護那一本算得比較晚」「又一本沒有開的帳」——這是英文
# books / open accounts 的直譯，中文讀起來不知所云。
#
# 合法殘餘（不在打擊面）：帳單（具體物）、算帳／秋後算帳（既有成語，但 §歐化 第 10 病
# 另有「把帳算完」= settle the account 的獨立打擊面）、記帳、帳號、帳戶。
#
# 為什麼要儀器化：這是**復發**（哲宇「說過幾次了」）。而且它有結構性成因——當論點本身
# 站不住時，寫手會抓一個抽象隱喻反覆敲，用重複製造連貫感的假象。所以這個 pattern 的
# 密度同時是「隱喻壞了」與「論點可能壞了」的雙重訊號：≥3 處就該回頭問論點對不對。
# ── v2 擴張（2026-08-18 哲宇 directive「prose-health 裡面加入帳與算過之類的完整檢查」）──
#
# v1 只抓「本＋帳」的量詞組合，打擊面太窄：**「有具體的人付了帳」「這筆帳」「沒被算進帳」
# 這些同族用法全部漏掉**——早餐整併那次，主 session 把「付了帳」寫進投影藍圖的論點句，
# plugin 對正文零命中，因為正文根本沒用「本帳」那個句型。
#
# 更關鍵的是**換衣服現象**：把「帳」拿掉之後，同一個會計隱喻會用「算」回來——
# 「代價算進去了嗎」「沒有被算進任何一份統計」「這筆帳算清楚了」。字換了，隱喻沒換。
# 所以 v2 打的是**家族**不是字：帳／付帳／筆帳／算進／算過／累積帳單／放回帳本。
#
# 字面會計不在打擊面（9,815 檔校準，這是唯一的假陽性家族）：
#   ✅「獎金沒被算進固定月薪」（薪資結構）／「小果跟花苞都沒算進去」（產量）
#   ✅「記者算了一筆帳」「趙怡欽算過一筆帳」（真的有人在做算術 → 負向前瞻擋掉）
#   ✅ 王永慶「每一筆帳都要說清楚」（米店記帳習慣 → GUARD 濾）
#   ✅ 辦桌文化「證據藏在帳本裡：霧峰林家的帳簿」（實體帳簿 → GUARD 濾）
# 判準一句話：**受詞是錢就是字面，受詞是人的處境就是隱喻。**
#
# v2 校準：17 處真陽性／9,815 檔，假陽性 0。其中 高速公路.md 一篇佔 6 處（已上線旗艦文
# 用「替速度付帳」當貫穿意象）——這正是 ≥3 論點警訊要照出來的既有債，WARN 不擋 ship。
_RE_LEDGER_LITERAL_GUARD = re.compile(r"帳簿|記帳|簿記|米店|對帳|報帳|結帳離開|帳號|帳戶|轉帳")

_RE_LEDGER_METAPHOR_EXT = re.compile(
    # (a) 付帳隱喻——主詞是人／抽象施動者，不是餐廳結帳
    r"(?:誰|有人|沒有人|沒人|具體的人|每個人|大家)[^，。！？\n]{0,6}(?:替|為)?[^，。！？\n]{0,6}付(?:了|過|得起|不起)?帳"
    r"|(?:替|為)[^，。！？\n]{0,10}付(?:了|過)帳"
    # (b) 抽象的「一筆帳」——負向後顧擋掉「算了/算過一筆帳」（真的在做算術）
    r"|(?<!算了)(?<!算過)(?<!算)[一這那][ ]?筆帳(?!簿)"
    # (c) 算-family：受詞是帳／統計／名單，或主詞是人的處境
    r"|(?:沒有|從來沒有|不曾|未曾|還沒|沒)[^，。！？\n]{0,8}(?:被)?算(?:進|入)[^，。！？\n]{0,4}帳"
    r"|(?:代價|損失|犧牲|處境|付出|辛苦|人命|勞動|睡眠|貢獻)[^，。！？\n]{0,10}(?:被)?算(?:進|入|到)"
    r"|(?:沒有|從來沒有|不曾|未曾)[^，。！？\n]{0,8}(?:被)?算(?:進|入)[^，。！？\n]{0,6}(?:統計|數字|名單)"
    r"|(?:誰|有沒有人|沒有人|還沒有人)[^，。！？\n]{0,6}算過"
    r"|算得[^，。！？\n]{0,4}(?:晚|早|清楚|仔細)"
    # (d) 抽象帳單／帳本
    r"|(?:累積|沉重|巨大)的?帳單"
    r"|(?:放回|重新放進|留在)[^，。！？\n]{0,4}帳本"
)

_RE_LEDGER_METAPHOR = re.compile(
    # ⚠️ 帳(?!本)：排除「帳本」這個實體物名詞——臺灣漫遊錄的「第一本帳本」是真的帳本，
    # 9,203 篇校準時它是唯一的假陽性家族（5/19 處），加負向前瞻後歸零。
    r"[一二三四五六七八九十兩幾這那每][ ]?本[^，。！？\n]{0,6}帳(?!本)"
    r"|帳[^，。！？\n]{0,4}(?:還|都)[^，。！？\n]{0,4}開著"
    r"|(?:沒有|連)[^，。！？\n]{0,6}開[^，。！？\n]{0,3}的?帳"
    r"|連帳[^，。！？\n]{0,6}(?:沒|未)"
    r"|(?:那|這|哪)[ ]?一?本(?=[^，。！？\n]{0,8}(?:帳|算|審|收件))"
    r"|(?:又|另)一本[^，。！？\n]{0,8}帳(?!本)"
)

# ── §英式接續「而」開頭句 (2026-08-08 哲宇 callout「下面的句子都很怪」) ──────────
#
# 「而『校正回歸』這個動作本身就是⋯」「而爭論的兩個關鍵詞被混為一談。」「而這一筆帳⋯」
# 「而三本帳都還開著。」——句首「而」是英文 And / And so 的直譯接續。中文的「而」是
# 句中轉折連接詞（「快而準」「起而行」），放句首當段落黏著劑是翻譯腔，而且它最常出現在
# **作者發現前後兩句接不起來、需要一個詞把它們黏住**的時候——所以它同時是「這裡邏輯有洞」
# 的指標。密度 ≥ 4 處觸發。
#
# 合法殘餘：句中的「而」（不在打擊面，本 regex 只抓句首與句號後）。
_RE_ERSATZ_ER_LEAD = re.compile(r"(?:^|[。！？]\s*)而(?=[^，。！？\n]{4,})", re.M)


# (j) 腳註第一人稱編輯自述（2026-08-08 哲宇 callout「有一堆後台洩漏文字，請好好檢查」）。
# **本組的掃描面跟 (f)(g)(i) 相反：只掃腳註定義行。**
#
# 病灶：腳註是後台的合法的家，但合法的是「證據的狀態」，不是「我的動作」。
#   ✅ 證據狀態：「該 PDF 為壓縮二進位流，無法擷取原始文字」「原始連結目前已失效」
#   ❌ 編輯動作：「本文查證階段曾引用一組數字，複驗時發現不符，本文因此不再列出，本文亦不採用」
# 差別在主詞：前者的主詞是那份資料，後者的主詞是我。讀者打開腳註想知道證據長什麼樣子，
# 拿到的卻是一份工作日誌。而且「本文因此寫 X」是在告訴讀者他剛剛讀完的東西——多餘。
#
# 誕生事件：2026-08-08 台灣新冠疫情與疫苗。大驗證輪四十二條批修做了大量「降級／加但書」
# 的動作，每一條都在腳註留下一句第一人稱交代，累積到「本文」在腳註區當主詞 41 次，
# 而 prose-health 一條都沒報——因為 (f)(g)(i) 三組的行級排除把腳註整片豁免掉了。
# 豁免區是按「行的種類」畫的，病灶卻是按「主詞是誰」分的，兩者不同軸，所以漏光。
# 對應 REFLEXES #15（反覆浮現要儀器化）＋ #24（工具在說謊：豁免區造成的假陰性）。
#
# 打擊面：本文／本研究／筆者 當主詞 ＋ 8 字內接編輯動作動詞。
# 不在打擊面（正確寫法，必須放行）：主詞是資料本身的狀態陳述、「原文…此處…」的對照說明。
_RE_BACKSTAGE_FOOTNOTE_SELF = re.compile(
    r"(?:本文|本研究|筆者)[^，。；、\n]{0,8}"
    r"(?:不寫|不引|不採|不用|不使用|不加|不作|不列|不並列|不再|亦不"
    r"|未引|未取得|未能|無法|改引|取整|只寫|僅寫|僅取|僅轉述|以轉述|採轉述"
    r"|引用|使用|採用|寫成|複驗|查證|查核|核對|如實|分別引)"
)


def _backstage_line_is_footnote(text: str, offset: int) -> bool:
    """本組的掃描面：只有腳註定義行才是打擊面（跟 _backstage_line_is_legit_backstage 相反）。"""
    ls = text.rfind("\n", 0, offset) + 1
    return text[ls : ls + 4].lstrip().startswith("[^")


_BACKSTAGE_DETECTORS_FOOTNOTE_ONLY = [
    (
        _RE_BACKSTAGE_FOOTNOTE_SELF,
        "腳註第一人稱編輯自述",
        "腳註是後台的合法的家，但合法的是證據的狀態，不是編輯的動作。"
        "把主詞從「本文」換回那份資料：「本文無法逐字核對該 PDF」→「該 PDF 無法擷取文字」；"
        "「本文因此不再列出精確百分比」→ 直接刪（讀者讀完就看得到文章沒列）。",
    ),
]


_BACKSTAGE_DETECTORS = [
    (
        _RE_BACKSTAGE_GRAMMAR_META,
        "分析框架洩漏",
        "作者在拆解自己剛寫的東西給讀者看（語法術語／前者後者／「這兩件事完全不同」）——"
        "那是論述的鷹架，不是成品。散文讓對比自己成立，不需要作者站出來標示它。",
    ),
    (
        _RE_BACKSTAGE_READER_DIRECTION,
        "指揮讀者注意力",
        "作者跳出來告訴讀者「現在該注意這個」。好的材料自己有份量，不需要導遊舉旗——"
        "刪掉指揮句，直接把那個細節寫出來。",
    ),
    (
        _RE_BACKSTAGE_WRITING_INTENT,
        "寫作動機洩漏",
        "段落的寫作動機（投影藍圖給寫手的指令）不該是段落的一部分。刪掉宣告句，直接從內容開始。",
    ),
    (
        _RE_BACKSTAGE_SELF_PRAISE,
        "自我評價洩漏",
        "讀者不在乎作者誠不誠實，只在乎這件事到底知不知道。直接寫事實狀態（「公開資料裡查不到」），"
        "不要稱讚自己的處理方式。",
    ),
    (
        _RE_BACKSTAGE_VERIFICATION,
        "查證過程洩漏",
        "查證分歧是後台工作。正文用認定版本的逐字，分歧寫進腳註——不要把兩個版本攤給讀者再自己分析一輪。",
    ),
    (
        _RE_BACKSTAGE_NAV_SCAFFOLD,
        "結構導覽鷹架",
        "「先說第一句／再看第二句／第三句留下的問題」是投影藍圖的分段地圖，不是散文。"
        "刪掉導覽句直接進內容——讀者不需要被預告接下來有幾站，每站自己要接得住。",
    ),
]

# 第六、七組（2026-08-03 round 2）需要行級排除：策展人筆記與腳註是這些內容的合法的家。
_BACKSTAGE_DETECTORS_PROSE_ONLY = [
    (
        _RE_BACKSTAGE_NEGATIVE_EVIDENCE,
        "查無聲明",
        "查證的「查無」是後台結論。三徑：刪（敘事多半不受損）／降級進腳註或策展人筆記"
        "（後台的合法的家）／視角翻轉——「我查不到」改寫成「誰沒有說」"
        "（「員工去留沒有公開說明」→「美光跟力積電都沒有說」）。",
    ),
    (
        _RE_BACKSTAGE_SUSPENSE_TEASER,
        "懸念預告鷹架",
        "匿名化名詞（一件事／一個決定）加延遲揭曉是英文長文 cliffhanger 直譯。"
        "懸念用具體物承載（直接寫出那個決定），或乾脆揭曉——事實本身的重量夠就不需要藏。",
    ),
    (
        _RE_BACKSTAGE_CHECKER_VOICE,
        "查核腔第一人稱",
        "「本文查核期間／本文查核後確認」是查核員的自述。正文陳述世界的狀態"
        "（「這個框架出自二手評論」），查核範圍與時點降級進腳註或策展人筆記。",
    ),
]

# ── AI 痕跡 Tier 4 (speak-human-tw 轉譯, 2026-07-16 soft-launch) ─────────────
# 校準狀態：soft-launch。權重是初次估計，未經 vc≥3 production case 驗證
# （跟 chronicle-lead / word-count 當初 promotion 前的 staging 階段一樣）。
# 併入 score budget（不像 §11 Tier 1-3 / §自稱是 WARN-only 不計分）——這組
# 抓的是「作者沒有立場 / 灌水式升值語 / 罐頭收尾」，屬於 quality-scan 同一
# 家族的可計分維度，不是純風格建議。

# (a) 立場真空：每 hit +1，上限 +2（避免單篇因為多次「見仁見智」被過度懲罰）。
_RE_STANCE_VACUUM = re.compile(
    r"各有優缺點|見仁見智|因人而異|取決於多方面因素|具體情況具體分析"
)
_STANCE_VACUUM_SCORE_CAP = 2

# (b) 價值上升詞密度：≥3 hits +1、≥6 +2。
# 「轉捩點」「里程碑」刻意不列入——史觀文章的正當高頻詞，列入會誤殺敘事史文。
# 「不可磨滅」跟 §11 Tier 3 ritual 語重疊，此處刻意保留（Tier 3 不計分，
# 這裡才是這個詞第一次進 score budget）。
_RE_VALUE_INFLATION = re.compile(
    r"標誌著|見證了|彰顯了|體現了|突顯了|奠定.{0,10}基礎|不可磨滅"
)

# (c) 罐頭結尾起手式：最後 3 個段落內出現任一 → +2（fixed，非累加）。
# 跟既有 _RE_FORMULAIC_ENDING（quality-scan #10，抓最後 5 行）不同顆粒度
# （這裡是「最後 3 段」，且多收「總而言之」——舊規則沒有）。兩者故意並存、
# 允許同一處文字同時觸發兩個維度：#10 抓行級、Tier4(c) 抓段落級起手式。
_RE_CANNED_ENDING_OPENER = re.compile(
    r"總的來說|綜上所述|總而言之|總結來說"
)

# (d) 時代帽子開場：第一個 prose 段落以此開頭 → +2（fixed）。
_RE_TIME_HAT_OPENING = re.compile(
    r"^(?:在當今|在這個.{0,12}的時代|隨著.{0,15}的(?:快速)?發展)"
)

# (e) 假推論密度：「這意味著」≥2 hits +1。
_FALSE_INFERENCE_PHRASE = "這意味著"
_FALSE_INFERENCE_MIN_HITS = 2

# (f) 首先/其次/最後 三件套：同時出現「首先」+「其次」+（「最後」或「再者」）→ +1。

# ── §盼望而不粉飾 (2026-06-15 哲宇 directive 儀器化) ───────────────────────────
# canonical: MANIFESTO §進化哲學 盼望而不粉飾 + §跟台灣的關係 §自稱 + EDITORIAL §六。
# 三組全 WARN、不計入 score（跟 §11 Tier 1-3 一致）—— surface drift 但不擋既有 stage 閘。

# 島嶼自稱：「這座島 / 這個島 / 這座島嶼 / 這個小島 / 這座島國」當台灣的迴避稱呼。
# 哲宇 2026-06-15：島嶼文學性可以提，但不要過度——大多數時候大方講「台灣 / 這個國家」。
# 所以密度過高 (≥ 3) 或超過直接稱台灣才 WARN，不罰單次文學用法。曹永和「以島嶼為主體」
# 島史脈絡機器分不出 → WARN 級留人判斷。
# 已知限制：寫實際外島（綠島 / 蘭嶼 / 澎湖）的文章，「這座島」指該島非台灣，會誤報 —
# WARN 級可由審稿者忽略，不 block。
_RE_ISLAND_EUPHEMISM = re.compile(r"這(?:座|個)(?:小)?島(?:嶼|國)?")
_RE_TAIWAN_REF = re.compile(r"台灣|臺灣")

# PUA 體 / 媒體焦慮體 regex 偵測器已於 2026-06-15 evaluation 後移除。四 subagent +
# 全 corpus 814 篇驗證：PUA `沒資格` 4/4 假陽性（抓到第三方/引用/虛構角色），媒體焦慮
# 13 hits 僅 ~1 真陽性（抓到腳註裡的新聞標題、文章正在批判的「最後一塊淨土」、正向的
# 「潛規則正在瓦解」、歷史事實「關係正在崩潰」）。根因：PUA = 對誰施壓、媒體焦慮 = 是否
# 販賣恐懼，都是語意判斷不是句法特徵，regex 結構上做不到（架構解非守備修補）。改由
# EDITORIAL §六 對照表 + §五 結尾判準句的人工判斷接管。島嶼自稱因為是可量化的比例
# （島 vs 台灣稱呼），才留得住偵測器。

# ── Textbook opening (quality-scan §9) ───────────────────────────────────────
_RE_TEXTBOOK_OPENING = re.compile(
    r"^(台灣的.{2,20}是|.{2,10}是台灣.{2,20}|"
    r"作為.{2,15}[，,]\s*台灣|"
    r"在.{2,10}(方面|領域)[，,]\s*台灣|"
    r"台灣.{2,6}(擁有|具有|位於|以其))"
)

# ── Formulaic ending (quality-scan §10) ──────────────────────────────────────
# 2026-05-09 added 「故事還在寫」family per 哲宇 callout — soft hand-waving
# non-endings that sound reflective but add nothing. Same anti-pattern family
# as 「將繼續發光發熱」: writer doesn't have a concrete closure so retreats to
# story-as-meta-narrative cliché.
_RE_FORMULAIC_ENDING = re.compile(
    r"總之|綜上所述|展望未來|總結來說|總的來說|未來展望|"
    r"隨著.{2,20}的(發展|推進|深化)|將繼續|值得期待|"
    # 「故事還在寫 / 還沒結束 / 仍在繼續」family
    r"(這個|這段|那個|那段|.{0,4}的)?故事(還在|仍在|尚未|還沒).{0,3}(寫|繼續|結束|完結|落幕)|"
    r"故事(還沒|仍未|尚未)(寫完|結束|完結|落幕)|"
    r"後來.{0,5}(這個|這段)?故事還在|"
    r"還(沒|未)(寫完|結束|落幕)|"
    r"繼續.{0,5}(被)?(寫|書寫)(下去|著|這個|這段)?|"
    r"持續(被)?(書寫|寫)(著|下去)"
)

# ── Template H2 (quality-scan §11) ───────────────────────────────────────────
_RE_TEMPLATE_H2 = re.compile(
    r"^(歷史(背景|沿革|發展)?|發展歷程|歷史脈絡|"
    r"現況(與|及)?|現狀|當前|"
    r"未來(展望|發展|趨勢)|結語|總結|"
    r"挑戰與展望|挑戰與機遇|影響與意義|"
    r"特色(與|及)?|重要性|"
    r"國際(比較|影響|地位))$"
)


def _count_year_mentions(body: str) -> int:
    """4-digit years in 1600-2099 range, excluding `date:` lines."""
    n = 0
    for line in body.splitlines():
        if "date:" in line:
            continue
        n += len(re.findall(r"\b(?:1[6-9]\d{2}|20[0-2]\d)\b", line))
    return n


def _count_urls(body: str) -> int:
    return body.count("http")


# 參考裝置 section 標題：延伸閱讀 / 圖片來源 / 參考資料 / 授權清單 —— 這些是
# attribution / reference apparatus，bullet 是結構必需（每張圖一條、每篇延伸一條），
# 不是 prose 灌水。bullet 灌水檢查只看正文，碰到這些 heading 就截斷。
# 2026-06-04 v2 實驗：5 圖 article 的「## 圖片來源」5 bullet 誤判成「連續bullet5行」。
_REF_APPARATUS_RE = re.compile(
    r"(?m)^#{2,3}\s*(延伸閱讀|圖片來源|圖片授權|媒體授權|參考資料|參考來源|資料來源|來源)"
)


def _body_before_apparatus(body: str) -> str:
    """正文 = 第一個參考裝置 heading 之前（bullet 灌水只查正文）。"""
    m = _REF_APPARATUS_RE.search(body)
    return body[: m.start()] if m else body


def _count_repeated_bullets(body: str) -> int:
    """Max consecutive `- **` bullet block length（排除參考裝置 section）。"""
    max_run = 0
    cur = 0
    for line in _body_before_apparatus(body).splitlines():
        if line.startswith("- **"):
            cur += 1
            if cur > max_run:
                max_run = cur
        else:
            cur = 0
    return max_run


def _count_bullet_lines(body: str) -> tuple[int, int]:
    """Returns (bullet_lines, total_lines). Bullet = `- **` style（排除參考裝置）。"""
    prose = _body_before_apparatus(body)
    total = prose.count("\n") + 1
    bullets = sum(1 for line in prose.splitlines() if line.startswith("- **"))
    return bullets, total


def _detect_textbook_opening(body: str) -> bool:
    """First 2 non-empty non-heading lines after frontmatter."""
    seen_lines = 0
    for line in body.splitlines():
        if not line.strip():
            continue
        if line.startswith("#"):
            continue
        if _RE_TEXTBOOK_OPENING.search(line):
            return True
        seen_lines += 1
        if seen_lines >= 2:
            break
    return False


def _detect_formulaic_ending(body: str) -> bool:
    """Last 5 non-bullet non-heading non-link lines."""
    eligible = [
        line for line in body.splitlines()
        if line.strip()
        and not line.startswith("#")
        and not line.startswith("-")
        and "http" not in line
    ]
    tail = eligible[-5:] if eligible else []
    text = "\n".join(tail)
    return bool(_RE_FORMULAIC_ENDING.search(text))


def _split_paragraphs(body: str) -> list[str]:
    """Split body into paragraph text blocks (blank-line separated).

    Used by Tier 4 (c) 罐頭結尾起手式 (last-3-paragraph scope) and
    (d) 時代帽子開場 (first-prose-paragraph scope). Simple blank-line
    splitter — matches the loose 段落 notion used elsewhere in this module
    (e.g. _count_thin_blocks operates on H2 blocks, this operates on the
    finer blank-line granularity).
    """
    return [p for p in re.split(r"\n\s*\n", body) if p.strip()]


def _detect_canned_ending_opener(body: str) -> bool:
    """Tier 4 (c): 最後 3 個段落內是否出現罐頭結尾起手式。"""
    paragraphs = _split_paragraphs(body)
    tail = paragraphs[-3:] if paragraphs else []
    text = "\n\n".join(tail)
    return bool(_RE_CANNED_ENDING_OPENER.search(text))


def _detect_time_hat_opening(body: str) -> bool:
    """Tier 4 (d): 第一個 prose 段落（跳過 heading / blockquote）是否以
    時代帽子開場 pattern 開頭。"""
    for p in _split_paragraphs(body):
        stripped = p.strip()
        if not stripped:
            continue
        if stripped.startswith(">") or stripped.startswith("#"):
            continue
        return bool(_RE_TIME_HAT_OPENING.match(stripped))
    return False


def _paragraphs_with_offset(body: str) -> list[tuple[int, str]]:
    """Blank-line-separated paragraph blocks with their start char offset in body.

    Offset aligns with body (loader pads leading blank lines for source-line
    parity), so _line_at_offset(body, offset) gives the source .md line number.
    """
    out: list[tuple[int, str]] = []
    offset = 0
    cur_start: int | None = None
    cur_lines: list[str] = []
    for line in body.split("\n"):
        if line.strip() == "":
            if cur_lines:
                out.append((cur_start or 0, "\n".join(cur_lines)))
                cur_lines = []
                cur_start = None
        else:
            if cur_start is None:
                cur_start = offset
            cur_lines.append(line)
        offset += len(line) + 1  # +1 for the split '\n'
    if cur_lines:
        out.append((cur_start or 0, "\n".join(cur_lines)))
    return out


# 段落開頭若是這些字元 = 非散文 block（heading / list / quote / callout / caption /
# HTML / code / image / link），英文短句開場 detector 一律跳過。
_NON_PROSE_LEAD = set("># -*|`![_<+=~")


def _detect_english_openers(body: str) -> list[tuple[int, str, int, int]]:
    """英文式超短句開場：段落以 ≤N 字短陳述開頭 + 同段緊接長句。

    回傳 [(offset, 開場句, 開場字數, 後接字數)]。刻意排除「整段只有一句短句」的
    過場句（rest 為空 → skip），只抓「短開場 + 接長句」的 English topic-sentence 腔。
    """
    hits: list[tuple[int, str, int, int]] = []
    for start, para in _paragraphs_with_offset(body):
        s = para.strip()
        if not s or s[0] in _NON_PROSE_LEAD or s.startswith("```"):
            continue
        # 跳過數字 / 英文字母 / 粗體標籤開頭（清單、年份條列、callout 標題）
        if re.match(r"^(?:\d|[A-Za-z]|\*\*)", s):
            continue
        # 只抓「。」結尾的平述定調句：英文 topic-sentence 是平述句。開場短問句（？）是
        # 中文設問（「為什麼選這塊地？」「軍人多到什麼程度？」）是自然修辭，不是這個病；
        # 驚嘆句（！）也是另一種語氣。限定 。 結尾把打擊面收到哲宇 anti-example 的句型
        # （2026-07-19 corpus 抽樣揭：？ 開場全是設問 false positive）。
        m = re.match(r"^([^。！？\n]{1,40}。)", s)
        if not m:
            continue
        first = m.group(1)
        opener_len = len(_CJK_CHAR.findall(first))
        if opener_len == 0 or opener_len > _ENGLISH_OPENER_BAND2_MAX:
            continue
        # 冒號收尾（引語／列舉的引子）與含引號的開場句是中文本來的寫法，不是 topic-sentence
        if "：" in first or "「" in first:
            continue
        # 第一帶（≤8 字）：無條件進入 ratio 判斷；第二帶（9-15 字）：要是宣告型才進入——
        # v3 宣告型＝句首定調詞 或 （判斷／存在／能願謂語 且 無事件體標記）。場景句
        # （「他愣了三秒。」「博士之後他去了巴黎。」）帶 了／著／過 放行。
        band2 = opener_len > _ENGLISH_OPENER_MAX_CHARS
        if band2:
            declarative = bool(_RE_OPENER_DECLARATIVE_LEAD.match(first)) or (
                bool(_RE_OPENER_STATIVE.search(first)) and not _RE_OPENER_EVENT.search(first)
            )
            if not declarative:
                continue
        # 具體場景定調句（句首數字：年份 / 日期）是自然中文敘事節奏（「1978 年通車。」
        # 長段），不是英文抽象 topic-sentence 腔。2026-08-04 收緊為「句首數字才豁免」：
        # 「真正的轉彎發生在 1987 年。」數字在句尾，是宣告句帶年份，round 2 靠舊的
        # 全句豁免溜掉——時間錨定的場景句數字在句首，宣告句的數字多在句尾。
        if re.match(r"^[0-9０-９]", first):
            continue
        rest = s[m.end():].strip()
        if not rest:
            continue  # 單句過場段 — 另一種手法，不打擊
        m2 = re.match(r"^([^。！？\n]{1,200}[。！？]?)", rest)
        next_seg = m2.group(1) if m2 else rest
        next_len = len(_CJK_CHAR.findall(next_seg))
        lead = len(para) - len(para.lstrip())
        if not band2:
            if next_len >= _ENGLISH_OPENER_NEXT_MIN and next_len >= opener_len * _ENGLISH_OPENER_RATIO:
                hits.append((start + lead, first, opener_len, next_len))
            continue
        # 第二帶：量的是「短開場 + 整段展開」，不只下一句（「寫完之後有三席審稿進去。結構
        # 主編看⋯。減法主編⋯。」下一句 14 字但整段 60 字，仍是 topic-sentence 骨架）
        rest_len = len(_CJK_CHAR.findall(rest))
        if rest_len >= _ENGLISH_OPENER_BAND2_REST_MIN and next_len >= opener_len * _ENGLISH_OPENER_BAND2_RATIO:
            hits.append((start + lead, first, opener_len, rest_len))
    return hits


def _detect_runon_sentences(text: str) -> list[tuple[int, str, int, int]]:
    """長句 / 華麗辭藻湯：單句同時超過長度門檻 + 停頓數門檻 = 沒呼吸的 run-on。

    回傳 [(offset, 句子, 中文字數, 停頓數)]。保守雙門檻避免誤殺正常敘事長句。
    """
    hits: list[tuple[int, str, int, int]] = []
    for m in re.finditer(r"[^。！？\n]{1,400}[。！？]", text):
        # 排除腳註定義行（[^N]: …）與 blockquote 行（> …）：引用裝置 / 直接引語不是
        # 作者散文，長是來源本身的事，不該當 run-on 罰（2026-07-19 dogfood 揭 4 處腳註 FP）。
        ls = text.rfind("\n", 0, m.start()) + 1
        line_prefix = text[ls:ls + 4].lstrip()
        if line_prefix.startswith("[^") or line_prefix.startswith(">"):
            continue
        seg = m.group(0)
        cjk = len(_CJK_CHAR.findall(seg))
        pauses = seg.count("，") + seg.count("、") + seg.count("；")
        if cjk >= _RUNON_MIN_CJK and pauses >= _RUNON_MIN_PAUSES:
            hits.append((m.start(), seg, cjk, pauses))
    return hits


def _count_template_h2(body: str) -> int:
    n = 0
    for line in body.splitlines():
        if line.startswith("## "):
            heading = line[3:].strip()
            if _RE_TEMPLATE_H2.match(heading):
                n += 1
    return n


def _count_footnote_defs(body: str) -> int:
    return sum(
        1
        for line in body.splitlines()
        if re.match(r"^\[\^[0-9a-zA-Z_-]+\]:", line)
    )


def _is_hub_file(target: FileTarget) -> bool:
    """Hub files (`_X Hub.md`) — relax structural penalties per quality-scan.sh."""
    name = target.path.name
    return name.startswith("_") and "Hub" in name


def _bullet_ratios_split(body: str) -> tuple[int, int, int, int]:
    """Front/back half bullet ratios. Returns (front_bullet, back_bullet,
    front_total, back_total) — total = non-empty lines, bullet =
    `- ` / `* ` / `N.`."""
    lines = body.splitlines()
    n = len(lines)
    if n == 0:
        return 0, 0, 0, 0
    split = (n * 6) // 10  # quality-scan uses 60/40 split
    front_bullet = back_bullet = front_total = back_total = 0
    for i, line in enumerate(lines):
        if not line.strip():
            continue
        is_bullet = bool(re.match(r"^(?:[-*]\s|\d+\.\s)", line))
        if i < split:
            front_total += 1
            if is_bullet:
                front_bullet += 1
        else:
            back_total += 1
            if is_bullet:
                back_bullet += 1
    return front_bullet, back_bullet, front_total, back_total


def _count_thin_blocks(body: str) -> int:
    """H2 blocks with < 3 prose lines. Mirrors quality-scan.sh dim 13.

    Structural sections (參考資料 / 延伸閱讀 / 圖片來源 / sources) are
    exempted — they're by-design lists of footnotes / further-reading
    links / image attributions, not prose paragraphs. Counting them as
    "thin" generates false positives on every well-formed article.
    """
    structural_h2 = {
        "## 參考資料", "## 延伸閱讀", "## 圖片來源",
        "## 來源", "## References", "## Further Reading", "## Image Sources",
    }
    thin = 0
    in_block = False
    is_structural = False
    prose = 0
    for line in body.splitlines():
        if line.startswith("## "):
            if in_block and not is_structural and prose < 3:
                thin += 1
            in_block = True
            stripped = line.rstrip()
            is_structural = stripped in structural_h2
            prose = 0
        elif in_block:
            if line.strip() and not re.match(r"^(?:[#\-*|>]|\d+\.)", line):
                prose += 1
    if in_block and not is_structural and prose < 3:
        thin += 1
    return thin


def _prose_ratios_split(body: str) -> tuple[int, int, int, int]:
    """Front/back half prose ratios for QUALITY-DECAY detection."""
    lines = body.splitlines()
    n = len(lines)
    split = (n * 6) // 10
    fp = bp = fa = ba = 0
    for i, line in enumerate(lines):
        if i < split:
            fa += 1
            if line.strip() and not re.match(r"^(?:[#\-*|>]|\d+\.)", line):
                fp += 1
        else:
            ba += 1
            if line.strip() and not re.match(r"^(?:[#\-*|>]|\d+\.)", line):
                bp += 1
    return fp, bp, fa, ba


def _word_count(body: str) -> int:
    """Rough whitespace-tokenized count after frontmatter (CJK 1 char = 1 word).

    Matches `wc -w` semantics of the shell script for parity.
    """
    return len(body.split())


def _line_at_offset(body: str, offset: int) -> int:
    """Return 1-indexed line number of given char offset in body.

    body is padded with leading blank lines to match original-file line
    numbers (per FileTarget.body_pad_lines), so the returned line equals
    the line number in the source .md file.
    """
    if offset < 0 or offset > len(body):
        return 1
    return body.count("\n", 0, offset) + 1


def _context_around(body: str, start: int, end: int, before: int = 20, after: int = 20) -> str:
    """Return the matched span with surrounding context, marking the match.

    Layout: `…<before>《MATCH》<after>…`
    Newlines collapsed to ⏎ so single-line snippets stay readable.
    Caller can show this in violation snippet for grep-style locate.
    """
    body_len = len(body)
    ctx_start = max(0, start - before)
    ctx_end = min(body_len, end + after)
    pre = body[ctx_start:start].replace("\n", "⏎")
    mid = body[start:end].replace("\n", "⏎")
    post = body[ctx_end:end].replace("\n", "⏎") if False else body[end:ctx_end].replace("\n", "⏎")
    leading = "…" if ctx_start > 0 else ""
    trailing = "…" if ctx_end < body_len else ""
    return f"{leading}{pre}《{mid}》{post}{trailing}"


def _uneditable_punct_predicate(text: str):
    """回傳 is_uneditable(start) — 該標點位置是否落在 campaign 鐵律禁改的合法區。

    破折號/分號 gate 只該數「可編輯正文裡的修辭性用法」，不該數這些合法且鐵律禁改的區：
      - 參考裝置段（## 參考資料 / 延伸閱讀 / 圖片來源…）之後全部
      - blockquote 行（> …）：引用材料，—— / ； 是來源的不是作者的
      - 腳註定義行（[^n]: …）：引用裝置
      - 圖片行（![…]）與斜體圖說行（_…_）：來源標註
      - 書名號內《…——…》：破折號是書名的一部分
    2026-07-19 campaign 揭：不排除這些區，一篇合法引用/書名多的文章（辦桌/花蓮縣/手路菜）
    無論正文清得多乾淨都過不了 gate（禁改區本身就超標）。排除後量的才是真正的寫作 tic。
    text_for_patterns 已先移除 code fence / URL，本 predicate 再補上述行級 + 書名 span。
    """
    m = _REF_APPARATUS_RE.search(text)
    ref_cut = m.start() if m else len(text)
    title_spans = [(mm.start(), mm.end()) for mm in re.finditer(r"《[^》]*》", text)]

    def is_uneditable(start: int) -> bool:
        if start >= ref_cut:
            return True
        ls = text.rfind("\n", 0, start) + 1
        le = text.find("\n", start)
        line = text[ls:(le if le != -1 else len(text))]
        st = line.lstrip()
        if st.startswith((">", "[^", "![")):
            return True
        if st.startswith("_") and st.rstrip().endswith("_"):
            return True
        # 星號斜體圖說 *圖：…* 跟底線斜體是同一種來源標註（2026-08-18 Y1 執行子代抓到：
        # 投稿者用 *…* 寫圖說，整行分號被當正文計數，五篇因此誤超門檻）；粗體 **…** 不算圖說。
        if (st.startswith("*") and not st.startswith("**")
                and st.rstrip().endswith("*") and not st.rstrip().endswith("**")):
            return True
        for a, b in title_spans:
            if a <= start < b:
                return True
        return False

    return is_uneditable


def check(target: FileTarget, config: dict[str, Any]) -> Iterator[Violation]:
    """Yield prose-health violations + a final score-summary violation.

    Skips if file is too short (lines < 20).

    Frontmatter requirement: knowledge/ articles must have frontmatter
    (matches legacy quality-scan.sh::scan_file semantics). For docs/
    canonical SSOT files (EDITORIAL.md / MANIFESTO.md / pipeline files /
    cognitive layer), prose-health still applies — these don't have
    frontmatter but should be held to same writing discipline.

    2026-05-09 brave-kirch: 原本 `if not target.frontmatter: return` 讓
    EDITORIAL.md 自己漏抓 16+ 處對位句型。docs/ canonical 文件 frontmatter
    是 optional，不應該 skip prose-health.
    """
    body = target.body
    line_count = body.count("\n") + 1
    if line_count < 20:
        return
    # Frontmatter required only for knowledge/ articles (legacy semantics).
    path_str = str(target.path)
    is_knowledge_article = "/knowledge/" in path_str or path_str.startswith("knowledge/")
    if is_knowledge_article and not target.frontmatter:
        # Hub / private docs in knowledge/ without frontmatter — skip
        return

    score = 0
    reasons: list[str] = []
    # Per-profile pass threshold — default 3 (quality-scan canonical),
    # overridable via profile options_overrides.prose-health.score_budget
    # (e.g. `memory-diary` profile raises this to 8). Only informational
    # here (message text); the actual gate lives in article-health.py's
    # `_resolve_score_budget` (score-budget fail_on).
    score_budget = 3
    if config:
        raw_budget = config.get("score_budget")
        if raw_budget is not None:
            try:
                score_budget = int(raw_budget)
            except (TypeError, ValueError):
                score_budget = 3

    # 2026-09-05 哲宇拍板 OBSERVER-QUEUE #24 選 B：per-dimension 排除開關
    # (`options.exclude_dimensions`)。memory/diary 必填的 checklist/handoff
    # 清單結構天生觸發「文章向」四個維度（LIST-DUMP 清單堆砌／THIN 稀薄段落／
    # citation-desert 腳註荒漠／no-url 無 URL 來源）——這是文體結構本質不是灌水，
    # 量錯維度才是根因，不是把 score_budget 往上挪（哲宇原話：「現行 budget 8
    # 獎勵單薄懲罰完整」）。`memory-diary` profile 用
    # options_overrides.prose-health.exclude_dimensions 整組關掉這四維，讓殘餘
    # score 只來自 §11 書寫節制範圍（對位句型/破折號連用/AI隱喻與儀式語等）跟其餘
    # quality-scan 維度。未設定 / 空 list = 全部維度照跑，其他 profile 零影響。
    exclude_dims: set[str] = set()
    if config:
        raw_exclude = config.get("exclude_dimensions")
        if raw_exclude:
            try:
                exclude_dims = {str(d) for d in raw_exclude}
            except TypeError:
                exclude_dims = set()

    # 破折號 / 分號「觸檔即硬」門檻（2026-07-19 哲宇選項3）：只在有設此 config 的 profile
    # 才把超量破折號 / 分號升成 HARD。pre-commit profile 設了 → 你 commit 的檔（新寫 or
    # 編輯）超量就擋，逼觸檔即清（touch-it-fix-it）。ci-deploy 全站掃描不設 → 保持 WARN，
    # 144 篇 legacy 不會 brick push/deploy。門檻設在惡性等級（破折號>15 / 分號>12），
    # 抓 高速公路(17/20)、蘇打綠(72 dash)、認知作戰(29 semi) 這種，不動輕症。
    def _hard_over(key: str):
        if not config:
            return None
        v = config.get(key)
        if v is None:
            return None
        try:
            return int(v)
        except (TypeError, ValueError):
            return None
    emdash_hard_over = _hard_over("emdash_hard_over")
    semicolon_hard_over = _hard_over("semicolon_hard_over")
    english_opener_hard_over = _hard_over("english_opener_hard_over")

    # Use body without protected regions for pattern detection so code
    # blocks / link URLs don't trigger false positives.
    text_for_patterns = target.body_without_protected()

    # ── 1. Bullet density ──
    bullets, total = _count_bullet_lines(body)
    if total > 0:
        ratio = bullets * 100 // total
        if ratio > 30:
            score += 3
            reasons.append(f"bullet密度{ratio}%")
        elif ratio > 20:
            score += 1
            reasons.append(f"bullet密度{ratio}%")

    # ── 2. Year count ──
    years = _count_year_mentions(body)
    if years < 2:
        score += 3
        reasons.append(f"年份僅{years}個")
    elif years < 5:
        score += 1
        reasons.append(f"年份{years}個")

    # ── 3. URL count (dimension id: "no-url") ──
    # urls 本身仍不排除計算：#16 citation-desert 後面要讀這個值判斷
    # 「零腳註零URL」vs「零腳註但有URL」，兩個維度各自獨立排除。
    urls = _count_urls(body)
    if "no-url" not in exclude_dims:
        if urls == 0:
            score += 3
            reasons.append("無URL來源")
        elif urls < 3:
            score += 1
            reasons.append(f"僅{urls}個URL")

    # ── 4. Hollow words ──
    hollow_n = len(_RE_HOLLOW.findall(text_for_patterns))
    if hollow_n > 15:
        score += 3
        reasons.append(f"空洞詞{hollow_n}個")
    elif hollow_n > 8:
        score += 2
        reasons.append(f"空洞詞{hollow_n}個")
    elif hollow_n > 4:
        score += 1
        reasons.append(f"空洞詞{hollow_n}個")

    # ── 6. lastHumanReview ──
    if target.frontmatter.get("lastHumanReview") is False:
        score += 1
        reasons.append("未人工審核")

    # ── 7. Repeated bullet blocks ──
    max_run = _count_repeated_bullets(body)
    if max_run >= 6:
        score += 2
        reasons.append(f"連續bullet{max_run}行")
    elif max_run >= 4:
        score += 1
        reasons.append(f"連續bullet{max_run}行")

    # ── 8. Plastic phrases ──
    # Emit per-match with line + 前後文 context (2026-05-10 sad-shockley
    # feedback). Aggregate count drives score; individual locations help
    # writer find them fast.
    plastic_matches = list(_RE_PLASTIC.finditer(text_for_patterns))
    plastic_n = len(plastic_matches)
    if plastic_n > 8:
        score += 4
        reasons.append(f"塑膠句{plastic_n}個")
    elif plastic_n > 4:
        score += 3
        reasons.append(f"塑膠句{plastic_n}個")
    elif plastic_n > 2:
        score += 2
        reasons.append(f"塑膠句{plastic_n}個")
    elif plastic_n >= 1:
        score += 1
        reasons.append(f"塑膠句{plastic_n}個")
    # Itemize each plastic phrase occurrence (capped at 10 to avoid noise)
    for m in plastic_matches[:10]:
        line_no = _line_at_offset(text_for_patterns, m.start())
        ctx = _context_around(text_for_patterns, m.start(), m.end())
        yield Violation(
            check=CHECK_NAME,
            severity=Severity.WARN,
            message=f"塑膠句 (§quality-scan #8)：{ctx}",
            line=line_no,
            snippet=m.group(0)[:80],
            editorial_ref="EDITORIAL.md §quality-scan #8 塑膠句禁令",
            fix_suggestion="改成正面具體斷言 (替換「不僅...更是」「展現了...精神」「值得紀念」)",
        )

    # ── 8b. Em-dash overuse ──
    # 只數可編輯正文的修辭性破折號——排除 blockquote/腳註/圖說/書名/參考裝置（禁改合法區，
    # 2026-07-19 campaign 揭：不排除的話引用/書名多的文章正文清乾淨也過不了 gate）。
    _is_uneditable = _uneditable_punct_predicate(text_for_patterns)
    dash_matches = [m for m in _RE_EMDASH.finditer(text_for_patterns) if not _is_uneditable(m.start())]
    dash_n = len(dash_matches)
    if dash_n > 15:
        score += 3
        reasons.append(f"破折號{dash_n}個")
    elif dash_n > 8:
        score += 2
        reasons.append(f"破折號{dash_n}個")
    elif dash_n > 4:
        score += 1
        reasons.append(f"破折號{dash_n}個")
    # 觸檔即硬 gate（哲宇選項3）：pre-commit profile 設 emdash_hard_over 時，超量升 HARD。
    if emdash_hard_over is not None and dash_n > emdash_hard_over:
        yield Violation(
            check=CHECK_NAME,
            severity=Severity.HARD,
            message=(
                f"破折號連用超硬門檻：{dash_n} 處 > {emdash_hard_over}"
                f"（§quality-scan #8b HARD gate，2026-07-19 哲宇選項3 觸檔即硬）"
            ),
            editorial_ref="EDITORIAL.md §破折號 + MANIFESTO §11.2",
            fix_suggestion=(
                f"這是 pre-commit HARD gate：你改到的檔破折號必須降到 ≤ {emdash_hard_over}。"
                "改用「，即」「（）」「：」/ 分句 / 短句。（全站 legacy 仍 WARN 不擋，只有你觸碰的檔要清。）"
            ),
        )
    # Only itemize if over budget (> 8) — don't spam < 5 instances
    if dash_n > 8:
        for m in dash_matches[:10]:
            line_no = _line_at_offset(text_for_patterns, m.start())
            ctx = _context_around(text_for_patterns, m.start(), m.end(), before=15, after=15)
            yield Violation(
                check=CHECK_NAME,
                severity=Severity.WARN,
                message=f"破折號連用 (§quality-scan #8b 第 {dash_matches.index(m)+1}/{dash_n} 處)：{ctx}",
                line=line_no,
                snippet="——",
                editorial_ref="EDITORIAL.md §quality-scan #8b + MANIFESTO §11.2",
                fix_suggestion="改用「，即」「（）」「：」/ 分句 / 短句 / bullet",
            )

    # ── 8c. Semicolon density (；) — 2026-07-19 哲宇 directive ──
    # 排除腳註定義行（引用裝置，分號分隔多來源可接受）。text_for_patterns 已排除
    # code fence（tw-timeline/tw-bars 的 ；不算）+ URL。
    # 同 §8b：只數可編輯正文的分號（排除 blockquote/腳註/圖說/參考裝置等禁改合法區）。
    semi_matches = [m for m in _RE_SEMICOLON.finditer(text_for_patterns) if not _is_uneditable(m.start())]
    semi_n = len(semi_matches)
    if semi_n > 8:
        score += 2
        reasons.append(f"分號{semi_n}個")
    elif semi_n > 3:
        score += 1
        reasons.append(f"分號{semi_n}個")
    # 觸檔即硬 gate（哲宇選項3）：pre-commit profile 設 semicolon_hard_over 時，超量升 HARD。
    if semicolon_hard_over is not None and semi_n > semicolon_hard_over:
        yield Violation(
            check=CHECK_NAME,
            severity=Severity.HARD,
            message=(
                f"全形分號超硬門檻：{semi_n} 處 > {semicolon_hard_over}"
                f"（§quality-scan #8c HARD gate，2026-07-19 哲宇選項3 觸檔即硬）"
            ),
            editorial_ref="EDITORIAL.md §歐化語法 §分號",
            fix_suggestion=(
                f"這是 pre-commit HARD gate：你改到的檔全形分號必須降到 ≤ {semicolon_hard_over}。"
                "拆句號句 / 並列改頓號。（全站 legacy 仍 WARN 不擋，只有你觸碰的檔要清。）"
            ),
        )
    # 2026-08-04 哲宇 directive「中文幾乎不會用分號寫文章」：門檻 >3 降到 ≥1，
    # 第一顆就逐處 WARN 讓寫的人看見（計分門檻與 HARD gate 不動，全站 gate 行為不變）。
    if semi_n >= 1:
        for m in semi_matches[:10]:
            line_no = _line_at_offset(text_for_patterns, m.start())
            ctx = _context_around(text_for_patterns, m.start(), m.end(), before=18, after=18)
            yield Violation(
                check=CHECK_NAME,
                severity=Severity.WARN,
                message=f"全形分號 (§quality-scan #8c 第 {semi_matches.index(m)+1}/{semi_n} 處)：{ctx}",
                line=line_no,
                snippet="；",
                editorial_ref="EDITORIAL.md §歐化語法 §分號 + quality-scan #8c",
                fix_suggestion=(
                    "繁中散文少用全形分號（翻譯腔水印）。多數情況：前後子句拆成兩個句號句"
                    "（；→。），或並列項改頓號（、）。分號讀起來像論文/法律條文不像人話。"
                ),
            )

    # ── 8d. Run-on sentence / 華麗辭藻湯 (soft-launch WARN，不計分) — 哲宇 directive ──
    for off, seg, cjk, pauses in _detect_runon_sentences(text_for_patterns)[:8]:
        line_no = _line_at_offset(text_for_patterns, off)
        yield Violation(
            check=CHECK_NAME,
            severity=Severity.WARN,
            message=f"長句沒呼吸 (§quality-scan #8d {cjk}字/{pauses}個停頓)：{seg[:50]}…",
            line=line_no,
            snippet=seg[:80],
            editorial_ref="EDITORIAL.md §段落呼吸 + §歐化語法",
            fix_suggestion=(
                "這句塞太多逗號子句、太長，讀起來像堆修飾語的湯。在意義段落處斷成 2-3 個"
                "句號句；一句話講一件事，讓句子之間有呼吸。"
            ),
        )

    # ── 8e. 英文式短句開場 — 2026-08-19 起計分（哲宇 directive「未來嚴格執行歐化檢查」）──
    # ≥3 處 +1、≥6 處 +2：一篇散文長到一萬字出現三四處還算節奏，六處以上整篇就是英文段落
    # 骨架（今天那篇改稿前 15 處）。
    english_openers = _detect_english_openers(body)
    if len(english_openers) >= 6:
        score += 2
        reasons.append(f"英式短句開場{len(english_openers)}處")
    elif len(english_openers) >= 3:
        score += 1
        reasons.append(f"英式短句開場{len(english_openers)}處")
    # 觸檔即硬 gate（同 7/19 破折號／分號的 pre-commit 路徑）：profile 設 english_opener_hard_over
    # 時超量升 HARD。2026-08-19 校準：992 篇 zh 裡 >10 處只有 24 篇（97.6% ≤ 9），門檻 10 只
    # 會在你碰到那 24 篇時逼你順稿，新文章寫到 10 處以上就是整篇英文骨架。ci-deploy 不設。
    if english_opener_hard_over is not None and len(english_openers) > english_opener_hard_over:
        yield Violation(
            check=CHECK_NAME,
            severity=Severity.HARD,
            message=(
                f"英文式短句開場超硬門檻：{len(english_openers)} 處 > {english_opener_hard_over}"
                f"（§歐化第 9 病 HARD gate，2026-08-19 哲宇 directive「嚴格執行歐化檢查」）"
            ),
            editorial_ref="EDITORIAL.md §歐化語法 §英文式短句開場",
            fix_suggestion=(
                f"這是 pre-commit HARD gate：你改到的檔英式短句開場必須降到 ≤ {english_opener_hard_over}。"
                "逐處把短開場接進後句，或用具體人事時地起頭；下面 WARN 列了每一處。"
            ),
        )
    for off, opener, olen, nlen in english_openers[:12]:
        line_no = _line_at_offset(body, off)
        yield Violation(
            check=CHECK_NAME,
            severity=Severity.WARN,
            message=f"英文式短句開場 (§歐化第 9 病：開場{olen}字→段落展開{nlen}字)：「{opener}」",
            line=line_no,
            snippet=opener[:60],
            editorial_ref="EDITORIAL.md §歐化語法 §英文式短句開場",
            fix_suggestion=(
                "段落以一句短平述句定調再展開，是英文 topic-sentence 腔（哲宇 anti-example："
                "「協議並沒有收尾。自救會指控…」「這些翻譯很多是在我家跑的。我家裡有一張 3090…」）。"
                "中文自然行文直接流進主題：把短開場接進後句（「翻譯這一層有很大一部分是在我家跑的："
                "重型的策展工作交給雲端，翻譯本身就交給家裡那張 3090…」），或用具體人事時地的句子起頭。"
                "冒號引出引語（「我那天的收尾是：」）與日期起頭的場景句是中文本來的寫法，不算。"
            ),
        )

    # ── 8e-bis. 英式段首宣告慣用式 (soft-launch WARN，不計分) — round 2 簽名檔 ──
    for m in list(_RE_DECLARATIVE_OPENER_IDIOM.finditer(text_for_patterns))[:6]:
        line_no = _line_at_offset(text_for_patterns, m.start())
        ctx = _context_around(text_for_patterns, m.start(), m.end(), before=4, after=24)
        yield Violation(
            check=CHECK_NAME,
            severity=Severity.WARN,
            message=f"英式段首宣告慣用式 (§歐化：跨篇簽名檔)：{ctx}",
            line=line_no,
            snippet=m.group(0)[:40],
            editorial_ref="EDITORIAL.md §歐化語法 §英文式短句開場",
            fix_suggestion=(
                "「真正的轉折發生在⋯」全站 9 篇在用，已是模板（同「值得停下來看」22 篇）。"
                "把判斷融進資訊句：直接寫那一年發生了什麼，讓「這是轉折」由事件自己長出來。"
            ),
        )

    # ── 8f. 「是⋯的」cleft 長片語型 (WARN-only 意識層，2026-08-04) ──
    for m in list(_RE_CLEFT_LONG_PREDICATE.finditer(text_for_patterns))[:4]:
        if _backstage_line_is_legit_backstage(text_for_patterns, m.start()):
            continue  # blockquote 引語／腳註是別人的話或來源裝置
        line_no = _line_at_offset(text_for_patterns, m.start())
        yield Violation(
            check=CHECK_NAME,
            severity=Severity.WARN,
            message=f"「是⋯的」cleft 長片語 (§歐化第 7 病動詞片語型)：「{m.group(0)}」",
            line=line_no,
            snippet=m.group(0)[:40],
            editorial_ref="EDITORIAL.md §歐化語法 §「是 X 的」判斷句",
            fix_suggestion=(
                "「是＋長片語＋的＋句號」是英文 cleft 直譯。兩條改法：改動作句"
                "（「媒體多年轉述之間，慢慢把這四個字添了上去」）或讓「的」接名詞"
                "（「是⋯添上去的頭銜」）。⚠️ 出處交代型（「是徐賢修拍板的」）是"
                "合法強調句——本組是意識層，逐處人判。"
            ),
        )

    # ── 9. Textbook opening ──
    if _detect_textbook_opening(body):
        score += 2
        reasons.append("教科書開場")

    # ── 10. Formulaic ending ──
    if _detect_formulaic_ending(body):
        score += 2
        reasons.append("套路結尾")

    # ── 11. Template H2 ──
    template_h2 = _count_template_h2(body)
    if template_h2 >= 4:
        score += 3
        reasons.append(f"萬用H2×{template_h2}")
    elif template_h2 >= 3:
        score += 2
        reasons.append(f"萬用H2×{template_h2}")
    elif template_h2 >= 2:
        score += 1
        reasons.append(f"萬用H2×{template_h2}")

    # ── 12. LIST-DUMP (dimension id: "LIST-DUMP"; back-half bullet density
    # disproportionate to front) ──
    # is_hub 不排除：§14 QUALITY-DECAY（未在排除範圍內）也要讀這個旗標。
    is_hub = _is_hub_file(target)
    if "LIST-DUMP" not in exclude_dims:
        front_b, back_b, front_t, back_t = _bullet_ratios_split(body)
        if front_t > 0 and back_t > 0:
            front_ratio = front_b * 100 // front_t
            back_ratio = back_b * 100 // back_t
            if is_hub:
                # Hub pages naturally back-heavy index lists — relaxed
                if back_ratio > 60 and back_ratio > front_ratio * 3:
                    score += 1
                    reasons.append(f"後段清單堆砌{back_ratio}%(Hub)")
            else:
                if back_ratio > 40 and back_ratio > front_ratio * 2:
                    score += 3
                    reasons.append(f"後段清單堆砌{back_ratio}%")
                elif back_ratio > 30:
                    score += 2
                    reasons.append(f"後段清單堆砌{back_ratio}%")

    # ── 13. THIN (dimension id: "THIN"; H2 blocks with < 3 prose lines) ──
    if "THIN" not in exclude_dims:
        thin = _count_thin_blocks(body)
        if is_hub:
            if thin >= 4:
                score += 1
                reasons.append(f"稀薄段落×{thin}(Hub)")
        else:
            if thin >= 2:
                score += 2
                reasons.append(f"稀薄段落×{thin}")
            elif thin >= 1:
                score += 1
                reasons.append(f"稀薄段落×{thin}")

    # ── 14. QUALITY-DECAY (front prose ratio >> back prose ratio) ──
    fp, bp, fa, ba = _prose_ratios_split(body)
    if fa > 0 and ba > 0:
        front_pr = fp * 100 // fa
        back_pr = bp * 100 // ba
        if is_hub:
            if back_pr < front_pr // 4:
                score += 1
                reasons.append(f"品質衰退前{front_pr}%後{back_pr}%(Hub)")
        elif front_pr > 0:
            if back_pr < front_pr // 2:
                score += 3
                reasons.append(f"品質衰退前{front_pr}%後{back_pr}%")
            elif back_pr < (front_pr * 7) // 10:
                score += 1
                reasons.append(f"品質衰退前{front_pr}%後{back_pr}%")

    # ── 16. Citation desert (dimension id: "citation-desert") ──
    if "citation-desert" not in exclude_dims:
        fn_defs = _count_footnote_defs(body)
        word_count = _word_count(body)
        if fn_defs == 0:
            if word_count > 500:
                if urls == 0:
                    score += 4
                    reasons.append("引用荒漠(零腳註零URL)")
                else:
                    score += 2
                    reasons.append("引用荒漠(零腳註)")
            elif word_count > 200:
                score += 1
                reasons.append("無腳註")

    # ── Manifesto §11 Tier 1: 對位句型 ──
    # Emit per-match with line + 前後文 context so writers can locate fast
    # (per 2026-05-10 sad-shockley feedback: tool 應該直接指出哪裡 + 前後文).
    tier1_total = 0
    for pat in _TIER1_PATTERNS:
        matches = list(pat.finditer(text_for_patterns))
        if matches:
            tier1_total += len(matches)
            for m in matches:
                line_no = _line_at_offset(text_for_patterns, m.start())
                ctx = _context_around(text_for_patterns, m.start(), m.end())
                yield Violation(
                    check=CHECK_NAME,
                    severity=Severity.WARN,
                    message=f"對位句型 (§11 Tier 1)：{ctx}",
                    line=line_no,
                    snippet=m.group(0)[:80],
                    editorial_ref="MANIFESTO.md §11 Tier 1 對位句型禁令",
                    fix_suggestion=(
                        "三題判準 (MANIFESTO §11.1)：(1) 對比是內容本身嗎？(2) 正面主張能獨立站立嗎？"
                        "(3) 讀者真會預設 X 嗎？三題全 no = 改成正面斷言"
                    ),
                )

    # ── §11 Tier 1 補：強加對比的收束句 — 2026-07-19 哲宇 directive ──
    for m in _RE_FORCED_CONTRAST_CLOSER.finditer(text_for_patterns):
        line_no = _line_at_offset(text_for_patterns, m.start())
        ctx = _context_around(text_for_patterns, m.start(), m.end())
        yield Violation(
            check=CHECK_NAME,
            severity=Severity.WARN,
            message=f"強加對比收束句 (§11 Tier 1 散文變體)：{ctx}",
            line=line_no,
            snippet=m.group(0)[:60],
            editorial_ref="MANIFESTO.md §11 Tier 1 + EDITORIAL §對位句型",
            fix_suggestion=(
                "把並列的兩者硬拗成「其實是兩件事 / 兩本帳 / 不同的語言」是對位句型的散文變體："
                "作者用一個抽象對比幫段落強行收尾。改法：直接寫出兩者各自是什麼、差在哪的具體"
                "後果，不要用「根本是兩件事」這種抽象標籤代替說明。"
            ),
        )

    # ── 歐化「(不)是 X 的」判斷句 — 2026-06-07 哲宇 directive 儀器化 ──
    for m in _RE_EURO_DE.finditer(text_for_patterns):
        line_no = _line_at_offset(text_for_patterns, m.start())
        ctx = _context_around(text_for_patterns, m.start(), m.end())
        yield Violation(
            check=CHECK_NAME,
            severity=Severity.WARN,
            message=f"歐化「是…的」判斷句：{ctx}",
            line=line_no,
            snippet=m.group(0)[:40],
            editorial_ref="EDITORIAL.md §歐化語法 (是…的判斷句)",
            fix_suggestion=(
                "去掉「是…的」讓形容詞直接當謂語：「這個選址不是隨便的」→「這個選址不隨便」"
                "或「挑這裡有它的道理」；「答案是顯而易見的」→「答案顯而易見」。"
            ),
        )

    # ── Manifesto §11 Tier 2: AI metaphor ──
    tier2_total = sum(text_for_patterns.count(w) for w in _TIER2_WORDS)
    # 「重」當抽象份量隱喻：regex 逐處 WARN（給 line + ctx）+ 計入密度
    # 2026-06-04 哲宇 callout「把『很重』列為 AI 氾濫用語」
    weight_hits = list(_RE_WEIGHT_METAPHOR.finditer(text_for_patterns))
    for m in weight_hits:
        line_no = _line_at_offset(text_for_patterns, m.start())
        ctx = _context_around(text_for_patterns, m.start(), m.end())
        yield Violation(
            check=CHECK_NAME,
            severity=Severity.WARN,
            message=f"AI 份量隱喻「{m.group(0)}」(§11 Tier 2「重」當抽象份量)：{ctx}",
            line=line_no,
            snippet=m.group(0)[:80],
            editorial_ref="MANIFESTO.md §11 Tier 2",
            fix_suggestion=(
                "把抽象的「重」改成具體後果或畫面：「最重的一刻」→ 直接寫那一刻發生什麼／"
                "為什麼忘不掉；「份量很重」→「壓得人喘不過氣」或寫出具體代價。物理重量例外。"
            ),
        )
    tier2_total += len(weight_hits)
    if tier2_total >= 2:
        yield Violation(
            check=CHECK_NAME,
            severity=Severity.WARN,
            message=f"AI 抽象 metaphor 密度 (§11 Tier 2): 累計 {tier2_total} 處",
            editorial_ref="MANIFESTO.md §11 Tier 2",
        )

    # ── Manifesto §11 Tier 3: ritual 語 ──
    tier3_total = sum(text_for_patterns.count(p) for p in _TIER3_PHRASES)
    if tier3_total >= 1:
        yield Violation(
            check=CHECK_NAME,
            severity=Severity.WARN,
            message=f"AI ritual 句 (§11 Tier 3): 累計 {tier3_total} 處",
            editorial_ref="MANIFESTO.md §11 Tier 3",
        )

    # ════════════════════════════════════════════════════════════════
    # §盼望而不粉飾 (2026-06-15 哲宇 directive) — 全 WARN，不計 score budget
    # （跟 §11 Tier 1-3 一致：surface drift 但不擋既有 stage 閘）
    # ════════════════════════════════════════════════════════════════

    # ── 島嶼自稱密度 (balance, not ban) ──
    island_hits = list(_RE_ISLAND_EUPHEMISM.finditer(text_for_patterns))
    island_n = len(island_hits)
    taiwan_n = len(_RE_TAIWAN_REF.findall(text_for_patterns))
    # ratio-based：島嶼文學用法不罰，只抓「拿島當台灣的迴避稱呼」的 crutch。
    # 條件 = island 佔「島+台灣」國名指稱 > 1/4 (3×island > taiwan) 且 ≥ 3 次，
    # 或完全不稱台灣只用島 (≥ 2 次 + taiwan_n==0)。長文 5 島 vs 77 台灣 = 健康
    # 文學用法，不 flag（避免 instrument 哭狼，REFLEXES #24）。
    if (island_n >= 3 and 3 * island_n > taiwan_n) or (island_n >= 2 and taiwan_n == 0):
        for m in island_hits[:10]:
            line_no = _line_at_offset(text_for_patterns, m.start())
            ctx = _context_around(text_for_patterns, m.start(), m.end())
            yield Violation(
                check=CHECK_NAME,
                severity=Severity.WARN,
                message=f"島嶼自稱密度偏高 ({island_n} 處 vs 台灣 {taiwan_n} 處，§自稱)：{ctx}",
                line=line_no,
                snippet=m.group(0)[:40],
                editorial_ref="MANIFESTO.md §跟台灣的關係 §自稱 + EDITORIAL §六",
                fix_suggestion=(
                    "島嶼文學性可以保留，但不要過度——大多數時候大方寫「台灣」「臺灣」「這個國家」。"
                    "逐處判斷：曹永和「以島嶼為主體」島史脈絡（留），還是不敢寫台灣的迴避稱呼（換）？"
                ),
            )

    # （PUA 體 / 媒體焦慮體偵測器已移除 — 見檔頭 docstring + _RE_ISLAND 上方註解。
    #   語意判斷非句法特徵，regex 92-100% 假陽性，改人工判斷 by EDITORIAL §六。）

    # ── §後台洩漏 backstage leak (2026-08-03) — 全 WARN，不計 score ──
    for regex, label, fix_hint in _BACKSTAGE_DETECTORS:
        for m in list(regex.finditer(text_for_patterns))[:6]:
            line_no = _line_at_offset(text_for_patterns, m.start())
            ctx = _context_around(text_for_patterns, m.start(), m.end(), before=18, after=18)
            yield Violation(
                check=CHECK_NAME,
                severity=Severity.WARN,
                message=f"後台洩漏／{label}（§後台洩漏）：{ctx}",
                line=line_no,
                snippet=m.group(0)[:40],
                editorial_ref="EDITORIAL.md §六 §後台洩漏",
                fix_suggestion=fix_hint,
            )

    # 第六、七組（round 2）：跳過 blockquote／腳註——那是這些內容的合法的家
    for regex, label, fix_hint in _BACKSTAGE_DETECTORS_PROSE_ONLY:
        # ⚠️ 先排除再截斷（2026-08-08 修）：舊寫法 [:6] 先截斷、再做行級排除，
        # 前 6 個 match 若剛好都落在腳註／策展人筆記，正文的真違規就被靜默丟掉——
        # 豁免區把上限額度吃光，是 REFLEXES #24「工具在說謊」的假陰性型。
        _hits = [
            m
            for m in regex.finditer(text_for_patterns)
            if not _backstage_line_is_legit_backstage(text_for_patterns, m.start())
        ][:6]
        for m in _hits:
            line_no = _line_at_offset(text_for_patterns, m.start())
            ctx = _context_around(text_for_patterns, m.start(), m.end(), before=18, after=18)
            yield Violation(
                check=CHECK_NAME,
                severity=Severity.WARN,
                message=f"後台洩漏／{label}（§後台洩漏）：{ctx}",
                line=line_no,
                snippet=m.group(0)[:40],
                editorial_ref="EDITORIAL.md §六 §後台洩漏",
                fix_suggestion=fix_hint,
            )

    # 第十一形狀（2026-08-08）：掃描面相反——只掃腳註行。
    # 腳註是後台的合法的家，但合法的是證據狀態不是編輯動作（見 (j) 註解）。
    for regex, label, fix_hint in _BACKSTAGE_DETECTORS_FOOTNOTE_ONLY:
        _hits = [
            m
            for m in regex.finditer(text_for_patterns)
            if _backstage_line_is_footnote(text_for_patterns, m.start())
        ][:6]
        for m in _hits:
            line_no = _line_at_offset(text_for_patterns, m.start())
            ctx = _context_around(text_for_patterns, m.start(), m.end(), before=18, after=18)
            yield Violation(
                check=CHECK_NAME,
                severity=Severity.WARN,
                message=f"後台洩漏／{label}（§後台洩漏）：{ctx}",
                line=line_no,
                snippet=m.group(0)[:40],
                editorial_ref="EDITORIAL.md §六 §後台洩漏",
                fix_suggestion=fix_hint,
            )

    # ── §量詞隱喻「帳／本」(2026-08-08) — WARN；≥3 處另附論點警訊 ──
    _ledger = list(_RE_LEDGER_METAPHOR.finditer(text_for_patterns))
    # v2：家族擴張（付帳／筆帳／算進／算過／累積帳單／放回帳本），字面會計以 GUARD 濾除
    for _m in _RE_LEDGER_METAPHOR_EXT.finditer(text_for_patterns):
        _lo = max(0, _m.start() - 40)
        _hi = min(len(text_for_patterns), _m.end() + 40)
        if _RE_LEDGER_LITERAL_GUARD.search(text_for_patterns[_lo:_hi]):
            continue
        _ledger.append(_m)
    _ledger.sort(key=lambda mm: mm.start())
    for m in _ledger[:6]:
        line_no = _line_at_offset(text_for_patterns, m.start())
        ctx = _context_around(text_for_patterns, m.start(), m.end(), before=16, after=16)
        extra = ""
        if len(_ledger) >= 3:
            extra = (
                f"（全文 {len(_ledger)} 處——同一個抽象隱喻反覆敲，"
                "通常代表論點本身接不起來，正在用重複製造連貫感的假象。回頭檢查論點。）"
            )
        yield Violation(
            check=CHECK_NAME,
            severity=Severity.WARN,
            message=f"量詞隱喻「帳／本」（§量詞隱喻）：{ctx}",
            line=line_no,
            snippet=m.group(0)[:40],
            editorial_ref="EDITORIAL.md §六 §量詞隱喻",
            fix_suggestion=(
                "中文的「帳」不用「本」數，也不當可數的抽象物件。"
                "「三本帳都還開著」→ 直接寫那三件事各自的狀態；"
                "「連帳都沒有開的那些人」→ 寫「這些人的處境從來沒有被統計過」。"
                "⚠️ 把「帳」換成「算」不算改掉——「代價算進去了嗎」「沒有被算進任何一份統計」"
                "是同一個會計隱喻換衣服。判準：受詞是錢＝字面（合法），受詞是人的處境＝隱喻（改寫）。" + extra
            ),
        )

    # ── §英式接續「而」開頭句 (2026-08-08) — 密度 ≥4 才報 ──
    _er = list(_RE_ERSATZ_ER_LEAD.finditer(text_for_patterns))
    if len(_er) >= 4:
        for m in _er[:5]:
            line_no = _line_at_offset(text_for_patterns, m.start())
            ctx = _context_around(text_for_patterns, m.start(), m.end(), before=6, after=26)
            yield Violation(
                check=CHECK_NAME,
                severity=Severity.WARN,
                message=f"句首「而」接續（§英式接續，全文 {len(_er)} 處）：{ctx}",
                line=line_no,
                snippet=m.group(0)[:20],
                editorial_ref="EDITORIAL.md §六 §英式接續",
                fix_suggestion=(
                    "句首「而」是英文 And 的直譯接續。中文的「而」是句中轉折詞，"
                    "放句首當段落黏著劑是翻譯腔——而且它最常出現在前後兩句本來就接不起來、"
                    "需要一個詞把它們黏住的地方。刪掉「而」直接寫下一句；如果刪掉之後讀不通，"
                    "那不是連接詞的問題，是那兩句之間真的缺一個論證。"
                ),
            )

    # ════════════════════════════════════════════════════════════════
    # AI 痕跡 Tier 4 (speak-human-tw 轉譯, 2026-07-16 soft-launch)
    # 併入 score budget（跟 quality-scan §1-16 同一計分家族）。
    # ════════════════════════════════════════════════════════════════

    # ── (a) 立場真空：每 hit +1，上限 +2 ──
    stance_hits = list(_RE_STANCE_VACUUM.finditer(text_for_patterns))
    if stance_hits:
        score += min(len(stance_hits), _STANCE_VACUUM_SCORE_CAP)
        reasons.append(f"立場真空×{len(stance_hits)}")
        for m in stance_hits[:10]:
            line_no = _line_at_offset(text_for_patterns, m.start())
            ctx = _context_around(text_for_patterns, m.start(), m.end())
            yield Violation(
                check=CHECK_NAME,
                severity=Severity.WARN,
                message=f"立場真空 (§AI痕跡 Tier4-a「{m.group(0)}」)：{ctx}",
                line=line_no,
                snippet=m.group(0)[:40],
                editorial_ref="speak-human-tw #37/#30 + EDITORIAL.md",
                fix_suggestion="留判斷：文章自己的立場是什麼？把「見仁見智」換成具體斷言或明確標示為留待讀者判斷的理由。",
            )

    # ── (b) 價值上升詞密度：≥3 hits +1、≥6 +2 ──
    value_inflation_hits = list(_RE_VALUE_INFLATION.finditer(text_for_patterns))
    vi_n = len(value_inflation_hits)
    if vi_n >= 6:
        score += 2
        reasons.append(f"價值上升詞×{vi_n}")
    elif vi_n >= 3:
        score += 1
        reasons.append(f"價值上升詞×{vi_n}")
    if vi_n >= 3:
        yield Violation(
            check=CHECK_NAME,
            severity=Severity.WARN,
            message=f"價值上升詞密度 (§AI痕跡 Tier4-b): 累計 {vi_n} 處 (標誌著/見證了/彰顯了/體現了/突顯了/奠定...基礎/不可磨滅)",
            editorial_ref="speak-human-tw #37/#30 + EDITORIAL.md",
            fix_suggestion="改成具體描述事件本身，不用「標誌著/見證了」幫它加冕。",
        )

    # ── (c) 罐頭結尾起手式：最後 3 段出現任一 → +2 (fixed) ──
    if _detect_canned_ending_opener(body):
        score += 2
        reasons.append("罐頭結尾起手式")
        yield Violation(
            check=CHECK_NAME,
            severity=Severity.WARN,
            message="罐頭結尾起手式 (§AI痕跡 Tier4-c)：最後 3 段內出現「總的來說/綜上所述/總而言之/總結來說」",
            editorial_ref="speak-human-tw #37/#30 + EDITORIAL.md",
            fix_suggestion="拿掉起手式，讓收尾句直接說結論本身。",
        )

    # ── (d) 時代帽子開場：第一個 prose 段落以此開頭 → +2 (fixed) ──
    if _detect_time_hat_opening(body):
        score += 2
        reasons.append("時代帽子開場")
        yield Violation(
            check=CHECK_NAME,
            severity=Severity.WARN,
            message="時代帽子開場 (§AI痕跡 Tier4-d)：第一段以「在當今/在這個...的時代/隨著...的(快速)發展」開頭",
            editorial_ref="speak-human-tw #37/#30 + EDITORIAL.md",
            fix_suggestion="從具體的人事時地物開始，不要先戴一頂時代帽子。",
        )

    # ── (e) 假推論密度：「這意味著」≥2 hits +1 ──
    false_inference_n = text_for_patterns.count(_FALSE_INFERENCE_PHRASE)
    if false_inference_n >= _FALSE_INFERENCE_MIN_HITS:
        score += 1
        reasons.append(f"假推論密度×{false_inference_n}")
        yield Violation(
            check=CHECK_NAME,
            severity=Severity.WARN,
            message=f"假推論密度 (§AI痕跡 Tier4-e「這意味著」): 累計 {false_inference_n} 處",
            editorial_ref="speak-human-tw #37/#30 + EDITORIAL.md",
            fix_suggestion="檢查每一處「這意味著」後面的推論是否文章本身證據支撐，不是就直接寫因果，是就去掉這個轉折詞。",
        )

    # ── (f) 首先/其次/最後 三件套：同篇同時出現 → +1 ──
    has_first = "首先" in text_for_patterns
    has_second = "其次" in text_for_patterns
    has_last = ("最後" in text_for_patterns) or ("再者" in text_for_patterns)
    if has_first and has_second and has_last:
        score += 1
        reasons.append("首先其次三件套")
        yield Violation(
            check=CHECK_NAME,
            severity=Severity.WARN,
            message="首先/其次/最後 三件套 (§AI痕跡 Tier4-f)：同篇同時出現「首先」+「其次」+「最後/再者」",
            editorial_ref="speak-human-tw #37/#30 + EDITORIAL.md",
            fix_suggestion="改成敘事順序（時間/因果）串接，不用條列式接續詞堆疊。",
        )

    # ── Final score summary as a single violation ──
    # The runner can gate on score via profile.fail_on = "score-budget".
    #
    # Severity 依「有沒有超出預算」分流（2026-08-04）：在預算內的總分是**參考讀數**
    # （INFO），超出預算才是**要你動手的警告**（WARN）。2026-08-04 之前無條件 WARN，
    # 於是這一條同時承載兩種根本不同的意思——正是 REFLEXES #38「混維度」在 severity
    # 欄位上的 instance：任何 fail_on="warn" 的 profile 只要文章 score > 0 就必定 fail，
    # 而 score > 0 幾乎是所有文章的常態，gate 因此好壞不分、不帶資訊。
    #
    # 對既有 gate 零影響（已驗）：fail_on="score-budget" 走 article-health.py 的
    # `_prose_health_score()`，它從 fix_suggestion 的數字字串取值、不看 severity；
    # fail_on="hard" 只數 hard_count。唯一行為變化是 fail_on="warn"（release-pr）
    # 不再因「預算內的總分」誤擋——那是修正，因為 ≤ budget 的定義本來就是 pass。
    if score > 0:
        yield Violation(
            check=CHECK_NAME,
            severity=Severity.INFO if score <= score_budget else Severity.WARN,
            message=f"prose-health score: {score} (≤ {score_budget} = pass) — {'; '.join(reasons)}",
            editorial_ref=EDITORIAL_REF,
            fix_suggestion=str(score),  # used by score-budget gating
        )
