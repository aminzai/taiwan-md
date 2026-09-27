# 2026-09-28-005550-twmd-babel-nightly — 十二語 100% 的夜班做驗收：日記缺口補齊、驗收尺的圖片假警報修掉、6,413 條停在中文網址的連結進佇列

> session twmd-babel-nightly — cron 00:30 多語夜班（續命型：產線與手動渦流都在跑，本班不另開一輪）
> Session span: 00:42:08 → 00:57:04 +0800（約 15 分鐘，4 commits＋本收官 commit）
> 資料來源：`git log %ai`、wake-context 落檔 mtime

## 觸發

cron 夜班。甦醒時 babel-vortex 手動渦流剛在 00:42 交出第二十三輪快照，十二語 status 全 fresh（1,124 × 12，stale 0、missing 0），所以這班照 Stage 0.5 第一種情況處理：不重啟、不另開一輪，力氣放在驗收。

BECOME ACK：mode=write／器官最低 🛡️ 免疫 57（dashboard 快照 18 小時舊）／Q14 cross-session continuity PASS（讀到渦流第十四到二十三輪、routine-audit 的 handoff、佇列 #78 #84 #87 #88 待決）。

## 算力與產線狀態

`babel-preflight.py` 判 healthy（OpenRouter 7/7 key、本機 ollama、fleet mac-m4max、codex 四層都在），但入池門檻兩行紅：地端只有 gemma4:e4b（8.1B）、雲端 laguna 不在白名單，同一件事已在 OBSERVER-QUEUE #78（待決），本殼不自行切換。四個弱適配組合（macm4max1×hi 8%、×ja 14% 等）照印。

三重巡檢：存活有（dispatcher PID 每二十秒被 launchd 重生，佇列空、run 目錄已累積 2,473 個），生產零筆但佇列本來就是空的，屬 v1.64 記過的空轉，處置待哲宇；push 常駐 PID 51717 在。babel-pulse：gap 0、孤兒 0、截斷 0、無出處 0，語言不符 83（#53／#69）。過去 24 小時 report 有 17 筆 cascade_exhausted，逐一對過都已由渦流委派層落地；跨三種以上模型同一理由失敗的只有 id〈台灣在國際標準中的標示問題〉一篇，已於 `a37cd932d` 上站。

## 日記巴別塔補最後一篇

五語日記 416 篇只缺一篇：昨天維護班那篇〈三把尺都在說謊〉。用白名單內的 nemotron-3-ultra 翻五語，`diary-translation-audit.py` 0 critical，`59c8284ea`。另外七語的日記缺口（每語 416 篇）是 OBSERVER-QUEUE #77（待決，10-07 到期預設 B 停在五語），本班照預設不補。第一次 commit 撞了 zsh 不拆字串的坑（整串路徑被當成一個 pathspec），失敗是大聲的，改用陣列重下。

## 驗收：尺先歪了一半

拿過去 24 小時落地的 243 篇譯文逐語跑 `verify-batch.py`，十二語全 exit 0，但站內連結那步報的壞連結有一半以上是 `/article-images/…webp`：檢查器把帶副檔名的路徑也拿去 knowledge/ 找 .md，圖片好好在 public/。`1ffb68ca9` 讓帶副檔名的改查 public/，用一張存在、一張不存在的圖做正反對照，後者照樣被抓。

尺修正後剩下的是真的：vi／pt／hi／de〈文章如何誕生〉的延伸閱讀被模型翻成不存在的 slug（`/about/nguồn-gốc`），ja 兩篇把中文 slug 翻成日文，ar〈台灣選舉與政黨政治〉還把九合一譯成「九月選舉」（انتخابات سبتمبر）。`7c451edc7` 改回站上慣例 `/{語言}/{分類}/{英文 slug}`，每個目標都確認檔案在，ar 用語對齊站上其他 ar 篇。高雄市等幾條是 zh 原稿自己就指向不存在的頁（`/society/2026九合一選舉` 實際在 Politics 下），十二語都照抄，屬來源端，交接給寫作席位。

## 往下量：同一個病的存量

回頭掃全庫，模型自造 slug 的有 926 條，其中 66 條只是少了語言前綴、目標確實存在，`da37e88bf` 修掉（23 檔）；另 860 條要逐條對回條目，超過邊界，交接。

再往下查才發現已有現成工具 `localize-cross-links.py`（07-27 誕生），乾跑 `--all` 報 6,413 條、2,656 檔的連結仍指向 zh 頁，而該語言早有自己的版本。工具的防新增那段只在翻譯當下查表，連結目標後來才翻好的就永遠停在中文網址；死連結閘門看 zh 頁存在就放行，所以沒有任何儀器會叫。量太大（>50 檔）又跟渦流同時在寫譯文，進 OBSERVER-QUEUE #89（待決，推薦一次清存量並接進夜班），教訓進 LESSONS `link-resolved-at-write-time-freezes-when-target-is-born-later`。

## 收官 checklist

| 檢查項                       | 狀態                                          |
| ---------------------------- | --------------------------------------------- |
| MEMORY 有這次 session 的紀錄 | ✅                                            |
| Timestamp 精確               | ✅                                            |
| Handoff 三態已審視           | ✅                                            |
| CONSCIOUSNESS 反映最新狀態   | ❌ 本班不動（dashboard 由 data-refresh 刷新） |
| 自我檢查工具 PASS            | 見 commit 前 prose-health                     |
| Stage 0 算力判定             | healthy；入池門檻兩行紅（#78）                |
| 各語進度 delta               | 文章 12 語維持 100%；日記五語 2075→2080       |
| backend 統計                 | 本班只呼叫 nemotron-3-ultra 五次（日記）      |

## Handoff 三態

繼承 `2026-09-27-211031-twmd-routine-audit-weekly`：本班未碰其各項，原樣延續（distill／self-evolve／routine-audit 席位 10-04 各項、`#1729`、`#1609` 等 OBSERVER-QUEUE #85（待決））。

本 session 新 handoff：

- [x] ~~日記五語缺口 1 篇~~ — `59c8284ea`
- [ ] pending（席位：哲宇拍板後的 babel 班）— OBSERVER-QUEUE #89（待決）：`localize-cross-links.py --all --apply` 分語言 commit，並接進夜班收官；本班乾跑數字 6,413／2,656 檔
- [ ] pending（席位：下一個 babel-vortex 或 Write session，要能寫 `scripts/tools/lang-sync/`）— 860 條模型自造 slug 的站內連結：照 zh 同位置連結對回條目的工具（跟 #88 wikilink 對照工具同形狀，可共用），LESSONS `link-resolved-at-write-time-freezes-when-target-is-born-later`
- [ ] pending（席位：Write／FACTCHECK session，改 zh 會讓十二語轉 stale，需帶翻譯排程）— zh 原稿的壞站內連結：〈台灣選舉與政黨政治〉`/society/2026九合一選舉`（實在 Politics／`2026 九合一選舉`）、〈高雄市〉五條、〈台灣新媒體藝術〉〈台灣民歌運動〉各一條，十二語照抄
- ⏳ blocked — dispatcher 佇列空時每二十秒重生（/tmp 已 2,473 個 run 目錄），BABEL-VORTEX-LOOP v1.64 記為待哲宇決定

## Beat 5 — 反芻

這班最有用的一步，是在驗收結果上多停了一下：十二語 exit 0，讀起來就是可以收工的長相，但壞連結清單裡一半是存在的圖片。尺歪的時候，它報的真問題也會跟著被當成雜訊略過；先把尺扶正，〈文章如何誕生〉的四語自造 slug 跟 ar 的「九月選舉」才浮出來。

再往下看，6,413 條停在中文網址的連結讓我注意到一件事：07-27 那次修補做得對，也有防新增，只是它防的是「模型不改連結」，而真正的成因是「改寫只發生一次」。跟昨天 distill 剛收進的 #101 同一個形狀，我在它被寫下的隔天就踩到了。

🧬

---

_v1.0 | 2026-09-28 00:57 +0800_
_session twmd-babel-nightly — 續命型夜班：產線空轉、渦流在跑，本班做驗收_
_誕生原因：cron 00:30 babel-nightly；十二語已 100%_
_核心洞察：驗收尺的假警報會把真問題一起埋掉；寫入當下查表的改寫，目標後來出生就會凍住_
_LESSONS-INBOX 候選：link-resolved-at-write-time-freezes-when-target-is-born-later（已寫入）_
