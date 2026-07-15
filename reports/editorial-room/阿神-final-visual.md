---
slug: 阿神
room: final-visual
stage: 3.6
date: 2026-07-15
verdict: PASS
rounds: 3
article: knowledge/People/阿神.md
projection: reports/article-projection/阿神.md
---

# 阿神 — Stage 3.6 最終視覺同步審稿

## Round 3 verdict（最新版）

**PASS**。

Round 2 的錯誤「羽毛怎麼了」縮圖已刪除；替代檔 `public/article-images/people/ashan-stops-daily-upload-2021.webp` 與正文 L74–78、圖片來源 L147、research manifest 及 projection 媒體規格全部一致。**殘餘 hard fixes：無。**

### 新圖逐像素驗收

| 核對層       | 實際 pixels                                                                                                              | 正文／規格                                                                                  | 裁決     |
| ------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------- | -------- |
| 左側人物     | 戴灰色口罩、披淺棕外套的阿神面對鏡頭                                                                                     | L74「左側阿神戴口罩面對鏡頭」                                                               | **PASS** |
| 右側貼文     | 顯示 `@Ashan_kouki`、`3月3日`；可見「需要照顧家人和我的身心狀態」「明天開始我會休息一陣子，停止11年來不間斷的日…」等文字 | L74「右側是他宣布停止十一年日更的推特貼文」；L78 引述停止日更並保留照顧家人／身心壓力的邊界 | **PASS** |
| 右下插畫     | 夜色候車亭、長椅與站在亭內的黃色頭髮角色                                                                                 | L74／L76「候車亭插畫」                                                                      | **PASS** |
| 敘事位置     | 圖放在平台勞動與本人公開轉折段末，後接貼文原句，再進入 Q&A 分工與兩次退休的區分                                          | projection L110 指定 2021 停止十一年日更的本人推特圖；沒有帶入羽毛或其他私領域旁支          | **PASS** |
| alt          | 描述左人、右貼文、候車亭三個主要視覺區塊，未把 caption 的評論句複製成 alt                                                | L74，長度與內容符合畫面描述要求                                                             | **PASS** |
| caption      | 明記 2021 年 3 月、停日更貼文的三部分構圖，credit 為阿神 Twitter，並透明說明由 DailyView 保存                            | L76；沒有把畫面外推成永久離場或醫療診斷                                                     | **PASS** |
| source／授權 | 圖片來源 L147 連到保存該圖的 DailyView 單篇報導；research manifest L308 同步標示阿神 Twitter／DailyView／fair use        | 精確可追溯，沒有冒稱 CC 或公有領域                                                          | **PASS** |
| 實檔健康     | VP8 WebP，940×650，71 KB，aspect 1.446                                                                                   | inline 護欄 0.75–2.5、400 KB 建議上限內                                                     | **PASS** |

### Round 3 全媒體終驗

- **Hero**：`ashan-2026-return-minecraft.webp` 仍準確承載 2026 主頻道復更；frontmatter `imageAlt` 與 pixels 一致，template 以 `frontmatter.imageAlt || title` 渲染。
- **唯一 iframe**：`60n6gPUEl7s` 貼著開場反證，L42 caption 明確限定「新片不等於固定排程恢復」；沒有第二支 iframe 或相鄰重複縮圖。
- **2021 停日更圖**：新 Twitter／DailyView 圖通過上述逐像素驗收。
- **CAPSULE 圖**：貼著 2021 停日更後仍持續公開工作的節點，alt、caption、精確文章來源與 fair-use label 齊全。
- **`tw-timeline`**：標題為「三個節點，三種工作狀態」，2021／2023／2026 三列與來源列正確，`viz-health` PASS。
- **搞神馬圖**：貼著共同節目 2026 仍更新的敘事，alt 描述實際縮圖，caption 與圖片來源均連 `CAOpagY34UI` 精確影片。
- **視覺節奏**：hero → 主頻道 iframe → 停日更貼文 → CAPSULE → timeline → 搞神馬；媒體之間有 prose 緩衝，沒有裝飾性堆疊或同證據重播。
- **密度**：4,500 CJK、6 visual（hero 1 + inline 3 + iframe 1 + timeline 1）＝約 **1.33/1k**，落在 1.2–2.0 健康帶。

### Round 3 gate

- `python3.11 scripts/tools/article-health.py knowledge/People/阿神.md --profile=rewrite-stage-4`：hard=0、warn=0；`image-health`、`paragraph-rhythm`、`media-richness`、`viz-health` 全過。
- 四張 `ashan-*.webp` 均存在，無外部 hot-link；1280×720／1262×708／940×650，71–150 KB，aspect 全在 hero／inline 護欄內。
- projection L110、research manifest L307–310、正文四張圖與一支 iframe 已同步。

### Round 3 殘餘 hard fixes

**無。准予 Stage 3.6 視覺同步 PASS。**

非阻擋 polish 沿用 Round 2 建議：L92 CAPSULE alt 可把「右側四名大人與孩童」再精確成「右側兩名成人與兩名孩童」；這不影響目前畫面辨識、來源或敘事對位。

---

## Round 2 verdict（歷史紀錄）

**REVISE**。

Round 1 的重複搞神馬 iframe、inline alt／caption、精確來源、timeline 標題與 hero alt fallback 均已修正；媒體數量與密度也已回到健康帶。Round 2 剩下一個會誤導讀者的實檔級 hard blocker：

- `knowledge/People/阿神.md:76-78` 使用的 `ashan-leaves-daily-youtube-2021.webp` **不是 alt／caption 所描述的畫面**。實檔中央是流淚的阿神，左右是兩個 Minecraft 角色，畫面文字為「全真心話」「正式回應」「羽毛」「怎麼了」「阿神」；圖上沒有「最後 Q&A」，也沒有「退出職業生涯」。現有 alt 與 caption 因此把一張視覺上指向「羽毛怎麼了」的縮圖誤寫成停止日更證據，還把「退出 YouTube 職業生涯」說成直接寫在縮圖上。

這不是只改 alt 就能通過的問題。若忠實描述現有畫面，它會把投影藍圖已排除的私人／旁支爭議帶回文章，且無法替 L64–80 的平台勞動與停止日更敘事提供視覺證據；必須**換成真正呈現 2021 退休／停止日更／Q&A 的官方縮圖或其他精確 scene visual**。

### Round 2 修正驗收

| Round 1 項目                       | 最新狀態                   | 證據                                                                                                           |
| ---------------------------------- | -------------------------- | -------------------------------------------------------------------------------------------------------------- | --- | ------ |
| 搞神馬 iframe 與同支縮圖相鄰重複   | **已修**                   | 正文只剩主頻道 `60n6gPUEl7s` 一支 iframe；搞神馬只留 L120 靜態縮圖                                             |
| 主頻道 iframe 缺 caption           | **已修**                   | L42 已有 narrative caption，並清楚限定「新片不等於固定排程恢復」                                               |
| CAPSULE 圖 alt／caption 不描述實檔 | **已修**                   | L88–90 已描述多人合成構圖並附 CAPSULE 精確來源                                                                 |
| 搞神馬 alt／caption／source 不精確 | **已修**                   | L120–122、L152 已連到 `CAOpagY34UI` 單支官方影片                                                               |
| timeline 把 2026 稱作第三次宣告    | **已修**                   | L101 改為「三個節點，三種工作狀態」；來源列仍在 L105                                                           |
| hero 使用文章 title 當 alt         | **已修**                   | 正文 L15 有 `imageAlt`；`src/templates/article.template.astro:355` 已為 `frontmatter.imageAlt                  |     | title` |
| 刪 iframe 後媒體密度不足           | **數量已修，素材選擇未過** | 4,511 CJK、6 visual（hero 1 + inline 3 + iframe 1 + timeline 1）＝約 **1.33/1k**；但新增 visual 實檔與文字不符 |

### Round 2 殘餘 hard fixes

1. **重新入庫／替換 L76 的 2021 scene visual**：新圖必須在像素層直接對應「停止日更、退出 YouTube 正職或退休 Q&A」，不得出現「羽毛怎麼了」這條本文未講、投影不收的旁支。不要把現有檔案只改名或只改 alt。
2. **替換後同步 L76 alt、L78 caption、L151 圖片來源**：alt 必須描述新檔實際可見人物／文字／構圖；caption 只陳述畫面與相鄰 L64–80 敘事真正支持的關係；圖片來源連到產生該縮圖的精確官方單支影片。
3. **維持 6 visual 或等值補位**：直接刪除 L76 圖而不補，會降成 5 visual／約 **1.11/1k**，低於 1.2 floor。替代圖應留在 L64–80 的長段落尾端，現有媒體間隔已合格。

### Round 2 非阻擋 polish

- L88 alt 的「右側四名大人與孩童」可再明確成「右側兩名成人與兩名孩童」，避免被讀成四名成人之外另有孩童；目前已比 Round 1 準確，這項不單獨擋 ship。
- L149 的「Hero 與作品縮圖」可縮成「Hero 縮圖」；目前同一素材只作 hero，文字略顯重複但不造成來源錯誤。

### Round 2 gate

- `python3.11 scripts/tools/article-health.py knowledge/People/阿神.md --profile=rewrite-stage-4`：hard=0、warn=0；4,511 CJK；3 inline + 1 hero；1 iframe；`viz-health` PASS。
- 四張實檔均存在：1280×720／1262×708，118–150 KB，aspect 1.778／1.782，全部通過 hero／inline 護欄。
- 視覺節奏：hero → 主頻道 iframe → 2021 scene → CAPSULE scene → timeline → 搞神馬 scene；除錯圖本身外，沒有相鄰媒體堆疊，段落間隔與 narrative arc 合格。
- 自動 gate 仍無法核對 alt/caption 是否描述實際 pixels，因此 profile 全綠不覆蓋本輪人工 **REVISE**。

**Round 2 改判 PASS 的唯一必要條件**：替換 `ashan-leaves-daily-youtube-2021.webp` 為真正對應 2021 停止日更／退出正職的官方 scene visual，並同步精確 alt、caption、單支來源；其餘 Round 1 hard fixes 已關閉。

---

## Round 1 verdict（歷史紀錄）

**REVISE**。

三張實檔都存在、尺寸與 aspect 合格；hero、2021 人物節點、`tw-timeline` 與主頻道 iframe 都貼著敘事。阻擋 ship 的問題集中在兩處：

1. `knowledge/People/阿神.md:116-122` 把「搞神馬」同一支 2026-07-15 影片的 iframe 與縮圖相鄰堆疊，沒有 2–3 段 prose 間隔；兩個 visual 傳達完全相同的證據。
2. 兩張 inline 圖的 alt 都沒有描述實際畫面，caption 也沒有依 Stage 4 格式提供可點的精確來源；其中 CAPSULE 圖實際是多人合成照，不是 alt 所稱的單一「阿神公開形象照」。

此外，投影藍圖 `reports/article-projection/阿神.md:110` 明定「只嵌入 2026 主頻道新片」，正文卻多嵌一支搞神馬影片，屬規格偏離。

## 逐項核對

| 媒體                                    |            正文位置 | 敘事對位                                                                                                                                                                          | 實檔／aspect                                                              | alt、caption、source、授權                                                                                                      | 裁決                                    |
| --------------------------------------- | ------------------: | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------- |
| Hero `ashan-2026-return-minecraft.webp` | L14–17；首節 L29–43 | 直接承載「2023 永久停更未成為永久離場」；與 L31–41 同支影片，角色不同：hero 建立視覺認知，iframe 提供一手影像證據。這是投影明定的受控重複，可留。                                 | 1280×720，1.778，150 KB；hero 0.9–2.0 內。畫面為 Minecraft 偽人影片縮圖。 | credit、fair-use label、精確影片 URL 齊全。文章模板目前以文章 title 當 hero alt，並非畫面描述。                                 | **REVISE alt；其餘 PASS**               |
| 主頻道 iframe `60n6gPUEl7s`             |              L37–41 | 緊接首頁新片論證，後文主動限定「只證明 2026-07-14 有新長片」，敘事與證據邊界準確。                                                                                                | 16:9 responsive iframe；位置在三段 prose 後，與 hero 不相鄰。             | `title` 可辨識，但缺 Stage 4 要求的 italic caption／官方來源頻道／敘事呼應句。                                                  | **REVISE caption**                      |
| CAPSULE 圖 `ashan-capsule-2021.webp`    |              L82–86 | 放在 2021 停日更節點，功能正確；但圖中除左側阿神外，右側另有四名大人與孩童，現有 alt／caption 把多人合成圖說成單一人物照，會讓螢幕閱讀器使用者與讀者誤判畫面。                    | 1262×708，1.782，71 KB；inline 0.75–2.5 內。                              | 文末有 CAPSULE 原文與 fair-use 說明；caption 無可點來源。alt 少於建議 30–80 字，也沒有描述誰、做什麼、構圖氛圍。                | **REVISE alt + caption**                |
| `tw-timeline`                           |             L96–104 | 三節點精確對應 2021 停日更、2023 宣告主頻道停片、2026 官方頁仍有新片，位置在兩次宣告分析後，確實把「不同賓語」壓成一眼可讀的結構。                                                | `viz-health` PASS；semantic fenced module，非圖片型圖表。                 | L101 已有來源列，符合 graph.md。惟標題「三次宣告」不準：2026 是官方頁狀態／新片證據，不是第三次宣告。                           | **REVISE 標題一詞；其餘 PASS**          |
| 搞神馬 iframe `CAOpagY34UI`             |            L116–118 | 內容與 L114 的 2026-07-15 新片日期相符，但偏離投影「只嵌主頻道新片」。iframe 後立刻接同支影片縮圖，沒有 prose 間隔，形成同證據重播。                                              | 16:9 responsive iframe。                                                  | `title` 可辨識；沒有自己的 italic caption。L122 是緊接圖片的 caption，不能兼任 iframe caption。                                 | **REMOVE / REPLACE**                    |
| 搞神馬圖 `ashan-gaoshenma-2026.webp`    |            L120–124 | 畫面確為阿神、馬田與「菜瓜布甜點／過季商品」影片縮圖，能證明共同節目仍更新；L122 對私交、分工、收益設限，敘事倫理正確。若刪上方重複 iframe，放在 L114 後可自然閉合共同節目 beat。 | 1280×720，1.778，136 KB；inline 0.75–2.5 內。                             | 現有 alt 只寫抽象結論，沒描述畫面；caption 無精確連結。L155 只連頻道首頁，不足以追到這張縮圖，應改連 `CAOpagY34UI` 的單支影片。 | **REVISE alt + caption + exact source** |

## 必改（具體到行）

1. **L116–118 刪除搞神馬 iframe**。它與 L120 圖片是同支影片、同一縮圖、同一證明，且違反媒體不得相鄰堆疊。這也讓正文回到投影 L110「只嵌入 2026 主頻道新片」的規格。

2. **不要只刪而不補 visual**。現況為 4,519 CJK、6 visual（hero 1 + inline 2 + iframe 2 + `tw-timeline` 1），密度約 **1.33/1k**，在 1.2–2.0 健康帶。若只刪搞神馬 iframe，會變 5 visual、約 **1.11/1k**，跌破 floor。應回 Stage 1 媒體 manifest 補一個**不同證據、不同畫面**的 scene visual，優先放在目前長時間無視覺呼吸的 L45–76（十一年日更／平台勞動段），或放一張 2023 宣告的精確來源截圖；不要再用 `CAOpagY34UI` 的任何變體。補圖後仍維持 6 visual、約 1.33/1k。

3. **L82 alt 改成實際畫面描述**，例如：

   `![左側阿神穿灰色西裝調整紅色領結，右側四名大人與孩童在白色背景前合影](/article-images/people/ashan-capsule-2021.webp)`

   不應再用「公開形象照」取代畫面，也不要把多人合成照默認為阿神單人肖像。

4. **L84 caption 改為精確說明合成圖、節點與來源**，例如：

   `_CAPSULE 2021 年人物報導使用的合成形象照；它錨定阿神停止日更後仍持續公開工作的節點，不提供頻道內部分工資訊。Photo: CAPSULE. [Fair use editorial commentary via CAPSULE](https://www.capsuleinc.cc/creators-news-inner/867)._`

5. **L120 alt 改成畫面內容**，例如：

   `![搞神馬縮圖中，金髮阿神與黑髮馬田分站左右，中央是綠色菜瓜布甜點與「過季商品」字樣](/article-images/people/ashan-gaoshenma-2026.webp)`

6. **L122 caption 補精確單支影片來源**，例如：

   `_搞神馬 2026 年 7 月 15 日官方影片縮圖：阿神與馬田共同節目仍在更新；此畫面不支持私交、分工或收益推論。Photo: 搞神馬官方 YouTube. [Fair use editorial commentary via official video](https://www.youtube.com/watch?v=CAOpagY34UI)._`

7. **L155 圖片來源由頻道首頁改成精確影片 URL** `https://www.youtube.com/watch?v=CAOpagY34UI`，標題同步寫「2026 年 7 月 15 日官方影片」。頻道首頁會動態變化，不能精確追溯特定縮圖。

8. **L39 後新增主頻道 iframe caption**，例如：

   `_阿神官方 YouTube 2026 年 7 月 14 日長片：2023 年停片宣告後，主頻道已重新出現錄製影片；它只證明復更，不證明固定排程恢復。_`

9. **L97 `tw-timeline` 標題改成「三個節點，三種工作狀態」**。2026 節點是官方頁面狀態，不是「宣告」；資料列與 L101 來源列可原樣保留。

10. **Hero alt 要在渲染層修正**。`src/templates/article.template.astro:354-355` 目前硬寫 `alt={title}`；即使本文增加 `imageAlt` 也不會生效。應讓模板優先讀 `frontmatter.imageAlt`，並在本文 frontmatter L14 附近新增，例如：

    `imageAlt: 'Minecraft 官方縮圖中央是兩個偽人怪物，左右為阿神與雪兔的方塊角色，標題寫著「麥塊最恐怖偽人」'`

## 授權與來源裁決

- 三張圖的本地 manifest、正文 frontmatter／圖片來源區都一致標為 **Fair use editorial commentary**，沒有宣稱 CC 或公有領域；本輪禁止上網，因此只能確認本地來源鏈與評論用途一致，不能替代人類最終法律判斷。
- Hero 的來源是精確單支影片，合格。
- CAPSULE 圖的來源是精確人物文章，合格；caption 仍須補可點來源。
- 搞神馬圖目前只連頻道首頁，追溯性不足；改為單支影片後才合格。
- 三張圖均為本地 WebP，無 hot-link；150 KB／71 KB／136 KB 均低於 hero 600 KB、inline 400 KB 建議值。

## Gate 記錄

- `python3.11 scripts/tools/article-health.py knowledge/People/阿神.md --profile=rewrite-stage-4`：hard=0、warn=0；4,519 CJK；2 inline + 1 hero；2 iframe；`viz-health` PASS。
- 實檔：三張皆 VP8 WebP，1280×720／1262×708／1280×720；aspect 1.778／1.782／1.778，全部在護欄內。
- 自動 gate 沒有抓到「同支影片 iframe + 縮圖相鄰」與「alt 描述錯畫面」，因此本報告維持人工 **REVISE**，不能以 profile 全綠覆蓋。

## Re-review 條件

- 搞神馬 iframe 不再與同支縮圖重複；投影恢復為只嵌主頻道新片。
- 補回一個不同 scene visual，使密度維持 ≥1.2/1k，且新媒體有完整來源／授權／alt／caption。
- 兩張 inline 圖與 hero 的 alt 都描述實際畫面；caption 可追到精確來源。
- `tw-timeline` 不再把 2026 官方頁狀態稱作「宣告」。

達成以上四項後可改判 **PASS**。
