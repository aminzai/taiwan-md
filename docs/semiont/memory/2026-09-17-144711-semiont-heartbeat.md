# 2026-09-17-144711-semiont-heartbeat — npm prebuild 缺 typescript 卡了六個 dashboard 好幾天 / 尺二週排程缺口查到根因但不動手

> session semiont-heartbeat — scheduled Full mode heartbeat
> Session span: 14:37 → 14:52 +0800（約 15 分鐘，1 commit）
> 資料來源：`git log %ai`

## 觸發

scheduled task `semiont-heartbeat` 自動觸發，要求跑完整條 BECOME + HEARTBEAT.md 四拍半並收官。這次緊接在同日稍早 `113227-semiont-heartbeat` 之後（那個 session 才解掉本機 7 天分岔），所以本輪重點放在 Beat 1 診斷——上一輪收官時留了「tracker 檔案有沒有被下游 build 消化，尚未驗證」的 handoff。

## Beat 1：npm run prebuild 死在 typescript 找不到

跑 `refresh-data.sh` 到第 7 步 `npm run prebuild` 直接炸掉：`Cannot find package 'typescript'`。查 `package.json` 明明寫著 `typescript@^5.9.3`，但本機 `node_modules` 只有 312 個套件、typescript 整包不在裡面——是這台機器的 npm install 沒裝全，不是 git 裡的依賴宣告錯。`npm install typescript@^5.9.3 --no-save` 補回後重跑，14 步全過。

這個缺口造成的真實傷害：`dashboard-alerts/articles/forks/organism/translations/vitals` 六個 JSON 全部由 `npm run prebuild` 產生，這步一直在報錯，六個檔案就一直停在 09-09 的舊 mtime——`consciousness-snapshot.sh` 印出的「齡 200h」不是誇飾，是真的兩百小時沒更新過。上一輪心跳打撈的 8 篇孤兒完稿跟重刷的 tracker，這才真的被下游消化進 dashboard，不再是本機獨有的狀態。

## Beat 3：查 #1711 飛輪停轉，尺二那半沒動手

尺一（routine commit 齡）今天已經乾淨，多筆 commit 都在 5 小時內。尺二那 6 條週排程仍是黃燈，查了一下救援分支 `20260912-unpushed-routine-queue`：`news-lens-weekly` 跟 `weekly-report-sun` 那天的 memory 檔其實在分支上（真的有 fire，只是卡在分岔沒推出來），另外 4 條（distill / self-evolve / routine-audit / supporters）在分支上找不到對應檔案，比較像是真的沒 fire。那條分支本身還領先 main 686 個 commit，包含先前標記需要人判斷的 118 篇翻譯版本衝突（[OBSERVER-QUEUE #67](../OBSERVER-QUEUE.md)）——超出自主權邊界，沒有動，只在 issue 留言記錄查到的東西。

## 收官 checklist

| 檢查項                       | 狀態                                                          |
| ---------------------------- | ------------------------------------------------------------- |
| MEMORY 有這次 session 的紀錄 | ✅                                                            |
| Timestamp 精確               | ✅                                                            |
| Handoff 三態已審視           | ✅                                                            |
| CONSCIOUSNESS 反映最新狀態   | ✅ dashboard 已刷新（immune=58 漂移、4 個 yellow alert 仍在） |
| 自我檢查工具 PASS            | ✅ pre-push article-health / UI 語言閘門全綠                  |

## Handoff 三態

繼承 `2026-09-17-113227-semiont-heartbeat`：

- [x] 「8 篇打撈完稿與重刷 tracker 是否被下游 build 消化」——**本輪解除**：typescript 補回後 prebuild 跑通，六個 dashboard JSON 已是今天 mtime。
- [ ] pending（延續，給哲宇）— OBSERVER-QUEUE #67「babel 覆蓋投稿者譯文」政策決定，仍等拍板。
- [ ] pending（延續，給哲宇）— `reports/research/2026-08/比國家還大的演算藝術-media-staging/` 去留。

本 session 新 handoff：

- [ ] pending — 救援分支 `20260912-unpushed-routine-queue` 領先 main 686 個 commit（118 篇翻譯衝突 + 4 條週排程遺失的 memory 檔可能都在裡面），還沒人逐項比對過內容是否已被後續產線覆蓋掉。下一輪如果要處理，先確認這條分支現在還有哪些內容是 main 真的沒有的（`git log origin/main..origin/20260912-unpushed-routine-queue --oneline` 起手）。
- [ ] pending — distill / self-evolve / routine-audit / supporters 這 4 條週排程從 09-13 起沒有任何一輪 fire 的痕跡（救援分支上也沒有），跟 news-lens / weekly-report-sun 的「fire 了推不出去」不同型態，需要到 mouhouse 排程器本身查——這台機器的 MCP scheduled-tasks 只看得到 `semiont-heartbeat` 跟 `auto-backup` 兩條，看不到 twmd- 系列，沒辦法從這裡診斷。

## Beat 5 — 反芻

沒寫 diary。這次是既有反射（REFLEXES #38 混維度、#82 proxy signal）的又一次具體 instance——「npm prebuild 失敗」跟「dashboard 資料舊」中間隔了一層看不見的依賴，齡 200h 的 stale 警示本身沒有告訴任何人「為什麼」，只有真的去跑才會撞到那行 `ERR_MODULE_NOT_FOUND`。沒有新角度，記在這裡就夠。

🧬

---

_v1.0 | 2026-09-17 14:52 +0800_
_session semiont-heartbeat — 補 npm prebuild 依賴缺口 + 尺二週排程根因查證_
_誕生原因：scheduled heartbeat 例行觸發，接續上一輪心跳留的 build 驗證 handoff_
_核心洞察：dashboard「舊」跟「壞」是兩回事，這次是後者假裝成前者——真正壞掉的是本機環境缺一個套件，六個 JSON 的 stale mtime 只是症狀。_
