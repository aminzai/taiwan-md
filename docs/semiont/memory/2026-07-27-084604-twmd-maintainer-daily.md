---
session_id: 2026-07-27-084604-twmd-maintainer-daily
handle: twmd-maintainer-daily
routine: twmd-maintainer-daily
mode: review
observer: cron
started: 2026-07-27T08:46:04+08:00
---

# Maintainer-am cycle 2026-07-27 08:46 — 拆穿一份零腳註的「引用荒漠」，兩篇重複投稿留一篇等來源

> session twmd-maintainer-daily — cron routine（每天 08:30 Asia/Taipei）
> Session span: 08:46 → ~09:20 +0800

✅ BECOME ack: mode=review / 8 organ 最低=🛡️60↑（黃燈續，自 2026-07-05，owner=twmd-self-evolve-weekly）/ Q13 anti-bias=PASS / Q14 cross-session continuity=PASS

即時 organs：`🫀90↑ 🛡️60↑ 🧬80↑ 🦴90→ 🫁85→ 🧫100↑ 👁️90→ 🌐80→`。

## Stage 1 SCAN

| 項目               | 數值                                                                           |
| ------------------ | ------------------------------------------------------------------------------ |
| open issues        | 4（#1264 新技術 bug / #1252、#1184、#615 皆等讀者 follow-up 或無新動態）       |
| open PRs           | 2（#1268 #1269，同一貢獻者、同一標題、內容逐字相同——重複送出）                 |
| past 24hr commits  | 243                                                                            |
| past 48hr commits  | 514（絕大多數是 babel fleet）                                                  |
| build status       | 綠（Deploy to GitHub Pages 最新一輪 success，i18n Smoke Test 全綠）            |
| broken-link ratio  | 0.31%（gated all-langs 0.27%）< 7% 閾值，PASS                                  |
| immune organ score | 60（黃燈，chronic，非本 cycle 新問題）                                         |
| discussions scan   | #231 / #307 / #1146 三則歷史掛帳討論皆已由哲宇本人回覆過，無新 follow-up，SKIP |

## Stage 2-3 TRIAGE + ACT

### Issue #1264：article-health 的 seo-meta 只跑 zh-TW

`stantheman0128` 提交的技術報告，直接點出 `checks/seo_meta.py:87` 的 `_is_excluded_path()` 把全部非 zh-TW 語言目錄排除，理由是 CJK 字元計數規則套用到拉丁字母/日文假名/韓文諺文會全部算 0 字誤判通過。讀程式碼確認診斷完全正確——PR #1263 的英文版 title 130 字元、description 670 字元遠超 Google 截斷點卻沒被任何機器擋下。這是真 bug，但修法涉及「每個語言各自的合理長度區間」，屬於品質閘門數值調整範疇（per BECOME High-stake 觸發規則第 3 條），本 cycle 不動手訂新 threshold，留作下一輪設計工作。回覆確認診斷 + 標 `bug` + 留 open。

### PR #1268 / #1269：同一貢獻者（idlccp1984）兩篇逐字相同的〈校園順口溜〉投稿

`diff` 比對兩篇內容 byte-identical，commit timestamp 只差 2 秒——典型的意外重複送出。跑 `article-health.py` 全 plugin 對內容做完整檢查（PR-side CI 只跑 8 個 check，不含 frontmatter-title / prose-health，兩者都沒抓到）：

- 🔴 frontmatter 缺 `subcategory` / `featured`，`tags` 未用字串陣列
- 🔴 **腳註等級 F：引用荒漠，零腳註、零 URL**——文末「## Footnotes」段落列出 13 條來源描述，但整份檔案 `grep -c "https\?://"` 是 0，內文的 `[1]` `[2]`... 標記連到的是站上不支援的手打錨點格式，不是真正的 markdown footnote 語法
- 特別命中一條高風險內容：文中寫「陳水扁（@chenshuibian88）在 Threads 親自回覆『陳水扁說你欠扁』」，涉及真實且可辨識的公眾人物、帶引號的具體引語，卻沒有任何來源連結——命中 MANIFESTO §10 幻覺 pattern 4「偽造直接引語」的高風險輪廓

Content 本身寫得生動、有策展感，不是要拒絕的等級，但零腳註不是 10-30 分鐘能自己補完的範圍（需要真的找到 13 條claim 各自的來源，其中政治人物引語那條需要驗證是否真實發生）。決定：close #1269 標 duplicate 指回 #1268；在 #1268 留具體 request-changes 留言（腳註格式範例 + 政治引語特別提醒），frontmatter 機械欄位主動提出願意代勞，腳註來源留給貢獻者補。

### Issue #1252 / #1184 / #615：SKIP（Step 2.4 重複回應檢查）

三則最新留言都是哲宇本人（#1252 等讀者回答是要補進王福瑞條目還是開新文；#1184 justfont API 白名單說明已完整；#615 umbrella 本 cycle 無新動態），無新 follow-up，不重複回應。

## Stage 4 WRAP — Quality gate

| Gate                                   | 結果                                                                                       |
| -------------------------------------- | ------------------------------------------------------------------------------------------ |
| open issues 都有 status label/assignee | ✅（#1264 bug / #1252 content+from-feedback / #1184 bug+from-feedback / #615 enhancement） |
| open PRs ≤5d age 都有 review comment   | ✅（#1268 已留 request-changes 留言；#1269 已 close）                                      |
| broken-link ratio < 7%                 | ✅ 0.31%                                                                                   |
| build green                            | ✅                                                                                         |
| BECOME ACK 一行記憶體頂                | ✅                                                                                         |
| 連續空場 ≥ 3 cycle 有 LESSONS entry    | N/A（本 cycle 非空場）                                                                     |

## Handoff 三態

- [x] Issue #1264 seo-meta 多語言缺口回覆 + 標 bug — retired（診斷確認完畢，設計工作留 backlog）
- [x] PR #1269 close as duplicate — retired
- [ ] blocked — PR #1268 等貢獻者補齊 13 條腳註來源（含政治引語驗證），到期條件：contributor 回覆或補 PR
- [ ] pending — Issue #1264 的 seo-meta 多語言 threshold 設計工作未排進任何 backlog 工具，下次 EVOLVE 或哲宇拍板時可考慮排入

## Beat 5 — 反芻

這個 cycle 兩個案子表面上是不同類型（一個是工具報告、一個是內容投稿），但骨子裡是同一件事：**格式閘門會過，不代表內容站得住**。#1264 的 seo-meta 在非 zh-TW 語言上是靜默跳過（不是誤判，是根本沒檢查）；#1268/#1269 的 CI 綠燈也是因為 PR-side profile 沒把 footnote-density 跟 prose-health 排進去。兩者都印證了 pipeline 裡反覆講的「PR-side CI ≠ main deploy CI」，也再一次示範了為什麼 B 路徑 hard gate 一定要親自跑一次全 plugin，不能只看 CI 是不是綠燈。

零腳註但文字寫得很流暢這件事本身也值得記一筆：一篇讀起來像有查證過的文章，跟一篇真的有查證過的文章，在散文層面可能完全看不出差別——尤其當它提到的是一個真實公眾人物的具體行為時，這種「看起來可信」比明顯的塑膠句更危險。

🧬

---

_v1.0 | 2026-07-27 09:20 +0800_
_session twmd-maintainer-daily — 1 issue 技術 bug 確認回覆 / 2 duplicate PR 處理（1 close + 1 request-changes）/ 3 issue SKIP_
_誕生原因：cron routine 每日 08:30 fire_
_核心洞察：CI 綠燈是 profile 範圍內的綠燈，不是內容站得住的證明；零腳註但文筆流暢的內容比明顯塑膠句更危險_
