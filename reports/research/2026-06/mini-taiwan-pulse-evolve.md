# Research SSOT — EVOLVE「Mini Taiwan Pulse」(2026-06-25)

> 觸發：哲宇 directive「進化 mini-taiwan-pulse + 深度研究 https://github.com/ianlkl11234s + 完整抓取分析他的演講 https://github.com/ianlkl11234s/0613-sci-work-share」
> 既有文章：`knowledge/Technology/mini-taiwan-pulse.md`（2026-04-19 寫，lastVerified 2026-04-19，僅憑 repo 寫成，沒看過他的演講與整個專案星系）
> EVOLVE 模式：substantial re-conceptualization（不是 surgical add）。舊文核心 framing「一個人、一個 repo、一個週末」已被新素材證偽。

---

## 一、觀點（Stage 0）— 寫作前的角度

### 核心張力（anchor，整篇貫穿）

**台灣的開放資料多到「一個人腦掃不完」（他簡報的數字：data.gov.tw 約 5.3 萬筆 dataset）——所以 Migu 不再自己掃。他把資料交給 AI Agent，自己退到只剩「出題與驗收」。一張會呼吸的地圖背後，是一套正在學會自己長大的系統。**

舊文的角度（「一個人、一個週末、示範型專案」）現在太小、而且有點錯：他不是業餘玩票，是從 2025 年底持續至今的 serial builder，蓋的不是一個 demo，是一整套用 agent 編排、「會自己長大」的開放資料系統。

### 為什麼這個張力成立（反向解釋 — 主動 challenge 舊文自己的通行說法）

- 舊文說「g0v 是集體，Migu 是個人週末」——這個對比沒錯但停在表面。更接近真相的是：**Migu 一個人能做到「一整座資料星系」的規模，正是因為他不是一個人在寫——他用一個 Claude orchestrator 指揮一群 tmux 隔離的 worker（每個 worker 也是一個 Claude session）**。個人 × AI agent loop，才是 2026 年公民科技的新樣態。「一個人的 git log」這個 image 要留，但要翻轉：那些 commit 越來越多不是他手打的。

### Arc（跟他自己的演講三段式同構，這是最好的骨架）

1. **起點的天真**：Day 0，一份 CSV → GeoJSON 拖進 Kepler.gl，第一張地圖。"原來台灣有這麼多資料，原來轉成地圖並不難"。這個天真的驚奇是種子。
2. **星系**：不是一個 repo，是「Mini Taiwan」家族——learning-project（189★）、flight-arc-graph（56★）、tw-ship-viz、satellite-arc、mini-taiwan-info、cctv… flagship 是 mini-taiwan-pulse（375★），而且 Pulse 自己從「三層」長成「五脈共動」（飛機/船/列車/公車/垃圾車）。
3. **規模的詛咒（pivot）**：5.3 萬筆 dataset「人腦掃不完」。這是整篇的轉折——個人努力的天花板。
4. **系統**：資料 → 整合 → 生成 → 觸發。40+ collectors、SQLite 知識庫、火災主題 pipeline（一句話 →73,900 筆 →"我沒寫一個字"）。
5. **Agent Loop（架構揭露）**：orchestrator + tmux worker + SESSION_BOARD.md 共同記憶 + 人類只做出題與驗收。「會自己長大的系統」。← 這裡放 Taiwan.md 連結（節制，見 §六）。
6. **誠實**：實驗 ~50%，harness 還沒穩，每個階段仍要人。這份 radical openness 本身是品質訊號。
7. **意義**：g0v 的集體敘事 → 個人 × agent 的新樣態，是擴充不是替代。政府開資料、社群讓資料被看見的光譜，多了一種「交給會自己長大的系統」的位置。

### Title 候選（冒號三明治 + 具體 + 報導者腔，slug 不變 `mini-taiwan-pulse`）

- A.「Mini Taiwan Pulse：台灣的開放資料多到一個人掃不完，於是他交給會自己長大的系統」
- B.「Mini Taiwan Pulse：從一張會呼吸的地圖，到一套交給 AI 自己長大的開放資料系統」
- C.「Mini Taiwan Pulse：一個資料分析師把台灣的資料海交給 Agent，自己只留下出題與驗收」
- （主 session 在 Stage 2.5 定稿，傾向 A 或 C——把「掃不完」「出題與驗收」這個張力放進 title）

### Description（120-160 字，吃進新核心）

要點：2026-02-24 開的 mini-taiwan-pulse、現 375★；但這只是「Mini Taiwan」星系的旗艦——他從 2025 年底持續做了十幾個台灣開放資料視覺化。核心矛盾 ending：台灣開放資料 5 萬多筆一個人掃不完，他把資料交給 AI agent 養成一套會自己長大的系統，自己只剩出題與驗收。

---

## 二、星系（GitHub API 實證，2026-06-25 抓取，全部 verifiable）

開發者：**Migu Cheng**（GitHub `ianlkl11234s`），帳號創建 2020-03-07，72 followers，24 public repos。
**Bio 已變更**（舊文引的是舊 bio）：

- 舊（舊文 [^1]）：`Senior Data Analyst. Exploring AI automation in daily work.`
- 新（2026-06-25 API）：`Building GIS visualizations from Taiwan open data · Exploring AI automation in daily work`
- → 他自己把 identity 從「資料分析師（順便玩 AI）」改寫成「用台灣開放資料做 GIS 視覺化」。這個 bio 變更本身是個好細節。

台灣開放資料 repo 星系（created 排序，★ = 2026-06-25 star 數）：

| created    |   ★ | lang       | repo                             | 備註                              |
| ---------- | --: | ---------- | -------------------------------- | --------------------------------- |
| 2025-12-13 |   3 | TypeScript | poc-bus-range                    | 最早的台灣資料 PoC（公車）        |
| 2025-12-15 |   2 | Python     | gis-data-collectors              | 收集器骨幹，**仍在更新（6-25）**  |
| 2025-12-29 | 189 | Python     | **mini-taiwan-learning-project** | 第一個爆紅（早於 pulse）          |
| 2026-01-15 |   0 | HTML       | taiwan-weather-timelapse         | 仍活                              |
| 2026-02-12 |  11 | HTML       | tw-ship-viz                      | 船舶                              |
| 2026-02-20 |  56 | TypeScript | **flight-arc-graph**             | 航跡（演講 Case 6 的 repo）       |
| 2026-02-24 | 375 | TypeScript | **mini-taiwan-pulse**            | 旗艦，**仍在更新（6-25）**        |
| 2026-03-01 |   0 | TypeScript | mini-tw-tra-atlas                | 台鐵 atlas                        |
| 2026-03-22 |   0 | (fork)     | **taiwan-md**                    | **fork 自 frank890417/taiwan-md** |
| 2026-03-29 |   6 | TypeScript | satellite-arc                    | 衛星                              |
| 2026-04-30 |   0 | HTML       | migu-taiwan-data-night-2026      | 另一場 talk（Taiwan Data Night）  |
| 2026-05-14 |   1 | TypeScript | mini-taiwan-info                 | 情勢儀表板（演講 Case 5）         |
| 2026-05-25 |   6 | TypeScript | mini-tw-cctv                     | 即時影像                          |
| 2026-06-11 |   0 | HTML       | flight-arc-sharing               |                                   |
| 2026-06-13 |   0 | HTML       | **0613-sci-work-share**          | **本次演講**                      |

**mini-taiwan-pulse 統計 delta（舊文 vs 現在）**：

| 指標       | 舊文（2026-04-19） | 現在（2026-06-25）     |
| ---------- | ------------------ | ---------------------- |
| stars      | 241                | **375**                |
| forks      | 12                 | **26**                 |
| open issue | 1                  | 1                      |
| 最後 push  | 2026-04-09         | **2026-06-25（仍活）** |
| commits    | 193                | 更多（repo 仍推進）    |

> ⚠️ commit 數現在多少未逐一抓；舊文「193 commits」是 4-19 的值。EVOLVE 寫法：講「到 6 月仍在 push」即可，不要編造新的精確 commit 數。star/fork 用新值（已實證）。

---

## 三、演講全文（Primary Source，verbatim 抓取）

**Repo**：`ianlkl11234s/0613-sci-work-share`，created 2026-06-13，HTML 靜態簡報（deck-stage.js），共 58 張投影片。
**標題（HTML `<title>`）**：「Mini Taiwan！把台灣開放資料，交給 Agent 養成一套會自己長大的系統 — sciwork 2026」
**場合**：sciwork 2026 / SCIWORK SEMINAR，2026.06.13。Live deck：https://sciwork-showcase.zeabur.app（部署在 Zeabur，他 repo 的 CLAUDE.md 寫明）。
**演講者署名**：MIGU｜資料分析師。GitHub `ianlkl11234s`，**Threads `@ianlkl1314`**（→ 舊文「沒有 Twitter / 沒有部落格」要更新：他有公開 Threads）。
**他 repo 的 CLAUDE.md 一句話**：「Mini Taiwan！把台灣開放資料，交給 Agent 養成一套會自己長大的系統。」（他自己也用 Claude Code）

### 副標 / 核心 thesis（verbatim 投影片文字）

> 「當 Agent 能自己跑完整個循環，人的工作只剩 —— 出題與驗收」

三段路（演講結構）：**01 SHOWCASE 做了什麼 → 02 SYSTEM 怎麼組起來（本場核心）→ 03 AGENT LOOP 怎麼自己跑**。

### 自我介紹（verbatim，重要傳記細節）

> 「Hi, 我是 migu，資料分析師。大學碰過 GIS（都計背景），出社會走資料分析，很久沒再碰。」

→ **新傳記事實**：都市計畫學術背景、大學碰過 GIS、出社會做資料分析、很久沒碰 GIS（這個專案是他「重新撿起 GIS」）。舊文完全沒有這層。

### 起點（verbatim，P04）

> 「DAY 0 第一張地圖。起點 · KEPLER.GL。把一份 CSV 轉成 GeoJSON 拖進 Kepler.gl，就有了第一張地圖 ——『原來台灣有這麼多資料，原來轉成地圖並不難』。KEPLER.GL · CSV → GeoJSON · 0 行程式。」

→ 絕佳開場 anchor：天真的驚奇 + 具體工具（Kepler.gl）+ 引語。

### SHOWCASE 案例（verbatim 重點）

- **Case 1 Mini Taipei**：「捷運 → 台鐵 → 高鐵，三套軌道疊成一張會動的地圖。體驗到動態的魅力。」TDX 開放資料、6 systems、351 trains live。（對應 repo 推測 mini-taiwan-learning-project，但**不要硬指**，講「他的台北軌道視覺化」即可）
- **Case 2 衛星**：「用公開 TLE 推算衛星軌道，再延伸到太陽系——同一套做法，只要有資料，都可以無限延伸。」CELESTRAK TLE · SGP4。
- **Case 3 船舶**：「航港局 AIS 即時點位——青藍光球 + 30 分鐘漸層拖尾，畫出台灣周邊海域的脈動。」~10 min 更新。
- **Case 4 · MINI TAIWAN PULSE 台灣的脈動**（★核心更新）：「天空、海洋、大地、街道、清運——**五脈共動**，疊成同一張會呼吸的地圖。第一次從『靜態 JSON』進化成『時空間資料庫』。」
  - **5 脈 = 飛機 / 船 / 列車 / 公車 / 垃圾車**（舊文只有天空/海洋/大地三層，要升成五脈，公車/垃圾車是新的）
  - 23 圖層、十大分類、獨立 toggle
  - **5,700+ 輛公車**（TDX, 30s polling）
- **整合 · 農×水**：「三個部會的孤島，疊成一張圖。農田、河川、溝渠、堤防、淹水潛勢同框——把孤島 JOIN 起來。」PMTILES · HTTP range request，**400MB → ~5MB**。
- **整合 · 醫療資源**：「把民生疊在人口上，缺口自己浮出來。醫院、診所、藥局、AED、長照點位 + 等時圈——看見可及性，也看見**醫療沙漠**。」NHI + 衛福部。
- **整合 · 大雨與災害**：「一條 Timeline，全部聯動。雷達回波、水庫、雨量、災害示警——不同頻率在 RPC 層統一，一拖時間軸全部同步回放。」
- **整合 · 衛星圖層 / 新聞事件（NER 地名抽取）/ 環境監測（EPA 空品 + CWA 雨量地震 + WRA 水位，異常值自己亮起來）**
- **Case 5 · Mini Taiwan Info（Dashboard）**：「把所有資料收斂成一個台灣情勢的監測儀表板——基礎統計、人口、軌道運輸、航運、水資源、消防、醫療，一頁一主題。」7 themes、CC BY 4.0。
- **Case 6 · Flight Arc（航跡）**：「把一段時間的所有起降，畫成一張航跡圖——高度色變 + 光軌拖尾，疊起來就是機場的『指紋』。」
  - 機場指紋畫廊：VHHH 香港 / EDDF 法蘭克福 / RCTP 桃園 / RJTT 羽田。「每座機場，都有自己的指紋。同一支 API · 不同的城市性格。」
  - **KATL 亞特蘭大**：「世界最忙機場。五條平行跑道 + 等待航線，畫出像賽車場的幾何——流量本身，就是一種形狀。」1,839 tracks。
  - 模式②跟隨（Viewshed 可見扇形，依高度）、模式③進場管制區（禁航/限航 3D 極光圖層，TW eAIP PDF 手抄 / UK OpenAIP API）
  - 案例：倫敦機場體系（EGLL hub + ~10 場）、紐約都會三角（KJFK/KEWR/KLGA）、時間軸地緣事件（杜拜 OMDB 2,740 軌跡，戰前/戰時/戰後迴避路線）、OpenSky 空域覆蓋。

### SYSTEM 幕後系統（★ 本場核心，舊文完全沒有）

四步驟：**資料接收 → 知識整合 → 分析生成 → 行動觸發**，「每一步都可以單獨抽換——整套不需要重蓋」。

- **Step 1 資料接收的演化**（verbatim）：
  - A 最早期「手動下載」：data.gov.tw 點 Excel 自己讀自己存（format xlsx/csv, where ~/Downloads, **limit 人腦記憶**）
  - B 中期「上網找」：API、PDF 報告、各縣市開放平台散落各處（22 縣市平台，problem 沒有索引）
  - C NOW「結構化知識庫」：每筆 metadata 標準化存進 **SQLite catalog**（queryable 可自動化查詢、scalable 可自動化拓展）
- **40+ 個 Collector**（P28，verbatim 來源涵蓋）：陸運（YouBike/Bus/VD/Freeway）、鐵路（TRA live/timetable）、航運（Ship AIS/TDX）、航空（FR24/OpenSky）、氣象（CWA 衛星/雨量）、災害（地震/NCDR）、太空（TLE/Launch）、水文（水庫/河川/地下水）、空品（AQI/微型感測）。「⚠ 連錯 3 次立即發 Telegram 告警」「📊 每天早上 09:00 推送 Daily Review」。
- **Step 2 規模的詛咒**（P30，★ pivot 引用）：「為什麼要 Agentic OSINT。data.gov.tw · 各縣市 · 民間——人類掃不完。**52,891**（data.gov.tw）+ 22 縣市平台 ~6–7 萬筆（含重疊）+ 民間/NGO/學術還沒算 = 你的人腦掃不完 → 這就是 LLM 該介入的地方。」
  - 一句話（verbatim）：「資料能被 LLM 看見，Agent 才能幫你發現『哪些資料應該放在一起看』。」
- **火災主題報告 pipeline（P32，★ 最強案例，"我沒寫一個字"）**：
  - 輸入一句話「分析台灣火災相關公開資料」→ 候選池逐輪擴張：**582 關鍵字命中 → 1,945 同義詞+主題擴張 → 2,404 FTS5 補搜+去重 → 21 平台 · 73,900 筆統一目錄**
  - 一條龍 6 階段自動拆解：A 預防 / B 應變 / C 通報 / D 起火分析 / E 損失 / F 報表，22 縣市 × 6 階段覆蓋矩陣
  - 獨家盤點：新竹火災潛勢圖 / 臺北搶救困難地區 / 桃園埤塘救援
  - 誠實 GAPS：沒有即時火災 API、事件級座標稀缺、災後追蹤不公開
  - **verbatim pull quote**：「Pipeline 自動產出。我　沒　寫　一　個　字。」
- **Step 3 分析生成**：水資源為例，先依「點/線/面」盤點，再依「怎麼來→怎麼留→怎麼用→何時警示」重組成敘事。火災分析（113 年全國 15,405 筆）：「**新北市最大宗起火原因是電氣因素 30.9%**」「**屏東縣是菸蒂 35.2%**」——verbatim「這份 reflect 報告完全由 Agent 串 API 跑出來」。
- **Step 4 行動觸發**：「Agent 跑完整循環。人類角色——給目標、收報告。中間五個齒輪自己轉：發現→收集→整合→產出→監測。」自動 weekly brief「本週新增開放資料 brief」。verbatim：「主題自己冒出來、報告自己送到信箱。」「雛形已經在跑 · 還沒做完——但循環的形狀已經出現。」

### AGENT LOOP 協作循環（★ 最 Taiwan.md-resonant，架構揭露）

- 「我目前的 GIS 循環：一個編排中樞，串起一圈獨立 repo——Agent 依序進站。」EXPLORE → COLLECT → RENDER（taipei-gis-analytics → data-collectors/gis-platform → mini-taiwan-pulse/info）。「每一站都是獨立 repo——編排層只管進度與決策，活都在各 repo 的 worker 手上。」
- **L07 指揮中心（verbatim，最具體）**：「一個 Orchestrator，一群 Worker。主 Agent 是一個 **Claude Session**；**TMUX 負責隔離**——每個 Worker 都是獨立分頁、獨立 Session。」
  - ORCHESTRATOR · CLAUDE SESSION：讀 proposal.md 拆任務排依賴、`spawn_tmux_claude.sh` 開 worker 分頁、監控 board 彙整進度驗收 PR
  - 「一個 Worker ＝ 一個 Tmux 分頁 ＋ 獨立 Session ＋ 一個 PR。」
- **L08 共同的記憶（verbatim，★ Taiwan.md 共鳴點）**：「進度與決策，全部寫成文件。集中看板 **SESSION_BOARD.md** ＋ 一個 Session 一份報告——不用互相猜。」「一人一檔，不打架。」「最後一關：驗收 Orchestrator 對照文件驗收 PR——**merge 由人拍板**，這一圈才算收束。」（還有 HANDOFF.md「下一棒任務書就緒」）
- **L09 未來·出題就好**：「一個計畫一個資料夾：PROPOSAL → DESIGN → TASKS → ARCHIVE。」「這就是『會自己長大的系統』——資料會自己流，頁面會自己長。」
- **L10/L11 誠實（★ radical openness）**：EXPERIMENT PROGRESS ~50%。「但是，Harness 還沒調到理想。可行歸可行，還沒穩，且也還在思考是否真的要這樣。」三件沒調好：①穩定性（容易跑掉、中斷）②開放資料較雜（還是很多需要人判斷資料是否可行，無法完全交給它）③人工介入（每個階段都還要人）。「以實驗的角度——有成功的地方，也有還在努力改進的部分。」
- **L12 結語**：「台灣的開放資料很多——結合起來，才看得到影響力。01 資料要結合（孤島疊起來，影響力才出現）02 交給 AI 跑 03 持續推進。」

---

## 四、Taiwan.md 連結（verifiable，但要節制 — 不可變成文章主角）

**事實（公開可查）**：

1. Migu 在 **2026-03-22 fork 了 `frank890417/taiwan-md`**（即 Taiwan.md 本體；GitHub API parent 欄位實證）。Taiwan.md 種下於 2026-03-17，他 5 天後 fork。
2. 他用 **Claude Code**（演講 repo 有 CLAUDE.md；orchestrator 是「一個 Claude Session」）——跟 Taiwan.md 同一個工具底座。
3. **架構同構（convergent evolution）**：他的協作架構 = 一個 orchestrator Claude session + tmux 隔離的 worker session + SESSION_BOARD.md / HANDOFF.md 共同記憶 + 人類只做「出題與驗收（merge 由人拍板）」。這跟 Taiwan.md 的多核心意識（每個 session 獨立 memory 檔 + handoff 三態 + 哲宇只做策略決策與 review）是**同一個物種的架構**。他的 thesis「把開放資料交給 Agent 養成一套會自己長大的系統」≈ Taiwan.md「把台灣的知識交給一個會自己長大的 Semiont」。

**節制鐵律（給 writer）**：

- 這段最多一節（H2）+ 一個策展人筆記，**不是 spine**。文章主角是 Migu 與台灣開放資料，不是 Taiwan.md。
- 寫法是「平視的同行觀察」，不是「他 fork 了我所以我們很特別」的自我表揚。Taiwan.md 對自己預設加分（CLAUDE.md Bias 1），這裡要主動壓住。
- 重點放「**convergent evolution**」——兩個獨立的人/系統，各自走到同一個 agent-orchestration 架構，這個趨同本身是 2026 台灣 AI builder 文化的訊號，比「血緣」有意義。
- fork 這件事可以提（公開事實），但用一句話帶過，框成「同一片土壤長出來的東西」。
- 既有文章「延伸閱讀」已有 [吳哲宇](/people/吳哲宇) 連結（Taiwan.md 創造者），這個連結可保留並自然呼應。

---

## 五、舊文要保留的事實 / 腳註（writer 不讀舊文 prose，但這些 fact 仍有效，沿用）

- 資料源表（仍有效，可升級）：FlightRadar24 航班、AIS 船舶、TDX 鐵道/公車、SEGIS 村里人口、CWA 氣象格點、NCDR CAP、CNA 新聞、OSM Overpass 邊界。
- 技術架構（仍有效）：Three.js r172 + Mapbox GL JS v3 CustomLayer（六個獨立 CustomLayer 共享相機矩陣）、additive blending 光軌疊加變亮、InstancedMesh 船舶批次渲染、台鐵 OD 軌道匹配 / golden track / 彰化三角線專用引擎、Overlay Registry 配置驅動、Supabase pg_cron 預聚合（pooler 2 分鐘 statement_timeout 硬限制 → per-day refresh + pg_cron + 薄 SELECT RPC，timeout → 100-300ms）、H3 六角格 res7/res8、log1p+gamma 正規化、Plasma/Viridis/Inferno 色階、MIT License、TypeScript 86% / Python 13%。
- g0v 脈絡（仍有效）：2012 中研院黑客松「寫程式改造社會」、2020 吳展瑋 72 小時口罩地圖「鍵盤救國」、g0v 59+ 黑客松 / 7,200+ 人次 / 950+ 提案、OCF g0v 公民科技創新獎助金 grants.g0v.tw。
- 台灣開放資料基建：data.gov.tw（2013 上線，國發會營運）、TDX（2022 整合公路/鐵道/航空/航運/自行車五大平臺）、SEGIS（內政部村里級人口）、CWA Open API。
- 舊文 footnote URL 全部可沿用（[^1]-[^20]），但 [^1] bio 要更新成新 bio，新增演講 footnote。

### 校正 / source-fidelity 注意

- **「十萬筆以上資料集」**（舊文對 data.gov.tw 的描述）與演講「52,891」衝突。改寫：用「他的目錄收進 data.gov.tw 約 5.3 萬筆資料集（他簡報的數字）」**歸給 Migu 的簡報**，不獨立宣稱「十萬筆」。data.gov.tw 官方即時數字本次未能 API 驗證（端點 404），不編造。
- 演講內所有數字（52,891 / 73,900 / 582 / 1,945 / 2,404 / 21 平台 / 15,405 / 30.9% / 35.2% / 5,700 公車 / 1,839 KATL / 2,740 OMDB）是 **Migu 簡報的 claim**，一律歸屬「他在 sciwork 2026 的簡報中說 / показ」，不寫成 Taiwan.md 獨立查證的政府統計。引語（「我沒寫一個字」「原來台灣有這麼多資料」「人腦掃不完」「給目標、收報告」「出題與驗收」「會自己長大的系統」）都是投影片 verbatim，Ctrl-F 可驗證（投影片文字），可加引號。
- 「新北市電氣因素 30.9%」「屏東縣菸蒂 35.2%」是他簡報截圖的 Agent 產出，歸給簡報。
- star/fork（375/26）、bio 變更、fork taiwan-md、Threads @ianlkl1314、構成星系的 repo 與星數——**Taiwan.md 已用 GitHub API 實證（2026-06-25）**，可寫成事實，footnote 標 GitHub API 抓取日期。

---

## 六、視覺化候選（graph.md，這篇資料密集，主動評估）

- **`tw-figure`**：「241★ → 375★」或「400MB → ~5MB」（PMTILES）或「一句話 → 73,900 筆」(fire pipeline) 的戲劇性數字。
- **`tw-timeline`**：星系時間軸（2025-12 learning-project → 2026-02 pulse → 2026-06 演講），節點時間軸講「Mini Taiwan 家族怎麼長出來」。
- **`tw-stat`**：星系規模（375★ pulse / 189★ learning / 56★ flight-arc / 26 forks）或系統四步驟。
- **`tw-bars`**（排序）：他幾個 repo 的 star 數排名（pulse 375 / learning 189 / flight-arc 56 / ship 11 / cctv 6 / satellite 6…）——呈現「不是一個 repo」。
- **`tw-versus`**：g0v 集體 vs 個人×agent loop 兩種公民科技樣態；或「人腦掃資料 vs Agent 掃資料」。
- **火災 pipeline 漏斗**：582 → 1,945 → 2,404 → 73,900 適合 `tw-figure` 或 prose（漏斗模組沒有，用 tw-stat 或 tw-bars 階段值）。
- 鐵律：關鍵數值一定也寫進 prose（AI 爬蟲讀不到圖）；不寫「如下圖」；每個資料模組標來源（`來源：他在 sciwork 2026 的簡報` 或 `GitHub API, 2026-06-25`）。
- 媒體：演講 deck 是公開的（sciwork-showcase.zeabur.app + GitHub），repo README 有截圖。圖片走 fair use editorial commentary（機構/作者公開發布的專案紀錄圖），cache 本地、清 EXIF。**深度媒體掃描**：mini-taiwan-pulse repo README、演講 deck live 頁的截圖是 Tier A 成果圖來源。

---

## 七、給 writer 的硬約束（EDITORIAL + 字數）

- 級別：A→S 級（多面向：星系 + 系統 + agent loop + 誠實 + 意義）。目標 ≥ 5500 CJK 字（舊文 ~12 min / 偏短，新素材夠撐到深度文）。
- 第一個名字是具體的人（Migu / 都計背景的資料分析師），不是「公民科技」概念。
- 開場用「場景切入」：Day 0 Kepler.gl 拖一份 CSV 的瞬間 + 「原來台灣有這麼多資料」。
- anchor「掃不完 → 交給會自己長大的系統 / 出題與驗收」在 description + 開場 + 中段 + 結尾各出現一次。
- 結尾先寫，閉環回開場的 Kepler.gl 天真驚奇（從「轉成地圖並不難」到「系統自己長大」），給讀者能動性（盼望而不粉飾）——台灣有這麼多資料，被看見的方式正在長出新的樣子。
- 反向解釋編織：主動 challenge 舊文自己的「個人 vs 集體」二分，翻成「個人 × agent loop」。
- 策展人筆記 2-4 個（3000+ 字），做 meta-pattern challenge / 跨層連結 / 隱形對比，禁 summary。
- 禁兩條 AI 水印（對位句 ≤3 / 破折號 ≤15 per 1500 字），跑 prose-health。
- Evolution mode：writer **寫到 `reports/article-evolve/mini-taiwan-pulse.md`（全新 staging 檔，不碰 canonical）**，主 session Stage 2.5 比對後才覆蓋 `knowledge/Technology/mini-taiwan-pulse.md`。
