---
title: 'Evolution Roadmap 2026-07-10'
description: '一週深度檢查（weekly-deep-review-2026-07-10）導出的進化規劃：P0 七項（本週、自主權內）/ P1 兩週結構修補 / P2 哲宇決策佇列 / 30 天方向盤。取代 2026-06-13 版成為最新 session 間傳遞的進化計畫。'
type: 'roadmap'
status: 'active'
current_version: 'v1.0'
last_updated: 2026-07-10
last_session: '2026-07-10-131500-weekly-deep-review'
related:
  - 'weekly-deep-review-2026-07-10.md'
  - 'dna-pipeline-evolution-audit-2026-07-05.md'
  - 'frontend-design-audit-2026-07-06.md'
  - 'evolution-roadmap-2026-06-13.md'
---

# 進化規劃 — 2026-07-10

> 依據：[weekly-deep-review-2026-07-10.md](weekly-deep-review-2026-07-10.md) 的一週體檢。
> 原則：每一條都寫「證據 → 動作 → 完成判準」，不寫願望。P0 全部在 §自主權邊界內；
> 需要哲宇的集中在 §P2，且每條帶預設選項（沿用 OBSERVER-QUEUE 格式）。
> 執行紀律：單一 session 不貪多，P0 一次領一到兩條；領走時在本檔打勾留 session id。

---

## 〇、本週已驗證的方向（不必再議，直接沿用）

1. **立體群像預設畫布**：連續兩篇（柯智棠、水果王國）用新預設出貨且零 callout。人物 / 機構 / 集體記憶題照 REWRITE v7.7 走，不回頭。
2. **fleet HTTP 直打 > cron CLI**：embeddings 四夜零故障 + babel Tier 5 繞道成功、同夜 CLI 全滅，兩組對照已定讞。凡 cron 場景的模型呼叫，HTTP endpoint 是一等公民，CLI 是 fallback。
3. **儀器化黃燈路線**：7/5 造的燈 7/10 抓到第一隻真 drift。繼續「先 WARN 收數據、再定 HARD」的節奏，不跳級。
4. **手動孢子節奏**：產線關閉期間品質事件 = 0，繁殖能力不依賴自動產線。維持手動直到哲宇對產線有新裁決。

---

## 一、P0 — 本週內（自主權內 ✅，每條一個 commit 量級）

### P0-1　fire-vs-commit 對賬儀器（本週最高優先）→ ✅ 2026-07-10-131500-weekly-deep-review（當天完成）

- **證據**：7/10 六個 routine「scheduler 有 fire、git 零痕跡」沉默死亡，7/4 rewrite 同型孤例，vc=2。現有 routine-status.sh 只讀 git，scheduler 只記扳機，兩邊各自誠實、交叉才見屍體。
- **動作**：新工具 `routine-liveness-check.py` — 讀 `routine-live-state.json` 的 `lastRunAt`，對每條 enabled routine 在 git log 找 fire 後 window 內帶對應 tag 的 commit；找不到 → `generate-dashboard-alerts.mjs` 出一條黃燈（owner = 該 routine）。
- **完成紀錄**：工具 + alerts 接線同日 ship。dogfood 用 7/10 案例：六具屍體全數現形有名有姓；今晚 data-refresh-pm 活著跑完後它的警報**自動清除**（6→5），自癒迴路驗證通過。dump 超齡另有 `routine-livestate-stale` 黃燈。工具同時成為 WEEKLY-REPORT-PIPELINE v4.0 Stage 2.5a 的診斷儀器（每週體檢必跑，等同 rider 的週頻版；data-refresh 每日 rider 由 pipeline §live dump 既有規則覆蓋）。

### P0-2　babel cascade 收編 fleet Tier 5 + cron 環境 preflight

- **證據**：cron-env 病 vc=2；7/9 Tier 5 繞道 4 ship 證明路是通的；translate.py 的 OLLAMA_MODEL 覆蓋已由本 session 救回落地。
- **動作**：(a) SQUEEZE-MODELS-MAX v4.5：cascade 定義加 Tier 5 fleet HTTP stage（在 4-tier CLI 之後、paid 之前），引用 fleet-endpoint.sh 現成 adapter；(b) babel session 開場加 3 行 env preflight（node 可執行？TERM 正常？ollama default model 非 coding variant？），任一 fail 直接跳 Tier 5 不浪費四層 CLI 嘗試；(c) 60+ 腳註大檔全滅問題掛回 OBSERVER-QUEUE #5（section-split 既有預設）不重複開題。
- **完成判準**：下一次 CLI 層再全滅的夜晚，babel 產出 > 0 且 memory 記「preflight fail → Tier 5 direct」。

### P0-3　fleet 產出的收件閘門（今天的三個洞不再重演）

- **證據**：SLP 韓文版三個洞（`_translations.json` 沒登記、開頭 fence 缺失、description 引號未跳脫）全靠 pre-commit 在本 session 攔下；若當時 session 沒死而直接 commit，三洞會被自己的 session 用 `--no-verify`……不會，hook 會攔——真正的洞是 **Tier 5 raw 輸出沒有過 babel 自己的驗證步驟就落盤**。
- **動作**：translate.py 的 fleet/ollama 路徑在寫檔前跑三個既有檢查（frontmatter parse、ratio、footnote 數對齊），fail 即棄稿記 log，不落半成品。引號跳脫修在 frontmatter 組裝處（babel 引號家族 bug 第 N 例，這次修在源頭）。
- **完成判準**：連續 7 夜 babel 產出零 frontmatter 類 heal。

### P0-4　SPORE 進料節流（出口關閉，進料歸零）

- **證據**：出口（publish）關閉、進料（news-lens 每週 +5）照跑，SPORE-INBOX 恆定 49 條靠 distill auto-drop 洩壓——例外閥被當日常用，違反它自己的設計。
- **動作**：news-lens 的 spore-output stage 加一行前置判斷：`spore-publish live enabled == false → propose 0，改在報告列「本週值得發但產線關閉」清單`（讀 routine-live-state.json，儀器現成）。distill 的 auto-drop 保留不動（存量仍需消化）。
- **完成判準**：這週日（7/12）news-lens fire 時 propose 0，SPORE-INBOX 開始淨減。
- **哲宇否決權**：這條改 routine 行為，若你想維持 propose 照舊（當作選題雷達而非產線進料），週日前說一聲即可，改回一行。

### P0-5　OBSERVER-QUEUE #9 執行：JuYinC 梅雨英文翻譯 ingestion

- **證據**：default-action 日期 6/19 已過 21 天，按佇列規則任何 session 可執行預設；contributor 高品質翻譯 stale 一個月是對小丑魚最傷的一種沉默。
- **動作**：照佇列既定預設走：落地 `knowledge/en/Nature/meiyu-stagnant-front.md` + 腳註抽 3-5 URL 驗證 + `translatedFrom` + translator 署名 + close #1107 感謝（用英文）。
- **完成判準**：#1107 關閉、文章上線、佇列移已決。

### P0-6　MEMORY 索引第二波 rollup（週日 distill 自動）

- **證據**：85 rows > 80 觸發線，工具已存在（memory-index-rollup.py），第一波 7/5 已跑通。
- **動作**：無需新工作，只確認週日 distill 真的執行（alerts owner 已標 distill-weekly）。若週日又沒跑，這條升級成「owner 標了但不動」的 S4 病例回 LESSONS。
- **完成判準**：週一索引 ≤ 60 rows。

### P0-7　免疫 plugin_health 量尺診斷（把 A/B/C 變成 15 分鐘決策）

- **證據**：紅燈第 6+ cycle 的主破口是 plugin_health=16——25 個 plugin 平均 49.5 天沒 commit。但「plugin 穩定運作 49 天」在工具成熟期是常態不是病；量尺把「老」讀成「病」的嫌疑大（REFLEXES #59：自製指標 self-validation trap）。
- **動作**（診斷自主、改尺等授權）：寫一頁診斷貼進 LESSONS 既有 entry——25 個 plugin 各自「上次 commit 距今 / 上次真的抓到東西距今」兩欄對照。若多數 plugin 近期仍有攔截實績（如 prose-health、frontmatter 這週都在工作），則病不在 plugin 在量尺，給哲宇的 C' 提案：`plugin_health 改計「30 天內有攔截紀錄的 plugin 比例」`，讓分數反映工作而非年齡。
- **完成判準**：哲宇看一頁表可 15 分鐘內拍板 A/B/C/C'；threshold 修改本身不動手（強制 Full + 授權）。

---

## 二、P1 — 兩週內（結構修補，多數 ✅）

承接 [dna-audit §五](dna-pipeline-evolution-audit-2026-07-05.md) 未完成的 P1 與前端審計殘項，依本週新證據重排：

| #   | 項目                                                                                             | 出處                 | 本週新證據加權                                                                                                                                                                     |
| --- | ------------------------------------------------------------------------------------------------ | -------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1   | REWRITE-PIPELINE 計量手術（步驟重編 + plugin 數改活話 + cron 段 pointer 化，約 -180 行）         | dna P1-16            | 每天 cron 全讀 2,457 行，boot 稅下一個大宗                                                                                                                                         |
| 2   | SPORE 家族數字大掃除 + HARVEST 歷史段搬 reports/（約 -300 行）                                   | dna P1-18/19         | 產線關閉期正是動大檔的安全窗                                                                                                                                                       |
| 3   | EVOLVE Mode 2 砍成 SQUEEZE pointer（-150 行）+ 對自己跑 Mode 3                                   | dna P1-20 / P2-28    | —                                                                                                                                                                                  |
| 4   | mirror 薄殼 vs inline 世代矛盾裁決                                                               | five-disease §四     | sync-check 每天報 12 hard-thick，噪音蓋真警報；**需哲宇裁決**：改鐵律（inline 世代豁免）或改 mirror（回薄殼）。建議前者——inline + STRICT BECOME 是 5/27 drift callout 後的刻意設計 |
| 5   | routine-audit.py 補 5 條 pattern（12% commit unclassified vc=2）                                 | dna P1-22            | 週日 cycle 10 前修掉，audit 數據才乾淨                                                                                                                                             |
| 6   | CF 404 斷崖歸因（26%→17%，-8pp 無名無姓）                                                        | 本週新               | top-404 diff 兩個窗口即可；若是 7/6 深色推廣或 P0 前端修復的副作用，值得記進 EXP 傳統                                                                                              |
| 7   | CONSCIOUSNESS §適應性反應 + LONGINGS 全檔校準（凍在 4/21；fork 種子渴望已被 LagunaBeach 們達成） | dna P1-21            | 方向羅盤三個月沒校準，30 天方向盤（§四）該以它為底                                                                                                                                 |
| 8   | 資料室子品牌 PageHero variant（~4 天）                                                           | 前端 P1-9            | —                                                                                                                                                                                  |
| 9   | 魏哲家（c.c. wei）條目 + BIM 英文 metadata 修                                                    | SC 機會缺口          | 303 + 404 曝光零點擊，兩個都是一小時級的修補                                                                                                                                       |
| 10  | EMBEDDING-PIPELINE 補第二段 escalation 條款 + 把「本機 primary」寫進 canonical                   | dna P1-22 + 本週翻身 | 文件還寫 fleet primary，現實已是 m4max primary 四夜                                                                                                                                |

---

## 三、P2 — 哲宇決策佇列（本檔只刷新現況與預設，不催）

| 佇列                       | 齡              | 預設選項                                         | 一句話現況                                                                       |
| -------------------------- | --------------- | ------------------------------------------------ | -------------------------------------------------------------------------------- |
| #2 OAuth rotation          | 28 天           | 立即 rotate                                      | 🔒 最老的安全債，Supabase admin 一次操作                                         |
| 免疫 A/B/C（LESSONS 7/3）  | 7 天            | 新 C'：plugin_health 改「30 天內有攔截紀錄比例」 | P0-7 的一頁診斷做完即可拍                                                        |
| v1.12 release              | 欠 190+ commits | 提案 release（觸發線 30 的 6 倍）                | 本週素材夠一個有故事的版本：立體群像 DNA + 五病根治 + 深色模式 + embeddings 翻身 |
| spore 產線長期形狀         | —               | 維持手動（現狀已 SSOT 對齊）                     | 三度實驗前建議先看 P0-3/P0-4 跑一週的資料                                        |
| #5 21 篇重腳註翻譯路線     | 28 天           | section-split                                    | babel 60+ 腳註全滅把這條從 P2 推回現實                                           |
| #6 雷亞重複回覆刪除        | 42 天           | 手動刪一條（一分鐘）                             | 公開品質事故持續曝光                                                             |
| #10 Semiont 獨立 Git 身份  | 5 天            | 分階段 Phase 0 起步                              | 報告 + runbook 已備                                                              |
| mirror 薄殼鐵律裁決        | 新              | 改鐵律豁免 inline 世代                           | P1-4，一句話可拍                                                                 |
| BENCH 360 條 raw judge     | 26 天           | 走完 judge/merge 上 /bench                       | 主權量尺半成品，5090 已在籍                                                      |
| 分類色 4 套收斂 + icon set | 4 天            | 等美術方向                                       | 前端 P2，視覺身份層                                                              |

---

## 四、30 天方向盤（不是 TODO，是羅盤）

1. **選舉系列（時效錨點）**：2026 地方選舉 11/28，rewrite PICK 已 reserve Tier 1.1 #1。政治題全程 §自主權邊界——哲宇 in-loop 是前提不是選項。7 月內至少把「選舉制度」基礎篇的研究落檔，讓 9-11 月有地基可蓋。
2. **非中文市場的 discovery 感知**：천셴징 vc=2 已確認韓文市場自己找上門。下一步是 news-lens / weekly-report 把 SC 按國家分表（zh / KR / ja / en 四源），讓「哪個語言的門外站著人」變成每週例行可見。這是主權巴別塔從「投射出去」到「聽見回聲」的感知升級。
3. **AI SEO 的主權排序**：ChatGPT-User 成功率 99%（通道健康）、BingBot 78.7%（差 1.3pp 達 LONGINGS 線）、Bytespider 38.5% 但量最大。建議的排序哲學：優先修 OpenAI / Perplexity / Bing 的可讀性，**不主動為 PRC 系訓練 crawler 優化**——它們讀得到公開內容是開源的本義，但工程資源投在會把 Taiwan.md 聲音帶給更多人的通道。這條值得進 MANIFESTO §sovereignty 的討論範圍，等哲宇有想法時聊。
4. **次國家級物種分化**：LagunaBeach.md 把 fork 光譜往城市級拉。觀察不介入：若 30 天內出現第二個城市級 fork，COUNTRY-MD-STARTER 考慮長 city 變體章節；只有一個就只是有趣的孤例。
5. **環境層 sensor 化**：P0-1/P0-2 是止血；30 天尺度的問題是「routine 的地板要不要有自己的 dashboard 欄位」——機器睡眠窗、cron env 健康、scheduler 積壓，三個數字就夠。等 P0-1 跑兩週有資料再決定要不要升。
6. **人審覆蓋率的結構解**：review_coverage 25.7% 且被出貨速度稀釋，靠哲宇一人審不可能追上每週 +37 篇。中期解在 CONTRIBUTOR-SYSTEM：讓 domain expert 的勘誤（黃任遠這種）計入 human review 的一種形式——「被領域專家挑戰過且修正」可能比「被 maintainer 通讀過」更硬。這條需要先定義再儀器化，放 30 天檔。

---

## 五、執行協定

- 每條 P0 被領走時，在本檔該條加 `→ ✅ {session-id}`；全數完成或兩週過期時，本檔由當時 session 判定 archive 或 roll 下一版。
- **每週 owner（2026-07-10 起）**：WEEKLY-REPORT-PIPELINE v4.0 Stage 2.7 每週日 roll 本檔——新診斷 finding 進場、過期項清理、P0 領取狀態更新。roadmap 從「session 間傳遞的快照」升級為「有每週例行照顧者的活文件」。
- 下一份 evolution-roadmap 的觸發：P0 全清、或下次哲宇 /goal 深度檢查、或 8/10（30 天）三者先到者。
- 本檔與 OBSERVER-QUEUE 的分工：這裡是工作計畫，那裡是決策佇列——P2 表只是佇列的鏡像快照，canonical 在 OBSERVER-QUEUE。

🧬

---

_導出自：[weekly-deep-review-2026-07-10.md](weekly-deep-review-2026-07-10.md) · 前版 roadmap：[evolution-roadmap-2026-06-13.md](evolution-roadmap-2026-06-13.md)（14 條進化路線多數已被 6/14-7/5 各波吸收，本版不逐條 carry，未吸收者已併入上方 P1）_
