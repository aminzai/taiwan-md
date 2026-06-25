### Spore #150/#151 Fact Blueprint — mini-taiwan-pulse

**Angle**（v2，哲宇 2026-06-25 reframe）：一個有都市計畫眼睛的資料分析師，用審美與策展，把台灣零散到打不開的開放資料，變成一座會呼吸的地圖。AI 處理撈資料的苦工，但「畫面美不美、講不講得出一件事」由他的品味決定。**不強調「人沒做事」，強調「好策展人的審美能做出很棒的作品」。**
**Template**：B 冷知識型（concrete-anchor + 反差 hook）— Tier 1b 具體性槓桿
**Platform**：both（Threads #150 + X #151）— 科技/開源 + zh 人物故事，雙平台
**Hook tier**：1b（具體 anchor「會呼吸的地圖」+「我沒寫一個字」+ 反差「一句話 → 73,900 筆」；Migu 非知名人物，不走 1a）
**Ethical flags**：無（無死亡/創傷/未成年/政治敏感）
**Hook Blueprint**：非結構性 briefing 題（anchored 在一個人 + 具體地圖，不是政策數字堆）→ 不強制觸發；開場已用「你知道嗎 + 具體人物/動作」滿足精神
**Taiwan.md 連結**：**刻意不寫進 spore**（Bias 1 — 對外公開貼文寫「他 fork 了我們/同構」= 自我宣傳）。spore 純講 Migu 的作品。

| #   | 事實（孢子出現順序）                            | 信度層          | 需跨源驗證？ | 敏感度 | 狀態 / 來源                                                   |
| --- | ----------------------------------------------- | --------------- | ------------ | ------ | ------------------------------------------------------------- |
| 1   | Migu 是資料分析師、大學唸都市計畫、很久沒碰地圖 | high_confidence | No（他自述） | 無     | ✅ 他 sciwork 2026 演講自我介紹投影片逐字                     |
| 2   | 把一份 CSV 拖進地圖工具做出第一張台灣地圖       | high_confidence | No           | 無     | ✅ 演講「DAY 0」投影片（Kepler.gl）                           |
| 3   | 半年內十幾個開放資料視覺化專案                  | high_confidence | No           | 無     | ✅ GitHub API 2026-06-25 實證（10+ repo 星系）                |
| 4   | 五脈共動：飛機/船/列車/公車/垃圾車              | high_confidence | No           | 無     | ✅ 演講 Case 4 Pulse 投影片逐字「五脈共動」                   |
| 5   | 中央開放資料五萬多筆（data.gov.tw 52,891）      | single_source   | 歸給他簡報   | 無     | ⚠️ Migu 簡報數字，spore 框「他算了一下」非獨立查證政府統計    |
| 6   | 一句「分析台灣火災相關公開資料」→ 73,900 筆     | single_source   | 歸給他簡報   | 無     | ⚠️ Migu 簡報火災 pipeline 數字，spore 框「他丟一句…系統自己」 |
| 7   | 跨 21 個平台收斂                                | single_source   | 歸給他簡報   | 無     | ⚠️ 同上，他簡報數字                                           |
| 8   | 分縣市的火災成因報告                            | single_source   | 歸給他簡報   | 無     | ⚠️ 他簡報 Agent 產出                                          |
| 9   | 「我沒寫一個字」                                | high_confidence | 逐字         | 無     | ✅ 演講投影片 verbatim（可在 deck Ctrl-F）                    |
| 10  | 「出題與驗收」+「會自己長大的系統」             | high_confidence | 逐字         | 無     | ✅ 演講副標 + 標題 verbatim                                   |

**信度結論**：人物/作品事實（1-4）GitHub API + 演講逐字實證；數字（5-8）是 Migu 簡報 claim，spore 全程歸屬「他算了一下 / 他丟一句 / 系統自己」，不寫成 Taiwan.md 獨立查證的政府統計（同文章 source-fidelity 處理）。引語（9-10）演講投影片逐字。

---

## Spore 本體（Threads 主貼 = X 主文）

你知道嗎？🗺️

一個叫 Migu 的資料分析師，大學唸都市計畫。他把台灣政府開放的那些零散資料，飛機、船、列車、公車、連垃圾車，疊成了一張會呼吸的地圖：每架飛機拖著一條彗尾般的光軌，航線交疊的地方自己亮起來，哪裡繁忙不用看數字，看光就知道。

台灣的開放資料其實多到嚇人，光中央就有五萬多筆，散在幾十個平台。多數人就算全抓下來，也只是一堆打不開的試算表。

Migu 真正厲害的，是他那雙都市計畫訓練出來的眼睛：知道哪幾層資料疊在一起會說故事，該用什麼顏色，讓哪一層亮、哪一層沉。撈資料的苦工他交給 AI，但畫面美不美、講不講得出一件事，由他決定。

把一堆死掉的試算表，變成一座會呼吸的台灣，靠的是一個策展人的眼睛。

## URLs

- Threads self-reply：完整故事 👉 https://taiwan.md/technology/mini-taiwan-pulse/?utm_source=threads&utm_medium=spore&utm_campaign=s150
- X inline：完整故事 👉 https://taiwan.md/technology/mini-taiwan-pulse/?utm_source=x&utm_medium=spore&utm_campaign=s151

（slug `mini-taiwan-pulse` 為 ASCII，無需 percent-encode）

## 配圖

square 1080×1080：mini-taiwan-pulse 文章 hero（會呼吸的地圖），make-spore.sh --prod（文章已 live 40min+）。
