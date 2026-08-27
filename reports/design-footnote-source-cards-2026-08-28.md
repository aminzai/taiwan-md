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

| 形狀                       | 條數   | 佔比  | 卡片能給什麼           |
| -------------------------- | ------ | ----- | ---------------------- |
| `[標題](網址) — 說明`      | 16,041 | 93.6% | 標題＋網域＋說明＋開啟 |
| 純網址（無 markdown 連結） | 445    | 2.6%  | 網域＋全文＋開啟       |
| 完全沒有網址               | 356    | 2.1%  | 全文（不顯示開啟鍵）   |
| 連結不在開頭               | 290    | 1.7%  | 全文＋第一個連結       |

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

不自己呼叫 `gtag`，改成滿足 `EventTracker` 既有的 markup contract，讓它自動接：

| 動作           | 掛的屬性                                                     | 產生的事件                                     |
| -------------- | ------------------------------------------------------------ | ---------------------------------------------- |
| 點 `[n]` 記號  | `data-ga-section="footnote_marker"` `data-ga-label="{編號}"` | `content_click`                                |
| 點「開啟來源」 | `data-ga-section="footnote_card"` `data-ga-label="{網域}"`   | `outbound_click`（第一次有來源點擊率這格資料） |

`EventTracker` 的點擊監聽掛在 `document` 上（[EventTracker.astro:200](../src/components/EventTracker.astro) `addEventListener('click', _onClick, {capture:true})`），動態產生的卡片自動被涵蓋。`section` / `label` / `link_url` / `page_lang` 四個參數都已註冊在 `register-ga4-custom-dimensions.py` 的 `ENGAGEMENT_DIMENSIONS`，**不新增任何參數，所以 `instrumentation-audit.py` 的 CI 閘門零改動**。

---

## 四、實作清單（IMPLEMENT 相）

| #   | 檔案                                                 | 動作                                                                               |
| --- | ---------------------------------------------------- | ---------------------------------------------------------------------------------- |
| 1   | `src/i18n/footnote.ts`（新）                         | `footnoteUI` 五條字串 × 12 語（來源／開啟來源／看文末腳註／關閉／腳註 aria）       |
| 2   | `src/i18n/ui.ts`                                     | import + 12 個 `...footnoteUI.{lang}` spread                                       |
| 3   | `src/components/FootnoteCard.astro`（新）            | 卡片 markup 模板＋樣式＋client script（索引、解析、定位、hover/tap/鍵盤、GA 屬性） |
| 4   | `src/templates/article.template.astro`               | 掛載 `<FootnoteCard lang={lang} />`；`.footnote-ref` 加 hover 提示樣式             |
| 5   | `src/styles/dark-polish.css`                         | 卡片暗色變體                                                                       |
| 6   | `reports/design-footnote-source-cards-2026-08-28.md` | 本報告（先於實作 commit）                                                          |

`src/utils/article-render.ts`、`knowledge/`、所有腳註檢查工具：**零改動**。

### 驗收（dogfood 硬閘門）

1. 四種腳註形狀各找一篇真文章，實際開卡截圖
2. 桌機 hover / click、手機 tap（375 寬）、鍵盤 Tab+Enter+Esc 各走一次
3. 暗色模式截圖
4. RTL（`/ar/...`）截圖，確認卡片與按鈕方向正確
5. 中文標籤腳註（`[^鴻源]`，〈台灣股市與資本市場〉）能正確開卡
6. `npm run build` 綠燈；朗讀功能點下去確認沒有唸到重複的腳註文字
7. `.footnotes` 區塊、`:target` 高亮、`↩` 返回鍵全部維持原行為

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

---

## 後記（IMPLEMENT 相摩擦回寫）

_實作中發現的問題補在這裡。_

🧬
