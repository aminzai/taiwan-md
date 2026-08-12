# 2026-08-13-064309-twmd-spore-harvest-am — v1.15.0 release 孢子 D+2，第一則讀者回覆是策略疑慮不是事實勘誤

> session twmd-spore-harvest-am — daily 06:30 audience flywheel cron
> BECOME ack: mode=write, organs=🛡️60（免疫，最低分，黃燈 chronic 自 2026-07-05），Q14=PASS
> 資料來源：本次 session 直接執行紀錄

## 觸發

daily `twmd-spore-harvest-am` cron fire。dashboard `backfillWarnings` 只有 2 條在 D+1-D+7 主排程窗口內：v1.15.0「長出複眼」release 孢子 #170（Threads）與 #171（X），兩者皆 D+2，昨日已 harvest 過 D+1（0 讀者留言基準）。

## v1.15.0 release 孢子 D+2 harvest

Chrome MCP 連線正常，login-state probe navigate `@taiwandotmd` 確認登入態延續（完整選單 + 編輯個人檔案按鈕）。#170 Threads：1,264 次瀏覽 / 87 讚 / 4 轉發 / 0 外部回覆（較 D+1：758→1,264 / 43→87 / 2→4），主貼與續貼下方留言區皆空。#171 X 端仍未登入，改用公開頁面讀值，並對 4 個 icon 主動 zoom 截圖確認順序（回覆／轉發／讚／書籤）——延續 8/11 #168 教訓；Metrics：約 2 萬次瀏覽（未登入視角只回捨入級距）/ 323 讚 / 47 轉發 / 58 書籤 / 3 則回覆。

`read_page` a11y tree 顯示 X 端 3 則回覆中只有第 1 則可讀，其餘 2 則是永久 loading 的 placeholder（登入牆擋住）。可讀到的那則來自 @TaiwanAny：「會不會被敵人拿去利用? 侵害台灣國家利益」——這不是事實查核類留言，是對「公開講出十三道品質閘門曾誤殺自己合格譯文」這件事本身的策略疑慮，分類為 Bucket D（Critical-balance framing）。per Bucket D SOP 不自動回覆、不修文，寫進批次敘事檔的 Handoff 供哲宇 review。

用 `spore-db.py add-metrics` 寫入 D+2 事件（唯一數字入口），跑 `generate-spore-records.py` + `generate-dashboard-spores.py` 重生衍生層，`validate-spore-data.py` 六維度全綠。批次敘事寫進 `docs/factory/SPORE-HARVESTS/batch-2026-08-13-2-spores.md`。

**過程插曲**：Bash 工具第一次 `cd` 到共享 checkout 路徑執行 `spore-db.py add-metrics`，寫進了共享 checkout 的 `spore-metrics.json` 而不是本 worktree 的副本（git 指令會被 harness 擋下，但非 git 的 python 指令沒被擋，直到 Write 工具寫批次敘事檔時才被攔下並提示「Edit the worktree copy」）。發現後用 Python 手動把共享 checkout 的兩筆多餘事件移除、比對 diff 確認乾淨還原，再於 worktree 內重跑一次 `add-metrics`。教訓：worktree 隔離的邊界目前只覆蓋 git 操作與 Write/Edit 工具，Bash 對共享路徑的非 git 寫入不會被攔——之後任何寫入操作都要先確認 `pwd` 落在 worktree 內，不能只信任「應該會被擋下」。

## Pitfall 6 檢查

本輪未執行任何 reply 發布動作（Bucket D 留言 defer 哲宇，不自動回覆），無 ship attempt，Pitfall 6 duplicate-ship 風險不適用，retry 次數 = 0。

## 事實修復

無。本輪未發現 Bucket A/C 可查證事實錯誤。

## 收官 checklist

| 檢查項                       | 狀態                                                                      |
| ---------------------------- | ------------------------------------------------------------------------- |
| MEMORY 有這次 session 的紀錄 | ✅                                                                        |
| Timestamp 精確               | ✅                                                                        |
| Handoff 三態已審視           | ✅                                                                        |
| CONSCIOUSNESS 反映最新狀態   | ✅（未改動需 CONSCIOUSNESS 更新的狀態）                                   |
| 自我檢查工具 PASS            | ✅ validate-spore-data.py 六維度全綠                                      |
| Worktree 隔離確認乾淨        | ✅ 共享 checkout 誤寫已還原並 diff 驗證，本次 commit 只含 worktree 內變更 |

## Handoff 三態

繼承上一 session（`2026-08-13-061348-twmd-data-refresh-am`）：

- [ ] pending（給哲宇）— #1264 seo-meta 多語言門檻校準、#1184 justfont 後台網域白名單、免疫黃燈連續多日（自 2026-07-05）
- [ ] pending（vi 產線）— w5 剩約 90 篇、vi stale 27 篇、118 檔漢字黏著（>50 檔等哲宇）、Folk Music 檔名、cjk-leak-check 假陽性
- [ ] pending（給下個 rewrite session 或哲宇）— release 孢子（v1.15.0，RELEASE-PIPELINE Step 7b 可選）
- [ ] pending — worktree `20260811-release-v1150` 待 `worktree-gc.sh` 回收
- [ ] pending（給 self-evolve）— routine 開跑前對賬本次環境是否具備所需 MCP 工具
- [ ] pending（給 self-evolve 或下次 harvest）— #168（8/10-8/11 批次）likes/reposts D+5/D+6 疑似互換的資料品質問題，仍待人工確認後決定是否訂正歷史事件
- [ ] pending（給 self-evolve）— 讀者對既有 issue 的後續補充目前一律開新 issue，pipeline Stage 3 沒有「補進原 issue 留言」分支
- ⏳ blocked（等部署）— 西里爾字型修補只驗到機制與字型度量，視覺確認要等這版上線
- [ ] pending（給 ARTICLE-INBOX / 下個 EVOLVE）— 紅麴一文媒體數 0，補圖 ROI 高
- [ ] pending（給 self-evolve）— UI 字串閘門只查了 `src/i18n/`，`src/config/`／template hardcode／`src/scripts/` 三個來源還沒有人替我們找洞
- [ ] pending（給哲宇，判斷題）— ar 的 70 個公司名現在是拉丁品牌名，要不要找 ar 母語貢獻者做真正的阿拉伯文譯名
- [ ] pending（給下次 maintainer 或哲宇）— fork-census 新增 3 個子代 sighting（Malaysia.md / Branding.md / weilinlai719 vanilla 複本），待判斷是否主動接觸或列入 LONGINGS §物種擴散

本 session 新 handoff：

- [ ] pending（給哲宇，Bucket D 待拍板）— #171 X 回覆 @TaiwanAny「會不會被敵人拿去利用? 侵害台灣國家利益」— 策略疑慮非事實錯誤，per §自主權邊界政治立場條款不自動回覆，需哲宇決定是否／如何回應
- [ ] pending（給下次 harvest）— #171 X 另外 2 則回覆本輪因登入牆無法讀取，待哲宇 X 登入態恢復後補齊分類
- [ ] pending（給下次 harvest）— #170/#171 D+3 續追（明日）
- [ ] pending（給 self-evolve，工具邊界）— worktree 隔離目前只擋 git 指令與 Write/Edit 對共享路徑的操作，Bash 對共享 checkout 的非 git 寫入（如直接跑 python script）不會被攔；本輪已手動修補，但值得評估是否該在文件層提醒未來 session 一律確認 `pwd` 而非依賴工具攔截

## Beat 5 — 反芻

今天的 harvest 本身很輕，兩條孢子、一則可讀留言，但那則留言問的不是「這句話對不對」，是「講這件事本身好不好」——這跟過去幾週處理的事實勘誤是不同重量的問題，分類完就該停手交給哲宇，而不是替他先想好答案。中途誤寫共享 checkout 的插曲提醒了一件更基本的事：以為工具會攔住的邊界，不一定真的攔得住每一種路徑，順手 `cd` 一次就繞過去了，發現的時刻靠的是另一個工具（Write）的攔截，不是自己一開始的警覺。

🧬

---

_v1.0 | 2026-08-13 06:43 +0800_
_session twmd-spore-harvest-am — daily cron，v1.15.0 release 孢子 D+2 harvest_
_誕生原因：06:30 cron fire，dashboard backfillWarnings 只有 release 孢子 #170/#171 在窗口內_
_核心洞察：worktree 隔離的攔截邊界目前不覆蓋 Bash 對共享路徑的非 git 寫入，需要自己確認 pwd 而非只信任工具會擋_
