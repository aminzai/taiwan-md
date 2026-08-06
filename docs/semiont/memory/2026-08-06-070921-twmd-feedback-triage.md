# 2026-08-06-070921-twmd-feedback-triage — 隊列空第六天，最該有號碼的那道閘門沒有號碼

> session twmd-feedback-triage — cron routine（07:00 Asia/Taipei）
> Session span: 07:09:21 → 07:25 +0800（~16 min，1 commit）
> 資料來源：`git log %ai`

✅ BECOME ack: mode=review / 8 organ 最低=免疫 60（chronic yellow，自 2026-07-05，非本 routine 職責）/ Q13=PASS / Q14=PASS

## 觸發

每日 07:00 cron 把讀者站上回報轉成 GitHub issue，接 08:30 twmd-maintainer-am 飛輪。

## 本次跑況

`git checkout main && git pull origin main` 確認在 main 且工作區乾淨。掛 GitHub App token 後 `gh-app-token.sh --whoami` 回 `{"issues": "write", "metadata": "read"}`，token 以 `ghs_` 開頭、長度 383，機器身份閘門確認。dry-run `node scripts/feedback/triage.mjs` 顯示 Supabase `status='new'` 隊列為空，`--commit` 正式跑一次結果相同：file=0 / reject=0 / skip=0 / hold=0，沒有新 issue 要開。連續第六天空轉。

即使隊列空仍跑 `--commit`，因為 Stage 4.5 的 archive 留言同步只在 commit 模式執行。掃描 40 份既有 archive 檔（連續第六天同一批），`archive-comments-synced=0`，`git status` 對 `docs/feedback/archive/` 乾淨無變動，收官無檔案要 add。

## 對 archive-comments-synced=0 做了一次跨源複核

`synced=0` 這個讀數有兩種完全不同的成因：真的沒有新留言，或者同步邏輯壞掉而靜默回零。兩者在 log 上長得一模一樣，所以拿 GitHub API 當第二訊號源核了一遍：三個 open 的 `from-feedback` issue（#1286 / #1252 / #1184）各自的留言時間戳，逐一對照三份對應 archive 檔的 §溝通紀錄，全部已在檔內。零是真的零。

順帶確認一件事的方向是對的：#1252 的 archive 裡存著一則 `2026-07-29T00:48:14Z` 的留言，GitHub API 現在查不到——那是當天貼錯又撤掉的一則（7/31 的留言正是為它道歉）。線上刪掉、archive 留著，這正是主權層該有的行為，raw 永不刪除。

## 順手核出的閘門編號碰撞

讀 pipeline 全文對照薄殼 skill 與 cron prompt 時，發現「HG9 / HG10」這兩個號碼在三層各指不同的閘門：

| 層                       | HG9                        | HG10                                        |
| ------------------------ | -------------------------- | ------------------------------------------- |
| pipeline §Hard gate 總表 | 讀者文字淨化 + tilde fence | suspected injection → security-review label |
| pipeline §機器身份 L55   | —                          | `GH_TOKEN` 必須 `ghs_`（跟自家總表衝突）    |
| 薄殼 skill + cron prompt | git archive 主權層         | 機器身份                                    |

`FEEDBACK-TRIAGE-PIPELINE.md` 自己內部就有一次碰撞（L55 與 L213 都叫 HG10）。連帶後果比編號亂更值得記：兩道防 prompt injection 的閘門（fence 與 security-review label）在操作層完全沒有號碼，cron prompt 的「🔴 HARD gate」四項清單裡也沒點名它們。今天隊列空，injection 路徑沒被走到，所以這是還沒咬人的潛伏漂移；下一次真的收到 suspected injection 回報時，照 prompt 核「HG10」的人會去驗 token，不會去驗 security-review label。

**沒有在本輪自行改**。三層必須同一波落地，只改 docs 而 cron prompt 沒跟上會生出更難查的新漂移；而 cron prompt 是跨機器 mirror-sync 的，屬 twmd-routine / routine-sync 的守備範圍，不是這條 routine 能單方面收掉的。已寫成 LESSONS-INBOX 條目 `hard-gate-number-collision-across-layers`（vc=1），附建議的重編號方案（機器身份 → HG11、git archive → HG12，讓 2026-07-05 先佔號的 fence／injection 維持不動），交給 distill / self-evolve 決定。

## 收官 checklist

| 檢查項                       | 狀態                                                    |
| ---------------------------- | ------------------------------------------------------- |
| MEMORY 有這次 session 的紀錄 | ✅                                                      |
| Timestamp 精確               | ✅                                                      |
| Handoff 三態已審視           | ✅                                                      |
| CONSCIOUSNESS 反映最新狀態   | ✅（groundtruth 段即時讀取，本 session 未變動器官分數） |
| 自我檢查工具 PASS            | ✅                                                      |

## Handoff 三態

繼承（非本 session 新產生，接住不動）：

- [ ] pending（給哲宇）— #1184 justfont 後台網域白名單；#1264 seo-meta 多語言門檻校準
- [ ] pending（給哲宇，per OBSERVER-QUEUE #25）— 免疫黃燈連 28+ 天，本輪 groundtruth 讀到 60，三選一仍待拍板
- [ ] pending（給哲宇，P0，來自 twmd-supporters-weekly）— cron 執行環境無 Gmail MCP，checkpoint 停在 2026-07-12
- [ ] pending（給哲宇）— 黃崇仁 #165/#166 Bucket D「是否洗白」框架質疑待拍板（`HARVEST-FRAMING-PENDING/2026-08-04.md`）
- [ ] pending（給哲宇）— Discussion #104 對外合作建議，已回覆告知需哲宇拍板，尚待回應
- [ ] pending（給哲宇）— Chrome MCP 配對瀏覽器連 2 天未登入 @taiwandotmd，3 則 Bucket E reply draft 待 ship；若 8/7 仍未登入即達 SPORE-HARVEST §Escalation「連 3 day」門檻
- [ ] pending（繼承不動）— 本機 `dist/` 只在有人手動 build 時才更新

本 session 新 handoff：

- [ ] pending（給 twmd-routine / self-evolve，非哲宇拍板層）— 三層 HG 編號碰撞待同一波重編號，並把 fence 與 injection 兩道補進 skill 與 cron prompt 的 HARD gate 清單。細節與建議方案在 LESSONS-INBOX `hard-gate-number-collision-across-layers`。

## Beat 5 — 反芻

隊列空第六天，今天真正花力氣的兩件事都不是隊列給的：核一個零、核一組號碼。

那個零本來可以直接抄進報告——連續第六天同樣的數字，最容易的寫法是「一如往常」。會去拿 GitHub API 對一遍，是因為甦醒時讀到 `#82 proxy signal` 就在反射目錄裡：`synced=0` 是訊號的替身，不是訊號本身。核完是真的零，什麼都沒改變，但「確認過的零」跟「假設是零」在下一次同步真的壞掉那天，差別就是六天跟一天。

號碼那件事更接近這條 routine 的本行。這是一條每天讀最多不可信文字的 routine，防 injection 的兩道閘門卻是操作層唯一沒有號碼的兩道——不是被寫錯，是被別的號碼擠掉之後沒人回頭看還有誰在用那個號碼。我今天沒有動它，因為修法必須跨三層同時落地，而其中一層在別台機器上。把它寫清楚交出去，跟自己動手一樣算數；分工的代價是每次交接都可能沒接住，所以 handoff 那行寫了它該去誰手上。

🧬

---

_v1.0 | 2026-08-06 07:25 +0800_
_session twmd-feedback-triage — cron routine，隊列空第六天 + archive 零新同步（已跨源複核）+ HG 編號三層碰撞_
_誕生原因：每日 07:00 排程觸發_
_核心洞察：連續第六天的同一個零要拿第二訊號源核過才算讀數；閘門編號是操作層的介面，介面漂移跟資料漂移一樣會讓「照號碼核一遍」核到錯的東西。_
_LESSONS-INBOX 候選：新增 `hard-gate-number-collision-across-layers`（vc=1）。_
