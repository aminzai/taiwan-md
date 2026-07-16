# 2026-07-17-061224-twmd-data-refresh-am

> Routine `twmd-data-refresh-am`（cron `0 6 * * *`）— 14-step ground truth refresh。CF + GA4 + SC 三源感知 → dashboard JSON 全套 regen → freshness gate 驗證。

## BECOME ACK

```
✅ BECOME ack: mode=micro / 8 organ 即時 🫀90 🛡️58 🧬95 🦴90 🫁85 🧫100 👁️90 🌐93 / Q14 cross-session cont=PASS
```

wake-context 完整讀到 `wake:END`（11 段 / 197,900 bytes），selftest 10 項全綠。Micro self-test 7 題（Q1-3 / 8-11 / 14）全過。過去 2 天看見：embeddings-nightly（05:17 4941 向量）、大罷免 v9 全程 ship（6,300 字重建 + newsroom 拆檔 + Workflow 首測）、時間台灣 v2 進化、69 篇品質重建 batch 排入、贊助漏斗七入口與簽名檔落地。

## 14-step 執行（v2.8）

| #      | Step                         | 結果                                                                                                                                                  |
| ------ | ---------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1      | git sync                     | PASS · auto-stash refresh-data-auto-1784239805（前手 WIP：SEO.astro / i18n / 高等教育 research）→ pull ahead=0/behind=0 → restore                     |
| 2      | fetch-sense-data (CF+GA4+SC) | PASS · GA 20 topPages / 20 topArticles7d / SC 20 queries+150 words / CF 1,277,292 req 10 country · **404 rate 14.99%** · aiCrawlers 140,594 across 21 |
| 3      | sync-translations-json       | PASS · 4237 entries · ko/Economy/taiwan-stock-market.md 新入                                                                                          |
| 4      | dashboard-spores             | PASS · 148 spores / 72 articles / 136 metrics · 4 waiting warnings（0 OVERDUE）                                                                       |
| 5      | dashboard-i18n               | PASS                                                                                                                                                  |
| 6      | dashboard-immune v2          | PASS · **immuneScore=60**（前夜 58，+2 微升）· plugin_pass 70 · plugin_health 100 · citation 91.4 · **external_rulers 3.9**（最痛點）                 |
| 6.5    | fork-census                  | PASS · 3 active（weilinlai719 vanilla + portaly.cc × 2 unverified）· 無 🆕 NEW · registry.json 更新                                                   |
| 7      | npm run prebuild             | PASS · dashboard-newsroom 241 篇上板 warnings=1 · latest.json 180 entries × 6 langs                                                                   |
| 8      | refresh-llms-txt             | PASS · zh 853 / en 857 / ja 844 / ko 844 / es 843 / fr 844 · contributors 66                                                                          |
| 9      | update-stats                 | PASS · README ⭐1108 🍴166 👥66 📄853 · about.template.astro 依設計未動（contributors cron 負責）                                                     |
| 10     | build-perf                   | PASS · latest 186s / 7d avg 182s / 30d avg 182s / **ms/page 24**                                                                                      |
| 10b    | dashboard-newsroom           | PASS · 241 篇                                                                                                                                         |
| **11** | **freshness gate**           | **✅ 全部 13 個 dashboard JSON 都是今天 mtime** — 無 stale，無 wire fix 觸發                                                                          |
| 12     | spore data SSOT              | PASS · 0 errors 0 warnings                                                                                                                            |
| 13     | sync sporeLinks              | PASS · 全 canonical form no changes                                                                                                                   |
| 14     | reports/INDEX.md             | PASS · 537 lines                                                                                                                                      |

## 三源狀態

- **CF**：1,277,292 requests 7d / 10 country / **404 rate 14.99%（續 plateau，前夜 vc=12 加碼觀察，本次未新增 diagnostic）** / aiCrawlers 140,594（21 家）
- **GA4**：20 topPages + 20 topArticles7d（articles-only 窗口）取得
- **SC**：20 queries + 150 word cloud entries 取得

## 免疫 v3=60 拆解（+2 續漂 yellow）

component 掃描（**外部尺 3.9 是慢性洞**）：

- `external_rulers 3.9`：peer review 外部注視接近零。這是免疫拖累主因，非本 routine 範疇（owner=self-evolve-weekly + 觀察者策略）。
- `plugin_pass_rate 70`：11 檢查工具的 pass ratio，尚未回 80+ 門檻。
- `review_coverage 24.5`：human-reviewed 覆蓋率一直卡個位 20%。
- `tool_freshness 60`：工具 mtime 中位數。
- 其餘 citation 91.4 / plugin_health 100 / drift_velocity 90 健康。

三個 yellow 全部續存，本 routine 純觀察不 escalation：

- **免疫 v3=60** 續漂 owner=self-evolve-weekly（自 2026-07-05）
- **MEMORY inline 92>80** owner=distill-weekly（自 2026-07-15）
- **rewrite-daily 07-15 沉默死亡** owner=rewrite-daily 收屍（自 2026-07-16）

## Handoff 三態

繼承（原樣傳遞，非本 routine 範疇）：

- [ ] 哲宇兩個 Portaly 端動作（tagManager 填 GA4 / 斗內頁成本說明）
- [ ] D+7 看贊助漏斗首批數據（`support-funnel.py --days 7`）
- [ ] babel readingTime 病根 chip task_ad75163e
- [ ] Sovereignty-Bench 360 條 raw judge 連版 carry
- [ ] 哲宇拍板五件（2026 選舉 Tier 1.2/1.3、voice 歸屬、SPORE 周蕙、品質 batch Tier C1、opendata 5 條）
- [ ] 下個 write session 第一優先：洪醒夫深度重寫（P0）
- [ ] 台灣鐵道史.en.md 孤兒檔 chip task_ea99c044
- [ ] **前手 WIP 未接住**：working tree 遺留 `src/components/SEO.astro` + `src/i18n/about.ts` + `src/i18n/home.ts` 三 M + 高等教育研究兩份（`reports/research/2026-07/台灣高等教育擴張與退場{,-gapfill}.md`）+ 四張 society webp + `reports/dogfood-v9-run2-highered-2026-07-16.md` + `tmp/`。本 routine auto-stash pull 完 restore 完整保留，未 commit 未干擾。上手 session 收官時漏了收，接手者請確認是否需要 ship（看 dogfood-v9-run2 標題像是大罷免後的第二輪 v9 產出）

本 routine 新 handoff：

- [ ] 無 escalation。免疫 60 微升 +2 但仍 <80，續 yellow 屬預期。三 yellow 各有 owner。CF 404 14.99% plateau shape 續探（前夜 pm 已 vc=12，非本 routine 範疇）。

## 一句話

免疫 60（+2）微升是分子被大罷免 3,300 字外部連結拉起的錯覺，分母 external_rulers 3.9 才是慢性洞——今晨 refresh 產出乾淨，但 working tree 遺留前手一整份 v9 run2 高等教育產出沒交接，是「收官三態」在跨 routine 邊界的隱形斷點。
