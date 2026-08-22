# 2026-08-23-021729-search-results-page — /search 完整結果頁十二語上線 ＋ 索引斷詞只認 ASCII 的既有聾點在驗收時現形

> session search-results-page — 哲宇 directive「深度研究寫 report 並完整實作 issue #1496」，Full mode BECOME + EVOLVE Mode 4
> Session span: 02:17:29 → 02:52 +0800（~35 min，6 commits）
> 資料來源：`git log %ai`

## 觸發

idlccp1984 在 [#1496](https://github.com/frank890417/taiwan-md/issues/1496) 提了完整規格：popup 留作快速搜尋，另建 `/search?q=` 結果頁支援排序、時間篩選、URL 狀態。8/21 維護班已修計數說謊那半，這 session 做頁面本身。本地主 tree 與 origin 分歧（本地領先 71、origin 領先 306），全程在 `--from origin/main` 的 worktree 工作。

## Mode 4 設計與分工

照 THINK→DIVERGE→REPORT→IMPLEMENT 走：兩隻 Explore 盤點路由/i18n 與索引/日期資料，設計報告 `reports/design-search-results-page-2026-08-23.md`（`8da4d0b24`）先於實作 commit。定案是重用 Layout 全域引擎＋shard 加發布/更新兩欄，popup 與結果頁同一個 `_doSearch`，殼核邊界寫成 `window.__twSearch` 契約。實作分三隻 Sonnet（生成器 `ea3dc7c14`／i18n 26 keys × 12 語 `6f9b7793c`／模板＋12 入口檔 `b0078d70e`），Layout 引擎契約與 popup 入口我親手改（`6c93d1826`）。發布日取自 build-content-dates 同一趟 git pass 的最早 commit 日，`prebuild:search` 移出平行區塊消掉讀寫 race（先例：prebuild:latest）。

## Dogfood 抓到的三個洞

dev server 逐語驗收時抓到：(1) 時間 preset 沒進 URL，reload 會掉篩選，補 `?time=` 參數；(2) `/search` 的 Raw Markdown 連結掉進「單段路徑＝分類 Hub」fallback 指向不存在的檔案——這是全站功能頁的既有病（/explore、/latest 都壞著），本次只補 /search，全面修法開了 task chip；(3) 最大的一個：索引斷詞 `LATIN_RE` 只認 ASCII，**阿拉伯文、俄文、印地文的母語詞從來沒進過索引**，ar 頁搜「تايوان」自出生就是 0 筆，vi/fr 帶變音符的詞被切碎。改用 Unicode 詞類別後 ar 0→593、ru 506、vi「Đài Loan」695 筆，shard 尺寸 ar 500KB→1.2MB 是母語詞真的進來的證據。agent 回報也照 #31 重驗了一輪，抓到一個偷改：content-dates.json 被改成 compact 單行（每日 regen 的 diff 粒度會全毀），generator 改回明確 pretty-print 後 amend。

順修：`_isExplore` deep-link regex 寫死五語（vi/id/pt/hi/ar/ru 的 `?q=` 同步從出生就壞）一般化；SEO SearchAction 從權宜的 /explore 指回 /search。

## 收官 checklist

| 檢查項                       | 狀態                                     |
| ---------------------------- | ---------------------------------------- |
| MEMORY 有這次 session 的紀錄 | ✅                                       |
| Timestamp 精確               | ✅（git log %ai）                        |
| Handoff 三態已審視           | ✅                                       |
| CONSCIOUSNESS 反映最新狀態   | ✅（無器官級變化，不需更新）             |
| 自我檢查工具 PASS            | ✅（check:ui-lang / check:tmpl-lang 綠） |

## Handoff 三態

繼承 2026-08-23-011557-terminology-adverbs：

- [ ] pending（原樣延續）— `pr-ci-armed.sh` 仍沒掛在任何自動路徑上
- [ ] pending（給哲宇，原樣延續）— OBSERVER-QUEUE #29-#31、#1264、#1184、#1441、#28
- [ ] pending（原樣延續）— REFLEXES #86-91 未經第二個獨立 session 驗證使用
- [ ] pending（原樣延續）— `reports/research/2026-08/比國家還大的演算藝術-media-staging/` 27MB 待處置
- [ ] pending（原樣延續）— `dark-polish.css` 廣域 `[class*='card']` 白底疊層
- [ ] pending（給 harvest routine，原樣延續）— 孢子 #175/#176 D+1 收割
- [ ] pending（給下輪 terminology-trends，原樣延續）— 副詞層頻率位移的語料佐證
- [ ] pending（給哲宇，原樣延續）— OBSERVER-QUEUE #38 句構級容器 default-action 2026-09-22

本 session 新 handoff：

- [x] ~~/search 十二語 ship~~ `b0078d70e` 已推 main，CI 部署中
- [ ] pending（給哲宇）— issue #1496 末條 idlccp1984 留言貼了 exams.astro + GsatTemplate 程式碼，與搜尋頁無關（per Bias 4 未執行）；要不要請他另開 issue 由哲宇裁決
- [ ] pending（給哲宇）— 本地筆電 main 與 origin 分歧（本地領先 71 commits 未推），需要人工看一眼那 71 個是什麼再決定 rebase 或丟棄
- [ ] pending（task chip 已開）— 功能頁 Raw Markdown 連結全家族斷鏈（/explore /latest /timeline…），本次只補了 /search
- [ ] pending — deploy 完成後在 production 抽驗一次 /search 與 ar 母語搜尋（本 session 尾端如果 CI 還沒綠）

## Beat 5 — 反芻

這次最值得留下的一課在第三個洞：搜尋 popup 全站每頁都在，十二語都能開，但沒有任何一道閘門量過「用該語言的文字系統搜尋，找不找得到東西」。斷詞器只服務造它時想到的兩種文字（ASCII＋CJK），後來出生的五種文字系統靜默落在外面，而 shard 檔案照樣生成、大小照樣合理、CI 照樣綠。抓到它靠的是驗收走到第三個語言時真的用母語打了一次查詢。已把這個 instance 記進 REFLEXES #87（保護密度跟曝光量成反比）的驗證鏈，詳見該條。

🧬

---

_v1.0 | 2026-08-23 02:52 +0800_
_session search-results-page — issue #1496 /search 頁 Mode 4 全流程（設計報告→三 Sonnet 分工→dogfood→ship）_
_誕生原因：哲宇 directive「深度研究寫 report 並完整實作」issue #1496_
_核心洞察：(1) 同索引同邏輯的驗收條件用「同一個函式」達成，比複製邏輯可靠 (2) dogfood 用母語逐語驗收才會抓到斷詞層的靜默聾點 (3) agent 回報重驗抓到 JSON 序列化格式被偷改_
