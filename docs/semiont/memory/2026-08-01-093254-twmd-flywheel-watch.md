# 2026-08-01-093254-twmd-flywheel-watch

✅ BECOME ack: mode=micro / Q14=PASS

routine `twmd-flywheel-watch` @ 09:32，跑在指揮部（commander-macbook）。工作只有一件：從飛輪外面看它還活著沒有。

---

## 判定：飛輪在轉，六條日更全部留痕，零警報

`git fetch origin`（不 pull）後跑 `python3 scripts/tools/flywheel-watch.py`，exit=0 / severity=ok。24 小時窗口（origin/main）commit 73 筆，`[routine]` 標記 7 筆，silent 與 unknown_cron 兩份清單都是空的。工具的分類欄不當結論用，逐條回 `git log origin/main` 對過訊息：

| 時間  | routine                 | 產出                                         |
| ----- | ----------------------- | -------------------------------------------- |
| 05:34 | twmd-embeddings-nightly | bge-m3 12 語 8686 向量，0 fail，vi 跨 400 篇 |
| 05:38 | twmd-routine-sync       | 17 條全 in-sync，零漂移連續第三日            |
| 06:15 | twmd-data-refresh-am    | 14 步全綠，文章 875，本週新增 22             |
| 06:45 | twmd-spore-harvest-am   | 6 events，零勘誤                             |
| 07:08 | twmd-feedback-triage    | 隊列空，同步 2 則維護者回覆進 git 主權層     |
| 08:44 | twmd-maintainer-daily   | 0 PR，5 件舊 issue 均無新 follow-up          |

maintainer-daily 今天是空場（0 PR、舊 issue 沒動靜），屬於「沒事就不 commit」那一類的反面——它照樣留了收官索引，所以在儀器裡看得見。這正是空場跟死掉能被分開的原因。第七筆是昨天 09:34 本條 routine 自己的 commit 滾進今天窗口。

其餘六十多筆是 vortex-babel 產線在指揮部這台連續跑（十語 unified dispatcher 加整點脈搏快照），不屬 routine 飛輪。live 狀態 dump 齡 3.3 小時。

## 第一把尺被 commit 訊息的前綴遮住，靠第二把尺接住

工具的 `fired` 清單今天出現 `twmd-memory` 跟 `twmd-embeddings` 兩個不存在的 routine 名。原因是收官 commit 寫成 `🧬 [routine] memory: twmd-routine-sync @ ...`，第一把尺（commit tag）取的是 `[routine] ` 後面第一個 token，於是抓到 `memory` 而不是真名。今天 embeddings-nightly、routine-sync、maintainer-daily 三條的 routine commit 全是這個句型，第一把尺一條都沒認出來，全靠第二把尺（MEMORY 索引的 session-id handle）補上。

兩把尺互補是設計本意，今天是它第一次真的獨力扛住三條。但這也標出一個假陽性缺口：某條 routine 如果只用 `memory:` 前綴這種 commit 句型，又剛好那次沒寫 MEMORY 索引列，會被誤報成靜默。修法是解析時剝掉 `memory: ` / `embeddings: ` 這類 topic 前綴再取 routine 名。不在本 cycle 動手（本條 routine 只看不動手），留 handoff。

## 不動手的部分

工作樹有十幾個已改檔加三十幾個未追蹤檔，全是平行 babel 產線的產出，全程不碰。這條 routine 不 pull、不 rebase，只 commit 自己的兩個檔。沒有需要觀察者決策的事項。

---

## Handoff 三態

繼承上一份 handoff（來源 `2026-08-01-064619-twmd-spore-harvest-am.md`）——五條全部非本 routine 範疇，原樣傳遞：#1264 seo-meta 門檻校準、#1184 justfont 網域白名單、#1286 轉換器詞性擴充、台灣鎢供應鏈 Bucket D 框架待哲宇拍板、stash@{0}/{1} 長期未認領。

- [x] ~~昨天兩條回看（第二把尺復活、本條不再自報靜默）~~ retired by 本 session：今天兩者都持續成立
- [ ] **flywheel-watch.py 第一把尺剝前綴**：`routine` 名解析要跳過 `memory:` / `embeddings:` 這類 topic 前綴，否則這類句型的 routine 只剩第二把尺護著。下一個有工具改動額度的 session 動手即可，非急件
- 無 blocked

---

_session 2026-08-01-093254-twmd-flywheel-watch — cron @ 09:30 指揮部。不碰營運機排程、不 pull、只 commit 本 routine 自己的兩個檔。_
_核心洞察：空場 routine 只要照樣留收官索引，儀器就分得出它跟死掉的差別；兩把尺的價值在今天第一次以「第一把全失手」的形式被證明。_
