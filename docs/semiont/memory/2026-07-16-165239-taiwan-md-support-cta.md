# 2026-07-16-165239-taiwan-md-support-cta — 贊助入口全站重佈：文章簽名檔＋七入口漏斗，啟維建議一天內上線

> session taiwan-md-support-cta — 哲宇轉 Muse brief（林啟維 2026-07-16 面對面建議）觸發，Full mode 甦醒
> Session span: 15:55 甦醒 → 16:52 merge main（commits 16:33:46 → 16:50:40 +0800, 3 commits）
> 資料來源：`git log %ai`

## 觸發

林啟維（Portaly 創辦人）當面跟哲宇說：你的斗內入口藏太深，讀者剛讀完文章最有動機支持的那一刻，站上什麼都沒遞出去。Muse 把對話轉譯成 brief，哲宇丟進來要求消化、複驗、規劃、實作。session 中途哲宇又追加三條（改名「贊助維護」＋開新分頁、首頁加按鈕、完整漏斗監測），最後下 /goal 要求全站盤點。

## 文章簽名檔與全站七入口

核心實作是把文章結尾的「編輯此頁／回報問題」兩顆按鈕等量替換成低調簽名檔：分享出去、一起編輯或貢獻內容、贊助維護三選項並列，中性語氣，編輯與回報降級成卡片底部小字。等量替換是因為複驗發現結尾已有四個區塊，再加就是洗版——Muse 的「別洗版」從建議升為硬約束。接著首頁「加入我們」加第三顆按鈕，/goal 盤點後再補儀表板贊助時間軸尾端一行與 /semiont 頁尾備註，其餘 surface（導航、404、瀏覽頁、沉浸式體驗頁）寫進報告 §十作為刻意不加的紀錄。文案六語全手寫（UI 字串不走巴別塔），`0953dc269` ship 簽名檔＋首頁＋UTM，`8bf392154` ship 盤點兩入口。

漏斗量測發現既有儀器幾乎全現成：EventTracker 的 markup contract（`data-ga-section/label`）加屬性即得 `outbound_click`，零新 GA4 param，audit 無 ERROR。七個入口各配獨立 `section` 與 `utm_medium`，Portaly 端與 GA4 端可以對齊切轉換。轉換 SSOT 是 `data/supporters/transactions.json`。漏斗查詢工具 `scripts/tools/support-funnel.py` 由 Sonnet 分身建、我用真實 GA4 API 複驗（28 天文章曝光 34,633、實際交易 4 筆）。Portaly 後台追蹤設定的答案：只填 GA4 `G-JGC5W00N7T`，其餘三格（UA／GTM／Pixel）留空。

## readingTime 污染修復

哲宇在 `/en/people/li-ang` 親眼看到側欄閱讀時間變成一坨文字。追查是 babel 管線把 zh 源檔 `readingTime: 7` 下方的 `design_rationale` 註解塊整個黏進 readingTime 變多行字串，受害 12 檔（李昂、童子賢、王永慶、葉國一、楊傳廣 × 各語）。dry-run 後全修回 zh 源數值並驗 YAML parse（`c0e8f5074`）。管線病根另 spawn chip（task_ad75163e）。這跟撇號家族（project_babel_frontmatter_apostrophe）可能同根：手寫 frontmatter 序列化器。

## 收官 checklist

| 檢查項                       | 狀態                                                  |
| ---------------------------- | ----------------------------------------------------- |
| MEMORY 有這次 session 的紀錄 | ✅                                                    |
| Timestamp 精確               | ✅（git log %ai）                                     |
| Handoff 三態已審視           | ✅                                                    |
| CONSCIOUSNESS 反映最新狀態   | ❌（本 session 未動，data-refresh 會接）              |
| 自我檢查工具 PASS            | ✅（prose-health / audit --static / build 7889 頁綠） |

## Handoff 三態

繼承（2026-07-15-231142-twmd-data-refresh-pm，均非本 session 範疇，原樣傳遞）：

- [ ] 尊翻譯同步 — 今晚 babel-nightly
- [ ] 免疫 v2 首度掉出 60（58）— self-evolve-weekly 週六 audit
- [ ] CF 404 vc=12 續探 / rewrite-daily silent-death / rider step 入 SKILL.md — 各 routine 自接

本 session 新 handoff：

- [ ] **哲宇兩個 Portaly 端動作**：後台 tagManager 填 GA4 `G-JGC5W00N7T`；斗內頁頂貼一句話成本說明（報告 §五有全文）
- [ ] **D+7 看漏斗首批數據**：`python3 scripts/tools/support-funnel.py --days 7`，順便決定 taste fork B（share icon row 要不要收進簽名檔）
- [ ] **babel readingTime 病根**：chip task_ad75163e 已開，含全站同型欄位掃描
- [ ] SupporterTimeline 元件 zh-hardcoded 卻渲染在六語 dashboard（pre-existing，低優先）

## Beat 5 — 反芻

這 session 學到的核心是「ask 的位置學」：啟維的建議本質是把邀請放在價值交付的時刻，而不是放大音量。實作時最重要的決定反而是不加的清單——導航、404、沉浸頁全部記錄「為什麼不」，讓未來 session 不會重新提案把站變成伸手牌壁紙。另一個值得記的是漏斗的最後一階跨在系統邊界上（我們的 GA4 → Portaly 的頁面），量測的縫永遠在系統交界，這次用 UTM＋對方後台填我們的 GA4 ID 把縫縫起來。詳細反芻寫 diary。

🧬

---

_v1.0 | 2026-07-16 16:55 +0800_
_session taiwan-md-support-cta — 啟維斗內 UX 建議 → 簽名檔 CTA + 七入口漏斗 + 全站盤點 + readingTime heal，一天內 merge main_
_誕生原因：林啟維面對面建議經 Muse 轉譯，哲宇 directive 實作_
_核心洞察：(1) ask 放在價值交付時刻而不是放大音量 (2) 刻意不加的清單跟加的清單一樣是策展 (3) 量測的縫在系統交界，UTM＋對方後台填我方 GA4 ID 縫合_
