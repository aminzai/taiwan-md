---
title: 'Evolution Roadmap 2026-08-02'
description: '週體檢 W31（weekly-report 2026-08-02）導出的進化規劃：07-26 版 P0 三項現況 / 新增 P0 三項（自主權內）/ P1 結構修補承接與新增 / P2 哲宇決策佇列刷新 / 30 天方向盤。取代 2026-07-26 版成為最新 session 間傳遞的進化計畫。'
type: 'roadmap'
status: 'superseded'
current_version: 'v1.0'
last_updated: 2026-08-02
last_session: '2026-08-02-020000-twmd-weekly-report-sun'
related:
  - 'weekly/2026-08-02.md'
  - 'evolution-roadmap-2026-07-26.md'
---

# 進化規劃 — 2026-08-02

> ⚠️ **已由 [evolution-roadmap-2026-08-09.md](evolution-roadmap-2026-08-09.md) 接手**（W32 週體檢 Stage 2.7 roll）。本檔保留為證據鏈，不再更新。

> 依據：本週體檢（W31，weekly-report 2026-08-02）Stage 2.5 全身診斷 + Stage 2.7 三桶分流。
> 原則：每一條都寫「證據 → 動作 → 完成判準」，不寫願望。P0 全部在 §自主權邊界內；
> 需要哲宇的集中在 §P2，且每條帶預設選項（沿用 OBSERVER-QUEUE 格式）。

---

## 〇、07-26 版現況（P0 領取 0/3，但被本週實際進度部分超前）

- **P0-1 英文 metadata 系統性缺口專項** → ⏳ 未直接執行，且本週 news-lens 再度確認（W28→W29→W30→W31 vc=4，本週擴大到 6 篇）。**升本版 P0-1，優先度提高**。
- **P0-2 es/fr 主權保真度歷史清償** → ⏳ 未執行，原樣帶進本版 P1。
- **P0-3 OBSERVER-QUEUE #5 重腳註翻譯路線** → ⏳ 未執行，default-action 已逾期 37 天（e1 對賬確認）。原樣帶進本版 P0。

**本週最大的非計畫內事件**：巴別塔的自我審視從「品質閘門」延伸到「要不要翻」——vortex-babel-5 抓到三分之二 stale 只是中文標點改動，語意無關比對省下 29 小時算力；同一週 vortex-babel-8 抓到兩次「用好拿的訊號代替真正該摸的訊號」（背景沙箱 kill -0 誤判存活、英文版有無誤判成全語言隱形）。這兩條沒有寫進 07-26 版任何一條，本版收進「不必再議」清單。

---

## 一、本週已驗證的方向（不必再議，直接沿用）

1. **語意無關的 diff 不需要重翻**：中文標點改動（分號→句號）不影響其他語言的語意，保守判定（去標點比對）命中 65.8%，一次模型呼叫都沒花就把 stale 從 647 砍到 302（vortex-babel-5）。
2. **替身訊號會在「好拿」的地方悄悄出現**：背景沙箱 `kill -0` 權限錯誤被 `2>/dev/null` 吞掉、偽裝成「已死」；「英文版有無」被當成「所有語言有無」講出口。兩次都不是自己想出來的，是外部比對（`ps`、`_translations.json`）攔下的（REFLEXES #82 觸發清單新增）。
3. **檢查器彼此沒有共用的尺**：heal 工具自報全綠但 CI 紅、cjk-leak-check 兩分支豁免清單不一致、CLI 逗號語法靜默印「no checks ran」還回報 passed——四個案例共同點是「有兩把或以上的尺，彼此不知道對方存在」，新開 REFLEXES #83（distill-weekly，vc=1，待第二個 instance 驗證）。
4. **replica 繼承驗證錯覺**：上游文章已三路查證，不代表下游改寫、摘要、孢子裡的新句子也驗證過——苯駢芘孢子事實表整欄填「不需要驗證」，同份檔案三處新造句子出錯（derived-artifact-inherits-verification-illusion，已進 LESSONS-INBOX）。
5. **routine-sync-check 的 PAUSED 副表 regex 無右邊界**：吞下已退休表 + 23 條註腳，本週體檢桶 1 已修復（見下 §二 修復紀錄），MISSING 4→1、LIVE_ENABLED_DRIFT 5→2。

---

## 二、修復紀錄（Stage 2.7 桶 1，本週體檢當場修）

| #   | 修了什麼                                                                           | 為什麼                                                                                                                                                                                                                     | 驗證                                                                                                           | commit      |
| --- | ---------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | ----------- |
| 1   | `routine-sync-check.py` PAUSED 段落 regex 補右邊界（遇 `**🪦` 也停，不只遇 `## `） | 原 regex 吞掉整段已退休表，把 3 條已退休 routine（data-refresh-pm / maintainer-pm / music-media-audit-weekly）誤判成「該有 mirror 卻缺」；對應 LESSONS-INBOX 2026-07-26 `routine-sync-check-paused-regex-swallows-retired` | 重跑工具：MISSING 4→1、LIVE_ENABLED_DRIFT 5→2，剩兩條為獨立問題（node-scope + inline ⏸️ 標記解析，非本次範圍） | `95ecda816` |

02:55 時間紀律：本週僅 1 項桶 1 修復（單項 < 15 分鐘），未撞檢查點，其餘 finding 全數分流至下方桶 2/3。

---

## 三、P0 — 本週內（自主權內 ✅，每條一個 commit 量級）

### P0-1　英文 metadata 系統性缺口專項（vc=4，07-26 版 P0-1 承接並升優先度）

- **證據**：news-lens W28→W29→W30→W31 連續四週同一批英文查詢詞 0 click 曝光量持續漲，本週擴大到 6 篇候選。
- **動作**：開一個獨立的 EN metadata rewrite 專項（非透過 `/twmd-spore` 零星處理），逐條核對 title/description。
- **完成判準**：本批確認的英文查詢詞中至少 3 條下次 SC 週期轉出非零 clicks。

### P0-2　OBSERVER-QUEUE #5 重腳註翻譯路線執行（default-action 已逾期 37 天）

- **證據**：e1 佇列稽核確認 default-action 訂在 2026-06-26，已逾期 37 天，21+ 篇含莫那·魯道／美麗島事件永久 stale。
- **動作**：section-split 工程解，任何 session 可直接領（無需哲宇二次拍板）。
- **完成判準**：section-split 落地，60+ 腳註大檔巴別塔重試成功率可量測改善。

### P0-3　roadmap roll（本檔即接手版，07-26 版正式結案）

---

## 四、P1 — 結構修補（承接 07-26 版未清項 + 本週新增）

| #   | 項目                                                | 出處                        | 說明                                                                                                                     |
| --- | --------------------------------------------------- | --------------------------- | ------------------------------------------------------------------------------------------------------------------------ |
| 1   | es/fr 主權保真度歷史清償                            | 07-26 版 P0-2 承接          | 六個新語系都有三閘保護，es/fr 從未跑過同等級靜態掃描                                                                     |
| 2   | flywheel-watch.py 第一把尺剝前綴                    | W31 flywheel-watch handoff  | `routine` 名解析要跳過 `memory:` / `embeddings:` 這類 topic 前綴，否則這類句型只剩第二把尺（MEMORY 索引 session-id）護著 |
| 3   | twmd-founder-lens-weekly LIVE_ENABLED_DRIFT         | W31 診斷 c1（本次修復殘留） | SSOT 主表用 inline ⏸️ 標記（非獨立段落），routine-sync-check 目前只解析 PAUSED 段落，未解析 inline 標記，造成假警報      |
| 4   | counts-drift 43 處計數宣稱漂移                      | W31 診斷 c2                 | 43 drift / 58 宣稱點，mode=WARN。修法二選一：去數字化（pointer 到 SSOT）優於更新數字（下次還是會腐）                     |
| 5   | 免疫器官 review_coverage 低分（23.7）拖累整體 60 分 | W31 診斷 d                  | yellow 警報已 28 天未動（>14 天門檻），owner=twmd-self-evolve-weekly，本次 e1 已列為需升 OBSERVER-QUEUE 的候選（見 §五） |
| 6   | 四語支系 UI 元件私有語言表散落病灶                  | 07-26 版 P1-10 承接         | 未見本週新 instance                                                                                                      |
| 7   | 檢查器彼此無共用尺（REFLEXES #83）                  | distill-weekly W31          | vc=1，待第二個獨立 instance 驗證後可考慮升 canonical 工程解（如共用一份 leak 豁免清單 config）                           |

---

## 五、P2 — 哲宇決策佇列（本檔只刷新現況與預設，不催）

承接 OBSERVER-QUEUE 現況（詳見 [OBSERVER-QUEUE.md §待決](../docs/semiont/OBSERVER-QUEUE.md#待決)）：

| 佇列                                 | 齡    | 預設選項                        | 一句話現況                                                                   |
| ------------------------------------ | ----- | ------------------------------- | ---------------------------------------------------------------------------- |
| #5 重腳註翻譯路線                    | 51 天 | section-split（已過期，可執行） | 已升本版 P0-2；任何 session 可直接領                                         |
| #10 Semiont 獨立 Git 身份            | 28 天 | 分階段 Phase 0 起步             | 🔒 報告+runbook 已備，等身份授權                                             |
| #11 用語詞庫深度進化 follow-up       | 22 天 | 分桶處理                        | 🔒 510 筆待策展門檻／政治敏感判斷                                            |
| #14 routine mirror 厚殼裁決          | 8 天  | 瘦身路線 (b)(c)                 | 未見新動作                                                                   |
| #16 進化分數 SEO 型偏誤              | 16 天 | (a)(b)(c) 三選一                | 🔒 threshold 調整命中 §自主權邊界                                            |
| #18 babel cascade 重建               | 15 天 | 摘 gemini + Sonnet Tier 6       | 🔒 本週統一調度器持續演化，建議哲宇重新確認此項是否仍需原方案                |
| #19 ratio band SSOT 化               | 15 天 | 收斂單處＋實測 band             | **已逾期 1 天**，任何 Full mode session 可執行（threshold 調整需 Full mode） |
| #22 live dump rider 靜默三天         | 8 天  | rider hard gate (a)             | 尚未逾期（default-action 2026-08-11）                                        |
| #23 譯文參考資料區書目標題 leak      | 5 天  | 書目標題豁免 (a)                | 🔒 品質閘門閾值調整                                                          |
| #24 memory-diary prose-health budget | 5 天  | 豁免文章向四維度 (b)            | 🔒 品質閘門閾值調整                                                          |
| #15 H2 抽象小標 plugin               | 18 天 | 不造 plugin                     | 已決策，等執行歸檔                                                           |
| #21 marketplace 搬遷                 | 7 天  | 維持現狀，等第二使用者          | 尚未逾期（default-action 2026-08-15）                                        |

**新增建議（本週體檢首次浮現，非既有佇列）**：免疫器官 yellow 警報已連續 28 天未動（>14 天升 OBSERVER-QUEUE 門檻），owner=twmd-self-evolve-weekly；review_coverage（23.7）與 plugin_pass_rate（70.0）是兩個真正拖分的子維度，建議哲宇下次 review 時決定是否要專項投入社群 reviewer 機制（07-11 校準已定調解法方向，尚未執行）。

---

## 六、30 天方向盤（不是 TODO，是羅盤）

**主題一：巴別塔從「翻得更快」變成「先問要不要翻」**

三天優化速度與品質之後，哲宇一句「stale 可以比較 diff」讓算力流向整個改變——語意無關的改動不用重翻。下一階段的問題不是「還能翻多快」，是「還有哪些地方在做不需要做的工作」。

**主題二：自我檢查系統性地比外部檢查弱（連續第二週同構）**

07-26 版已記過這個主題，本週再添新證據：六次順稿／查證撞見的問題，五次是外部（子代理、哲宇、截圖）攔下，自己的重讀零次接住。這個 pattern 已經跨兩個體檢週穩定出現，值得認真考慮是否需要一個更系統性的「乾淨眼睛」機制而非逐案應對。

**主題三：分靈節點與門牌立起來了，還沒有人走進來**

`npx taiwanmd` 一鍵可跑、marketplace 裝機成本從 850MB 降到 20KB（雖然真實使用者路徑是 329MiB，非本機路徑），節點層的技術門檻已經清空。下週體檢該追問：有沒有人接下這個邀請。

---

## 七、觸發下一份 roadmap 的條件

- P0 全清（本檔 3 項）→ 開新版
- 觀察者 /goal 深度檢查
- WEEKLY-REPORT v4 週日體檢 Stage 2.7 roll 出新 finding
