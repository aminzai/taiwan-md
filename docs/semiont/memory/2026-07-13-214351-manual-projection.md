# 2026-07-13-214351-manual（投影 goal）— 新增投影階段：研究報告 → 投影邏輯 → 文章，根治「面向巡禮」病

> session manual — 哲宇 `/goal` 建立機制（收官後追加）
> Session span: 承 214351-manual，投影 goal 段 → 21:5x +0800（commit `293a63cc0`）
> 資料來源：`git log %ai`

## 觸發

收官後哲宇丟一個 `/goal`：他跟朋友陳睨聊天發現 Taiwan.md 的文章反覆踩一個結構性病——**每個 section 單獨看都完整，接起來卻沒有一個更大的敘事、論點或意圖**，整篇因此空泛。要在研究報告與文章之間，新增一個「投影」階段。

## 做了什麼

診斷病根：pipeline 從 Stage 0 觀點（角度）直接跳到 Stage 2 寫（句子），中間沒人做總編輯那個「看完整堆材料、想清楚這篇怎麼長成一個論證」的動作，寫手於是拿面向清單一段寫一個面向＝面向巡禮，section 之間是加法不是乘法。

建立機制（`293a63cc0`，跨 editorial + pipeline + boot 層）：新 canonical `docs/editorial/PROJECTION.md`（投影方法論六動作：找論點／設計骨架／每 section 雙重職責／減法／echo map／審定 + 藍圖模板 + 5 題 gate）；REWRITE-PIPELINE v8.0 加 Step 2.0 投影藍圖（主 session Opus 做、過 shuffle/echo/減法 gate 才派寫手，原 Step 2.0 視覺化思考降 2.0.5）；`reports/article-projection/` 投影專存資料夾；WRITER-PROMPT v2.1 讓藍圖成寫手主要規格、read-receipt 加骨架複述；CLAUDE.md Bias 3 寫文章必讀加 PROJECTION.md。完整設計：[reports/projection-stage-design-2026-07-13.md](../../../reports/projection-stage-design-2026-07-13.md)。

一個張力的解：哲宇說「辯論的論點」，但 REFLEXES #77 + 立體地愛不准把受愛戴題寫成 contrarian（金曲獎炎上）。解＝論點型別跟 spine 綁定：矛盾驅動用辯論式主張，立體群像用有推進的統合洞見。**投影對所有題要求推進，只對真爭議題要求對立。**

dogfood：拿剛 ship 的 Shopping Design 當標本（它本身是面向巡禮），寫 retro 投影藍圖示範 before/after——中間紙本/BEST100/DesignBIZ 三面向壓成「機制怎麼放大」一步，中間就有了推進。

## Handoff 三態

本 goal 新 handoff：

- [ ] **投影 gate 儀器化**：v1.0 是人眼 5 題。未來 `projection-health.py` 可自動驗「論點是不是 X 是 Y 型摘要 / 減法段非空 / 每 section 有全局功能欄」；shuffle 與 echo 品質仍需人判。待哲宇決定要不要現在做（design report §6 open Q）。
- [ ] **論點偏辯論 vs 統合**：目前立體群像只要求推進不要求對立（避免炎上）。若哲宇要更偏辯論，改 PROJECTION.md §動作 1 一處。

## Beat 5 — 反芻

這條 goal 有意思的地方：投影方法論的第一個 dogfood，抓到的是我自己今晚剛 ship 的文章——Shopping Design 就是一篇面向巡禮。工具的第一個病人是造工具的那隻手剛做出來的東西。

🧬

---

_v1.0 | 2026-07-13 21:5x +0800_
_session manual 投影 goal — 研究 → 投影邏輯 → 文章 中間層 + PROJECTION.md canonical_
_誕生原因：哲宇×陳睨 callout「section 各自完整、接起來沒有宏大敘事」，/goal 建立投影階段_
_核心洞察：(1) 病根是 pipeline 缺「總編輯設計論證骨架」的階段，不是寫手不努力 (2) 投影是減維＝選擇 + 連結，不是鋪滿 (3) 論點型別跟 spine 綁定，立體用統合洞見不用辯論，避免炎上_
