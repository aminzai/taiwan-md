---
title: 'TERMINOLOGY-TRENDS-PIPELINE'
description: '用語保存計劃月度趨勢觀察 — SC 需求 → 多切面搜索 → 缺口對照 → 高信心入庫（≤20 條/輪）→ 月度趨勢報告。7 stage + 6 hard gate。'
type: 'pipeline-canonical'
status: 'canonical'
current_version: 'v1.0'
last_updated: 2026-08-04
last_session: '2026-08-04-104614-支語研究（首輪 dogfood：30 agent 艦隊 559 搜索、49 詞條入庫）'
sister_docs:
  - 'EVOLVE-PIPELINE.md'
  - 'DATA-REFRESH-PIPELINE.md'
upstream_canonical:
  - '../semiont/MANIFESTO.md'
  - '../../reports/terminology-zhiyu-deep-research-2026-08-04.md'
---

# TERMINOLOGY-TRENDS-PIPELINE — 用語趨勢月度觀察 v1.0

> **第一性原理**：語言滲透是連續過程，詞庫是它的時間序列感測器。每月一輪「需求 → 搜索 →
> 對照 → 入庫 → 報告」，長期累積出台灣視角的語言滲透紀錄——這份資料沒有任何機構在做。
> 姿態站在查證與保存，不站在出征（MANIFESTO §13 立體地愛的語言層）。
>
> 誕生：2026-08-04 支語深度研究（哲宇 goal＋「未來可以定期做這件事情跟趨勢觀察」拍板月度）。
> 首輪完整範本：[reports/terminology-zhiyu-deep-research-2026-08-04.md](../../reports/terminology-zhiyu-deep-research-2026-08-04.md)。

---

## 🗺️ ASCII spine

```
╭──────────────────────────────────────────────────────────────────────╮
│   TERMINOLOGY-TRENDS — 月度 7 stage（每月 5 日，Opus）               │
│                                                                      │
│   Stage 0: BECOME（write mode）+ git pull                            │
│   Stage 1: DEMAND — SC 需求缺口（demand-rank 28d）                   │
│   Stage 2: SWEEP — 6-8 切面搜索（每切面 10-15 次）                   │
│   Stage 3: GAP — 對照詞庫（雙防線查重）🎬                            │
│   Stage 4: INGEST — 高信心入庫 ≤20 條 🎬（帶肉＋證據＋誠信標註）     │
│   Stage 5: REPORT — reports/terminology-trends/YYYY-MM.md            │
│   Stage 6: QUEUE — 超自主權項進 OBSERVER-QUEUE                       │
│   Stage 7: /twmd-finale（memory 必寫）                               │
╰──────────────────────────────────────────────────────────────────────╯
```

## 🚦 Hard Gate Inventory

| Gate               | Stage | 條件                                                                                       | 不過 = ?             |
| ------------------ | ----- | ------------------------------------------------------------------------------------------ | -------------------- |
| 雙防線查重         | 3     | 檔名 `test -f` ＋ 新詞 china/taiwan 值對全庫值掃描（含簡繁形）兩道都跑                     | 重複條目污染詞庫     |
| 入庫上限           | 4     | 每輪 ≤ 20 條新檔；超出的進 gap 清單留下輪                                                  | 無人審批的規模擴張   |
| 帶肉入庫           | 4     | 每條必有 etymology.origin 詞源敘事＋sources 證據 URL（GA4 實證：薄殼進不了長尾）           | AI Slop 式灌庫       |
| 誤判四型必查       | 4     | 日源／中國方言源／港澳源／台灣本有——四型逐條查，命中即在 notes 誠信標註，不武斷歸類        | 詞庫變黑名單失去公信 |
| QA 四件套          | 4     | 全庫 yaml parse＋`terminology-charcheck.js`＋重複掃＋`scripts/core/extract-china-terms.py` | 壞檔進 build         |
| 政治敏感／大批刪改 | 6     | 任何刪除、「是支語嗎」類判定徽章、大批重分類 → OBSERVER-QUEUE，不自主施作                  | §自主權邊界違反      |

## Stage 細則

**Stage 1 DEMAND**：`python3 scripts/tools/terminology-demand-rank.py --days 28`＋
`--state MISSING`。MISSING 清單是本輪入庫的第一優先（讀者已在搜）。

**Stage 2 SWEEP**：6-8 個切面、每切面 10-15 次搜索。固定四切面：Threads「支語」搜尋現場
（瀏覽器或 site: 搜索）／PTT 近月新串／中國年度流行語榜單動態（咬文嚼字、百度沸點）／
誤判鑑定案例（「X 是支語嗎」類討論）。機動切面依上輪報告的觀察挑（例：某類詞爆發、
某傳播通道變化）。可用 sub-agent fan-out；工具額度是共享池，dispatch 前留預算
（2026-08-04 首輪教訓：30 agent 撞 WebSearch session 上限，fallback WebFetch 直搜）。
搜到的「台灣怎麼說」寧可引台灣網友／媒體原話，不憑模型語感填（模型預設中國語料基準，
會把台灣名洗向中國名——REFLEXES #16 sovereignty 特化）。

**Stage 3 GAP**：新詞對照 `data/terminology/`（2,383+ 條）。雙防線 hard gate 見上表。
產出：本輪缺口清單（含證據 URL、切面交叉數、爭議標記）。

**Stage 4 INGEST**：從缺口挑高信心 ≤20 條入庫。判準：SC MISSING 交集 > 多切面交叉 >
單一來源高熱。schema 照現有 YAML（id／category／fork_type／display／etymology.origin／
notes／sources／added）。fork_type 務實判：網路時代功能詞 C、流行語感類 E，**不預設 B**
（73% B 無佐證是歷史債，不再擴大）。台灣本有對應詞（推坑／工具人／出包型）在 taiwan 欄
保留為資產。

**Stage 5 REPORT**：`reports/terminology-trends/YYYY-MM.md` 短報告（1-2 頁）：本月新進詞／
收編動態（哪些詞從抵抗走向接受）／誤判翻案／SC 需求變化。這是時間序列的一格，簡潔勝過全面。

**Stage 6 QUEUE**：超自主權項照 hard gate 表進 OBSERVER-QUEUE；缺口餘量 append 進
`reports/research/` 當月 gap 清單。

---

_v1.0 | 2026-08-04 — 誕生於支語深度研究 session，哲宇拍板月度。首輪（研究版，超出月度
規模）：559 次搜索／913 詞條／49 入庫，之後每輪縮小到 6-8 切面 ≤20 條的常規節奏。_
