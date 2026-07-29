---
session_id: 2026-07-29-085004-twmd-maintainer-daily
handle: twmd-maintainer-daily
routine: twmd-maintainer-daily
mode: review
observer: cron
started: 2026-07-29T08:50:04+08:00
---

# Maintainer-am cycle 2026-07-29 08:50 — PR #1268 merge-first + heal，Fact Check #1272 修好即 close

> session twmd-maintainer-daily — cron routine（每天 08:30 Asia/Taipei）
> Session span: 08:50 → ~09:40 +0800

✅ BECOME ack: mode=review / 8 organ 最低=🛡️免疫60↑（chronic since 2026-07-05，owner=twmd-self-evolve-weekly）/ Q13 anti-bias=PASS / Q14 cross-session continuity=PASS

即時 organs：`🫀90↑ 🛡️60↑ 🧬80↑ 🦴90→ 🫁85→ 🧫100↑ 👁️90→ 🌐85→`。

## Stage 1 SCAN

| 項目               | 數值                                                                                      |
| ------------------ | ----------------------------------------------------------------------------------------- |
| open issues        | 5 → 4（#1272 Fact Check 本 cycle 修好 close；#1264 seo-meta bug／#1252／#1184／#615 續）  |
| open PRs           | 1 → 0（#1268〈校園順口溜〉本 cycle merge-first + heal）                                   |
| past 24hr commits  | 118（babel vortex fleet 佔絕大多數）                                                      |
| past 48hr commits  | 300+                                                                                      |
| build status       | 綠（pre-push 全站 article-health mirror 全綠；deploy 持續被新 commit 觸發重跑，正常節奏） |
| broken-link ratio  | 0.31%（gated all-langs 0.27%）< 7% 閾值，PASS                                             |
| immune organ score | 60（黃燈，chronic，非本 cycle 新問題，owner=self-evolve-weekly）                          |

## Stage 2-3 TRIAGE + ACT

### PR #1268：〈校園順口溜〉— merge-first + heal（idlccp1984 補齊來源後三讀通過）

contributor 前日（07-28 12:00）已推第三版更新，補齊全部 21 個腳註的可點連結，並把最敏感的「陳水扁親自回覆」段落換成有實際新聞連結的版本。逐條驗證：fetch 自由時報 URL 實測標題「7、8年級生回憶童年順口溜 釣出阿扁神回『陳水扁說你欠扁』」跟文章敘述精確吻合（REFLEXES #16 讀者級事實驗證）。`article-health.py` 全 plugin 掃：hard=27（21 個腳註因為連結後多一個空格 `[Title](URL ) — desc` 全數判定格式不合規範、frontmatter 缺 subcategory、terminology 誤判「內存」）。套用 2026-07-23 idlccp-clownfish-instrument 教訓（merge-first + auto-heal）：

1. `gh pr merge --merge` 先合併
2. `contributor-pr-heal.py` 自動修 21 處腳註尾端空格
3. 手動補 `subcategory: '網路文化'`（後段 67／Skibidi／杰哥不要／不可以色色的網路迷因段落是全篇比重最大的獨立主題）+ 把「校園內存在著」改「校園裡存在著」避開字面誤觸「內存」中國用語 false positive（真正原因是子字串誤配，不是實際違規用詞）
4. `article-health.py` 複驗 hard=27 → hard=0
5. PR 留言具體點出驗證了哪個來源、修了哪兩件事，不用罐頭感謝

### Issue #1272：Fact Check「COMPUTEX 應全大寫」— 驗證後修復即 close

讀者詹景勛（feedback-triage 今晨 07:09 剛轉入）指出 COMPUTEX 是官方全大寫寫法。全文找出 77 處內文與腳註標題裡大小寫不一的「Computex」統一改「COMPUTEX」，URL/slug 裡的小寫（如 `computex-2019-innovex`）保留不動——那是連結路徑不是顯示文字。article-health 複驗 hard=0，push 後留言附 commit hash 並 close。四天靜默隊列後首筆進單，即知即修完成閉環。

### Issue #1252：〈張寶成延伸閱讀〉— 驗證後發現姓名不符，改問清楚不硬做

讀者 javaing 想幫忙加國藝會文集連結，但 fetch 兩個 archive.ncafroc.org.tw URL 後標題作者都是「張又升」，不是 issue 標題寫的「張寶成」，站上目前也沒有任何文章提過這兩個名字。REFLEXES #16 適用：peer/reader 提供的名字是線索不是事實，逐一 fetch source 驗證後發現名字對不上，沒有硬套進任何文章，改留言問清楚是筆誤還是要連去哪篇文章，標籤加 `question`。

### Issue #1264：article-health seo-meta 只跑 zh-TW — 驗證屬實，但不倉促訂門檻

複驗讀者的技術分析：`seo-meta` 確實只對 zh-TW 註冊，非中文版本 `hard=0 warn=0` 是「沒檢查」不是「過關」，跟已合併的 #1263（英文 title 130 字元／description 670 字元）互相印證。這牽涉重新校準一個橫跨全站上萬篇譯文的 quality gate 門檻（且每個語言的 SEO 慣例長度可能都不同），屬於 BECOME §High-stake 強制升 Full 的「threshold / quality gate 數值調整」類別，不適合在日常巡邏裡倉促決定數字。留言承認問題屬實 + 說明為何不現場修 + `spawn_task` 記一個獨立 follow-up session（task_750dfe3d）。

### Issue #1184 / #615：SKIP（Step 2.4 重複回應檢查）

#1184 最新留言已是哲宇本人（等待他去 justfont 後台確認網域白名單，AI 端無法動）；#615 是長期 umbrella tracking issue，本 cycle 無新留言，不重複回應。

## Stage 4 WRAP — Quality gate

| Gate                                   | 結果                                                                                             |
| -------------------------------------- | ------------------------------------------------------------------------------------------------ |
| open issues 都有 status label/assignee | ✅（#1264 bug／#1252 question+content+from-feedback／#1184 bug+from-feedback／#615 enhancement） |
| open PRs ≤5d age 都有 review comment   | ✅（0 open PR，#1268 已 merge + heal + 感謝留言）                                                |
| broken-link ratio < 7%                 | ✅ 0.31%                                                                                         |
| build green                            | ✅（pre-push mirror 全綠；deploy workflow 因連續 commit 持續重跑屬正常節奏）                     |
| BECOME ACK 一行記憶體頂                | ✅                                                                                               |
| 連續空場 ≥ 3 cycle 有 LESSONS entry    | N/A（本 cycle 非空場，真實 backlog：1 PR + 4 issue 都動了）                                      |

## Handoff 三態

- [x] PR #1268 merge + heal（21 腳註格式 + subcategory + terminology false positive）+ 感謝留言 — retired
- [x] Issue #1272 Fact Check 修復 + close — retired
- [ ] pending（非本 routine）— Issue #1252 等 javaing 回覆姓名是否筆誤／目標文章；Issue #1264 seo-meta 多語言門檻設計已 spawn task_750dfe3d 待啟動；免疫 60 chronic owner=self-evolve-weekly（僅留一次 pointer，避免 cross-routine SPOF 信號通膨）

## Beat 5 — 反芻

同一個 fetch-verify 動作今天在兩個方向給出相反的結果：#1268 的「陳水扁親自回覆」claim 一驗就對得上（讀者自己做了功課），#1252 的「張寶成」一驗就發現名字根本不是文集作者。兩次都靠同一個習慣——不信任 issue 標題或 PR 敘述裡的人名，實際 fetch 原始來源逐字核對——才沒有把驗證通過的內容誤判成有問題，也沒有把驗證不通過的內容誤判成沒問題。REFLEXES #16「peer/probe 是線索不是 source」今天在兩個相反方向各驗證一次。

merge-first + heal 模式（idlccp-clownfish-instrument 教訓）今天在同一位貢獻者 idlccp1984 身上第三次驗證：前兩天分別在動保.md、本次在校園順口溜.md 都是「內容本身已經達標，格式債是唯一阻塞」，先合併保留 GitHub Merged 狀態與貢獻者社會契約，再回頭補格式，比 close 等對方重開 PR 更省來回成本。

🧬

---

_v1.0 | 2026-07-29 09:40 +0800_
_session twmd-maintainer-daily — 1 PR merge-first + heal / 1 issue fact-check 即修即 close / 1 issue 驗證後發現姓名不符改問清楚 / 1 issue 驗證屬實但 spawn 獨立 follow-up / 2 issue SKIP_
_誕生原因：cron routine 每日 08:30 fire_
_核心洞察：同一個 fetch-verify 習慣在兩個方向各驗證一次——救回一個讀者真的做過功課的 claim，也擋下一個讀者記錯人名的請求；merge-first + heal 模式連續第三天在同一貢獻者身上驗證，是可重複操作_
