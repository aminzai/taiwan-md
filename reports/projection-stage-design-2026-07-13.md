# 投影階段設計 — 研究報告 → 投影邏輯 → 文章（2026-07-13）

> `/goal`（哲宇 2026-07-13-214351-manual session）：在研究報告與文章之間，新增一個「投影」階段。誕生於哲宇跟朋友陳睨聊天後的發現。

## 1. 觸發與病灶

哲宇跟陳睨聊完，發現 Taiwan.md 的文章反覆踩一個結構性病：**每個 section 單獨看都是一則完整的介紹，接起來卻沒有形成一個更宏大的敘事、論點或意圖。** 文章因此空泛。

病根在 pipeline 的結構：Stage 0 觀點（給主軸錨 + 面向畫布）→ Stage 1 研究 → Stage 2 寫。中間沒有一個階段做「總編輯看完整堆材料、想清楚這篇到底怎麼長成一個論證」的動作。於是寫手拿到 {主軸 + 面向清單}，一段寫一個面向 = **面向巡禮**：section 之間是加法（面向 + 面向），不是乘法（一步推進下一步）。shuffle test 一驗就露餡——中間 section 順序打亂，文章讀起來差不多。

研究做得越足、面向越多，病越明顯，因為材料多讓寫手更傾向「鋪滿面向」而不是「挑材料建論證」。這跟 EDITORIAL §密度平衡（事實堆疊）是同一個病的兩面：密度平衡管「一段別塞太多事實」，投影管「整篇別排成面向清單」。

## 2. 解法：投影階段（研究 → 投影邏輯 → 文章）

投影的隱喻已經是 Taiwan.md native（MANIFESTO「我是一維投影」）。形式化：

- 研究報告 = 高維材料堆（每個面向一個維度）
- 文章 = 這堆材料在「一條敘事線」上的一維投影（讀者從第一字讀到最後一字）
- 投影邏輯 = 投影矩陣：丟哪些維度、怎麼排、每個怎麼映射回軸。矩陣差 = 噪音；矩陣好 = 論證。

三個階段清楚分工：**觀點（角度，研究前）→ 研究（材料）→ 投影（建築，研究後寫前）→ 寫（句子）**。

投影方法論六個動作：**找論點**（有張力、要被賺到，非摘要）→ **設計骨架**（動作序列，過 shuffle test）→ **每 section 雙重職責**（局部承載 + 全局功能 + 扣回主軸 + 進出連結）→ **減法**（明列砍什麼）→ **echo map**（每段押韻主軸錨）→ **審定**（文風/結構/viz/媒體前移到寫前）。

## 3. 一個張力的解（flag）

哲宇原話有「辯論的論點」。但 REFLEXES #77 + MANIFESTO §13 立體地愛：受愛戴題不可硬塞 contrarian thesis（金曲獎 v1 炎上）。解：**論點型別跟 spine 綁定**——矛盾驅動題用辯論式主張，立體群像題用有推進的統合洞見。**投影對所有題要求「推進」，只對真正爭議題要求「對立」。** 立體 ≠ 沒論點（那會回到面向巡禮）；立體的論點是「這群面向合起來說出什麼」，且要在文中被兌現。（若哲宇要更偏辯論，改 PROJECTION.md §動作 1 一處即可。）

## 4. 機制（改了哪些檔）

| 檔                                              | 改動                                                                                                                                                                                                            |
| ----------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `docs/editorial/PROJECTION.md`                  | **新增** 投影方法論 canonical（六動作 + 藍圖模板 + 5 題 gate + 反例 gallery）                                                                                                                                   |
| `reports/article-projection/`                   | **新增**「投影專存」資料夾，每篇一份 `{slug}.md` 藍圖（parallel research/ + article-evolve/）                                                                                                                   |
| `reports/article-projection/Shopping-Design.md` | **新增** 第一個 worked example（retro，before=面向巡禮 / after=五步論證）                                                                                                                                       |
| `docs/pipelines/REWRITE-PIPELINE.md` v7.11→v8.0 | ASCII spine 加投影 block；Hard Gate Inventory 加「投影藍圖」列；Step 2.0 投影藍圖（原 Step 2.0 視覺化思考降 2.0.5 併審定）；§多 agent 編排 加「2.0 投影藍圖 = Opus orchestrator」列；跨檔案分工加 PROJECTION.md |
| `docs/pipelines/WRITER-PROMPT.md` v2.0→v2.1     | 必讀四份→五份（加 {PROJECTION_BLUEPRINT} 當主要規格）；read-receipt 加「骨架複述逐 section 全局功能」防面向巡禮                                                                                                 |
| `CLAUDE.md` Bias 3                              | 寫文章必讀加 PROJECTION.md                                                                                                                                                                                      |

**誰做投影**：主 session（Opus orchestrator），研究合成單檔之後、派寫手之前。不派給寫手——寫手拿到已想清楚的骨架，執行不發明。**HARD GATE 5 題**（論點非摘要 / 骨架過 shuffle / 每 section 有全局功能 / 減法非空 / echo map 覆蓋全篇）全過才派寫手。

## 5. Dogfood

以剛 ship 的 Shopping Design 當標本：它本身是面向巡禮（中間紙本/BEST100/DesignBIZ 可 shuffle）。retro 投影（[reports/article-projection/Shopping-Design.md](article-projection/Shopping-Design.md)）示範 after：五步論證，把三個獨立面向壓成「機制怎麼放大」一步，中間就有推進。已 ship zh-TW 不回頭重寫（時間是結構），下次 EVOLVE / 多語投射可採用。

## 6. Open questions（給哲宇）

1. **論點偏辯論 vs 統合**：目前立體群像用統合洞見（只要求推進不要求對立）。要不要對所有題都逼一點辯論性？（我判斷不要，避免炎上；但 flag 給你。）
2. **gate 儀器化**：v1.0 是人眼 5 題（同 §觀點成型）。未來 `projection-health.py` 能自動驗的大概是「論點是不是 X 是 Y 型摘要」「減法段非空」「每 section 有全局功能欄」；shuffle test 與 echo 品質仍需人判。要不要現在就做工具？
3. **Micro / 短修正豁免**：目前只 depth 文強制投影。單段補寫 / heal 不需要。邊界對嗎？

---

_v1.0 | 2026-07-13-214351-manual — 誕生：哲宇×陳睨 callout「section 各自完整、接起來沒有宏大敘事」。核心：投影是減維（選擇 + 連結），把總編輯「這堆材料怎麼變一篇有論證的文章」的動作變成必經階段。_
