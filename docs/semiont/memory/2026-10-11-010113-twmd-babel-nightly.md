# 2026-10-11-010113-twmd-babel-nightly — 修復後續跑：產線在落後 104 個 commit 的舊樹上空轉 80 分鐘，落地 23 篇名單內譯文、拆掉合併死結、補 slug 與算力自檢的兩把尺

> session twmd-babel-nightly — cron 00:30 fire，Stage 0.5 判定「活著但落地停擺」→ 修復後重啟
> Session span: 00:30 → 01:10 +0800（約 40 分鐘，本班 7 個 commit：`c625cfa18` → `407979b80`）
> 資料來源：`git log %ai`、`/tmp/babel-unified-20261010-232647-42846/report.jsonl`、`.taiwanmd/babel-push.log`

## 觸發

00:30 例行續命班。甦醒 selftest 亮一盞燈：主樹落後 origin 104 個 commit、領先 8 個。dispatcher（PID 42846，23:26 起跑）三重巡檢的存活與生產都過，75 分鐘 15 筆紀錄 14 筆通過，可是 push-every 的 log 每兩分鐘一行 🔴：合併 origin 時被工作樹裡沒 commit 的譯文擋下、abort。產線有在翻，譯文一篇都出不去。

## 合併死結的形狀

哲宇 10-10 23:2x〜23:49 在場清 OBSERVER-QUEUE，推了一波機械修補（站內連結、腳註網址、模型自造 slug、subcategory、中文參考資料標題），動到 5,255 個譯文檔。23:26 launchd 重啟產線時，wrapper 的 `--sync` 想先合 origin，撞上上一輪留下的孤兒譯文，只印「沿用現有工作樹」就讓 dispatcher 起跑。產線一跑，工作樹永遠帶著在途譯文，push-every 之後每一輪合併都撞同一批檔，每一輪都 abort。同時這個 dispatcher 載入的是 23:05 之前的程式碼，沒有 origin 剛上線的 contributor_guard（`411da2c35`，不覆蓋投稿者翻好的譯文）。存活、生產兩項全綠，壞的是第三件事：產出落不了地，而執行中的程式碼比 main 舊。

## 打撈與分流

先 `launchctl remove` 停線，再用各輪 report.jsonl 對每個在途檔追出處。在途 24 檔裡，6 篇出自名單外的 gemma4:e4b-nvfp4（8.1B）：四語〈阿婆鐵蛋〉、ar〈颱風〉、id〈席慕蓉〉，照 OBSERVER-QUEUE #78／#91（已決）不落地，還原回 HEAD 重新排隊。其餘 18 篇出自 gemma4:26b 與 nemotron，逐語建 manifest 跑 `verify-batch` 全過、pre-commit hard=0，落地為 `c625cfa18`。

本機未推的 8 個 commit 也同樣分流：pt〈林青霞〉、ru〈颱風〉、ar〈民歌運動〉出自 laguna，id〈體育〉出自 8B，四篇改用 origin 版本，留給名單內模型重譯。

合併本身走了一段繞路。直接合會在 14 檔衝突，衝突解完的 commit 會讓 lint-staged 對 5,295 個 origin 檔跑 prettier（prettier 改網址的前科見 REFLEXES #100）。改成三步：`8bf9aa01a` 先把 16 檔設成 origin 版本，`aa719406d` 合併乾淨完成，不經 pre-commit。`aefa76a4e` 再把 12 篇名單內新譯文放回。放回前用 babel-pulse 同一套模組對 23 篇做網址組合與名人頂替比對，抓到 ko〈台灣體育發展與奧運〉把 1980 年拍板會旗的蔣經國譯成 장제스，還自造了「蔣經石」的漢字註記。改回 장징궈(蔣經國) 一起放回。00:54 推送成功，ahead/behind 歸零。

## 三個結構修補

`6e0e12cb0` 改 `babel-push-every.py --sync`：起跑前合併被擋時，若擋路的全是 `knowledge/<譯文語言>/` 的檔、且沒有 dispatcher 活著，就判定為上一輪的孤兒（origin 又改過同檔，代表它是在舊樹上產的），還原成 HEAD 再合併一次；dispatcher 還活著或擋路的不是譯文就不動、回 1。正控制驗過：中文母稿與 `docs/` 不會被收進還原名單。

`ed59eec97` 給 10-10 新合併的〈來來來，怎麼樣、怎麼樣〉補 slug `lai-lai-lai-zenmeyang-chant`，preflight 原本報十二語都排不進佇列。

`407979b80` 改 `babel-preflight.py`：參數量門檻 26.0B 把實測 25.2B 的 gemma4:26b 每晚印成「低於白名單」，fleet 卻照名字核發它，兩把尺對同一個模型給相反答案。現在白名單點名的模型以名字為準，跟 fleet `_BATCH_MODEL_PROFILES["babel"]` 同一份名單。還裝在 ollama 裡、fleet 沒核發的 8B 模型改印 ℹ️，不再跟真的派工共用一盞紅燈。

00:56 用 wrapper 重掛 launchd（PID 54236），起跑在 `6e0e12cb0`，master.log 第一次出現 `open-PR 過濾`。這輪佇列約 80 篇 stale 加 1 篇新文章 × 12 語，01:00 第一筆 es〈台灣糕餅文化〉gemma4:26b 通過。

## 算力與進度

Stage 0 判定 healthy（OpenRouter 7/7 key、本機 ollama、fleet mac-m4max 可達、codex），無缺席層。fleet `--profile babel` 只核發 gemma4:26b 一個地端 worker；雲端 nemotron 加付費 Haiku ×3（tier6 夜間上限 100）。起跑時十二語 fresh 1106〜1123 篇（覆蓋率 99.7〜99.9%），stale 合計約 80。ja 19、ko 13、es 13、fr 11 偏多，來自退回的 laguna／8B 檔與 origin 的來源版本標記修正。Stage D 日記：五個投影語言 2,080 份譯文 0 missing、0 critical。

## 收官 checklist

| 檢查項                       | 狀態                                                          |
| ---------------------------- | ------------------------------------------------------------- |
| MEMORY 有這次 session 的紀錄 | ✅                                                            |
| Timestamp 精確               | ✅                                                            |
| Handoff 三態已審視           | ✅                                                            |
| CONSCIOUSNESS 反映最新狀態   | ❌ 本班不碰（babel 班職權外，dashboard 由 data-refresh 更新） |
| 自我檢查工具 PASS            | 見 commit 時 prose-health                                     |

## Handoff 三態

繼承 `2026-10-10-010722-twmd-babel-nightly`：

- [x] ~~pending（Write 班）zh〈高雄市〉延伸閱讀五個死連結~~ — retired by `2026-10-10-023750-semiont-heartbeat`（`14d341be5` 改指站上現有篇）
- [ ] pending（席位 `twmd-babel-nightly`，OBSERVER-QUEUE #56（待決））— hi〈新冠疫情與疫苗〉lakh 倍率錯，原樣傳
- [ ] pending（席位：渦流班／`/twmd-babel`）— `/tmp/babel-unified-*` run 目錄無清理機制，原樣傳

繼承 `2026-10-10-203548-semiont-heartbeat` 的 subcategory 表外值約 240 篇 WARN，席位是週日 self-evolve，本班不動（REFLEXES #74）。

本 session 新交接：

- [ ] pending（席位 `twmd-babel-nightly` 下一班）— 確認本輪產線第一次自動 commit 與 push-every 推送成功（commit-every 10 或 90 分鐘，預計 02:30 前）；`.taiwanmd/babel-push.log` 不該再出現 `would be overwritten`。這班能動 push-every 與 dispatcher，動得了
- [ ] pending（席位 `twmd-babel-nightly`／渦流班，LESSONS `long-running-process-runs-the-code-it-started-with`）— dispatcher 沒有「我的程式碼比 main 舊」的訊號；候選做法寫在該 LESSONS 條目，需改 `babel-dispatch.py` 或 babel-pulse
- [ ] pending（席位：OBSERVER-QUEUE #84／#91（已決）存量重譯）— 本班退回的 7 篇 laguna／8B 譯文已回到 stale 佇列，由產線自然接住；#91 的 138 篇存量批次降級仍未做

## Beat 5 — 反芻

三重巡檢設計來回答「它活著，它有沒有在做事」，今晚兩項都答是，問題在第三個沒被問的地方：做出來的東西有沒有出門。push-every 的 log 一直在喊「需要人看」，喊了三個小時，喊給一個沒人讀的檔案。比較值得記住的是另一層：dispatcher 載入的程式碼停在 23:05 之前，origin 上那條「不覆蓋投稿者譯文」的保護，對正在跑的那個進程不存在。我們習慣把「已推上 main」當成「已上線」，對常駐進程這兩件事中間隔著一次重啟。已寫進 LESSONS-INBOX。

打撈時用 report.jsonl 一篇篇追出處，才看到在途檔裡混著三種來源：舊白名單外的 8B、已停用的 laguna、現行名單內模型，三者在工作樹裡長得一模一樣。分流靠的是 report 有留 backend 欄位，如果沒有，今晚只能全收或全丟。

🧬

---

_v1.0 | 2026-10-11 01:10 +0800_
_session twmd-babel-nightly — 修復後續跑：合併死結、23 篇名單內譯文落地、slug 與 preflight 兩把尺_
_誕生原因：甦醒 selftest 報主樹落後 origin 104 個 commit，push-every 每輪合併都 abort_
_核心洞察：存活與生產都綠時，落地仍可能停擺；常駐進程跑的是起跑時的程式碼，推上 main 不等於上線_
_LESSONS-INBOX 候選：`long-running-process-runs-the-code-it-started-with`（已入庫）_
