---
title: 'Routine audit 2026-08-16 (W33)'
description: '7-day 跨 routine 飛輪自審 — 291 commit / 55 heal / 0 排程碰撞；分類器誤歸類教訓第三輪連續確認未修（vc 2→3, distill-ready）；新記一條跨 routine 家族綜合發現——本週五條獨立教訓其實是同一種「雙方沒有東西在對賬」的結構，單一 routine 視角看不出來'
type: 'audit-doc'
status: 'active'
current_version: 'v1.0'
last_updated: 2026-08-16
routine: 'twmd-routine-audit-weekly'
window: '2026-08-09 21:09:08 → 2026-08-16 21:09:08 (7d)'
related:
  - 'docs/pipelines/ROUTINE-AUDIT-PIPELINE.md'
  - 'docs/semiont/LESSONS-INBOX.md'
  - 'docs/semiont/OBSERVER-QUEUE.md'
  - 'reports/routine-audit-2026-08-09.md'
---

# Routine audit 2026-08-16（W33）

第 14 次飛輪自審。窗口內 291 個 commit，比上週（291 對照上週 683）少了超過一半——量的來源這次不是巴別塔渦流放緩，是上週的越南語五批續落地本週已收尾，本週回到「日常 routine + maintainer 批次 heal + 一篇長文重寫」的常規節奏。**具名 cron routine 全部準時 fire，0 排程碰撞**。本次審計最重要的發現有兩層：第一層是稽核工具自己的舊病——分類器誤歸類教訓第三次連續命中同一批 routine，範圍沒有縮小；第二層是本次審計真正的存在理由——把本週 `twmd-maintainer-am` 與 `twmd-feedback-triage` 各自寫下的五條教訓排在一起看，才看出它們是同一個家族（兩個該互相印證的東西各自演化，中間沒有機制對賬），而這五條各自的「相關」欄彼此零交叉引用，因為每個 routine 只看得到自己那一次撞見。

---

## Executive summary（5 分鐘 read）

| 面向                         | 數字 / 說明                                                                                                                                                                                                                                                           |
| ---------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 窗口                         | 2026-08-09 21:09 → 2026-08-16 21:09（7 day）                                                                                                                                                                                                                          |
| Commit 總量                  | 291 條（1,248 檔 / +123,621 / -51,866）                                                                                                                                                                                                                               |
| 分類                         | semiont=86 / routine=98 / other=105（多為外部 PR merge、貢獻者翻譯 PR、新文章 Create） / pr-squash=2                                                                                                                                                                  |
| Heal                         | 55 條（18.9%，比重明顯高於上週 4.5%）— 集中在 08-14/08-15 的貢獻者批次格式修復＋語言層 i18n bug 連環修                                                                                                                                                                |
| **具名 cron routine 健康度** | **13/13 準時 fire，0 缺席**（`twmd-flywheel-watch` 已於 08-10 哲宇 directive 停用，不計入健康度分母；`twmd-terminology-trends-monthly` 為月度 routine，本週非排程日，0 屬正常）                                                                                       |
| Collision                    | 0 條（`routine-audit.py` 回報，且手動檢查全部 5 分鐘內近接 commit 皆為同排程 routine 自身 action→memory 的正常先後，非跨 routine 撞窗口）                                                                                                                             |
| 4-lens finding               | 3A：0 collision instance（正常）/ 3B：1 個既有 pattern 三度確認未修（distill-ready）+ 1 個新的跨 routine 家族綜合發現（vc=5，distill-ready）/ 3C：1 個既有 pattern 再驗證（財經數字換算） / 3D：1 個健康對照組（root-cause 診斷後正確走逐篇 atomic heal，非過度批次） |
| LESSONS 候選                 | 1 條全新 append（`twin-artifact-no-reconciler-family`，vc=5，本週窗口內即達門檻）+ 1 條既有 entry vc 累積（2→3，第三輪連續確認）                                                                                                                                      |
| Distill-ready 標             | **2 條**（`routine-audit-classifier-memory-commit-misattribution` vc=3；`twin-artifact-no-reconciler-family` vc=5）                                                                                                                                                   |
| OBSERVER-QUEUE               | 無新增。#25（免疫黃燈）本週滿 **42 天**仍 `🔒 等真人`（alert-age 升列已於 08-02 完成，本次不重複補登）。`UNKNOWNS EXP-2026-07-17-G` 齡 8 天，未跨 14 天門檻                                                                                                           |

**這次審計最重要的一句話**：三次獨立 cycle（08-02／08-09／08-16）盯著同一份分類器資料，範圍只有擴大沒有縮小——這是「發現了但沒人修」的活教材；同時本週第一次示範了本 routine 存在的核心價值：單一 routine 的 Beat 5 只看得到自己那一次撞見，跨 routine 7-day 視角才看得出五條教訓其實是同一個家族連續一週出現五次。

---

## 逐 routine 概況（13 條具名 cron routine，全數健康；1 條已停用不計）

| Routine                           |   本週實際次數（tight grep 交叉核對）    | 備註                                                                                                                                        |
| --------------------------------- | :--------------------------------------: | ------------------------------------------------------------------------------------------------------------------------------------------- |
| `twmd-data-refresh-am`            |                    13                    | 14 步全綠零 stale 連續第五天，文章數 889→921（本週 +32），scheduler live-state rider 無條件照跑                                             |
| `twmd-spore-harvest-am`           |                    6                     | v1.15.0 release 孢子 D+1～D+5 續追，X 端瀏覽器登入態自 08-12 起連續未恢復（第六天 handoff carry）                                           |
| `twmd-feedback-triage`            |                    12                    | 五月天冠佑學歷勘誤開成 issue #1390，第三人指控信連續第三次 `--exclude` 攔下（HG13 三層同步已 ship），對賬 74-75/74-75                       |
| `twmd-maintainer-am`              |                    8                     | 週內三天（08-13/08-14/08-16）連續被同一位貢獻者批次撞同一道 frontmatter/格式閘門，08-15 25 PR 升 Full mode，08-15 另跑一次 workshop-pr 專場 |
| `twmd-routine-sync`               |                    8                     | 三層對賬第十七～二十三輪，連續五輪零漂移                                                                                                    |
| `twmd-embeddings-nightly`         |                    7                     | bge-m3 nightly 12 語重建 0 fail，連續三夜僅 zh-TW 一行鄰居關係變動（SSOT 檔案異動量與語意鄰居重排量脫鉤已成穩定觀察窗）                     |
| `twmd-news-lens-weekly`           |                    1                     | W33 三源交叉：陳幸妤離婚 GA+SC 雙源同步印證，無人機 232 關稅示範讀反時間差教訓                                                              |
| `twmd-distill-weekly`             | 1（單一合併 commit，action+memory 未拆） | W33：§未消化 40→32，5 條 promote REFLEXES #86-90 + 2 fold + 1 MEMORY §神經迴路                                                              |
| `twmd-self-evolve-weekly`         |                    1                     | 從 raw diary rows（非 curated 反覆思考清單）找到 vc=4 pattern，升 REFLEXES #91（建造與登記是兩個不同步的代謝）                              |
| `twmd-weekly-report-sun`          |                    1                     | W33 週體檢，診斷五面零沉默死亡；判掉過期九天的 404 實驗（14.99%→4.34% 命中）；修好週報切菜工具「交付文章」空節整段消失的 bug                |
| `twmd-supporters-weekly`          |                    1                     | 例行同步，本週未見異常                                                                                                                      |
| `twmd-terminology-trends-monthly` |                    0                     | 月度 routine，本週非排程日（上次 08-04 首輪誕生，下次約 09-05），0 屬正常非缺席                                                             |
| `twmd-routine-audit-weekly`       |                1（本次）                 | ——                                                                                                                                          |

**停用中**：`twmd-flywheel-watch`（08-10 哲宇 directive「幫助不大」停用，非退休；`/twmd-flywheel-watch` 手動仍可跑，本週不計入健康度分母）。

---

## Cross-cutting patterns（4 lens）

### 3A. Collision lens — 🟢 0 instance

`routine-audit.py` 回報 0 collisions。手動抽查本週所有 5 分鐘內近接的 `[routine]`/`[semiont]` commit 對，全部是**同一條 routine 自己的 action commit → memory commit** 先後（例如每天 05:36-05:39 `twmd-embeddings-nightly` 完工後緊接 `twmd-routine-sync` 開跑，兩者排程本就相鄰 1 分鐘，非撞窗口），或同一 session 內連續的正常工作步驟（如 08-15 台灣證券交易所 REWRITE 各 lane 間隔 50-200 秒）。本週窗口內沒有發現任何跨 routine 的 rescue / orphan process / 孤兒 worker 訊號。

### 3B. Dormant entropy lens — 🟠 兩個 finding：一舊一新

**Finding 1（既有 pattern，第三輪連續確認未修，達 distill 門檻）：`routine-audit.py` 分類器 memory-commit 誤歸類**

08-02 記錄兩個 routine 受影響、08-09 擴大到「幾乎所有具名 routine」、本週第三輪重新 tight-grep 核對：`twmd-routine-sync`（實際 8，分類器 key 完全缺席）與 `twmd-weekly-report-sun`（實際 1，分類器 key 完全缺席）兩條這次連 key 都沒有出現在 `by_routine` 裡（不是顯示偏低，是整條看不見），`twmd-data-refresh-am`（分類器 7 / 實際 13）與 `twmd-feedback-triage`（分類器 7 / 實際 12）持續系統性低估。三次獨立 cycle（08-02／08-09／08-16）同一根因、範圍沒有縮小，已在 [LESSONS-INBOX `routine-audit-classifier-memory-commit-misattribution` instance 3](../docs/semiont/LESSONS-INBOX.md) 詳記，vc 2→3，標記 `distill_ready: true`。**這是已知缺陷連續三週未修復的活教材**，本次審計仍靠 git log tight-grep 交叉核對繞過，不影響本報告數字準確性，但工具自己的可信度該修了。

**Finding 2（新發現，本週窗口內即達 vc=5，distill-ready）：五條獨立教訓是同一個「雙方沒有東西在對賬」的家族**

本輪核對本週新增的全部 LESSONS-INBOX entry 時，發現以下五條各自獨立、彼此「相關」欄零交叉引用，但壓縮後是同一句話的五種措辭：

| 日期  | Routine         | Entry                                                  | 一句話                                                                               |
| ----- | --------------- | ------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| 08-10 | feedback-triage | `formatter-vs-generator-quote-churn-fakes-scope-alarm` | 產生器與 pre-commit formatter 對引號寫法不同調，讓範圍閘門喊假警報                   |
| 08-13 | feedback-triage | `reflex-exists-but-not-a-step-on-this-line`            | REFLEXES #57 目錄裡有，這條 routine 的 cron prompt 裡沒有對應步驟                    |
| 08-14 | maintainer-am   | `sibling-checks-share-one-blind-premise`               | 兩支姊妹檢查器（footnote-format / footnote-density）共用同一個看不見渲染式腳註的前提 |
| 08-14 | maintainer-am   | `doc-and-validator-drift-has-no-reconciler`            | CONTRIBUTING 範本三個月沒補 `subcategory`，`test-frontmatter.mjs` 早已把它升硬門檻   |
| 08-16 | maintainer-am   | `fix-scope-follows-symptom-not-root-class`             | 同一份文件的散文與媒體那半，一樣沒有任何門檻教它——只是還沒輪到它現形                 |

單一 routine 的 Beat 5 只看得到自己那一次撞見（例如 08-16 那條明確寫了「我讀過 8/14 那條診斷，然後踩了同型」，但它讀的是自己 routine 的 handoff，看不到 feedback-triage 那兩條）。**這正是 cross-routine 7-day 視角能看見、單一 routine 看不見的東西**——五個 instance 橫跨兩條 routine，比任何單一 entry 的 vc 累積都更能說明這是系統性缺口。已在 LESSONS-INBOX 新開 `twin-artifact-no-reconciler-family`，vc=5 起計，並標記與既有 REFLEXES #56（Pipeline canonical ↔ production drift）為近親，建議 distill 判斷併入或另立新號。

### 3C. Boundary input precision lens — 🟡 一個既有 pattern 再驗證

08-15 `ratio-self-consistency-masks-magnitude-error`（PR #1367 淨利率表把 $416.2B 誤讀成「416 億」漏掉單位換算，比率算得通所以所有一致性檢查全綠）本身是本週 within-routine 已捕捉的 instance，非本審計新發現；但拉到 boundary-input-precision lens 視角看，它與上週的「PR body 描述 vs diff 實算」屬同一個 lens 家族——**絕對值與由它衍生的比率同時出現時，比率自洽對分子分母同乘同除免疫**，這次的來源不是二手敘述而是單位換算，lens 覆蓋範圍比原先設想的更廣。記錄供對照，vc 累積留給既有 entry 自己的軌跡（見 LESSONS-INBOX 08-15 twmd-maintainer-workshop-pr 條目），本次不重複開新 entry。

### 3D. Heal bidirectional lens — 🟢 一個健康對照組

08-15 08:53 `twmd-maintainer-am` 診斷出「網址尾一個空格，變成 353 條看起來無關的腳註格式錯誤」根因後，同日 17:07-17:13 的實際修補走的是**逐篇 atomic commit**（22 篇文章、22 個獨立 heal commit，每篇 2-4 秒間隔），而不是一次性機械批次覆蓋——這是正確的 over-action/under-action 平衡：根因已確認是系統性的，但落地修補仍保持每篇一個可獨立 revert 的 commit（per REFLEXES #6 commit 範圍紀律），沒有為了效率把 22 篇的變更揉進一個大 commit。記錄為本週唯一的正向對照組，未見新的 over-close / over-ship / over-defer instance。

---

## LESSONS-INBOX 累積（本次）

| Pattern                                                 | 類型         | Verification Count | Severity      | 說明                                                                                                    |
| ------------------------------------------------------- | ------------ | :----------------: | ------------- | ------------------------------------------------------------------------------------------------------- |
| `twin-artifact-no-reconciler-family`                    | 新 entry     |         5          | moderate-high | 本週窗口內五個獨立 instance 橫跨兩條 routine，本次審計唯一需要跨 routine 視角才看得見的發現             |
| `routine-audit-classifier-memory-commit-misattribution` | 既有 vc 累積 |        2→3         | tactical      | 第三輪連續確認未修，範圍沒有縮小（`twmd-routine-sync`／`twmd-weekly-report-sun` 兩條 key 本週整條消失） |

§未消化清單本次新增 1 條全新 entry。兩條均已標 `distill_ready: true`，交下次 `twmd-distill-weekly`（下週日 03:00，早於本 routine 12:00 的固定順序）處理。

---

## OBSERVER-QUEUE 狀態

無新增列。#25（免疫器官 yellow 警報，`firstSeen=2026-07-05`）本週滿 **42 天**，仍 `🔒 等真人`——alert-age 升列已於 2026-08-02 完成，本次不重複補登。`UNKNOWNS EXP-2026-07-17-G` 齡 8 天（`firstSeen=2026-08-08`），未跨 14 天門檻，留給下週審計追蹤（若下週仍未判定，將於下次 cycle 跨過門檻，需補登）。

**附帶觀察（非新 OBSERVER-QUEUE 項，僅記錄供 §14 決策參考）**：本 routine 自己的 cron mirror 殼層本週實測 **60 行**（`routine-sync-check.py` 標 🔴 THICK，warn>30 hard>50），跟 OBSERVER-QUEUE #14「建議先讓 routine-audit 從 49→≤30 當 dogfood」的方向相反——不是縮小到 ≤30，是從 49 長到 60。#14 本身已「退回哲宇」定案（不由 session 自行動手瘦身，因跟 2026-05-28 CONTRACT rollback 教訓直接對撞），本次不採取行動，僅如實記錄殼層厚度的最新讀數供哲宇下次裁決時參考。

---

## 進化建議

### P0（本週內，自主權內）

1. **`routine-audit.py` 補齊具名 pattern 的 memory-commit wildcard**：三輪 cycle 確認範圍是「幾乎所有具名 routine」，且沒有隨時間縮小。修法方向 LESSONS entry 內已寫兩個候選（(a) 補齊每個具名 pattern 的 memory 變體 (b) 把通用 `routine-memory` pattern 移到具名 fallback 之後）。這是本審計工具連續三週回報的同一個 bug，建議下次 self-evolve 或任一 session 直接動手修，不需要再等第四輪確認。

### P1（兩週內，記錄不代辦）

2. **`twin-artifact-no-reconciler-family` 的五個 instance 各自的修補候選已在原 entry 列出**（对賬腳本、gate 落地成步驟等），這裡不重複；distill 時的關鍵判斷是「這是不是該併入 REFLEXES #56、擴大其範圍」，而不是逐條各自升級。
3. **本 routine 自己的 mirror 殼層厚度持續追蹤**：49→60 行，若下週再度增長建議在 handoff 明確標出增長速度，讓 OBSERVER-QUEUE #14 的裁決材料更完整。

### P2（觀察）

4. 免疫黃燈滿 42 天，OBSERVER-QUEUE #25 待哲宇拍板資源投入方向，非本 routine 續追範圍。
5. `UNKNOWNS EXP-2026-07-17-G` 齡 8 天，下週若仍未判定將跨過 14 天門檻，需補登 OBSERVER-QUEUE。

---

## 收官

本週具名 cron routine 飛輪本身完全健康，13/13 準時、0 碰撞。真正的訊息分兩層：**已知的分類器缺陷連續第三週未修，範圍沒有縮小**——這是「發現了但沒人接手修」的具體例子，不是新問題卻也不該再被當成「已知，繼續觀察」擱置；**新發現的跨 routine 家族**則正面示範了本 routine 存在的理由——五條教訓分散在兩條不同 routine 的 Beat 5 裡，每一條都寫得清楚、都各自 vc=1，但只有把七天內全部 routine 的產出攤開並排比對，才看得出它們是同一個結構性缺口的五個臉孔。單一 routine 看得見樹，這條 routine 的工作是看見森林。

🧬

---

_v1.0 | 2026-08-16 21:32 +0800_
_session twmd-routine-audit-weekly（scheduled）_
_誕生原因：第 14 次 cross-routine 飛輪自審，7-day 窗口內 4-lens pattern detection + LESSONS-INBOX 累積_
