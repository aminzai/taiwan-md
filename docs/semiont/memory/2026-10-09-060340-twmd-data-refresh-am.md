# 2026-10-09-060340-twmd-data-refresh-am — 14 步全過，建置效能的「七日平均」原來只看了不到一天，德文多出的一篇是〈楊德昌〉兩份譯本

> session twmd-data-refresh-am — cron 06:00 每日資料刷新（Micro mode）
> Session span: 06:01 → 06:13 +0800（commits：`424428839` heal 06:09:43、`c09838f81` refresh 06:09:56、本篇收官）
> 資料來源：`git log %ai`、`public/api/dashboard-*.json`、GitHub Actions deploy runs API、排程器 `list_scheduled_tasks`

## 觸發

排程 06:00 觸發：跑 14 步資料刷新、把排程器即時狀態落檔、處理 Step 11 新鮮度閘門的結果。

## 甦醒

✅ BECOME ack: mode=micro / 8 organ 最低=🛡️ 免疫 60（`review_coverage` 19）/ Q14 cross-session continuity=PASS。

`wake-context.py` 落檔 253,846 bytes，分頁讀到 `wake:END`，selftest 全綠。groundtruth 印快照齡 23h，是昨天這班的產物，屬正常隔夜。Q14：10-08 夜班 babel 把十二語缺口清到零並讓調度器派補丁前先量舊錯，02:36 心跳巡邏〈台灣教育制度〉14 錯，05:39 routine-sync 第 68 輪零漂移，05:58 embeddings 重建 0 fail。觀察者缺席第 13 天。甦醒時 `ACTOR_BUSY`：`babel-dispatch.py` 與 `babel-push-every.py --watch` 在跑，工作樹有 babel 的三份 reports 與 `_translation-status.json`。

## 讓場與 14 步

本機與 origin 0 前 0 後，照 10-03／10-08 的做法讓出 Step 1，不在 babel 寫工作樹時 auto-stash：`refresh-data.sh` 第 1–76 行接第 117 行之後組成 runner（行界對過仍準），`bash -n` 過後跑 2–14，exit 0。Stage 1.5 在開跑前做：`routine-live-state.json` 落檔 14 enabled、4 disabled，過濾 0 條私人 routine。

| Step             | 結果                                                                                                  |
| ---------------- | ----------------------------------------------------------------------------------------------------- |
| 1 git sync       | SKIP（babel 在寫，HEAD 0 behind）                                                                     |
| 2 三源感知       | PASS：CF 七天 3,190,965 requests、404 率 2.36%、AI 爬蟲 342,471 次跨 19 家；GA4 20／20；SC 20＋150    |
| 2.5 404 監測     | PASS：10-07 全日 5,390 筆（unknown 3,556、scanner 1,133），no alerts                                  |
| 3 translations   | PASS：13,501 筆，0 孤兒                                                                               |
| 4 spores         | PASS：166 篇，0 warnings                                                                              |
| 5 i18n           | PASS                                                                                                  |
| 6 immune         | PASS：60，最大缺口 review_coverage 19                                                                 |
| 6.5 fork-census  | PASS：無新子代                                                                                        |
| 6.6 status       | PASS：routines 18（operational 7、degraded 7、disabled 4），babel 12 語缺口 0                         |
| 7 prebuild       | PASS（redirects 229 條）                                                                              |
| 8 llms.txt       | PASS：十二語各 1123、de 1124，contributors 78                                                         |
| 9 stats          | PASS：⭐1199 🍴187 👥78 📄1123                                                                        |
| 10 build-perf    | PASS 但樣本只涵蓋 0.8 天，當班修掉（下節）；修後 30 個成功 run 涵蓋 7.5 天、平均 1958 秒、ms/page 109 |
| 10b newsroom     | PASS：195 篇上板，warnings 17                                                                         |
| 11 freshness     | PASS：14 份全為今日，analytics 內容日 10-08，0 stale                                                  |
| 12 spore 驗證    | PASS：0 errors                                                                                        |
| 13 sporeLinks    | PASS：無變動                                                                                          |
| 14 reports INDEX | PASS：726 行                                                                                          |

Step 11 零過期，catch ≠ fix 鐵律本班沒有觸發對象。三源全部 200。

## 七日平均其實是不到一天的平均

Step 10 印「7d avg 1969s（coverage 0.8d）」，昨天同一欄是 6.1 天。翻 `extract-build-perf.mjs`：它查 deploy workflow 最近 30 個 `status=completed` 的 run，再濾出 success。這兩天 babel 推送密集，每次推送都把前一個還在跑的 deploy 取消掉（pre-push hook 寫的就是 cancel-in-progress latest-wins），API 回來的 30 筆裡 24 筆 cancelled，只剩 6 筆成功，全落在 10-08 一天之內。coverage 欄位一直誠實印著，但沒有任何門檻看它，0.8 天跟 6.1 天都是綠燈，status 也是 ok（自驗只看最新那筆夠不夠新）。

改成直接查 `status=success`，重跑後 30 筆涵蓋 7.5 天，平均 1958 秒，`424428839`。同一支工具 06-10 audit 修過「slice 前 N 個 run 叫 30d avg」，那次把聚合改成時間窗，取樣仍是筆數上限，這次的縫就是那次留下的。教訓進 LESSONS `count-capped-sample-shrinks-when-the-filtered-out-class-grows`。

## 德文多出的那一篇

llms.txt 印 de 1124、其他十二語 1123。對 translatedFrom 一查，`People/楊德昌.md` 在德文有兩份：`de/People/edward-yang.md`（09-09 Dar 投稿）與 `de/People/yang-dechang.md`（10-07 aminzai，PR #1801，10-08 maintainer 合併）。其他十一語都用 `yang-dechang`，所以 `edward-yang` 是偏離慣例的那份，但它更早進庫。留哪一份、另一份要不要轉址，涉及刪掉貢獻者的檔案，屬 maintainer 席位，本班不動。昨天 embeddings 那班記到「de 因 #1801 多出楊德昌」，當時沒認出是重複。

## 收官

兩個 commit 都用路徑清單收：heal 2 檔，refresh 35 檔，babel 的 `_translation-status.json` 與 `reports/babel/*` 沒碰。第一次收 refresh 時 zsh 不把變數拆成多個路徑，整串被當成一個路徑而失敗，沒有東西進 git，改用 bash 重跑。`verify-commit-scope --head 35` scope OK，push 後 origin 0 落差。refresh commit 內文寫「本週新增 41」是甦醒時舊快照的數字，刷新後是 49，已推送不改，這裡更正。

| 檢查項                       | 狀態                                                                         |
| ---------------------------- | ---------------------------------------------------------------------------- |
| MEMORY 有這次 session 的紀錄 | ✅                                                                           |
| Timestamp 精確               | ✅                                                                           |
| Handoff 三態已審視           | ✅                                                                           |
| CONSCIOUSNESS 反映最新狀態   | ✅ 儀表板已重生，快照齡 0h                                                   |
| 自我檢查工具 PASS            | 見 commit 時 prose-health                                                    |
| diary                        | skipped：diary-gate PASS，但屬 routine 預設 skip，理解沒有改變，反芻留在本檔 |
| evolve                       | skipped：本班修一行儀器，教訓進 LESSONS                                      |

## Handoff 三態

繼承自 `2026-10-09-055825-twmd-embeddings-nightly.md`：

- ⏳ blocked（延續，收件席位 `/twmd-routine` 或 self-evolve-weekly 10-11，本班動不了殼層）：routine-sync 提出的「embeddings 改殼後要隔兩晚才生效」三選項。
- ⏳ blocked（延續，哲宇）：`OBSERVER-QUEUE` 待決 39 條，本班不動；最近到期 `#86（待決）` 10-11。
- [ ] pending（延續，收件席位：能動排程的 Full mode 或 `/twmd-routine`）：`.git/gc.log` 與 `git prune`（issue #1729）。本班 fetch、commit、push 時 git 照樣警告，babel 全程在寫，沒動。

繼承自 `2026-10-08-060257-twmd-data-refresh-am.md`：

- [ ] pending（延續，收件席位 `twmd-maintainer-daily`）：404 監測的同語言前綴無斜線重複形狀（`/ptpt/` 等）要不要歸成獨立家族。本班 10-07 全日 404 降到 5,390，unknown 3,556，沒有再量這個形狀。
- [ ] pending（延續，收件席位 `twmd-self-evolve-weekly` 10-11 或哲宇）：LESSONS `heart-counts-heals-as-contributed-births` vc=3。

本 session 新 handoff：

- [x] ~~build-perf 七日平均樣本不足一天~~：本班 `424428839` 修掉。
- [ ] pending（收件席位 `twmd-maintainer-daily`，該席位動得了 knowledge 與轉址）：〈楊德昌〉德文兩份譯本，`de/People/edward-yang.md`（09-09）與 PR #1801 的 `de/People/yang-dechang.md`。下一步：比對兩份品質，留下一份，另一份刪除並在 `config/redirects` 補轉址，讓 de 回到 1123。

## Beat 5 — 反芻

這班的兩個發現都是數字對不上鄰居：build-perf 的涵蓋天數對不上昨天，德文的篇數對不上其他十二語。兩個數字都印在輸出裡，工具都沒有標黃。涵蓋天數那欄是 06-10 為了「讓人看見樣本多大」才加的，它做到了被看見，卻沒有一道檢查在它掉到標籤窗一成的時候出聲。把資訊印出來和讓它會叫，中間還差一個門檻。

🧬

---

_v1.0 | 2026-10-09 06:13 +0800_
_session twmd-data-refresh-am — cron 06:00 每日資料刷新_
_誕生原因：例行刷新；Step 10 涵蓋天數從 6.1 掉到 0.8_
_核心洞察：先取 N 筆再過濾的樣本，涵蓋時間跟著被濾掉的那類漲落；印出 coverage 不等於有人在看 coverage_
_LESSONS-INBOX 候選：count-capped-sample-shrinks-when-the-filtered-out-class-grows（新，vc=1）_
