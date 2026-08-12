---
feedback_id: '9dc2c3e7-ecdd-45dd-8846-df5acc43d5a7'
created_at: '2026-08-11T19:36:42.836164+00:00'
contributor: 'CJ C'
type: 'bug'
status: 'filed'
page_kind: 'semiont'
article_slug: ''
lang: 'zh-TW'
source_url: 'https://taiwan.md/semiont/'
issue_url: 'https://github.com/frank890417/taiwan-md/issues/1322'
issue_number: 1322
---

# Feedback — bug · 認知層 — Taiwan.md Semiont

**回報者**：CJ C
**時間**：2026-08-11T19:36:42.836164+00:00

**回報內容**
生態系統的整體運作
關於使用「海量」這個詞彙，由於是屬於台灣的AI資料庫，應該使用「大量」比較恰當。

**系統初判**
已收到，自動初判分類為「網站問題」，已轉維護者。

**GitHub issue**：https://github.com/frank890417/taiwan-md/issues/1322

## 溝通紀錄

<!-- issue 留言由 twmd-feedback-triage 定期 sync 到這裡 -->

<!-- comment:frank890417-2026-08-12T01:05:17Z -->

**frank890417** · 2026-08-12 01:05

修好了，commit `0357a38b4`。

`/semiont/` 那個節點原本寫「網路海量知識」，現在是「網路大量知識」。採用回報者建議的「大量」而不是詞庫裡的「巨量」——「巨量」在台灣幾乎只黏在「巨量資料」這個詞上，一般語境用「大量」比較自然。同一個檔案往上九行本來就寫著「大量搜尋撈取」，「海量」是那裡唯一的例外。

**這則回報最有價值的地方，是它指出了一個結構性的空洞。**

Taiwan.md 自己維護著一份 2,394 條的用語保存詞庫，`data/terminology/巨量.yaml` 白紙黑字寫著 `china: 海量` / `taiwan: 巨量`。也就是說，我們有詞庫、有判準，卻從來沒有任何閘門拿它來檢查自己的介面字串。昨天才替 `src/i18n/` 補上的語言閘門查的是「字形」——簡體字、整串沒翻——而「海量」是正體字寫的，字形檢查當然放行。**字形對，詞彙錯。**

所以這則回報的處置不只是改一個詞，而是補了一道閘門：`check-ui-language.mjs` 新增 `PRC_TERM` 檢查（commit `b8b536f7d`），拿已經在 889 篇文章上實戰過的用語對照表掃 zh-TW 介面字串，接上 pre-push 與 CI。以後這類詞混進介面會在 push 當下就被擋下來，不用再等讀者發現。

順帶掃出並修掉兩處指 source code 卻寫成「代碼」的按鈕文字。

謝謝這則回報 🧬
