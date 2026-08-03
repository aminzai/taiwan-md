# 2026-08-02-093355-twmd-flywheel-watch

✅ BECOME ack: mode=micro / Q14=PASS

routine `twmd-flywheel-watch` @ 09:33，跑在指揮部（commander-macbook）。工作只有一件：從飛輪外面看它還活著沒有。

---

## 判定：飛輪在轉，日更六條加週更三條全部留痕，零警報

`git fetch origin`（不 pull）後跑 `python3 scripts/tools/flywheel-watch.py`，exit=0 / severity=ok。24 小時窗口（origin/main）commit 22 筆，`[routine]` 標記 14 筆，silent 與 unknown_cron 兩份清單都是空的。工具的分類欄不當結論用，逐條回 `git log origin/main` 對過訊息：

| 時間  | routine                 | 產出                                                          |
| ----- | ----------------------- | ------------------------------------------------------------- |
| 01:16 | twmd-news-lens-weekly   | W31 三源交叉，6 條候選，ARTICLE-INBOX stale flag              |
| 03:17 | twmd-distill-weekly     | W31 distill，REFLEXES #56 v6 + #75(f)，未消化 14→8            |
| 04:16 | twmd-self-evolve-weekly | REFLEXES #38 加 (f) 存活≠生產變體，vc 1→3                     |
| 05:33 | twmd-embeddings-nightly | bge-m3 12 語 8695 向量 0 fail，vi 與 id 雙雙站穩門檻          |
| 05:38 | twmd-routine-sync       | 17 條全 in-sync，零漂移連續第四日                             |
| 06:14 | twmd-data-refresh-am    | 14 步全綠，文章 875，第五個連續全綠早晨                       |
| 06:41 | twmd-spore-harvest-am   | 4 spores，零新勘誤                                            |
| 07:10 | twmd-feedback-triage    | 隊列空，archive 掃描零新同步                                  |
| 08:46 | twmd-maintainer-daily   | PR #1287 黑蝙蝠中隊 merge-first + heal，deploy 一度轉紅後復綠 |

跟昨天最大的差別在 maintainer-daily：昨天是空場只留索引，今天真的接到一個 PR，補完 frontmatter、腳註、延伸閱讀，還修了對位句型。週六的三條週更（news-lens / distill / self-evolve）也都在凌晨依序落地。live 狀態 dump 齡 3.3 小時。

## 24hr 總數從 73 掉到 22，不是飛輪變慢

昨天窗口有 73 筆、今天只有 22 筆，差距全在 vortex-babel 產線：它跑在指揮部這台，今天的成果還留在本機（`git rev-list origin/main...HEAD` 顯示本地領先 32 筆、落後 19 筆）。origin/main 看不到它們，不代表它停了。這條 routine 量的是 routine 飛輪，babel 產線的推送節奏歸它自己管，本 cycle 不碰。

## 第一把尺的前綴缺口第二天仍在

工具的 `fired` 清單今天又出現 `twmd-memory`、`twmd-heal`、`twmd-embeddings` 三個不存在的 routine 名，原因跟昨天同一個：收官 commit 寫成 `🧬 [routine] memory: twmd-data-refresh-am @ ...`，第一把尺取 `[routine] ` 後第一個 token，抓到的是主題字而不是 routine 真名。今天 embeddings-nightly、routine-sync、data-refresh-am、spore-harvest-am、maintainer-daily 五條都是這個句型，第一把尺一條都沒認出來，全靠第二把尺（MEMORY 索引的 session-id handle）補上。

昨天記為 vc=1，今天同型重現升 vc=2。缺口仍是同一個：某條 routine 若只用這種 commit 句型、又剛好沒寫 MEMORY 索引列，會被誤報成靜默。修法不變，解析時先剝掉 `memory: ` / `heal: ` / `embeddings: ` 這類主題前綴再取名。本條 routine 只看不動手，續留 handoff。

## 不動手的部分

工作樹有十幾個已改檔加三十幾個未追蹤檔，全是平行 babel 產線的產出，全程不碰。不 pull、不 rebase，只 commit 自己的兩個檔。沒有需要觀察者決策的事項。

寫索引時多做一步：本機 MEMORY.md 落後 origin 十三列（今天各 routine 的收官都推上去了，這台還沒接），直接在舊尾巴後面接一列，等 babel 產線下次併回來就會在同一個錨點撞上。改成先 `git checkout origin/main -- docs/semiont/MEMORY.md` 單檔對齊再接，工作樹其餘檔案一根寒毛都沒動，而合併時雙方那十三列內容相同、只有我這一列是單邊新增，可以自動接上。單檔 checkout 不是 pull，這條 routine 的禁令守住了。

---

## Handoff 三態

繼承上一份 handoff（來源 `2026-08-01-093254-twmd-flywheel-watch.md`）——五條全部非本 routine 範疇，原樣傳遞：#1264 seo-meta 門檻校準、#1184 justfont 網域白名單、#1286 轉換器詞性擴充、台灣鎢供應鏈 Bucket D 框架待哲宇拍板、stash@{0}/{1} 長期未認領。

- [ ] **flywheel-watch.py 第一把尺剝前綴**（vc=2，連兩天同型）：`routine` 名解析要跳過 `memory:` / `heal:` / `embeddings:` 這類主題前綴，否則這類句型的 routine 只剩第二把尺護著。下一個有工具改動額度的 session 動手即可，非急件
- 無 blocked

---

_session 2026-08-02-093355-twmd-flywheel-watch — cron @ 09:30 指揮部。不碰營運機排程、不 pull、只 commit 本 routine 自己的兩個檔。_
_核心洞察：commit 總數掉了三分之二卻不是飛輪變慢，是產線的成果還沒推出去——看 origin/main 的儀器只看得見推上去的那部分，讀數要連著「量的是哪一層」一起讀。_
