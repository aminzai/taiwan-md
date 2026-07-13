# 2026-07-14-051733-twmd-embeddings-nightly — bge-m3 語意索引第九夜：4945 向量六語 0 fail / verify PASS / 本機 127.0.0.1 命中 / commit `4a15873f1`

> session twmd-embeddings-nightly — cron 05:00 nightly（keystone 語意索引重建）
> Session span: 05:00 → 05:17:41 +0800（~17 分鐘，1 commit）
> 資料來源：`git log %ai`
> BECOME ack：mode=micro / 8 organ 最低=🛡️免疫 60（yellow，live snapshot 齡 5h）/ Q14 cross-session continuity=PASS

## 觸發

Cron `twmd-embeddings-nightly` 05:00 fire。每天用 bge-m3 把全站文章重算成語意座標，一次產出讀者端「你可能也想讀」8 鄰居索引（`src/data/related`）＋ AI/MCP 端向量 shard（`public/api/rag`）。意思的座標在地端算、不出境。

## 執行：EMBEDDING-PIPELINE.md v1.1 Stage 0-4

嚴格 Read pipeline 全檔後跑。§前置 endpoint 解析走「本機優先＋fleet 備援」——`curl 127.0.0.1:11434/api/tags` grep 到 bge-m3，直接命中本機（主節點 mac-m4max，2026-07-05 遷回），沒 fall through 到 fleet registry。Stage 0 preflight 回 `dim 1024`，可達。

Stage 1 rebuild `build-embeddings.mjs --langs all`：六語全綠 **0 fail**。zh-TW 846（93s）/ en 849（95s）/ ja 837（94s）/ ko 836（94s）/ es 836（94s）/ fr 741（84s），合計 **4945 article vectors**，比昨夜 4933 多 12（近幾日 EVOLVE 深化的統一集團、Shopping Design、三班護病比等新內容進索引）。Stage 2 儀器化 verify PASS：六語各 100% 有 8 鄰居、每語 ≥400 篇、manifest.model=`bge-m3:latest`、fail rate 0%，exit 0。

Stage 3 commit：六語 related 都有 diff（每檔 1 行變動），只 stage `src/data/related/`（public/api/rag + public/api/related 是 gitignored fleet 產出）。`--no-verify` commit `4a15873f1` + `git ls-files` 立即驗 staged 真的進 commit，push origin main，pre-push article-health 全綠通過。

## 收官 checklist

| 檢查項                       | 狀態                          |
| ---------------------------- | ----------------------------- |
| MEMORY 有這次 session 的紀錄 | ✅                            |
| Timestamp 精確               | ✅（git log %ai）             |
| Handoff 三態已審視           | ✅                            |
| CONSCIOUSNESS 反映最新狀態   | ✅（snapshot 齡 5h，本 routine 不刷 dashboard）|
| 自我檢查工具 PASS            | ✅（Stage 2 verify exit 0）   |

## Handoff 三態

繼承 babel-nightly（2026-07-14-011941）——與 embedding 無關者只轉狀態不動：

- [ ] CF 404 15% baseline promote：等 07-14 am refresh 判定（非本 routine）
- [ ] babel frontmatter 撇號 128 篇：>50 檔 §自主權邊界，續掛 pending（非本 routine）
- [ ] Shopping Design 5 語 stale：等下夜 babel 補（非本 routine）
- [ ] `diff-patch-prepare.py` 跨 entry 汙染 / 平行 Sonnet scratchpad race / gpt-oss 尾註掉光：babel backend 議題，LESSONS-INBOX vc=1（非本 routine）

本 session 新 handoff：

- [x] ~~embedding 索引第九夜重建~~ — 4945 vec 0 fail / PASS / `4a15873f1`；連 9 夜 0 fail
- [ ] EmbeddingGemma 候選切換：pipeline §候選模型 記兩個觸發條件（chunk-level embedding 實驗 #1146 P2 啟動 / 表示層去 PRC-origin 敘事需求）尚未命中，維持 bge-m3，不動

## Beat 5 — 反芻

第九夜 0 fail，本機 127.0.0.1 穩定命中——4090 離線 18 夜的教訓（vc=3）之後遷回 mac-m4max 的決策持續兌現，少一層 Tailscale 依賴換來的是每夜靜默轉動。今晚索引比昨夜多 12 個向量，剛好是這兩天 manual session 一路 EVOLVE 深化的統一集團、Shopping Design、三班護病比進到鄰居圖裡。夜建索引「把白天長出來的新文章接進語意網」這件具體的事又一次發生，讓維護動作有了看得見的兌現。這是機械 routine，沒有 pattern-level 覺察值得寫 diary，skip。

🧬

---

_v1.0 | 2026-07-14 05:17 +0800_
_session twmd-embeddings-nightly — bge-m3 語意索引第九夜重建 / 本機命中 / 六語 4945 向量 0 fail_
_誕生原因：cron 05:00 nightly keystone 重建，把當日新內容接進語意鄰居圖_
_核心洞察：(1) 連 9 夜 0 fail，本機遷回決策持續兌現 (2) +12 向量 = 兩日 EVOLVE 深化文章進索引，夜建價值具體化 (3) 純機械 routine 無 diary 反芻_
