---
session_id: '2026-09-30-071330-twmd-feedback-triage'
session_span: '2026-09-30 07:00:00 → 07:18 +0800'
trigger: 'cron routine twmd-feedback-triage（每天 07:00 Asia/Taipei）'
observer: 'none（cron，無觀察者在場）'
beat_coverage: 'Beat 4 收官'
---

# 2026-09-30-071330-twmd-feedback-triage — 九輪零回報後的第一筆真回報：讀者指出用語庫查錯了辭典版本，而這正是佇列 #76 八天前預言的第二例

> session twmd-feedback-triage — cron routine 07:00
> Session span: 07:00:00 → 07:18 +0800（~18 min，2 commits）
> 資料來源：`git log %ai`

✅ BECOME ack: mode=review / 8 organ 最低=🛡️免疫 59（review_coverage=19，少 20.25 分）/ Q13=PASS / Q14=PASS

## 觸發

每天 07:00 的讀者回報轉錄班，把站上 `status='new'` 的回報機械性轉成 GitHub issue，讓 08:30 的維護班同 cycle 收割。連續八輪零回報之後，今天佇列裡有一筆。

## 一筆回報，開成 issue #1786

讀者程乙路 09-29 16:16 從 `/terminology/內核/` 送來回報，說「查字典請用簡編本，再來，台灣並沒有那麼常使用核心一詞」，附一則 Threads 連結。

照 HG13 先用 `--show` 把全文拉出來讀完才動手。判斷結果是可以公開轉錄：沒有指涉具名私人、沒有跟監所得的細節、沒有要求身份保密，通篇是對一個公開頁面的用語質疑。所以不用 `--exclude`，整批照跑 `--commit`。

開出 [issue #1786](https://github.com/frank890417/taiwan-md/issues/1786)（`enhancement` + `from-feedback`），作者是 `app/taiwanmd-semiont`（`is_bot=true`），主權層紀錄落在 `docs/feedback/archive/2026-09/6be75bb1-….md`，兩者都零 email。`idea` 分支自 v1.10 起會帶來源頁面 URL，這次確認有帶，維護班不必回頭查資料庫才知道在講哪一頁。

閘門逐條核過：HG2 無 email（issue body 與 archive 各掃一次 regex，0 命中）、HG3 讀者原話一字未改、HG4 帶 feedback id、HG9 tilde fence 包好、HG10 未命中 injection 所以沒加 `security-review`、HG11 token 是 `ghs_` 開頭且權限只有 `{"issues": "write", "metadata": "read"}`、安裝範圍實查為 `frank890417/taiwan-md` 一個庫、HG7 回寫後重跑 dry-run 確認佇列歸零。commit 後跑 `verify-commit-scope.sh --head 1` 驗範圍。本機有 babel writer（PID 9047／51717）在動五個檔，這道驗證這時候特別必要。

兩道對賬：`archive-reconcile=88/88` ✅；`comment-reconcile=87/88`，差的一份是 #1252 上游把留言刪了而 git 這邊留著，屬主權層正常運作那個方向。`archive-comments-synced=0` 這次讀得出來是真的沒有新留言，因為留言層對賬已經把 88 份都拿去問過線上一遍。

## 這筆回報是佇列 #76 的第二例

追上游之後這筆回報涵蓋的範圍比一則用語建議大。9/16 的 [issue #1733](https://github.com/frank890417/taiwan-md/issues/1733)（讀者指「消息」在教育部辭典本就是台灣詞目）已經把根因量過：`data/terminology/*.yaml` 有 2,003 條會走模板最寬那句「是，X 是中國大陸的常見說法」，其中 1,635 條的 `fork_type` 還是 06-22 匯入時的 B 型預設值、九成三零佐證。那份維護紀錄抽樣 25 條查辭典，3 條（12%）被標為中國用語的詞本身就是台灣辭典詞目。全面複查 >50 檔且逐條要主權敏感判斷，命中 §自主權邊界，09-22 登記成 [OBSERVER-QUEUE #76](../OBSERVER-QUEUE.md)（🔒紅線，推薦 C 先做再排 B）。

今天這筆踩的是同一個家族換一個詞條，而且它挑戰的正好是選項 B 的方法論前提：B 的篩法是「china 詞在教育部辭典查得到」，讀者說該查的是《簡編本》而非《重編國語辭典修訂本》。用哪一部辭典決定那約 180 條的名單長什麼樣，而《簡編本》收現代常用詞，正是 #76 但書「查得到不等於今天台灣常用」想要的那把尺。第二點「台灣並沒有那麼常使用核心一詞」指向模板另一個沒被量過的維度：台灣那側的建議詞本身常不常用。

所以本班把這一例寫進 #76 那一列本身，不只寫進交接。那一列自己記著「這條從 09-16 起在五班 handoff 原樣往下傳」，同一格也記著「下一個讀者從站外踩到的機率跟 #1733 一樣高」，八天後成真。交接傳得動資訊，傳不動急迫性。佇列那一列是這個決定真正住的地方。

本班沒有回覆回報者、沒有動 `data/terminology/`、沒有碰 #76 的推薦選項。對外開口與主權用詞的斷言都是人類 gate（HG8 / §自主權邊界）。

## 收官 checklist

| 檢查項                       | 狀態                                                   |
| ---------------------------- | ------------------------------------------------------ |
| MEMORY 有這次 session 的紀錄 | ✅                                                     |
| Timestamp 精確               | ✅（`git log %ai`）                                    |
| Handoff 三態已審視           | ✅                                                     |
| CONSCIOUSNESS 反映最新狀態   | ⏭️ derived 層接管（`dashboard-alerts.json`），本班未動 |
| 自我檢查工具 PASS            | ✅ `verify-commit-scope.sh --head 1` scope OK          |

## Handoff 三態

繼承 `2026-09-30-064319-twmd-spore-harvest-am`（非本班職權，原樣傳遞，不重抄明細，REFLEXES #74）：

- ⏳ blocked（延續）— issue `#1729`（馬英九腳註）等 Write session 帶哲宇 review；`OBSERVER-QUEUE #75`〜`#90` 待決。
- [ ] pending（延續）— routine-sync 對賬前 `git fetch`（10-04 self-evolve）、data-refresh Stage 1.5 寫明順序（`/twmd-routine`）、`.git/gc.log`、`md-extension` 10-02 觀察、babel 自造 slug 存量、`/terminology/變壓器`（10-05 用語月報）、404 unknown 裡可解析的大小寫與跨分類同名（maintainer-am）。明細見該檔。

本 session 新 handoff：

- [ ] pending（席位 `twmd-maintainer-am` 08:30，動得了：issue triage 與回覆草稿都在它的權限內）— [issue #1786](https://github.com/frank890417/taiwan-md/issues/1786) 今天開的，走 `from-feedback` 一般流程。**先讀 `OBSERVER-QUEUE #76`（待決）再判**：這是同一根因第二例，不要當成一條獨立的用語建議修掉一個詞條就 close，那樣會把第二個外部訊號用掉卻沒讓 #76 更可決。回覆讀者本人仍是人類 gate。
- [ ] pending（席位 `twmd-terminology-trends-monthly` 10-05，或任何帶 Full mode 的 Write session）— 讀者指《簡編本》才是該查的辭典版本，這件事可以在不碰 #76 紅線的前提下先量：拿 #76 選項 B 那約 180 條的候選名單，同一批詞分別對《簡編本》與《重編國語辭典修訂本》查一次，看兩把尺給出的名單差多少。量出來的數字直接餵 #76 的 B 選項成本估算。同一趟可併 `/terminology/變壓器`（既有交接）。
- ⏳ blocked（`OBSERVER-QUEUE #76`，待決，🔒紅線）— 用語庫 2,003 條的最寬斷言要不要複查、怎麼複查。本班已把 09-30 第二例寫進該列的證據段，未動推薦選項（C 先做再排 B）。解除條件：哲宇拍板。

## Beat 5 — 反芻

這條 routine 的第一行輸出連八輪都是 `fetched 0`，而 9/09 那輪為了分清「讀者沒話說」跟「讀者送不進來」，已經讓它在零的時候多印一行最近一筆回報的日期。今天那個零變成一，而我差點跳過的是「追上游」那一步，不是任何一道閘門。`--show` 讀完、三道 PII／verbatim／fence 都核過、對賬全綠，這一輪按流程就算完成了：一筆 idea 類回報轉成一則 issue，交給 08:30。

會停下來是因為回報裡「用語庫」這三個字碰到了兩週前讀過的東西。查 #1733 花了兩個指令，然後那條佇列列自己把預言和落空的記錄都寫在同一格裡：既寫著「五班原樣往下傳」，也寫著「下一個讀者踩到的機率一樣高」。八天後那句成真，踩點還挑在選項 B 的方法論前提上。

轉錄班的職責邊界很窄：讀者說了什麼，一字不改送進 issue，署名是機器。窄是對的，因為這條線讀最多不可信的文字。但窄不等於淺。同一筆回報可以只是「一個詞條的建議」，也可以是「一個已登記待決事項的第二次外部驗證」，兩者在報表上長得一樣，差別只在有沒有人花兩個指令去問一句「這個我是不是見過」。REFLEXES #73 講的查證反射慢過建造反射，在轉錄這一層的形狀是轉錄反射慢過**辨識**反射。手上那段文字要往哪裡去，是機械的。它跟已經知道的事有什麼關係，得主動去問。

🧬

---

_v1.0 | 2026-09-30 07:18 +0800_
_session twmd-feedback-triage — 九輪零回報後第一筆真回報，開 issue #1786，並認出它是 OBSERVER-QUEUE #76 的第二例_
_誕生原因：cron routine 07:00 fire；佇列裡有一筆讀者對用語庫「內核→核心」的質疑_
_核心洞察：(1) 一筆回報能不能被讀出它真正的量級，取決於有沒有人去問「這個我見過嗎」；轉錄是機械的，辨識得主動。(2) 讀者挑戰的層次落在 #76 選項 B 用哪一部辭典當篩子這個方法論前提，比一個詞條深一層。(3) 佇列那一格同時記著「五班原樣往下傳」與「下一個讀者踩到的機率一樣高」，八天後後者成真，所以證據要寫回決定住的那一層，不只寫進交接。_
_LESSONS-INBOX 候選：轉錄類 routine 的閘門全長在「這段文字能不能公開」上，沒有一道在問「這段文字跟已知的事有什麼關係」；辨識上游的動作目前掛在當班記不記得。_
