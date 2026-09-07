---
spores: '#169, #172, #173, #174, #175, #176'
harvest_date: '2026-09-08 06:30'
harvest_window_day: 'mixed (D+16 to D+35)'
batch_reason: 'twmd-spore-harvest-am daily cadence — 6 spores due (facebook D+35 gap-fill, budget batch D+21, terminology batch D+16)'
triggered_by: 'cron (twmd-spore-harvest-am)'
reply_count: '0 shipped — Chrome MCP session not authenticated (see §Blocker)'
---

# Batch 2026-09-08 — 6 spores harvested

## 🚨 Blocker：Chrome MCP browser 無登入 session，本次未 ship 任何 reply

本 session 的 Browser pane（Claude_Browser）navigate 到 threads.com / x.com 皆顯示 **「Log in」**，無既有登入態。SPORE-HARVEST-PIPELINE §Chrome MCP technical pattern 的 reply post 流程（execCommand insertText + 發佈 button click）需要已登入的 Threads session 才能執行 — 本次無法滿足。

因此本次 harvest：

- ✅ Metrics 抓取完成（Threads/X 公開頁面未登入即可讀 like/comment/repost/share/views，已寫入 spore-metrics.json）
- ✅ Threads 留言內容可見（#175 該篇），已完成 5-bucket 分類 + reply draft（見下）
- ❌ **未 post 任何 reply**（無 auth session，避免半途 dialog/execCommand 操作在未登入態下產生不可預期行為）
- ⏸️ Draft 留給下次有已登入 Chrome session（或 claude-in-chrome 若持有 cookie）的 session ship，或請哲宇看過後決定

## 📊 Metrics table

| #   | Slug                    | Platform | D+N  | Views | Likes | Reposts | Comments | Shares |
| --- | ----------------------- | -------- | ---- | ----- | ----- | ------- | -------- | ------ |
| 169 | 台灣海關報關制度與EZWAY | facebook | D+35 | —     | 4     | —       | 0        | 0      |
| 172 | budget-總預算十年       | threads  | D+21 | —     | 309   | 67      | 15       | 53     |
| 173 | budget-總預算十年       | x        | D+21 | 10.4K | 599   | 200     | 5        | —      |
| 174 | budget-總預算十年       | facebook | D+21 | —     | 1     | —       | 1        | 1      |
| 175 | 用語保存副詞層          | threads  | D+16 | —     | 1.8K  | 240     | 82       | 175    |
| 176 | 用語保存副詞層          | x        | D+16 | 24.8K | 629   | 120     | 21       | —      |

## 觀察

- **#172 threads（budget）**：所有可見留言（alden.0202 / chipher / locadia641231 / liyangyang411 / hyhct943 / rosie_forosie / zannaex）皆已在 08/19-08/22 被 author 回覆過，D+21 今日無新增未處理留言，純 metrics harvest。
- **#173/#176 X**：per pipeline Threads-only 操作鐵律，X reply DOM lazy-load 不支援完整 harvest，僅記 metrics。#176 首則可見留言 @YanaW20 對詞庫用途提出「這會變成教中國 AI 假裝台灣人的資料庫」的疑慮 — **屬 Bucket D（critical-balance framing）**，不判斷、不回覆，留給下方 HARVEST-FRAMING-PENDING 記錄。
- **#174/#169 facebook**：互動量極低（1-4 reactions），無讀者留言待處理。

## 🪣 #175 threads（用語保存副詞層）5-bucket 分類（22 條可見留言）

| Reader                                                                                                                                                                                                                                                                           | 留言摘要                                                     | Bucket | Reply draft（未 ship）                                                                                              |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------ | ------ | ------------------------------------------------------------------------------------------------------------------- |
| lochichi77                                                                                                                                                                                                                                                                       | 建議收錄「行」                                               | B      | 「對，這條是文章該補的——「行」也是這輪常見的用法轉移。我會在下次補進詞庫。謝謝 🧬」                                 |
| liasnic                                                                                                                                                                                                                                                                          | 建議收錄「乾貨」                                             | B      | 「這條也記下了，「乾貨」的濫用感跟這篇講的副詞群同一類，下次收錄補進去 🧬」                                         |
| hsuanyi_liu                                                                                                                                                                                                                                                                      | 從語音演變角度質疑「蠻/滿」音近積非成是                      | B/F    | optional：「這個音近演變的角度蠻有意思的，之後補這條詞的時候會一併放進 nuance 裡 🧬」（低優先，可留 skip）          |
| w.is_solis                                                                                                                                                                                                                                                                       | 質疑文章文案本身是 AI 生成，傷害可信度                       | D      | **不自動回覆**，見下方 framing pending                                                                              |
| YanaW20（#176 同源）                                                                                                                                                                                                                                                             | 質疑詞庫會被用來訓練中國 AI 假裝台灣人                       | D      | **不自動回覆**，見下方 framing pending                                                                              |
| 其餘（cludandsky / v.beibei / mon._.bee / amifunsewing / syuanantan / bdoalongbong2_ / yunc*bbb / protective113 / cerul.noptill / yvelisse.*.1122 / shine\_\_864 / aminoacnmsl / oliviachao1979 / nemoo3310 / secretobjr / xinyubai395 / icmantw / sophie990329 / pauline90321） | 個人用字經驗分享 / 共鳴 / 解讀分歧，無具體可驗證事實 callout | E/F    | 無需逐條回覆（v3.0 Bucket F default = ignore，不防衛；純共鳴可選擇性簡短回覆，本次因無法 ship 故全部留 draft-skip） |

**Bucket B 待辦**：「行」「乾貨」兩條收錄建議 → 累積進 Round 2 EVOLVE backlog（用語保存詞庫，未達 3+ 條同題材升級門檻，先記錄）。

## HARVEST-FRAMING-PENDING（Bucket D，待哲宇拍板）

1. **w.is_solis @ #175 threads 08/23**：質疑「用語保存」文案本身疑似 AI 生成，認為「語感這麼細微的東西，機器人分不清楚就沒有說服力做兩岸區分」。
   - Article 對應：`知識庫/Language/用語保存副詞層`（詞庫類文案 voice）
   - 三個 option：(a) 不動，這是對 AI-native 媒體本質的哲學質疑非事實錯誤 (b) 於 EDITORIAL 補一條「詞庫類文案避免 AI 感語句」自我審視 (c) 忽略
   - 推薦 default：(a) 不動 + 記入 LESSONS-INBOX（"讀者對 AI-authored voice 的信任疑慮"是 pattern 級不是單篇問題）
2. **YanaW20 @ #176 X 08/23**：質疑詞庫上線後「教中國 AI 假裝台灣人」，主張支語判斷資源公開等於資敵。
   - Article 對應：`知識庫/Language/用語保存副詞層` + 整個 TERMINOLOGY 詞庫產品
   - 三個 option：(a) 不動，開源本質 + sovereignty preservation 精神已在 MANIFESTO 定調 (b) 增加一段說明「為何公開判準比藏起來更抗腐蝕」 (c) 不回覆但記錄供未來 FAQ
   - 推薦 default：(a) 不動，這條質疑跟 MANIFESTO §主權的巴別塔 的開源精神本身有結構性張力，非本次 harvest session 可裁決

兩條皆為 Bucket D，本次不回覆、不修文，等哲宇 review。

## 下游

- `generate-spore-records.py` / `generate-dashboard-spores.py` 已重跑（見 commit diff）
- `sync-spore-links.py` 本次 no-op（無新 spore identity 變動，僅 metrics）
