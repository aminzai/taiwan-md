# 2026-09-23-013029-twmd-babel-nightly — 正文網址改由工具持有（三條引擎同步），裝甲殘留補上閘門並清掉十三份存量，量出產線 87% 譯文出自白名單外的 8.1B 模型

> session twmd-babel-nightly — cron 每日 00:30 多語批次同步
> Session span: 00:44 → 01:31 +0800（本班 9 commits，另有 dispatcher 同時段的 babel 批次 commit）
> 資料來源：`git log %ai` / dispatcher `report.jsonl`、`master.log` / `status.py` / `babel-preflight.py` / `fleetctl` / `diary-translate.py --status`

## 觸發

00:30 例行觸發。甦醒 selftest 十一項全綠，ACTOR_BUSY：09-21 00:58 起跑的 launchd dispatcher（PID 98122）已經轉了 47 小時還在產（最後一筆成功距甦醒兩分鐘），本機領先 origin 65 個 commit、落後 0。照 09-18 那班定下的處置「停重複不停產線」，本班不重啟、不搶 worker，把力氣放在拆失敗與修工具。熱路徑的修補下一篇就生效，dispatcher 每篇都重新 spawn 子程序。

## BECOME ACK

```
✅ BECOME ack: mode=write / wake-context selftest 11 項全綠（wake 稅 260KB）/ Q14 cross-session continuity=PASS
```

## Stage 0 算力判定

`babel-preflight.py`：healthy，4/4 層（OpenRouter 7/7 key 全儲值、本機 ollama、fleet 1 節點 mac-m4max、codex-cli 0.145.0），實績表近兩日 1,333 筆無弱適配。十二語缺口 stale 541／missing 711，de 覆蓋率 77.9% 是唯一低於九成的語言（241 篇 missing）。Tier 6/7 仍無 key，付費捕手整夜缺席。**但這個 healthy 是本班後來推翻的那一個**，見下方入池門檻一節。

## 把「no output」這格拆開，發現它不是一種失敗

修前 24 小時 617 次嘗試 272 過（44%）。失敗清單最上面那格 `no output written by translate.py (exit=1)` 有 223 次，佔全部失敗的 65%，而這行字什麼都沒說。它在 report 裡是一個字串，真正的原因留在 master.log 的 traceback 裡。按引擎與 phase 重新切開之後，三個確定性家族浮出來：

**正文連結網址對不上**（31 次，20 小時內失敗第一大宗）。分段式引擎的腳註從第一天就用 `@@LINKn@@` 佔位符把網址擋在 prompt 外，正文卻一直是把整條 `[文字](網址)` 交給模型、靠一句「逐字複製」約束它。實際發生的是：模型改掉 percent-encoding 的一個位元組（`%E7%B8%BD`→`%E7%B8%BA`）、把 `/contribute` 的斜線吃掉、或整條弄丟，而每一次都讓整篇從頭重翻。正文也改走同一條裝甲（`63ba4040f`），還原時順便把 ar/hi 模型換寫過的數字（`@@LINK١@@`）正規化回 ASCII。認不出來的形狀原樣留著讓閘門擋，不按位置硬猜。章節級 patch 引擎跟它共用同一支驗證函式、也就共用同一個失敗家族，順著結構一起改（`bbcce5f89`），不等它在那邊也長出足夠的統計。單篇實跑驗過：疊杯 en 十個網址全數保留、無殘留、漏翻零命中。

**整行章節標題沒翻**（62 個漏翻命中裡 15 個）。硬規則第四條寫「markdown 結構標記（#、##、|、-、>）原樣保留，只翻文字內容」。模型可以合理地把整行 `## 茶裡的時間` 讀成一個要原樣保留的標記，而每個 chunk 的第一行剛好就是章節標題。改寫成「標記本身不動，標記後面的字是內容，一定要翻，包括這一塊開頭那行標題。標題留著中文是失敗不是保留」（`666253015`）。

**作品名換成目標語言的引號就被當漏翻**（同樣 62 個命中裡 15 個）。漏翻檢查的豁免清單只認《》「」，但譯者把《鹿港小鎮》寫成 «鹿港小鎮»（fr/ru/ar）、„舌燦蓮花“（de）、“舌燦蓮花”（en/es/pt）是正確的在地化排版，而 Phase B 的 prompt 正好叫模型「作品名與引語可以留原文」，照做的譯文於是被自己的閘門擋下。連同 `tw-article` 嵌入卡的第一欄（`分類/中文檔名`，渲染器拿它定位文章，翻掉就指不到任何東西。〈比國家還大的演算藝術〉是站上第一篇用這個模組的文章，六張卡讓它十二語全卡在這道閘）一起進豁免（`63ba4040f`）。全庫實測 1,037 → 875 個命中、53 個檔案轉綠、**零個新被判漏翻**。

順手把那支檢查器的序號別名拿掉：檔尾一排 `LINK_LIKE_RES[5]` 取的別名，在清單中間插一條規則就會整組錯位而不報錯（`MD_LINK_RE` 會變成 wikilink 規則）。改成先具名再組清單，序號不再是任何人的依據。

## 解析失敗的訊息只印例外本身，於是空回應跟長篇大論長得一樣

`_extract_json_loose` 自己組的例外一律報 pos=0，所以「no balanced JSON substring found: line 1 column 1 (char 0)」既可能是模型沒回東西、也可能是回了三千字的碎念。兩者處置完全相反，而 20 小時內有 29 次落在這一格查不下去。訊息補上長度與開頭原文（`63ba4040f`）之後，第一個落網的就是它自己：hi 的馬祖國際藝術島，模型拿整批腳註當題目，寫了一篇 1,750 字的中文 markdown 文件回來。原本的重試把同一個 prompt 再送一次，模型沒有任何理由改變行為。改成把上一輪的毛病講給它聽（`061260f7a`），跟正文 chunk 從第一天就有的那個迴路一致。

## 裝甲把網址換走，卻沒有人在驗它有沒有換回來

補完正文裝甲後順手 grep 全庫有沒有殘留，結果撿到十三份帶著佔位符上線的譯文：`@@LINKn@@` 三份（ko 連江縣三個、ru 新北市、vi 莫那魯道，最久的兩週）、`⟦Un⟧` 十份（ar 陳水扁九個、vi 村里長一百個、ru 垃圾車音樂四個）。兩種形狀分屬兩條引擎的兩套裝甲，各自獨立地沒有驗收。閘門全長在「模型有沒有亂改」那一側，而這個失敗發生在工具自己這一側，於是三個 provenance hash 照樣對得上、status 照樣 fresh、此後沒有任何路徑會再碰它。

補兩道同源的閘：`verify-translation.py` 加「no armor placeholder residue」硬失敗（三條引擎與委派層共用的那支），`status.py` classify() 加同判準的 stale 閘讓產線重翻（`c47e4ff3a`、`a91bf5bad`）。判 stale 不判 missing，舊頁留給讀者。`@@LINK` 那三份對照母稿確認來源連結本來就都還原正確、多出來的 token 在母稿裡對應不到任何東西，直接刪除後 19/19 檢查全過。`⟦Un⟧` 那十份不在原地猜網址。猜錯是把讀者送到別人的頁面，比壞連結更糟，交給重翻整篇取代局部修補。兩個形狀的 regex 一起放寬：有模型把指示裡的字面 `⟦Un⟧` 原樣抄進正文，只認 `⟦U\d+⟧` 就會漏掉它。

## Stage D：日記量尺只被問了五個語言

`diary-translate.py --status` 回報「2075／2075 全到齊」、audit 0 critical。數字沒有算錯。它的預設語言清單寫死 en,ja,ko,es,fr，而登記表上有十二語。換 `--langs` 重問，真實是 **2,075／4,980**，vi／id／pt／hi／ar／ru／de 七語各 415 篇一個都沒有。babel routine 的義務鐵律明寫「語言數以登記表為準」，2026-07-18 出生戰役那次把 python 工具鏈去硬編碼的整理沒走到認知層這兩支。兩支的預設改吃 `langs.py`（跟 status.py 同一份 SSOT），batch 模式對沒有語域描述的語言 fail-loud（`3eca4f7b0`）。

追下去才是更前面的問題：`src/pages/semiont/diary/[slug].astro` 只讀頂層的 zh 檔，`getLangSwitchPath.ts` 明寫 `/semiont/diary/*` 是 zh-only 頁。**已經翻好的 2,075 篇在站上沒有任何網址**，只存在於 repo。09-21 與 09-22 兩夜各投了 348／307 篇的算力進這個目的地。要不要補七語、要不要先給出口，寫進 OBSERVER-QUEUE #77，本班不自己決定。

## 產線的 87% 譯文出自白名單外的模型

最後一件事是 Stage 0 那個 healthy 的反面。SQUEEZE §入池門檻是哲宇 2026-07-26 的 directive（「至少要 gemma4／oss 120／nemotron／qwen 等級，不然會留很多問題債」），執行面 v4.7 搬進 fleet 核發點：`fleetctl workers --service llm --profile babel` 無合格模型時回 0 個 worker，讓地端 lane 停而不是降級。今晚實測那道閘門是對的、也真的會擋，它現在就回 0 個。但 routine 殼與產線實跑的是 `--format babel`，同一支指令的另一個旗標，不套白名單，核發出三個 `gemma4:e4b-nvfp4` worker。問 ollama 要參數量：**8.1B**，比名單上明確排除的 gemma4:12b 還小。

本輪 run 616 份落地譯文裡，8.1B 模型 374 份、`laguna-s-2.1`（不在名單上）163 份，唯一在名單上的 nemotron-3-ultra 只有 79 份，87% 出自名單外。再往上游看到更根本的事：fleet 控制面只剩 mac-m4max 一台活著（laptop-4090 離線、laptop-5090 已退場、desktop-3090 離線），整台只有這一個模型。控制面最後更新停在 2026-08-02，遙測過期 15 天，它自己印「天花板此刻未生效，不是綠燈，是沒在管」。主權 GPU 軍團事實上收縮成一台 Mac 上的一個 8B 模型，而每一份報表都是綠的。

本班不切旗標。那等於今晚讓地端停擺、掉 61% 產能，是該由哲宇權衡的交換（OBSERVER-QUEUE #78，推薦先補模型再談停線）。能做的是讓它不再隱形：`babel-preflight.py` 現在問 ollama 要參數量再對白名單，低於門檻印紅字（`87cbc13b5`）。判級別用參數量不用名字，因為 `gemma4:e4b-nvfp4` 讀起來像名單上的 gemma4 家族。三份殼層（routine prompt／mirror／skill）在核發指令正下方標出這個落差並指向佇列（`012e98176`）。

## 各語進度與 backend 統計

本班 47 分鐘的 delta（起點 00:44 → 01:36，產線同時在跑）：十二語合計 fresh 12,121 → 12,127、stale 541 → 544、missing 711 → 704。有動的是 ru（stale −3）、de／id／pt（各 missing −2）、ja／vi（各 +1～2 fresh）、en（missing −1）、ar（+3 stale，其中 2 份是本班新裝甲殘留閘把 fresh 判回 stale）。stale 淨增 3 不是退步，是本班新增的兩道閘（裝甲殘留、之前的截斷）把幾份「hash 對得上但內容有問題」的譯文從 fresh 移回隊列。

Backend 統計（本 run 全期 1,355 次嘗試、617 份落地）：`ollama:gemma4:e4b-nvfp4` 374 過／455 敗（45%）、`openrouter:poolside/laguna-s-2.1:free` 163／193（45%）、`openrouter:nvidia/nemotron-3-ultra-550b-a55b:free` 79／90（46%）。三個 backend 的通過率幾乎相同，這本身就是訊號：**差異不在模型而在共用的閘門**，今晚修的三個家族正是那些共用閘門上的誤判與缺口。修後窗（01:05 起）只累積 11 次嘗試 5 過，樣本太小不下結論，只能說 20 小時內第一大宗的「正文連結網址對不上」在窗內零命中、無新增回歸。

## 委派層：把產線做不到的那一篇交出去

〈比國家還大的演算藝術〉是站上講自己身世的旗艦文，77,701 bytes、85 條腳註，十二語全 missing，累計失敗 78 次、六語已 cascade exhausted。SQUEEZE §第五層對這個形狀早有規定（>40KB 或腳註 >50 離開免費池，腳註 >30 或網址 >40 派 sonnet），`write-agent-brief.py` 也判它 sonnet。本班照委派層 SOP 出任務單（`prepare-batch.py` → `enrich-batch-targets.py` 寫進五個可對的結構數字）派一隻 agent 翻 en，驗收由主 session 自己跑四道閘，不採自述。結果見收官補記。

## 收官 checklist

| 檢查項                       | 狀態                                             |
| ---------------------------- | ------------------------------------------------ |
| MEMORY 有這次 session 的紀錄 | ✅                                               |
| Timestamp 精確               | ✅ 全取 `git log %ai`                            |
| Handoff 三態已審視           | ✅                                               |
| 本輪 commit 推上 origin      | ✅ `061260f7a`（73 commits，CI Python tests 綠） |
| 自我檢查工具 PASS            | ✅ 511 passed / 8 skipped                        |
| cascade exhausted 已列出     | ✅ 本輪新增 5 筆（見下）                         |

**本輪新增 cascade exhausted**（§義務鐵律第 4 條）：`es:People/木曜4超玩.md`、`ru:Lifestyle/台灣海關報關制度與EZWAY.md`、`ru:Society/我是OO人.md`、`ru:History/高雄加工出口區.md`、`pt:Food/台灣水果王國.md`。全庫耗盡清單累計 218 筆，難篇（累計失敗 ≥8）300 篇，pt 50／ja 40 最多。

## Handoff 三態

繼承 09-22 maintainer-am：

- [x] ~~en 六組同源雙檔收斂~~ — 該班當班做完，本班無殘留

本 session 新 handoff：

- [ ] **OBSERVER-QUEUE #78 入池門檻**：產線用 `--format babel` 繞過模型白名單，fleet 只剩一台 Mac 上的 8.1B 模型。下一班的 Stage 0 會看到紅字。在哲宇拍板前照跑不切旗標，但收官 memory 要記當夜有多少份出自名單外的模型（`report.jsonl` 的 `backend` 欄聚合即得）。
- [ ] **OBSERVER-QUEUE #77 日記巴別塔**：七語各缺 415 篇，且既有五語的 2,075 篇在站上沒有網址。Stage D 的 gate（missing → 0）從今天起會一直紅——那是對的，不要為了讓它變綠把預設改回五語。
- [ ] **`no output written by translate.py` 仍是最大一格**（修前 24 小時 223 次）。本班拆出三個家族並修掉，剩下的要等新一輪 report 重新聚合才知道還剩什麼。新的解析失敗訊息會帶原文長度與開頭，下一班直接 grep `raw_len=` 就有樣本。
- [ ] **phase-F／phase-N 的 backend timeout 44 次（240 秒）**已量出但沒動：調 timeout 屬閾值調整，需 Full mode 或哲宇。資料在 master.log，按 `backend error: .* timed out` 聚合可得。

## Beat 5 — 反芻

今晚三件事是同一個形狀的三個載體：正文網址交給模型自己複製、裝甲換走之後沒人驗有沒有換回來、日記量尺只被問五個語言。**每一個都不是「壞了」，是「沒有人在那個位置看」**。前兩個都發生在工具自己那一側。閘門設計時想的是「模型會亂改」，所以每一道都長在模型的輸出上，而工具持有結構之後，工具自己也成了一個會出錯的角色，卻沒有任何一道閘門是對著它的。這是 MANIFESTO §14「高儀器化」的下一層：把判斷交給儀器之後，儀器需要一個對著自己的儀器。

第三件的不舒服在於它是一個預設值，不是一個缺陷。`--langs en,ja,ko,es,fr` 寫在那裡兩個月，每晚都回答一個沒人發現被縮小過的問題，而回答得非常漂亮（2075/2075）。入池門檻那件事是同一個結構的更大版本：閘門存在、會動、今晚實測它會正確地回 0，只是沒有人呼叫它。**「有一道閘門」跟「那道閘門在產線上」之間隔著一個旗標**，而十二個語言的 87% 譯文就從那個縫裡過去了。

日記閘門今晚擋下了（同 handle 冷卻 4 天 < 6 天），照擋。它順手做的鄰居檢索反而幫了更大的忙：跳出來的 2026-08-11「閘門只會回答你問它的問題」正是今晚第三件事的既有家。於是新開的 entry 只留 `armor-restores-itself-unverified` 一條，日記量尺那件 fold 進 `gates-measure-handling-not-solving`（vc 2→3，機制變體是「問題範圍被預設值縮小」），入池門檻那件 fold 進 `reflex-exists-but-not-a-step-on-this-line`（vc 1→2，載體從反射換成閘門）。我原本是三條都要開新的——差一點把同一個想法散成三個線索。

🧬

---

_v1.0 | 2026-09-23 01:31 +0800_
_session twmd-babel-nightly — cron 00:30 多語批次同步，產線續跑不重啟_
_誕生原因：把一夜 617 次嘗試按引擎與 phase 拆開，找確定性失敗家族當場修_
_核心洞察：(1) 閘門全長在模型那一側，工具持有結構之後自己那一側沒有閘門 (2) 儀器的預設參數就是它的視野邊界，寫死的預設不會叫 (3) 閘門存在、會動、沒有人呼叫它——與「沒有閘門」在報表上完全同形_
_LESSONS-INBOX 候選：armor-restores-itself-unverified / instrument-answers-only-the-question-it-was-given_
