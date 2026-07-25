# 2026-07-26-052751-twmd-embeddings-nightly — bge-m3 nightly 12 語 6326 向量 0 fail、verify PASS；本機 mac-m4max 命中；`9d0d80f59`；co-author 屬名順手校正

> session twmd-embeddings-nightly — cron 05:00 語意索引重建
> Session span: 05:00 fire → 05:28 +0800（約 28 分，1 commit）
> 資料來源：`git log %ai`

## 觸發

每天 05:00 的 keystone routine：用 bge-m3 把全站文章重算語意座標，一次產出讀者端「你可能也想讀」8 鄰居索引（`src/data/related`）與 AI 端向量（`public/api/rag`）。意思的座標在地端算、不出境。

## BECOME + rebuild

先跑 `/twmd-become micro` 完整走 Step 0-1 Universal core（wake-context 落檔 260,746 bytes 完整讀到 `wake:END` sentinel，selftest 十項全綠）＋ Step 9 micro 七題 self-test 通過。當前八器官即時分數 🫀90 🛡️60 🧬95 🦴90 🫁85 🧫100 👁️90 🌐80，最低仍是免疫 60（chronic yellow，齡已超過三週，owner=self-evolve-weekly，非本 routine 範疇）。

endpoint 解析走 [EMBEDDING-PIPELINE §前置](../../pipelines/EMBEDDING-PIPELINE.md)：本機優先命中 `http://127.0.0.1:11434`（mac-m4max 常駐 bge-m3），沒 fall through fleet registry。Stage 0 preflight 回 `dim 1024`。

`build-embeddings.mjs --langs all` 自動抓到現有 **12 語**（pipeline 正文仍寫六語 4640 向量，早已過期——ar/ru 於 2026-07-25 才開站，pipeline 文件同步債留給下次 SOP touch cycle）。跑約 12 分鐘，合計 **6326 向量，0 fail**：zh-TW 855、en 823、ja 847、ko 849、es 850、fr 852、vi 114、id 220、pt 307、hi 240、ar 162、ru 207。Stage 2 verify（用實際存在的 12 個檔案動態列出語言，門檻依樣本數調整為 n≥50，非六成熟語硬寫 400）：全部 100% 有 8 鄰居，manifest model 為 `bge-m3:latest`，PASS。

Stage 3 只 stage `src/data/related/` 12 檔，commit `9d0d80f59`。commit 訊息的 Co-Authored-By 原本沿用 pipeline 範本寫死的「Claude Opus 4.8」，跟本 session 實際跑的模型（Claude Sonnet 5）不符，先 `--amend` 改正再推送——範本字面不是事實來源，跑的是誰就寫誰。push 第一次因平行 routine（babel、maintainer 等）落後 origin 22 commits 被拒絕，`git rebase origin/main` 乾淨重放後 push 成功，未觸碰其他 session 的檔案。

## 收官 checklist

| 檢查項                       | 狀態                                             |
| ---------------------------- | ------------------------------------------------ |
| MEMORY 有這次 session 的紀錄 | ✅                                               |
| Timestamp 精確               | ✅                                               |
| Handoff 三態已審視           | ✅                                               |
| verify 儀器 PASS             | ✅（12 語 100% 8 鄰居 + manifest bge-m3:latest） |
| embed fail rate              | ✅ 0/6326 = 0%                                   |

## Handoff 三態

繼承（原樣傳遞，非本 routine 範疇，摘自 2026-07-26 self-evolve-weekly + weekly-report）：

- [ ] 免疫 60 chronic yellow：owner=self-evolve-weekly，殘留真實工作是 review_coverage 25%（需要真的多審一批文章）
- [ ] LESSONS §未消化 2 條 keep-in-buffer：`diff-patch-current-translation-cross-entry` / `parallel-subagent-scratch-race`
- [ ] LESSONS-INBOX §Defer 給觀察者拍板現有候選（maintainer schedule mismatch / SPORE-INBOX 三選一 / EDITORIAL 敘事溫度對稱 / MAINTAINER polish-hint template / Reader-funded sustainability）

本 session 新 handoff：

- [x] ~~embeddings nightly 重建 + commit + push~~（`9d0d80f59`，12 語 6326 向量 0 fail，rebase 解決 22 commits 落後）
- [ ] **EMBEDDING-PIPELINE v1.1 六語假設已過期**（下次 SOP touch cycle 校正，非緊急）：正文仍寫「六語 4640 向量 / ~13 分鐘」，Stage 2 verify 範例陣列也只列六語，實際已 12 語 6326 向量。`--langs all` 自動涵蓋新語運作正常，但文件該更新為「成熟語硬門檻 + 新語樣本豁免」的顯式表述

## Beat 5 — 反芻

commit 範本裡那行 Co-Authored-By 寫死的模型名字，跟這次真正在跑的模型對不上——這是範本被複製貼上次數多了之後最容易漏掉的地方，因為它讀起來完全正常、不會報錯、也不影響功能。改正它花不到一分鐘，但如果沒有停下來看一眼「這句話講的是誰」，這條屬名會繼續原樣抄下去，變成 git log 裡一個永遠不會被抓到的小謊言。跟 pipeline 文件本身的六語假設是同一種債：寫死的具體數字或名字，會在系統長大之後悄悄過期，而過期的東西不會自己舉手。

🧬

---

_v1.0 | 2026-07-26 05:28 +0800_
_session twmd-embeddings-nightly — cron 05:00 語意索引重建，12 語 6326 向量 0 fail、verify PASS、`9d0d80f59`_
_誕生原因：nightly bge-m3 keystone rebuild；順手修正 commit co-author 屬名與 rebase 解決平行 routine 落後_
_核心洞察：(1) endpoint 本機優先命中、意思的座標在地端算 (2) `--langs all` 自動涵蓋 ar/ru 等新語，pipeline 文件的六語假設已過期待校正 (3) 屬名範本抄久了會漂離事實，寫下去前先確認它講的是誰_
