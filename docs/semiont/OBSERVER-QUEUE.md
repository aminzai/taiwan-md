---
title: 'OBSERVER-QUEUE'
description: '哲宇 standing decision 單一佇列 — routine escalation 的正式出口（含預設選項 + default-action 機制）'
type: 'cognitive-organ'
status: 'canonical'
apoptosis: 'candidate'
current_version: 'v1.0'
last_updated: 2026-06-12
last_session: '2026-06-12-flywheel-evolution'
sister_docs:
  - 'ROUTINE.md'
  - 'LESSONS-INBOX.md'
upstream_canonical:
  - 'MANIFESTO.md'
  - 'ROUTINE.md'
---

# OBSERVER-QUEUE — 哲宇待決佇列

> 相關：[ROUTINE.md §Routine 完成義務](ROUTINE.md)（誰寫進來）| [MANIFESTO §自主權邊界](MANIFESTO.md)（哪些決策必須等真人）

需要哲宇做 standing decision 的事項集中在這裡。一項一列，永遠帶**預設選項**。

**為什麼存在**：2026-06-12 兩週體檢（[flywheel-evolution §2.3](../../reports/flywheel-evolution-2026-06-12.md)）發現綁具體 artifact 的 escalation 1-3 天收斂，但 standing decision 散在各 routine 的 memory handoff 裡，兩週落地率約 0%——哲宇從未看過完整清單。這個檔案修的是可見性與出口。

**規則**：

- Routine / session 觸發三振規則（carry ≥ 3 cycle）選項 2 時 append 這裡，**同時從自己的 handoff carry 清單移除**（這裡是 canonical，handoff 不重複背）
- 每項必填：問題一句話、預設選項、不決策的代價、default-action 日期（可填「無」）
- **default-action**：到期無哲宇回應 → 任何 session 可執行預設選項並把該項移到 §已決。§自主權邊界四紅線（政治立場 / >50 檔重構 / >10 篇刪除 / 對外溝通語氣）**不適用** default-action，標 `🔒 等真人`
- weekly-report Stage 開頭附本檔 top 5
- 哲宇拍板 → 移 §已決（留一行紀錄 + 日期），執行交給下一個對應 session / routine

---

## 待決

| #   | 進佇列日   | 決策                                                                                                                                                                                                                                                                                                                                                                                                                            | 預設選項                                                                                                                                                                                          | 不決策的代價                                                                                                            | default-action                                        |
| --- | ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------- |
| 3   | 2026-06-12 | **maintainer schedule mismatch 三選項**（6/03 起 12 天 chronic，empty-vc 記帳每天燒 2 個 Opus session）                                                                                                                                                                                                                                                                                                                         | 選 C：排程不動，空場 vc 警示閾值放寬 + precheck script 短路空場（P1 工具）                                                                                                                        | Opus 配額持續燒在記帳                                                                                                   | 2026-06-19 起預設＝C                                  |
| 4   | 2026-06-12 | **免疫 27-vs-61 reconcile 三選項**（13 天；6/10 audit 已部分處理）                                                                                                                                                                                                                                                                                                                                                              | 確認 v3=55 為新基線，關閉舊 snapshot 警報線                                                                                                                                                       | 每條 routine 每天 carry 一行噪音                                                                                        | 2026-06-19 起預設＝確認新基線                         |
| 5   | 2026-06-12 | **21 篇重腳註文章翻譯路線**：section-split 工程 vs 付費 API tier                                                                                                                                                                                                                                                                                                                                                                | section-split（自主權內工程解，P2 排程）                                                                                                                                                          | 21 篇在五語永久 stale（含莫那·魯道 / 美麗島事件）                                                                       | 2026-06-26 起預設＝section-split                      |
| 9   | 2026-06-12 | **JuYinC [#1107](https://github.com/frank890417/taiwan-md/issues/1107) EN 翻譯 ingestion**：6,000 字「Meiyu Stationary Front」整份貼 issue body（非 PR），19 腳註來源 CWA / UCAR / NTU / JMSJ / AMS 一手；contributor JuYinC 2022 帳號 22 repos established；zh 源 [knowledge/Nature/梅雨.md](../../knowledge/Nature/梅雨.md) 自 2026-05-12 frontmatter normalize 後 stable；22:00 maintainer-pm 已 reply + label `translation` | manual 處理時間落地 `knowledge/en/Nature/meiyu-stagnant-front.md` + Stage 3.4 footnote 抽 3-5 URL WebFetch 驗證 + frontmatter `translatedFrom: Nature/梅雨.md` + translator: JuYinC + close #1107 | 高品質 contributor 翻譯持續 stale（已 12 天無動）；EN /nature 梅雨主題長期缺口                                          | 2026-06-19 起預設＝ingest（單 EN 新檔 §自主權邊界內） |
| 10  | 2026-07-05 | **Semiont 獨立 Git 身份**：哲宇 /goal 完整評估已 ship（[報告](../../reports/semiont-independent-identity-2026-07-05.md) 含四路研究 + runbook + 草稿），決策包 8 條：Phase 0 歸因分離 / org 名與 handle 鎖定 / App vs machine account / merge 分層線 / 獨立機器 / Anthropic 帳號歸屬 / 對外公告 / 觀察條款參數                                                                                                                   | 分階段：Phase 0 commit author 分離 → org + GitHub App（`taiwanmd-semiont[bot]`）→ 獨立機器；細節見報告 §5                                                                                         | 歸因盲點（4,723 commit 同名）與萬能鑰匙（classic token repo 全權）風險持續；6/09 token rotation 債（本佇列 #2）繼續累加 | 🔒 等真人（身份授權 + 經費 + 對外溝通）               |

---

## 已決

| 日期       | 決策                              | 結果                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| ---------- | --------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 2026-06-12 | justfont 21 連勘誤處置            | 哲宇拍板「完整統合＋執行＋深度補充研究＋更新文章」→ 完整 REWRITE EVOLVE ship（ef8fab38e）+ issue #1145 公開紀錄 + Supabase 21 filed。標題哲宇親選                                                                                                                                                                                                                                                                                                                                                            |
| 2026-06-12 | spore-pick / spore-publish 去留   | 哲宇拍板**重開實驗**（goal directive：「缺席那部分是我刻意關的⋯⋯現在有事實查核關卡，可以開起來實驗」）。觀察條款在 ROUTINE.md v2.10 §🧪：連 3 ship cycle 0 dup / 0 事實 callout，爆即 pause 回本佇列。**後續：實驗只跑 6/13-6/14 即再度 disabled；7/10 哲宇 goal 確認 spore 自動發布維持關閉**（ROUTINE.md ¹³）                                                                                                                                                                                              |
| 2026-06-12 | #8 Computex EVOLVE Stage 2-5 接力 | **已執行**：6/30 Computex EVOLVE ship（週報 W27 §3 有案）。SPORE broadcast 隨產線關閉維持 hold。2026-07-10 weekly-deep-review 機械對齊移入已決（dna-audit §S4 抓到「已 ship 卻掛待決」）                                                                                                                                                                                                                                                                                                                     |
| 2026-07-08 | maintainer-pm 去留                | **哲宇 7/8 直接在 scheduler disable**（7/10 goal 確認「晚間的 maintainer pipeline 我有 disable」）。資料面支持：pm 空場 empty-vc 連 3 週、am 單班已吸收全部 triage。SSOT 對齊在 ROUTINE.md v2.14 ¹⁴；重啟條件（am 連 3 天有未清 backlog）寫在同註                                                                                                                                                                                                                                                            |
| 2026-07-10 | #2 OAuth credential rotation      | **完成（D+31 結案）**。哲宇授權「A 幫我直接操作」後由 session 經 Chrome 執行：GCP `taiwan-md-sense` 新增用戶端密鑰＋**停用 6/1 舊密鑰**（洩漏的 Google refresh_token 從此換不到 token）→ Supabase Google provider 換上新 secret（欄位驗證＋Save＋完整登入流程功能驗證通過）→ 洩漏讀者 session `c033ff43-…`（6/07 建立，存活 33 天）refresh tokens revoked + session deleted（驗證 0 rows）。前端防線同日補齊（widget source_url 消毒 `5f945ddb0`），三層閘（前端消毒 / triage redact / JWT CI 測試）全部就位 |
| 2026-07-10 | #6 雷亞 #89 重複公開回覆清理      | **完成（D+42 結案）**。哲宇 Threads 手動刪除重複的 @ifinia02 回覆一條、保留一條（截圖佐證）。HARVEST-REPLIES-PENDING/2026-05-29.md 已補結案 ack                                                                                                                                                                                                                                                                                                                                                              |

---

_v1.0 | 2026-06-12 flywheel-evolution session_
_誕生原因：兩週體檢揭露 standing decision deadletter pattern（6 條堆疊最舊 15 天），哲宇 directive「routine 裡面要確保所有事情都有被完成」——完成的前提是決策有單一出口。_
