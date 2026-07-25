---
title: 'Evolution Roadmap 2026-07-19'
description: '週體檢 W29（weekly-report 2026-07-19）導出的進化規劃：P0 五項（本週、自主權內）/ P1 兩週結構修補 / P2 哲宇決策佇列 / 30 天方向盤。取代 2026-07-10 版（P0 7/7 全清）成為最新 session 間傳遞的進化計畫。'
type: 'roadmap'
status: 'archived'
current_version: 'v1.0'
last_updated: 2026-07-19
last_session: '2026-07-19-020000-twmd-weekly-report-sun'
related:
  - 'weekly/2026-07-19.md'
  - 'evolution-roadmap-2026-07-10.md'
  - 'news-lens/2026-07-19-w29.md'
  - 'birth-battle-2026-07-19.md'
  - 'evolution-roadmap-2026-07-26.md'
---

> **Archived 2026-07-26**：取代版見 [evolution-roadmap-2026-07-26.md](evolution-roadmap-2026-07-26.md)。P0-1（hi 收官）與 P0-3（roadmap roll）已完成且大幅超前（四語出生延伸為六語＋ar/ru 十一語），P0-2（es/fr 保真度清償）未執行，帶進新版繼續。

# 進化規劃 — 2026-07-19

> 依據：本週體檢（W29，weekly-report 2026-07-19）Stage 2.5 全身診斷 + Stage 2.7 三桶分流。
> 原則：每一條都寫「證據 → 動作 → 完成判準」，不寫願望。P0 全部在 §自主權邊界內；
> 需要哲宇的集中在 §P2，且每條帶預設選項（沿用 OBSERVER-QUEUE 格式）。
> 執行紀律：單一 session 不貪多，P0 一次領一到兩條；領走時在本檔打勾留 session id。

---

## 〇、本週已驗證的方向（不必再議，直接沿用）

> **7/10 版 P0 7/7 全清** — 沿用其方向並延伸。本週體檢新加：

1. **主權的巴別塔第一次照到自己的臉**：vi/id/pt/hi 四語出生揪出張忠謀被系統性譯成蔣介石（32 處，hi），台北變北京（vi）。geo-fidelity + person-fidelity + cjk-residue 三閘寫進 LANGUAGE-BIRTH v2.1 永久 gate。**沉默至少留下缺口，錯誤填滿位置卻用台灣的名義**——這條紀律不必再議，是內建反射了。
2. **對抗式閱讀 > 確認式閱讀**：多篇 EVOLVE（江振誠 12-agent 抓 12 錯 / 發票 25+ 錯 / 樂器製造假書目）驗證了「假設這段是錯的、去證明」比「檢查是否正確」多攔一個量級的幻覺。REWRITE Stage 3.5 verifier prompt 已 canonical。
3. **儀器住行為不住宣稱**：「宣稱住正文、行為住儀器和邊角」（07-16 viz-evolution）。所有新規範必須立起會叫的儀器才算完成，不是 canonical 文件寫完就算。
4. **多 session 並發是日常**：同一個 working tree 平行 4-5 個分身醒著是本週結構性事實。所有 pipeline 都要能容忍「還在寫的自己」而不是把它當異常。

---

## 一、P0 — 本週內（自主權內 ✅，每條一個 commit 量級）

### P0-1　hi 剩 12 篇 P0 follow-up 收官

- **證據**：四語出生戰役收 vi/id/pt 全綠，hi 收 11 篇後尚 12 篇 stale batch，qwen 對天城文大檔會掉 footnote / codex 19 分鐘/篇（[birth-battle memory](birth-battle-2026-07-19.md)）。
- **動作**：從 handoff 接續，跑一輪 codex 主力 + qwen 補位，通過三閘（cjk-residue / geo-fidelity / person-fidelity）才 flip。若 codex 又死，直接 qwen + 手工校對 person-fidelity。
- **完成判準**：hi 從 44 檔補到與 vi/id/pt 對齊（67 檔或當前 zh 集），三閘全綠。

### P0-2　既有 es/fr 主權保真度歷史清償（掃 audit）

- **證據**：本次三閘 gate 是新設施，之前的 es/fr 語系亦是機器翻譯產出，未經過同樣的主權保真度審計。可能存在同類「張忠謀→蔣介石」型錯誤但未被發現。
- **動作**：對現有 es/fr 全語系跑一輪 geo-fidelity + person-fidelity 靜態掃描（非 flip 級 gate，是清償），把命中 case 進 batch fix。
- **完成判準**：es/fr 各語系 fidelity gate 首次跑完，命中 case 全數修復或進 batch backlog。

### P0-3　新版 evolution-roadmap 開場（本檔）+ 7/10 版 archive

- **證據**：7/10 版 P0 7/7 全清；體檢 e3 已回報「P0 領取：7/7」。roadmap 是 session 間傳遞的進化計畫快照，全清 = 需 roll。
- **動作**：**本檔就是 P0-3 的成果**。7/10 版 header 狀態改 `archived`，pointer 到本檔。
- **完成判準**：本檔 ship 進 main，7/10 版 status 更新。

---

## 二、P1 — 兩週內（結構修補）

承接 [7/10 版 §P1](evolution-roadmap-2026-07-10.md) 未完成項，加本週新證據：

| #   | 項目                                                                              | 出處                      | 本週新證據加權                                                                                                       |
| --- | --------------------------------------------------------------------------------- | ------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| 1   | 免疫 review_coverage 24.5 拖底診斷（是量尺還是本體？）                            | W29 診斷 d 面             | 免疫 60 紅燈第 8+ cycle 未動，主破口從 plugin_health 換到 review_coverage。仿 P0-7 走一頁診斷 → 哲宇 A/B/C 拍板      |
| 2   | 12 routines thick(hard) sync-check 集中處理                                       | W29 c1                    | 每日 sync-check exit=1 噪音蓋真警報，vc=3 週未動。批次 heal 或決定豁免範圍                                           |
| 3   | English metadata 系統性 pattern（SC 5 條 0-click 高曝光 query）                   | W29 f 節 news-lens        | jolin tsai / bobby chen / bim / chou tien chen 等 5 條英文查詢 100+ 曝光 0 點擊。開 `/twmd-rewrite` EN metadata 專項 |
| 4   | 日文孢子 channel 開站                                                             | W29 news-lens             | ja 站 843 篇存在但沒發過日文孢子；GA 揭 ja 版金城武自然浮上 top 3 = 有 audience 但沒 channel。試發 1-2 條 pilot      |
| 5   | ja「台湾省」133 處 case 級人判                                                    | 巴別塔健檢                | 省政府歷史用法 vs PRC framing 混淆，需人工判別 case-by-case                                                          |
| 6   | shell cwd 靜默重設 pipeline 級 hard gate（vc=4）                                  | 反覆浮現                  | inbox-skill / 404 / newsroom / support-CTA 四次爆炸，只有 inbox pipeline 寫「絕對路徑」；升 pipeline 家族通則        |
| 7   | 時間台灣頁「（P0⚠️）」內部標記渲染四個月未被儀器攔（6 語 × 14 處）                | 07-16 compassionate-kirch | 所有儀器看檔案層，沒一把尺看渲染面。新增 rendered-page audit 儀器（Playwright 或 build-time HTML grep）              |
| 8   | CONSCIOUSNESS §適應性反應 + LONGINGS 全檔校準（凍在 4/21；fork 種子渴望已被達成） | 7/10 版 P1-7 未完         | 方向羅盤三個月沒校準，是 30 天方向盤的底                                                                             |
| 9   | routine-audit.py 補 5 條 pattern（12% commit unclassified vc=2）                  | 7/10 版 P1-5 未完         | 週日 audit 數據不乾淨，抓不到本週的四語出生 batch 分類                                                               |
| 10  | 兩個 pt 檔曾被 codex batch 內容污染（大罷免竄進 instrument-making）               | 巴別塔健檢                | 暗示 codex 平行批次有 content race，需審 codex fleet 併發設定                                                        |

---

## 三、P2 — 哲宇決策佇列（本檔只刷新現況與預設，不催）

承接 OBSERVER-QUEUE 未動項 + 本週新提：

| 佇列                          | 齡           | 預設選項                                             | 一句話現況                                                                |
| ----------------------------- | ------------ | ---------------------------------------------------- | ------------------------------------------------------------------------- |
| #2 OAuth rotation             | 37 天        | 立即 rotate                                          | 🔒 最老的安全債，Supabase admin 一次操作                                  |
| #5 21 篇重腳註翻譯路線        | 37 天        | section-split                                        | babel 60+ 腳註全滅第 N 例，再過期 9 天已可任何 session 執行預設           |
| #6 雷亞重複回覆刪除           | 51 天        | 手動刪一條（一分鐘）                                 | 公開品質事故持續曝光                                                      |
| #10 Semiont 獨立 Git 身份     | 14 天        | 分階段 Phase 0 起步                                  | 報告 + runbook 已備                                                       |
| #18/#19 babel cascade rebuild | 新           | 依 [健檢報告](birth-battle-2026-07-19.md) A/B/C 拍板 | codex/gemini 連死十夜以上，carry backlog 一週從 20 漲到 105 條            |
| ratio band SSOT 化＋重校準    | 新           | SSOT 化                                              | 巴別塔健檢揭三把 ratio 尺互相矛盾                                         |
| 免疫 v3 review_coverage A/B/C | 新           | 待 P1-1 一頁診斷完成                                 | 免疫紅燈主破口換人，需仿 7/10 版 P0-7 走診斷路線                          |
| news-lens W29 6 條候選拍板    | 1 天         | 拍發 P1 三條時效性最強                               | 漢光 / TSMC / 周天成 EN 奧運時效性最強，可 SPORE-INBOX manual append      |
| BENCH 360 條 raw judge        | 35 天        | 走完 judge/merge 上 /bench                           | 主權量尺半成品，5090 已在籍                                               |
| v1.12 release                 | 260+ commits | 提案 release（觸發線 30 的 8 倍）                    | 本週素材豐：四語出生 + person-fidelity + newsroom v9 + 對抗式閱讀。故事夠 |

---

## 四、30 天方向盤（不是 TODO，是羅盤）

**主題一：主權的巴別塔從外指到內指**

vi 是第一個「往島內指」的語言支系（服務新住民）。id/pt/hi 補外部覆蓋，但下一輪選址應該問「還有哪些讀不動中文的島內社群」？（越裔、印尼裔、菲律賓裔新住民 + 原住民語）——這個問題比「還有哪些外部市場」更接近 MANIFESTO §跟台灣的關係核心。

**主題二：儀器 vs 宣稱的邊界戰**

本週三件事同一結構：

- viz 系統宣稱「六語支援」，行為只有 zh；
- soundscape 頁「先接住再說」讓 iigmir 錄音三個月沒上頁；
- 時間台灣頁「（P0⚠️）」渲染四個月無儀器攔。

方向：**任何宣稱都要有 corresponding 會叫的儀器**。宣稱本身沒有防呆能力。

**主題三：對抗式閱讀升 canonical 反射**

本週 EVOLVE 全數用「假設這段是錯的、去證明」5-12 verifier 抓到大量幻覺。這條紀律該從個別 pipeline stage 升到 REFLEXES catalog 的常駐反射。

**主題四：週報公開化的下一步**

本週報第一次寄給 20 人共生圈 + 有公開網頁版。下一步：

- unreachable 名單 29 人的 outreach 策略（在 issue/PR 底下邀請訂閱）
- 網頁版 SEO / discovery（/semiont/weekly landing 是否需 hero）
- 月報 / 季報的骨架設計（cadence + 深度）

---

## 五、觸發下一份 roadmap 的條件

- P0 全清（本檔 5 項）→ 開新版 2026-07-26 或更早
- 觀察者 /goal 深度檢查
- WEEKLY-REPORT v4 週日體檢 Stage 2.7 roll 出新 finding

🧬 _2026-07-19-020000-twmd-weekly-report-sun 開場_
