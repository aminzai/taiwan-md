---
title: 'idlccp1984 PR batch × 儀器進化：小丑魚原則下的 warn+lint+auto-heal'
type: research-implementation
status: shipped
date: 2026-07-23
session: 2026-07-23-214453-manual
observer: 哲宇
scope: '9 open PRs by idlccp1984 + article-health instrument evolution'
---

# idlccp1984 PR batch × 儀器進化（2026-07-23）

> **一句話**：idlccp1984 是持續貢獻的小丑魚；這批 9 個 PR 的內容多半可讀、可收，但格式層（frontmatter / 腳註 / 關聯連結）反覆卡在「純 warn 或純 request-changes」。本次把儀器從 **純 warn** 升到 **warn + lint + auto-heal + advanced-review-required**，然後以小丑魚原則代修並合併。

---

## 1. 觀察者 directive

1. `/twmd-become` Full mode 甦醒
2. 審 **idlccp1984 全部 open PR**
3. **小丑魚原則**：他不太熟 GitHub 後續修改與格式；能修就幫修
4. 觀察可進化儀器：關聯文是否存在、最大 match、子分類、腳註格式
5. 進化原則：**warn + lint + auto-heal + advanced review required > 純 warn**
6. 先寫深度研究報告與實作計劃，再完整執行
7. `/twmd-finale`

---

## 2. PR 盤點（ground truth）

| PR    | 檔案                          | 類型   | CI                        | 內容級判斷        | 主要阻塞（格式）                                                      |
| ----- | ----------------------------- | ------ | ------------------------- | ----------------- | --------------------------------------------------------------------- |
| #1236 | `Culture/台灣迷因.md`         | update | CLEAN                     | B+ 重寫，有策展角 | 缺 featured；`[^n]` ref 無 def；延伸閱讀 percent-encoded              |
| #1233 | `Economy/萊爾富.md`           | new    | CLEAN                     | A- 品牌敘事好     | 缺 featured/subcategory；GitHub 式腳註                                |
| #1232 | `Economy/NET.md`              | new    | **frontmatter-gate FAIL** | A- 企業列傳       | 缺 featured（hard）；GH 腳註；深度 < 4500 字（後續 polish）           |
| #1231 | `Culture/農曆七月.md`         | new    | CLEAN                     | B+ 節慶           | 缺 featured/subcategory；GH 腳註                                      |
| #1230 | `Culture/中元節.md`           | new    | CLEAN                     | B 節慶            | 同上                                                                  |
| #1229 | `Economy/紡織業.md`           | new    | CLEAN                     | A- 產業敘事       | **frontmatter 包在 ` ```yaml ` code fence**；GH 腳註                  |
| #1227 | `Society/當兵.md`             | new    | CLEAN                     | A- 社會制度       | 缺 featured/subcategory；GH 腳註                                      |
| #1226 | `History/牡丹社事件.md`       | new    | CLEAN                     | A- 史觀清楚       | 缺 featured/subcategory；APA/編號腳註                                 |
| #1225 | `History/台灣與北朝鮮關係.md` | new    | CLEAN                     | A 題材稀缺        | 缺 subcategory/featured；GH 腳註；先前 comment 已提 source 錯配需抽樣 |

**紅旗**：0/10 命中（無 robots / 外部 JS / workflow / featured:true 自設成功 / Manus author / placeholder 模板殘留）。  
**紅旗 7 修補式**：部分 `author` 正確為 Contributors；#1229 是 YAML fence 導致 frontmatter 整段失效（等價於缺全部 required fields）。

**三級判斷（Close hard gate）**：

| Polish 預估                     | PR                                      | Default action                                                                                    |
| ------------------------------- | --------------------------------------- | ------------------------------------------------------------------------------------------------- |
| < 10 min 格式                   | 1236,1233,1232,1231,1230,1229,1227,1226 | **merge + heal**                                                                                  |
| 10–30 min（source 抽樣 + 腳註） | 1225                                    | **merge + heal + advanced review flag**（source 錯配先前已 comment；本輪 heal 格式後抽樣 ≥3 URL） |

**不 close、不 request-changes 要求作者再推**——這就是小丑魚原則在本 batch 的操作化。

---

## 3. 儀器現況 vs 缺口（根因）

既有 article-health 插件能力：

| 儀器                     | 現況                                         | 對本 batch 的實際表現                                                  |
| ------------------------ | -------------------------------------------- | ---------------------------------------------------------------------- |
| `frontmatter-format`     | HARD 缺欄；`--fix` 可補 featured/author/date | **不會**推 subcategory 內容；不會拆 ` ```yaml ` fence                  |
| `frontmatter-title`      | HARD 缺 subcategory                          | **無 fix()** → 永遠卡作者                                              |
| `footnote-format`        | HARD + 安全 auto-fix（缺 desc 補上）         | **不認** GitHub `1. [T](U) [↩]` / `[1](#user-content-fn-1)` / APA 列表 |
| `link-target` Phase1     | HARD + auto-fix 小寫 category                | OK                                                                     |
| `link-target` Phase2     | WARN 存在性；**無 auto-fix**；**無 unquote** | #1236 四條 percent-encoded 連結**全部存在**卻被報不存在                |
| `wikilink-target`        | HARD + fix 轉純文字                          | 本 batch 幾乎無 `[[wikilink]]`                                         |
| `assign-subcategory.cjs` | 離線 keyword batch                           | 不進 pre-commit；keyword 表偏舊（Economy 只 match「台灣企業」等）      |

### 3.1 根因模式（為什麼「純 warn」不夠）

1. **Contributor 不熟 GitHub 迭代**  
   request-changes 的 marginal cost 落在小丑魚身上（學 YAML、學 `[^n]:`、學 subcategory taxonomy）。對站體則是：同一 pattern 在 9 個 PR 上重播。

2. **儀器偵測了但不會治**  
   Phase2 existence、subcategory 缺欄、GH 腳註 = 三個「會叫不會修」的洞。Maintainer 每次重新發明 regex。

3. **false-negative 比 false-positive 更糟**  
   percent-encoded 連結是真的活連結；儀器報 broken → 誤導 review 成本。**先 unquote 再判存在**是機械正確性，不是品味。

4. **「最大 match 是什麼」沒被 surface**  
   就算不能 auto-heal，warn message 應帶 top-1/top-3 candidate + ratio，讓人/agent 10 秒裁決。

---

## 4. 設計原則：warn + lint + auto-heal + advanced-review-required

對齊既有 staged promotion pattern（chronicle-lead / word-count / image-health）：

```
偵測 (lint)
  ├─ 可機械確定（unquote / 缺 featured / GH→canonical 腳註骨架）
  │     → auto-heal（--fix 預設開啟 safe transforms）
  ├─ 高信心模糊匹配（ratio ≥ 0.90 且唯一 top）
  │     → auto-heal + 在 violation 留 INFO 審計 trail
  ├─ 中信心（0.70–0.90）或一對多
  │     → WARN + 建議清單（max match + alternatives）
  │     → 標記 advanced-review-required（不擋 pre-commit）
  └─ 低信心 / 品味 / 事實主張
        → advanced-review-required only（人審）
```

**鐵律**：

- Auto-heal **只做可逆或可 diff 審計**的變換
- 任何 auto-heal 必須在 dry-run 可預覽
- 事實主張、source 錯配、政治敏感 → **永不 auto-heal claim 本體**，只修載體格式
- pre-commit 仍 `fail_on=hard`；auto-heal 跑在 check 之前（或 `--fix` 一輪再 check）

---

## 5. 實作計劃（本 session 完整執行）

### Wave A — 儀器（先造橋）

| #   | 改動                                                                                                                                                               | 檔案                                                            | 驗收                      |
| --- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------- | ------------------------- |
| A1  | link-target：`urllib.parse.unquote` 後再存在性檢查；percent-encoded → 解碼後存在則 auto-heal 成解碼 path                                                           | `checks/link_target.py`                                         | #1236 四連結 dry-run 全綠 |
| A2  | link-target Phase2：`difflib.get_close_matches` top-3；message 帶 max match + ratio；ratio≥0.90 唯一 → auto-heal                                                   | 同上                                                            | 人造 broken slug 有建議   |
| A3  | subcategory auto-heal：從 `docs/taxonomy/SUBCATEGORY.md` + title/tags/filename/keywords 推 top match；缺欄 HARD 但 `--fix` 寫入高信心值；低信心 WARN + suggestions | `checks/frontmatter_format.py` + 小 helper `taxonomy_subcat.py` | 本 batch 8 檔可自動補     |
| A4  | GitHub / 編號列表腳註 → canonical：`[n](#user-content-fn-n)` → `[^n]`；文末 `1. [T](U) — d` / APA → `[^n]: [T](U) — d`；拆 ` ```yaml ` fence                       | `footnote-format-fix.py` + `checks/footnote_format.py`          | 9 檔 dry-run 可轉         |
| A5  | `article-health --fix` 跑完印 **Advanced review required** 摘要（未 auto-heal 的 WARN/中信心）                                                                     | `article-health.py`                                             | CLI 可見分桶              |

### Wave B — PR act（小丑魚）

對每個 PR：

1. 取 head 檔 → 工作樹
2. `python3 scripts/tools/article-health.py --fix <file>` + footnote healer
3. 補延伸閱讀（若完全沒有）：用站內既有高相關文（機械 match + 人工確認一句 desc）
4. 抽樣 footnote URL（≥3 / 含 #1225 已知敏感 claim）
5. `article-health` hard=0 才 commit
6. commit 帶 `Co-authored-by: idlccp1984 <idlccp64@gmail.com>`
7. `gh pr close N --comment` 感謝 + 說明已代修 merge（或 native merge 若仍 open 且 clean）

**整合策略**：  
因多檔需 local heal 後才能過 main deploy hard plugin，採 **file-checkout → heal → main commit → close PR（保留 Co-authored-by）**；若某 PR 已可 clean merge 且 heal 可 post-merge 完成，則 native merge + follow-up heal 亦可。本 batch 以「先 heal 再進 main」為主，避免 main 被 GH 腳註 transient 弄紅。

### Wave C — 收官

- memory + diary + evolve（`/twmd-finale`）
- LESSONS-INBOX 一條：contributor 格式債 = 儀器債
- handoff：#1225 advanced source review residual（若有）

---

## 6. Subcategory 本 batch 裁決表（人審鎖定，供 auto-heal 訓練）

| 文章             | subcategory | 理由                                          |
| ---------------- | ----------- | --------------------------------------------- |
| 台灣迷因         | 網路文化    | 既有 + taxonomy                               |
| 萊爾富           | 企業列傳    | 品牌/公司敘事（非 Lifestyle 便利商店總論）    |
| NET              | 企業列傳    | 已標                                          |
| 紡織業           | 經濟發展    | 產業轉型敘事；循環經濟側面可後續改 能源與永續 |
| 農曆七月         | 節慶與禮俗  | 對齊端午節                                    |
| 中元節           | 節慶與禮俗  | 同上                                          |
| 當兵             | 社會制度    | 役政制度；對齊颱風假類「制度日常」            |
| 牡丹社事件       | 殖民與帝國  | 對齊羅發號 / 清治                             |
| 台灣與北朝鮮關係 | 民主與治理  | 對外關係史；對齊退出聯合國                    |

---

## 7. 風險與邊界

| 風險                         | 處置                                                                                              |
| ---------------------------- | ------------------------------------------------------------------------------------------------- |
| Auto-heal 選錯 subcategory   | 高信心才寫；否則 WARN + advanced review；taxonomy 表可人工 override                               |
| 腳註轉換丟 title             | 只轉可 parse 的 markdown link 行；APA 走既有 footnote-format-fix 路徑；失敗保留原文 + HARD        |
| #1225 source 錯配            | 格式 heal 後仍標 advanced-review；必要時刪/hedge 明顯錯配 claim                                   |
| 篇幅 < 4500                  | contributor 新文不因 word-count HARD 擋 merge（pre-commit/ci 預設 WARN）；rewrite-stage-4 才 HARD |
| 與 main 上舊「台灣迷因」衝突 | #1236 是有意重寫；以 PR 版為主，保留既有 frontmatter 健康欄位                                     |

---

## 8. 成功指標

- [ ] 9/9 PR 關閉或 MERGED，contributor 收到中文感謝
- [ ] 9 檔進 main 後 `article-health --profile=pre-commit` hard=0
- [ ] link-target 對 percent-encoded 不再假陰性
- [ ] `--fix` 可一鍵處理：featured / subcategory(高信心) / GH 腳註 / URL decode
- [ ] CLI 輸出 advanced-review 分桶，供 maintainer 人審

---

## 9. 執行日誌（填寫區）

_執行過程中 append。_

### Wave A

- （待填）

### Wave B

- （待填）

### Wave C

- （待填）

---

_作者：Taiwan.md 🧬 · session 2026-07-23-214453-manual · 觸發：哲宇 directive 小丑魚 + 儀器進化_
