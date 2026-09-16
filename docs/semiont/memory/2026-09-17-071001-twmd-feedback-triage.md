---
session: '2026-09-17-071001-twmd-feedback-triage'
date: 2026-09-17
routine: 'twmd-feedback-triage'
mode: 'review'
---

# twmd-feedback-triage @ 2026-09-17 07:10 — 佇列又空了，但昨天那筆已經在一天內閉環。想把它長出的決策送進佇列時，發現佇列本身分成了兩本

> session twmd-feedback-triage — cron 07:00 daily（maintainer-am 之前）
> Session span：07:10:01 → 07:2x +0800（0 個 knowledge 變更，1 份 archive 留言同步，1 條 LESSONS，本檔）
> 資料來源：`triage.mjs` 報表 / `gh issue view 1733` / `git diff main origin/main -- docs/semiont/OBSERVER-QUEUE.md`

✅ BECOME ack: mode=review / 8 organ 最低=🫀 心臟 30（red，自 2026-09-15）/ Q13=PASS / Q14=PASS

## 觸發

07:00 例行。昨天十輪來的第一筆真回報（#1733「消息」被判為中國用語）已經開成 issue，今天要看有沒有新的，
並把留言層同步回主權層。

## 這輪做了什麼

`fetched 0`，最近一筆回報 2026-09-15（距今 1.6 天，status=filed），讀取端沒在漏接。
零輸入照樣跑完 `--commit`，收進一則留言：09-16 上午 frank890417 在 #1733 留下的維護紀錄，判定回報屬實、
已修 `ca0a0926b`（PR #1737），`data/terminology/訊息.yaml` 的 `fork_type` 從 B「1949 分流」改成 F「同詞不同語感」，
頁面 FAQ 從「是，『消息』是中國大陸的常見說法」改為「兩岸都用，但語感不同」。issue 已 CLOSED。
從 07:00 開 issue、08:30 收割修好、當天關閉——這條線設計裡寫的「當天閉環」，這次真的在 26 小時內走完了。

兩道對賬：`archive-reconcile=85/85` ✅，`comment-reconcile=84/85`（上游已刪留言 1 份紀錄 git 留著：#1252，主權層正常）。
`file=0 reject=0 skip=0 hold=0`。HG11 機器身份驗過：`ghs_` token、`{"issues": "write", "metadata": "read"}`、安裝範圍 `frank890417/taiwan-md` 一個庫。
沒有需要 `--show` 的筆（佇列空）。

## 想路由一條決策，結果先量到佇列分家了

那則維護紀錄末尾附了一個血緣量測：全庫 2,003 條用語走最寬那層「是中國大陸的常見說法」斷言，1,635 條的 `fork_type`
是匯入預設值 B，抽樣 25 條有 3 條本身就是教育部辭典詞目。全面複查 >50 檔且主權敏感，命中 §自主權邊界。
09-16 maintainer-am 的 memory 把 A/B/C 三個選項與推薦 default（C：改模板先止血，再排 B）寫進了 handoff——但只在 handoff，
沒進 OBSERVER-QUEUE。跟 9/13 diary 記的 #56 是同一個形狀：選項寫好了，準確地交給下一個人，沒有人把它放到決策面。

本輪想把它正式路由進 §待決，動手前先比了本機與 origin 的 `OBSERVER-QUEUE.md`：本機編到 #57（#56 是分岔裁決、#57 是 SPORE-INBOX 高原），
origin 編到 #67（#56 是十語 941 處數量級譯錯、#57 是 102 行整行沒翻），兩側都是 9/09 分岔後各自從「下一個空號」往下編的。
本機 33 份 memory/diary 寫「per OBSERVER-QUEUE #56」指分岔裁決，origin 那側 2 份寫「#56」指的是譯錯。
我要新增的 #58，在 origin 已經是「80 篇參考區標題還是中文」。

所以**這輪沒有把用語庫決策寫進本機佇列**：寫進去只會讓撞號再深一層，而且哲宇讀的是部署那一側，看不到。
決策本身沒丟（origin 側 9/16 maintainer memory handoff 有完整選項），丟的是它到觀察者面前的路，跟 #56 自己的處境一模一樣。
記進 LESSONS `decision-queue-forked-with-the-tree-it-lives-in`。併入 #56 裁決時要一起處理的事：兩側 #56/#57 重編號、
回改 35 份交接文的引用（或改用進佇列日＋slug 當主鍵），以及一道「本機 vs origin §待決 最大編號」的對帳行。

## Stage 0 的判斷：這輪一樣不 pull

`check-parallel-actor.sh` 報 ACTOR_BUSY（babel dispatcher PID 12398 第四夜仍在跑）＋ origin 領先 203。
逐檔驗本 routine 依賴的五個檔：`archive.mjs`／`gh-app-token.sh` 兩邊相同，`triage.mjs`／`classify.mjs`／`FEEDBACK-TRIAGE-PIPELINE.md`
全是本機領先（9/16 那批 idea 來源 URL 修補），origin 對這五個檔零 commit。照 9/14 教訓，讀 origin 版反而退回舊版，所以用本機版跑。
分岔本身（ahead 683 / behind 203）是 🔒 紅線，缺席協議亦不代理，比照過去十二輪不 pull/rebase/push，只 stage 本任務範疇的檔。

## 收官 checklist

| 檢查項                  | 狀態                                                               |
| ----------------------- | ------------------------------------------------------------------ |
| BECOME gate             | ✅ wake-context 讀到 wake:END sentinel，selftest 10 項全綠         |
| HG11 機器身份           | ✅ ghs\_ token，權限與安裝範圍皆如預期                             |
| HG13 讀全文才判斷       | N/A（fetched 0）                                                   |
| `--commit` 零輸入照跑   | ✅ 1 則留言同步進 git                                              |
| HG12b archive-reconcile | ✅ 85/85                                                           |
| HG12c comment-reconcile | ✅ 84/85，#1252 上游已刪 git 留著                                  |
| HG8 不以維護者身份開口  | ✅ 本輪零對外留言                                                  |
| git add 範圍            | ✅ 只 archive 1 檔 + LESSONS + 本檔 + MEMORY 索引，不碰 babel 產出 |
| push                    | ⏸️ 刻意不 push（真分岔，OBSERVER-QUEUE #56 本機側，🔒）            |

## Handoff 三態

繼承上一 session（09-16 feedback-triage）：

- ⏳ blocked（延續）— main 本機 683 未推送 commit 與 origin 203 個真分岔，118 篇雙邊譯文取捨等哲宇選 A/B/C，per OBSERVER-QUEUE #56（**本機側編號**，origin 側 #56 是另一件事，見本檔第三節）。
- ⏳ blocked（延續）— issue #1729（馬英九腳註 2/2 對不上）等 FACTCHECK Full mode 排程。
- [x] ~~#1733 開著時考慮升成 `needs-verification`~~ — retired by 本輪：09-16 maintainer 已當事實問題查證修好並 close，不需改標籤。

本 session 新 handoff：

- ⏳ blocked（給哲宇，隨 #56 一起拍）— 用語庫 blanket claim 血緣複查（2,003 條／1,635 條 B 預設／抽樣 12%），選項 A/B/C 與推薦 C 完整寫在 **origin 側** `memory/2026-09-16-090341-twmd-maintainer-am.md` §Handoff。本機佇列因撞號未登記，合併 #56 時一併補進佇列。
- [ ] pending（給合併 #56 的那個 session）— OBSERVER-QUEUE 兩側 #56/#57 撞號，合併前先決定主鍵策略（重編號＋回改 33+2 份引用，或改「進佇列日＋slug」），細節在 LESSONS `decision-queue-forked-with-the-tree-it-lives-in`。
- [ ] pending（延續觀察）— dispatcher PID 12398 跨十四個排程窗未重啟，無異常訊號，不動作。

## Beat 5 — 反芻

這條線今天的正事是一個空佇列與一則收進來的留言，五分鐘就跑完了。值得記的是那則留言把一個決策丟給了我，
而我在把它放到該放的位置之前，先發現那個位置已經有兩個版本。分岔的成本一直被算成「檔案數」與「義工工時」，今天量到第三種：
**指向決策的名字失效了**。33 份交接文說「#56」，在觀察者會讀的那本裡是別的東西。反芻寫進 diary。

🧬

---

_v1.0 | 2026-09-17 07:2x +0800_
_session twmd-feedback-triage — 零回報 / #1733 一天閉環 / 決策佇列兩側撞號_
_誕生原因：cron 07:00 例行，把留言層同步回主權層時撞見用語庫決策沒地方放_
_核心洞察：載決策去找觀察者的器官自己也會分岔，而「單一佇列」這個假設沒有任何儀器在守_
_LESSONS-INBOX 候選：`decision-queue-forked-with-the-tree-it-lives-in`（已寫入）_
