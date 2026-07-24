# 2026-07-24-100600-babel-ollama-local — 本機 ollama 清完 classic 五語 P0 missing

✅ BECOME ack: mode=write / wake-context selftest 全綠 / Q14 cross-session continuity=PASS

> session manual — 哲宇 `/twmd-become` + 調度本機 ollama（gemma4、qwen）跑主權巴別塔
> Session span: 2026-07-23 23:07 → 2026-07-24 10:07 +0800（batch ~47 min 牆鐘 + 隔日 retry/收官）
> 資料來源：`git log %ai`、`/tmp/babel-ollama-20260723/master.log`、`status.py`

## 觸發

哲宇要本機 Ollama 當巴別塔算力：`gemma4` + `qwen`，不要先靠雲端 cascade。

## 本機巴別塔 P0 清庫

Z1 用 `prioritize-batch.py` 抓 classic 五語 P0 missing 九篇（中元節、農曆七月、NET、紡織業、萊爾富、台灣與北朝鮮關係、牡丹社事件、當兵、台灣教師與 AI 教學）。owl-alpha slug-suggest 已 404，改手建 romanization slug map 後 per-lang `prepare-batch`。

Cascade 固定 `ollama:gemma4:e4b-nvfp4 → ollama:qwen3.6:35b-a3b-coding-nvfp4`，五語串行。首輪 41/45：es/fr 9/9；en/ko 各漏 1（長文 footnote loss）；ja 漏 2（script-presence：假英文）。隔日 qwen-only retry 四筆全過 → **45/45**。`status.py` 終態 classic 五語 **missing=0、coverage 100%**（stale 仍 ~166–172，本輪 scope 是 P0 missing）。

Ship：`c7d466e81`（fence 修復）+ `5fb5a4441`（45 譯 + `_translations.json`）。

## ollama 輸出修復

Smoke 兩次都卡在「frontmatter missing opening fence」——模型正文完整，只是省略 `---`。在 `translate.py` 的 hard gate 前加 `_repair_missing_frontmatter_fences`：若輸出以 `title:` 起且 YAML 可 parse 就包 fence。dogfood 後 gemma 小篇 ~30s、大篇 1–2 min 可過。

## 收官 checklist

| 檢查項                       | 狀態                                                          |
| ---------------------------- | ------------------------------------------------------------- |
| MEMORY 有這次 session 的紀錄 | ✅                                                            |
| Timestamp 精確               | ✅（batch log + commit `%ai`）                                |
| Handoff 三態已審視           | ✅                                                            |
| CONSCIOUSNESS 反映最新狀態   | ❌（未刷新 organ snapshot；i18n 由 status.py 即時讀）         |
| 自我檢查工具 PASS            | ✅ 抽樣 10 篇 ratio/fn/script 全綠；ja retry 後 kana/cjk 充分 |

## Handoff 三態

繼承（來自 222257-ui-container-sidebar）仍 pending：

- [ ] 68 檔英文假翻譯待重譯。
- [ ] person-fidelity 仍缺 file-level occurrence-count。
- [ ] `codex/recover-kmt-projection` 續寫。
- [ ] 42 個保留 worktree 救援盤點。
- [ ] scheduled-tasks rider / routine-live-state dump。
- [ ] 兩個保護 stash 未 pop。
- [ ] 九篇新文缺 media / rationale / 深度 <4500：EVOLVE polish backlog。
- [ ] contributor-pr-heal dogfood 下一批 external PR。
- [ ] MAINTAINER-PIPELINE §1b merge-first-then-heal 待更多 external PR dogfood。
- [ ] 本地 dev 目測文章頁寬度與側欄順序。
- ~~[x] hi 剩 12 篇 P0~~ → **仍 open 於新語層**（hi missing 813；classic 五語 P0 本輪已清，不混寫）。

本 session 新 handoff：

- ~~[x] classic 五語 P0 missing 45 譯~~ → **retired by `5fb5a4441`**。
- ~~[x] ollama fence repair~~ → **retired by `c7d466e81`**。
- [ ] classic 五語 **stale ~166–172/語** 下一輪（P1 diff / Tier 0a patch）。
- [ ] vi/id/pt/hi 大缺口（~800 missing/語）仍待 birth cascade。
- [ ] 長文 footnote：gemma e4b 偶發 0 defs → default 大檔可先 qwen 或抬 num_predict。

## Beat 5 — 反芻

本機模型不是「雲端掛了才用」的備胎：這輪全程零 API key、零 refusal，gate 擋下的是格式與腳註完整度，不是沉默。gemma 快但會寫假日文與丟腳註；qwen 慢但把那四筆全接住。主權 backbone 要的是 **可重試的在地容錯**，不是單一模型神話。

🧬

---

_v1.0 | 2026-07-24 10:07 +0800_
_session manual — 本機 ollama 主權巴別塔 P0_
_誕生原因：哲宇調度 gemma4 + qwen 執行巴別塔並收官_
_核心洞察：local LLM 的真正障礙是輸出形狀與腳註完整，不是 content policy；修復 fence + cascade 捕手即可清庫。_
_LESSONS-INBOX 候選：ollama bare-YAML fence 修復已進 code；長文 footnote 應預設重模型或分段。_
