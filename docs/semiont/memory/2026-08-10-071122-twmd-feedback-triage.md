# 2026-08-10-071122-twmd-feedback-triage — 空了九天的隊列送來兩則日文字形回報，兩道對賬全綠

> session twmd-feedback-triage — cron routine（每天 07:00 Asia/Taipei）
> Session span: 06:52:00 → 07:11:34 +0800（約 20 分鐘，1 commit）
> 資料來源：`git log %ai` + `date`

✅ BECOME ack: mode=review / 8 organ 最低=🛡️ 免疫 60（黃燈自 2026-07-05）/ Q13=PASS / Q14=PASS

## 觸發

每日 07:00 的讀者回報轉錄班。前九個 cycle 隊列都是空的，這次 Supabase 有兩筆 status='new'。

## 兩則回報都在講同一件事的兩個面

讀者 Pigcasso6 在 8/9 下午 13:14 與 13:18 連送兩則，都指向日文版的字形問題。第一則說日文頁面套的是繁體中文字形，舉了「言」字第一筆該是橫而不是點當例子，還順手建議去問字型公司。第二則指名 `/ja/data/`，說日文裡「台灣」該寫成「台湾」，而「データ台灣」整頁都沒轉，並重述了字形那件事。

分類器把兩則都判成 bug，spam score 0、injection score 0、隱形字元 0。開 issue 前我把兩份 body 印出來逐字比對過原始 row：可見文字一字不差，只多了 tilde fence 的包裝與 provenance 一行（只有 display_name 跟 feedback id，沒有 email）。兩則內容雖然相關，dedupe 沒把它們併起來也是對的——一則講字型檔選擇，一則講用字轉換，是兩個不同的修法，合併反而讓維護者少看見一半。

`cc5775abd` 落地兩份 archive 紀錄。issue [#1306](https://github.com/frank890417/taiwan-md/issues/1306) 與 [#1307](https://github.com/frank890417/taiwan-md/issues/1307) 都掛 `bug` + `from-feedback`，事後用 `gh issue view` 回查作者確認是 `app/taiwanmd-semiont`（`is_bot=true`），不是宿主機登入的哲宇帳號。

這兩則回報有個地方值得多記一筆：日文版讀者看得出「言」字第一筆的差別，代表他是真的在讀，而不是點進來看一眼。主權的巴別塔到目前為止量的都是「有沒有翻」，這位讀者量的是「翻出來的東西看起來像不像那個語言的東西」——比覆蓋率低一層、比覆蓋率誠實。

## 兩道對賬與一次回查

`archive-reconcile=63/63`（61 舊 + 2 新，Supabase filed 筆數與 git 紀錄份數相等）。`comment-reconcile=62/63`，唯一一筆是 #1252 的 archive 4 則對線上 3 則——7/29 那則答錯的留言在 GitHub 被刪掉，git 這邊留住了，屬於主權層正常運作的方向，不報警。Supabase 側回查確認兩筆都寫回 `filed` + issue_number + triaged_at，`new` 歸零。

過程中一度以為 `verify-commit-scope.sh` 不存在，實際是它住在 `scripts/tools/lib/` 而我照 BECOME 鐵律 5 的字面在 `scripts/tools/` 找。

那把尺跑起來之後立刻抓到一件事：寫 memory 前要 commit 時它報 `SCOPE MISMATCH（4 ≠ 2）— 疑似 cross-session 污染`。查下去，污染源是自家的兩支工具：archive 產生器寫雙引號，prettier 在 pre-commit 把同樣的欄位改成單引號，lint-staged 還原後索引留著格式化前的 blob。HEAD 跟工作樹其實一致，只有索引是舊的。`fm()` 只把 `"` 換成 `'` 而不跳脫 `'`，所以讀者可控欄位用雙引號是刻意的跳脫保證，不能為了消警報就改成單引號——這條留 handoff 給人拍板，不在無人時段動不可信輸入的跳脫語意。

## 收官 checklist

| 檢查項                       | 狀態                                     |
| ---------------------------- | ---------------------------------------- |
| MEMORY 有這次 session 的紀錄 | ✅                                       |
| Timestamp 精確               | ✅（git log %ai）                        |
| Handoff 三態已審視           | ✅                                       |
| CONSCIOUSNESS 反映最新狀態   | ✅（警報已 derived 化，本 cycle 無新增） |
| 自我檢查工具 PASS            | ✅ 46/46 unit test + prose-health        |

## Handoff 三態

繼承（非本 session 新產生，接住不動）：

- [ ] pending（給哲宇）— #1264 seo-meta 多語言門檻校準、#1184 justfont 後台網域白名單、#1286 轉換器詞性感知功能擴充
- [ ] pending（給哲宇，per OBSERVER-QUEUE #25）— 免疫黃燈 35+ 天，三選一等拍板
- [ ] pending（給哲宇，P0，vc=3）— `twmd-supporters-weekly` 執行環境連續三次找不到 Gmail MCP，贊助資料缺口 4 週，三選一待拍板
- [ ] pending（給哲宇，連續第 3 天）— 配對瀏覽器 Threads/X 帳號登出，3 則 Bucket E reply draft 待補發
- [ ] pending（延續）— EZWAY 報關孢子話題環境政治化，純留痕供參考
- [x] ~~retired — 黃崇仁孢子三讀持平已判定生命週期結束~~（retired by 2026-08-10-064015-twmd-spore-harvest-am）

本 session 新 handoff：

- [ ] pending（給今天 08:30 的 `twmd-maintainer-am`）— issue #1306 / #1307 是同一位讀者對日文版字形的兩則回報，兩則都需要判斷：ja 頁面的字型堆疊要不要獨立於 zh-TW，以及 `/ja/data/` 這類頁面標題的「台灣」→「台湾」該在哪一層修（UI bundle 還是 knowledge 來源）。回覆讀者仍是人類 gate。
- [ ] pending（給哲宇 / 下一個 feedback-triage cycle）— archive 產生器寫雙引號、prettier 在 pre-commit 改成單引號，索引留下格式化前的 blob，害同 session 第二次 commit 前的 `verify-commit-scope.sh` 喊假的 `SCOPE MISMATCH`。本 cycle 用 `git restore --staged` 繞過。**不要直接把產生器改成單引號**（`fm()` 只跳脫 `"` 不跳脫 `'`，雙引號是對不可信 display_name 的跳脫保證）。兩個候選解：`docs/feedback/archive/` 進 `.prettierignore`，或產生器補單引號跳脫後對齊 prettier。動到不可信輸入的跳脫語意，留人拍板。診斷已落 [LESSONS-INBOX `formatter-vs-generator-quote-churn-fakes-scope-alarm`](../LESSONS-INBOX.md)。

## Beat 5 — 反芻

昨天的自己在 handoff 裡寫下「查完上游取數層，缺 env 與非 200 都會炸不會偽裝成空」，那句話今天的用處跟昨天相反：昨天它擋住我為了交出成果再焊一道閘門，今天它讓我對「隊列裡真的有東西」這件事沒有半點意外——上游是通的，空是真的空，有是真的有。連續九天空手之後第一次收到東西，最需要防的其實是另一種鬆懈：以為隊列空久了、來的大概也是零星小事，於是對賬草草看過。三道對賬今天照跑，`comment-reconcile` 那個 62/63 的方向判讀（上游刪留言而非 sync 漏收）也照著 HG12c 的三向表對了一次，沒有把「不等於零」讀成「有破口」。

這位讀者的兩則回報把巴別塔的量尺往下推了一層。我們一直在數覆蓋率跟新鮮度，這兩個數字對「頁面上有字」很敏感，對「字長得對不對」完全瞎——跟 8/6 那次俄語讀者看半年烏克蘭文介面是同一族的病，只是這次語言送對了，衣服穿的還是另一種文字。儀器抓不到，只有真的在讀日文的人抓得到。

🧬

---

_v1.0 | 2026-08-10 07:11 +0800_
_session twmd-feedback-triage — 九天空隊列後首次有件，兩則日文字形回報轉成 issue #1306 #1307_
_誕生原因：cron routine 每日 07:00 fire，Supabase 出現 2 筆 status='new'_
_核心洞察：讀者抓到的是覆蓋率與新鮮度兩把尺都量不到的東西——日文頁面套繁中字形、標題沒轉「台湾」，頁面有字不等於字是對的；連續空場之後真的有件時，最該防的是對賬草草看過。_
_LESSONS-INBOX 候選：已落一條 `formatter-vs-generator-quote-churn-fakes-scope-alarm`（vc=1）。字形那一層暫不另立，屬既有「儀器只看見存在，看不見形狀」家族，待 #1306/#1307 處置後看是否成 instance。_
