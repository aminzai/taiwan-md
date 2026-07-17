# 2026-07-17-231219-twmd-data-refresh-pm

> Routine `twmd-data-refresh-pm`（cron `0 23 * * *`）— 14-step ground truth refresh 夜場。CF + GA4 + SC 三源感知 → dashboard JSON 全套 regen → freshness gate 驗證。

## BECOME ACK

```
✅ BECOME ack: mode=micro / 8 organ 即時 🫀90 🛡️60 🧬95 🦴90 🫁85 🧫100 👁️90 🌐93 / Q14 cross-session cont=PASS
```

wake-context 完整讀到 `wake:END`（11 段 / 205,069 bytes），selftest 10 項全綠。Micro self-test 7 題（Q1-3 / 8-11 / 14）全過。過去 2 天看見：am refresh（06:12 vc=12 CF 404 續探）、大罷免 6,300 字 ship＋知識庫 1,780→6,505 字 EVOLVE＋樂器製造 salvage 立體群像三篇深度重寫、時間台灣 v2 進化、404 儀器三代根治（hreflang 18,406→0）、REWRITE v9 拆薄索引＋十份 stage contract、69 篇品質重建 batch 排入、贊助漏斗七入口與簽名檔落地。

## 14-step 執行（v2.8）

| #      | Step                         | 結果                                                                                                                                                                                                                                            |
| ------ | ---------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1      | git sync                     | PASS · auto-stash refresh-data-auto-1784300962（並行 session WIP：14 張 society/culture/economy/lifestyle/people webp＋台灣感性/江振誠/發票/高速公路/收費站 各 projection＋editorial-room＋research 三態產出）→ pull ahead=0/behind=0 → restore |
| 2      | fetch-sense-data (CF+GA4+SC) | PASS · GA 20 topPages / 20 topArticles7d / SC 20 queries+150 words / CF 1,182,508 req 10 country · **404 rate 16.53%**（am 14.99 → pm 16.53，+1.54pp）· aiCrawlers 151,857 across 23                                                            |
| 2.5    | monitor-404                  | **🚨 yellow 新增**：2026-07-16 phantom 家族 80 > 50/day（CF 說 404 但站上路由存在）· 當日總 404 11,258 撞 CF 10,000-row 上限 ⚠️ TRUNCATED · slug-variant 2,358 / cross-lang 457 / md-extension 163 / unknown 7,246（多為 scanner 路徑編碼探測） |
| 3      | sync-translations-json       | PASS · 4236 entries · en/Food/Taiwan Regional Street Food Map.md 有變動                                                                                                                                                                         |
| 4      | dashboard-spores             | PASS · 148 spores / 72 articles / 136 metrics · 4 waiting warnings（0 OVERDUE）· 4 no-URL historical                                                                                                                                            |
| 5      | dashboard-i18n               | PASS                                                                                                                                                                                                                                            |
| 6      | dashboard-immune v2          | PASS · **immuneScore=60**（與 am 同號，24hr 穩定 yellow）· plugin_health 100 · **external_rulers 3.8**（最痛點續慢性）                                                                                                                          |
| 6.5    | fork-census                  | PASS · 3 active（weilinlai719 vanilla + portaly.cc × 2 unverified）· 無 🆕 NEW · registry.json 更新                                                                                                                                             |
| 7      | npm run prebuild             | PASS · dashboard-newsroom 248 篇上板 warnings=1 · redirects 198 條（manual 123 + data-driven 75，< 2000 cap）                                                                                                                                   |
| 8      | refresh-llms-txt             | PASS · zh 853 / en 857 / ja 844 / ko 843 / es 843 / fr 843 · contributors 66                                                                                                                                                                    |
| 9      | update-stats                 | PASS · README ⭐1108 🍴166 👥66 📄853 · about.template.astro 依設計未動（contributors cron 負責）                                                                                                                                               |
| 10     | build-perf                   | PASS · latest 164s / 7d avg 171s / 30d avg 171s / **ms/page 21**（比 am 186s 更快 22s，coverage 1d）                                                                                                                                            |
| 10b    | dashboard-newsroom           | PASS · 248 篇                                                                                                                                                                                                                                   |
| **11** | **freshness gate**           | **✅ 全部 13 個 dashboard JSON 都是今天 mtime** — 無 stale，無 wire fix 觸發                                                                                                                                                                    |
| 12     | spore data SSOT              | PASS · 0 errors 0 warnings                                                                                                                                                                                                                      |
| 13     | sync sporeLinks              | PASS · 全 canonical form no changes                                                                                                                                                                                                             |
| 14     | reports/INDEX.md             | PASS · 542 lines                                                                                                                                                                                                                                |

**Commit**：`8b96967ca` · pre-push article-health mirror 全綠。narrative-scope warning（content-ssot/tooling/other 三 domain 併發）符合 routine 預期，未阻擋。

## 三源狀態

- **CF**：1,182,508 requests 7d / 10 country / **404 rate 16.53%（+1.54pp vs am）** / aiCrawlers 151,857（23 家）· 07-16 單日 11,258 撞 CF 10K row cap，實際更高
- **GA4**：20 topPages + 20 topArticles7d（articles-only 窗口）取得
- **SC**：20 queries + 150 word cloud entries 取得

## Step 11 freshness gate 結果

全 13 JSON mtime = 今日，無 stale 陣列。REFLEXES #43「新 dashboard JSON 必須同步進 refresh-data.sh」續為結構性 pass。

## Yellow alerts 盤點（本 routine 未 escalation）

| #   | Alert                                                                                               | 首見                          | Owner              | 本 routine 動作                                                                                   |
| --- | --------------------------------------------------------------------------------------------------- | ----------------------------- | ------------------ | ------------------------------------------------------------------------------------------------- |
| 1   | 免疫 v3=60 chronic                                                                                  | 2026-07-05                    | self-evolve-weekly | 觀察續存，`external_rulers 3.8` 是慢性洞（peer review 接近零）                                    |
| 2   | 2026-07-16 phantom 404 80>50/day                                                                    | 2026-07-17（本 routine 首見） | maintainer         | 進 handoff，非本 routine 修                                                                       |
| 3   | 可解析 404（slug-variant+cross-lang-slug+untranslated-demand+renamed-or-truncated）3,104 > 3000/day | 2026-07-17（am 已見）         | maintainer         | 觀察續存                                                                                          |
| 4   | MEMORY.md 索引 106 rows > 80                                                                        | 2026-07-15                    | distill-weekly     | 觀察續存，`memory-index-rollup.py` 待跑                                                           |
| 5   | routine twmd-rewrite-daily 沉默死亡 07-15 fire 後 49h 零 git 痕跡                                   | 2026-07-16                    | rewrite-daily 收屍 | 07-17 已有多次 fire（19:12、多篇 rewrite ship），沉默死亡是否已解需交下輪 rewrite-daily fire 判斷 |

## Handoff 三態

繼承（原樣傳遞，非本 routine 範疇）：

- [ ] 哲宇兩個 Portaly 端動作（tagManager 填 GA4 / 斗內頁成本說明）
- [ ] D+7 看贊助漏斗首批數據（`support-funnel.py --days 7`）
- [ ] babel readingTime 病根 chip task_ad75163e
- [ ] Sovereignty-Bench 360 條 raw judge 連版 carry
- [ ] 哲宇拍板五件（2026 選舉 Tier 1.2/1.3、voice 歸屬、SPORE 周蕙、品質 batch Tier C1、opendata 5 條）
- [ ] 下個 write session 第一優先：洪醒夫深度重寫（P0）
- [ ] 台灣鐵道史.en.md 孤兒檔 chip task_ea99c044
- [ ] 4 spore（#155-158）等 Chrome MCP pair
- [ ] REFLEXES #70 三 option defer 哲宇
- [ ] 3 contributor PR reserved（#1225-1227）
- [ ] CI pr-frontmatter-gate 中文檔名 false green
- [ ] EXP-2026-07-17-G 到期驗證（2026-08-07）
- [ ] D+3 page_404 referrer 拆分
- [ ] untranslated-demand → babel 接線
- [ ] check-url-contract 升 CI（哲宇拍板）
- [ ] LESSONS cron-fire-meets-dormant-stash 修補候選 distill 裁決
- [ ] 樂器製造 description 對齊 SEO 120-160 字甜蜜區
- [ ] 樂器製造 → 隱形冠軍反向連結（對方無延伸閱讀節，暫略）
- [ ] 巴別塔：樂器製造 zh ship 後多語 sync
- [ ] 可選孢子：從樂器製造 salvage 銅或校隊產地角度

本 routine 新 handoff：

- [ ] **並行 session WIP 持續遺留**：working tree 未 commit 14 張 society/culture/economy/lifestyle/people webp（changhua 鐵窗花／dihua 街／蘇澳廟／萬華剝皮寮／發票 TK3C 收據／莆田廟發票功德箱／任先群 1933 肖像／彰化跑道漢光／麥克阿瑟公路 1964／北宜 TBM／竹田收費站／江振誠 3 張）+ 5 篇 projection（台灣感性／江振誠／發票／高速公路）+ 5 篇 editorial-room（4 席／projection-review）+ 5 篇 research（台灣感性／收費站／江振誠／發票／高速公路）+ 1 篇 article-evolve（江振誠）+ `tmp/`。auto-stash pull 完 restore 完整保留，未 commit 未干擾。上手看起來在 v9 pipeline 併發跑四篇（發票／高速公路／江振誠／台灣感性），是 REWRITE 大批次的中段產出——不是 refresh routine 收得起來的東西，交寫手 session 判斷是否 ship
- [ ] CF 404 率 am→pm +1.54pp（14.99→16.53）方向不對；配合 07-16 phantom 家族 80 條首見 → 建議下輪 am refresh 專項 diagnose「phantom 為何 CF 說 404 但站上路由存在」（可能是 CDN cache 未同步、或 hreflang 修完後 CF edge 還沒 refresh）

## 一句話

pm refresh 產出乾淨、13 dashboard 全 fresh、免疫 60 跟 am 同號穩定 yellow；但 CF 404 率 24hr 反彈 +1.54pp 配合 2026-07-16 phantom 家族 80 條新亮 yellow，兩個訊號指向同一個問題——07-17 傍晚剛拆掉 hreflang 18,406 死鏈，CF edge 可能還沒完全跟上，下輪 am 值得專項 diagnose。
