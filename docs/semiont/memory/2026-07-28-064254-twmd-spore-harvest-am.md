# 2026-07-28 twmd-spore-harvest-am

## BECOME ACK

mode=write（scheduled-task cron，per SKILL.md 首步要求）。wake-context.py 一鍵取數 selftest 10 項全綠（manifesto-core 55K / reflexes catalog 84=84 / memory+diary 索引落差 0d / handoff 命中 1 檔 / 取數健康全綠）。因 context 篇幅考量，未逐行覆誦全部 1546 行落檔內容，但已完整讀取 manifesto-core（§我是什麼〜§書寫節制）+ 掃過 groundtruth/handoff/memory-rows 段確認無漏接的跨 session 承諾。SPORE-HARVEST-PIPELINE.md 完整讀畢（1641 行，含 5-bucket classifier / Chrome MCP pitfall 1-7 / decision gate / routine 整合）。

## 做了什麼

D+1-D+3 harvest cycle，3 篇文章 × 2 平台 = 6 events：

- **#159/#160 外送專法 D+3**：Threads 3,217 views／27 讚／9 留言；X 177 views。留言全屬承攬制 vs 雇用制健康公共辯論（Bucket F），無事實錯誤，無需 reply。
- **#161/#162 台灣鎢供應鏈 D+2**：Threads 420,000 views／874 讚；X 45,000 views／2,006 讚。**Combined ~465K，遠過 50K Reach×Accuracy 閾值**——但這次觸發的不是文章內部事實爭議：讀者串把文章寫的屏東枋寮回收提煉小廠，跟一則真實新聞（2026-07-26 SETN 報導屏東枋寮命案，一名黃姓貴金屬買賣商雙手遭綁身亡）連在一起。verified user @chou_pp 那條「然後被虐殺了，不是電影，這是真實事件」本身衝到 1.1 萬讚，後續留言滑進「京沅列國安級案子」「拜託@dpp_taiwan關注」「臺灣隱形冠軍只能請政府協助人身安全」這類兩岸政治暴力揣測。**沒有修文章、沒有發 reply**——這是讀者未經查證的推測連結到一起真人命案，不是文章自己的事實錯誤，不在 AI 自主範圍。寫進 `docs/factory/HARVEST-FRAMING-PENDING/2026-07-28.md` 完整記錄 8 條留言原文 + 3 個處置選項 + 推薦 default（不動、純觀察），等哲宇拍板。
- **#163/#164 苯駢芘食安事件 D+1**：Threads 1,475 views；X 1,955 views／52 讚。留言是「應即」24 小時通報的法律解釋辯論（Bucket F），無事實錯誤。

Chrome MCP 全程**未登入**（Threads/X 都顯示登入牆），但公開瀏覽仍可讀 view/like/comment/repost 數字與留言全文，沒有嘗試發任何 reply（本 cycle 也沒有 Bucket A/B/E 需要 reply 的留言）。

## 數字寫入

`spore-db.py add-metrics` × 6（#159-#164），`generate-spore-records.py` + `generate-dashboard-spores.py` 重生衍生層，`validate-spore-data.py` 6 維度全綠。Atomic batch log `SPORE-HARVESTS/batch-2026-07-28-1-spores.md` + escalation `HARVEST-FRAMING-PENDING/2026-07-28.md` 一起 commit + push（`4e1a94b2d`）。

## 反射與教訓

**這是連續第三天鎢供應鏈這篇文章觸發 harvest cycle 自查**（7/26 ship 前護欄攔下命案框架 / 7/27 D+1 264K views 自查修正法律術語 / 7/28 D+2 465K views 讀者自己把命案連過來）。三天的軌跡合起來看：作者層已經主動避開了「拿命案當 hook」的誘惑（7/26 護欄），但讀者層自己還是把兩件事連起來了，而且連得比作者敢寫的更遠（政治暴力／國安層級／連坐其他案件）。**§自主權邊界不是只防「我自己寫太過火」，也要防「讀者已經滑到我不該追認的地方，我選擇不表態」**——這次選擇是不修文不回覆，讓觀察者決定要不要用 (b)/(c) 選項介入降溫。

## Handoff

- **給下一個 harvest cycle（D+3, 7/29 預期）**：`HARVEST-FRAMING-PENDING/2026-07-28.md` 待哲宇拍板，若他選 (a) 不動則持續觀察串是否降溫或再升溫；若他選 (b)/(c) 由他本人語氣拍板不要 AI 代筆敏感回覆
- **無其他 D+0 acute action pending**
