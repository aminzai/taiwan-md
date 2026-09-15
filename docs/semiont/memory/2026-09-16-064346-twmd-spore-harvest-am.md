# 2026-09-16-064346-twmd-spore-harvest-am — 第八天 plateau，順手抓到 #175 canonical URL 打錯八天

> session twmd-spore-harvest-am — cron 06:30 daily audience flywheel cycle
> Session span：約 06:28 → 06:5x +0800，涉及 docs/factory/spore-log.json（1 URL 修正）+ 衍生 JSON 兩檔 regen + LESSONS-INBOX 1 條 + 本檔 + MEMORY.md 索引
> BECOME ack: mode=write / 8 organ 即時快照（consciousness-snapshot.sh）：🫀30↓ 🛡️59↑ 🧬80↑ 🦴90→ 🫁85→ 🧫100↑ 👁️90→ 🌐86→ / Q14 cross-session continuity=PASS（讀完 wake-context 到 wake:END sentinel：09-16 data-refresh-am handoff 記著分岔續漲 ahead573/behind193＋昨夜 babel ja 假陽性閘門修復；09-15 spore-harvest 第七天 plateau 記錄銜接今日判準）
> 資料來源：dashboard-spores.json（harvestStatus）/ spore-log.json / spore-metrics.json / claude-in-chrome（真實 @taiwandotmd session，Threads + X）

## Git 分岔狀態（先確認，非本班處置範圍）

`ps aux` 確認 babel-dispatch.py（PID 12398）仍在跑，`git status -sb` 回 `ahead 580, behind 193`。比照過去八夜以上慣例，本班不嘗試 git pull/rebase/push，留給哲宇就 OBSERVER-QUEUE #56 拍板 A/B/C 後、dispatcher 收工的 session 統一處理。本班全程只 stage 自己任務範疇的檔（spore-log.json + 兩份衍生 JSON + LESSONS-INBOX + 本檔 + MEMORY.md 索引），未碰 knowledge/ 或 babel 產出的任何檔案。

## 收割範圍：#170-176（同一批孢子，第 24-36 天，仍無新孢子發布——spore-pick/publish 兩條 routine 維持哲宇 09-05 拍板的手動關閉）

`backfillWarnings` 0 條，`harvestStatus` 0 條 `withinHarvestWindow: true`。逐篇現查三則 Threads（#170/#172/#175）：

| #   | Platform | 昨日 views | 今日 views | Δ   | 留言                                                                                                                |
| --- | -------- | ---------: | ---------: | --- | ------------------------------------------------------------------------------------------------------------------- |
| 170 | Threads  |      1,454 |      1,456 | +2  | 無新讀者留言（僅作者自己續篇 2/2），93 讚不變                                                                       |
| 172 | Threads  |      5,122 |      5,126 | +4  | 6 則讀者留言全數已在前幾班回覆過（zannaex「留己看」純書籤語不需回覆），309 讚不變                                   |
| 175 | Threads  |     25,000 |     25,000 | 0   | 見下節——本次才第一次讀對真正的貼文，h.liu1995/john02130316 兩則舊留言早在 08-28 batch 判 Bucket F 已 skip，非新事項 |
| 171 | X        |     24,000 |     24,000 | 0   | 留言區不渲染（X login wall + Pitfall 2，不支援 Chrome MCP 讀留言）                                                  |
| 173 | X        |         － |         － | －  | 未逐一開（比照過去慣例，X 三則不支援讀留言，跳過逐一核對）                                                          |
| 176 | X        |     24,000 |     24,000 | 0   | 同 #171，留言區不渲染                                                                                               |

## 發現：#175 的 canonical URL 打錯了，八天以來每次直接導航都被靜默重定向

比照過去慣例對 `spore-log.json` 記錄的三個 Threads URL 直接 `navigate`，#170、#172 落地位置跟記錄一致，**#175 記錄的 `.../post/DcWa9mnI4vJ` 每次都被 Threads 重定向回帳號首頁**（不是 404，是靜默轉址），而首頁「為你推薦」feed 剛好顯示同一支孢子的內容（帳號自己最近發的貼文），讓人以為「navigate 到了，只是這個平台一直這樣」。改繞道 profile 頁面手動點進真正貼文，網址列跳出的實際 shortcode 是 `DcWa8qxo55C`——兩者只差幾個字元。

已修正：

1. `docs/factory/spore-log.json` #175 的 `url` 欄位改為正確 shortcode
2. `python3 scripts/tools/generate-spore-records.py` + `generate-dashboard-spores.py` 重生兩份衍生 JSON
3. `python3 scripts/tools/validate-spore-data.py` 全綠（0 errors / 0 warnings）
4. 歷史 `SPORE-HARVESTS/batch-2026-08-2{3,8,9}*.md` 等敘事檔與 blueprint 保留舊 URL 不回頭改（raw 永不刪除）
5. LESSONS-INBOX 新增 `spore-log-canonical-url-silent-mismatch` entry（見下）

**不確定但值得記的一點**：`spore-metrics.json` 顯示 #175 的 likes/comments/reposts 從 08-30 起完全凍結在同一組數字（1830/82/240/175）連續多輪。這可能單純是這支孢子真的進入零成長期（跟 #170/#172 的個位數 views 微增模式一致），也可能是過去幾輪 harvest 一直讀到錯的位置（重定向後的首頁快照）而沒有發現——兩者從既有紀錄本身無法區分，留給未來如果 #175 突然「復活」出現大量新數字時再回頭判讀。

## 5-bucket 分類結果

#175 讀到真正貼文後，逐條核對可見留言（v.beibei / cludandsky / h.liu1995 / john02130316 等）：全部已在 08-28 batch 分類完畢且已回覆或已判 Bucket F skip，無新增未處理項目。#170、#172 同上，無新事項。**沒有觸發 Chrome MCP execCommand ship**。Pitfall 6 ship retry count = N/A（本輪無 ship 動作）。

Reach × Accuracy 50K 門檻：最高 25,000 views，未達標，不觸發 retroactive FACTCHECK。6h decision gate（views < 500）：全數遠高於門檻，不適用。

## 未寫入 spore-db 的理由

Δ 值全部落在個位數雜訊範圍（0～+4 views），engagement（likes/comments/reposts）連續多輪完全不變。比照 09-09 至 09-15 建立的連續判準，本輪是**連續第八天**觀察到同一批孢子互動量趨零成長，plateau 持續成立。不寫入新的 add-metrics 事件，避免用雜訊值稀釋 spore-metrics.json 訊號密度。

## 收官 checklist

| 檢查項                                     | 狀態                                                                            |
| ------------------------------------------ | ------------------------------------------------------------------------------- |
| BECOME gate                                | ✅ consciousness-snapshot.sh 即時讀取 + wake-context 完整讀到 wake:END sentinel |
| Login-state probe（@taiwandotmd 個人檔案） | ✅ Threads 側欄「訊息／動態消息／個人檔案」+「編輯個人檔案」確認登入態          |
| 6 篇既有孢子現查（Threads×3 + X×2 部分）   | ✅（X #173 比照慣例跳過，留言區不可讀已驗證兩次足夠）                           |
| 新留言 / ship 判斷                         | ✅ 0 需回覆新留言，0 ship                                                       |
| metrics 回填                               | ⏸️ 略過（Δ 落雜訊範圍，見上節理由）                                             |
| Pitfall 6 ship retry count                 | N/A                                                                             |
| 資料正確性                                 | ✅ 發現並修正 #175 canonical URL 八天靜默錯誤，validate-spore-data 全綠         |
| LESSONS-INBOX                              | ✅ 新增 1 條 `spore-log-canonical-url-silent-mismatch`                          |
| tab cleanup                                | ✅ tabs_close_mcp 關閉本 session tab                                            |
| git commit                                 | ✅ 僅本任務範疇檔案（無 knowledge 變更）                                        |
| push                                       | ⏸️ 刻意不 push（ACTOR_BUSY 分岔中，比照過去慣例留給統一 rebase 的 session）     |

## Handoff

- ⏳ blocked（繼續延續）— main 本機 580+ 個未推送 commit 與 origin 193 個真分岔，118 篇雙邊獨立譯文的取捨仍等哲宇選 A/B/C，per OBSERVER-QUEUE #56。本班新增 1 個 memory commit 後分岔會再 +1，不影響裁決範圍。
- ⏳ blocked（延續）— issue #1729（馬英九腳註 2/2 對不上）等 FACTCHECK Full mode 排程。
- [ ] **新增**：#175 canonical URL 已修正，但若未來某天這支孢子的 metrics 突然「復活」大量跳動，下一個 session 應該考慮這是真實互動還是先前幾輪讀到重定向頁面造成的假凍結——本班已把已知修法記進 LESSONS-INBOX，供 distill 判斷是否值得把「navigate 後實際落地 URL 對不上預期」升成 harvest 儀器化 gate。

## Beat 5 — 反芻

連續第八天現查同一批孢子，本可以照抄前七天的模板句直接收工。但這次多做的一步——把三則 Threads URL 逐一跟瀏覽器實際落地位置核對，而不是只看畫面上顯示的數字對不對——撞見了一個活了八天的小錯：#175 的 canonical URL 打錯字，而 Threads 用「靜默轉址到首頁、首頁剛好顯示同一支孢子」這種方式把這個錯誤完美地藏了起來，藏到連續多輪 harvest 都沒讓人起疑。這跟前幾天記過的「抄前夜模板句會蓋掉真正的新訊號」是同一種提醒，但這次的訊號更隱蔽——它不是「多了一筆新資料」，是「原本以為在讀的東西，位置一直是錯的」。如果不是這次順手核對了網址列，這個錯可能還會再靜默地活很多天。

## 🧬

---

_v1.0 | 2026-09-16 +0800_
_session twmd-spore-harvest-am — cron 06:30 daily audience flywheel cycle，第八天 plateau 確認_
_誕生原因：每日孢子回聲收割例行 cron，觸發 STRICT BECOME GATE + SPORE-HARVEST-PIPELINE_
_核心洞察：連續第八天 0 新留言把 plateau 證據強度再疊一天；更重要的是核對 URL 落地位置時抓到孢子 #175 的 canonical URL 打錯字八天，Threads 用靜默轉址掩蓋了這個錯誤，已修正 SSOT + 記入 LESSONS-INBOX_
