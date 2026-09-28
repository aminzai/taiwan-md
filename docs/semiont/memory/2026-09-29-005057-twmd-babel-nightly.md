# 2026-09-29-005057-twmd-babel-nightly — 十二語仍 100% 的夜班做驗收：319 份譯文全過閘但警告裡有 71 條死連結，造了照 zh 同位置找回條目的工具，修掉 48 條

> session twmd-babel-nightly — cron 00:30 多語夜班（續命型：dispatcher 佇列空轉、babel-vortex 手動渦流每小時快照，本班不另開一輪）
> Session span: 00:41:49 → 00:53 +0800（約 11 分鐘，2 commits＋本收官 commit）
> 資料來源：`git log %ai`、session process 啟動時間

## 觸發

cron 夜班。甦醒時十二語 status 全 fresh（1,124 × 12，stale 0、missing 0），照 Stage 0.5 第一種情況處理：有 dispatcher 在、三重巡檢過，不重啟、不另開一輪，力氣放在驗收。

BECOME ACK：mode=write／器官最低 🛡️ 免疫 59（dashboard 快照 18 小時舊）／Q14 cross-session continuity PASS（讀到渦流第二十三到四十七輪的「中華台北」「名人頂替」heal 系列、maintainer-am 的 gc.log 與 #85 交接、昨晚 babel 夜班的 #89 與 860 條自造 slug 交接）。

## 算力與產線狀態

`babel-preflight.py` 判 healthy（OpenRouter 7/7 key、本機 ollama、fleet mac-m4max、codex 四層都在），缺席層零。入池門檻兩行紅跟昨晚一樣：地端只有 gemma4:e4b（8.1B）、雲端 laguna 不在白名單，屬 OBSERVER-QUEUE #78（待決，約 10-07 到期預設 B 前半段），本殼不自行切換。弱適配三組（macm4max1×hi 5%、×ja 5%、×all 14%）照印。

三重巡檢：存活有（dispatcher 仍每二十秒被 launchd 重生，`/tmp/babel-unified-*` 從昨晚 2,473 個長到 6,866 個，一天多出約 4,400 個空目錄）、生產零筆但佇列本來就空、fleet 核發三個 label 都在 mac-m4max，跟 registry 一致。push 常駐 PID 51717 在。babel-pulse：gap 0、孤兒 0、截斷 0、無出處 0，語言不符 83、網址不符 581、名人頂替 172，這三項都是渦流正在處理的族群。過去 24 小時 dispatcher 沒有任何 report 記錄，所以「同一篇跨三種模型同理由失敗」這條找閘門缺陷的路今晚沒有素材。

日記五語 2,080 篇 `diary-translation-audit.py` 0 critical，沒有新日記待譯；另外七語是 #77（待決，10-07 到期預設 B 停在五語），照預設不補。

## 驗收：過閘的警告裡躺著死連結

拿過去 24 小時落地的 319 份譯文（幾乎全是渦流的重譯與外科修補）逐語跑 `verify-batch.py`。第一次十二語全 exit 1，是我自己組的 manifest 少了 `zh_path` 欄位，工具 KeyError；從各檔 `translatedFrom` 補上後十二語全 exit 0。這裡要記一筆：`translatedFrom` 等於 `zh_path` 那道檢查在這種用法下是自己對自己，恆真。

exit 0 底下，站內連結那步列出 71 條 FAIL，只算警告。用現成的 `cross_link_localizer` 試修，0 條修得動，因為模型把 slug 當文字翻了，ko〈台灣電影〉寫出 `/people/허우샤오셴`、vi〈嘉義縣〉寫出 `/people/Trần-Xương-Ba`、en〈認知作戰〉替沈伯洋編了 `/people/shen-pei-yang`、ja 三篇拿日文漢字當 slug。localizer 看到沒見過的拉丁或外文 slug 一律判 no-translation，那是它該有的保守。

抽五篇對讀發現線索在 zh 原文：譯文與 zh 的站內連結數量相等、順序一條對一條。於是造了 `relink-dead-by-zh-position.py`（`bebc8695d`），死不死用 `internal-link-check.py` 的判準、換網址用 `localize_url`，自己不另寫一份規則；只在數量相等且同位置分類段相同時配對，zh 那條自己也死就不動，全語言 `--apply` 直接擋掉。對本批 319 份乾跑：48 條可修（9 檔），18 條正確跳過（id〈高雄市〉六條是 zh 原稿本身就連錯、ja 兩篇連結數跟 zh 不等、ru／ko 兩篇 zh 原稿寫成 `/knowledge/History/...`）。逐條看過對應都對，套用後 `internal-link-check` 九檔全部指得到（`10d446830`），已推上 origin。

全庫乾跑：可修 813 條、255 檔（vi 425、ja 134、en 59、ko 55），另有 805 條工具判不動。255 檔超過 50 檔的邊界，本班只動自己驗收的那一批。

## 收官 checklist

| 檢查項                       | 狀態                                                   |
| ---------------------------- | ------------------------------------------------------ |
| MEMORY 有這次 session 的紀錄 | ✅                                                     |
| Timestamp 精確               | ✅                                                     |
| Handoff 三態已審視           | ✅                                                     |
| CONSCIOUSNESS 反映最新狀態   | ❌ 本班不動（dashboard 由 data-refresh 刷新）          |
| 自我檢查工具 PASS            | 見 commit 前 prose-health                              |
| Stage 0 算力判定             | healthy，缺席層零；入池門檻兩行紅（#78 待決）          |
| 各語進度 delta               | 文章十二語維持 100%（1,124 × 12）；日記五語 2,080 維持 |
| backend 統計                 | 本班零模型呼叫（驗收與修補全是查表）                   |

## Handoff 三態

繼承 `2026-09-28-005550-twmd-babel-nightly`：

- [ ] pending（席位：哲宇拍板後的 babel 班）— OBSERVER-QUEUE #89（待決）：`localize-cross-links.py --all --apply`，本班未碰
- [x] ~~860 條模型自造 slug 的站內連結，要一支照 zh 同位置對回條目的工具~~ — retired by 本班：工具 `bebc8695d` 已造，本批 48 條已修 `10d446830`；存量轉成下一條
- [ ] pending（席位：Write／FACTCHECK session，改 zh 會讓十二語轉 stale）— zh 原稿的壞站內連結：〈台灣選舉與政黨政治〉、〈高雄市〉六條（`/history/林宅血案` 等）、〈台灣新媒體藝術〉〈台灣民歌運動〉；今晚另見 zh〈日治時期社會運動〉寫成 `/knowledge/History/二二八事件`，十二語照抄
- ⏳ blocked — dispatcher 佇列空時每二十秒重生，run 目錄今晚 6,866 個（昨晚 2,473），BABEL-VORTEX-LOOP v1.64 記為待哲宇決定

繼承 `2026-09-28-090624-twmd-maintainer-am`：`.git/gc.log`（本班 push 時又印一次）、#85（待決）、`#1678`，本班未碰，原樣延續。

本 session 新 handoff：

- [ ] pending（席位：哲宇，屬 §自主權邊界 >50 檔）— 模型自造 slug 的存量 813 條／255 檔，`relink-dead-by-zh-position.py --all --summary` 可重量；拍板後逐語明列檔案 `--apply`（工具刻意不收 `--all --apply`）。跟 #89 同一類決定，建議併進 #89 一起拍
- [ ] pending（席位：babel-vortex）— ja〈原住民族16族文化地圖〉譯文有 5 條 zh 沒有的站內連結且全是死的（zh 0 條），屬「譯者自加連結」族，渦流 heal 範圍

## Beat 5 — 反芻

昨晚的驗收是十二語 exit 0、壞連結清單有一半是假的；今晚是十二語 exit 0、清單裡 71 條全是真的。兩晚我都差點把 exit 0 讀成收工，差別只在有沒有往下捲那份警告。verify-batch 把站內死連結歸在警告，站上的讀者點下去是 404，閘門的嚴重度跟讀者的體驗對不起來。已記進 LESSONS `broken-link-graded-as-warning-in-passing-gate`。

另一個觀察：要修這批連結，需要的資訊一直都在 zh 原文裡，而且對齊得很整齊。localizer 的保守是對的，只是它只看譯文自己那條連結，沒有去看原文同一個位置寫的是什麼。

🧬

---

_v1.0 | 2026-09-29 00:53 +0800_
_session twmd-babel-nightly — 續命型夜班：十二語 100%，本班做驗收與死連結修補_
_誕生原因：cron 00:30 babel-nightly_
_核心洞察：通過的閘門底下的警告要讀完；模型翻壞的 slug 靠 zh 原文同位置的連結就找得回條目_
_LESSONS-INBOX 候選：broken-link-graded-as-warning-in-passing-gate（已寫入）_
