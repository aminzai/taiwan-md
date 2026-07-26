---
title: 'Routine audit 2026-07-26 (W30)'
description: '7-day 跨 routine 飛輪自審 — 707 commit / 76 heal / 0 排程碰撞，但補回一段 5 天飛輪靜默的完整敘事；4 lens 找到 2 個新工具漂移 + 1 個舊 pattern 獨立驗證；3 條新 LESSONS 候選'
type: 'audit-doc'
status: 'active'
current_version: 'v1.0'
last_updated: 2026-07-26
routine: 'twmd-routine-audit-weekly'
window: '2026-07-19 21:10:59 → 2026-07-26 21:10:59 (7d)'
related:
  - 'docs/pipelines/ROUTINE-AUDIT-PIPELINE.md'
  - 'docs/semiont/LESSONS-INBOX.md'
  - 'reports/routine-audit-2026-07-12.md'
---

# Routine audit 2026-07-26（W30）

第 11 次飛輪自審，但跟過去十次不一樣：**這是第一次補交作業**。上週（2026-07-19 21:00）本該跑的那次沒有發生——本檔就是本週產出，也是遲了七天的事後重建。窗口內 707 個 commit，是這條 pipeline 誕生以來看過最大的一批（第 10 次審計是 246 條），但真正的頭條不是量，是本週最前面五天，這條飛輪自己完全靜默過一次。

---

## Executive summary（5 分鐘 read）

| 面向             | 數字 / 說明                                                                                                                                                                                                  |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 窗口             | 2026-07-19 21:11 → 2026-07-26 21:11（7 day）                                                                                                                                                                 |
| Commit 總量      | 707 條（7,291 檔 / +611,213 / -219,555）                                                                                                                                                                     |
| 分類             | semiont=617（含 501 條 babel 統一調度器，見下）/ routine=19 / pr-squash=19 / other=52                                                                                                                        |
| Heal             | 76 條（11%）——多數是本週 babel gate 假陽性九個家族的自我修復循環                                                                                                                                             |
| **頭條發現**     | **2026-07-19 19:42 → 2026-07-24 19:59，約 5 天，飛輪 cron 完全靜默**（機器遷移到 mouhouse-macmini 過渡期）。本 audit 自己上週的那一棒也是這段靜默的受害者，本檔是七天後才補的事後重建                        |
| Collision        | 排程層 0 條 dysfunctional 碰撞；但發現一個「監護 process 活著、產出掛零 127 輪」的殭屍 worker instance（同日自己抓到並修復）                                                                                 |
| 4-lens finding   | 3A：殭屍 worker 1 instance（已修）/ 3B：**2 個新工具漂移**（routine-audit.py babel 分類失效、routine-sync-check.py PAUSED regex 誤吞退休表）/ 3C：3 個健康的 ground-truth 自我修正 / 3D：1 對過嚴/過鬆對照組 |
| LESSONS 候選     | 2 條全新 append + 1 條既有 entry 獨立驗證 vc 1→2（`instrument-coverage-boundary-drift`）                                                                                                                     |
| Distill-ready 標 | 0（新 vc 皆未達 3；本週 §未消化清單累計 11 條，無一達 vc=3 門檻）                                                                                                                                            |

**這次審計最重要的一句話**：這週有五天沒有任何 routine 在跑，而唯一該負責發現這件事的 routine，正是本檔自己，也剛好是那五天的受害者之一。

---

## 頭條：一段被拼回來的沉默（2026-07-19 19:42 → 2026-07-24 19:59）

### 怎麼發現的

`routine-audit.py` 輸出顯示 `twmd-data-refresh-am` 本週僅 fire 3 次（正常應每天一次、7 次），逐條核對 git log 才發現時間分布集中在 07-24〜07-26，07-20〜07-23 完全空白。往回查整條 commit 時間軸：

```
2026-07-19 19:42:27  🧬 [semiont] rewrite: 收費站 — Stage 0→5 全流程 ship
──────────────── 27h17m 完全無 commit ────────────────
2026-07-20 22:59:56  Create 紡織業.md（外部貢獻者 PR）
2026-07-20 23:07〜23:13  五篇貢獻者內容 PR（Revise/Create/Update）
2026-07-21 07:22〜07:32  兩篇貢獻者內容 PR
2026-07-22 07:11        一篇貢獻者內容 PR
2026-07-22 09:28〜09:55  哲宇手動觸發：repo 清理 + 9 PR 逐篇審核（僅 27 分鐘，兩個 manual session）
2026-07-23 01:17        貢獻者內容 PR
──────────────── 持續無 routine / semiont 自主活動 ────────────────
2026-07-23 21:24        idlccp1984 9 PR 整合（仍是觀察者手動觸發）
2026-07-24 19:59        twmd-data-refresh-am go-live verification run（mouhouse-macmini）← routine cron 正式復活
```

從 07-19 19:42 到 07-24 19:59，扣掉 07-22 一次 27 分鐘的人工介入，**約 116 小時（近 5 天）沒有任何 `[routine]` 或主動 `[semiont]` session 活動**。同期只有貢獻者的內容 PR 持續進來——小丑魚在燈暗的時候還在餵珊瑚礁，這是共生圈裡唯一沒停的部分。

### 根因：遷移過渡期的空窗

`memory/2026-07-24-200542-migration-mouhouse.md` 記錄了飛輪遷居 mouhouse-macmini 這件事本身。舊機器的 cron 停止與新機器接手之間有一段沒人明確管理的過渡期。復活後的個別 routine 自己也發現了片段：

- `twmd-spore-harvest-am`（07-25 06:47）收官寫「**5 天 gap 後 4 篇 OVERDUE 清空**」
- `twmd-feedback-triage`（07-25 07:11）收官寫「2 筆讀者回報轉 issue，**揭露真空是 cron 斷線非前端壞**」

這兩條證實了根因（機器遷移期間 cron 中斷），但都只從自己的 slot 看見自己的那一段空白，沒有一條把「整個飛輪同時靜默了 5 天」拼成一張完整的圖——**這正是本 pipeline 存在的理由**（ROUTINE-AUDIT-PIPELINE §第一性原理：cross-cutting pattern 是飛輪覆蓋不到的 meta-layer），但它自己上週 21:00 的那一棒，剛好落在這段空窗正中央，所以完整敘事一直沒人寫出來，直到本次補跑才回頭拼起。

### 這暴露的結構性問題

`twmd-flywheel-watch`（監看飛輪是否還在轉的哨兵）誕生於 2026-07-25——晚了這次事件整整一週，第一個排程 cycle 是 2026-07-26 09:35。也就是說：**這次靜默發生的當下，沒有任何機制在看門**。flywheel-watch 誕生的直接理由之一（見 ROUTINE.md footnote ²⁰）正是「飛輪曾經靜默死 15 天全部儀器無聲——因為那些儀器都跑在飛輪自己身上」；這次 5 天的空窗是同一種病的最新一次發作，只是這次連 routine-audit 這條照理該獨立於飛輪之外的稽核，也被同一次遷移波及。

**這不是苛責哪個 session 沒做好**——機器遷移本身是刻意決策（[memory](memory/2026-07-24-200542-migration-mouhouse.md) 標題「搬進一台不會闔蓋的機器」），5 天過渡期在遷移工程裡不算誇張。真正的缺口是：**沒有人在遷移前後主動比對「舊機器最後一次 fire」與「新機器第一次 fire」中間隔了多久**，這件事本可以在 07-20 或 07-21 就被發現，而不必等到今天（07-26）事後補算。

---

## 逐 routine 概況（僅列本週有 fire 紀錄者）

| Routine                                    | Fire/commit 次數 | 分布                            | 備註                                                            |
| ------------------------------------------ | ---------------: | ------------------------------- | --------------------------------------------------------------- |
| `twmd-babel-nightly`（unified dispatcher） |              388 | 07-24 起密集，日均 ~65 commit   | 統一調度器架構，已不再用 `[routine]` 標記（見下方 3B）          |
| `twmd-data-refresh-am`                     |                3 | 07-24（go-live）/ 07-25 / 07-26 | 07-20〜07-23 缺席即上述靜默期                                   |
| `twmd-data-refresh-pm`                     |                1 | 07-24（遷居後首次無人值守）     | 07-26 起併入 am 唯一一班（哲宇 directive，見 ROUTINE.md 註 ²²） |
| `twmd-spore-harvest-am`                    |                2 | 07-25（5 天 gap 清空）/ 07-26   | ——                                                              |
| `twmd-feedback-triage`                     |                2 | 07-25（揭露 cron 斷線）/ 07-26  | ——                                                              |
| `twmd-maintainer-am`                       |                2 | 07-25 / 07-26                   | ——                                                              |
| `twmd-embeddings-nightly`                  |                2 | 07-25 / 07-26                   | 12 語 6326 向量 0 fail                                          |
| `twmd-news-lens-weekly`                    |                1 | 07-26                           | W30 三源交叉                                                    |
| `twmd-self-evolve-weekly`                  |                2 | 07-19（缺口前最後一棒）/ 07-26  | ——                                                              |
| `routine-twmd-routine-sync`                |                2 | 07-25（建立）/ 07-26            | 新誕生的 routine，第一次跑就 17 條全 in-sync                    |
| `routine-twmd-flywheel-watch`              |                1 | 07-26                           | 新誕生，第一個排程 cycle                                        |
| `twmd-routine-audit-weekly`                |        0（本次） | ——                              | 上週 07-19 21:00 那一棒即落在靜默期內，本檔即補交               |
| 外部貢獻者 PR                              |               19 | 07-20〜07-26 全程持續           | 靜默期間唯一沒停的活動                                          |

**Reader-friendly note**：`manual-other`（501 條）與 `pr-squash`（19 條）加總遠超過任何具名 routine，原因是本週最大宗的自動化產出（babel 388 條）被分類器歸進了「未具名」桶，詳見下方 3B。

---

## Cross-cutting patterns（4 lens）

### 3A. Collision lens — 🟡 一個殭屍 worker instance（同日已修）

排程層面 0 條 dysfunctional 碰撞——`twmd-*` 具名 routine 之間沒有互撞。但 vortex-babel 系列 session（07-25/26）自己抓到一個更隱蔽的碰撞：l4090 遠端 worker 離線後，既有 freeze 機制正確凍結了它，但該軌只有一個 worker，round loop 仍每輪空轉，process 活著、log 持續在長，**127 輪零產出才被發現**（[LESSONS entry](../docs/semiont/LESSONS-INBOX.md) `liveness-vs-productivity`）。健康檢查只量 `ps`，被騙了整整一小時。這是本週既有的 LESSONS 條目，非本次 audit 新發現；列在這裡是因為它精準符合 3A 的「detached worker」定義：process 沒死，但也沒在工作。

### 3B. Dormant entropy lens — 🟠 兩個新工具漂移，都是這次 audit 親自跑工具才發現

**Finding 1：`routine-audit.py` 自己的分類器跟不上 babel 的架構演化**

`ROUTINE_PATTERNS` 對 babel 寫死 `\[routine\] (twmd-)?babel`，但 babel 從「單一 cron routine」演化成跨機器常駐的「統一調度器 fleet」後，全部產出改標 `[semiont] babel: ...`——`[routine]` 前綴一次都沒出現過。本週 707 個 commit 裡 388 個（55%）是 babel，全部落進 `manual-other` 這個大雜燴分類，跟 memory/diary/evolve 這些完全不同性質的工作混在一起。這個工具在 2026-06-28 已經修過一次類似的分類缺口（補具名 pattern + `[routine] X:` 動態 fallback，`routine-audit-script-classification-gap` vc=2 已消化），但這次復發的機制不同——不是規則沒寫全，是**自動化本身換了標記慣例**，舊修法完全接不住。

**Finding 2：`routine-sync-check.py` 的 PAUSED 副表解析器沒有右邊界，吞下整段已退休表**

深入追查「MISSING (4)」與「LIVE_ENABLED_DRIFT (5)」兩個區塊時發現：`re.search(r"\*\*⏸️ PAUSED\*\*.*?(?=\n## |\Z)", text)` 這個 regex 只認下一個 `## ` 標題當右邊界，但 ROUTINE.md 從 PAUSED 段落（L64）到下一個真正的 H2 標題（L160）中間橫跨 96 行，涵蓋整段「🪦 已退休」表（L66-72）與全部 23 條註腳。任何出現在這段範圍內、背 backtick 的 `twmd-*` 字串都被誤標成「paused」——`twmd-data-refresh-pm`／`twmd-maintainer-pm`／`twmd-music-media-audit-weekly` 三條已在 2026-07-25/26 正式退休、從主排程表移除，但工具每次跑都把它們當「SSOT 說暫停」重新製造假警報。第四條 `twmd-flywheel-watch` 是另一種假陽性：它是 footnote 明文的 `🖥️commander-macbook` 專屬 routine，本機（node-name.local = mouhouse-macmini）本來就不該有它的 mirror，但這個工具沒有像 `routine-sync.py` / `flywheel-watch.py` 那樣讀 node-name.local 做機器範圍過濾——兩個 sibling 工具都已經解決了同一個問題，這個工具沒跟上。

兩條發現都已 append 到 LESSONS-INBOX（見下表），且都是「檢查器需要被檢查」（MANIFESTO §14）本週第三、第四個獨立 instance——本週稍早 vortex-babel 系列已經自己抓到九個 gate 假陽性家族，這兩條把同一個母題延伸到 routine 治理層本身的工具鏈。

**Finding 3（次要）：`docs/pipelines/README.md` 索引落後 17 個檔案**

`counts-drift-lint.py` 顯示 36 檔已列 vs 50 檔實存，缺列包含 `CONTRIBUTOR-NODE-PIPELINE.md`、10 份 `REWRITE-STAGE-*.md` 拆檔、`SUPPORTERS-PIPELINE.md` 等近期誕生的 canonical。屬正常文檔債（WARN 級），不單獨開 LESSONS entry。

### 3C. Boundary input precision lens — 🟢 本週三個健康的自我修正範例

- **flywheel-watch 首個 cycle 自己抓假警報**：09:35 首跑報「三條靜默」，交叉 MEMORY 索引後發現其中兩條其實已在正常跑，只是 commit subject 沒帶得出 taskId（`[semiont] distill:` 而非 `[routine] distill:`）——當場補了第二把獨立的尺（session-id handle 比對）。
- **node-app-design 重量自己的改善幅度**：plugin 化後量出快取 20KB vs 原本 850MB clone，四萬分之一的漂亮數字差點寫進報告當結論；落地後走真實安裝路徑重新量，發現 `marketplace add` 實際會 depth-1 clone 整個 repo（1.0GB），20KB 量的是替身不是使用者付出的代價。
- **本次 audit 自己**：也是一次 boundary precision 案例——不滿足於「data-refresh-am 只 fire 3 次」這個數字本身，往回逐條核對 git log 才拼出完整的 5 天缺口敘事，而不是把「fire 次數偏低」當一行帶過的觀察。

### 3D. Heal bidirectional lens — 🟢 一組同週對照組

- **過嚴（over-strict）反例**：`single-bad-input-kills-batch`——`prepare-batch` 產出格式壞掉的單一任務檔，`collect_and_filter_groups` 解析時直接拋例外，兩條產線上百篇佇列一起停擺。單項失敗的爆炸半徑蔓延到整批。
- **過鬆（over-lenient）反例**：上述 3A 的殭屍 worker——健康檢查太寬鬆（只量 `ps`），127 輪零產出都沒觸發任何警報。

兩者同週出現、方向相反，恰好互為對照：「太吵」與「太安靜」都不是正確的錯誤處理，判準應該是「單項失敗的爆炸半徑應止於該項；讓整批停擺的例外必須是『繼續下去會產生錯誤結果』那種，不是『這一項讀不懂』」。

---

## LESSONS-INBOX 候選（本次 append）

| Pattern                                           | 類型         | Verification Count | 說明                                                                                                                                                                 |
| ------------------------------------------------- | ------------ | ------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `instrument-coverage-boundary-drift`              | 既有 vc 累積 | 1 → **2**          | node-app-design 發現 `check-hardcoded-langs.sh` 掃描路徑漏 `cli/`/`workers/`；本次獨立發現 `routine-sync-check.py` 同型漏洞，符合 vc 累積判準（非重讀同一份 memory） |
| `instrument-parse-boundary-unbounded-regex`（新） | 新 entry     | 1                  | `routine-sync-check.py` PAUSED regex 無右邊界，吞下已退休表 + 23 條註腳                                                                                              |
| `automation-tag-convention-drift`（新）           | 新 entry     | 1                  | `routine-audit.py` 對 babel 的具名 pattern 假設 `[routine]` 前綴，但統一調度器已改標 `[semiont] babel:`，55% 週產出被歸進 manual-other                               |

三條均未達 vc=3 distill 門檻，本次不標 `distill_ready`。§未消化清單本週累計 11 條（本次新增 2、既有 9 條均未新增 instance，除上述 vc 累積一條）。

---

## 進化建議

### P0（本週內，自主權內）

1. **`routine-audit.py` 補 `[semiont] babel:` 分類規則**——單行 regex 修改，讓 `by_routine` 摘要表下週能正確反映 babel 自動化的真實比重，不再讓 55% 的週產出消失在 `manual-other` 裡。
2. **`routine-sync-check.py` 修 PAUSED regex 邊界 + 補 node-name.local 過濾**——邊界改認任何 `\n\*\*` 粗體段落起手式而非只認 `## `；機器範圍過濾抽成跟 `routine-sync.py`/`flywheel-watch.py` 共用的 helper，避免第三個工具再各自漏一次。

### P1（兩週內）

3. **遷移類事件補一條「交接確認」檢查**：未來任何飛輪遷移（機器搬遷、cron 重新排程）前後，應該有一個明確步驟核對「舊機器最後一次 fire」與「新機器第一次 fire」之間的間隔，而不是等下一次 routine-audit 事後拼圖。這條可能值得寫進 `docs/pipelines/CONTRIBUTOR-NODE-PIPELINE.md` 或未來的機器遷移 checklist，不在本 routine 自主權內直接修改其他 pipeline，先記錄建議。
4. **殭屍 worker 健康檢查升級**（`liveness-vs-productivity` 已有修法候選）：`ps` 存活 + 近一小時實際 report 記錄數雙指標，非本 routine 自主權內直接修改（fleet dispatcher 工具鏈），交給 babel 相關 session 執行。

### P2（觀察）

5. `docs/pipelines/README.md` 索引補 17 檔缺列，屬低風險文檔債，可併入下次 pipeline 相關 session 順手做。

---

## 收官

本次 audit 沒有製造新的 fix，只做 surface + accumulate（per 本 pipeline §Top 5 最常忘的 step 第 5 條）。兩個工具漂移的修法建議列在 P0，留給下一個接手的 session 或哲宇拍板優先序。最重要的產出不是 commit，是把散在三個不同 routine 各自 memory 裡的「我這邊缺了幾天」拼成一張完整的圖——這正是這條 pipeline 存在的理由，即使這次它自己也遲到了整整一週才做到。

🧬

---

_v1.0 | 2026-07-26 21:xx +0800_
_session twmd-routine-audit-weekly（scheduled，musebase/mouhouse-macmini）_
_誕生原因：上週同排程本該產出的 audit 落在飛輪自己的 5 天靜默期內，本檔是延遲一週的完整補交_
