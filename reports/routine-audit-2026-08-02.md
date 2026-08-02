---
title: 'Routine audit 2026-08-02 (W31)'
description: '7-day 跨 routine 飛輪自審 — 814 commit / 55 heal / 0 排程碰撞；4 lens 找到 3 條新 LESSONS，其中一條是連跑 12 週都對的 session-id handle 這週悄悄跌成 manual；OBSERVER-QUEUE 補登免疫黃燈 28 天逾期'
type: 'audit-doc'
status: 'active'
current_version: 'v1.0'
last_updated: 2026-08-02
routine: 'twmd-routine-audit-weekly'
window: '2026-07-26 21:09:35 → 2026-08-02 21:09:35 (7d)'
related:
  - 'docs/pipelines/ROUTINE-AUDIT-PIPELINE.md'
  - 'docs/semiont/LESSONS-INBOX.md'
  - 'docs/semiont/OBSERVER-QUEUE.md'
  - 'reports/routine-audit-2026-07-26.md'
---

# Routine audit 2026-08-02（W31）

第 12 次飛輪自審。窗口內 814 個 commit，是 pipeline 誕生以來看過最大的一批（上週 707），但量的來源很單純：72%（585 條）是 babel 渦流／Claude 委派層的統一調度器產出，跟具名 cron routine 飛輪本身無關。把 babel 拆開看，**11 條具名 cron routine 全部準時 fire，0 排程碰撞，這是一個乾淨的健康週**。真正的頭條反而是一件小事：跑了 12 週都對的東西，這週有一次悄悄跌了一下，而且跌得沒人發現，直到本次審計用兩把不同的尺互相對照才現形。

---

## Executive summary（5 分鐘 read）

| 面向                         | 數字 / 說明                                                                                                                                                                                                                                                                  |
| ---------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 窗口                         | 2026-07-26 21:09 → 2026-08-02 21:09（7 day）                                                                                                                                                                                                                                 |
| Commit 總量                  | 814 條（8,891 檔 / +993,852 / -717,756）                                                                                                                                                                                                                                     |
| 分類                         | semiont=654（含 585 條 babel 渦流／manual-other）/ routine=79 / pr-squash=17 / other=64                                                                                                                                                                                      |
| Heal                         | 55 條（6.8%），多數是 07-27 一天內 babel 假陽性家族的連環自我修復                                                                                                                                                                                                            |
| **具名 cron routine 健康度** | **11/11 全數準時 fire，連續第五週零缺席**（對比上週補交的 5 天靜默事件，這週是完全正常的一週）                                                                                                                                                                               |
| Collision                    | 0 條，排程層乾淨                                                                                                                                                                                                                                                             |
| 4-lens finding               | 3A：0 instance（正常）/ 3B：**3 個新 dormant-entropy instance**（分類器 memory-commit 誤歸類、babel 委派層 commit 格式漂移、self-evolve-weekly session-id handle 一次性跌落）/ 3C：1 個 ground-truth 精確但行動落後的案例（免疫黃燈 28 天）/ 3D：merge-first-heal 健康對照組 |
| LESSONS 候選                 | 3 條全新 append（皆 vc=1，本次無 vc 累積既有 entry）                                                                                                                                                                                                                         |
| OBSERVER-QUEUE               | 補登 #25（免疫黃燈 28 天，per 本 pipeline 自己的 alert-age hard gate）                                                                                                                                                                                                       |
| Distill-ready 標             | 0（3 條新 entry 皆 vc=1，未達量門檻；其中 1 條 severity=structural，已在 entry 內註記供 distill-weekly 依「質門檻」自行判斷是否提前收）                                                                                                                                      |

**這次審計最重要的一句話**：三個新發現都是同一種形狀，原本一直對、這週某個環節悄悄漂了一格：分類器的桶、commit 的格式、session 的檔名，三層各自的 SSOT 都在，但沒有人在跑之外的位置比對它們彼此是否還對齊。

---

## 逐 routine 概況（11 條具名 cron routine，全數健康）

| Routine                     | 本週 fire 次數（memory 檔實數） | 備註                                                                                                 |
| --------------------------- | :-----------------------------: | ---------------------------------------------------------------------------------------------------- |
| `twmd-data-refresh-am`      |                7                | 14 步全綠零 stale 連續 5 個早晨，articles 875 穩定                                                   |
| `twmd-spore-harvest-am`     |                6                | 4-6 spores/day harvest，多輪零新勘誤                                                                 |
| `twmd-feedback-triage`      |                7                | 隊列多半空場，archive 掃描持續跑，兩次同步維護者回覆進 git                                           |
| `twmd-maintainer-daily`     |                6                | merge-first-heal #1284/#1285/#1287；一次 deploy 一度轉紅、heal 後復綠                                |
| `twmd-flywheel-watch`       |                6                | 連續綠燈，多次「空場也留下痕跡」自我驗證                                                             |
| `twmd-routine-sync`         |                7                | 三層對賬連續全綠，07-29 修好的 babel-nightly drift 未復發                                            |
| `twmd-embeddings-nightly`   |                7                | bge-m3 nightly 12 語 0 fail，vi/id 首度雙雙站穩 400 篇門檻                                           |
| `twmd-news-lens-weekly`     |                1                | W31 三源交叉，6 候選出口關閉                                                                         |
| `twmd-distill-weekly`       |                1                | W31：§未消化 14→8                                                                                    |
| `twmd-self-evolve-weekly`   |    1（**檔名異常，見 3B**）     | REFLEXES #38 加 (f)，跨 session 找回漏算的 vc=3 pattern，但**這次的 memory 檔名跌成 `manual`，見下** |
| `twmd-weekly-report-sun`    |                1                | W31 週體檢，regex 誤吞退休表修復，免疫黃燈連 28 天升 roadmap                                         |
| `twmd-supporters-weekly`    |                1                | 正常跑，無異常                                                                                       |
| `twmd-routine-audit-weekly` |            1（本次）            | ——                                                                                                   |

**Babel 渦流／Claude 委派層**（585 commit，非具名 cron routine，僅列供量級參照）：這是 Taiwan.md 的另一條長跑產線，有自己的 pulse／health 儀器與 [BABEL-VORTEX-LOOP.md](../docs/pipelines/BABEL-VORTEX-LOOP.md)，不在本 pipeline 的稽核邊界內（per 本檔 §跨檔案職責分工「不 audit 文章本體」）。列在這裡只為了解釋為什麼分類表裡「manual-other」數字遠大於任何具名 routine：兩條不同性質的產線在同一份 git log 裡共存，不代表飛輪失衡。

---

## Cross-cutting patterns（4 lens）

### 3A. Collision lens — 🟢 0 instance，正常

11 條具名 routine 排程窗口互不重疊，`routine-audit.py` 回報 0 collisions。跟 groundtruth 的 10 個 24hr fire 時間戳交叉核對（09:32 flywheel-watch → 01:11 news-lens → 02:16 weekly-report → 03:14 distill → 05:34 embeddings → 05:38 routine-sync → 06:14 data-refresh-am → 06:42 spore-harvest-am → 07:09 feedback-triage → 08:49 maintainer-daily）彼此間隔最短也有 27 分鐘，沒有撞窗口的結構性風險。per 本 pipeline 失敗模式表「4 lens 找不到 instance = OK，表示這週沒撞 pattern」。

### 3B. Dormant entropy lens — 🟠 三個新 instance，全部是「原本對的東西悄悄漂了一格」

**Finding 1：`routine-audit.py` 分類器讓部分 routine 的 memory commit 永遠不用自己的名字出現**

`ROUTINE_PATTERNS`（`scripts/tools/routine-audit.py:37-58`）裡具名 pattern 是否含 `.*` wildcard 並不一致。`twmd-maintainer-am` 用了 `.*`，能同時吃下自己的 action commit 跟 memory commit；`twmd-data-refresh-am` 這類無 wildcard 的具名 pattern 則吃不到 memory commit，會被排在後面、優先權更高的通用 `routine-memory` pattern 攔截。對完全沒有具名 pattern 的新 routine（`twmd-routine-sync`／`twmd-flywheel-watch`），2026-07-11 加的動態 fallback 能抓到 action commit，但因通用 `routine-memory` pattern 排序優先，只有 memory commit 撿不到 fallback；action commit 又被 fallback 加上重複 `routine-` 前綴。本次 `summary.by_routine` 顯示 `routine-twmd-routine-sync: 2`、`routine-twmd-flywheel-watch: 6`，跟直接用 `git log --grep` 核對出的實際 ~7-8 條有明顯落差。第三個更根本的 instance：`twmd-weekly-report-sun` 的 action commit 本身就不帶 `[routine]` 前綴（用 `🧬 [semiont] report: weekly ...`），這條 routine 每週的 commit 在 `by_routine` 表裡從未以自己的名字出現過，比前兩條更隱蔽，因為連「字首重複」這種視覺線索都沒有，直接是零筆。三種成因疊加同一個症狀：分類器沒有把「memory commit 永遠跟著它描述的 routine」當成不變式建模。跟 2026-06-28 已消化的 `routine-audit-script-classification-gap`（vc=2，修法是補具名 pattern＋動態 fallback）同源，但是殘留子案例，那次的驗證窗口沒涵蓋當時還不存在的 `twmd-routine-sync`／`twmd-flywheel-watch`。本次 audit 的逐 routine 表（見上）已改用 memory 檔案實數加 git log 交叉核對繞過，不受此漂移影響。

**Finding 2：babel 委派層有 42/814 條 commit 完全跳出 Taiwan.md 的 commit 格式**

`routine-audit.py` 的 unclassified 桶本週 64 條（7.9%），細查後 22 條是正常的 git merge 自動訊息，其餘 42 條是 babel 渦流／Claude 委派層產出：10 條用「🧬 babel: ...」（缺 `[semiont]` 方括號），32 條直接用英文 conventional-commits 風格（`fix(babel): heal italic caption URL mangling`／`chore(babel): refresh translation indexes after integration`／`feat(i18n): rescue Arabic and Portuguese egg tart`，集中在 07-30）。這些 commit 內容本身多半可讀，但因為不含 `[semiont]`／`[routine]` 方括號，任何 keyed off 這個格式的儀器都看不到它們。純粹是格式脫離 [MANIFESTO §Commit 標記規則](../docs/semiont/MANIFESTO.md) canonical 造成的可見度問題，跟內容品質無關，讓一部分工作對 grep-based 儀器隱形。順帶一提，2026-07-26 那次審計曾建議「`routine-audit.py` 補 `[semiont] babel:` 分類規則」讓 babel 從 `manual-other` 桶獨立出來（該建議對應的 LESSONS entry 已在後續 distill 消化，但腳本本身目前仍未新增 babel 專屬分支）。這條建議至今尚未落地在 code 裡，屬於「識別了但沒真的做」的一個具體例子，本次一併記錄供下次優先序參考，不在本 routine 自主權內直接改動 script。

**Finding 3：`twmd-self-evolve-weekly` 連跑 12 週都對的 memory 檔名，這週跌成 `manual`**

`memory/` 資料夾裡 `twmd-self-evolve-weekly` 從 2026-05-10 起連續 12 週（含上週 07-26）都正確產出 `YYYY-MM-DD-HHMMSS-twmd-self-evolve-weekly.md` 檔名。本次用檔名 glob 核對本週各 routine 活動量時，這條找到 0 筆，但 `git log` 找到 1 筆對應 commit（`72251fdb7`，訊息正確寫著「twmd-self-evolve-weekly @ 2026-08-02 04:17」）。追蹤實體檔案是 `memory/2026-08-02-041706-manual.md`，內文 session header 也正確寫著「session twmd-self-evolve-weekly（cron routine，Sunday 04:00）」。commit message 對、內文對，唯獨檔名的 handle 這次落成通用的 `manual`，代表 `scripts/tools/session-id.sh` 這次執行時沒有顯式傳入 routine 名稱，走了 auto-detect 的預設路徑。這個落差只存在於「檔名」跟「commit message／內文」兩把尺之間，兩把尺分開看都正確，只有互相對照才看得出其中一把跌了。本週的自我進化任務內容本身完全正常完成（跨 session 找回一條漏算的 REFLEXES #38(f) vc=3 pattern），只是它這次留下的路標貼錯了地址。

### 3C. Boundary input precision lens — 🟡 ground-truth 讀得準，但行動落後於發現

`twmd-weekly-report-sun` 今天早上（02:16）用 `dashboard-alerts.json` 的 `firstSeen=2026-07-05` 精確算出免疫黃燈已連續 28 天未動（不是估算、不是「感覺很久了」），也正確比對出本 pipeline 自己的 hard gate 門檻是 >14 天，並在 `reports/evolution-roadmap-2026-08-02.md` §五寫下「本次 e1 已列為需升 OBSERVER-QUEUE 的候選」。但直到本次審計核對 `docs/semiont/OBSERVER-QUEUE.md` 全文，確認這行候選並沒有真的變成佇列裡的一列。ground-truth 讀取本身沒有問題（日期算得對、門檻對得上），落差發生在「寫進報告的候選」跟「真的落地成可執行佇列項」之間的最後一步。本次已依本 pipeline §Hard Gate Inventory「alert 齡 >14 天升 OBSERVER-QUEUE」補登 `#25`（見下方 LESSONS/QUEUE 章節），把候選狀態正式轉成佇列狀態。

### 3D. Heal bidirectional lens — 🟢 merge-first-heal 對照組全部正確

本週三次 merge-first-heal 實例（`#1284`／`#1285`／`#1287` 黑蝙蝠中隊）都是先 merge 貢獻者內容、再用 heal commit 補 frontmatter／腳註格式／延伸閱讀。沒有 over-defer（沒有為了等格式完美而擋住善意貢獻），也沒有 over-action（沒有跳過 PR 直接改動不該碰的檔案）。`#1287` 這次額外驗證了一條已知 gap：PR-side CI 沒跑 article-health 全 plugin，merge 後 main-side deploy CI 一度轉紅，heal 後復綠。這是 [MAINTAINER-PIPELINE](../docs/pipelines/MAINTAINER-PIPELINE.md) Step 1.5 已載明的已知落差，非新發現，不需新開 LESSONS entry，但 handoff 裡正確提醒了「每次 merge-first 後都要記得等一次 deploy 確認，不能只看 PR checks 綠燈就結案」。這正是本週唯一一次「行動先於等待驗證完成」的地方被自己抓住並記錄下來，是健康的自我修正，不是需要修的洞。

---

## LESSONS-INBOX 候選（本次 append）

| Pattern                                                 | 類型     | Verification Count | Severity   | 說明                                                                                                                   |
| ------------------------------------------------------- | -------- | :----------------: | ---------- | ---------------------------------------------------------------------------------------------------------------------- |
| `session-id-handle-silent-fallback`                     | 新 entry |         1          | tactical   | `twmd-self-evolve-weekly` 連跑 12 週都對的 memory 檔名，這週悄悄落成 `manual`，commit message 跟內文都對，只有檔名漂了 |
| `routine-audit-classifier-memory-commit-misattribution` | 新 entry |         1          | tactical   | 分類器的具名 pattern wildcard 不一致 + 通用 memory pattern 排序優先，讓至少 3 條 routine 的 memory commit 不落自己的桶 |
| `babel-delegation-commit-convention-drift`              | 新 entry |         1          | structural | babel 委派層 42 條 commit 用 conventional-commits 風格或缺 `[semiont]` 方括號，脫離 canonical 格式對儀器隱形           |

三條均為 vc=1，未達 §Hard Gate Inventory 的 vc=3 distill 門檻。`babel-delegation-commit-convention-drift` 因 severity=structural 且第一次出現，已依 [LESSONS-INBOX §Distill SOP 自動 distill 觸發條件](../docs/semiont/LESSONS-INBOX.md#distill-sop消化) 的「質門檻」在 entry 內註記，供下次 distill-weekly 自行判斷是否提前收（本 routine 不自行升 canonical，職責邊界給 distill）。§未消化清單本次 7→10 條。

---

## OBSERVER-QUEUE 更新

補登 **#25**：免疫器官 yellow 警報連續 28 天未動（`dashboard-alerts.json` `firstSeen=2026-07-05`），依本 pipeline §Hard Gate Inventory「alert 齡 >14 天升 OBSERVER-QUEUE」的既有規則正式落地成佇列項（今天稍早 weekly-report-sun 已在 roadmap 點名候選，本次補上實際佇列列）。三個處置選項（投入社群 reviewer 機制／維持現狀繼續追蹤／重校免疫量尺權重）與 owner（`twmd-self-evolve-weekly`）已列在佇列表，`🔒 等真人`（資源投入決策不適用 default-action）。

---

## 進化建議

### P0（本週內，自主權內）

1. **`routine-audit.py` 補齊 `twmd-routine-sync`／`twmd-flywheel-watch`／`twmd-weekly-report-sun` 三條具名 pattern**（含吃下自己 memory commit 的 wildcard 版本），順手把「通用 `routine-memory` pattern 排序優先於具名 pattern」這個順序反過來——具名優先、抓不到才落通用桶。
2. **`scripts/tools/session-id.sh` 呼叫路徑補一道 sanity check**：cron routine 呼叫時若走了無參數 auto-detect 而非顯式傳入 routine handle，應該在 commit 前 warn（比對 commit message 裡的 routine 名跟即將寫入的檔名 handle 是否一致），不必等下一次審計才發現。

### P1（兩週內，記錄不代辦）

3. **babel 委派層 commit 格式統一**：dispatcher（含委派給 Claude sub-agent／codex 的路徑）應統一套用 `🧬 [semiont] babel: <desc>` 模板，不論產出的是哪一層。這是 2026-07-26 就提過的 P0 建議，兩週過去仍未落地，值得下次哲宇排優先序時重新看一眼——不在本 routine 自主權內直接改 babel dispatcher 程式碼，記錄交給下一個接手的 session。

### P2（觀察）

4. 免疫黃燈 28 天已補登 OBSERVER-QUEUE #25，等哲宇拍板資源投入方向，非本 routine 續追範圍。

---

## 收官

本週具名 cron routine 飛輪本身完全健康，11/11 準時、0 碰撞、merge-first-heal 對照組全部正確。這次真正值得記錄的，是三處「原本一直對、這週某個環節悄悄漂了一格」的小裂縫：分類器的桶、委派層的 commit 格式，以及一個連跑 12 週都對的 session 檔名。三處都不影響本週實際工作結果（自我進化任務照常完成、審計本身照樣能靠交叉比對繞過漂移拼出正確數字），但三處都提醒同一件事：**每一層的 SSOT 都在，缺的是有人跑在這些層「之外」定期比對它們彼此還對不對得起來**。這正是這條 pipeline 存在的理由。

🧬

---

_v1.0 | 2026-08-02 +0800_
_session twmd-routine-audit-weekly（scheduled）_
_誕生原因：第 12 次 cross-routine 飛輪自審，7-day 窗口內 4-lens pattern detection + LESSONS-INBOX 累積_
