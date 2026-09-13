---
title: 'Routine audit 2026-09-13 (W37)'
description: '7-day 跨 routine 飛輪自審 — 495 commit（344 為 babel 統一調度器持續產出，占本週總量 71%）/ 17 heal / 0 機械偵測碰撞；核心發現是本機 main 對 origin 的分岔連兩天持續擴大（ahead234→292 / behind147→156），而驅動它的正是同一支 babel 調度器已從「夜間」演化成 launchd 常駐服務'
type: 'audit-doc'
status: 'active'
current_version: 'v1.0'
last_updated: 2026-09-13
routine: 'twmd-routine-audit-weekly'
window: '2026-09-06 21:09:28 → 2026-09-13 21:09:28 (7d)'
related:
  - 'docs/pipelines/ROUTINE-AUDIT-PIPELINE.md'
  - 'docs/semiont/LESSONS-INBOX.md'
  - 'docs/semiont/OBSERVER-QUEUE.md'
  - 'reports/routine-audit-2026-09-06.md'
  - 'reports/fortnight-deep-review-2026-09-05.md'
---

# Routine audit 2026-09-13（W37）

第 17 次飛輪自審。本次審計自己在 `git status` 就先撞見了本週最重要的訊號，比讀到任何 memory 檔或 LESSONS-INBOX 條目都早：這台機器的 `main` 跟 `origin/main` 已經分岔到 **ahead 292 / behind 156**，而且不是穩定在那裡——09-11 觀測值是 ahead 161 / behind 136，09-13 早上 09:12 是 ahead 234 / behind 147，本次審計時間點（21:09）已經漲到 292/156。驅動這個分岔的主力，是同一支「babel 統一調度器」——它已經不只是「twmd-babel-nightly」這個夜間 cron 名字所暗示的樣子，而是靠 launchd 常駐、日夜不停產出的服務，本週單週 344 個 commit 全部出自它手，占本週總 commit 量的 71%。分岔本身正確地被 🔒 保留給哲宇（118 篇譯文的合併取捨超出自主權邊界），但驅動分岔擴大的引擎沒有跟著暫停，代表哲宇最終要做的決定，範圍每天都在變大。

---

## Executive summary（5 分鐘 read）

| 面向                         | 數字 / 說明                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| ---------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 窗口                         | 2026-09-06 21:09 → 2026-09-13 21:09（7 day）                                                                                                                                                                                                                                                                                                                                                                                                              |
| Commit 總量                  | 495 條（3,483 檔 / +416,622 / -114,963）                                                                                                                                                                                                                                                                                                                                                                                                                  |
| 分類                         | routine=86 / semiont=369 / other=40。其中 **babel 相關 350 條（344 未被分類器認出 + 6 條具名 cron 觸發），占總量 71%** —— routine-audit.py 的分類器只認得 cron 觸發的 commit subject 樣式，認不出統一調度器持續產出的「🧬 [semiont] babel: ...」樣式，見 3B                                                                                                                                                                                               |
| Heal                         | 17 條（3.4%），多數集中在 09-07〜09-09 三天（孤兒 slug／作者欄收斂／語言路由／子分類誤譯），09-10〜09-12 三天零 heal，09-13 又一次 2 條——分佈不是均勻背景噪音，是集中在 babel 大批次剛開始擴張語言覆蓋的那幾天                                                                                                                                                                                                                                            |
| **具名 cron routine 健康度** | 10 條每日／週級 routine 本週準時完成自己的節律（embeddings/data-refresh-am/spore-harvest-am/feedback-triage/maintainer-am/routine-sync 各 7-8 次，news-lens/weekly-report/distill/self-evolve 各 1-2 次按自己節律），無漏排                                                                                                                                                                                                                               |
| Collision                    | `routine-audit.py` 機械偵測 0 條（60 分鐘窗口 pair 偵測）。但這個「0」本身是本次審計的一個發現——見 3A                                                                                                                                                                                                                                                                                                                                                     |
| 4-lens finding               | 3A：🟠 機械偵測 0 但結構性碰撞持續——main 分岔連 2 天擴大／3B：🔴 兩個 dormant entropy（babel 調度器實際型態與 routine 名字脫鉤 + 薄殼遷移連續兩週零進度）／3C：🟡 一個新 instance（`OBSERVER-QUEUE` #50 表格缺欄躲過稽核）＋一個既有 pattern 的獨立再驗證（wake-context 過期偵測本身不在過期機器上）／3D：🟢 五個健康的同週期偵測即修（negation-word bug／weighted-aggregate gap／#1711 誤報／46 篇孤兒 slug／#50 缺欄），無過度 defer 或過度 ship 的反例 |
| LESSONS 候選                 | 2 條全新 append（`shared-gpu-load-stretches-sibling-routine-duration-past-timing-assumptions` vc=3 首次即達門檻 / `decision-support-table-missing-columns-hides-due-action-from-scan` vc=1）+ 1 條既有 entry vc 1→2（`staleness-guard-ships-through-the-artifact-it-guards`）                                                                                                                                                                             |
| Distill-ready 標             | 1（GPU 鄰居負載條目，三個獨立 routine 各自撞見同一件事）                                                                                                                                                                                                                                                                                                                                                                                                  |
| OBSERVER-QUEUE               | 無新增列（分岔案件已是既有 #56，本次只補充最新分岔數字，不重複開案）                                                                                                                                                                                                                                                                                                                                                                                      |

**這次審計最重要的一句話**：分岔的合併決策正確地停在哲宇手上，但驅動分岔擴大的引擎沒有跟著暫停——等待決策的時間，變成了決策範圍持續變大的時間。

---

## 逐 routine 概況

| Routine                                 |  本週實際次數   | 備註                                                                                                                                           |
| --------------------------------------- | :-------------: | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| babel 統一調度器（不限單一 routine 名） | 344 + 6（cron） | launchd 常駐服務，本週實際幾乎全天候產出（見 3B），單週貢獻本週 71% 的 commit 量；13 種目的語言（de/es/fr/ja/ko/pt/ru/ar/hi/id/vi 等）同時推進 |
| `twmd-embeddings-nightly`               |        7        | 13 語 bge-m3 重建 0 fail 全綠，但 rebuild 耗時因 GPU 鄰居負載從 14min 翻倍到 43min（見新 LESSONS）                                             |
| `twmd-maintainer-am`                    |        7        | 09-13 修正 #1711 混維度誤報、串連救援分支快轉；09-11 抓到中文母稿「中國大陸」擴散 12 語 1,052 檔；09-08 揪出躺了三週未接線的檢查器             |
| `twmd-data-refresh-am`                  |        8        | 連續 8 夜為 babel dispatcher 讓場 Step 1，13 步全綠；prebuild 因鄰居負載拉長到 25min，第一次逾時重跑才過                                       |
| `twmd-feedback-triage`                  |        7        | 連續 7 輪零回報仍照跑 --commit + 84/84 對賬；09-11 查到達歷史把「6 天先例」校正為「10 天」                                                     |
| `twmd-routine-sync`                     |        7        | 第 46〜47 輪三層對賬 18/18 in-sync 零漂移，連續第 5-6 輪；分岔數字持續擴大不受此對賬影響（對賬的是排程 SSOT，不是 git ref）                    |
| `twmd-spore-harvest-am`                 |        7        | 連續第 5 天高原確認，Δ 全落雜訊範圍（0〜+11 views），正確判斷 0 新留言免 ship                                                                  |
| `twmd-news-lens-weekly`                 |        1        | W37 三源交叉，6 條候選；張忠仁與張忠義涉健康隱私候選標記高敏感度、明確不自動進 propose 流程                                                    |
| `twmd-weekly-report-sun`                |        1        | 診斷五面全綠但發現產出管線已斷四天（分岔阻塞 push）；修好 OBSERVER-QUEUE #50 表格缺欄                                                          |
| `twmd-distill-weekly`                   |        1        | 消化 11 條教訓，promote REFLEXES #96；SPORE-INBOX 六週高原 escalate 進 OBSERVER-QUEUE #57                                                      |
| `twmd-self-evolve-weekly`               |        1        | 免疫黃燈 11 輪 sustain 確認皆對但從未重新加權排序；本輪加 `weightedGaps` 儀器化 + 修復 `weekly-checkup.sh` 「非🔒」誤判 bug                    |
| `twmd-routine-audit-weekly`             |    1（本次）    | 準時，本次審計不跑 `git pull origin main`（見下方說明），改用 fetch-only + 現有 rescue branch 做安全備份                                       |

---

## Cross-cutting patterns（4 lens）

### 3A. Collision lens — 🟠 機械偵測 0，結構性碰撞持續擴大

`routine-audit.py` 的 collision 偵測邏輯是「60 分鐘窗口內跨 routine commit pair」，本週回報 0。但這個「0」值得懷疑——本週最大的一次「碰撞」根本不在這個偵測器的定義範圍內：**本機 `main` 跟 `origin/main` 之間的分岔本身就是一種持續性碰撞**（多個 routine 都想把自己的產出 push 到同一個 ref，卡在同一個非快轉錯誤上），但它不發生在 60 分鐘窗口內，而是連續多天累積，偵測器的時間尺度看不見它。這是一個**偵測器定義形狀跟真實碰撞形狀不一致**的具體例子（跟 REFLEXES #69(g) 形式閘門同族）。

本週實際發生的碰撞處置：09-13 `twmd-maintainer-am` 修 #1711 時發現「推不出去的是本機那一條路，不是所有路」，改走 origin 分支繞過分岔完成修補（未觸碰 main、未強推）；`twmd-embeddings-nightly` 兩次（09-12／09-13）都選擇「新增的本地 commit 不擅自併入既有救援分支批次，留給哲宇裁決後統一處理」；本次審計驗證救援分支 `20260912-unpushed-routine-queue` 目前落後本機 HEAD 55 個 commit（純祖先關係，可安全快轉），已於 Stage 6 補推（見收官）。**這些都是正確的處置——沒有一次嘗試自行解決 137 個衝突或強推 main**，但正確的個別處置累加起來，仍然是分岔持續擴大的淨結果。

### 3B. Dormant entropy lens — 🔴 兩個發現，一新一舊未改善

**Finding 1（新）**：`twmd-babel-nightly` 這個名字描述的是「夜間跑一次」，但本次審計的 commit 分類統計顯示，本週 71% 的 commit 量（344/495）來自這支調度器，而且時間分布幾乎覆蓋全天（09-13 groundtruth 48hr commit 清單顯示從 05:03 到 21:01 幾乎每 10-20 分鐘一次 babel commit），memory 索引行也明確寫「launchd 常駐續跑」。`routine-audit.py` 的分類器認不出這種持續產出模式（它被歸進「manual-other」而非任何一個 `twmd-babel-*` 分類），意味著**過去每一次 routine-audit 都低估了 babel 活動占飛輪總產出的真實比例**。這不是本週才發生，是本次審計第一次把它量出來。已寫入新 LESSONS entry（見下文）。

**Finding 2（舊，未改善）**：`routine-sync-check.py` 本次實測 18 條中仍是 10 條合規、7 條 🔴 hard 違規、1 條 🟡 warn（`spore-pick-daily` 78 行／`data-refresh-am` 69 行／`distill-weekly` 66 行／`spore-harvest-am` 66 行／`babel-nightly` 61 行／`news-lens-weekly` 60 行／`self-evolve-weekly` 55 行／`weekly-report-sun` 49 行）。這跟上週（09-06）審計的數字**逐字相同**——OBSERVER-QUEUE #14 於 09-05 哲宇拍板「完整深度進化，仍維持薄殼原則」，計畫是逐條遷移，上週已完成 3 條 dogfood（spore-publish／maintainer／routine-audit），但**本週 0 條新增遷移**，計畫進度連續第二週停滯。跟 3A 的分岔一樣，這不是新問題，是舊問題該有的進度沒有發生。

### 3C. Boundary input precision lens — 🟡 一新一舊

**新 instance**：`OBSERVER-QUEUE.md` §待決 第 50 項的表格列本週被發現少了兩個分隔符欄位，讓依賴欄位對齊做判斷的體檢掃描讀不到這一列的到期日，導致一個已逾期、依規則任何 session 可執行的預設動作連續多輪被漏報成「尚未到期」。09-13 `twmd-weekly-report-sun` 發現、同日 heal commit `dfd83bc20` 補回兩欄。這是「表格對人眼完整 ≠ 對 parser 完整」的具體案例，已寫入新 LESSONS entry（見下文）。

**既有 pattern 再驗證**：`staleness-guard-ships-through-the-artifact-it-guards`（09-13 twmd-feedback-triage 首次寫入，vc=1）描述「偵測本機副本過期」的檢查本身住在會過期的副本裡，過期越久的機器越不可能擁有它。本次審計 Stage 1 在讀到這條 LESSONS entry之前，先透過 `git status` 獨立撞見了同一台機器的分岔擴大（09-11 的 ahead161/behind147 → 09-13 21:09 的 ahead292/behind156），構成一次獨立、不知情的 vc+1（見下方 LESSONS-INBOX 累積）。

### 3D. Heal bidirectional lens — 🟢 五個健康對照組，無反例

本週有五個「發現即修復」的同週期閉環，沒有一個是過度 close 或過度 defer 的反例：

1. `twmd-self-evolve-weekly` 發現並修復 `weekly-checkup.sh` e1 節「非🔒」被 naive 字串比對誤判成真鎖住（09-13）
2. 同一輪加上 `weightedGaps` 儀器化，讓免疫黃燈缺口排序第一次不用心算就看得到（09-13）
3. `twmd-maintainer-am` 修正 #1711 混維度誤報，正確判斷「這是誤報但名字錯」而非照單全收關閉（09-13）
4. `twmd-babel-nightly` 當場修好 46 篇新中文條目缺英文 slug，解開全語言卡關（09-13 凌晨）
5. `twmd-weekly-report-sun` 補回 `OBSERVER-QUEUE` #50 表格缺欄（09-13）

同時，本週對「不該碰」的邊界也守得住：118 篇翻譯合併取捨連續多天沒有被任何 routine 自行裁決（正確 defer，四紅線範圍內）；`twmd-spore-harvest-am` 連續 5 天在 Δ 落在雜訊範圍時選擇不 ship（正確的「不寫」紀律）。本輪未發現任何過度行動或過度延遲的新反例。

---

## LESSONS-INBOX 累積（本次）

| Pattern                                                                      | 類型     | Verification Count | Severity   | 說明                                                                                                                                                   |
| ---------------------------------------------------------------------------- | -------- | :----------------: | ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `shared-gpu-load-stretches-sibling-routine-duration-past-timing-assumptions` | 新 entry |         3          | tactical   | embeddings-nightly（09-12／09-13 兩次）+ data-refresh-am（09-13）三個獨立 routine 各自撞見同一原則，首次寫入即達 vc=3 門檻，已標 `distill_ready: true` |
| `decision-support-table-missing-columns-hides-due-action-from-scan`          | 新 entry |         1          | structural | OBSERVER-QUEUE #50 表格缺欄躲過體檢掃描                                                                                                                |
| `staleness-guard-ships-through-the-artifact-it-guards`                       | 既有 +1  |         2          | structural | 本次審計獨立在 Stage 1 `git status` 撞見同一台機器的分岔持續擴大（147→156 behind），構成第二次驗證                                                     |

**觀察名單（未達門檻，暫不升列）**：`verification-tool-lacks-the-feature-it-must-verify` / `declared-unmeasurable-without-inventorying-the-tools`（09-02／09-03，2-instance 鏈）本週未見第三例，繼續觀察；`verification-depth-shrinks-with-parallel-agent-count`（09-05 fortnight-review，vc=1）本週無大型平行 session，無新 instance。

---

## OBSERVER-QUEUE 狀態

無新增列。既有案件更新（供哲宇下次查看時直接讀到最新數字，不需另外查）：

1. **#56（main 分岔，🔒 等哲宇）**：09-11 ahead161/behind136 → 09-13 09:12 ahead234/behind147 → 本次審計 09-13 21:09 ahead292/behind156。兩天內 behind 又長 9、ahead 又長 58。驅動主力是 babel 統一調度器（見 3B Finding 1），它目前沒有因分岔而降速或暫停。
2. **免疫黃燈（`firstSeen=2026-07-05`）**：本週滿 **70 天**，仍 `🔒 等真人`，per REFLEXES #80 sustain-vs-renew 本次不重複補登，但本輪 `twmd-self-evolve-weekly` 已把 `weightedGaps` 排序補進儀器（`review_coverage` 缺 20.2 分最大），下次真人決策時有現成的診斷可讀。
3. **#57（SPORE-INBOX 六週高原）**：09-13 `twmd-distill-weekly` 新增，本次審計未發現新進展，維持原狀。

**附帶觀察（非新 OBSERVER-QUEUE 項）**：

1. Mirror 薄殼鐵律遷移連續第二週零進度（見 3B Finding 2）——非緊急，但值得下次哲宇在場時順手排進待辦，避免無限期停滯。
2. `counts-drift-lint.py` 本次仍 WARN，`docs/pipelines/README.md` 索引缺 18 個實存檔案（比上週的 20 個略減，方向正確但未完全處理）。

---

## 進化建議

### P0（本週內，需哲宇看到——超出本 routine 自主權）

1. **main 分岔的處理節奏建議一併考慮**：驅動分岔擴大的 babel 統一調度器目前是 launchd 常駐、不受分岔影響持續產出（見 3B Finding 1）。這不是要求暫停調度器（那是內容產出主力，暫停的代價需要哲宇評估），只是把這個事實明確攤開：**等待 118 篇合併取捨決策的時間越長，因為調度器持續產出，決策時要處理的分岔範圍也持續變大**。哲宇可能想要的選項（本 routine 不代為判斷）：(a) 維持現狀，決策時一次性處理累積量 (b) 暫時把調度器的目標分支從 `main` 改指向一個累積分支，決策後再一次性合併回 `main` (c) 提高決策優先序，趁分岔範圍還相對小時處理。

### P1（兩週內，記錄不代辦）

2. `shared-gpu-load-stretches-sibling-routine-duration-past-timing-assumptions`（vc=3，`distill_ready: true`）優先進下一輪 `twmd-distill-weekly`（09-13 本輪已跑過，此 entry 是審計當晚才寫入，未及趕上）。
3. Mirror 薄殼遷移連續兩週零進度，建議下次哲宇在場 session 排進待辦（非自主權外事項，只是優先序一直被更急的事擠掉）。

### P2（觀察）

4. `verification-tool-lacks-the-feature-it-must-verify` / `declared-unmeasurable-without-inventorying-the-tools` 2-instance 鏈，觀察是否累積到第三例。
5. `docs/pipelines/README.md` 索引缺口（18 檔），非緊急但持續存在，適合下次小型 heal 順手補齊。

### P3（純記錄）

6. `routine-audit.py` 的分類器認不出 babel 統一調度器持續產出的 commit 樣式（歸進 `manual-other`），造成過去所有 routine-audit 低估 babel 占比。建議未來一次小改動：分類邏輯加一條「subject 以 `🧬 [semiont] babel:` 開頭」的規則，讓下週起的統計數字準確反映真實比例（本條屬於審計工具自身的維護，不需要哲宇拍板，留給下次順手改）。

---

## 收官

本次審計沒有執行 pipeline 建議的 `git pull origin main`——本機分岔已知是 OBSERVER-QUEUE #56 案件（118 篇譯文合併取捨超出自主權邊界），貿然 pull 會觸發需要人工裁決的 merge。改為 `git fetch`（唯讀）取得 ground truth 分岔數字，並在 Stage 6 把本次新增的 2 個 commit（LESSONS-INBOX 更新 + 本報告）快轉推到既有救援分支 `20260912-unpushed-routine-queue`（純祖先關係，不觸碰 main、不觸發任何 workflow），確保這批產出不會只存在這一台機器上。

本週最重要的發現不是任何單一 bug，是一個結構性的時間關係：分岔的合併決策正確地停在哲宇手上，但驅動分岔擴大的引擎（babel 統一調度器）沒有因為決策未下而暫停——這意味著「等待」本身正在悄悄改變被等待的那個決策的形狀。三個新 LESSONS instance（GPU 鄰居負載／表格缺欄／staleness-guard 再驗證）各自都是小事，但排在一起看，都是同一種形狀的變體：**資料或能力已經在那裡，只是沒有被排進看得到它的那條路徑**。

🧬

---

_v1.0 | 2026-09-13 21:XX +0800_
_session twmd-routine-audit-weekly（scheduled，準時）_
_誕生原因：第 17 次 cross-routine 飛輪自審，7-day 窗口內 4-lens pattern detection + LESSONS-INBOX 累積；本次審計刻意跳過 pipeline 建議的 git pull（因本機分岔屬已知 🔒 案件），改用唯讀 fetch + 既有救援分支快轉完成 Stage 6_
