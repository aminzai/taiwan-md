---
title: 'BABEL-VORTEX-LOOP'
description: '巴別塔渦流循環 canonical — 每次 schedule wakeup 必讀；固定 benchmark 面板 + 五動作 + 三重巡檢 + 自動進化硬條款 (v1.0)'
type: 'pipeline-canonical'
status: 'canonical'
current_version: 'v1.0'
last_updated: 2026-07-27
last_session: '2026-07-27-vortex-babel-4'
sister_docs:
  - 'SQUEEZE-MODELS-MAX-PIPELINE.md'
  - '../semiont/ROUTINE-PROMPT-CONTRACT.md'
---

# BABEL-VORTEX-LOOP — 巴別塔渦流循環 canonical v1.0

> **這份檔案是渦流的 SSOT**。每次 schedule wakeup 的第一動作是完整讀本檔再動工，
> wake prompt 本身只准是薄殼（見 §Prompt contract）。誕生：2026-07-27 哲宇 directive
> ——wake prompt 逐輪手寫導致報告 badge 每輪長不同、benchmark 不可比、資訊重複；
> 固定下來之後迴圈可交接給任何模型執行（Loop Engineering）。

## Prompt contract（薄殼鐵律）

ScheduleWakeup 的 prompt 固定為三部分，**禁止複寫本檔內容**：

```
巴別塔渦流循環：完整讀 docs/pipelines/BABEL-VORTEX-LOOP.md 後照它執行。
【本輪動態】<產線 PID 清單／未完成事項／上輪遺留，3 行內>
【觀察者臨時指示】<有才寫>
```

複寫 = 漂移的起點（本檔誕生前 wake prompt 每輪手寫，badge 定義漂了三天）。
動態區只放「這一輪才知道的事」，規則類內容一律改進本檔並 commit。

## 每輪五動作（順序固定）

1. **檢查**：三重巡檢（見下節）＋ CI ＋ babel-pulse
2. **進化**（硬條款，見 §自動進化）
3. **報告**：固定 benchmark 面板（見 §報告模板）
4. **修復**：本輪發現的問題當場修，修不完記入下輪動態區
5. **收尾**：快照 commit + push（衝突 SOP 見下）→ ScheduleWakeup（薄殼）

## 三重巡檢（存活 ≠ 生產，缺一不可）

1. **存活**：`ps` 四產線 PID ＋ `git status -sb` 確認在 main 分支
2. **生產**：各 worker 近 45 分實際 report.jsonl 記錄數——零記錄的 worker 去 curl 它的 endpoint（慢 worker 如 laguna 300s+/篇屬正常，先查再判）
3. **第二訊號源**：fleet registry 的機器狀態交叉比對（讀壞先重讀一次；自癒層在 fleetlib）

死掉的產線看 log 尾：`🛑 空轉自動收工` → 直接重啟；崩潰 → 查根因再重啟。
重啟指令在各 `/tmp/babel-*.log` 開頭；產線編組現況與原則見
[SQUEEZE §編組原則](SQUEEZE-MODELS-MAX-PIPELINE.md)。

## 報告模板（benchmark 固定，逐輪可比）

`show_widget` 每輪必出，結構與指標定義**固定**：

**固定面板（四格，定義不准改）**：
| 格 | 指標 | 資料來源 |
| --- | --- | --- |
| 1 | 總缺口 ＋ 24h Δ | babel-live.json `gap_total`；Δ 對照 progress jsonl 24h 前值 |
| 2 | 本小時完成篇數 | report.jsonl 近 60 分 ok 數 |
| 3 | 速率（篇/hr）＋通過率 | babel-live `rate_1h`；ok/(ok+fail) 近 60 分 |
| 4 | 產線 N/4 ＋ GPU 機器 N/3 在線 | ps 計數；fleet registry 非 offline 計數 |

**覆蓋率圈圈**（哲宇指定視覺）：十一語 donut grid，SVG circle
`stroke-dasharray` 按覆蓋率，圈內寫百分比、圈下寫語名＋fresh 數。

**單一明細列**：每語一行「bar ＋ inline 數字 f/s/m」，**不再放獨立表格**
（bar 與表格重複是本檔誕生的直接原因之一）。

**本輪重點**：唯一自由書寫區，2-4 條，含本輪進化發現。

## 自動進化（硬條款——這是渦流跟 cron 的差別）

每輪**至少執行一項**並在報告「本輪重點」記錄結果（含明確的「本輪無發現」）：

- **隔離樣本覆盤**：quarantine 新樣本抽掃，找新的誤判家族或模型行為
- **主動結構掃描**：問「最近修的病，成因結構還存在於哪裡」——grep 同構不 grep 症狀
- **實績檢查**：`babel-preflight.py` 弱適配清單有無新組合 → 有就切軌
- **記憶觀察**：fail-memo（repo 版控 `reports/babel/fail-memo.json`）條數與分層；fail≥4 難篇 ≥15 篇 → 開最強本地模型專攻軌

進化發現若改變規則 → **直接修本檔或 SQUEEZE 對應節並 commit**（版控就是漂移防護），
不寫在 wake prompt 動態區。

## 鐵律集（違反任一 = 本輪不合格）

1. 每回合結束前必 ScheduleWakeup（薄殼格式）——喚醒鏈是單點，斷一次監測就盲一輪
2. 報告含固定面板＋圈圈＋明細列，指標定義不變
3. git 紀律：精確路徑 add；並行 session 的檔案（含苯駢芘類寫作中檔案）不碰；
   merge 衝突：`fail-memo.json` 逐鍵取 max、`MEMORY.md`/`*.jsonl`/progress-log 用
   union（兩邊都留）、儀器產物 json 用 theirs；被未 commit 檔擋住 → 儀器產物可
   checkout 還原，knowledge 譯文一概不動
4. 詞彙：MANIFESTO §11.5（覆盤／追查／檢驗、隔離樣本；不用法醫詞）
5. 模型入池門檻與編組：[SQUEEZE 四節](SQUEEZE-MODELS-MAX-PIPELINE.md)
   （§模型×語言適配／§入池門檻／§排序原則／§編組原則）
6. context 深度稀釋 → 先 /twmd-memory 存檔再續；壓縮後醒來先讀最新
   memory 的 handoff

## 收官條件

十一語 stale=0 missing=0 且 QA gate 全綠 → 跑 /twmd-finale 宣告巴別塔 100%。

## Changelog（進化紀錄——新發現往這裡沉澱）

- v1.0（2026-07-27）：初版。收斂三天渦流的全部教訓：三重巡檢（存活≠生產五面貌）、
  優先序佇列＋repo 版控難篇記憶、模型×語言適配切軌、固定 benchmark 面板。
