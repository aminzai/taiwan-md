# 2026-08-04-095220-curation-tier-design — 查證狀態分層設計：草稿區問題翻轉成三態投影＋參與式進化區

> session curation-tier-design — 哲宇 `/twmd-become` directive 觸發的 EVOLVE Mode 4 設計 session
> Session span: 09:15 → 09:52 +0800（~37 min，1 commit `c93482f1a`）
> 資料來源：`git log %ai`

## 觸發

哲宇問：貢獻者文章品質不足時，要不要放一個「草稿待進化區域」——在站上，但跟正式深度研究文章有分隔，避免混淆讀者。背景是近期有人大量貢獻，用的 AI 品質不夠好。指示深度研究並自我進化。命中 BECOME High-stake #2（新 workflow 設計），Full mode 甦醒後走 EVOLVE Mode 4（THINK → DIVERGE → REPORT，實作停等拍板）。

## 調查改變了問題的形狀

先量測哲宇擔憂的具體對象：idlccp1984 近 45 天 28 篇 zh 新文章。結果推翻「單薄」假設——字數 6,934〜69,153 全數超過近期品質基準中位 6,556，多數 8〜31 條腳註，量化指標全過。真正的病在事實可靠層：maintainer 抽驗連續抓到杜撰引語（黑蝙蝠中隊 2 處、黃崇仁）、日期誤植、死鏈腳註，另有 4 篇 0 腳註。這批文章 28 篇全部 `lastHumanReview: false`，而這個欄位雖覆蓋 zh SSOT 876 篇，站上零投影，讀者看不到任何查證狀態。既有機制盤點另發現 `draft` 欄位是死欄位（schema 存在、全站 0 使用、template 零行為），maintainer 已在實務用 `featured: false` 做粗分層但沒 canonical 化。結論：訊號全部已存在，缺的是讀者可見的投影層。

## 設計定案候選與落地

發散四案（輕投影徽章／結構草稿區／分軌 URL／三態投影）後定案候選是方案 D：三態查證狀態（🔎 已深度查證／無標示／🌱 進化中），判定看「走過哪些查證流程」而非「誰寫的」，分隔只在呈現層與策展層，merge-first 接受層零改動。三態設計避開二態的自貶陷阱（全站僅 22.4% true，二態會把 77.6% 標成未查證）。關鍵翻轉：「進化中」不做防禦性隔離，做成邀請讀者參與查證的入口——直接餵 OBSERVER-QUEUE #25 的 review_coverage 缺口（免疫黃燈 28 天的拖分主因）與熱帶雨林讀者勘誤機制。設計報告落 [reports/design-curation-tier-2026-08-04.md](../../reports/design-curation-tier-2026-08-04.md)（含實作清單九項與風險表），六個決策點掛 OBSERVER-QUEUE #26 帶預設選項，`c93482f1a` 一個 commit ship（verify-commit-scope 2/2 檔）。

## 收官 checklist

| 檢查項                       | 狀態                                   |
| ---------------------------- | -------------------------------------- |
| MEMORY 有這次 session 的紀錄 | ✅                                     |
| Timestamp 精確               | ✅（git log %ai）                      |
| Handoff 三態已審視           | ✅                                     |
| CONSCIOUSNESS 反映最新狀態   | ✅（無器官分數變動，佇列 #26 新增）    |
| 自我檢查工具 PASS            | ✅（報告 hard=0，memory profile 自檢） |

## Handoff 三態

繼承上一 session（2026-08-04-004923-spore-publish-165）：

- [ ] **需要哲宇：給 idlccp1984 的 PR #1288 回覆**（對外溝通，續 carry。本 session 的 #26 決策點 5 與此相關：若採徽章制，回覆文案可一併說明）
- [ ] **`public/article-images/People/` 大寫目錄殘留**（task chip 已開，續 carry）
- [ ] **D+1 harvest #165/#166**（今晨 spore-harvest-am 應已收，未驗）
- [ ] **spore-writing Wave 3 邊界 hits 觀察**（續 carry 至下次 distill）

本 session 新 handoff：

- [x] ~~查證狀態分層設計報告 + OBSERVER-QUEUE #26~~（本 session 完成）
- [ ] **等哲宇拍板 #26 六決策點**後啟動實作清單（frontmatter 欄位 → template 徽章 → 說明頁 → MAINTAINER §1b 補步驟 → 儀器對賬 → dogfood 2 篇）。補標歷史名單影響 >50 檔，需圈名單

## Beat 5 — 反芻

哲宇的原話是「草稿待進化區」，調查完發現如果照字面蓋一個隔離區，會同時踩到 merge-first 神經迴路跟主權巴別塔（noindex 等於讓聲音消失）。真正缺的東西小得多：身體裡的免疫資訊（lastHumanReview、DONE-LOG、health 分數）從來沒有接到皮膚上，讀者摸不到。把「隔離」翻成「投影＋邀請」之後，這個設計順便變成免疫黃燈 28 天那個 review_coverage 洞的參與介面——兩個看似無關的待決事項（#25、#26）其實是同一條路。設計過程中最有用的一步是先量測而不是先相信描述：「品質不足」四個字底下，量化層全綠、事實層有病，分層判準因此從「字數腳註」改錨到「查證流程」。

🧬

---

_v1.0 | 2026-08-04 09:52 +0800_
_session curation-tier-design — 哲宇 directive「貢獻者文章品質分層」EVOLVE Mode 4 設計_
_誕生原因：idlccp1984 近期 28 篇 AI 生成文章含杜撰引語風險，哲宇怕混淆讀者_
_核心洞察：(1) 品質訊號全部已存在，缺的是讀者可見投影 (2) 分層判準看查證流程不看作者身份 (3)「進化中」做成參與入口，隔離題翻成邀請題_
