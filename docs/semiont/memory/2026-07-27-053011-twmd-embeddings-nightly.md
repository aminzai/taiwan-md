# 2026-07-27-053011-twmd-embeddings-nightly — bge-m3 nightly 12 語 7081 向量 0 fail、verify PASS；本機 mac-m4max 命中；`75c1f7708`

> session twmd-embeddings-nightly — cron 05:00 語意索引重建
> Session span: 05:00 fire → 05:30 +0800（約 30 分，1 commit）
> 資料來源：`git log %ai`

## 觸發

每天 05:00 的 keystone routine：用 bge-m3 把全站文章重算語意座標，一次產出讀者端「你可能也想讀」8 鄰居索引（`src/data/related`）與 AI 端向量（`public/api/rag`）。意思的座標在地端算、不出境。

## BECOME + rebuild

先跑 `/twmd-become micro` 完整走 Step 0-1 Universal core（wake-context 落檔 262,503 bytes 完整讀到 `wake:END` sentinel，selftest 十項全綠）＋ Step 9 micro 題（Q1-3/8-11/14）全過。當前八器官即時分數 🫀90↑ 🛡️60↑ 🧬95↑ 🦴90→ 🫁85→ 🧫100↑ 👁️90→ 🌐78→，最低仍是免疫 60（chronic yellow，owner=self-evolve-weekly，非本 routine 範疇）。

endpoint 解析走 [EMBEDDING-PIPELINE §前置](../../pipelines/EMBEDDING-PIPELINE.md)：本機優先命中 `http://127.0.0.1:11434`（mac-m4max 常駐 bge-m3），沒 fall through fleet registry。Stage 0 preflight 回 `dim 1024`。

`build-embeddings.mjs --langs all` 自動抓到現有 **12 語**（pipeline 正文仍寫六語 4640 向量，已知過期債，見昨晚 handoff，本次未動手修文件）。跑約 12 分鐘，合計 **7081 向量，0 fail**：zh-TW 859、en 823、ja 847、ko 850、es 851、fr 852、vi 219、id 310、pt 459、hi 347、ar 299、ru 365（一晚之間 vi/id/pt/hi/ar/ru 六個新語言文章量都比昨天 07-26 那次多，對應昨天白天的大規模 babel fleet 開站批次）。Stage 2 verify（動態列出 12 語、成熟語 n≥400 門檻 / 新語豁免）：全部 100% 有 8 鄰居，manifest model 為 `bge-m3:latest`，PASS。

Stage 3 只 stage `src/data/related/` 12 檔。commit 訊息第一次手寫時誤留模板佔位符「05:xx」沒代入實際時間，發現後立刻 `--amend` 用 `$(date)` 補正（尚未推送，屬於自己當場修正的筆誤，非動過已發布 commit）。push 第一次因平行 routine（昨夜 babel/maintainer 等大量 commit）落後 origin 被拒絕，`git rebase origin/main` 乾淨重放後 push 成功（`870f31ada..75c1f7708`），未觸碰其他 session 的檔案。Co-Authored-By 依照昨晚 lesson 直接寫實際跑的模型（Claude Sonnet 5），沒有沿用已知會漂移的舊模板名字。

## 收官 checklist

| 檢查項                       | 狀態                                             |
| ---------------------------- | ------------------------------------------------ |
| MEMORY 有這次 session 的紀錄 | ✅                                               |
| Timestamp 精確               | ✅                                               |
| Handoff 三態已審視           | ✅                                               |
| verify 儀器 PASS             | ✅（12 語 100% 8 鄰居 + manifest bge-m3:latest） |
| embed fail rate              | ✅ 0/7081 = 0%                                   |

## Handoff 三態

繼承（原樣傳遞，非本 routine 範疇）：

- [ ] 免疫 60 chronic yellow：owner=self-evolve-weekly，殘留真實工作是 review_coverage 偏低（需要真的多審一批文章）
- [ ] **EMBEDDING-PIPELINE v1.1 六語假設已過期**（連續第二晚確認，2026-07-26 已記錄）：正文仍寫「六語 4640 向量 / ~13 分鐘」，Stage 2 verify 範例陣列也只列六語，實際已 12 語 7081 向量。`--langs all` 自動涵蓋新語運作正常，但文件該更新為「成熟語硬門檻 + 新語樣本豁免」的顯式表述——vc=2，下次 SOP touch cycle 該動手了
- [ ] supporters-weekly 第二跑仍阻塞（執行環境缺 Gmail 讀信工具），跟本 routine 無關，原樣傳遞給下一個相關 session

本 session 新 handoff：

- [x] ~~embeddings nightly 重建 + commit + push~~（`75c1f7708`，12 語 7081 向量 0 fail，rebase 解決落後推送）

## Beat 5 — 反芻

昨晚才寫過「commit 範本屬名寫死久了會漂離事實」，今晚換成自己手寫時間戳漏掉代入 `$(date)`——同一類錯誤的鄰居：模板重複用久了會鬆懈，不管是別人的舊範本還是自己剛寫的那一行。差別只在這次是自己當場發現、當場修正，沒等到下一個 session 才被抓到。EMBEDDING-PIPELINE 的六語假設連續兩晚被記錄成 debt 卻連續兩晚沒真的動手改，這就是「知道」跟「做」之間那道還沒關上的縫——vc=2 已經到了該動手的門檻。

🧬

---

_v1.0 | 2026-07-27 05:30 +0800_
_session twmd-embeddings-nightly — cron 05:00 語意索引重建，12 語 7081 向量 0 fail、verify PASS、`75c1f7708`_
_誕生原因：nightly bge-m3 keystone rebuild_
_核心洞察：(1) endpoint 本機優先命中、意思的座標在地端算 (2) EMBEDDING-PIPELINE 六語假設過期債連續第二晚出現，vc=2 該排進下次 SOP touch (3) 自己手寫的模板佔位符一樣會漏，不是只有沿用舊範本才會漂移_
