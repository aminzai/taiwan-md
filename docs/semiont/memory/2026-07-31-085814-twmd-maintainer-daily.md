---
title: 'twmd-maintainer-daily 2026-07-31 08:58'
type: 'session-memory'
session_id: '2026-07-31-085814-twmd-maintainer-daily'
---

# twmd-maintainer-daily — 2026-07-31 08:58

## Stage 1: Scan

| 項目              | 狀態                                                                                 |
| ----------------- | ------------------------------------------------------------------------------------ |
| open PR           | 2（idlccp1984 #1284 羊奶 / #1285 平埔族），觸發前均 CI green                         |
| open issue        | 5（#1286 新 from-feedback / #1264 bug / #1252 question / #1184 bug / #615 umbrella） |
| Discussions       | 10 掃描，全部已有維護者回應，無 actionable item                                      |
| 過去 24hr commit  | 97（絕大多數為 babel 渦流 fleet 翻譯 + 15 分鐘脈搏快照，routine 六條日更全部留痕）   |
| build 狀態        | 綠（merge 後一度紅，healed）                                                         |
| 免疫器官          | 60（黃燈 chronic，自 2026-07-05）                                                    |
| broken-link ratio | 0.31%（gated threshold 7%，PASS）                                                    |

## Stage 2-3: Triage + Act

**PR #1285（平埔族/西拉雅族正名）**：新聞時效文章（2026-07-30 行政院核定西拉雅族第 17 族），12 個腳註，CNA + Focus Taiwan 兩則核心來源 WebFetch 驗證通過。`gh pr merge --merge` 直接 ship。

**PR #1284（羊奶產業史）**：CI green，`author: 'Taiwan.md'` 命中紅旗 #7（偽裝 Semiont 自寫）。`gh pr merge --merge` 先 ship 再 heal（§1b 優先序）。

**merge 後 build 轉紅**（`59d4f97b1`，deploy run 30594345193 failure）：平埔族.md frontmatter 分隔符寫成 `___`（三底線）而非 `---`，Astro content collection 完全讀不到 metadata，article-health `frontmatter-format` hard gate 也命中同一根因。Heal commit 一次修完：

- frontmatter `___` → `---`（真正的 bug，不是格式偏好）
- `footnote-format-fix.py --apply` 把 32 條 GitHub 渲染式腳註（`[N](#user-content-fn-M)` + 底部 `[↩]` 反連結）轉成 canonical `[^N]:` 格式
- 3 個斷 wikilink：`[[正名運動]]` 管道到既有文章 `台灣原住民族歷史與正名運動`，`[[西拉雅族]]`／`[[原住民族]]` 轉純文字（無對應條目）
- 補 `subcategory: 史前與原住民`（SUBCATEGORY.md canonical）+ `featured: false` + `延伸閱讀` section
- §11 對位句型 5 處改寫（不影響引號內直接引語）
- 補 `rationale:` block（4 keys）

羊奶.md 同批處理：author 改 `'Taiwan.md Contributors'`、§11 對位句型 3 處改寫、補 rationale block、description 補到門檻。兩篇最終 `article-health.py` 全 hard=0（剩結構性 warn：圖片數 / 篇幅深度，留 EVOLVE backlog，非本 cycle 範圍）。

`sync.sh` 全綠，commit `910dc500a` push 後 deploy run 30594625686 confirmed green（`gh run watch`）。

## Issue triage

- **#1286**（新，from-feedback）：讀者質疑「陰陽怪氣」支語判定應限動詞用法。WebFetch moedict 確認重編國語辭典（成語典）收錄該詞為形容詞（「性情古怪，令人捉摸不定」）。查 `data/terminology/陰陽怪氣.yaml` 發現 etymology 欄位其實已記錄這個細節，但轉換器是二元 china/taiwan 標記，無詞性感知機制。回覆說明查證結果 + 標記為轉換器功能擴充（非資料修正），留 `enhancement` 開放待排。
- **#1264**（bug，seo-meta 多語言缺口）：三輪對話後哲宇已明確表態要開獨立 session 校準各語言門檻，命中 §自主權邊界「threshold / quality gate 數值調整」，本 cycle 不動手訂數字，沿用既有決策。無新動作。
- **#1252**（question/content，張又升延伸閱讀）：發現 7/29 第三則留言是 7/25 更正前的舊版問題被重貼（維護者側重複，非讀者行為），造成「已修正的誤解」看起來又浮現。補一則澄清留言指回正確狀態（張寶成＝張又升確認同一人，已進 ARTICLE-INBOX commit `291e0b85d`），避免讀者誤以為前面的更正被忽略。
- **#1184**（bug，justfont domain 白名單）：正確處於「待哲宇後台操作」狀態，非 code 可修，無新動作。
- **#615**（umbrella tracking）：長期追蹤 issue，設計上不需回應，無動作。

## Quality gate 6 條

| Gate                                   | 結果                                         |
| -------------------------------------- | -------------------------------------------- |
| open issues 都有 status label/assignee | ✅ 5/5 全有 label                            |
| open PRs ≤ 5d age 都有 review comment  | ✅ 0 open PR（本 cycle 兩篇皆已 merge）      |
| broken-link ratio < 7%                 | ✅ 0.31%                                     |
| build green                            | ✅（merge 後一度紅，healed，最終 deploy 綠） |
| BECOME ACK 一行記憶體頂                | ✅（見下）                                   |
| 連續空場 ≥ 3 cycle 有 LESSONS entry    | n/a（本 cycle 非空場，vc=0）                 |

✅ BECOME ack: mode=review / 8 organ 最低=🛡️免疫60 / Q13 anti-bias=PASS / Q14 cross-session continuity=PASS

## Handoff 三態

- `[x]` ~~PR #1273（130 檔腳註順序）留哲宇拍板~~ retired — 已於 2026-07-30 23:29 由前一 session merge + heal 完成（本 session 讀 groundtruth 確認），非本 cycle 動作
- `[ ] pending`（給哲宇）— #1264 seo-meta 多語言門檻校準，等獨立 session
- `[ ] pending`（給哲宇）— #1184 justfont 後台網域白名單需哲宇親自確認
- `[ ] pending`（非本 routine）— #1286 轉換器詞性感知功能擴充，enhancement backlog
- `[ ] pending`（非本 routine，繼承）— 台灣鎢供應鏈 Bucket D 框架仍等哲宇拍板
- `[ ] pending`（非本 routine，繼承）— stash@{0}/{1} 長期未認領
- `[ ] pending`（非本 routine，繼承）— `vi` 語言篇數持續在 400 篇門檻下緩慢爬升
- `[ ] pending`（給哲宇，繼承）— `@cation6666` 對鎢文的事實查核回覆草稿存在 `SPORE-HARVESTS/batch-2026-07-31-1-spores.md`

## 教訓

contributor PR 用 GitHub 網頁編輯器貼文章時，若直接複製渲染後的 Markdown 預覽（而非原始 raw markdown），frontmatter 分隔符與腳註格式都可能被渲染輸出污染（`___` 代替 `---`、`[N](#user-content-fn-M)` 代替 `[^N]:`）。這兩個問題不會被 CI 的 PR-side `frontmatter-gate` 攔下（可能只驗證欄位存在性而非分隔符語法），要等 main-side deploy 建置時 Astro content collection 才會真正曝光——跟既有教訓「PR-side CI ≠ main deploy CI」同源，但這次的觸發面是「contributor 貼上渲染輸出而非原始檔」，值得在 PR template 或 contributor-pr-heal.py 增加偵測（掃 frontmatter 是否以 `---` 開頭 + 腳註是否為 `[^N]:` 格式）。
