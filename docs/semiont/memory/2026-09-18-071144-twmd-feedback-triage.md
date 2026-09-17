---
session: '2026-09-18-071144-twmd-feedback-triage'
date: 2026-09-18
routine: 'twmd-feedback-triage'
mode: 'review'
---

# twmd-feedback-triage @ 2026-09-18 07:11 — 周蕙勘誤開成 #1746，核對開完的 issue 時發現 `--show` 少印一欄，HG13 那次「讀完全文」其實只讀了一半

> session twmd-feedback-triage — cron 07:00 daily（maintainer-am 之前）
> Session span：07:11:44 → 07:2x +0800（0 個 knowledge 變更，1 個 issue，1 份 archive，1 個工具修補，本檔）
> 資料來源：`triage.mjs` 報表 / `gh issue view 1746` / `git diff main origin/main`

✅ BECOME ack: mode=review / 8 organ 最低=🫀 心臟 30（red，自 2026-09-15）/ Q13=PASS / Q14=PASS

## 觸發

07:00 例行。佇列有一筆新回報，是連續兩天零回報之後的第二筆真回報。

## 這輪做了什麼

`fetched 1`：讀者 Joanne Yap 昨天 04:34 對〈周蕙〉送的 `content` 勘誤，說 4/25 小巨蛋那段寫的「開票快速售罄、加開一場」與事實不符，只有一場、也沒有售罄。先 `--show` 讀全文，判斷是對公眾人物演唱會的事實勘誤，沒有具名私人、沒有跟監細節、沒有保密請求、沒有指令樣文字，可以公開。`--commit` 開成 [#1746](https://github.com/frank890417/taiwan-md/issues/1746)（`needs-verification` + `from-feedback`），作者 `app/taiwanmd-semiont`（is_bot），body 零 email、兩段讀者文字都在 tilde fence 裡、provenance 帶 feedback id。archive `docs/feedback/archive/2026-09/8bd8ca0d-….md` 落地。

兩道對賬：`archive-reconcile=86/86` ✅、`comment-reconcile=85/86`（上游已刪留言 1 份紀錄 git 留著：#1252，主權層正常）。`file=1 reject=0 skip=0 hold=0`。HG11：`ghs_` token、`{"issues": "write", "metadata": "read"}`、安裝範圍 `frank890417/taiwan-md` 一個庫。

## 核對 issue 時多出一段沒讀過的文字

開完 issue 逐條核 HG2/HG3/HG9 時，body 裡有兩個 fence：第一段是 `--show` 印過的回報全文，第二段「4/25小巨蛋的演唱会就只有一场，并没有加开⋯」我沒讀過。那是 Supabase 的 `correct_info` 欄（表單上的「正確資訊 + 來源」）。讀者自由文字有四個欄位（`source_url` / `body` / `quote` / `correct_info`），`detectInjection`、`scrubSecrets`、`buildArchiveRecord` 全掃四個，唯獨 8/31 為 HG13 造的 `formatForShow()` 只印 `body` 跟 `quote`。這一筆的第二段內容無害，但如果一封指控信把具名私人寫在「正確資訊」欄，這條 routine 的讀取閘門會讓它直接進公開 issue。

修法是純讀取面：`formatForShow()` 補印 `correct_info`（沒有就不印空段，「沒有」跟「空字串」不共用長相），+1 unit test，`node --test` 63/63 綠。`FEEDBACK-TRIAGE-PIPELINE.md` 升 v1.11 把「印四個欄位」寫進 §不能轉錄的那一筆。不碰判準、不碰 HG8。這是 LESSONS `held-fact-never-crosses-into-the-layer-that-acts-on-it` 的第五次，instance 補進原 entry（vc 4→5），沒開新 entry。

## Stage 0 的判斷：這輪一樣不 pull

`check-parallel-actor.sh` 報 ACTOR_BUSY（babel dispatcher 六個 writer 進程，昨夜 01:03 換過設定後的新一代）＋ origin 領先 548、本機領先 771。逐檔驗本 routine 的五個依賴：`archive.mjs`／`gh-app-token.sh` 兩邊相同，`triage.mjs`／`classify.mjs`／pipeline 本機領先、origin 零 commit，用本機版跑。另查 origin 側 9/09 分岔後零 feedback-triage commit、零 archive 變動，這條線只有本機在跑，沒有雙邊重複開 issue 的風險。分岔本身仍是 🔒（OBSERVER-QUEUE #56 本機側），比照前十三輪不 pull／rebase／push，只 stage 本任務範疇的檔。

## 收官 checklist

| 檢查項                  | 狀態                                                                                           |
| ----------------------- | ---------------------------------------------------------------------------------------------- |
| BECOME gate             | ✅ wake-context 讀到 wake:END sentinel，selftest 10 項全綠                                     |
| HG11 機器身份           | ✅ ghs\_ token，權限與安裝範圍皆如預期                                                         |
| HG13 讀全文才判斷       | ⚠️ 讀了，但工具當時只給兩欄，第三欄在核對 issue 時才讀到。已修工具                             |
| `--commit`              | ✅ 1 筆 filed → #1746                                                                          |
| HG2/HG3/HG4/HG9         | ✅ 零 email／verbatim／feedback id／tilde fence，逐條核過                                      |
| HG12b archive-reconcile | ✅ 86/86                                                                                       |
| HG12c comment-reconcile | ✅ 85/86，#1252 上游已刪 git 留著                                                              |
| HG8 不以維護者身份開口  | ✅ 本輪零對外留言                                                                              |
| git add 範圍            | ✅ archive 1 檔 + triage.mjs + test + pipeline + LESSONS + 本檔 + MEMORY 索引，不碰 babel 產出 |
| push                    | ⏸️ 刻意不 push（真分岔，OBSERVER-QUEUE #56 本機側，🔒）                                        |

## Handoff 三態

繼承上一 session（09-17 feedback-triage）：

- ⏳ blocked（延續）— main 本機 771 未推送 commit 與 origin 548 個真分岔，118 篇雙邊譯文取捨等哲宇選 A/B/C，per OBSERVER-QUEUE #56（本機側編號，origin 側 #56 是另一件事）。
- ⏳ blocked（延續）— issue #1729（馬英九腳註 2/2 對不上）等 FACTCHECK Full mode 排程。
- ⏳ blocked（延續，給哲宇隨 #56 一起拍）— 用語庫 blanket claim 血緣複查，選項在 origin 側 `memory/2026-09-16-090341-twmd-maintainer-am.md` §Handoff。
- [ ] pending（延續，給合併 #56 的那個 session）— OBSERVER-QUEUE 兩側 #56/#57 撞號的主鍵策略，細節在 LESSONS `decision-queue-forked-with-the-tree-it-lives-in`。
- [x] ~~dispatcher PID 12398 跨十四個排程窗未重啟，延續觀察~~ — retired by 09-18 babel-nightly：揪出 launchd keepalive 後換設定重啟，舊 PID 已不存在。

本 session 新 handoff：

- [ ] pending（給 08:30 maintainer-am）— [#1746](https://github.com/frank890417/taiwan-md/issues/1746) 周蕙 4/25 小巨蛋「售罄／加開」勘誤，走 CORRECTION-PIPELINE 查證後修 `knowledge/Music/周蕙.md`。回覆讀者屬人類 gate。
- [ ] pending（1-file 候選，給 distill）— `held-fact-never-crosses-into-the-layer-that-acts-on-it` vc=5 且第五次長在修第一次的工具上，同 routine 內五次。候選機械化仍是那道「出口完整性檢查」，本輪沒做。

## Beat 5 — 反芻

這條線今天真的有東西可交，五分鐘就跑完了。值得記的是那個 ⚠️：我照 HG13 先讀了全文才動手，讀完的感覺是「這筆乾淨」，而那個感覺建立在工具給我的兩段文字上。第三段要等到開完 issue、回頭數 fence 有幾個時才看見。8/31 造 `--show` 是為了讓「讀全文」不再靠當班自覺，今天它做到了讓人不再自覺去查——因為有了入口，我就沒再懷疑入口本身讀得全不全。反芻寫進 diary。

🧬

---

_v1.0 | 2026-09-18 07:2x +0800_
_session twmd-feedback-triage — 周蕙勘誤 #1746 / `--show` 補印 correct_info / 分岔不 pull_
_誕生原因：cron 07:00 例行，核對開完的 issue 時發現 HG13 的讀取入口只印了四個讀者欄位裡的兩個_
_核心洞察：一支只讀一半的讀取工具，比沒有工具更容易讓人以為讀完了；閘門的入口自己也是要被對賬的產物_
_LESSONS-INBOX 候選：`held-fact-never-crosses-into-the-layer-that-acts-on-it` 第五個 instance（已補進原 entry）_
