# 2026-09-16-004655-twmd-babel-nightly — ja 書目區簡體殘留閘門誤殺日文新字体，三重巡檢確認在跑的 dispatcher 不重啟

> session twmd-babel-nightly — cron 每日 00:30 多語批次同步
> Session span: 00:36:20 → 00:47:02 +0800（約 11 分鐘，2 commits）
> 資料來源：`git log %ai`

## 觸發

每日 00:30 babel 例行同步。BECOME write mode 甦醒後讀 handoff 得知本機已有一個 unified dispatcher（PID 12398）從 2026-09-14 00:53 跑到現在，三重巡檢後決定不重複起跑，把本輪心力放在算力自檢揭露的一個系統性缺陷。

## 三重巡檢 + 算力自檢

`babel-preflight.py` 判定 healthy（OpenRouter 7/7 key、本機 ollama 1 模型、fleet 1 節點可達），但「實績檢查」印出 ja 在全部 5 個 worker×backend 組合近兩日通過率全數 <15%（lagunas 1%／macm4max1 9%／macm4max2 0%／macm4max3 0%／nemo 5%，n=20-74）。`ps` 確認 dispatcher 存活 1 天 23 小時、`git log` 最近提交 20 分鐘前、`fleetctl workers` 交叉核對節點名單一致——三訊號都健康，於是不重啟，改查那個跨後端一致的 ja 低分。

## ja 假陽性家族：国/学/画

拆 dispatcher 自己的 `master.log`，144/166 次 ja 失敗的外層原因都是通用訊息「no output written by translate.py (exit=1)」，蓋掉了真正原因。往回追才看到 `detect_cjk_leak` 的具體理由：「書目區簡體殘留」。統計整份 log 的命中字集，76 次命中 100% 落在 ja，字集正好是国(45)／学(19)／画(12)三字，同期其他語言合計只有 5 次零星命中且都是別的字形（团/议/间/线/华）。

根因是 `cjk-leak-check.py::detect_simplified_residue`（`SIMPLIFIED_ONLY_CHARS` 書目區簡體殘留判準）沒有 lang 參數，這把尺是為 ru/ar 這類完全不用漢字的語言校準的，套進 ja 全字集照擋。國→国、學→学、畫→画 三字剛好是日本自己戰後新字体跟 PRC 簡化字收斂到同一個 Unicode 碼位，「我が国」「大学」「動画」這類日常詞出現在書目區（幾乎必然出現）就被整篇判 leak。

修法：`detect_simplified_residue(text, lang=None)` 新增 lang 參數，`lang="ja"` 時豁免 `JA_SHINJITAI_OVERLAP = frozenset("国学画")`，其餘簡體字判定不變；兩個呼叫端（`cjk-leak-check.py::scan_file`、`translate.py::detect_cjk_leak`）同步傳 lang。離線測過三案例（ja 含国/学 放行、ja 含真洩漏「维」仍擋、非 ja 語言判定不變）。因為 dispatcher 用 subprocess 呼叫 `translate.py`，不需重啟直接吃到新版——下一篇 ja 文章（台北橋機車瀑布）從先前必敗變成 71 秒過關存檔，`status.py` 也即時印出 ja fresh 767→768、missing 229→228。commit `57ff48fe0` + LESSONS-INBOX 記錄 `93cb07bd5`。

## 各語進度（本輪 delta，session 起點 vs 收官）

| Lang | Fresh | Missing | Δfresh                   |
| ---- | ----- | ------- | ------------------------ |
| en   | 972   | 54      | +1                       |
| ja   | 768   | 228     | +1（首次修完後成功案例） |
| ko   | 982   | 47      | 0                        |
| es   | 962   | 62      | +2                       |
| fr   | 956   | 65      | +1                       |
| vi   | 882   | 82      | +1                       |
| id   | 767   | 297     | +2                       |
| pt   | 952   | 90      | 0                        |
| hi   | 793   | 281     | +1                       |
| ar   | 864   | 200     | +1                       |
| ru   | 909   | 161     | 0                        |
| de   | 688   | 426     | 0                        |

Backend 統計（本 run dir 累計，2026-09-14 00:53 起）：lagunas 467/728（64%）、macm4max1 224/336（67%）、macm4max2 212/322（66%）、macm4max3 206/318（65%）、nemo 232/321（72%），總計 1341/2025（66%）。ja 的修復預期會把這個總平均往上拉，但需要下一輪 ja 批次規模才看得出量級。

## 分岔止血

本地 main 領先 origin 551 commit、落後 193（OBSERVER-QUEUE #56 🔒 紅線，等哲宇選 A/B/C，本輪不代理）。照既有慣例把 main fast-forward 推兩次到救援分支 `20260912-unpushed-routine-queue`（`f26b0b7c5` 與 `93cb07bd5`），origin/main 本身未動。

## 收官 checklist

| 檢查項                       | 狀態                                                    |
| ---------------------------- | ------------------------------------------------------- |
| MEMORY 有這次 session 的紀錄 | ✅                                                      |
| Timestamp 精確               | ✅（git log %ai）                                       |
| Handoff 三態已審視           | ✅                                                      |
| CONSCIOUSNESS 反映最新狀態   | ❌（本輪未跑 refresh，沿用上次快照，非本 routine 職責） |
| 自我檢查工具 PASS            | ✅（verify-commit-scope.sh 2/2 確認）                   |

## Handoff 三態

繼承上一 session：

- ⏳ blocked（延續）— main 本機 551/193 真分岔，118 篇雙邊獨立譯文取捨等哲宇選 A/B/C，per OBSERVER-QUEUE #56。本輪 +2 commit，不影響裁決範圍。
- ⏳ blocked（延續）— issue #1729（馬英九腳註）等 FACTCHECK Full mode 排程。

本 session 新 handoff：

- [ ] 下一班觀察 ja 批次規模拉大後的整體通過率是否真的顯著跳升（目前只有 1 篇即時驗證，樣本太小），若仍卡在低位要重新檢查是否還有其他假陽性字元未被本次的 `国学画` 三字集窮盡。
- [x] ~~三重巡檢確認 dispatcher 健康~~ — 已確認不重啟。

## Beat 5 — 反芻

這輪最有意思的地方不是修了 bug，是「跨後端一致的低分」這個訊號本身。五個完全不同的 worker（本機 ollama、雲端 openrouter 兩家）對 ja 都卡在個位數通過率，如果只看單一 worker 會很容易懷疑是那個模型不行，但五個一起低分排除了模型能力假設，指向共用的一道閘門。這跟 MANIFESTO §14 講的「假陽性家族默默屠殺好產出」是同一個母體現象的新形狀——上次是括號 gloss／ja 的了 markers／書名號三個家族，這次是書目區簡體殘留閘門對日文新字体視而不見。細節記進 LESSONS-INBOX。

🧬

---

_v1.0 | 2026-09-16 00:47 +0800_
_session twmd-babel-nightly — cron 每日多語批次同步_
_誕生原因：00:30 例行觸發，三重巡檢確認既有 dispatcher 健康後，把心力放在算力自檢揭露的 ja 全 worker 低分異常_
_核心洞察：跨後端一致的失敗率是「閘門攔下」訊號而非「模型能力」訊號；共用檢查器對校準時沒考慮到的目標語言天生有誤殺風險面_
_LESSONS-INBOX 候選：shared-gate-blind-to-target-language-orthography（已 append，commit 93cb07bd5）_
