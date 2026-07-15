---
title: 'EDITORIAL-ROOM'
description: '編輯室對抗 canonical — 投影後／正文後乾淨 context 分席審稿；主編裁決；結構外部尺'
type: 'editorial-canonical'
status: 'canonical'
current_version: 'v1.0'
last_updated: 2026-07-15
last_session: '2026-07-15-112237-manual'
sister_docs:
  - 'PROJECTION.md'
  - 'EDITORIAL.md'
  - '../pipelines/REWRITE-PIPELINE.md'
  - '../pipelines/EDITORIAL-ROOM-PROMPTS.md'
upstream_canonical:
  - 'PROJECTION.md'
  - '../pipelines/REWRITE-PIPELINE.md'
---

# EDITORIAL-ROOM — 編輯室對抗

> 投影藍圖與正文成品，各過一間**乾淨 context 編輯室**：角色分席、任務互斥、主編裁決。  
> 同一顆腦不准又寫又審。subagent claim 是線索（[REFLEXES #31](../semiont/REFLEXES.md)）。  
> 設計背景：[reports/editorial-room-adversarial-design-2026-07-15.md](../../reports/editorial-room-adversarial-design-2026-07-15.md)

---

## 一句話

**把「總編輯看完整桌材料、質疑、要改寫」變成可重跑的 subagent 結構**——不是社群彈幕 UI，不是假留言牆。

---

## 兩道關

```text
研究 report 合成
    ↓
Step 2.0 投影藍圖（orchestrator 寫）
    ↓
⭐ Step 2.0-R 投影編輯室  ← 本檔 §投影室
    ↓ pass
fresh writer 寫正文
    ↓
⭐ Step 2.5-R 正文結構編輯室（包 A）+ Step 3.6 成品總驗（包 B）
    ↓
主編合併 → ship
```

| 關         | REWRITE 錨點 | 輸入                              | 產物                                                      |
| ---------- | ------------ | --------------------------------- | --------------------------------------------------------- |
| 投影室     | Step 2.0-R   | research report + projection 藍圖 | `reports/editorial-room/{slug}-projection-review.md`      |
| 正文結構室 | Step 2.5-R   | staging/正文 + 同一投影藍圖       | `reports/editorial-room/{slug}-prose-structure-review.md` |
| 正文事實室 | Step 3.6     | 成品 + footnotes + report         | research §audit + 既有 3.6 流程                           |

---

## 材料桌（足跡契約）

| 允許                                        | 禁止                             |
| ------------------------------------------- | -------------------------------- |
| 研究 report、一手 URL、投影藍圖、正文 draft | 憑記憶發明「讀者留言／社群情緒」 |
| 新聞／部落格／論文／podcast（經 research）  | FB／IG 主爬當預設材料            |
| 標 single-source hedge 的口述               | 腦補現場補洞                     |

足跡不夠 → 席位 **block**，指令「回 Stage 1 補研」或「砍該 beat」，不准寫手腦補。

---

## 席位（1 agent = 1 角色，平行）

### 投影室（depth HARD；Thin = 結構 + 炎上 + 主編）

| 席                       | 任務                                         | verdict               |
| ------------------------ | -------------------------------------------- | --------------------- |
| **結構主編**             | 論點非摘要、骨架 shuffle、全局功能、面向巡禮 | pass / revise / block |
| **減法主編**（可併結構） | 減法誠實、密度、CV 感                        | pass / revise / block |
| **炎上／倫理**           | spine × 立體地愛 × 政治中立；contrarian 炎上 | pass / revise / block |
| **主編**                 | 永遠主 session：收件、≤7 必改、裁決歧見      | 合成最終報告          |

### 正文結構室（包 A）

| 席           | 任務                                             |
| ------------ | ------------------------------------------------ |
| **結構主編** | 正文是否**執行**藍圖全局功能？有無退回面向巡禮？ |
| **論點兌現** | 論點是否在中段被證明／複雜化，而非頭尾各喊一次？ |

### 正文事實室（包 B = 既有 3.6）

原子重驗 / 順稿 / 視覺同步——不重寫規則，pointer 到 [REWRITE Step 3.6](../pipelines/REWRITE-PIPELINE.md)。

---

## 報告模板（HARD schema）

```markdown
---
slug: { slug }
room: projection | prose-structure
date: YYYY-MM-DD
seats: [structure, ethics, ...]
overall: pass | revise | block
rounds: 1
---

# 編輯室報告 — {room} — {slug}

## 各席

### {席名}

- verdict: pass | revise | block
- findings: （子彈，可執行）
- evidence: （指向藍圖 § 或 正文段落）

## 必改清單（≤ 7）

1. ...

## 建議不擋 ship（≤ 5）

1. ...

## 歧見與主編裁決

...

## 回修指令（給 orchestrator）

- [ ] 改投影 §…
- [ ] 回 Stage 1 補…
- [ ] 正文改 section…
```

儀器：`python3 scripts/tools/editorial-room-health.py reports/editorial-room/{file}.md`

---

## Gate

| overall    | 動作                                           |
| ---------- | ---------------------------------------------- |
| **block**  | 必回修；投影室最多 2 輪全席，第 3 輪升級觀察者 |
| **revise** | 主編勾選採納；修後可只重跑曾 raise 的席        |
| **pass**   | 准下一 stage                                   |

**depth EVOLVE / Fresh / A 級**：投影室 HARD。  
**standard / 短修**：Thin 或 skip。  
**Micro**：skip。

---

## Context 隔離（每席 prompt 鐵律）

見 [EDITORIAL-ROOM-PROMPTS.md](../pipelines/EDITORIAL-ROOM-PROMPTS.md)。摘要：

1. 你沒有寫過這份藍圖／正文
2. 只讀附件清單內的檔
3. 不准讀 knowledge 舊文（除非 brief 明示 EVOLVE 對照）
4. 不准重寫全文；只列必改
5. 輸出嚴格用報告模板

---

## 與其他機制邊界

| 機制              | 編輯室關係                    |
| ----------------- | ----------------------------- |
| PROJECTION 5 題   | 作者自檢；編輯室 = **外部尺** |
| persona gap-audit | 讀者缺口；不取代結構主編      |
| 3.6 verifier      | 正文事實包 B                  |
| FACTCHECK         | 事後／高流量；不取代          |

---

_v1.0 | 2026-07-15 — dogfood Shopping Design 投影／正文結構室。_
