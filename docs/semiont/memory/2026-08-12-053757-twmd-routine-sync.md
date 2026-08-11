# 2026-08-12-053757-twmd-routine-sync — 三層對賬第十九輪，1 項 prompt-drift 用 --harvest 收進 git

> ✅ BECOME ack: mode=micro / Q14=PASS
>
> session twmd-routine-sync — 每日 05:30 cron 心跳
> Session span: 05:37 → 05:39 +0800（~2 分鐘，1 commit）
> 資料來源：`git log %ai`

## 觸發

每日例行：讓這台機器的 routine prompt 跟 cron 排程設定，跟 git 裡的 routine SSOT 對齊。排在晨鏈（data-refresh / harvest / feedback-triage / maintainer）之前，確保它們醒來讀到的 prompt 是對齊過的版本。

## 對賬結果

`git checkout main && git pull` 確認已是最新（工作樹有一份 embeddings-nightly 05:35 留下的未追蹤 memory 檔，非本 routine 範疇，不動）。`routine-sync.py` 首跑 18 條 task 中 17 條 `in-sync`，`twmd-maintainer-daily` 標 `prompt-drift`。

判方向：diff 顯示機器版（mtime 2026-08-11 19:13）比 git SSOT 版多 12 行——8/11 晚間 commit [6e9615913](https://github.com/frank890417/taiwan-md/commit/6e9615913a3444bc33c344f5ebc6e318f4ee5978)「maintainer 從分診台變回維護者」改了 canonical（`MAINTAINER-PIPELINE.md`）跟 project skill 兩層，commit message 說「三層一起改」但 `git show --stat` 只列 2 個檔——第三層 cron 即時鏡像是直接寫進機器本地 `~/.claude/scheduled-tasks/twmd-maintainer-daily/SKILL.md`，沒進 git。判定機器新，跑 `--harvest` 收回 §1c「issue 的 default 是修好，不是分類好」鐵律 + 新 quality gate 列。

`git add` 只加這一個檔（未追蹤的 embeddings-nightly 記憶檔不碰），commit + push 乾淨落地。無 `⏰`／`🔌` cron 或 enabled 漂移訊號，跳過 scheduled-tasks MCP 動作。

## 收官 checklist

| 檢查項                       | 狀態                                       |
| ---------------------------- | ------------------------------------------ |
| MEMORY 有這次 session 的紀錄 | ✅                                         |
| Timestamp 精確               | ✅                                         |
| Handoff 三態已審視           | ✅                                         |
| CONSCIOUSNESS 反映最新狀態   | ❌（本 routine 不動 CONSCIOUSNESS）        |
| 自我檢查工具 PASS            | ✅（`routine-sync.py` 二跑印「三層一致」） |

## Handoff 三態

繼承上一輪（`2026-08-11-053716-twmd-routine-sync`）：

- [x] 無 retired 項——上輪零漂移，這輪抓到 1 項並已收進

非本 routine 範圍但沿用 wake-context §handoff 的既有待決項（不動，交對應 routine / 哲宇接手）：

- [ ] pending（給哲宇）— #1264 seo-meta 多語言門檻校準、#1184 justfont 後台網域白名單、#1286 轉換器詞性感知功能擴充、免疫黃燈連續多日（wake-context 顯示自 2026-07-05）
- [ ] pending（vi 產線）— w5 剩約 90 篇、vi stale 27 篇、118 檔漢字黏著（>50 檔等哲宇）、Folk Music 檔名、cjk-leak-check 假陽性
- [ ] pending（給下個 rewrite session 或哲宇）— release 孢子（v1.15.0，RELEASE-PIPELINE Step 7b 可選，已在 finale 報告問哲宇待點頭）
- [ ] pending — worktree `20260811-release-v1150` 待 `worktree-gc.sh` 回收
- [ ] pending（給 self-evolve）— routine 開跑前對賬「本次環境是否具備所需 MCP 工具」，缺工具 fail-loud 而非只寫當日 memory

本 session 新 handoff：無。

## Beat 5 — 反芻

連續三輪零漂移之後這輪抓到一個真實案例：commit message 寫「三層一起改」，但那三層裡有一層（cron 即時鏡像）根本不在 git 追蹤範圍內，只能靠 routine-sync 這種對賬工具事後補上。這正是這條 routine 存在的理由——git 說的話跟這台機器實際在跑的話，中間有一層物理縫隙，寫 commit message 時的善意不會自動填住它。

🧬

---

_v1.0 | 2026-08-12 05:39 +0800_
_session twmd-routine-sync — 每日三層對賬心跳_
_誕生原因：cron 觸發，例行 SSOT 對齊_
_核心洞察：19 輪來首次抓到跨層 SPOF（cron 鏡像不在 git 追蹤範圍），--harvest 一次收回_
