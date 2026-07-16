# 時間台灣（/timeline）實作報告

> _2026-07-16 compassionate-kirch session。設計依據：[timeline-page-design-2026-07-16.md](timeline-page-design-2026-07-16.md)。_

## 一、交付內容

「探索」底下新增**時間台灣**：六語言的歷史時間軸頁，把台灣從史前南島到當代分成八個時代由上往下展開，40 個關鍵事件、74 篇站內文章接進軸線。對應地理台灣（/map）的時間版。

| 檔案                                                   | 動作      | 說明                                                                                                            |
| ------------------------------------------------------ | --------- | --------------------------------------------------------------------------------------------------------------- |
| `src/data/timeline-eras.json`                          | 新增      | 策展資料層 SSOT：8 時代 × 6 語（title/subtitle/intro/yearsLabel）＋ 40 事件 ＋ 74 文章 ref ＋ 明鄭 desertNote   |
| `src/templates/timeline.template.astro`                | 新增      | 頁面本體：hero、sticky era chip bar、垂直 spine、事件 `<ol>`、ArticleCard（detailed 主幹 / row 雙欄）、終章 CTA |
| `src/pages/timeline.astro` ＋ en/ja/ko/es/fr 五個 shim | 新增      | 六語路由（5 行 shim 慣例）                                                                                      |
| `src/i18n/timeline.ts` → `ui.ts` spread                | 新增/修改 | UI chrome 六語（nav label、meta、區塊標題、CTA）                                                                |
| `src/components/Header.astro`                          | 修改      | 探索 dropdown（desktop）＋ mobile 子選單各加「⏳ 時間台灣」                                                     |
| `src/styles/dark-polish.css`                           | 修改      | `.timeline-page` 加入 ArticleCard 深色規則的 page-wrapper 組（`.latest-page` 同款）                             |

## 二、關鍵實作決策

1. **文章跨語解析不重造輪子**：ref（`Category/中文slug`）→ zh 索引 fail-loud 驗證（查不到 = throw = build 失敗，slug typo 不可能上線）→ 非 zh 語言經 `getLangSwitchPath`（`_translations.json` registry）拿該語言 URL，再從該語言 `getArticlesIndex` 拿在地化標題與描述；翻譯缺口 fallback 連 zh 路徑。「slug 打錯」與「翻譯還沒有」是兩種 cause 分開處置（REFLEXES #38 / #52）。
2. **時代內容住資料檔、UI chrome 住 i18n**：per 神經迴路既有教訓（i18n module 給 chrome，list-heavy 條目用 localized inline struct）。幾何（年份數字、顏色、slug）語言無關，文字欄六語。
3. **visible-by-default**：全部內容 server-render 在初始 HTML，唯一 client JS 是 era chip 的 IntersectionObserver active 追蹤（漸進增強）。六語的台灣史骨架對 AI 爬蟲完整可讀。
4. **色彩**：8 時代各配一個 mid-tone accent（磚紅、海青、官褐、銅綠⋯⋯），表面與文字全走 tokens（`--color-bg/-ink/-border`），深色模式大多自動成立，ArticleCard 部分沿 dark-polish page-wrapper 慣例補。
5. **明鄭沙漠誠實標示**：站上唯一沒有獨立條目的時代，直接在該時代放「這一段還很薄」＋貢獻 CTA——把缺口寫成邀請函，是 NMTH 第八展區「你也是寫歷史的人」的開源版。

## 三、驗證紀錄

- **production build 綠燈**（`npm run build` exit 0），六語 `dist/{lang}/timeline/index.html` 全部產出。
- **內部連結 gate 通過**：broken ratio 0.39%（= baseline，本頁貢獻 0 條新斷鏈）；zh dist 74 張卡 href 全部 percent-encoded 正常。
- **六語 dev 驗證**：en 74/74 卡連英文路徑（0 fallback）；ja/ko/es/fr 各 74 卡、各 1 篇誠實 fallback 到 zh。
- **視覺 smoke test**：zh 亮色全頁、深色模式（tokens 自動翻轉 + chip bar 正常）、mobile 375px（chips 橫向捲動、事件單欄）。era chip active 追蹤與點擊跳轉正常。
- **Header nav**：六語頁面的 nav 各自連到正確的 `/{lang}/timeline`。
- **事實驗證**：40 個事件年份逐條對站內已查核文章 grep 驗證（設計報告 §八）；兩處寫入前攔下的偏差——長濱文化站內口徑是「約 2-3 萬年前」（不用 5 萬）、福爾摩沙命名不用 1544 葡萄牙說（站內文章已引研究修正，改用 1584 Gali 文獻＋「荷蘭時代後確立」）；明鄭寫「二十一年」（神經迴路舊教訓：22 年是錯的，NMTH 校正為 21 年）。

## 四、實作中抓到的問題

1. **`content-visibility:auto` 白屏**：初版在文章格加了 `[content-visibility:auto]`，整頁在瀏覽器 pane 完全不繪製。移除後正常。頁高 ~13K px 不需要這個微優化，正確性優先。
2. **史前文章 description 殘留內部標記**：「（P0⚠️）」渲染在文章卡上——這是該文章 frontmatter 的既有問題，已開獨立 task chip，不混進本次 diff。

## 五、後續候選（不在本次範圍）

- 明鄭／荷西沙漠的補文（東寧王國、陳永華、施琅、熱蘭遮城）——ARTICLE-INBOX 候選。
- 時代事件的年份錨點連到對應文章段落（現在事件是純文字，文章連結集中在卡片層）。
- graph.md v3 scrollytelling-lite 上線後，era 轉場可考慮 CSS scroll-driven 漸進效果（維持零 JS）。
- GA4 觀察：`timeline_page` section 事件已埋（EventTracker 全站 mount 自動 cover + 卡片 dataAttrs），上線一週後看 scroll depth 與 era 點擊分布，決定要不要調時代順序或卡片密度。
