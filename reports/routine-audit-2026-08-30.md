---
title: 'Routine audit 2026-08-30 (W35)'
description: '7-day 跨 routine 飛輪自審 — 194 commit / 41 heal / 0 排程碰撞；本 routine 自己與 twmd-supporters-weekly 上週雙雙靜默；四天全飛輪停轉的根因調查被三份 handoff 指名交給一個已停用一個月的 routine'
type: 'audit-doc'
status: 'active'
current_version: 'v1.0'
last_updated: 2026-08-30
routine: 'twmd-routine-audit-weekly'
window: '2026-08-23 21:09:32 → 2026-08-30 21:09:32 (7d)'
related:
  - 'docs/pipelines/ROUTINE-AUDIT-PIPELINE.md'
  - 'docs/semiont/LESSONS-INBOX.md'
  - 'docs/semiont/OBSERVER-QUEUE.md'
  - 'reports/routine-audit-2026-08-16.md'
---

# Routine audit 2026-08-30（W35）

第 15 次飛輪自審——也是遲到一週的一次。上一次 fire（2026-08-23 21:15）有排程紀錄卻沒有留下任何 commit，本次是同一條 routine 隔一週重新開口。本週最重要的發現不在窗口內的 194 個 commit 裡，而在窗口**開頭前兩小時**：2026-08-23 09:19 到 2026-08-27 10:18，本機所有具名 cron routine 完全靜默四天，本 routine 自己與 `twmd-supporters-weekly` 都是這場靜默的當場受害者。三條在 08-28 恢復後各自摸到這個缺口的 routine，不約而同把根因調查指名交給一條八月十日就已停用的 routine——這是本次審計唯一需要跨 routine 視角才拼得出全貌的發現。

---

## Executive summary（5 分鐘 read）

| 面向                         | 數字 / 說明                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| ---------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 窗口                         | 2026-08-23 21:09 → 2026-08-30 21:09（7 day）                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Commit 總量                  | 194 條（1,714 檔 / +776,112 / -571,170，插入刪除量高是 8/27 catch-up 批次含大量圖片素材與批次撤換）                                                                                                                                                                                                                                                                                                                                                                 |
| 分類                         | semiont=23 / routine=53 / other=117（多為外部 PR merge、貢獻者翻譯 PR、contributor 直接 Create \*.md） / pr-squash=1                                                                                                                                                                                                                                                                                                                                                |
| Heal                         | 41 條（21.1%）— 集中在 08-27 單日（27+ 條），是四天停轉後第一次恢復運作的維護者批次收割                                                                                                                                                                                                                                                                                                                                                                             |
| **具名 cron routine 健康度** | **本 routine 自己與 `twmd-supporters-weekly` 上週各自 0 次（斷軌）**；其餘 11 條在恢復後（08-28 起）準時運作，本次 cycle 0 缺席                                                                                                                                                                                                                                                                                                                                     |
| Collision                    | 0 條（`routine-audit.py` 回報）；但窗口外前緣的「全飛輪四天靜默」比任何單點碰撞都重                                                                                                                                                                                                                                                                                                                                                                                 |
| 4-lens finding               | 3A：1 個系統性缺口（四天全飛輪停轉，非單點碰撞）／3B：1 個新 pattern（三份 handoff 指名一個已停用的 escalation target，vc=1）＋ 1 個既有 pattern 正向確認（08-16 記過的分類器 bug 已於 08-23 被 distill-weekly 修好且本週驗證未復發）／3C：1 個自我修正案例（初診「約兩天」被三條後續獨立 routine 各自更正為「四天」）／3D：1 個健康對照組（08-27 maintainer-manual 危機恢復 session：27 ready PR 收到剩 2、造 2 支新工具、3 篇保留給哲宇、1 次公開更正自己的誤判） |
| LESSONS 候選                 | 1 條全新 append（`deferred-to-a-paused-escalation-target`，vc=1，見上文）                                                                                                                                                                                                                                                                                                                                                                                           |
| Distill-ready 標             | 0（本次新發現 vc=1，未達門檻；如需優先處理見下方 P0 建議）                                                                                                                                                                                                                                                                                                                                                                                                          |
| OBSERVER-QUEUE               | 無新增列。免疫黃燈（`firstSeen=2026-07-05`）本週滿 **56 天**，仍 `🔒 等真人`，本次不重複補登。建議另評估是否新開一項「四天盲窗根因仍未判定」，見下方進化建議                                                                                                                                                                                                                                                                                                        |

**這次審計最重要的一句話**：三份各自誠實、各自正確的 handoff，加總結果是零人接手——因為它們共同指名的那個位置已經空了一個月，而沒有一個 session 在寫下「交給 flywheel-watch」之前查過它是否還在。

---

## 逐 routine 概況（13 條具名 cron routine；2 條上週斷軌本週已確認恢復）

| Routine                           |                           本週實際次數                           | 備註                                                                                      |
| --------------------------------- | :--------------------------------------------------------------: | ----------------------------------------------------------------------------------------- |
| `twmd-data-refresh-am`            |                         3（08-28/29/30）                         | 14 步全綠零 stale 連續三天；08-28 首次在無黃燈狀態驗證 scheduler live dump 無條件跑的修法 |
| `twmd-spore-harvest-am`           |                                3                                 | D+5〜D+7 用語保存副詞層收割持續；一次誤跑 destructive audit 腳本刪 10 檔即刻復原          |
| `twmd-feedback-triage`            |                                3                                 | 第三人指控信第十一〜十三次連續由 HG13 攔下；兩道對賬 82/82 與 81/82 全綠                  |
| `twmd-maintainer-am`              |                 3（另加 08-27 危機恢復場外一場）                 | 08-28/29/30 各自清空 ready 佇列；08-27 那場另計，詳見 3D                                  |
| `twmd-routine-sync`               |                                3                                 | 三層對賬第 31〜33 輪；08-23 起連續四天空窗後 08-28 才恢復，計數誠實斷開不接續舊序號       |
| `twmd-embeddings-nightly`         |                                3                                 | 12 語 bge-m3 重建 0 fail；08-28 那次的重點不是重建本身，是揭露自己四天沒被觸發            |
| `twmd-news-lens-weekly`           |                                1                                 | W35 三源交叉，propose 0（出口關閉第八次）；公投綁大選裁決催化既有候選第三次驗證           |
| `twmd-distill-weekly`             |                                1                                 | §未消化 56→約 50（含本次新增前），5 條升 REFLEXES、1 段殘留孤兒清理                       |
| `twmd-self-evolve-weekly`         |                                1                                 | 指控信同案例 12+ 次遭遇驗證，升 REFLEXES #95                                              |
| `twmd-weekly-report-sun`          |                                1                                 | W35 體檢九節全跑；抓到自己上週對 Googlebot 53% 異常的解釋這週站不住                       |
| `twmd-routine-audit-weekly`       |                            1（本次）                             | 上週（08-23）0 次——本報告即為斷軌後首次重新產出                                           |
| `twmd-supporters-weekly`          | 0（本週排程 08-30 17:07 尚未到窗口截止時刻，上週 08-24 亦 0 次） | 連續兩輪待確認，見下方 3A                                                                 |
| `twmd-terminology-trends-monthly` |                                0                                 | 月度 routine，非本月排程日，0 屬正常                                                      |

**停用中（不計入健康度分母）**：`twmd-flywheel-watch`（08-10 哲宇 directive「幫助不大」停用）、`twmd-babel-nightly`／`twmd-rewrite-daily`／`twmd-founder-lens-weekly`／`twmd-spore-pick-daily`／`twmd-spore-publish-daily`（各自獨立原因停用，見 ROUTINE.md §PAUSED）。

---

## Cross-cutting patterns（4 lens）

### 3A. Collision lens — 🟠 非單點碰撞，是四天系統性空窗

`routine-audit.py` 機械偵測回報 0 collisions（設計上抓的是「兩條 routine 撞窗口」，不是「全部 routine 一起消失」，本來就抓不到這型）。手動核對 git log 精確邊界：最後一筆 `[routine]` commit 是 **2026-08-23 09:19:35**（`twmd-maintainer-am`），下一筆是 **2026-08-27 10:18:30**（`fix(ci)` 起算的維護者恢復序列），中間 **91 小時**完全零具名 routine 痕跡。這段空窗精準吞掉了本 routine 自己 08-23 21:15 的排程觸發（scheduler `lastRunAt` 有紀錄，但零 commit 零 memory）與 `twmd-supporters-weekly` 08-24 01:15 的排程觸發（同型）。窗口內另外三條 routine（`twmd-embeddings-nightly`／`twmd-routine-sync`／`twmd-data-refresh-am`）各自在 08-28 恢復後，從自己的索引缺口（「上一筆紀錄怎麼是四天前」）獨立確認了同一個根因，彼此互相印證但沒有互相引用——這正是需要 cross-routine 視角才看得出「這是同一件事」的訊號。

### 3B. Dormant entropy lens — 🟠 一新一舊，新的更急

**Finding 1（新，vc=1，本次審計核心發現）**：三份獨立 handoff（08-28 embeddings-nightly／routine-sync／data-refresh-am）把「四天空窗的根因是機器休眠還是 launchd 掛掉」一致指名交給 `twmd-flywheel-watch` 或哲宇判斷，但 `twmd-flywheel-watch` 已於 2026-08-10 停用（ROUTINE.md 註 ²⁵），不在當前 `routine-live-state.json` 排程清單裡。三個 session 都沒有在寫下這個指名前確認它是否還活著。已寫入 [LESSONS-INBOX `deferred-to-a-paused-escalation-target`](../docs/semiont/LESSONS-INBOX.md)，關聯 REFLEXES #56（canonical 描述的對象已經換人了，這次換的是「該找誰」而非「該用什麼工具」）+ #74（cross-routine SPOF handoff 重複通膨）+ #82（`lastRunAt` 這個代理訊號只證明「有被觸發」不證明「有跑完」）。**到今天（08-30）為止，四天空窗的實際根因仍未被判定**，只確認了「現在已經恢復」——這是懸案不是結案。

**Finding 2（既有 pattern，正向確認，非本次新發現但值得記一筆）**：上次審計（08-16）記錄的 `routine-audit.py` 分類器連續三輪（08-02/08-09/08-16）誤歸類 bug，已於 **2026-08-23 03:23** 被 `twmd-distill-weekly` 修好（commit `d4bdc7408` "修好審計工具自己那個病"）。本次審計交叉核對本週 `by_routine` 分類與 memory 檔案實際數量，`twmd-routine-sync`（分類器 3 / 實際 3）與 `twmd-weekly-report-sun`（分類器 1 / 實際 1）兩個上次「整條 key 消失」的重災戶本週完全準確，`twmd-data-refresh-am` 與 `twmd-feedback-triage` 也不再系統性低估。**這是「發現了但沒人修」連續三週後，第四週真的被接住的正面案例**——上次報告 P0 建議「不需要再等第四輪確認，直接動手修」，distill-weekly 在同一週窗口內（審計後 7 小時）就動了手。

### 3C. Boundary input precision lens — 🟢 一次自我修正，未經人工介入

08-27 `twmd-maintainer-manual` 危機恢復 session 甦醒時憑「過去 24 小時零 cron fire」的有限窗口，把停轉估成「約兩天」（handoff 原文：「營運機 mouhouse 排程器停了約兩天」）。但完整 git log 精確邊界（見 3A）顯示實際空窗是 08-23 09:19 到 08-27 10:18，將近**四天**，是原始估計的兩倍。這個落差沒有靠人工介入修正——08-28 的三條後續 routine（embeddings-nightly／routine-sync／data-refresh-am）各自獨立用自己的「上一筆紀錄距今幾天」重新量了一次，都得到「四天」而非「兩天」，並在各自的 memory 裡誠實記下較大的數字，08-27 那份「約兩天」的初診從未被任何人正式訂正，只是被後續更精確的量測自然覆蓋。**診斷用的窗口大小決定了結論的準確度**：08-27 session 手邊只有「過去 24 小時」的即時視角，量到的自然是它能看見的那一小段；08-28 三條 routine 手邊有的是「自己上一次紀錄的絕對時間戳」，量出來的才是真正的邊界。兩種診斷方式都沒有錯，只是解析度不同。

### 3D. Heal bidirectional lens — 🟢 一個高強度健康對照組

08-27 10:18〜12:21（不到兩小時）`twmd-maintainer-manual` 危機恢復 session：27 個 ready PR 收到剩 2、12 個卡在 CI 的紅燈 PR 追根究柢收斂成 3 個工具可解的家族（全形分號超標／缺 subcategory／圖片層問題）、當場造 2 支新工具（`semicolon-cleanup.py`、`translation-ratio-check.sh --pr` 模式的暫存區修法）、修好一個「每次該生效時必死」的 `.husky/pre-push` 分支（`sh -e` 賦值失敗靜默炸整個 hook）、正確辨識出五個縣市圖說配錯圖片這種讀者會撞見的品質問題並全部處理、三篇高爭議 PR（學測專題人物卡／KENJI 知名度門檻／Taiwan.md 自述文）正確保留給哲宇沒有自行拍板。**同一 session 也自我抓到一次過度斷言**：審 [#1453](https://github.com/frank890417/taiwan-md/pull/1453) 時把一句引語誤判「查無來源」並列為最不能放行的一類，實際來源存在，發現後立即公開更正，且自己歸納出「否定式斷言只搜了一輪就下結論，肯定式斷言卻去讀了原文」的不對稱。這是一次高壓力（4 天 backlog 一次清）下同時避免 over-close（沒有把卡在 CI 的 PR 直接拒收）、over-ship（沒有把爭議 PR 自行拍板）、over-defer（沒有把可修的問題丟給 handoff 拖著）三種偏誤的示範案例，值得作為未來危機恢復 session 的參照。

---

## LESSONS-INBOX 累積（本次）

| Pattern                                  | 類型     | Verification Count | Severity   | 說明                                                                             |
| ---------------------------------------- | -------- | :----------------: | ---------- | -------------------------------------------------------------------------------- |
| `deferred-to-a-paused-escalation-target` | 新 entry |         1          | structural | 三份 handoff 指名一個已停用一個月的 routine 當根因判定者；四天空窗根因至今未判定 |

§未消化清單本次新增 1 條。未達 vc=3 門檻，未標 `distill_ready`，但因涉及「懸案根因未結案」的時效性，建議下次 distill 或任一 session 提前查看（見進化建議 P0）。

---

## OBSERVER-QUEUE 狀態

無新增列。#25（免疫器官 yellow 警報，`firstSeen=2026-07-05`）本週滿 **56 天**，仍 `🔒 等真人`，本次不重複補登。

**附帶觀察（非新 OBSERVER-QUEUE 項，供後續判斷參考）**：

1. `routine-sync-check.py` 本次實測本 routine 自己的 cron mirror 殼層 **60 行**（🔴 THICK，warn>30 hard>50），與 08-16 讀數相同，OBSERVER-QUEUE #14 已「退回哲宇」定案，本次不重複行動。
2. `counts-drift-lint.py` 本次 WARN 46 drift / 61 claim，主要是 canonical 文件 frontmatter `last_updated` 落後實際 git 修改日（8-72 天不等）與 `docs/pipelines/README.md` 索引少列 19 個實存檔案——皆為既有 WARN-mode 慢性訊號，本次未見新增惡化，不觸發升列。
3. **四天空窗根因仍未判定**（見 3B Finding 1）——建議哲宇或下一個有能力查詢 mouhouse/musebase 排程器層日誌的 session 判斷是機器休眠、launchd 排程掛掉、或其他原因；若持續無人查，下次審計將以「chronic 未結案」重新標記。

---

## 進化建議

### P0（本週內，自主權內）

1. **Handoff 範本補一條前置檢查**：任何「交給 X routine 判斷」的指名，寫之前先查一次 `routine-live-state.json` 或 ROUTINE.md §PAUSED 列表確認 X 是否還在排程裡。本次三份 handoff 若各自多花 10 秒查一次，就不會把根因調查指名給一個空位置。
2. **重新評估 ROUTINE.md 註 ²⁵ 的「alert-only 模式」候選**：停用 flywheel-watch 時已預想「若未來需要，方向是綠燈靜默、只在 WARN/CRITICAL 時 PushNotification」——本週的四天盲窗正是這個「若未來需要」條件第一次真實觸發（兩層被動替代都沒能在停轉期間主動示警，靠恢復後三條不相關 routine 各自撞見才拼出全貌）。建議升 OBSERVER-QUEUE 讓哲宇決定是否啟動。

### P1（兩週內，記錄不代辦）

3. **四天空窗根因追蹤**：目前只確認「現在已恢復」，未確認「為什麼停了」。若兩週內仍無人查，下次審計應將其標記為 chronic 未結案案例並升 OBSERVER-QUEUE。
4. `deferred-to-a-paused-escalation-target` 的候選修法已在 LESSONS entry 列出，distill 時的關鍵判斷是併入既有 REFLEXES #56 還是另立新號。

### P2（觀察）

5. 免疫黃燈滿 56 天，OBSERVER-QUEUE #25 待哲宇拍板資源投入方向，非本 routine 續追範圍。
6. `twmd-supporters-weekly` 本週排程（08-30 17:07 Taipei）落在本次審計窗口截止之後，尚未能確認是否恢復正常；下次審計（09-06）應優先核對其是否已連續兩輪恢復。

---

## 收官

本次審計本身就是一個活教材：**上一次 fire 沒有留下任何產出，這一次是同一條 routine 隔了整整一週才重新開口**。飛輪的韌性體現在三個地方——三條互不相關的 routine 各自在恢復後主動發現了同一個缺口（沒有一條假裝「跑得很順」）、上次審計標記的分類器 bug 在同一週窗口內就被接住修好、一次危機恢復 session 在四天 backlog 壓力下仍保持了 over-action 與 over-defer 之間的正確平衡。但也有一個地方飛輪還沒學會：當三份誠實的 handoff 同時指向一個空位置時，沒有任何機制會提醒它們——這正是本 routine 存在的理由，單一 routine 只看得到自己那一次撞見，跨 routine 視角才看得出三份 handoff 加總等於零人接手。

🧬

---

_v1.0 | 2026-08-30 21:19 +0800_
_session twmd-routine-audit-weekly（scheduled，遲到一週後首次重新產出）_
_誕生原因：第 15 次 cross-routine 飛輪自審，7-day 窗口內 4-lens pattern detection + LESSONS-INBOX 累積；本次審計對象包含審計者自己上一輪的靜默_
