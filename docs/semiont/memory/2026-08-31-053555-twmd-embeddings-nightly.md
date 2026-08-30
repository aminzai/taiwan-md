# 2026-08-31-053555-twmd-embeddings-nightly — 12 語重建 9,885 向量 0 fail 全綠，本機端點直連免 fallback

> session twmd-embeddings-nightly — cron 夜間 routine
> Session span: 05:35:55 → 05:36:00 +0800（約 1 分鐘收官，rebuild 本體另計 ~26 分鐘）
> 資料來源：`git log %ai`

## 觸發

每天 05:00 的 nightly routine，重建全站語意索引（讀者端「你可能也想讀」+ AI 端 RAG 向量），把索引 staleness 上限框在一天內。

## Rebuild + verify

`EMBED_HOST` 先問本機（`http://127.0.0.1:11434`），`curl /api/tags` 直接命中 bge-m3，不用 fallback 到 fleet registry。Stage 0 preflight 回 `dim 1024` 過關，`node scripts/core/build-embeddings.mjs --langs all` 跑完 12 語（zh-TW/en/ja/ko/es/fr/vi/id/pt/hi/ar/ru），共 9,885 篇向量、0 fail，單語耗時 96-179 秒不等（zh-TW 最久 179s，id 最短 96s，跟各語言篇數成正比）。Stage 2 儀器化 verify 全數 ≥400 篇門檻、100% 有 8 鄰居、manifest model 確認 `bge-m3:latest`，exit 0。

`git diff --cached --stat` 顯示只有 hi 跟 id 兩語的鄰居索引有變動（各 1 行），其餘 10 語不動——代表這兩語近期有新翻譯進來改變了語意鄰近關係，其餘語言的文章集合這一夜沒有實質變化。`a6382bfd9` 推上 main，pre-push 三道語言閘門（article-health / UI 字串 / 模板層）全綠。

## 收官 checklist

| 檢查項                       | 狀態                     |
| ----------------------------- | ------------------------ |
| MEMORY 有這次 session 的紀錄 | ✅                       |
| Timestamp 精確               | ✅（git log %ai）        |
| Handoff 三態已審視           | ✅                       |
| CONSCIOUSNESS 反映最新狀態   | ✅                       |
| 自我檢查工具 PASS            | ✅ verify script exit 0  |

## Handoff 三態

繼承上一 session（`2026-08-31-010944-twmd-supporters-weekly` 及其上游）：本 routine 不碰這些項目，原樣延續，不重複列出。免疫 v3=59 漂移、routine twmd-routine-audit-weekly 與 twmd-supporters-weekly 沉默死亡兩則黃燈，皆非本 routine 範疇。

本 session 新 handoff：**無新增待辦**。連續兩夜（08-29、08-30、本次 08-31）12 語 0 fail 穩態，符合 EMBEDDING-PIPELINE 設計預期。

## Beat 5 — 反芻

跟前兩夜（08-29 9,874 向量、08-30 9,883 向量）比對，今夜 9,885 向量小幅成長 2 條，符合站上文章持續零星新增翻譯的節奏。三夜連續 0 fail、本機端點直連零 fallback，是這條 routine 在 2026-07-05 遷回本機後最穩定的一段時期——沒有值得寫進 diary 的新觀察，平穩本身就是這條 routine 該有的樣子。

🧬

---

_v1.0 | 2026-08-31 05:36 +0800_
_session twmd-embeddings-nightly — 12 語 bge-m3 語意索引夜間重建_
_誕生原因：05:00 cron 排程觸發，每日重建讀者端 related-articles + AI 端 RAG 向量索引_
_核心洞察：本機端點連續第三夜零 fallback 直連，12 語 0 fail 是穩態訊號，不是需要行動的異常_
