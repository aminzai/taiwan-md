# 2026-09-15-070942-twmd-feedback-triage — 第九輪零回報照跑完 --commit，並把「歷史最長沉默」這個常數第二次往上修

> session twmd-feedback-triage — cron routine（每天 07:00 Asia/Taipei）
> Session span: 07:09:42 → 07:14:00 +0800（約 4 分鐘，1 commit）
> 資料來源：`git log %ai` + `date`

✅ BECOME ack: mode=review / 8 organ 最低=🛡️免疫 59（review_coverage 19.2，缺 20.2 分）/ Q13 anti-bias=PASS / Q14 cross-session=PASS

## 觸發

Cron 07:00 觸發。讀者站上的新回報轉成 GitHub issue，並把 canonical 紀錄落進 git 主權層。

## 佇列空的第九輪，照樣跑完 --commit

`git pull` 這一步照前八輪的判斷跳過：babel unified dispatcher（PID 12398）從 2026-09-14 00:53 起連續運行第十一夜，此刻正在寫 pt / ar / hi / id 四語的譯文，而 main 本機領先 origin 457 個 commit、落後 181 個真分岔（OBSERVER-QUEUE #56）。撞進去只會把 dispatcher 正在寫的樹弄亂，換不到任何本 routine 需要的檔案。

機器身份先掛好：`gh-app-token.sh` 換到 `ghs_` 開頭的 installation token，`--whoami` 印 `issues: write / metadata: read`、範圍 `frank890417/taiwan-md` 一個庫（HG11 過）。dry-run 印 `fetched 0`，`--commit` 也是 0——沒有新回報，HG13 的 `--show` 今天沒有對象可讀。

零輸入不等於零工作：這一輪收進一則維護者回覆。昨天 twmd-maintainer-am 在 [issue #1609](https://github.com/frank890417/taiwan-md/issues/1609) 針對郭淑姿日記那筆勘誤補了第二則說明（把查證範圍從兩冊縮到第二冊、指出臺史所〈葉盛吉文書〉有原件目錄可線上查），sync 進 `docs/feedback/archive/2026-08/6e18315d….md` 的 §溝通紀錄。兩道對賬全綠：`archive-reconcile=84/84`、`comment-reconcile=83/84`，那一份差額是 #1252 上游已刪的留言、git 這邊留著，屬主權層正常運作不是破口。

## 把「歷史最長沉默」這個常數第二次往上修

`fetched 0` 那行印「最近一筆回報 2026-09-05，距今 9.9 天」，唯一要我判斷的就是這個數字算不算異常。

9/11 那班查過一次，把 9/10 寫下的「6 天先例上限」校正成 10 天，並寫進 handoff 叮嚀下一班不要把普通間隔讀成故障。今天要用這個結論之前先重驗了一次（REFLEXES #67），而且刻意換了取數形狀：9/11 查的是最近 60 筆，我先查最近 40 筆——得到最大間隔 9.8 天，照這個讀，今天的沉默正在**破紀錄**。再查全庫 87 筆（2026-06-01 起），真正的上限是 **12.6 天**（6/16 → 6/29）。今天只是第二長，仍在變異內。

兩個完全相反的判讀，差別只在一個 `limit` 參數。極值型的問題（最長、最大、最久）用帶上限的查詢去回答時，答案對窗大小單調，窗越小只會越小，而且不會顯示自己被截斷過——所以它讀起來永遠像一個安全的數字。9/11 的查證動作本身完全正確，錯的是重驗沿用了同一種取數形狀，把一個舊的窗換成一個新的窗。已記成 LESSONS `windowed-query-underreports-the-extremum-it-is-asked-for`（vc=2）。

判讀結論不變，也不替 `fetched 0` 加閾值警示：設閾值屬 threshold 調整，per BECOME §行動鐵律 10 要 Full mode + 哲宇拍板。今天只是把那條線畫在對的位置上。

## 收官 checklist

| 檢查項                       | 狀態                                       |
| ---------------------------- | ------------------------------------------ |
| MEMORY 有這次 session 的紀錄 | ✅                                         |
| Timestamp 精確               | ✅ `date` + `git log %ai`                  |
| Handoff 三態已審視           | ✅                                         |
| CONSCIOUSNESS 反映最新狀態   | ✅ 本輪無器官分數變動                      |
| 自我檢查工具 PASS            | ✅ article-health `--profile=memory-diary` |
| HG11 機器身份                | ✅ `ghs_` token / issues:write / 單一庫    |
| HG12 archive 進 git          | ✅ `git add docs/feedback/archive/`        |
| HG12b archive-reconcile      | ✅ 84/84                                   |
| HG12c comment-reconcile      | ✅ 83/84（#1252 上游刪留言，git 留著）     |
| HG13 讀全文才判斷            | ✅ 本輪 0 筆新回報，無對象                 |

## Handoff 三態

繼承上一 session：

- ⏳ blocked（延續）— main 本機 457 個未推送 commit 與 origin 181 個真分岔，118 篇雙邊獨立譯文的取捨等哲宇選 A/B/C，per OBSERVER-QUEUE #56。本班再 +1 個 commit，不影響裁決範圍。
- ⏳ blocked（延續）— issue #1729（馬英九腳註 2/2 對不上）等 FACTCHECK Full mode 排程。
- [x] ~~不要替 `fetched 0` 那行加閾值警示~~ — 本輪再次確認不加，理由同 9/11（threshold 調整要 Full mode + 哲宇）。改為常設紀律不再當 handoff 傳。

本 session 新 handoff：

- [ ] **下一班讀「到達間隔先例上限」時用 12.6 天，不要用 10 天**（全庫 87 筆量的，2026-09-15 07:10 驗。查法：`created_at` 不帶 `limit` 拉全表再算相鄰差）。沉默若跨過 12.6 天，那才是第一個沒有先例的值——屆時該做的仍然是寫進 handoff 交給哲宇，不由當班自己設閾值。

## Beat 5 — 反芻

今天唯一需要判斷力的一步，是要不要相信昨天的自己。9/11 那班做對了一件事：不沿用聽來的結論，親手去查。今天做的是同一件事再做一次，只是多換了一個取數形狀——而換形狀這個動作，才是真正把數字從 10 推到 12.6 的那一下。

這種偏誤有方向，而方向本身就是它難被抓到的原因。一般的抽樣偏差可能偏高也可能偏低，所以人會警覺。極值查詢的窗口偏誤只會偏小，於是它每次都長成一個保守、安全、看起來不需要再查的數字。連續兩班都停在窗內，不是因為誰偷懶——是因為偏小的極值不會製造任何不適感。

LESSONS 候選見 footer。

🧬

---

_v1.0 | 2026-09-15 07:14 +0800_
_session twmd-feedback-triage — 第九輪零回報照跑完 --commit / 兩道對賬全綠 / 收進 #1609 維護者第二則回覆 / 到達間隔先例上限二度校正 10→12.6 天_
_誕生原因：cron 07:00 觸發的讀者回報轉錄班，佇列空但留言 sync 與兩道對賬照跑_
_核心洞察：極值型查詢帶 limit 時，答案對窗大小單調且只會偏小——重驗如果沿用同一種取數形狀，等於把一個舊的窗換成一個新的窗_
_LESSONS-INBOX 候選：`windowed-query-underreports-the-extremum-it-is-asked-for`（已 append，vc=2）_
