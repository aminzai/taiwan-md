---
title: 'prose-health 儀器升級：分號 / 英文短句開場 / 長句 / 強加對比 + 偵測 vs 執行落差'
description: '哲宇 live review 高速公路.md 揪出四類中文寫作病 → prose-health 補三 dim + 一 Tier1 變體，全 corpus 853 篇校準；並揭露「破折號偵測早就 work 但 WARN-only 不擋 ship」的偵測-執行結構落差'
date: 2026-07-19
type: 'evolve-report'
status: 'shipped'
mode: 'Mode 4 目標驅動設計進化'
target_article: 'knowledge/Lifestyle/高速公路.md'
---

# prose-health 儀器升級（2026-07-19）

## 觸發

哲宇 live review [高速公路.md](../knowledge/Lifestyle/高速公路.md)（2026-07-18 寫的 depth 文，`lastHumanReview: false`），指出五類問題並要求「自我改良儀器 + 偵測到時清楚說明給未來 agent」。

## 五類問題 → 現況 → 處置

| 哲宇指出                              | 儀器現況                                            | 處置                                  |
| ------------------------------------- | --------------------------------------------------- | ------------------------------------- |
| ①「；」全形分號                       | **無偵測器**                                        | **新增 §8c**，scored                  |
| ②段落太長 / 語感不順 / 華麗辭藻湯     | 部分（塑膠/空洞詞），無長句偵測                     | **新增 §8d** run-on 長句，WARN-only   |
| ③英文式超短句開場「協議並沒有收尾。」 | **無偵測器**                                        | **新增 §8e**，WARN-only               |
| ④「——」破折號一堆                     | **早就有偵測器，且早就 fire**                       | 見下方「偵測 vs 執行落差」            |
| ⑤不是 X 是 Y 變體 + 不必要對比        | Tier1 抓到 3 處，但「…是兩件事 / 兩本帳」收束句沒抓 | **新增 Tier1 變體**「強加對比收束句」 |

## 最關鍵發現：偵測 vs 執行是兩件事

哲宇「懷疑是沒有完整跑儀器」——**跑了，而且 fail 了**。跑 `article-health.py 高速公路.md`：

```
✅ prose-health  hard=0 warn=17
   warn: prose-health score: 5 (≤ 3 = pass) — 未人工審核; 塑膠句1個; 破折號17個
Summary: passed=False (fail_on=warn)
```

破折號 17 處（+3）早就被抓到、score 5 > 3 早就 fail。文章照樣 ship 的真正原因：

- **pre-commit 與 ci-deploy 都是 `fail_on = "hard"`**（`article-health.config.toml`）。prose-health 全部是 WARN，所以**破折號 / 塑膠 / 分號永遠不擋 commit 也不擋 deploy**。
- prose-health 的 score budget 只在 `rewrite-stage-3` profile（`fail_on = "score-budget"`）咬——也就是 agent 走 REWRITE-PIPELINE 主動寫 / polish 的時候。
- 這篇 `lastHumanReview: false` 是批量寫的，沒有走完整 rewrite-stage-3 editorial 閘就落地。

**結論**：破折號不是「偵測缺口」，是「執行缺口」。偵測器沒問題，問題在「WARN 級 + 批量文章沒過 editorial 閘」。這個落差本身值得哲宇決策（見下方建議）。

## 新增偵測器 + 全 corpus 校準（853 篇）

REFLEXES #24「儀器哭狼」守則：新偵測器一定要對全 corpus 量假陽性率。

| 偵測器             | 初版                 | 校準後                                                  | 校準動作                                                                                                                                                              |
| ------------------ | -------------------- | ------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| §8c 分號           | —                    | 42% 命中                                                | scored；42% 是 AI 語料系統性水印（真陽性），且只在 rewrite-stage-3 咬，不會回頭 fail 850 篇 corpus                                                                    |
| §8d run-on 長句    | 55字/7停頓 → 37%     | 62字/8停頓 → 23%                                        | 收緊門檻 + **排除腳註行 / blockquote**（dogfood 揭 4 處腳註 FP）；WARN-only                                                                                           |
| §8e 英文短句開場   | ≤10/≥15/2× → **58%** | ≤8字 + ≥28字 + ≥3.5× + **限 。結尾 + 開場無數字** → 29% | 58% 是哭狼。三步收緊：①設問（？）是中文修辭非病 → 限平述句；②含數字是具體場景句（「1978 年通車了。」）→ 豁免；③抽樣確認剩下 29% 多為真陽性（AI 語料真的愛甩短句開場） |
| Tier1 強加對比收束 | —                    | 0.6%                                                    | 高精度，「根本是兩件事 / 兩本帳 / 不同的語言」，實指「這篇要做兩件事」不誤報                                                                                          |

高速公路.md 升級後：score **5 → 7**（+2 分號），5 類全中，含哲宇 anti-example「協議並沒有收尾。」逐字命中。0 crash / 867 檔，38 test（30 舊 + 8 新）全過。

## 執行缺口：哲宇選 選項3（升 hard）→ 責任式分階段實作

哲宇選最強的選項 3（破折號/分號升 hard）。但升 hard 前先量 blast radius：

| 惡性門檻             | 會 hard-fail 的 legacy 篇數 |
| -------------------- | --------------------------- |
| 破折號 > 15          | 68 篇                       |
| 全形分號 > 12        | 89 篇                       |
| 聯集（> 15 或 > 12） | **144 篇**                  |

最惡：蘇打綠 72 破折號、認知作戰 29 分號 + 24 破折號、醫療與健保 46 分號。**直接把 ci-deploy 全站升 hard 會 brick 每一次 push**（144 篇立刻紅），而這 144 篇的清理是判斷密集的改寫（拆句要讀懂語意），不是機械 auto-fix。

**責任式實作（本 session 已 ship，425d41125）**：破折號 > 15 / 分號 > 12 只在 **pre-commit profile**（`--staged`，只查你 commit 的檔）升 HARD；ci-deploy 全站掃描刻意不設 → legacy 144 維持 WARN、**不 brick**。

- 效果：你**新寫或編輯**的檔超量就擋 commit（觸檔即清 touch-it-fix-it）→ recurrence 立刻止血，且觸碰 legacy 就順手清。
- 方向安全性：pre-commit 比 ci-deploy 嚴（過嚴閘必過鬆閘），非 2026-05-11 那種 pass-local-fail-CI 反向 asymmetry。
- 驗證：認知作戰.md ci-deploy=hard0（過）/ pre-commit=hard2（擋）；全站 ci-deploy sweep passed=True。

**剩下的：全站升 hard 需要 legacy 清理 campaign**。144 篇批次清（分號拆句、破折號減半），清完再把同組 override 加進 ci-deploy → 全站升 hard，達成完整選項 3。這步是 >50 檔判斷密集改寫，屬 §自主權邊界，要哲宇點頭 scope／節奏（一次全清 vs 分批 vs 只清 featured 旗艦文）才啟動。

高速公路.md 本篇已個別 polish（見 git log）。

## 給未來 agent 的一句話

看到 prose-health `passed=False` 不代表「儀器沒跑」——多半是**跑了、fail 了、但因為是 WARN 級而沒擋下 ship**。要判斷一篇有沒有過品質閘，看它走的是哪個 profile：`fail_on=hard`（commit/push/deploy，只擋 hard）還是 `fail_on=score-budget`（rewrite-stage-3，WARN 也計分）。
