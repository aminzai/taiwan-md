# 2026-07-18-052228-twmd-embeddings-nightly — bge-m3 nightly 4942 向量六語 0 fail／verify PASS；本機 127.0.0.1 命中；`b8c157d2f`；pre-push `set -e` 撞平行 session 未同步 `_translations.json` 靜默擋 push，走文件化逃生閘門

> session twmd-embeddings-nightly — cron 05:00 語意索引重建
> Session span: 05:00 fire → 05:23 +0800（約 23 分，1 commit）
> 資料來源：`git log %ai`

## 觸發

每天 05:00 的 keystone routine：用 bge-m3 把全站文章重算語意座標，一次產出讀者端「你可能也想讀」8 鄰居索引（`src/data/related`）與 AI 端向量（`public/api/rag`）。意思的座標在地端算、不出境。

## BECOME + rebuild

先跑 `/twmd-become micro` 完整走 Step 0-1 Universal core（wake-context 落檔 206KB 完整讀到 `wake:END` sentinel，selftest 十項全綠）＋ Step 9 micro 七題 self-test 通過。當前八器官即時分數 🫀90 🛡️60 🧬95 🦴90 🫁85 🧫100 👁️90 🌐93，最低仍是免疫 60（external_rulers 慢性痛）。

endpoint 解析走 [EMBEDDING-PIPELINE §前置](../../pipelines/EMBEDDING-PIPELINE.md)：本機優先命中 `http://127.0.0.1:11434`（mac-m4max 常駐 bge-m3，2026-07-05 遷回後 steady-state），沒 fall through fleet registry。Stage 0 preflight 回 `dim 1024`。Stage 1 `build-embeddings.mjs --langs all` 約 9 分鐘跑完六語：zh-TW 845／en 850／ja 837／ko 835／es 835／fr 740 = **4942 向量，0 fail**。Stage 2 儀器 verify PASS——六語都 100% 有 8 鄰居、manifest model 為 `bge-m3:latest`。Stage 3 只 stage `src/data/related/`（六檔各一行 minified JSON 有 diff），commit `b8c157d2f`；順帶把前一手 babel-nightly 未推的 `0934bb0ad`（00:38）一起 push 上 origin，收官後 origin/main 與 HEAD 對齊 0/0。

## pre-push `set -e` 撞未同步 `_translations.json`

push 第一次被 husky pre-push 擋（code 1），但奇怪的是：`sh .husky/pre-push` 直接跑 exit 0、`git push` 卻 exit 1。診斷後根因在 husky wrapper `.husky/_/h` 用 **`sh -e`（errexit）** 跑 hook，而我手動測試用的是無 `-e` 的 `sh`。orphan gate 那行 `tf_out="$(python3 sync-translations-json.py --check ...)"` 是命令替換賦值——`--check` 因 `_translations.json` 暫時 out-of-sync（平行寫手 session 留的 untracked `knowledge/{en,ja}/Culture/shopping-design.md` 兩檔還沒進 json，加上 4 檔 missing translatedFrom）而 exit 1，`set -e` 讓整個賦值語句非零就直接 abort，**根本走不到後面那道只認「Orphan translations」字串的 grep 判斷**（實際 orphans=0）。也就是說這道 gate 的設計意圖是「只有真 orphan 才擋」，但 `set -e` 把它變成「json 一有任何 out-of-sync 就擋」。

判定這不是真的 deploy 阻斷：全站 article-health `--all --profile=ci-deploy` 獨立跑過 exit 0（綠）、真 orphans 為 0、那兩個 untracked 檔不在我的 push 範圍內（CI fresh clone 不會有它們、json 在那邊是同步的、CI 會綠）。所以走 hook 自己文件化的逃生閘門 `TWMD_SKIP_PREPUSH_SWEEP=1 git push`（reflog 留痕、CI 仍把關），push 成功。沒去改 hook、也沒去跑 sync-translations 動別的 session 的 WIP——兩者都超出本 routine 範疇。

## 收官 checklist

| 檢查項                       | 狀態 |
| ---------------------------- | ---- |
| MEMORY 有這次 session 的紀錄 | ✅   |
| Timestamp 精確               | ✅   |
| Handoff 三態已審視           | ✅   |
| verify 儀器 PASS             | ✅（六語 100% 8 鄰居 + manifest bge-m3） |
| embed fail rate              | ✅ 0/4942 = 0% |

## Handoff 三態

繼承（原樣傳遞，非本 routine 範疇；來自 2026-07-17-231219-data-refresh-pm）：

- [ ] 並行 session WIP 續留 working tree：14 webp + 5 projection + 5 editorial-room + 5 research + 江振誠 article-evolve（v9 REWRITE 大批次中段，交寫手 session 判斷 ship）
- [ ] 下輪 am refresh 專項 diagnose 07-16 phantom 家族 80 條（CF 說 404 但站上路由存在，疑 CDN cache / hreflang 修後 edge 未 refresh）
- [ ] 哲宇拍板五件（2026 選舉 Tier 1.2/1.3、voice 歸屬、SPORE 周蕙、品質 batch Tier C1、opendata 5 條）
- [ ] 下個 write session 第一優先：洪醒夫深度重寫（P0）
- [ ] babel readingTime 病根 chip task_ad75163e／台灣鐵道史.en.md 孤兒檔 chip task_ea99c044
- [ ] 4 spore（#155-158）等 Chrome MCP pair／REFLEXES #70 三 option defer 哲宇
- [ ] 3 contributor PR reserved（#1225-1227）／CI pr-frontmatter-gate 中文檔名 false green

本 session 新 handoff：

- [x] ~~embeddings nightly 重建 + commit + push~~（`b8c157d2f`，六語 4942 向量 0 fail）
- [ ] **pre-push orphan gate `set -e` 脆弱性**（LESSONS-INBOX 候選，交 distill / 哲宇裁決）：`.husky/_/h` 用 `sh -e` 跑 hook，`.husky/pre-push` 的 `tf_out="$(sync-translations-json.py --check)"` 在 `_translations.json` 任何 out-of-sync 時（非只真 orphan）就 abort 全 hook，擋掉 scope 乾淨的 routine push。凡有平行寫手留 untracked 新譯檔就會復發。低風險修法：`|| true` 包命令替換、或把 orphan 判斷改成「先存 exit code 再只認 grep」。屬共用 correctness gate 改動（§自主權邊界），本 cron session 不逕自改，flag 給觀察者
- [ ] 上游 write session 收官時記得對 `shopping-design.md`（en+ja）跑 `sync-translations-json.py` 補進 `_translations.json`，否則後續每個 routine push 都要走逃生閘門

## Beat 5 — 反芻

今晚是純機械 rebuild，但撞出一個像樣的洞：一道 gate 的「意圖邏輯」（只擋真 orphan）跟它在真實執行環境（husky `sh -e`）下的「實際行為」（json 一髒就擋）分岔，而分岔點藏在一行命令替換賦值裡——直接跑 hook 看不到、只有在 git 真正調用的 `-e` 環境下才現形。這跟 §神經迴路 反覆講的「工具在說謊 / proxy signal」同科：hook 印出「✅ article-health 全綠」讓人以為過了，其實是下一行才靜默 abort，訊號跟結果對不上。診斷靠的是老實比對「我怎麼跑」vs「git 怎麼跑」的差異，而不是信任任一次表面輸出。修補我沒動手——共用閘門的改動該讓在場的人拍板，cron 在場的只有我自己。

🧬

---

_v1.0 | 2026-07-18 05:23 +0800_
_session twmd-embeddings-nightly — cron 05:00 語意索引重建，六語 4942 向量 0 fail、verify PASS、`b8c157d2f`_
_誕生原因：nightly bge-m3 keystone rebuild；push 時撞上 pre-push `set -e` × 平行 session 未同步 `_translations.json` 的靜默擋 push_
_核心洞察：(1) endpoint 本機優先命中、意思的座標在地端算 (2) gate 的意圖邏輯與 `sh -e` 下的實際行為分岔，藏在命令替換賦值裡，只有 git 真正調用才現形 (3) scope 乾淨 + article-health 獨立驗綠時，走 hook 文件化逃生閘門是對的，改 hook 留給觀察者_
_LESSONS-INBOX 候選：husky `sh -e` + 命令替換賦值一個 exit≠0 的腳本 = 全 hook abort，繞過原本只認 grep 的 gate 判斷邏輯（pre-push orphan gate 脆弱性，凡平行寫手留 untracked 新譯檔即復發）_
