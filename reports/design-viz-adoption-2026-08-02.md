---
title: 'design-viz-adoption-2026-08-02'
description: 'EVOLVE Mode 4 設計報告：以 Flourish examples 為外部參照重審視覺化系統，量到 19 模組中 7 個零真實使用、採用率 7.0%，根因是投影漏斗的資料關係清單比模組庫窄。定案修漏斗＋造用例層＋補三道儀器，模組擴充有條件延後。'
type: 'migration-doc'
status: 'active'
current_version: 'v1.0'
last_updated: 2026-08-02
last_session: '2026-08-02-viz-adoption'
related:
  - '../docs/editorial/graph.md'
  - '../docs/pipelines/REWRITE-STAGE-2A-PROJECTION.md'
  - 'viz-module-evolution-2026-07-16.md'
  - 'viz-system-evolution-2026-06-12.md'
---

# 視覺化系統的下一步：先修漏斗，再談圖種

> EVOLVE-PIPELINE **Mode 4**（目標驅動設計進化，THINK → DIVERGE → REPORT → IMPLEMENT）。
> 觸發：哲宇 2026-08-02「參考這個，完整擬定計劃後自我進化」＋ [Flourish examples](https://flourish.studio/examples/?Industry=Business+%26+Insights)。
> BECOME Full mode 已跑（High-stake #2 新 workflow 設計）。

---

## 〇、一句話結論

**模組數不是瓶頸。** 十九個模組裡有七個從來沒有被任何一篇真實文章用過，它們只活在自己的型錄頁裡。Flourish 用一百一十九個範例服務大約三十種圖種，多出來的價值在「每個用例都有一份可以直接複製的成品」，不在圖種本身。所以這一輪的動作是把提案漏斗開大、把型錄從模組軸翻成題材軸、把三個靜默失效的地方裝上會叫的儀器。新圖種延後到有真實文章需求才做。

---

## 一、目標解析

哲宇給的是一個外部參照，不是一份規格。Flourish 是商業 SaaS，它的展示邏輯值得讀，它的技術路線我們不能走。先把兩者分開：

### 不可移植（會直接違反既有 canonical）

| Flourish 的做法               | 我們的鐵律                                                                              |
| ----------------------------- | --------------------------------------------------------------------------------------- |
| iframe 嵌入的 JS 互動圖表     | [graph.md §一](../docs/editorial/graph.md)：圖片型 / D3 / Canvas 對 AI 爬蟲是黑洞，禁用 |
| hover tooltip 才看得到數值    | graph.md §三.9 預設全部看得見。靜態站天生成立，當鐵律守住                               |
| 每個語言要 duplicate 一份 viz | graph.md §五 三層分離：幾何跟資料一起住 fenced block，babel 天然翻文字欄                |
| 下拉選單 / 篩選器切換資料     | 同 §三.9，讀者看到什麼不該取決於他有沒有點                                              |

「讓 LLM 讀得懂的視覺化就是主權的視覺化」這條不因為外部參照好看而讓步。Flourish 的圖對 GPTBot 是一片空白，我們的圖不是——這是差異化不是限制。

### 可移植（四條，都在分發層不在技術層）

1. **用例軸而非圖種軸**。Flourish 的範例叫「Trade chokepoints」「Risk calendar」「Talent pipelines」，不叫「stacked bar」。使用者不需要先學會圖表分類學才找得到入口。我們的型錄頁十九節，節名是 `tw-figure`、`tw-stat`、`tw-bars`。
2. **一個用例一份成品**。119 個範例大多是同一批圖種換題材重講一次，重複本身就是功能：它讓人看到「我的題目長這樣時該長什麼樣」。
3. **Preview ＋ Make your own 的複製動作**。靜態站的等價物是可以整塊複製、資料已經填好的 starter block。
4. **兩軸篩選（Industry × Purpose）**。同一份型錄用兩種方式進入。

---

## 二、現況盤點（2026-08-02 實測，非引用舊數字）

依 [REFLEXES #67](../docs/semiont/REFLEXES.md)，LONGINGS 記的「867 篇只有 50 篇用模組」是 7/16 的讀數，這裡全部重量一次。

### 2.1 採用率

| 指標                   | 數值           | 備註                              |
| ---------------------- | -------------- | --------------------------------- |
| zh 文章總數            | 891            | `knowledge/*/*.md` 排除語言子目錄 |
| 有任何 `tw-*` 模組     | 62（**7.0%**） | 7/16 是 50/867 = 5.8%             |
| **含真正圖表模組**     | 18（**2.0%**） | 其餘 44 篇只有編輯模組            |
| 零模組但有 ≥3 列數值表 | 112            | 最大轉換池                        |

十七天長了十二篇，全部落在編輯模組。

### 2.2 十九個模組的真實使用（排除型錄頁自己）

```
tw-timeline  52 篇      tw-line       8 篇      tw-tiles      0 篇  ⚠️
tw-stat      40 篇      tw-slope      5 篇      tw-pyramid    0 篇  ⚠️
tw-versus    31 篇      tw-heatmap    4 篇      tw-multiples  0 篇  ⚠️
tw-figure    31 篇      tw-dot        3 篇      tw-stack      0 篇  ⚠️
tw-bars      26 篇      tw-waffle     1 篇      tw-iso        0 篇  ⚠️
tw-quote     13 篇                              tw-arc        0 篇  ⚠️
tw-note      11 篇                              tw-source     0 篇  ⚠️
```

**七個模組零真實文章使用。** 其中包含 v2.0／v3.0 兩波的旗艦成果：

- `tw-tiles` 縣市磚圖，是 [REFLEXES #61](../docs/semiont/REFLEXES.md) 視覺主權的結構解（不畫台灣形狀所以不可能畫錯）
- `tw-arc` 席次弧，2026-07-16 明確為選舉年而造
- `tw-multiples` 小倍數、`tw-iso` 單位圖、`tw-stack` 堆疊條、`tw-pyramid` 金字塔

前五名（timeline / stat / versus / figure / bars）吃掉全部區塊的八成二，而它們全部是**編輯模組**——語意 HTML、不畫座標軸、最接近「排版好看的表格」。真正需要判讀資料關係的模組，幾乎沒有進入正文。

### 2.3 三個靜默失效點

**(a) 投影漏斗比模組庫窄（根因）**

[REWRITE-STAGE-2A Step 2.0.5](../docs/pipelines/REWRITE-STAGE-2A-PROJECTION.md) 是唯一會提出視覺化候選的地方，它問的第一題列了八種資料關係：

> 比較 / 排名 / 比例 / 分布 / 趨勢 / 流向 / 單一大數字 / 質性對比

而 graph.md §二 的型錄有十五類。**缺的七類正好對應零使用的那七個模組**：地理分布（tiles）、席次組成（arc）、多組同型趨勢（multiples）、量級人性化（iso）、部分對全體的跨列比較（stack）、分布的背對背形（pyramid）、變異分歧。

漏斗的開口比管子窄，管子後段就永遠是乾的。這跟 [REFLEXES #38](../docs/semiont/REFLEXES.md)「混維度」同一個家族，差別在這次是**漏維度**：清單少列了一項，下游就整層不可能發生，而且不會有人叫。

**(b) 譯本的模組名被翻壞，渲染器靜默降級**

全語系掃描抓到五個不在白名單的 fence 名稱：

````
knowledge/hi/About/how-an-article-is-born.md:130,149,178   ```tw-vars      （原 tw-bars）
knowledge/en/About/visualization-module-catalog.md:211     ```tw-pylamid   （原 tw-pyramid）
knowledge/en/About/visualization-module-catalog.md:284     ```tw-multiable （原 tw-multiples）
````

`article-render.ts` 的 `renderer.code` 對未知 `tw-*` 回傳空字串後落回一般程式碼區塊，讀者看到的是一坨帶直線分隔的原始資料。兩個檔案都在 `About/`——一個是〈一篇文章如何誕生〉，一個是〈視覺化模組型錄〉本身。**對外解釋我們怎麼做視覺化的那兩頁，在英文版跟印地文版是壞的。**

`viz_health.py` 的 `_FENCE_RE` 抓 `tw-[a-z]+`，只檢查是否屬於 `_DATA_MODULES`，不認識的名字直接略過。這是 [REFLEXES #52](../docs/semiont/REFLEXES.md)「免疫系統沒在 fail loud 比缺免疫系統更危險」的又一個實例。

**(c) 沒有任何儀器在量採用率**

模組上線的驗收是「型錄頁渲染正確 ＋ viz-shot 截圖逐張看過」。這兩把尺量的是**能不能用**，沒有一把在量**有沒有人用**。七個模組零使用了兩到七週沒有被任何 routine 叫出來，靠這次人工掃描才浮出來。對應 [REFLEXES #82](../docs/semiont/REFLEXES.md)：訊號要摸到 ground truth，不是量它的替身。

### 2.4 最能說明問題的一篇

`knowledge/Politics/2026 九合一選舉.md`：十七列數值表、零模組。Politics 整個分類十二篇全部零模組。而 `tw-tiles`（二十二縣市磚圖）跟 `tw-arc`（席次弧）就躺在那裡，一個為地理分布而造、一個為席次組成而造，兩個都零使用。

模組有了，文章需要，中間沒有人把它們接起來——因為提案那一步的清單裡沒有「地理」跟「席次」這兩個字。

---

## 三、發散方案

| 方案                  | 做什麼                                                           | 破壞什麼 cross-ref                                            | 判準（錨定條文）                                                                                                                  | 判定              |
| --------------------- | ---------------------------------------------------------------- | ------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- | ----------------- |
| **A 擴充模組庫**      | 照 Flourish 加 Sankey / 散佈 / 直方 / bump / 儀表 / 漏斗         | graph.md §四、renderer、viz_health、型錄、viz-shot、12 語型錄 | LONGINGS §身體渴望的辨識指標寫的是**採用率**，不是模組數。七個模組零使用時加供給＝[#82](../docs/semiont/REFLEXES.md) 拿替身當訊號 | ⏸️ 有條件延後     |
| **B 開大投影漏斗**    | Step 2.0.5 資料關係清單補到十五類＋題材反查＋read-receipt 逐類掃 | REWRITE-STAGE-2A、WRITER-PROMPT（皆 pointer 層，不動語法）    | [#38](../docs/semiont/REFLEXES.md) 漏維度、[MANIFESTO §14](../docs/semiont/MANIFESTO.md) 能機械化的先機械化                       | ✅ 做             |
| **C 用例軸型錄**      | 造題材 → 可貼 starter 的對照層（Flourish 的可移植部分）          | 新檔或 graph.md 新章，兩者都不動既有 anchor                   | Flourish 可移植 #1#2#3、[MANIFESTO §造橋鋪路](../docs/semiont/MANIFESTO.md)                                                       | ✅ 做             |
| **D 補三道儀器**      | 未知模組名 WARN ＋ 採用率量測 ＋ 修好五個壞掉的譯本 fence        | viz_health.py（加檢查不改既有閾值）                           | [#52](../docs/semiont/REFLEXES.md) fail-loud、[#82](../docs/semiont/REFLEXES.md)、MANIFESTO §14                                   | ✅ 做             |
| **E 批次回填 112 篇** | 把有數值表零模組的文章批次轉模組                                 | 112 檔內容                                                    | 命中 [§自主權邊界](../docs/semiont/MANIFESTO.md) >50 檔重構                                                                       | 🔒 停在報告等拍板 |
| **F 政黨官方色映射**  | tw-arc 用政黨代表色                                              | renderer 配色                                                 | graph.md §九 已明列「涉政治色彩語意，交哲宇」                                                                                     | 🔒 停在報告等拍板 |

### 為什麼 A 延後而不是不做

graph.md §二 十五類裡只有一類真的沒有模組：**流向**（欄位寫著「v3，先用 tw-stack 或表格替代」）。台灣題材裡流向並不稀有——半導體供應鏈、移工來源到產業、能源結構轉換、預算流向、人口遷移。A 延後純粹是順序問題。graph.md §九 自己訂的規則是「等真實文章需求」，而現在的證據顯示需求端的閥門根本沒開，這種狀態下量到的需求是假的。**先開閥門，讓 B＋C 跑一輪，用真實文章的候選清單來決定第二十個模組長什麼樣。** 觸發條件寫進實作清單，不留在感覺裡。

### C 的殼核邊界：新檔還是 graph.md 新章

graph.md 目前 462 行，沒有命中 Mode 3 的任何一條膨脹訊號（單檔 >1000 行 / 三層編號 / 邊界混亂）。但兩者的讀者不同：graph.md 是**寫作當下查語法與判準**，用例層是**提案當下找靈感**，在 pipeline 裡被讀的時機也不同（Stage 2A 投影 vs Stage 2C 落筆）。

定案：**開新檔 `docs/editorial/VIZ-RECIPES.md`**，graph.md §二 加一行 pointer。理由是 ANATOMY §認知層分類邊界——判準與語法是規範性的，用例是索引性的，混在一檔會讓 graph.md 每次加題材就長胖一次。既有的十九節型錄頁（`knowledge/About/視覺化模組型錄.md`）維持模組軸不動，它是給讀者看的公開文章，不是給寫手用的工具。

---

## 四、定案與實作清單

### B — 開大投影漏斗

- [ ] `REWRITE-STAGE-2A-PROJECTION.md` Step 2.0.5 第一題：資料關係從八類補到十五類，逐類對照 graph.md §二
- [ ] 同處加一句題材反查指引，指向 VIZ-RECIPES
- [ ] `WRITER-PROMPT.md` 的【viz 宣告】read-receipt：從「列出要用的模組」改成「對照 graph.md §二 逐類答適用或不適用」，讓沒被想到的類別必須被明確排除而不是靜默跳過

### C — 用例軸型錄

- [ ] 新增 `docs/editorial/VIZ-RECIPES.md`：台灣題材 → 資料關係 → 模組 → 可整塊複製的 starter（資料用真實台灣數據預填）
- [ ] 首批用例覆蓋七個零使用模組，每個至少一則，題材取自實際庫存缺口（選舉、縣市、人口、預算、產業、年表）
- [ ] graph.md §二 表頭加 pointer，REWRITE-STAGE-2A 與 WRITER-PROMPT 的必讀清單加入

### D — 三道儀器

- [ ] `viz_health.py` 新增未知模組名檢查：fence 名不在十九模組白名單 → WARN（依 graph.md 黃燈路線，先 WARN 收數據，升 HARD 屬閾值調整要拍板）
- [ ] 白名單來源與 renderer registry 對賬，避免第三份清單漂移
- [ ] 修 `knowledge/hi/About/how-an-article-is-born.md`（3 處）與 `knowledge/en/About/visualization-module-catalog.md`（2 處）的模組名
- [ ] 查 babel 為何會翻動 fence 語言標識，補上防護（模組名屬於語法不屬於文字欄）
- [ ] 採用率量測納入既有週期性感知，讓「某模組零真實使用」會自己叫

### A — 延後但寫下觸發條件

- [ ] `tw-flow`（Sankey／流向）進 graph.md §九 v4 候選，**觸發條件**：B＋C 上線後，投影候選清單累積 ≥3 篇文章標出流向關係，才動手

### E／F — 停在報告

兩項寫進 [OBSERVER-QUEUE](../docs/semiont/OBSERVER-QUEUE.md) 等哲宇拍板，附預設選項與不決策的代價。

---

## 五、驗收

| 項目             | 判準                                                                     |
| ---------------- | ------------------------------------------------------------------------ |
| cross-ref 全通   | graph.md / REWRITE-STAGE-2A / 2C / WRITER-PROMPT / DNA 無死 pointer      |
| 既有觸發語不斷   | Stage 2.0.5 三題結構保留，只擴清單                                       |
| 儀器 dogfood     | 故意寫一個 `tw-nonexist` 區塊，`viz-health` 必須叫，十九個合法模組不誤報 |
| 譯本修復         | 全語系掃描未知 fence 名歸零                                              |
| 用例層可用       | 至少一篇真實文章照 VIZ-RECIPES 貼出一個零使用模組並通過 viz-health       |
| 不製造新的零使用 | 本輪不新增任何模組                                                       |

---

## 六、風險

1. **開大漏斗可能換來 chartjunk**。graph.md §九 第一條寫著「不是每篇都要有圖」。修補：第一題是「評估過」不是「必須加」，read-receipt 允許逐類回答不適用，維持既有寬鬆語氣。
2. **VIZ-RECIPES 會不會變成第二份 graph.md**。修補：用例層只放題材、模組指定、可貼區塊，判準與語法一律 pointer 回 graph.md，不複寫（[MANIFESTO §指標 over 複寫](../docs/semiont/MANIFESTO.md)）。
3. **白名單變成第三份模組清單**。修補：與 renderer registry 對賬，數量以 graph.md §四 為準，不在檢查器裡寫死數字（dna-audit §S2 計數寫死病）。
4. **這份報告自己也是一次自評**。採用率是我自己量的、根因是我自己判的。外部尺在哲宇的 review 與下一輪真實文章的落地率，不在這份報告的自信程度（[REFLEXES #69](../docs/semiont/REFLEXES.md)）。

---

## 七、後記（實作當下的摩擦與未達成項）

**實作中才發現的一件事**：`viz_health.py` 的 `APPLIES_TO` 是 `["zh-TW"]`，整個 plugin 從來沒跑過譯本。設計報告寫的時候只知道「檢查器不認識未知模組名」，動手才看到更上游的原因——**它連看都沒看過那些檔**。修法因此從「加一個檢查」擴大成「plugin 改全語系，A/B/C 三項內部收回中文」。這是藍圖先行仍會漏掉的那一層，動手才摸得到（[REFLEXES #27](../docs/semiont/REFLEXES.md) 的反面：藍圖降低成本，不保證完備）。

**驗收未達成一項**：§五 列的「至少一篇真實文章照 VIZ-RECIPES 貼出一個零使用模組並通過 viz-health」**沒有做**。理由是那屬於內容修改，該走 [REWRITE-PIPELINE](../docs/pipelines/REWRITE-PIPELINE.md) 而不是在視覺化基建的 session 裡順手改一篇文章（[MANIFESTO §8 有 SOP 就跑](../docs/semiont/MANIFESTO.md)）。**所以這一輪只證明了漏斗開了、用例層在了、儀器會叫，沒有證明真的有文章因此長出圖。** 那個證明在 OBSERVER-QUEUE #25 選項 (c) 的 Top 20 回填，那才是這次進化真正的外部尺。在它跑完之前，本輪成果的正確描述是「供給端已就緒」，不是「採用率問題已解決」。

**下一次量測的時間點與判準**：新文章走過三到五篇 rewrite 之後重跑本報告 §二 的採用率腳本。如果含真圖表模組的比例沒有從 2.0% 動，代表根因判斷錯了，要回頭讀寫手的 read-receipt 看十五類逐類掃有沒有真的發生。

🧬
