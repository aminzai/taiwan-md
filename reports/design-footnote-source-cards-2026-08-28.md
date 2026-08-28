# 設計報告：腳註即時來源卡 — 把 17,113 條引用從文末搬到讀者的游標旁

> 2026-08-28 footnote-cards session（EVOLVE-PIPELINE Mode 4：THINK → DIVERGE → REPORT → IMPLEMENT）
> 觸發：哲宇 directive。當天與《報導者》交流，對方設計師指出——學術論文式的腳註格式看起來清楚，但讀者想深究時，很少真的會「點下去 → 滑到文末 → 讀完 → 再點連結開新頁」這一整串動作。需求：更直覺的資訊卡呈現腳註內容，以及一個能立刻開啟來源的入口。
> 自主權邊界檢查：不涉政治立場、不動 `knowledge/`、改動檔案 6 個、零刪除。§自主權邊界四紅線零命中 → 報告落檔後直接續跑 IMPLEMENT。

---

## 〇、一句話結論

腳註的資訊住在文末，指向它的記號住在正文——**中間隔著 3 到 25 個螢幕高度**，而只有 12% 的頁面瀏覽會抵達文末那一區。做法是讓 `[n]` 自己把那條腳註帶到讀者眼前：滑過就展開一張含來源標題、網域與說明的卡片，卡片上一顆按鈕直接開新分頁。卡片的內容**不新增第二份資料**，是從頁面上既有的 `<ol class="footnotes">` 即時取出來的。

---

## 一、現況盤點（THINK 相）

### 1.1 引用資產的規模

全站中文文章 1,133 篇，其中 **958 篇（84.6%）有腳註**，腳註定義總數 **17,113 條**，每篇中位數 13 條、平均 17.9 條、最多 92 條（〈楊德昌〉）。

腳註定義的形狀（全站 17,132 條定義掃描）：

| 形狀                                              | 條數   | 佔比  | 卡片能給什麼           |
| ------------------------------------------------- | ------ | ----- | ---------------------- |
| `[標題](網址) — 說明`（含 `(<網址>)` 角括號寫法） | 16,133 | 94.2% | 標題＋網域＋說明＋開啟 |
| 純網址（無 markdown 連結）                        | 383    | 2.2%  | 網域＋全文＋開啟       |
| 完全沒有網址                                      | 356    | 2.1%  | 全文（不顯示開啟鍵）   |
| 連結不在開頭                                      | 260    | 1.5%  | 全文＋第一個連結       |

引用最多的來源網域前六名：`zh.wikipedia.org`（1,704）、`cna.com.tw`（549）、`en.wikipedia.org`（254）、`news.ltn.com.tw`（251）、`udn.com`（241）、`twreporter.org`（237）。《報導者》本身就是站上第六大引用來源，這次的建議算是他們自己的稿子在替自己說話。

### 1.2 距離：實測

在 1280×900 的視窗量「從 `[n]` 記號到對應腳註定義」的捲動距離中位數：

| 文章                   | 腳註數 | 中位距離（螢幕高） | 最遠 |
| ---------------------- | ------ | ------------------ | ---- |
| 〈中元節〉             | 8      | 2.9                | —    |
| 〈咖波〉               | 18     | 7.0                | 11.5 |
| 〈張忠謀〉             | 7      | 11.1               | 16.4 |
| 〈楊德昌〉             | 93     | 13.8               | 17.4 |
| 〈台灣新冠疫情與疫苗〉 | 116    | 24.9               | 32.9 |

點一次 `[n]`，讀者被丟到 3 到 25 個螢幕之外的一份清單裡，在裡面找到那一行，讀完說明，再點連結開新頁，然後靠 `↩` 或瀏覽器上一頁回到原本讀到一半的句子。**四個動作換一次查證。** 這正是報導者設計師說「通常不太會再點下去」的那個成本。

### 1.3 誰真的抵達文末（GA4，近 30 天）

| 指標                         | 數值    | 佔頁面瀏覽 |
| ---------------------------- | ------- | ---------- |
| 頁面瀏覽總數                 | 103,972 | 100%       |
| 捲動深度 25%                 | 53,477  | 51.4%      |
| 捲動深度 50%                 | 34,502  | 33.2%      |
| `section_view` = `footnotes` | 12,840  | 12.3%      |
| 捲動深度 75%                 | 14,628  | 14.1%      |
| 捲動深度 100%                | 5,392   | 5.2%       |

`footnotes` 是站上所有 landmark 裡 `section_view` 最高的一個（12,840，第二名 `article_signature` 7,722），但那也只是 12.3% 的頁面瀏覽。**指向來源的記號在超過一半的讀者面前，來源本身只在八分之一的讀者面前。**

### 1.4 來源點擊率：不是 0 次，是 0 筆資料

`outbound_click` 近 30 天全站 98 次，全部來自 `hero_cta`（72）、`footer_support`（16）等六個 CTA。腳註區一次都沒有。

原因不是沒人點，是**沒有東西在量**：`EventTracker` 的點擊委派要求元素身上有 `data-ga-section`（[EventTracker.astro:84](../src/components/EventTracker.astro)），而 `processFootnotes()` 產出的 `<a class="footnote-ref">` 與 `.footnotes li a` 兩種連結都沒有這個屬性。17,113 條來源連結全站零儀器。

這是 [REFLEXES #82](../docs/semiont/REFLEXES.md) proxy signal 家族的另一個面貌，也是 §神經迴路「儀器只看見存在、看不見缺席」——我們有一個很漂亮的 `section_view` 曲線告訴自己「讀者有滑到腳註」，卻從來沒有一格在量「滑到之後有沒有人真的點出去」。本次改動最重要的副產物是把這格補上。

### 1.5 渲染層現況

- `processFootnotes()` 住在 [article-render.ts:1343](../src/utils/article-render.ts)，產出 `<sup id="fnref-N"><a href="#fn-N" class="footnote-ref">N</a></sup>` 與文末 `<section class="footnotes"><ol><li id="fn-N">…<a class="footnote-backref">↩</a></li></ol></section>`。
- 樣式在 [article.template.astro:1607-1729](../src/templates/article.template.astro) 的 scoped `.prose :global(...)`，暗色在 [dark-polish.css 2532-2576](../src/styles/dark-polish.css)。已有 `:target` 高亮（issue #1212）與手機加大點擊區。
- 腳註標籤有 306 條是中文（`[^鴻源]`、`[^台積電條款]`），所以 `href` 會是 `#fn-鴻源`，client 端定位必須走 `getElementById(decodeURIComponent(...))`，不能直接把 `href` 丟進 `querySelector`。
- 12 個上線語言（`de` 仍 `enabled: false`，見 OBSERVER-QUEUE #29），`ar` 是 RTL。

### 1.6 Cross-ref 掃描（Mode 4 hard gate）

grep `footnote` 掃過 `scripts/`、`src/`、`.github/`、`.husky/`：

- **全部腳註工具吃 markdown 源，不吃渲染後的 HTML**——`article-health.py` 的 `footnote_density` / `footnote_format` / `footnote_url` 三個 plugin、`fact-atom-diff.py`、`footnote-format-fix.py`、babel 的 `optimized-translate.py` / `patch-translate.py` / `restore-footnote-urls.py`，正規式全部對 `[^n]` / `[^n]:`。動渲染層對它們零影響。
- `check-url-contract.mjs` 只看 `<head>` 的 hreflang / canonical 與 sitemap，不看正文連結。
- `TextToSpeech.astro:186` 朗讀 `.prose` 的文字。**這條是唯一的真限制**：卡片內容若以靜態 HTML 塞進 `.prose`，朗讀會把每條腳註唸兩次，搜尋索引與選取複製也會拿到重複文字。
- `article.template.astro:1227` 有一段 `is:inline` 把 `.prose .footnotes` 標成 `data-ga-view="footnotes"`，本次要保留。

### 1.7 這件事的親戚

昨天（08-27）進 OBSERVER-QUEUE 的 **#39「正文內部連結荒漠」** 條目裡有一句：「我們把互鏈幾乎都放在文章最底下的延伸閱讀，而那個位置的問題自己記過一次——哲宇 6/14 問『轉換都在最下面但其實大家用得很少』。」

腳註是同一個結構的第三次現形：**把讀者要用的東西放在讀者到不了的位置**。延伸閱讀在文末、互鏈在文末、來源在文末。這次處理的是其中一條，另外兩條留在 #39。

---

## 二、方案發散（DIVERGE 相）

### 方案 A：伺服器端把腳註內容烤進 `<sup>` 的 data 屬性

`processFootnotes()` 產出時就把標題、網址、說明寫進 `data-fn-title` / `data-fn-url` / `data-fn-desc`，client 直接讀屬性畫卡。

- ✅ client 不需要查 DOM，任何位置的腳註記號都能用
- ❌ 每頁多一份完整腳註文字。〈楊德昌〉92 條 × 約 120 字 ≈ 11KB，乘上 1,133 篇 × 12 語
- ❌ 同一份內容變成兩個副本，將來只會改到一邊——正是 [REFLEXES #92](../docs/semiont/REFLEXES.md) twin-artifact 家族在講的病
- ❌ 屬性裡的 HTML 要 escape，連結要重建，說明裡的內嵌連結會失去可點性

### 方案 B：純 client 增強，內容從既有 `.footnotes li` 取

頁面本來就有那份 `<ol>`。卡片開啟時用 `getElementById('fn-N')` 找到對應 `<li>`，clone 出來解析成卡片。

- ✅ 零 payload 增加，零第二份真相，SSOT 就是那份 `<ol>`
- ✅ 腳註定義改了，卡片自動跟著改，沒有東西需要對賬
- ✅ 卡片節點掛在 `<body>` 尾端而不在 `.prose` 裡，朗讀、搜尋索引、SEO、選取複製全部零影響
- ✅ `article-render.ts` 一行不動——13 語 × 1,133 篇的產出 HTML 完全不變，dist 差異為零
- ✅ 沒有 JS 的讀者退回現行的錨點跳轉，完全不壞（漸進增強）
- ❌ 依賴頁面上有 `.footnotes` 區塊，也就是依賴現況

### 方案 C：改成側欄註解（Tufte 式 sidenote）

寬螢幕把腳註直接排在正文右側，不用點就看得見。

- ✅ 查證成本降到零
- ❌ 右側已經被 [ArticleSidebar.astro](../src/components/ArticleSidebar.astro) 佔著（目錄、閱讀時間、版本、貢獻者）
- ❌ 92 條腳註的文章側欄會爆掉，且腳註分布不均會產生大片空白
- ❌ 手機完全無解，等於只服務桌機讀者
- ❌ 動到全站 12 語 × 1,133 篇的版面節奏，遠超出「讓人點得到來源」這個目標的尺寸

### 判準與定案

| 判準                                            | A   | B   | C   |
| ----------------------------------------------- | --- | --- | --- |
| SSOT 自洽（不長出 twin artifact，REFLEXES #92） | ❌  | ✅  | ✅  |
| 對朗讀 / 搜尋索引 / SEO 零副作用                | ⚠️  | ✅  | ⚠️  |
| 手機可用                                        | ✅  | ✅  | ❌  |
| 改動規模對得起目標（MANIFESTO §合適尺寸）       | ⚠️  | ✅  | ❌  |
| 沒有 JS 時不壞（漸進增強）                      | ✅  | ✅  | ✅  |

**定案：方案 B。** 判準錨定 [REFLEXES #92](../docs/semiont/REFLEXES.md)（兩個該同步的產物中間沒有東西在對賬）＋ MANIFESTO §信念 6（`src/content/` 是投影不是 SSOT，同構原則套到「卡片是那份 `<ol>` 的投影」）＋ §造橋鋪路（改進系統而不是多蓋一份資料）。

---

## 三、互動設計

### 3.1 桌機

- 游標移入 `[n]`：延遲 **120ms** 開卡（避免掃過文字時亂跳）
- 游標離開：延遲 **220ms** 關卡；游標若在這段時間內移進卡片，取消關閉（卡片與記號之間留一條看不見的橋）
- **點擊 `[n]` 改為開卡，不再直接跳文末**。逃生口是卡片上的「看文末腳註」，那是一條真的 `href="#fn-N"`，行為與現在完全相同
- `⌘/Ctrl/Shift/中鍵 +click` 不攔截，交還瀏覽器
- 鍵盤 Tab 走到 `[n]` 時開卡，Enter 把焦點移進卡片第一顆按鈕，`Esc` 關閉並把焦點還給記號

### 3.2 手機

沒有 hover，所以 tap 就是開卡。卡片改成**底部抽屜**（bottom sheet）：從下緣升起、上方有半透明遮罩、點遮罩或「關閉」收起。手機的閱讀位置不會被推走，這比把讀者丟到文末好得多。

### 3.3 卡片長什麼樣

```
┌────────────────────────────────────────┐
│ 來源 ·  twreporter.org                 │  ← 網域徽章，一眼看出可信度層級
│                                        │
│ 報導者：一座島嶼的移工紀事              │  ← 來源標題（第一個連結的文字）
│                                        │
│ 2019 年系列調查報導，訪談 47 名漁工，   │  ← 腳註說明（破折號之後那段）
│ 附完整訪談逐字稿與船籍資料。            │
│                                        │
│ ┌──────────────┐  ┌────────────────┐  │
│ │ 開啟來源  ↗  │  │ 看文末腳註  ↓  │  │
│ └──────────────┘  └────────────────┘  │
└────────────────────────────────────────┘
```

**網域徽章是這張卡片最被低估的一格。** 讀者現在要判斷一條引用可不可信，得先跳到文末、讀完整行、注意到連結指向哪裡。徽章把「這是國史館還是某個內容農場」提前到記號旁邊，是策展式（MANIFESTO §信念 1）在引用層的具體樣子。

四種腳註形狀的降級：有標題連結 → 完整卡；只有裸網址 → 網域徽章＋全文＋開啟鍵；沒有網址 → 只有全文，不長出開啟鍵；連結不在開頭 → 全文，開啟鍵指向第一個連結。

### 3.4 儀器化

> 這一節在實作中被哲宇校正過一次（§後記 3）。初版只靠 `EventTracker` 的 markup contract，只涵蓋點擊——而桌機的主要互動是 hover，「有多少人在用」剛好量不到，等於原地復發 §1.4 罵的那個病。下面是校正後的版本。

三個訊號，一條漏斗：

| 訊號       | 事件                 | 怎麼來                                                                                                 | 回答什麼                             |
| ---------- | -------------------- | ------------------------------------------------------------------------------------------------------ | ------------------------------------ |
| 展開一張卡 | `footnote_card_open` | 元件自己送，帶 `trigger`（hover／click／focus）＋ `section` `label` `link_url` `page_lang` `page_type` | 多少人在用、用哪種手勢、展開哪些來源 |
| 點 `[n]`   | `content_click`      | `<a class="footnote-ref">` 掛 `data-ga-section="footnote_marker"`，EventTracker 自動接                 | 有多少是主動點的（相對於滑過去的）   |
| 點開來源   | `outbound_click`     | 卡片上的連結掛 `data-ga-section="footnote_card"` ＋ `data-ga-label="{網域}"`                           | **來源點擊率第一次有資料**           |

**節制**：`footnote_card_open` 同一頁同一條腳註只送一次（跟 `section_view` 的 `seen` 同一種去重）。所以事件數 = 讀者展開過幾條不同的來源，`activeUsers` = 多少人用過這個功能。不去重的話，游標在一段文字上來回掃就會把同一條灌成幾十筆。

**閘門對齊**：`EventTracker` 的點擊監聽掛在 `document` 的 capture 階段（[EventTracker.astro:200](../src/components/EventTracker.astro)），動態產生的卡片自動涵蓋。新參數只有 `trigger` 一個，已加進 `register-ga4-custom-dimensions.py` 的 `ENGAGEMENT_DIMENSIONS`、跑過 register script（GA4 `customDimensions/15511942910`）；`FootnoteCard.astro` 也加進 `instrumentation-audit.py` 的 `TRACKER_FILES`，不然它是下一個靜默漂移。

---

## 四、實作清單（IMPLEMENT 相）

| #   | 檔案                                                 | 動作                                                                                  |
| --- | ---------------------------------------------------- | ------------------------------------------------------------------------------------- |
| 1   | `reports/design-footnote-source-cards-2026-08-28.md` | 本報告（先於實作 commit — Mode 4 hard gate）                                          |
| 2   | `src/i18n/footnote.ts`（新）                         | `footnoteUI` 六條字串 × 12 語（來源／註解／開啟來源／看文末腳註／關閉／腳註 aria）    |
| 3   | `src/i18n/ui.ts`                                     | import + 12 個 `...footnoteUI.{lang}` spread                                          |
| 4   | `src/components/FootnoteCard.astro`（新）            | 卡片骨架＋樣式（含暗色與 RTL）＋client script：索引、解析、定位、hover/tap/鍵盤、埋點 |
| 5   | `src/templates/article.template.astro`               | 掛載 `<FootnoteCard lang={lang} accent={categoryInfo.color} />`                       |
| 6   | `src/styles/dark-polish.css`                         | 把 `fn-card` 加進 `[class*='card']` 廣域深色規則的例外清單（理由見 §後記 4）          |
| 7   | `scripts/tools/register-ga4-custom-dimensions.py`    | `ENGAGEMENT_DIMENSIONS` 新增 `trigger`                                                |
| 8   | `scripts/tools/instrumentation-audit.py`             | `TRACKER_FILES` 新增 `FootnoteCard.astro`                                             |

`src/utils/article-render.ts`、`knowledge/`、所有腳註檢查工具（`article-health.py` 三個 plugin／`fact-atom-diff.py`／babel 那批）：**零改動**。卡片的暗色與 RTL 樣式住在元件自己的 `is:global` 區塊，不散進 `dark-polish.css`。

### 驗收（dogfood 硬閘門，全部實跑）

用 Playwright 對 dev server 跑真實瀏覽器，不靠讀碼推論。

**形狀 × 情境 7 案**（每案截圖＋讀計算後樣式）：

| 案                          | 結果                                                                        |
| --------------------------- | --------------------------------------------------------------------------- |
| 桌機淺色〈咖波〉            | ✅ 白底卡、來源徽章 `bugcatcapoo.com`、分類紫「開啟來源」                   |
| 桌機深色                    | ✅ `rgb(22,22,26)` 不透明（修掉廣域規則的半透明覆蓋後）                     |
| 手機 390×780                | ✅ 底部抽屜、遮罩、把手、加大點擊區                                         |
| 無網址〈台灣國樂 [^18]〉    | ✅ 徽章降級成「註解」、不長出開啟鍵、只剩「看文末腳註」                     |
| 連結不在開頭〈五月天 [^1]〉 | ✅ 無標題、網域 `zh.wikipedia.org`、開啟鍵指向內文那條連結                  |
| 中文標籤〈`[^鴻源]`〉       | ✅ `getElementById` 解出 `#fn-鴻源`，完整卡                                 |
| RTL 阿拉伯文                | ✅ `dir=rtl`、「المصدر」「فتح المصدر」、卡片跟著記號置中（修掉 RTL 定位後） |

**互動 14 項**：hover 開卡／hover 後點擊仍開著／再點收起／移開游標自動關／`Esc` 關閉並還焦點／點外面關閉／鍵盤 Enter 開卡且焦點落在主要動作／換腳註內容跟著換／「看文末腳註」跳到定義且 `:target` 亮起／`.footnotes` 8 條原封不動／`.prose` 內沒有卡片（朗讀不受污染）／埋點屬性齊全／手機真觸控 tap 開抽屜且 `hidden` 只切換一次（不閃爍）／點遮罩收起 —— **14/14 通過**。

**儀器對賬**：`instrumentation-audit.py`（static + live）三方對齊 0 ERROR，GA4 27 個維度全註冊。

**建置**：`astro build` 綠燈；`check-url-contract --strict` 綠燈。

---

## 五、風險與對策

| 風險                                                | 對策                                                                                                       |
| --------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| 點 `[n]` 的行為改變，老讀者的肌肉記憶被打斷         | 卡片上永遠有「看文末腳註」，那條連結的行為與現在逐位元相同；`⌘+click` 也不攔截                             |
| 卡片被 header（`z-[1001]`）蓋住                     | 卡片 `z-index: 1000`，且定位時把上緣夾在 header 高度之下；空間不足時翻到記號上方                           |
| 螢幕閱讀器把卡片當成干擾                            | 卡片預設 `hidden`，開啟時才進無障礙樹；`.footnotes` 那份 `<ol>` 原封不動，語意路徑完全保留                 |
| 朗讀唸到重複內容                                    | 卡片節點掛 `<body>` 尾端，不在 `.prose` 內（TextToSpeech 讀的是 `.prose`）                                 |
| 92 條腳註的文章一次建索引太慢                       | 索引 lazy 建立（第一次要開卡才建），且只是一次 `querySelectorAll` + Map 填充                               |
| 描述過長把卡片撐爆                                  | 內容區 `max-height` + 內部捲動                                                                             |
| 新語言出生時字串靜默退回中文（2026-07-26 那次的病） | `footnoteUI` 走 `useTranslations` 的 `FALLBACK_CHAIN`，缺 key 退英文再退中文；de 上線時補一條進本檔＋ui.ts |

---

## 六、這次沒做、但值得記下的

1. **正文內部連結的 hover 預覽**——同一套卡片機制可以直接服務 OBSERVER-QUEUE #39（674 篇正文零站內連結）。但那是內容層的缺口，補連結才是主菜，預覽是配菜，不在本次範圍。
2. **側欄註解**——方案 C 被否掉的是「全站預設」，不是「永遠不做」。若未來出現腳註密度均勻、寬螢幕為主的長文型態，可以當成單篇的排版實驗。
3. **來源可信度分層**——網域徽章目前只顯示網域。若之後想長出「一手來源 / 新聞 / 百科 / 社群」的分層標記，資料面在 [CITATION-GUIDE §來源品質要求](../docs/editorial/CITATION-GUIDE.md) 已有判準，可以接上去。
4. ~~**同一條腳註被多次引用時 `fnref-N` 這個 id 會重複**~~ → **同日補完**（哲宇 directive「徹底處理」，見 §後記）。實際規模比這裡估的大一個量級：全站 8,135 個有腳註的檔案裡 **72.6% 帶重複 id、合計 76,318 個**，最兇的〈北投溫泉街〉單頁 115 個。已改成每個出現位置各自的 id。

---

## 後記（IMPLEMENT 相摩擦回寫，2026-08-28）

### 哲宇實作中的三次校正

1. **「開啟來源的時候要另開新分頁」** — markup 本來就有 `target="_blank"`，但我當時在嵌入式瀏覽器裡看到它在原地導走，就加了一層
   `window.open(href, '_blank', 'noopener,noreferrer')` 當保險。

2. **「除了開新頁面原本的網頁也會跳轉過去」** — 上一條的保險本身就是 bug。**帶 `noopener` 的 `window.open()` 依規格回傳 `null`**（opener 關係被切斷，沒有 window 物件可回），所以我寫的 `if (win) e.preventDefault()` 永遠不成立，瀏覽器接著又跑一次 `<a>` 的預設行為——同一次點擊走了兩趟。修法是把整層保險刪掉：使用者手勢觸發的 `target="_blank"` 本來就不會被彈出視窗阻擋，那條路徑最穩。
   **教訓形狀**：我為了防「可能不會另開分頁」加的護欄，製造了「真的會多開一次」。護欄的回傳值語意沒查就拿來當條件，等於用一個沒讀過規格的判斷去守一個沒證實的病。跟 LESSONS `fix-scope-follows-symptom-not-root-class` 同族——只是這次連症狀都是我腦補的（嵌入式瀏覽器的 `_blank` 行為 ≠ 真實瀏覽器）。

3. **「也同步加入有多少人使用這個功能的 GA 追蹤」** — 原設計只靠 `EventTracker` 的 `content_click`／`outbound_click` markup contract，好處是零新參數、CI 閘門零改動，但**它只涵蓋點擊**。桌機的主要互動是 hover，那條路徑不經過任何點擊事件，所以「有多少人在用」在原設計裡量不到——這正是本報告 §1.4 在罵的那個病（儀器只看見存在），差點原地復發一次。
   補法：`footnote_card_open` 事件，帶 `trigger`（hover／click／focus）、`section`、`label`、`link_url`、`page_lang`、`page_type`。同一頁同一條腳註只回報一次（跟 `section_view` 的 `seen` 同一種節制），所以事件數 = 讀者展開過幾條不同來源，`activeUsers` = 多少人用過這個功能。
   連帶三件事一起做完，不然它就是下一個靜默漂移：`trigger` 進 `register-ga4-custom-dimensions.py` 的 `ENGAGEMENT_DIMENSIONS`、`FootnoteCard.astro` 進 `instrumentation-audit.py` 的 `TRACKER_FILES`、真的跑一次 register script 讓 GA4 建好維度（`customDimensions/15511942910`）。`instrumentation-audit.py` 三方對賬（code ↔ SSOT ↔ GA4 live）0 ERROR。

### 自己撞到的三個

4. **`requestAnimationFrame` 不是可靠的樣式提交點**：開卡動畫原本用 rAF 加 `is-open`，頁面在背景不重繪時 callback 不跑，卡片就永遠停在 `opacity: 0`。改成 `void card.offsetHeight` 強制一次 reflow 再加 class。
5. **視窗寬度可能回報 0**：嵌入式瀏覽器與截圖工具會給 `innerWidth === 0`，而 `0 <= 768` 為真，於是卡片誤判成手機、進抽屜模式、`place()` 也跟著早退。`isSheet()` 與 `place()` 都補上 `w > 0` 的下界。這是 [REFLEXES #38](../docs/semiont/REFLEXES.md)「混維度」的小號變體：`0` 同時表示「很窄」跟「量不到」。
6. **`resize` 不該關卡**：手機網址列收合、螢幕旋轉、截圖工具都會發 `resize`，一律關掉會讓卡片在正常操作中莫名消失。改成重新定位。

### 三個只有真的用瀏覽器點下去才會現形的

7. **抽屜模式的 hover 迴圈**：窄視窗但仍回報 `hover: hover` 的裝置（二合一筆電、把桌機視窗拉窄）上，抽屜一開就連著一層全螢幕遮罩，游標的命中對象從記號變成遮罩 → 記號收到 `mouseleave` → 關卡 → 遮罩消失 → 記號收到 `mouseenter` → 又開卡。實測序列：開 @1789ms、關 @2033ms、開 @2242ms，無限閃爍。修法是抽屜模式一律不走 hover 路徑（`isSheet()` 直接 return）。**這個 bug 靠讀碼看不出來**——要真的在 390 寬的視窗點一下、而且監看 `hidden` 屬性的變動次數才會看見。
8. **focus 跟 click 打架**：滑鼠按下去會先 `focus`（開卡），接著 `click` 判斷「已經開著 → 收起來」，於是按一下等於開了又關。修法兩層：`focus` 只在 `:focus-visible`（真正的鍵盤焦點）時開卡；click 的收合只在「這張卡本來就是被點開的」才觸發，hover 開著時再點一下是「留住」不是「關掉」。
9. **焦點環變成輸入框**：鍵盤開卡時焦點原本落在標題連結（區塊級），瀏覽器畫成一個方框，第一眼會讀成輸入欄位。改成焦點給主要動作（開啟來源）＋自訂 `:focus-visible` 圓角環；而且只有鍵盤啟動（`e.detail === 0`）才搬焦點，滑鼠點擊不搬。

### 順手還掉的 RTL 債

改 `dark-polish.css` 觸發了 `check-rtl-safe-css.sh`，它報了一條**不是我寫的**違反：`.resources-page .featured-card` 的 `border-left-color`。查下去發現那條其實早就掛在該腳本的 DEBT 清單裡（`dark-polish.css:1433`），只是**行號漂了**，所以閘門把一筆已知的債報成了新違反。三件事一起做完：

- 把那條改成 `border-inline-start-color`（該檔現在零 physical directional）
- DEBT 清單移掉這一條（債還清了）
- ALLOWLIST 的兩條置中從 1052/1099 重新釘到 1063/1110，並在表頭寫明「行號會漂、看到已知條目變成違反先確認是不是只是漂了」

順帶把 `FootnoteCard.astro` 加進該腳本的 SCOPE——新元件出生時不在受守護清單裡，等於 RTL 閘門對它是瞎的（`fix-scope-follows-symptom-not-root-class` 的同型：護欄只掛在寫它的人當時在看的那條路徑上）。加進去之後才發現原本 CSS 裡那句 `left: 0` 本來就該拿掉：桌機座標整個交給 JS 的 inline style，CSS 一個 physical inset 都不留。

### 三件 handoff 徹底處理（同日，哲宇 directive「徹底處理」）

收官原本留了三條 pending，同一晚全部收掉。

**(1) 「D+3 回頭看數字」原本是自律，現在是閘門。** 先用 Playwright 對**正式站**攔 GA 的 `/g/collect` 請求，確認 `footnote_card_open`（`trigger=hover` 與 `trigger=click` 各一筆）與 `content_click(section=footnote_marker)` 真的送得出去——通道確認是通的，不是「等三天看有沒有資料」。接著造 [`scripts/tools/footnote-card-adoption.py`](../scripts/tools/footnote-card-adoption.py)，一行問完整條漏斗（頁面瀏覽 → 滑到文末腳註區 → 展開卡片 → 點開來源），並把預測寫成 [UNKNOWNS EXP-2026-08-28-fncard](../docs/semiont/UNKNOWNS.md)（due 2026-09-11）。`generate-dashboard-alerts.mjs` 機械檢查到期未判定，所以這件事不再依賴誰記得。上線首小時實測 19 次展開 / 7 人 / 8 次點開（含我自己驗證貢獻的 2-3 筆，已在 EXP 註記污染）。

**(2) `fnref` 重複 id 根治。** 規模比估的大一個量級：**76,318 個重複 id、72.6% 的有腳註檔案中招**。改法是每個出現位置各自的 id（`fnref-2`、`fnref-2-2`、`fnref-2-3`⋯，第一次維持舊格式所以既有外部深連結不斷），文末返回鍵改成一排各自指回的連結。驗收：〈北投溫泉街〉144 個 `<sup>` / 144 個返回鍵 / 0 重複 id / 0 個指不到的返回鍵，引用最多的那條（22 次）的 22 個返回鍵指向 **22 個相異位置**。順手抓到一個 specificity 問題：`.footnotes a` 的 underline 壓過 `.footnote-backref` 的 `text-decoration: none`，一排序號底下會拖出像壞掉的虛線，要帶元素型別寫成 `a.footnote-backref` 才壓得過去。

**(3) RTL 檢查器不再用行號釘條目。** 改成兩層：第一層是語意判準——`left/right: 50%` 若同一個規則區塊裡有 `-50%` 的 translate 就是置中慣用法，自動放行，不需要任何清單（原本那兩條 ALLOWLIST 因此整個清空）；第二層才是「檔案＋宣告文字」比對的一次性例外與掛號中的債。另外加一道對賬：清單裡對不上任何一行的條目會被印出來提醒核對——那正是今天那半小時的病根（一條掛了一個月的債因為行號漂掉被當成新違反）。三個性質都實測過：整檔位移 40 行後零違反、真的插一條非置中的 `left: 12px` 照樣被抓、把債改好但沒從清單移除時對賬會叫。

### 做這三件時撞到的鄰居（沒收，已進佇列）

`article-render.ts` 的標題 id 產生器用 `[^\w\u4e00-\u9fff-]` 過濾，而 **JS 的 `\w` 只認 ASCII**。實測 **ko 有 7,158 個標題 id 塌成一串破折號、3,638 個重複；ru 7,010/2,922；ar 6,999/2,912；hi 6,057/2,526**——這四語的目錄連結點得到，但指向同名重複裡的第一個，也就是錯的那個標題。修它會動到全站約六萬個 `#anchor`（拉丁語系的重音字元目前被吃掉，改了既有分享連結的 fragment 會失效），命中 §自主權邊界，因此進 [OBSERVER-QUEUE #44](../docs/semiont/OBSERVER-QUEUE.md) 附選項與推薦 default，不在本輪收。

**這一段本來差點寫錯**：我第一次用 Python 重寫新舊 slug 函式跑全站對照，得到「所有語言 0 個 id 會變」，差一步就寫成「零風險」。Python 的 `\w` 預設吃 Unicode 字母，JS 的不吃——兩邊的正規式**長得一模一樣**，沒有型別錯誤、沒有例外、沒有空輸出，只有一個很乾淨的錯答案。改用 Node 跑才看到真實規模。教訓已進 LESSONS（`measured-one-engines-semantics-with-another`）。

### 資料修正

`[標題](<網址>)` 這種角括號包網址的寫法（維基中文條目常見，因為網址裡有括號），第一版統計的正規式沒認出來，被算進「純網址」桶。重算後 leading-link 從 93.6% 修正為 **94.2%**，純網址 2.6% → 2.2%，連結不在開頭 1.7% → 1.5%。渲染層不受影響（`marked` 認得角括號寫法，DOM 裡就是一個正常的 `<a>`，卡片解析走 DOM 不走 markdown），但報告的數字該是對的。

🧬

🧬
