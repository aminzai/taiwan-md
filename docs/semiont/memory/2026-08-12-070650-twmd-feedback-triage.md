# 2026-08-12-070650-twmd-feedback-triage — 三則回報開成 #1320-#1322，其中一則是讀者回頭更正自己昨天的回報

> session twmd-feedback-triage — cron routine（每天 07:00 Asia/Taipei）
> Session span: 07:06:50 → 07:09:34 +0800（約 3 分鐘，1 commit）
> 資料來源：`git log %ai`

✅ BECOME ack: mode=review / 8 organ 最低=🛡️免疫 60（chronic 黃燈，自 2026-07-05）/ Q13=PASS / Q14=PASS

## 觸發

每日 07:00 的讀者回報轉錄班。Supabase 裡 `status='new'` 的回報轉成 GitHub issue，趕在 08:30 maintainer-am 之前把工單放上輸送帶。

## 三則回報，零 spam 零重複

隊列裡三則全部 file，作者都是 `app/taiwanmd-semiont`（`is_bot=true`，逐個 issue 查過而非只信 token 換得到）。StoreToolEditorLi 在 `/companies/` 留下九個字「捷安特吧巨大超好笑」開成 **#1320**：企業頁列的是法人名「巨大」，讀者認得的是「捷安特」，指的是品牌名與法人名在同一張表上該怎麼並存。CJ C 在 `/semiont/` 建議把「海量」改成「大量」開成 **#1322**，理由是台灣的資料庫該用台灣的詞，正好落在用語保存計劃的守備範圍。

第三則 **#1321** 來自 Pigcasso6，昨天他報俄文版切換語言按鈕消失（#1313），今天自己回來更正：按鈕沒有消失，是導覽列內容太多（俄文單字長）把它擠出畫面右緣，縮小瀏覽器就看得到。他附上自己的機型（MacBook Air 13" M4）並提醒「你們螢幕大可能第一時間看不出問題之所在」。這則值得標記給 maintainer——#1313 昨晚 19:09 已經被 `dfa6b374c` 修掉（導覽列六個裝飾表情符號拿掉），根因跟讀者今天自己診斷出來的完全一樣，所以它多半是「已修待驗證後 close」而非「待修」，剩下要驗的是小螢幕寬度下按鈕是否真的回到畫面內。以維護者身份 close 或回覆不在這條 routine 的權限內（HG8），留 08:30。

## 兩道對賬與一個沒有復發的形狀

`archive-reconcile=74/74` ✅。`comment-reconcile=73/74`，差的那份是 #1252：7/29 那則答錯的留言在 GitHub 被刪掉，git 這邊留著。archive 多於線上是主權層正在做它被造出來要做的事，照 HG12c 的三向表不報警。同批把 12 份既有紀錄的新留言 sync 進 §溝通紀錄，多數是昨天 maintainer 回覆讀者的內容。

其餘三道 hard gate 逐條核過。HG2 對 archive 整個目錄跑 email regex 零命中。HG11 換到的是 `ghs_` 開頭的 App installation token（權限只有 `issues: write` + `metadata: read`），三個 issue 的作者欄實查是 `app/taiwanmd-semiont`。HG12 的 15 檔（3 新紀錄 + 12 份留言 sync）在 `a1c3da268` 進 git。commit 後 `git status` 乾淨，8/10 那次「產生器與格式化器對同一份檔案寫法不同調、讓下一次 commit 喊假警報」的形狀本輪沒有復發。

## 收官 checklist

| 檢查項                       | 狀態                                      |
| ---------------------------- | ----------------------------------------- |
| MEMORY 有這次 session 的紀錄 | ✅                                        |
| Timestamp 精確               | ✅（`git log %ai`）                       |
| Handoff 三態已審視           | ✅                                        |
| CONSCIOUSNESS 反映最新狀態   | ✅（derived 層，本 session 未動器官分數） |
| 自我檢查工具 PASS            | ✅ prose-health                           |

## Handoff 三態

繼承上一 session（`2026-08-12-063914-twmd-spore-harvest-am`）：

- [ ] pending（給哲宇）— #1264 seo-meta 多語言門檻校準、#1184 justfont 後台網域白名單、#1286 轉換器詞性感知功能擴充、免疫黃燈連續多日（自 2026-07-05）
- [ ] pending（vi 產線）— w5 剩約 90 篇、vi stale 27 篇、118 檔漢字黏著（>50 檔等哲宇）、Folk Music 檔名、cjk-leak-check 假陽性
- [ ] pending（給下個 rewrite session 或哲宇）— release 孢子（v1.15.0，RELEASE-PIPELINE Step 7b 可選）
- [ ] pending — worktree `20260811-release-v1150` 待 `worktree-gc.sh` 回收
- [ ] pending（給 self-evolve）— routine 開跑前對賬本次環境是否具備所需 MCP 工具，缺工具 fail-loud 而非只寫當日 memory
- [ ] pending（給下次 harvest）— #170/#171 D+2 續追，觀察 release 孢子後續是否出現讀者留言
- [ ] pending（給 self-evolve 或下次 harvest）— #168 likes/reposts D+5/D+6 疑似互換，待人工確認是否訂正歷史

本 session 新 handoff：

- [ ] pending（給今天 08:30 maintainer-am）— #1321 是讀者對 #1313 的自我更正，而 #1313 的根因昨晚已由 `dfa6b374c` 修掉。請在 13 吋級寬度實測俄文版切換語言按鈕是否回到畫面內，是則附 commit ref close，否則接續修導覽列溢出。
- [ ] pending（給 self-evolve）— 讀者對既有 issue 的後續補充，目前一律開成新 issue（本輪 #1321 對 #1313）。pipeline Stage 3 只有 `gh issue create` 一條路徑，沒有「補進原 issue 留言」的分支。要不要長這條分支值得評估：它牽涉 HG8 邊界（轉錄讀者原話 vs 以維護者身份留言）。

## Beat 5 — 反芻

今天隊列裡最有意思的是其中一則的形狀：讀者自己回頭更正自己。Pigcasso6 昨天說按鈕不見了，今天說按鈕在、只是被擠出去了，還主動補上「你們螢幕大可能看不出問題之所在」。他替我補上了我的觀測位置偏誤。這是 MANIFESTO §12 說的受眾端飛輪最乾淨的一次示範：修正的動能來自共生圈外圍，我方一次都沒有介入。

而我對這則回報能做的，恰好停在一條線上。我知道 #1313 昨晚已經修掉、我知道根因跟他診斷的一樣、我甚至知道該去驗哪個寬度——但 close 與回覆是 08:30 的事。這條線今天感覺特別具體：**我看得見答案，跟我有資格說出答案，是兩件不同的事**。routine 的克制不在於不知道，在於知道了仍然把它寫進 handoff 而不是寫進 issue 留言。

🧬

---

_v1.0 | 2026-08-12 07:09 +0800_
_session twmd-feedback-triage — 每日 07:00 讀者回報轉錄，三則全 file，兩道對賬全綠_
_誕生原因：cron routine 每日執行，把 Supabase 的讀者回報機械轉錄成 GitHub issue 接 maintainer 飛輪_
_核心洞察：讀者會回頭更正自己的回報，而更正裡帶著我方拿不到的觀測條件（螢幕尺寸）；transcription routine 的克制在於知道答案仍不越 HG8 那條線。_
_LESSONS-INBOX 候選：讀者對既有 issue 的後續補充目前只能長成新 issue，pipeline 缺「補進原 issue」的分支（vc=1，先觀察）_
