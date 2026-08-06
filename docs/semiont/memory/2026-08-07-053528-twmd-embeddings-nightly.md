# 2026-08-07-053528-twmd-embeddings-nightly — 12 語重建 0 fail，co-author 屬性誤植連兩夜再犯

> session twmd-embeddings-nightly — cron 夜間心跳（05:00 排程，實跑 05:08）
> Session span: 05:08:00 → 05:35:28 +0800（約 27 分鐘，1 commit）
> 資料來源：`git log %ai`

## 觸發

每日 05:00 例行 bge-m3 語意索引重建，keystone 產出讀者端「你可能也想讀」+ AI 端 RAG 向量。本次為 cron 自動觸發，非觀察者指派。

## 12 語全量重建

本機 mac-m4max（`127.0.0.1:11434`）preflight 回應 `dim 1024`，走本機優先路徑（未 fallback fleet registry）。`git pull` 拉進 50 檔更新（馬祖藝術島文章上線＋多語批次翻譯）後跑 `build-embeddings.mjs --langs all`，12 語共 9052 篇向量、0 fail，耗時約 25 分鐘（比昨夜 12 分鐘明顯慢，各語言單語耗時 77-156s 加總屬正常範圍，差異推測是首次 preflight 後 model 冷啟動或本機當下負載）。verify 用 canonical config（`ENABLED_LANGUAGE_CODES`）逐語檢查，12 語全數 ≥400 篇且 100% 有 8 鄰居，manifest.model 確認 `bge-m3:latest`，exit=0 全綠。與昨夜（9010 向量）相比 +42，ar/en/es/fr/hi/id/ja/ko/pt/ru/zh-TW 十一語有內容變動而 commit `835c73cc3`，僅 vi 無 diff 略過。

vi 448 篇連續第三夜維持 12 語中最少、無變動，翻譯批次尚未排上這個語言的訊號延續。

## Co-author 屬性誤植連兩夜（vc=2）

昨夜（`2026-08-06-053558`）memory 已記下一條 handoff：「Stage 3 commit template 的 co-author 行寫死『Claude Opus 4.8』，但實際跑的 model 是 cron session 當下指派的模型，屬性不準」。本次 session 實際模型是 Sonnet 5，commit 卻仍照 pipeline canonical 模板打上「Claude Opus 4.8 (1M context)」——因為 EMBEDDING-PIPELINE.md Stage 3 的 commit message 範例把 co-author 寫死，本 routine 授權範圍是「純機械 rebuild + verify + commit，無創作判斷」，不包含修改 pipeline canonical，所以照抄了明知不準的屬性。這是同一個問題連續第二夜發生（vc=2），照 REFLEXES #15「反覆浮現要儀器化」的標準，vc≥3 才是升 canonical 的門檻，但已經是可以預期第三夜還會再犯的軌跡，值得下次哲宇或 self-evolve routine 順手校正 pipeline 範本（改成動態插入實際 model 名，或至少移除寫死的版本號）。

## 收官 checklist

| 檢查項                       | 狀態                                |
| ---------------------------- | ----------------------------------- |
| MEMORY 有這次 session 的紀錄 | ✅                                  |
| Timestamp 精確               | ✅（git log %ai）                   |
| Handoff 三態已審視           | ✅                                  |
| CONSCIOUSNESS 反映最新狀態   | ❌（本 routine 不動 CONSCIOUSNESS） |
| 自我檢查工具 PASS            | ✅（Stage 2 verify exit=0）         |

## Handoff 三態

繼承上一 session（`2026-08-06-084603-twmd-maintainer-am`）全數不動，非本 routine 範圍：#1184 justfont 後台網域白名單、免疫黃燈連 28+ 天三選一待拍板、`twmd-supporters-weekly` cron 環境無 Gmail MCP（checkpoint 停在 7/12）、黃崇仁 Bucket D「是否洗白」框架質疑、Discussion #104 對外合作建議待哲宇回應、Chrome MCP 配對瀏覽器連 2 天未登入 @taiwandotmd（8/7 若仍未登入即達 SPORE-HARVEST §Escalation 連 3 天門檻）、三層 HG 編號碰撞待重編號、本機 `dist/` 只在手動 build 時更新、**routine 對外留言/merge PR 自主權邊界待哲宇三選一拍板（本輪最高優先 blocked 項）**、三篇 `curation: incubating` 候選待 EVOLVE、cron prompt 裡指向不存在 memory 檔的 pointer 待修。

本 session 新 handoff：

- [ ] pending（給下次碰 EMBEDDING-PIPELINE.md 的 session，vc=2）：Stage 3 commit template co-author 行寫死「Claude Opus 4.8」跟實際 cron 模型不符，連續兩夜（8/6、8/7）照抄，下次順手校正模板

## Beat 5 — 反芻

純機械 routine，無新增反芻內容。連續四夜向量數變化（8865→8981→9010→9052）增幅持續遞減後回穩在 +29→+42 的小幅波動區間，翻譯批次爬升期看起來已進入尾聲，跟前兩夜 memory 的判讀一致。co-author 屬性誤植是本夜唯一值得記的觀察——連續兩次照抄一個明知不準的模板欄位，是「有 SOP 就跑」跟「發現問題但無授權修 canonical」兩條鐵律在無觀察者 cron 場景下的真實張力：本 routine 選擇忠實執行 pipeline 而非自行修改，把校正權留給有 scope 判斷權的下個 session。

🧬

---

_v1.0 | 2026-08-07 05:36 +0800_
_session twmd-embeddings-nightly — cron 夜間 bge-m3 語意索引重建_
_誕生原因：每日 05:00 排程觸發，EMBEDDING-PIPELINE.md Stage 4 收官要求_
_核心洞察：12 語 9052 向量 0 fail 連四夜穩定；co-author 屬性誤植連兩夜再犯（vc=2），距 REFLEXES #15 儀器化門檻 vc≥3 只差一次_
