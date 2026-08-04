# 語言分支樹 /fork-graph/ 進化設計報告（EVOLVE Mode 4）

> 哲宇 /goal（2026-08-04）：「完整深度研究＋思考進化 https://taiwan.md/fork-graph/ ，
> 讓這個頁面對所有人有更多意義與呈現，深度研究與發想後寫報告然後實作。」
>
> Mode 4 四相：THINK → DIVERGE → REPORT（本檔）→ IMPLEMENT。
> 同 session 上游：支語深度研究（reports/terminology-zhiyu-deep-research-2026-08-04.md）——
> 本頁進化直接吃那輪的三波世代模型與 49 條新詞條。

---

## §1 THINK：現況盤點

### 1.1 P0：圖壞了將近四個月，沒有任何儀器叫

live 頁面的分支圖是**空白的**。根因：`drawGraph()` 開頭
`document.querySelector('.fork-graph-wrap')` 找不到元素直接 return——2026-04-10
Phase 6 Tailwind 遷移（`03e03a8cb`）把 wrapper 的 scoped class 改成 utility class 時，
`.fork-graph-wrap` 這個 JS 依賴的 hook 被一併刪除。從那天到今天，頁面 header、legend、
footer 全部正常渲染，唯獨核心的圖是一個空灰框。

這是「儀器只問有沒有渲染、沒問長什麼樣」的又一個實例（同型：viz 引語卡壞 6 天驗證全綠，
REFLEXES #69 家族）。頁面被 Footer 全站鏈入＋terminology index／converter／speciation
四處引用，等於全站每一頁的頁腳都連向一張空白圖。

### 1.2 資料層：10 個詞 hardcode，與 2,383 條詞庫完全脫鉤

10 個代表詞（含 taiwan/china/type/note/年份）直接寫死在 .astro frontmatter。同站的
`data/terminology/` 有 2,383 條 YAML（本日剛 +49 條帶完整詞源敘事），其中 **186 條有
`fork_point`（格式 `~1950s`／`~1974`，可 parse 成年份）**、509 條有 origin 敘事。
頁面與詞庫是兩套真相：詞庫今天新增了鬆弛感／搭子／社死這批 2020s 世代詞，分支樹的
時間軸右端永遠停在 2020 的「人設」。knowledge/ → src/content 的 SSOT 鐵律在這頁的
對應物（data/terminology → 頁面資料）從未建立。

### 1.3 呈現層缺口

- **手機／觸控無內容**：唯一的資訊深度在 hover tooltip，觸控裝置摸不到；圖橫向 900px
  min-width 靠捲動。
- **節點是死的**：不連 `/terminology/{id}` per-term 頁（2,300 個 SEO 落地頁是現成的
  深度層，卻沒有從全景圖進去的路）。
- **Legend 有 D 型（台客語底層）但圖上零個例**——說明書列了六種分歧，圖只畫了四種。
- 詞數 10、跨度停在 2020，「正在分歧」的當下感是空的。

### 1.4 cross-ref 與慣例

引用面：Footer.astro（全站）、terminology/index、terminology/converter、
semiont/speciation。D3 v7 走 CDN 是站上三頁共同慣例（graph.astro／FoodViz 同款），
本次不動（避 scope creep，屬另一個基建題）。

### 1.5 受眾：「對所有人」拆開是誰

| 受眾                                 | 現況給了什麼          | 缺什麼                                         |
| ------------------------------------ | --------------------- | ---------------------------------------------- |
| 一般讀者                             | 10 條線＋hover 小故事 | 故事層太薄；手機上連故事都沒有                 |
| 支語討論者（本日研究證實的活躍社群） | 無                    | 「這個詞什麼時候分歧的」的查詢入口；新世代詞   |
| per-term 頁讀者（SEO 進站主力）      | 無                    | 從單詞到全景、從全景回單詞的雙向路             |
| 教育者／研究者                       | 六類型 legend         | 「滲透在加速嗎」的時間序列證據；可引用的全景圖 |
| 詞庫貢獻者                           | 頁腳一顆貢獻按鈕      | 看見自己的詞條出現在圖上的回饋感               |

---

## §2 DIVERGE：三案與判準

| 案                             | 內容                                                                                                                                  | 意義密度       | 成本 | 風險                                                                                                                          |
| ------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------- | -------------- | ---- | ----------------------------------------------------------------------------------------------------------------------------- |
| **A 修復＋接資料**             | 修 selector；資料 build-time 從詞庫 derive；詞數 10→40；節點連 per-term                                                               | 中             | 低   | 意義升級有限，仍是「一張圖」                                                                                                  |
| **B 三世代敘事策展**（A 全含） | 時間軸三波世代染色＋世代策展短文（吃本日研究）；全庫 186 條 fork_point → 分歧密度曲線（「滲透在加速」的視覺證據）；tap 支援；D 型補例 | 高             | 中   | 頁面變長，需控制策展文密度                                                                                                    |
| **C 全量互動全景**             | 186 條全上時間線＋搜尋＋年代 scrub 動畫＋統計面板                                                                                     | 中（資訊過載） | 高   | 與 /terminology/ index 的瀏覽功能重複（#38 混維度：本頁的獨特值是時間維度，index 的值是瀏覽搜尋）；186 行 × 56px 的圖無人能讀 |

**判準（錨定 canonical）**：

1. MANIFESTO §1 策展式非百科式——精選 40 詞好過全量 186 條 dump，C 案否決的主因。
2. GA4 實證「帶肉才有讀者」（terminology per-term 長尾全由 E 型帶肉條目撐起）——頁面
   要長出故事層，A 案不夠的主因。
3. REFLEXES #21 SSOT——資料必須 derive 自詞庫，三案共識，hardcode 不再擴大。
4. MANIFESTO §14 高儀器化——全部 build-time 生成，不加 runtime 依賴。
5. #38 混維度——時間維度是本頁專屬生態位，瀏覽／搜尋留給 index，不重複造輪。

**定案：B**，外加 C 案中意義密度最高的一項（分歧密度曲線）輕量納入。

---

## §3 定案設計

### 3.1 資訊架構（新頁面五段）

1. **Header**（保留形式，計數改動態：N 個精選詞／跨越 130 年／密度資料 186 條）
2. **精選分支樹**（修復＋擴充）：10→40 詞、六類型全有代表、時間軸右端到 2026
   （鬆弛感／偷感／搭子讓「正在分歧」活起來）；節點 click/tap 開 tooltip＋
   「查看詞條 →」連 per-term 頁；行動裝置 tap 完整可用
3. **分歧密度曲線**（新）：全庫 186 條 fork_point parse 成年代 → per-decade
   stacked 長條（by 六類型配色）。這是「語言滲透的時間形狀」第一次被畫出來——
   1949-1950s 的高峰、2000s 網路時代的第二波、2020s 正在長高的第三波。
   點某年代 → 列出該年代分歧的詞（各連 per-term）
4. **三波世代策展短文**（新，每段 80-120 字）：日源層（含新日源繞道現象：彈幕／佛系
   ／打call 是日本詞經中國二次加工再進台灣——跟便當那代的直接繼承對照）／1949 分流層
   ／網路與短影音層。策展聲音來自本日研究報告，是頁面的「肉」
5. **Legend＋Footer**（保留，legend 每類型加動態計數 badge：D 台客語底層 21 條⋯⋯
   連 terminology index 的類型篩選）

### 3.2 資料機制（SSOT 分工）

```
data/terminology/*.yaml（語言內容 SSOT：display/type/origin 敘事/fork_point）
        +
data/terminology/_fork-graph-featured.yaml（策展層 SSOT：40 詞 id 清單＋
        originYear/forkYear/origin 標籤——時間軸座標詞庫沒有的部分）
        ↓ build-time
scripts/core/generate-fork-graph-data.py（prebuild；parse fork_point、
        merge、驗證 id 存在、輸出計數）
        ↓
src/data/fork-graph.json（gitignored derived，頁面 import）
```

hardcode 資料退場；未來加詞 = 改 featured 清單一行（或純密度層自動吸收）。

### 3.3 精選 40 詞清單（六類型 × 三世代）

- **A 日語遺產（老層）**：便當／盒飯、品質／質量、瓦斯／煤氣、歐巴桑／大媽、OK繃／創可貼
- **A 新日源繞道**（本日研究發現的敘事亮點）：彈幕、佛系、打call（日→中→台，
  與老層「日→台直收」對照）
- **B 1949 分流**：軟體／軟件、捷運／地鐵、演算法／算法、雷射／激光、洋芋片／薯片、
  鮭魚／三文魚、計程車／出租車、太空人／宇航員
- **C 網路時代**：影片／視頻、按讚／點贊、網紅、外送／外賣、行動電源／充電寶、
  取消追蹤／取關、網路霸凌／網暴、螢幕鎖定／鎖屏
- **D 台客語底層**：機車／摩托車（雙層分歧：日治底層＋1949 固化）、尾牙／年會、
  芭樂／番石榴、辦桌／流水席
- **E 正在分歧（2020s 右端）**：擺爛／躺平、內卷、碰瓷、天花板、社死、推坑／安利、
  工具人／舔狗、鬆弛感、搭子／牌咖、偷感
- **F 同詞不同語感**：窩心（方言歧義）、土豆（三方歧義）、估計／立馬（收編爭議）

（實作時以詞庫實際 id 對齊，缺條目者跳過不硬造；最終數以 commit 為準）

### 3.4 驗收（dogfood hard gate）

1. dev server 開 /fork-graph/：圖真的畫出來（不是「code 看起來對」——本頁就是
   死在這種驗收上）
2. 觸控模擬：tap 節點出 tooltip、連結可點進 per-term
3. 密度曲線與詞庫計數對賬（曲線總數 == parse 成功的 fork_point 條數）
4. build 全綠（prebuild script 進 package.json、gitignored derived 不進 git）
5. Footer 等四處既有入口連結不變（URL 不動）

### 3.5 風險

- 策展文過長壓過圖 → 每段硬上限 120 字
- fork_point parse 失敗率未知 → script 印 parse 統計，失敗條目列 stderr 不進資料
- 40 詞的 originYear/forkYear 是策展判斷 → featured 檔每條留 note 欄記依據，
  錯了可單條修

---

_v1.0 | 2026-08-04 | session 支語研究（同 session 第二個 goal）_
_Mode 4：THINK（P0 bug 取證＋資料脫鉤診斷＋五受眾拆解）→ DIVERGE（三案＋五判準）→
定案 B＋密度曲線 → IMPLEMENT 清單見 §3。自主權檢查：單頁＋新 build script＋curation
單檔，內部操作，哲宇 goal 明確授權。_
