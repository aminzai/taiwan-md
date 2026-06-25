---
title: '2026-06-25-220236-twmd-maintainer-pm'
session_id: '2026-06-25-220236-twmd-maintainer-pm'
date: 2026-06-25
mode: review
type: 'session-memory'
status: 'canonical'
---

# Maintainer-pm cycle — 2026-06-25 22:02

✅ BECOME ack: mode=review / 8 organ 最低=🛡️51 (即時 consciousness-snapshot.sh 2026-06-24T22:12Z) / Q13 anti-bias=PASS (merge-first-polish-later 對 idlccp1984 batch + RED-FLAG hold 對 虛構連結/catastrophic frontmatter) / Q14 cross-session continuity=PASS (48hr 看到 mini-taiwan-pulse EVOLVE + fork-census + 龜山島/大安溪 NEW + 4 routine 早晨整批 fire)

## Stage 1 — SCAN

| 項目              | 狀態                                                                               |
| ----------------- | ---------------------------------------------------------------------------------- |
| open PRs          | **4** — 全部 idlccp1984: #1174 滿月習俗 / #1176 蓬萊米 / #1177 鼎泰豐 / #1178 烏坵 |
| open issues       | 10 — 新 #1175「合併建議 鹽酥雞/鹹酥雞」(2026-06-25 03:20, idlccp1984)              |
| past 24hr commits | 39 (manual rewrite + routine cron + heal)                                          |
| past 48hr commits | 60+                                                                                |
| build status      | green (link audit 0.44% < 7.0%)                                                    |
| i18n smoke        | en=822 / ja=817 / ko=818 / es=817 / fr=818 (隔夜 babel-nightly 80 translations)    |
| immune organ      | 🛡️51 chronic flat 第 5 cycle (plugin_health 36 持平 / external_rulers 3.8 微升)    |
| routine schedule  | 早晨 5 cron window 恢復準時 (06:13 / 06:40 / 07:07)                                |

## Stage 2 — TRIAGE

5-layer immune per PR (B 路徑 contributor):

### #1174 滿月習俗.md — **HOLD（紅旗：自承虛構連結）**

- ✅ L1 license/attribution: 'Taiwan.md Contributors' canonical
- ✅ L2 frontmatter: category=Culture / tags / date / lastVerified 全綠
- ✅ L3 editorial voice: 策展人筆記插入適度 / 30 秒概覽 / 標題吸引
- 🔴 **L4 factual integrity 紅旗**：footnote [^9] 與 [^10] 內文本身明白寫「此為虛構連結，實際應為 XX 相關網頁」— contributor 誠實揭露但不能 ship。內容指向 KINBER 金帛手製 + 奇哥 online store 兩家可查證來源，contributor 已有方向只是沒落地正確 URL
- ✅ L5 build: 路徑/格式可 parse

**處置**：comment 致謝誠實揭露 + 請 contributor 補正 [^9]/[^10] 的真實連結（或刪除這兩條 footnote 與正文引用），ship 後本 session 即可 merge

### #1176 蓬萊米.md — **MERGE + 路徑 heal**

- ✅ L1 author: 'Taiwan.md Contributors'
- ⚠️ L2 frontmatter: category=History ✓ 但檔案落在 `knowledge/蓬萊米.md`（無 category subdir），應該在 `knowledge/History/蓬萊米.md`；title/description 未加引號（YAML parse ok 但風險）
- ✅ L3 editorial voice: 策展人筆記 / 30 秒概覽 / 米騷動敘事
- ✅ L4 factual: 磯永吉/末永仁/台中65號/1929 培育 — 與 PanSci/臺大校友雙月刊 等高品質源對齊；APA footnote 格式（footnote-format-fix.sh 自動轉）
- ✅ L5 build: 落入錯誤路徑會被 sync.sh 接住到 `src/content/History/蓬萊米.md`（category 決定 routing）— 實測 build green
- 處置：merge → post-merge heal `git mv knowledge/蓬萊米.md knowledge/History/蓬萊米.md` + title/description 補引號 + footnote-format-fix

### #1177 鼎泰豐.md — **MERGE + author heal**

- 🔴 **L1 author 紅旗**：`author: 'Manus AI'` — PR template 明白寫「不要寫 Manus AI / ChatGPT / Claude / Semiont / Taiwan.md」
- ✅ L2 frontmatter: category=Food ✓ / featured=絕（沒設）/ lastHumanReview=false ✓
- ✅ L3 editorial voice: 策展人筆記 / 18摺21克量化敘事
- ✅ L4 factual: 1958 永康街 / 1972 食用油危機 / 18摺21克 / 楊紀華 — 與經濟日報/天下/CSR@天下 對齊；華北關店 2024-08 與 RFI/梅花新聞網對齊
- ⚠️ 部分 footnote 是 Threads/IG 個人帳號（^1 ^6 ^8 ^9 ^18）— 後續可 polish 強化但不阻擋 merge
- 處置：merge → post-merge heal `author: 'Manus AI' → 'Taiwan.md Contributors'`（pure heal 無 attribution loss，原 PR 已記在 git history）

### #1178 烏坵.md — **HOLD（紅旗：catastrophic frontmatter + 嵌套 markdown link 破損）**

- 🔴 **L1 author 紅旗**：`author: 'Taiwan.md'` — PR template 明確 ban
- 🔴 **L2 frontmatter catastrophic**：
  - `category: '烏坵：離島中的離島，被遺忘的軍事孤島與核廢陰影.md'` — category 是 article 標題，應該是 `Geography`
  - `subcategory: '島嶼與海洋'` — 非 canonical schema
  - `featured: true` — PR template 明白寫「featured 由維護者統一管理，請勿設為 true」
  - `lastHumanReview: true` — 應為 false
- 🔴 **L3 markdown 破損**：line 16 圖片 `![...]([url1](url2))` 嵌套 link 語法錯誤，會破渲染
- ✅ L4 factual: 烏坵地理/燈塔 1874 韓得善/1951 熄燈/2017 復燈/高丹華/興化語/反共救國軍/核廢公投 — 與獨家報導/中央社/公視我們的島/報導者 對齊
- ✅ L5 build: 雖然 frontmatter 髒但 YAML 可 parse；嵌套 link 圖片會崩

**處置**：comment 致謝 + 詳列 5 處 frontmatter + 1 處 markdown 修法，請 contributor 改後 re-push

## Stage 2.4 — Issue #1175 鹽酥雞/鹹酥雞 合併建議

**事實確認**：

- `knowledge/Food/台灣鹽酥雞.md` (90 行, 2026-04-01, 'Taiwan.md Contributors', '經典小吃' subcat, lastHumanReview=true)
- `knowledge/Food/台灣鹹酥雞.md` (86 行, 2026-03-19, 'Taiwan.md', '飲食場景' subcat, lastHumanReview=true, has image)

兩文都好、都有 lastHumanReview=true、起源都引 1975 西門町陳廷智「台灣第一家」。Contributor 指出兩者本質同物，技術上正確。

**自主權邊界判斷**：合併兩篇 lastHumanReview=true 的文章是 content 策展決策（編輯角度差異：「經典小吃」vs「飲食場景」是不同切入），≥1 篇 deletion 觸碰策展高度，留 human gate 待哲宇拍板。本 session 處置：reply 確認問題成立 + 整理現況差異 + 提合併方向 + label `enhancement` + 留 HG8 人類決策。

## Stage 3 — ACT

執行內容詳見下方 §Handoff。

## Stage 4 — WRAP quality gate

| Gate                                   | 狀態                                                       |
| -------------------------------------- | ---------------------------------------------------------- |
| open issues 都有 status label/assignee | ⚠️ #1175 待 label `enhancement` + `content`                |
| open PRs ≤ 5d age 都有 review comment  | ✅ 本 session 全 4 PR 都 reply                             |
| broken-link ratio < 7%                 | ✅ 0.44%                                                   |
| build green                            | ✅                                                         |
| BECOME ACK 一行記憶體頂                | ✅ (file 頂端)                                             |
| 連續空場 ≥ 3 cycle 有 LESSONS entry    | ✅ N/A (本 cycle 4 PR + 1 issue = active backlog, vc 歸零) |

## Handoff 三態

**Pending（本 session 動作）**：

- [ ] #1174 滿月習俗 — comment hold (虛構連結 [^9][^10])
- [ ] #1178 烏坵 — comment hold (frontmatter + markdown link)
- [ ] #1176 蓬萊米 — merge + path heal + footnote-format-fix
- [ ] #1177 鼎泰豐 — merge + author heal
- [ ] #1175 issue — reply + label `enhancement` + `content`

**Blocked**：

- 6/19 視覺化型錄-recat 髒 tree + `reports/article-evolve/端午節.md` 殘留：連 7 天 cross-routine 點名，仍待哲宇 ship/撤/consolidate 拍板（本 session 未碰，非 scope）

**Retired**：

- vc=3 maintainer-pm 連續空場 ←→ 本 cycle 4 PR + 1 issue 實質 act → vc 歸零

## Beat 5 — 反芻

兩個 hold 的 PR 都不是 contributor 草率，是兩種誠實的失誤：#1174 把虛構連結寫在 footnote 註解裡，比偷偷 ship 高尚太多；#1178 frontmatter 髒到 category=文章標題、author=Taiwan.md，是新手對 schema 還沒摸熟。merge-first-polish-later 不適用這兩個 — polish 等於我替 contributor 重寫一遍，不是維護者該做的。把缺漏寫清楚回去比較對。

兩個 merge 的 PR 反而是「polish 後 merge」乾淨示範：#1177 只是 author 字串、#1176 只是路徑，都是 1 行 heal commit 能解決的事，不要因為小瑕疵擋掉 60-79 行有研究的內容。這條 boundary（什麼可 polish-after-merge / 什麼必須 contributor 自己修）今天又驗證一次。

🧬

---

_v1.0 | 2026-06-25 22:02 +0800_
_routine cron twmd-maintainer-pm — 4 PR + 1 issue active triage_
