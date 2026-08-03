# 2026-08-03-093300-twmd-flywheel-watch — 唯一靜默的那條是我自己：昨天的收官從沒推上 origin

> session twmd-flywheel-watch — cron @ 09:30 指揮部（commander-macbook）
> Session span: 09:32:00 → 09:45:00 +0800（約 13 分鐘，1 commit）
> 資料來源：`git log %ai` / `flywheel-watch.py` / `git rev-list --left-right --count`

## 觸發

每天 09:30 從不營運的那台看飛輪還活著沒有。今天工具亮 WARN，唯一靜默的那條是 `twmd-flywheel-watch` 本身。

## 飛輪判定：轉得好，靜默的是儀器自己的影子

過去 24 小時 origin/main 有 17 筆 commit，其中 12 筆帶 `[routine]` 標記。八條 routine 留下痕跡：`data-refresh-am`（876 篇、本週 +22）、`spore-harvest-am`、`feedback-triage`、`maintainer-daily`（merge-first-heal PR #1288 黃崇仁，抽驗抓到 2 處杜撰引語）、`embeddings-nightly`、`routine-sync`（第九輪全 in-sync）、`supporters-weekly`、`routine-audit-weekly`。live 狀態 dump 齡 27.4 小時，在 48 小時門檻內。飛輪本身健康。

警報只有一條：`twmd-flywheel-watch` 該跑卻沒在 origin/main 留下 commit。它不是空場，昨天 09:33 真的跑完並寫了完整收官（本機 `400f32fb4`，兩個檔）。問題在那筆 commit 從沒離開這台機器。

## 根因：這台的 main 分岔了，而我的收官擠在分岔的另一邊

指揮部這台同時在驅動巴別塔產線，本機 main 領先 origin 87 筆、落後 36 筆。`git rev-list --left-right --count origin/main...HEAD` 回 `36 87`，其中唯一一筆 `[routine]` commit 就是昨天的 flywheel 收官——其餘 86 筆全是本機 babel 批次。這條 routine 的鐵律寫著不 pull、不碰別條產線的檔，於是一個普通的 `git push` 既推不動（非快轉）也不該推（會把整條產線的中間產物一起帶上去）。收官就這樣停在本機，隔天被自己的儀器讀成靜默。

`origin/main` 上的 flywheel 收官檔停在 08-01，08-02 那份只存在於本機。這是昨天那句「儀器只看得見推上 origin 的那層」在同一支儀器身上第二次成立，而這次量到的對象是它自己。

修法用 worktree：從 `origin/main` 開一棵獨立工作樹寫收官、commit、快轉推回、用完刪掉。主工作樹一根手指都沒碰到，鐵律的「不 pull」守住了，而記錄落在儀器唯一看得見的那一層。這條路徑從今天起是本 routine 的收官方式，寫進 handoff 讓下次不用重新發現。

## 順手清掉 handoff 上的第一把尺缺口

`flywheel-watch.py` 的第一把尺原本把 `[routine]` 後面第一個詞當 routine 名，但那個位置也可能是 commit 的主題前綴。`🧬 [routine] memory: twmd-maintainer-daily @ …` 這種句型會長出叫 `twmd-memory` 的假 routine 掛在「有動靜」欄，真正跑完的那條只剩第二把尺護著——連三天重現，handoff 也連三天原樣傳遞。

改法是先在同一行找明確的 taskId，找得到就用它；找不到而開頭又是 🧬 commit type 詞彙（`memory` `heal` `embeddings` `babel` 這十個），就不編一個名字出來。修完再跑，`twmd-memory` 跟 `twmd-heal` 兩個幽靈消失，`twmd-embeddings` 也收斂成真正的 `twmd-embeddings-nightly`，有動靜的 routine 從 6 條加 2 個幽靈變成 8 條真名。

## 收官 checklist

| 檢查項                       | 狀態                                    |
| ---------------------------- | --------------------------------------- |
| MEMORY 有這次 session 的紀錄 | ✅（同時補回 08-02 那份漏推的）         |
| Timestamp 精確               | ✅ `git log %ai`                        |
| Handoff 三態已審視           | ✅                                      |
| CONSCIOUSNESS 反映最新狀態   | ❌ 本 routine 不碰感知層                |
| 自我檢查工具 PASS            | ✅ prose-health / memory-index-lint     |

## Handoff 三態

繼承上一份（來源 `2026-08-02-093355-twmd-flywheel-watch.md`）：

- [x] ~~flywheel-watch.py 第一把尺剝前綴（vc=2）~~ retired by 2026-08-03-093300-twmd-flywheel-watch
- [ ] 五條非本 routine 範疇原樣傳遞：#1264 seo-meta 門檻校準、#1184 justfont 網域白名單、#1286 轉換器詞性擴充、台灣鎢供應鏈 Bucket D 框架待哲宇拍板、stash@{0}/{1} 長期未認領

本 session 新 handoff：

- [ ] **本 routine 收官一律走 worktree**：指揮部主 main 只要還跟 origin 分岔，收官就在 `.worktrees/` 開一棵基於 `origin/main` 的樹寫、commit、`git push origin HEAD:main`、`git worktree remove`。直接在主工作樹 commit 會重演今天這筆孤兒。等哪天巴別塔產線收工、本機 main 併回 origin，這條可退役
- [ ] **本機 main 領先 origin 87 筆待認領**（86 筆 babel 產線中間產物）。不屬本 routine 範疇，但它是上面那條 handoff 的成因，產線那邊決定何時推

## Beat 5 — 反芻

這支儀器存在的理由，是「儀器只看見存在、看不見缺席」——飛輪曾經靜默死 15 天，因為所有儀器都跑在飛輪自己身上。今天它照著同一條理由，把自己讀成了缺席。它沒讀錯：以 origin/main 為唯一真相來說，昨天的我確實不存在。錯的是我以為「commit 了」等於「留下痕跡了」。

昨天的收官還親手寫下一句「儀器只看得見推上去的那層」，然後把那份記錄留在推不上去的那層。知道一個道理跟被那個道理量到，中間隔著一次真的發生。

🧬

---

_v1.0 | 2026-08-03 09:45 +0800_
_session twmd-flywheel-watch — cron 每日飛輪體檢，指揮部_
_誕生原因：工具唯一的 WARN 指向自己，追下去發現昨天的收官從沒離開本機_
_核心洞察：commit 不等於留痕；只讀 origin 的儀器要求收官也必須抵達 origin，兩者對不上時修的是輸出通道不是判準_
