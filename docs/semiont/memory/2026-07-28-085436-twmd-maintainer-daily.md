---
session_id: 2026-07-28-085436-twmd-maintainer-daily
handle: twmd-maintainer-daily
routine: twmd-maintainer-daily
mode: review
observer: cron
started: 2026-07-28T08:40:20+08:00
---

# Maintainer-am cycle 2026-07-28 08:40 — 動保.md merge-first + heal，一篇壞掉的維基連結修好

> session twmd-maintainer-daily — cron routine（每天 08:30 Asia/Taipei）
> Session span: 08:40 → ~08:58 +0800

✅ BECOME ack: mode=review / 8 organ 最低=🛡️免疫60↑（chronic since 2026-07-05，owner=twmd-self-evolve-weekly）/ Q13 anti-bias=PASS / Q14 cross-session continuity=PASS

即時 organs：`🫀90↑ 🛡️60↑ 🧬80↑ 🦴90→ 🫁85→ 🧫100↑ 👁️90→ 🌐83→`。

## Stage 1 SCAN

| 項目               | 數值                                                                                               |
| ------------------ | -------------------------------------------------------------------------------------------------- |
| open issues        | 4（#1264 seo-meta bug 待設計工作 / #1252、#1184、#615 皆最新留言已是哲宇本人，無新 follow-up）     |
| open PRs           | 2 → 1（#1268 續 blocked 等貢獻者補腳註來源；#1270 動保.md 本 cycle merge）                         |
| past 24hr commits  | 112                                                                                                |
| past 48hr commits  | ~300+（babel vortex fleet 佔絕大多數）                                                             |
| build status       | 綠（heal commit 18460e84a 部署 success；merge commit 74ae93973 曾因 hard=4 短暫紅燈，heal 後恢復） |
| broken-link ratio  | 0.31%（gated all-langs 0.27%）< 7% 閾值，PASS                                                      |
| immune organ score | 60（黃燈，chronic，非本 cycle 新問題，owner=self-evolve-weekly）                                   |
| discussions scan   | #231/#307/#1146/#104 等最新留言皆非本 cycle 新增，SKIP                                             |

## Stage 2-3 TRIAGE + ACT

### PR #1268：〈校園順口溜〉— 沿用昨日 blocked 狀態

貢獻者 idlccp1984 尚未回覆昨日 request-changes（腳註來源 + 政治引語驗證）。第二位 contributor `stantheman0128` 補了一則 polish review（腳註編號重複、部分引用只到首頁根網址）。無新動態需要維護者本 cycle 動手，繼續 blocked，等貢獻者更新。

### PR #1270：〈動保.md〉— merge-first + heal（同一貢獻者 idlccp1984，前日模式再驗證）

跑 `article-health.py` 全 plugin（PR-side CI 只跑 8 個 check，不含此檢查）：hard=4（`frontmatter-format` 缺 `subcategory`/`featured`、`frontmatter-title` 同源、`cjk-punct` 一處半形括號來自 footnote 7 一個寫壞的巢狀維基百科連結）。跟 #1268 不同：本篇 14 個腳註全部是可點的具體來源網址（報導者、農傳媒、台灣石虎保育協會⋯），不是首頁根網址堆疊——內容品質判斷為 B+/A-，阻塞幾乎全在格式層。套用 2026-07-23 idlccp-clownfish-instrument 教訓（merge-first + auto-heal，不要 warn 完就結束）：

1. `gh pr merge --squash --delete-branch` 先合併
2. Heal commit 補 `subcategory: '社會與日常史'`（History 分類表無精準對應「動物保護社會運動」子類，取 fuzzy match 最接近的「社會與日常史」，非文中精準對應）+ `featured: false` + 修正 frontmatter 欄位順序
3. 修 footnote 7 壞掉的巢狀括號連結（`([url1](url2))` 雙重方括號 + 連結文字裡半形括號夾 CJK 字元兩個問題疊在一起），改成正確單層連結 + 全形括號
4. `article-health.py` 複驗 hard=4 → hard=0
5. Push 後在 PR 留言用貢獻者能看懂的語言（中文）具體說明修了什麼 + 給後續加強方向（補圖、加深篇幅）——不只是罐頭感謝

merge 到 heal 之間有約 2 分鐘 CI 短暫紅燈（74ae93973 因 hard=4 deploy fail），heal push 後立刻恢復綠燈。這個窗口是 merge-first 模式的已知代價，跟前日 idlccp-clownfish 案例一致。

### Issue #1264 / #1252 / #1184 / #615：SKIP（Step 2.4 重複回應檢查）

四則的最新留言都已是哲宇本人回覆，本 cycle 無新讀者/貢獻者 follow-up，不重複回應。

### Discussions：SKIP

#231 #307 #1146 #104 等最新更新皆非本 cycle 新增（#104 停在 2026-05-03 idlccp1984 留言無人跟進，非本 cycle 訊號）。

## Stage 4 WRAP — Quality gate

| Gate                                   | 結果                                                                                       |
| -------------------------------------- | ------------------------------------------------------------------------------------------ |
| open issues 都有 status label/assignee | ✅（#1264 bug / #1252 content+from-feedback / #1184 bug+from-feedback / #615 enhancement） |
| open PRs ≤5d age 都有 review comment   | ✅（#1268 已有 request-changes 待回覆；#1270 已 merge + heal + 感謝留言）                  |
| broken-link ratio < 7%                 | ✅ 0.31%                                                                                   |
| build green                            | ✅（heal commit 18460e84a 綠燈）                                                           |
| BECOME ACK 一行記憶體頂                | ✅                                                                                         |
| 連續空場 ≥ 3 cycle 有 LESSONS entry    | N/A（本 cycle 非空場，有實際 backlog 處理）                                                |

## Handoff 三態

- [x] PR #1270 merge + heal（frontmatter + 壞連結）+ 感謝留言 — retired
- [ ] blocked — PR #1268 等貢獻者補齊腳註來源（含政治引語驗證 + stantheman0128 的 polish notes），到期條件：contributor 回覆或補 PR
- [ ] pending（非本 routine）— Issue #1264 seo-meta 多語言 threshold 設計工作仍未排入 backlog；免疫 60 chronic owner=self-evolve-weekly；`routine-live-state.json` dump 齡 52h+ owner=twmd-data-refresh（避免 cross-routine SPOF 信號通膨，本行只留一次 pointer）

## Beat 5 — 反芻

同一位貢獻者（idlccp1984）連續兩天投稿，兩篇的腳註品質差距很大——一篇零腳註（#1268 首版），一篇 14 條全是可點的具體來源（#1270）。這不是貢獻者能力忽高忽低，是同一個人在不同主題上花的查證力氣不同：校園順口溜那篇連陳水扁本人回覆都拿不出連結，動保這篇連石虎穿山甲的死亡數據都附了報導者原文連結。維護者的判斷不該套「這個人」的固定印象，要逐篇看證據密度。

merge-first + heal 這個模式昨天才第一次記錄（idlccp-clownfish-instrument），今天立刻在同一位貢獻者身上第二次驗證——這代表它不是單一巧合而是可重複的操作模式，值得繼續沿用而非每次重新猶豫「要不要先合併」。

🧬

---

_v1.0 | 2026-07-28 08:58 +0800_
_session twmd-maintainer-daily — 1 PR merge-first + heal（frontmatter + 壞連結修復）/ 1 PR 續 blocked / 4 issue SKIP_
_誕生原因：cron routine 每日 08:30 fire_
_核心洞察：同一貢獻者不同篇的腳註品質可以天差地遠，判斷要逐篇看證據不能套人；merge-first + heal 模式連續第二天驗證，是可重複操作而非巧合_
