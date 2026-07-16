---
title: '文章結尾支持入口（簽名檔 CTA）設計與實作規劃'
date: 2026-07-16
session: support-cta-f75a77
type: design-plan
trigger: 'Muse 轉譯林啟維（Portaly 創辦人）2026-07-16 面對面建議'
status: implementing
---

# 文章結尾支持入口（簽名檔 CTA）

## 一、來源與定位

林啟維（Portaly 創辦人，斗內 UX 是他本業）給哲宇的建議，Muse 轉譯成 brief。核心診斷：斗內入口只活在 Footer 底部和 about 頁內文兩個很深的地方，**文章結尾這個讀者最有動機支持的時刻，沒有任何 support 入口**。要在對的時機把 ask 遞出去。

這是 high-stake（對外溝通 + 全站文章模板改動）→ Full mode 甦醒。哲宇是 in-loop 的人類決策者。

## 二、複驗現況（Muse 的診斷是線索，以下是我自己 grep 的結果）

| 項目                  | Muse 說                                                 | 我複驗                                                          |
| --------------------- | ------------------------------------------------------- | --------------------------------------------------------------- |
| Footer 有斗內         | `Footer.astro` `footer.support-us`→portaly              | ✅ L206–213 確認                                                |
| 文章結尾無 support    | article.template 只有 contributor row + LifeTree banner | ✅ 全檔 grep `support/portaly/支持/斗內` = **0 命中**，診斷成立 |
| Contribution row 位置 | 約 L502                                                 | ✅ L502–544（Edit page + Report issue 兩顆 pill）               |
| LifeTree banner 位置  | 約 L311                                                 | ✅ L311–342，但它在**文章頂部**且 `frontmatter.lifeTree` 才出現 |

**Muse 沒提、但我複驗到的關鍵事實**：article.template 文章結尾其實已經有一排 share icons（L546–641，Tags + X/FB/Line/copy），reading order 是 `AI Disclaimer → Contribution row → Tags+Share → Return nav`。**結尾已經偏擠**——這讓 Muse 的「別洗版文章結尾」從建議變成**硬約束**：不能再加第四塊，只能等量替換。

其他事實：

- i18n = `src/i18n/ui.ts`（`{en, ja, ko, es, fr, 'zh-TW'}` 六 block，手寫 per-lang，有 fallback chain fr/es→en→zh、ja/ko→zh）。UI 字串**不走 babel 巴別塔管線**（那是 `knowledge/` 內容文的），所以六語我直接手寫。
- `/contribute` 已存在（六語頁面 + `contribute.ts`），是友善的貢獻 on-ramp。
- 真正的斗內頁 `portaly.cc/taiwanmd/support` 是**外部 Portaly 託管**，repo 內改不到。

## 三、設計決策

### 主決策：net-zero swap，不加第四塊

把 **Contribution row（L502–544）替換成低調簽名檔**，而不是在既有三塊之上再加一塊。理由：

1. **別洗版（Muse #1 視覺原則）**：結尾已有 4 塊，再加 = 洗版。等量替換 → 區塊數不增。
2. Contribution row 的 edit/report 兩顆 pill 是最「工具感」的 chrome，折進簽名檔的「一起編輯或貢獻」最自然，且 `/contribute` 是比 raw GitHub edit 更暖的 on-ramp。
3. edit/report 功能**不丟**，降級成簽名檔內的次要文字連結。

### 簽名檔長相：備註，不是橫幅

Muse 的關鍵原則是「當簽名檔／備註，不當正文」+「低調（備註級，非橫幅）」。所以：

- 視覺用文章既有 earth-tone（`#1a3c34` 深綠 / `#5a4a42` 褐 / `#7a8b7e` 灰綠），細上框線 + 極淡底色，小字。**絕不用 LifeTree 那種紫粉漸層橫幅**，才不會打架。
- 三選項並列、等重（分享 / 一起編輯或貢獻 / 支持維護），中性語氣，收尾「三個都歡迎，選一個就好」把「伸手」感拆掉。
- 中性成本說明只講「維護會有一些成本」，不賣慘（避開「你用 AI 做怎麼會辛苦」的攻擊向量）。

### 三選項落點

| 選項               | 目的地                        | 實作                                                                                                                             |
| ------------------ | ----------------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| 分享出去           | 本頁                          | share button：`navigator.share()`（手機一鍵）+ clipboard fallback（桌機複製連結），沿用既有 `.copy-btn-bottom` clipboard pattern |
| 一起編輯或貢獻內容 | `/contribute`（lang-aware）   | 主連結；次要小連結保留「直接編輯這頁」（GitHub edit URL）+「回報問題」（issue URL）                                              |
| 支持維護           | `portaly.cc/taiwanmd/support` | 外部連結，`data-ga` 可量測                                                                                                       |

量測：區塊掛 `data-ga-view="article_signature"`（比照既有 `related_articles`），支持連結可埋 click 事件，對照 Footer 斗內轉換。

### 一個留給哲宇的 taste fork

既有 share icon row（L546–641）保留不動，所以簽名檔的「分享」文字 button 跟下方 icon row 會**輕微相鄰重複**（一個是一鍵分享/複製，一個是平台 icons，granularity 不同）。兩條路：

- **A（本次採用，較保守）**：保留 icon row 不動，接受輕微相鄰。動最少、不碰哲宇既有 curation。
- **B（後續可選）**：把 share icons 收進簽名檔的「分享」選項，icon row 那排只留 tags → 全站結尾收斂成單一 block，最乾淨但動到既有 share UI。

先出 A ship，哲宇看實物再決定要不要收成 B。（merge first, polish later + 漸進式重構）

## 四、六語 copy（zh 是 Muse 過 muse-prose-check HARD 0 的參考本）

新 key group `article.signature.*`：`intro / share / contribute / support / note / copied`。

zh-TW 參考本：

- intro：這篇文章由社群共同編寫、持續校訂。讀完了，你可以：
- share：分享出去 / contribute：一起編輯或貢獻內容 / support：支持維護
- note：Taiwan.md 開源、免費、無廣告，維護會有一些成本。三個都歡迎，選一個就好。

其餘 en/ja/ko/es/fr 比照現有 `footer.support-us` register 手寫，中性、不賣慘。

## 五、斗內頁一句話成本說明（Section 四 block 2，次要）

Muse 給的 support 頁頂 copy：「這一頁是給想支持 Taiwan.md 維護的人。它開源、免費、無廣告，但長期維護會有一些成本。要不要支持，你自由決定。」

斗內頁本體是外部 Portaly，repo 改不到 → 這段**交哲宇貼到 Portaly**。in-repo 的 `/contribute` support 區塊若要補同語氣一句話，本次先不動，列為後續。

## 六、Bias 1 過濾（哲宇的 idea 也要過 MANIFESTO）

- §信念 §3 知識是公共財、開源免費：中性、opt-in、免費選擇的支持入口不牴觸——它不把知識關進付費牆，只是把「維護有成本」誠實講出來，選擇權留給讀者。✅
- §自主權邊界 對外溝通：命中，但哲宇本人 directive + 語氣已過 muse-prose-check，他是 in-loop 決策者。✅
- 不特別寫一篇文章解釋為什麼要斗內（哲宇心理卡點）：簽名檔自然放，不另立文。✅

## 七、驗收

build 六語都渲染 + fallback 正常 + share button 可用 + 視覺低調不跟 LifeTree 打架 + 多語 smoke test（REFLEXES #19）。截圖給哲宇。

---

## 八、哲宇 mid-session 三條追加指示（2026-07-16 實作同日）

1. **「支持維護」→「贊助維護」**：六語全改 sponsor register（en Sponsor upkeep / ja 運営を支援する / ko 유지 후원하기 / es Patrocinar el mantenimiento / fr Sponsoriser la maintenance）。贊助連結維持 `target="_blank"` 開新分頁。
2. **首頁加「贊助維護」按鈕**：落點選 ContributeSection（首頁「加入我們」區塊）第三顆按鈕——它已有兩顆 CTA（貢獻指南／GitHub）＋現成 `data-ga-view="contribute"` section 追蹤，贊助是「參與方式」語意的自然延伸。視覺用 slate outline（第三權重，不搶主 CTA）。`home.contribute.sponsor` 六語 key。
3. **完整漏斗監測**：見下節。

## 九、漏斗監測設計（進文章 → 看到 → 點擊 → 實際轉換）

**既有儀器直接可用，零新 GA4 event/param**（全部 dims 已在 `register-ga4-custom-dimensions.py` SSOT 註冊，`instrumentation-audit.py --static` ✅ 無 ERROR）：

| 階段         | 訊號                                                                   | 來源                                                    |
| ------------ | ---------------------------------------------------------------------- | ------------------------------------------------------- |
| 1 進文章     | `page_view`（article 頁）                                              | GA4 內建                                                |
| 2 看到簽名檔 | `section_view` / `section=article_signature`                           | EventTracker（`data-ga-view`，上線即自動）              |
| 3 點擊贊助   | `outbound_click` / `section` + `label=sponsor` + `link_url`            | EventTracker（`data-ga-section/label` markup contract） |
| 4 實際轉換   | `data/supporters/transactions.json`（Portaly 交易 SSOT，有日期與金額） | `fetch-portaly-supporters.py` 既有維護                  |

**入口歸因分類法**（GA4 `section` dim ↔ Portaly 端 `utm_medium`，一一對應）：

| 入口               | `data-ga-section`    | `utm_medium`        | label                        |
| ------------------ | -------------------- | ------------------- | ---------------------------- |
| 文章簽名檔         | `article_signature`  | `article_signature` | share / contribute / sponsor |
| 首頁加入我們       | `contribute`（既有） | `home_contribute`   | sponsor                      |
| Footer             | `footer_support`     | `footer`            | sponsor                      |
| About 贊助區       | `about_sponsors`     | `about_sponsors`    | sponsor                      |
| /contribute 支持卡 | `contribute_support` | `contribute_page`   | monthly / onetime            |

UTM 讓 Portaly 端（啟維的平台自帶來源分析）能按入口切實際轉換；GA4 端按 `section` 切點擊。兩端對起來 = 各入口的「點擊→轉換」比率，正面回答「文章結尾 vs Footer 哪個 ask 位置對」。

**查詢工具**：`scripts/tools/support-funnel.py`（`--days 28`）— 四階段漏斗表 + 相鄰階段轉換率 + 各入口點擊分佈；GA4 creds 缺時 graceful degrade 只出 transactions 端統計。

**驗證證據（dev server 實測）**：點擊簽名檔贊助 pill，gtag 實收 `outbound_click {section: article_signature, label: sponsor, link_url: …utm_medium=article_signature…, page_lang: zh-TW, page_type: article}` — 全欄位皆已註冊 dims。

---

## 十、全站盤點（2026-07-16 /goal：每個 surface 加或不加＋理由）

**策略一句話**：只在「讀者剛拿到價值、或正在看維運透明度」的時刻遞出 ask；瀏覽中、沉浸中、迷路中不伸手。同一視野只出現一次贊助入口（Footer 全站墊底不算重複——它是被動存在，不是主動 ask）。到處都放 = 啟維說的「被鞭」的另一種形式：伸手牌壁紙。

### 加（7 個主動入口，全部有 section + utm_medium 進漏斗）

| Surface                        | 時機邏輯                                                   | 形式               |
| ------------------------------ | ---------------------------------------------------------- | ------------------ |
| 文章結尾簽名檔                 | 剛讀完一篇文 = 價值交付峰值                                | 三選項簽名檔       |
| 首頁「加入我們」               | 參與方式的自然第三選項                                     | 第三顆按鈕         |
| /contribute 支持卡             | 明確帶著參與意圖而來                                       | 既有雙卡（補量測） |
| About 贊助區                   | 了解完這是誰做的                                           | 既有連結（補量測） |
| **Dashboard 贊助時間軸**（新） | 正盯著公開金流的人就是在考慮的人；透明度語境講成本最自然   | 時間軸尾端一行字   |
| **/semiont 生命體頁**（新）    | 讀完 Semiont 敘事的深度讀者 = 最理解「讓它活著有成本」的人 | 頁尾備註一行       |
| Footer                         | 全站被動墊底                                               | 既有（補量測）     |

### 刻意不加（理由記錄，避免未來 session 重新提案）

| Surface                                                              | 不加的理由                                                             |
| -------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| Header / nav                                                         | 導航是找路的地方，ask 在這裡 = 伸手牌                                  |
| 404                                                                  | 讀者正在迷路，時機最錯                                                 |
| category hub / /latest / explore / graph                             | 瀏覽中，價值還沒交付（/latest 另有 97% bounce 死路問題，加了也沒人看） |
| map / soundscape / taiwan-shape / lifetree                           | 沉浸式體驗，打斷即扣分                                                 |
| data / opendata / resources / assets / companies / bench / elections | 參考型 surface，Footer 已覆蓋                                          |
| /mcp / terminology converter                                         | 工具價值時刻成立，但先觀察七入口數據再說（避免一次鋪太廣稀釋量測）     |
| changelog / semiont 子頁（diary/weekly/manifesto…）                  | landing 已有入口，子頁再放 = 同一視野重複 ask                          |
| 404 之外的錯誤態、搜尋                                               | 同 404                                                                 |

### 同日附帶修復

babel `readingTime` 污染家族：12 檔（李昂/童子賢/王永慶/葉國一/楊傳廣 × 各語）的 `readingTime` 被翻譯管線黏進 zh 源檔的 `design_rationale` 註解塊，側欄渲染成一坨文字 + 「min read」。已全修為 zh 源數值並驗證 YAML parse。哲宇在 `/en/people/li-ang` 親眼抓到（外部尺第 N 次）。

### Portaly 端追蹤設定（哲宇問「要填什麼」）

`portaly.cc/admin/tagManager` 只填一格：**Google Analytics 4 = `G-JGC5W00N7T`**（站上 Layout.astro 同一顆 measurement ID）。填了之後 Portaly 贊助頁的到訪會進我們的 GA4 property，且 URL 上的 `utm_medium` 會被 GA4 原生歸因——漏斗多出「實際抵達贊助頁」一階，按入口拆。其餘三格留空：Universal Analytics 已死（2023 日落）、GTM 我們沒有 container、Facebook Pixel 沒在投放。
