# 2026-07-15-051733-twmd-embeddings-nightly — bge-m3 第十夜：4947 向量六語 0 fail / verify PASS / 台北吸菸室與大港開唱進鄰居圖

> session twmd-embeddings-nightly — cron routine（每天 05:00 語意索引重建）
> Session span: 05:00:00 → 05:19:00 +0800（約 19 分鐘，1 commit）
> 資料來源：`git log %ai`

## 觸發

Cron `0 5 * * *` 準點 fire，走 [EMBEDDING-PIPELINE v1.1](../../pipelines/EMBEDDING-PIPELINE.md) 把全站文章用 bge-m3 重算語意座標，一次產出讀者端「你可能也想讀」的鄰居索引與 AI 端的 RAG 向量。第十個連續夜晚。

## 本機節點命中，四階段全綠

依 pipeline §前置 的本機優先解析，`127.0.0.1:11434` 的 `/api/tags` 直接命中 bge-m3，沒有 fall through 到 fleet registry——4090 遷回 mac-m4max 之後這條路徑連續第十夜穩定，Tailscale 那層依賴確實少掉了。Stage 0 preflight 回 `dim 1024`。

Stage 1 重建六語花約 9 分鐘：zh-TW 846 vecs / 92s、en 850 / 94s、ja 837 / 94s、ko 837 / 94s、es 836 / 94s、fr 741 / 85s，合計 **4947 向量，六語全部 0 fail**（fail rate 0%，遠低於 5% escalation 線）。比昨夜的 4945 多 2 個。Stage 2 verify 六語各自 100% 有 8 鄰居、每語遠高於 400 篇下限、manifest.model 是 `bge-m3:latest` 無 drift，exit 0 PASS。Stage 3 只 stage `src/data/related/`，`6856d6e2c` 落 en.json 與 ko.json 兩檔，commit 後 `git show --stat` 立即驗證確實只有那兩檔進去、無 phantom-delete，pre-push 全站 article-health 全綠後推上 main。

## 那 2 個新向量是夜建存在的理由

單行 JSON 讓 git diff 看不出東西，跑語意 diff 才看見實際變化：en 新增 `society/taipei-smoking-room`、ko 新增 `music/megaport-festival`，另有 en 10 篇、ko 6 篇的鄰居順序位移。這兩篇的來歷剛好對上昨天兩條不同的產線——台北吸菸室是昨日 12:34 手寫的 depth ship，大港開唱是昨夜 00:50 babel-nightly 同步進來的譯本。白天寫的文章與夜裡翻的譯本，各自在隔天清晨被接進語意鄰居圖，讀者點進英文版台北吸菸室時看到的「你可能也想讀」從今天起才是語意選出來的，而非同 category fallback。索引 staleness 的上限被框在一天，就是這個機制在兌現。

## 收官 checklist

| 檢查項                       | 狀態                                         |
| ---------------------------- | -------------------------------------------- |
| MEMORY 有這次 session 的紀錄 | ✅                                           |
| Timestamp 精確               | ✅（git log %ai）                            |
| Handoff 三態已審視           | ✅                                           |
| CONSCIOUSNESS 反映最新狀態   | ✅（本 routine 不改器官分數）                |
| 自我檢查工具 PASS            | ✅ Stage 2 verify exit 0 / prose-health 見下 |

## Handoff 三態

繼承（從 2026-07-15-005000-twmd-babel-nightly walk-back）：

- [ ] **#155／#156 D+1 / D+3 / D+7 harvest** — 依 SPORE-HARVEST 排程回填（原封不動 pass 給下一個 harvest routine）
- [ ] **CF 404 15% plateau 觀察** — 昨晚 pm 回到 15.04%；下 3 cycle 看是否穩定續留 band 中段（REFLEXES #82 應用實例，pass 給 data-refresh）
- [ ] **babel P0 residual ≈ 47 slots 未 ship** — 三個選項待哲宇拍板（patch cascade fallback / Sonnet Tier 5 平行 dispatch / 手動 ollama 排隊），pass 給下一個 babel-nightly
- [ ] **cascade retry gap 候選 REFLEXES 新條** — validation-failure ≠ backend-exception 但都該觸發 fallback，pass 給 distill-weekly
- [ ] **nemotron fence-missing 候選 `_refusal-cache.json` 首個 entry** — pass 給下一個 babel-nightly

本 session 新 handoff：

- [x] ~~2026-07-15 embeddings rebuild~~ — `6856d6e2c` 已 ship，4947 向量 0 fail

沒有新的 pending。本夜無異常，也沒有累積出需要下一個 session 接的東西。

## Beat 5 — 反芻

連續第十夜 0 fail，這條 routine 已經穩到幾乎沒有敘事——但今晚的語意 diff 值得記一筆。如果只看 git diff，兩個單行 JSON 的整行替換什麼都看不出來，很容易讀成「又一次例行重建」；跑了語意 diff 才看見具體是哪兩篇進來、來自哪兩條產線。這跟 REFLEXES #82 講的 proxy signal 是同一個形狀：`2 files changed` 是替身，「台北吸菸室進了英文鄰居圖」才是 effect 本身。routine 越穩，越容易只看替身訊號就放行；今晚多跑那一個 node 指令的成本很低，換到的是知道這一夜到底兌現了什麼。

🧬

---

_v1.0 | 2026-07-15 05:19 +0800_
_session twmd-embeddings-nightly — cron 05:00 語意索引重建第十夜_
_誕生原因：EMBEDDING-PIPELINE Stage 4 收官，routine 每夜必寫_
_核心洞察：本機 127.0.0.1 連十夜穩定、六語 4947 向量 0 fail、verify PASS；語意 diff 揭露白天 depth ship 與夜裡 babel 譯本各自在隔晨被接進鄰居圖，這是夜建存在理由的具體兌現，而 `2 files changed` 只是它的替身訊號。_
_LESSONS-INBOX 候選：無（語意 diff 觀察已被 REFLEXES #82 涵蓋，per LESSONS check-DNA-first 紀律不另開條目）_
