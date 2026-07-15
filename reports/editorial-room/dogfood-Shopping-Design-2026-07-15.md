---
title: 編輯室對抗 dogfood — Shopping Design
date: 2026-07-15
status: complete
---

# Dogfood 總結 — 編輯室 v1.0 × Shopping Design

## 跑了什麼

| 關                    | 席                            | 結果                |
| --------------------- | ----------------------------- | ------------------- |
| 投影室 Step 2.0-R     | 結構 / 減法 / 炎上 + 主編     | **overall: revise** |
| 正文結構室 Step 2.5-R | 結構 / 論點兌現 + 主編        | **overall: pass**   |
| 儀器                  | `editorial-room-health.py` ×2 | 見下方              |

## 關鍵發現（系統有效性）

1. **乾淨 context 抓到作者自檢不易抓的第二層**
   - 減法席：§4 有五條仍 **revise**（履歷 CV、競品、年表未砍）
   - 炎上席：非 block，但抓到「證明鏈偏熱／掀開語感」— 正是 #77 邊界微調

2. **正文室證明「執行藍圖」可驗**
   - 已 ship 文五 H2 對齊 after 藍圖 → **pass**
   - 與投影 §0 before 診斷對照：病在歷史版本；現行正文已壓合機制放大一步

3. **規格債 vs 成品債分流**
   - 投影仍 revise（寫手規格要補刀）
   - 正文 pass（成品結構 OK）
   - 主編未把兩者混成同一個 overall

4. **假彈幕未出現**
   - 全席只引用 report／藍圖／正文；無發明社群留言

## 儀器

```bash
python3 scripts/tools/editorial-room-health.py reports/editorial-room/Shopping-Design-projection-review.md
python3 scripts/tools/editorial-room-health.py reports/editorial-room/Shopping-Design-prose-structure-review.md
```

## 落地檔案

| 檔                                                       | 角色             |
| -------------------------------------------------------- | ---------------- |
| `docs/editorial/EDITORIAL-ROOM.md`                       | 方法論 canonical |
| `docs/pipelines/EDITORIAL-ROOM-PROMPTS.md`               | 分席 prompt      |
| `scripts/tools/editorial-room-health.py`                 | schema gate      |
| REWRITE Step 2.0-R / 2.5-R                               | 流程插入         |
| `*-projection-review.md` / `*-prose-structure-review.md` | 本輪產物         |

## 下一步（非本 dogfood 範圍）

- [ ] 投影藍圖依必改 1–6 回修（規格債）
- [ ] 下一篇 **綠地** depth EVOLVE 全程 2.0 → 2.0-R → write → 2.5-R → 3.6
- [ ] 可選：負例測試（故意面向巡禮藍圖 → 結構席應 block）

---

_session 2026-07-15 · 五席 subagent id 見各 review 檔_
