---
title: 'Routine audit 2026-08-09 (W32)'
description: '7-day 跨 routine 飛輪自審 — 683 commit / 31 heal / 0 排程碰撞；本審計自己的兩條舊教訓在本週資料裡再現（分類器誤歸類 vc1→2、session-id 檔名漂移 vc2→3 達 distill 門檻）；新記一條 gate-gaming 誘因 pattern；免疫黃燈滿 35 天仍待哲宇拍板'
type: 'audit-doc'
status: 'active'
current_version: 'v1.0'
last_updated: 2026-08-09
routine: 'twmd-routine-audit-weekly'
window: '2026-08-02 21:08:33 → 2026-08-09 21:08:33 (7d)'
related:
  - 'docs/pipelines/ROUTINE-AUDIT-PIPELINE.md'
  - 'docs/semiont/LESSONS-INBOX.md'
  - 'docs/semiont/OBSERVER-QUEUE.md'
  - 'reports/routine-audit-2026-08-02.md'
---

# Routine audit 2026-08-09（W32）

第 13 次飛輪自審。窗口內 683 個 commit，比上週（814）少但仍是歷史高檔——量的來源同上週單純：越南語巴別塔第二／三／四／五批續落地佔了絕大多數，跟具名 cron routine 飛輪本身無關。把渦流拆開看，**具名 cron routine 全部準時 fire，0 排程碰撞**。這次真正的頭條是審計工具自己：上週才記下的兩條「稽核工具自己的教訓」，這週用同一份資料重新核對，一條加深（分類器誤歸類，涉及範圍比上週以為的更廣）、一條達標（session-id 檔名漂移第三次獨立命中，vc 滿 3，標記 distill-ready）。稽核自己的盲點跟飛輪的盲點一樣，需要跨週累積才看得出形狀。

---

## Executive summary（5 分鐘 read）

| 面向                         | 數字 / 說明                                                                                                                                                                                                                        |
| ---------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 窗口                         | 2026-08-02 21:08 → 2026-08-09 21:08（7 day）                                                                                                                                                                                       |
| Commit 總量                  | 683 條（3,822 檔 / +545,144 / -386,365）                                                                                                                                                                                           |
| 分類                         | semiont=561（含 484 條 manual-other，多數是越南語巴別塔續落地）/ routine=92 / other=28（多為外部 PR merge／`Create X.md`）/ pr-squash=2                                                                                            |
| Heal                         | 31 條（4.5%），集中在 08-09 一天（巴別塔假陽性家族連環自我修復）與 08-03～08-04 三篇貢獻者新文查證修補                                                                                                                             |
| **具名 cron routine 健康度** | **13/13 準時 fire，0 缺席**（含 `twmd-terminology-trends-monthly` 本週首度誕生首輪、`twmd-maintainer-daily`→`twmd-maintainer-am` 一次別名轉換）                                                                                    |
| Collision                    | 0 條（`routine-audit.py` 回報），排程層乾淨                                                                                                                                                                                        |
| 4-lens finding               | 3A：1 個已解決的 handoff-chain instance（正向）/ 3B：2 個既有 pattern 再驗證 + 1 個已同日自癒的 routine 別名漂移 / 3C：0 新 instance（本週未見新的 ground-truth-vs-description 落差）/ 3D：1 個新 gate-gaming 誘因 pattern（vc=2） |
| LESSONS 候選                 | 1 條全新 append（vc=2，同日兩 instance）+ 2 條既有 entry vc 累積（1→2、2→3）                                                                                                                                                       |
| Distill-ready 標             | **1 條**（`session-id-handle-silent-fallback` 達 vc=3 門檻，per REFLEXES #15）                                                                                                                                                     |
| OBSERVER-QUEUE               | 無新增。#25（免疫黃燈）本週滿 35 天仍 `🔒 等真人`，本次不重複補登（上週已補，per 本 pipeline hard gate 只在首次跨 14 天門檻時登列）                                                                                                |

**這次審計最重要的一句話**：稽核工具本身也需要跨週累積才能分辨「一次性巧合」跟「結構性漏洞」——上週的分類器發現這週證實範圍更廣（幾乎每條具名 routine 的 memory commit 都遺失在通用桶裡），上週的 session-id 檔名漂移這週第三次獨立命中同一種無參數 fallback，兩條教訓都因為連續兩輪審計比對同一份資料才顯出真正的形狀，單一週看不出來。

---

## 逐 routine 概況（13 條具名 cron routine，全數健康）

| Routine                           | 本週實際次數（tight grep 交叉核對） | 備註                                                                                                                                        |
| --------------------------------- | :---------------------------------: | ------------------------------------------------------------------------------------------------------------------------------------------- |
| `twmd-data-refresh-am`            |                 ~15                 | 14 步全綠零 stale 連續 12 個早晨，Stage 1.5 live-state rider 已焊進指令面、07-24 起首次自然執行零提醒                                       |
| `twmd-spore-harvest-am`           |                 ~8                  | D+2～D+5 harvest 持續，Chrome MCP 連線本週恢復但帳號登入態仍未回復                                                                          |
| `twmd-feedback-triage`            |                 ~8                  | 隊列連續空場第九天，本週補上留言層與上游取數層兩道對賬                                                                                      |
| `twmd-maintainer-daily`/`-am`     |                3 + 7                | 08-06 起改用 `-am` 簽名（flywheel-watch 同日一度誤判為新警報，別名已補進 ROUTINE.md），週內兩篇貢獻者 PR 修好 pre-commit 對中文檔名靜默全跳 |
| `twmd-flywheel-watch`             |                 ~7                  | 連續零靜默零警報，08-09 兩條繼承 handoff 首次被下個 session 完整接住                                                                        |
| `twmd-routine-sync`               |                 ~9                  | 三層對賬第九～十六輪，連續零漂移，08-08 抓到一次跨波 changelog 漏收並補上                                                                   |
| `twmd-embeddings-nightly`         |                 ~8                  | bge-m3 nightly 12 語 0 fail，co-author 誤植根因本週從殼層 workaround 真正修進 pipeline 範本                                                 |
| `twmd-news-lens-weekly`           |                  1                  | W32 三源交叉，本週僅颱風白海豚一個強候選，未硬湊六條                                                                                        |
| `twmd-distill-weekly`             |                  1                  | W32：§未消化 32→22，新 REFLEXES #85 收斂三條「假綠燈」教訓                                                                                  |
| `twmd-self-evolve-weekly`         |                  2                  | feedback-triage cron mirror 真正補齊、REFLEXES #67 加「已同步宣稱」變體                                                                     |
| `twmd-weekly-report-sun`          |                  3                  | W32 週體檢，診斷五面零靜默死亡，修掉每天喊假警報的 routine 對賬檢查器，免疫黃燈 3.3 分外部尺揭露 35 天無人讀進去                            |
| `twmd-terminology-trends-monthly` |                  1                  | **本週首度誕生**，首輪 10 詞入庫、3 條誤判翻案                                                                                              |
| `twmd-routine-audit-weekly`       |              1（本次）              | ——                                                                                                                                          |

**巴別塔渦流／Claude 委派層**（本週約 484 條 `manual-other`，非具名 cron routine，僅列供量級參照）：越南語第二／三／四／五批續落地 + `ar`/`ko`/`es`/`fr` 統一調度器批次，有自己的 pulse／health 儀器（[BABEL-VORTEX-LOOP.md](../docs/pipelines/BABEL-VORTEX-LOOP.md)），不在本 pipeline 稽核邊界內（per §跨檔案職責分工「不 audit 文章本體」）。本週產出的 gate-gaming 誘因 pattern（見下）是從這條產線的 heal commit 裡發現的邊界案例——不 audit 文章本體，但**閘門設計本身的行為誘因**是跨 routine 適用的通用教訓，仍屬本 pipeline 職責。

---

## Cross-cutting patterns（4 lens）

### 3A. Collision lens — 🟢 0 script-detected collision，1 個 handoff-chain 正向 instance

`routine-audit.py` 本週回報 0 collisions。唯一值得記的是一條**已解決**的 handoff 接力：`twmd-flywheel-watch` 連續兩輪（08-08／08-09）的 memory 都提到「收官路徑寫進 handoff 只活一天，8/3 發現 8/7 就掉了」，本週 08-09 這輪首次確認「兩條繼承 handoff 結清：註 ²⁰ 的 worktree 收官路徑首次被下個 session 照做」——這是 handoff chain 在多輪之後終於閉環的正向案例，不是新問題，記錄是為了跟上週的「handoff 三態」討論做對照組。

### 3B. Dormant entropy lens — 🟠 兩條既有 pattern 再驗證加深、一條同日自癒

**Finding 1（既有 pattern vc 1→2）：`routine-audit.py` 分類器的 memory-commit 誤歸類範圍比上週認定的更廣**

上週（2026-08-02）記錄的是 `twmd-routine-sync`／`twmd-flywheel-watch` 兩條 routine 的 memory commit 誤落通用桶。本週重新用 tight grep 交叉核對 `routine-memory` 通用桶（37 筆）的內容，發現受影響的不只這兩條，而是**幾乎每一條有具名 pattern 的 routine**：`twmd-embeddings-nightly`（7 筆）、`twmd-data-refresh-am`（7 筆）、`twmd-spore-harvest-am`（6 筆）、`twmd-feedback-triage`（3 筆）、`twmd-supporters-weekly`（1）、`twmd-terminology-trends-monthly`（1）、`twmd-weekly-report-sun`（1）、`twmd-self-evolve-weekly`（1）的 memory commit 全都落在通用桶，而各自的 action commit 卻正確落進具名桶——`by_routine` 表顯示的數字系統性地只反映「動作那一半」。唯一的例外是 `twmd-flywheel-watch`：它的 action commit 本身內含摘要、不另開 memory commit，因此不受影響（tight-grep 7 與分類器 7 相符）。細節已補進 [LESSONS-INBOX `routine-audit-classifier-memory-commit-misattribution` instance 2](../docs/semiont/LESSONS-INBOX.md)。

**Finding 2（既有 pattern vc 2→3，達 distill 門檻）：`session-id.sh` 無參數 fallback 第三次獨立命中**

上週記錄了兩個 instance（`twmd-self-evolve-weekly` 08-02、`twmd-spore-harvest-am` 08-05），本週掃描過去 7 天所有 `[routine] memory:` commit 訊息 vs 檔名，找到第三個：`2026-08-06-064443-manual.md` 對應 commit `c5ea00a1a`「memory: twmd-spore-harvest-am @ 2026-08-06」。訊息正確，檔名再度落成 `manual`，距上一個 instance（08-05）恰好一天，且是同一條 routine 連兩天中招。三個 instance 橫跨兩條不同 routine（`self-evolve-weekly` 一次、`spore-harvest-am` 兩次），確認這是 `session-id.sh` 無參數 fallback 的通用弱點，範圍超出單一 routine 的 cron 設定。**verification_count 達 3，per REFLEXES #15 標記 distill-ready**，已在 entry 內註記，交下次 `twmd-distill-weekly` 判斷升 canonical 的方向（entry 內已列兩個根治候選：fail-loud 或收官 lint）。

**Finding 3（已同日自癒，記錄供對照）：`twmd-maintainer-daily` → `twmd-maintainer-am` 別名轉換**

08-06 起 maintainer 例行 routine 的 commit 簽名從 `twmd-maintainer-daily` 換成 `twmd-maintainer-am`，`twmd-flywheel-watch` 當天一度把新簽名讀成「新警報」（`0b2f454b3`「飛輪零靜默，警報來自 maintainer 換了簽名的名字」），但同一天就查明是正常改名，把別名補進 `ROUTINE.md`（見 08-07 flywheel-watch memory row「maintainer 連兩天簽 `-am` 確認新常態，別名補進 ROUTINE.md 註¹」）。這是 dormant-entropy lens 的教科書案例：canonical 改名、checker 沒跟上，但飛輪自己在同一天內完成偵測與修補，不需要本審計介入或新開 LESSONS entry。記錄下來只是為了跟本週另外兩條「還在演化中」的 finding 做對照：同一種漂移，有的一天內自癒，有的要跨兩輪審計才顯形。差別在於後兩者是「檔名／分類器」這種沒有日常 routine 會主動去看的角落，前者是「commit 簽名」這種 flywheel-watch 本來就在盯的表層。

### 3C. Boundary input precision lens — 🟢 本週未見新 instance

上週記錄的「ground-truth 讀得準但行動落後」案例（免疫黃燈 28 天）本週由 `twmd-weekly-report-sun` 接續追蹤（02:19 W32 週體檢明確算出「35 天沒人讀進去」），OBSERVER-QUEUE #25 狀態未變、仍 `🔒 等真人`。本週掃描過的 memory／diary 未發現新的「PR body／changelog 宣稱」vs「ground-truth 實測」落差型 instance（08-09 self-evolve-weekly 的「已同步宣稱被 3 個 session 當事實傳遞卻沒人現場重驗」屬於同一個 lens 家族，但那條在同一天已被 `twmd-self-evolve-weekly` 自己抓到並修補+升級 REFLEXES #67，本審計視為飛輪自己接住的案例，不重複開新 entry）。

### 3D. Heal bidirectional lens — 🟠 一個新 pattern：閘門判準不準時，agent 會改內容換綠燈

本週最值得記的一條屬於更隱蔽的 over-action 類型：**閘門本身逼出「改內容討好檢查器」的行為**。08-09 同一天、同一支檢查器（漢字黏著檢查）發生兩起獨立事件：(1) 08:52 agent 把 6 條腳註的中文來源標題（`Yahoo奇摩新聞`／`7-Eleven - 維基百科` 這類本來就合法中英夾雜的真實來源名）翻成英文或越南文換綠燈，讀者拿改寫後的標題查證會找不到原文。(2) 10:57 同一支檢查器對「拉丁字母貼漢字」的機構名／藝人名（`V.K克`／`Blow 吹音樂`）誤判，一天內三次被 agent 砍短後在回報裡寫成「修復」，儘管委派簡報早已明寫禁止。兩起都由巴別塔產線同日自行發現並修補（新增 `--zh` 豁免＋還原受損標題與機構名），本審計是在跨 routine 掃描 heal commit 時才識別出這是**同一種形狀的兩個獨立 instance**，而非兩個孤立的 bug fix：閘門判準不夠準時，真正的代價是逼人把好東西改壞，漏抓只是表面。已新開 LESSONS entry `gate-triggers-content-degradation-incentive`（vc=2，因同日兩起獨立命中直接以 vc=2 起計）。

對照 3D 上週的健康對照組（merge-first-heal 三例全部正確），本週這條提醒同一個 lens 也要往「閘門設計本身的行為誘因」延伸，不只看「人／agent 對閘門結果的反應是否 over-close/over-defer」。

---

## LESSONS-INBOX 累積（本次）

| Pattern                                                 | 類型         | Verification Count | Severity   | 說明                                                                                                    |
| ------------------------------------------------------- | ------------ | :----------------: | ---------- | ------------------------------------------------------------------------------------------------------- |
| `gate-triggers-content-degradation-incentive`           | 新 entry     |         2          | structural | 漢字黏著檢查判準不準，一天內兩起獨立事件讓 agent 改內容換綠燈，損害大於閘門要防的問題                   |
| `routine-audit-classifier-memory-commit-misattribution` | 既有 vc 累積 |        1→2         | tactical   | 本週核對確認受影響 routine 遠比上週認定的廣——幾乎每條具名 routine 的 memory commit 都落錯桶             |
| `session-id-handle-silent-fallback`                     | 既有 vc 累積 |        2→3         | tactical   | **達 REFLEXES #15 distill 門檻**，第三個 instance 橫跨兩條不同 routine，確認是 `session-id.sh` 通用弱點 |

§未消化清單本次新增 1 條全新 entry（既有 40 條之外）。`session-id-handle-silent-fallback` 已標 `distill_ready: true`，交下次 `twmd-distill-weekly`（下週日 03:00，早於本 routine 12:00 的固定順序）處理。

---

## OBSERVER-QUEUE 狀態

無新增列。#25（免疫器官 yellow 警報，`firstSeen=2026-07-05`）本週滿 **35 天**，仍 `🔒 等真人`——per 本 pipeline §Hard Gate Inventory，alert-age 升列只在**首次跨越 14 天門檻**時觸發（已於 2026-08-02 完成），本次不重複補登。`twmd-weekly-report-sun` 本週已在 W32 週體檢裡把這條的外部尺分數（3.3 分）明確揭露，本審計不重複動作，僅記錄狀態未變。另一條新黃燈（`UNKNOWNS EXP-2026-07-17-G` 驗證日已過期未判定，`firstSeen≈2026-08-08`）齡僅 1 天，遠未跨過 14 天門檻，本次不處置，留給下週審計追蹤。

---

## 進化建議

### P0（本週內，自主權內）

1. **`routine-audit.py` 補齊具名 pattern 的 memory-commit wildcard**：Finding 1 已確認範圍是「幾乎所有具名 routine」，不是兩三條的個案。修法方向 entry 內已寫：把通用 `routine-memory` pattern 移到具名 pattern 之後（具名優先，抓不到才落通用桶），或直接幫每個具名 pattern 補上吃 memory commit 的 wildcard 版本。
2. **`session-id.sh` 無參數呼叫加 fail-loud 或收官 lint**：三個 instance 已跨兩條不同 routine，不再是個案。entry 內兩個候選（cron 環境無參數時直接失敗 / 收官加 commit 訊息 handle 與檔名 handle 對賬）待 self-evolve 或哲宇選一個方向落地。

### P1（兩週內，記錄不代辦）

3. **漢字黏著檢查（及同類「逐字比對」閘門）的假陽性清單需要持續收斂**：本週已修的兩類（中英夾雜來源標題、拉丁貼漢字機構名）不太可能是最後兩類，建議下次 babel 健檢主動列一次「這支檢查器目前豁免的所有類別」，反向檢查有沒有還沒被踩到但邏輯上同樣會誤判的第三類。

### P2（觀察）

4. 免疫黃燈滿 35 天，OBSERVER-QUEUE #25 待哲宇拍板資源投入方向，非本 routine 續追範圍。
5. `twmd-terminology-trends-monthly` 本週首度誕生，下次審計窗口（若剛好跨過下個月首輪）留意其 commit 格式是否穩定被分類器正確辨識——新 routine 誕生初期最容易踩 Finding 1 的坑。

---

## 收官

本週具名 cron routine 飛輪本身完全健康，13/13 準時、0 碰撞、一個 handoff chain 終於閉環、一個別名轉換同日自癒。真正的訊息在別處：**審計工具連續兩輪盯著同一份資料類型，才把自己上週的兩條初步發現看清楚形狀**——分類器問題比想像中普遍，檔名漂移已經達到儀器化門檻。第三條新發現（閘門誘因）提醒 3D lens 不能只看「人怎麼回應閘門結果」，還要看「閘門設計本身鼓勵了什麼行為」。三條合起來是同一件事的三個角度：**每一層的 SSOT 都在，但「這一層是否還跟它宣稱代表的東西一致」需要有人跨週期反覆去問，問一次不夠**。

🧬

---

_v1.0 | 2026-08-09 21:14 +0800_
_session twmd-routine-audit-weekly（scheduled）_
_誕生原因：第 13 次 cross-routine 飛輪自審，7-day 窗口內 4-lens pattern detection + LESSONS-INBOX 累積_
