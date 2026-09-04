# 2026-09-05-053657-twmd-embeddings-nightly — 12 語 bge-m3 全量重建，9,906 向量 0 fail，僅 zh-TW 鄰居變動

> session twmd-embeddings-nightly — cron 夜間心跳（05:00 排程）
> Session span: 05:23:00 → 05:37:00 +0800 (~14 min, 1 commit)
> 資料來源：`git log %ai`

## 觸發

`0 5 * * *` cron 排程觸發 `twmd-embeddings-nightly`：每夜用 bge-m3 重建全站語意索引，餵讀者端「你可能也想讀」與 AI 端 RAG 向量。

## Rebuild + verify

端點解析走 EMBEDDING-PIPELINE §前置本機優先規則：`curl http://127.0.0.1:11434/api/tags` 直接命中 bge-m3，不必 fallback 到 fleet registry。Stage 0 preflight 對「台灣」跑 embedding 拿到 `dim 1024`，PASS。Stage 1 `node scripts/core/build-embeddings.mjs --langs all` 對 12 語（zh-TW/en/ja/ko/es/fr/vi/id/pt/hi/ar/ru）跑完，共 9,906 篇向量、0 fail，耗時 99-186 秒不等（zh-TW 最久因 1,109 篇最多）。Stage 2 verify 逐語言對照 `ENABLED_LANGUAGE_CODES` canonical 清單，12 語全數 ≥400 篇且 100% 有 8 鄰居，manifest model 確認 `bge-m3:latest`，exit 0。

`git diff --stat src/data/related/` 只顯示 `zh-TW.json` 1 行變動，其餘 11 語內容與昨夜逐位元組相同——語言組合逐夜輪替是這條 routine 的正常樣子，不是異常訊號（同 2026-09-02/09-04 memory row 的既有判讀）。

## Commit + push

Stage 3 依 pipeline 規則先 `NOW=$(date ...)` 落變數並印出確認再代入 commit message，避免手抄時間戳出錯（`retyping-shell-substitution-loses-the-substitution` 教訓）。`d4db0bce9` 只 stage `src/data/related/`，`git ls-files` 立即驗證進 commit，`--no-verify` 繞開 husky（pipeline 允許），push 前 pre-push hook（article-health / UI 語言閘門 / 模板層語言閘門）全綠，`d4db0bce9` 推上 `origin/main`。

## 收官 checklist

| 檢查項                       | 狀態 |
| ----------------------------- | ---- |
| MEMORY 有這次 session 的紀錄 | ✅   |
| Timestamp 精確               | ✅   |
| Handoff 三態已審視           | ✅   |
| CONSCIOUSNESS 反映最新狀態   | ✅   |
| 自我檢查工具 PASS            | ✅   |

## Handoff 三態

繼承上一 session（`2026-09-04-084247-twmd-maintainer-am`）：本 routine scope 內無可行動項，其餘 pending / blocked 項（OBSERVER-QUEUE #33/#36、main 紅燈出口、`--header-h` 硬編碼、D+14/D+30 milestone 追蹤等）維持不動，留給對應 routine 接手。

本 session 新 handoff：無新增。

## Beat 5 — 反芻

這是一條純機械 routine：端點解析、rebuild、verify、commit 全部有明確的 pass/fail 判準，沒有創作判斷需要做。今夜唯一值得記的是「只有 zh-TW 動、其餘 11 語不動」這個形狀本身在連續多夜出現後已經不構成訊號——這正是 pipeline 設計要達成的穩態：staleness 上限每天重新框回一天，語言組合輪替只反映哪些文章昨天被新寫或改寫。

🧬

---

_v1.0 | 2026-09-05 05:37 +0800_
_session twmd-embeddings-nightly — cron 夜間心跳_
_誕生原因：`0 5 * * *` 排程觸發，EMBEDDING-PIPELINE Stage 4 收官要求_
_核心洞察：12 語全綠 0 fail 是這條 routine 的穩態，本機端點直連免 fallback 第 N 次確認主節點健康_
