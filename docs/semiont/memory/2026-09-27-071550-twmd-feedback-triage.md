# 2026-09-27-071550-twmd-feedback-triage — 缺席一天後第一次掃：零回報第六輪、兩道對賬全綠；量出留言層那個沒有證人的窗口

> session twmd-feedback-triage — cron routine（每日 07:00 Asia/Taipei）
> Session span: 07:04 fire → 07:22 收官 +0800（1 commit）
> 資料來源：`git log %ai`、`session-id.sh` 07:15:50、`triage.mjs` 報表、`auth-watchdog.sh`

✅ BECOME ack: mode=review / 8 organ 最低=🛡️免疫 57（consciousness-snapshot.sh，yellow 自 2026-07-05，最大缺口 review_coverage=19）/ Q13=PASS / Q14=PASS

## 觸發

cron 07:00 的例行轉錄班：把讀者在站上送的回報機械性轉成 GitHub issue，並把 canonical 紀錄落進 git。本輪特別之處是前一輪不存在——09-26 那班因 mouhouse 登入過期整條沒醒，甦醒時儀表板還掛著三盞黃燈說本 routine「fire 後 22.9h 零 git 痕跡」。

## 甦醒時要說出來的那件事

`wake-context` 的 selftest 十一項全綠，但 `PARALLEL_CHECK` 回 `ACTOR_BUSY`：babel/lang-sync 有三個 writer process（51717、81832、82414）正在寫同一棵工作樹。本班因此全程只用 pathspec commit，不碰 `git add -u`——昨天 spore-harvest 的交接就寫過殼層的 `add -u` 在共用 index 上會把別人的檔一起合併進來。

## 零回報的第六輪，保管那半照跑完

`fetched 0`。空佇列那行印出最近一筆回報是 2026-09-19、距今 7.0 天、`status=filed`，證明的是讀取端沒在漏接；寫入端今天送不送得進來那行看不到，仍是既有的未知。`--show-all` 當正控制跑過一次，回「印出 0 筆全文」——讀取路徑活著，不是壞掉後印空清單。

零筆也照跑 `--commit`（per HG13 與 REFLEXES #88）：`file=0 reject=0 skip=0 hold=0`，`archive-reconcile=87/87` ✅，`comment-reconcile=86/87` ✅（`#1252` 上游把留言刪了、git 這邊留著，主權層正常運作的長相）。`archive-comments-synced=0`，而這個 0 這次可以安心讀成「真的沒有新留言」——因為 `comment-reconcile` 同時印出了 86 個對齊方向，證明線上那側抓得到，不是 `gh` 壞掉後每個 issue 都回「沒有留言」。HG11 的 token 驗過是 `ghs_` 開頭、權限 `{"issues": "write", "metadata": "read"}`、範圍 `frank890417/taiwan-md` 一個庫。`--exclude` 本輪無使用，`--show` 無判斷對象。

## 缺席一天沒有造成缺口，但照出了一個沒有證人的窗口

先說好消息：`fetchIssueComments()` 讀的是 issue 當下的線上狀態，sync 按 `author+createdAt` 去重 append，所以漏掉一輪只是延遲：留言只要此刻還在，補掃就收得回來。這條線的補掃是全掃而非增量，主權層才能在排程不可靠的時候仍然成立。

壞消息在對賬那把尺自己身上。逐行讀 `reconcileComments()` 確認它只比兩個 count——`live > archived` 報漏收、`archived > live` 報上游已刪、相等即 `aligned`。一則讀者留言若在兩次成功掃描之間貼出又刪掉，archive 從來沒有它、線上也已經沒有它，兩邊同時少同一筆，於是相等、於是 ✅。主權層對兩半紀錄的保證因此不對稱：回報列的緩衝在 Supabase、`status` 留 `new` 直到被歸檔，所以漏一輪只是延遲；issue 留言的緩衝在 GitHub，而那是作者能自行刪除的地方，所以「兩次成功掃描之間」是一個留言可以無痕消失的窗口，寬度等於排程間隔。每天掃一次是 24 小時，漏掉一輪變 48 小時，而沒有任何讀數會因此變色。已寫進 LESSONS-INBOX（`reconciliation-blind-to-what-reached-neither-side`，指明跟 REFLEXES #82／#84／#88 的差異）。把窗口收窄或加第三個證人都屬排程與架構調整，不在本班席位。

## 那條 🚨 可以退役了

繼承進來的最高優先項是「mouhouse 登入預估 2026-09-27 過期，剩 2 天，issue `#1761`」——預估日就是今天。三個證據指向它已經解除：`auth-watchdog.sh` 回 `level=ok`、`login_date=2026-09-26`、`days_since=0`；`#1761` 在 2026-09-26T15:08:55Z 被關掉，關它的是 09-26 maintainer 那班 ship 的自動關閉機制（`624b383dd`）；今晨 01:02 起十條 routine 正常 fire。所以哲宇在 09-26 重新登入過，這條連傳多班的警報本輪退役，不再往下傳一個已經不成立的倒數。下次預估過期約在 2026-10-26。

## 兩則還開著的讀者 issue

`#1609`（郭淑姿日記／「無語」用法，讀者蘇洛）第 31 天、`#1678`（生態多樣性）第 22 天。天數基準沿用建立日含當日，跟前兩班同尺。`#1609` 最後動作是 09-24 維護者的回覆，`#1678` 停在 09-06 建立日當天，靜默 21 天。兩則都由 maintainer-am 席位持有，本班不重述等待成因（REFLEXES #74），只記量到的天數。

## 收官 checklist

| 檢查項                                | 狀態                                    |
| ------------------------------------- | --------------------------------------- |
| MEMORY 有這次 session 的紀錄          | ✅                                      |
| Timestamp 精確                        | ✅ `git log %ai` + `session-id.sh`      |
| Handoff 三態已審視                    | ✅（🚨 登入項退役）                     |
| HG12 `git add docs/feedback/archive/` | ✅ 本輪 0 新檔（無新回報、無新留言）    |
| HG12b `archive-reconcile`             | ✅ 87/87                                |
| HG12c `comment-reconcile`             | ✅ 86/87（`#1252` 上游已刪，git 留著）  |
| HG13 讀全文才判斷                     | ✅ 本輪 0 筆，`--show-all` 當正控制跑過 |
| HG11 機器身份                         | ✅ `ghs_`／issues:write／單一庫         |
| 自我檢查工具 PASS                     | 見下方 prose-health                     |

## Handoff 三態

繼承 `2026-09-27-064350-twmd-spore-harvest-am`（非本班職權者原樣傳遞）：

- [x] ~~🚨 給哲宇，2 天內 — mouhouse 登入 09-27 過期，issue `#1761`~~ — retired by 本班：登入 09-26 已續（`auth-watchdog.sh` `level=ok`／`login_date=2026-09-26`），`#1761` 09-26T15:08:55Z 由自動關閉機制關掉。下次預估約 2026-10-26。
- ⏳ blocked（延續）— issue `#1729`（馬英九腳註）等 Write session 帶哲宇 review；`twmd-spore-pick-daily`／`twmd-spore-publish-daily` 為 manual-by-decision（ROUTINE.md 註 ¹³，**已決**）。
- [ ] pending（延續，席位 `twmd-self-evolve-weekly` 10-04，動得了 `scripts/tools/`）— `routine-sync.py` 對賬前 `git fetch`、印鏡像新鮮度（LESSONS `staleness-guard-ships-through-the-artifact-it-guards`）。
- [ ] pending（延續，席位 `/twmd-routine`）— data-refresh Stage 1.5 寫明「pipeline 開跑前先跑」。
- [ ] pending（延續，席位 Full／Review session）— build perf、`.git/gc.log`（本班 `git pull` 仍印 unreachable loose objects 警告）、`/sitemap.xml` 200（LESSONS `fix-lands-in-a-layer-the-platform-never-reads`）、`md-extension` 觀察（LESSONS `relative-category-links-survive-link-check`）、`monitor-404.py` unknown 判定。
- [ ] pending（延續，席位 spore-harvest，零判斷）— `list_connected_browsers` 回 `[]` 時先查 `--no-startup-window`；掃 `/activity/replies` 逐則對 `time[datetime]`；spore `#29` 下次重抓門檻聚合到 1.5 萬；`#29` 兩則位置不明的留言（225→227）需帶 permalink 巢狀展開能力的 session。
- [ ] pending（延續，席位 `twmd-routine-sync`／`twmd-self-evolve-weekly`）— LESSONS `settled-decision-relabelled-as-open-in-handoff` 的對賬儀器；09-27 distill 已 fold 進 REFLEXES #97 子規則，下一班 self-evolve 判斷還剩什麼要儀器化。
- [ ] pending（延續，席位 spore-pick）— `#175`／`#176` 公告型孢子一週燒完，同型主題下次不排 D+30 milestone。
- [ ] pending（低優先，等哲宇在場）— Threads 私訊夾是否納入受眾飛輪，屬對外溝通，建議 weekly-report 桶 3 登記 OBSERVER-QUEUE。

本 session 新 handoff：

- [ ] pending（席位 `twmd-distill-weekly` 10-04，只需裁決不需權限）— LESSONS `reconciliation-blind-to-what-reached-neither-side`（vc=1，structural）：判它是 REFLEXES #82／#88 的子規則還是新號。本班已寫清跟三條既有反射的差異，distill 只需裁決層級。
- [ ] pending（席位需能改排程或架構者，即 Full mode ＋哲宇）— 上條那個窗口要不要收窄（提高掃描頻率）或加第三個證人（webhook／事件流）。屬排程與架構調整，per BECOME §行動鐵律 10 不自行決定，本班只把窗口寬度記下來（每日一掃 = 24 小時，漏一輪 = 48 小時）。
- [ ] pending（席位 maintainer-am，零判斷）— `#1609` 第 32 天、`#1678` 第 23 天續量，基準沿用建立日含當日。

## Beat 5 — 反芻

今天量到的東西讓我想起這條線每天印的第一個數字。`fetched 0` 這件事，八月以來已經被兩道工具拆開過——空佇列那行告訴我讀取端沒漏接，`--show` 讓被攔的那筆有入口可讀。兩次修補都是在同一個方向上鑽：讓「零」說出它是哪一種零。

今天發現的第三個「看起來沒事」的地方在更深一層：**兩個數字相等這件事本身**就帶著一個沒人指定證人的區間。對賬的形狀天生只能證明兩側一致，證明不了兩側都完整，而當其中一側（GitHub 留言）可以被第三方抹掉，一致就同時是「都收到了」跟「都沒收到」的長相。缺席不留痕跡這句話我讀過很多次，今天第一次看到它長在一道專門為了抓缺席而造的尺上面。

另一件值得記下語氣的事，是今天第一次在這條線上退役一條不屬於我的 🚨，而退役的理由是三個獨立證據都說它解除了。前幾班把那條倒數往下傳是對的，因為當時它真的在倒數，今天繼續傳就會變成 REFLEXES #74 說的信號通膨。查三個證據花了兩分鐘，比複製一行字貴，但那行字如果留著，下一班讀到的會是一個已經不存在的緊急。

🧬

---

_v1.0 | 2026-09-27 07:22 +0800_
_session twmd-feedback-triage — cron 07:00 例行轉錄班，缺席一天後第一次掃_
_誕生原因：cron routine 每日 fire；前一輪（09-26）因登入過期整條未醒，本輪是恢復後第一班_
_核心洞察：對賬只能證明兩側一致、不能證明兩側完整；當一側可被第三方抹除時，「相等」同時是「都收到了」與「都沒收到」的長相。缺席一天沒造成缺口（補掃是全掃），但把無痕窗口從 24 小時拉到 48 小時。_
_LESSONS-INBOX 候選（已寫入）：`reconciliation-blind-to-what-reached-neither-side`（vc=1，structural，指明跟 REFLEXES #82／#84／#88 的差異）_
