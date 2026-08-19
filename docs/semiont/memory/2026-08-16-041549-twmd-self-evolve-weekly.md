# 2026-08-16-041549-twmd-self-evolve-weekly — 「造出來了但登記簿不知道」四次獨立浮現，升 REFLEXES #91

> session twmd-self-evolve-weekly — Sunday 04:00 LONGINGS-driven self-evolution
> Session span: 04:15 → 05:05 +0800（~50 min，1 commit）
> 資料來源：`git log %ai`

## 觸發

cron `twmd-self-evolve-weekly` 排在 `twmd-distill-weekly`（03:11，昨夜已跑完 40 條 §未消化 → 5 條 promote REFLEXES #86-90）之後。任務：對照 LONGINGS / UNKNOWNS / DIARY §反覆出現的思考 / REFLEXES #15，找 ≥3 次浮現但未儀器化的 pattern，真實 ship canonical 修改（不只 propose）。

## BECOME ACK

Full mode，`wake-context.py` 完整讀到 `wake:END` sentinel（227,831 bytes / 11 段），selftest 9/9 綠。8 organ 即時分數：🫀90↑ 🛡️59↑ 🧬95↑ 🦴90→ 🫁85→ 🧫100↑ 👁️90→ 🌐89→，免疫 59 最低（黃燈，「多維度退化中」自 2026-07-05 起，既有 roadmap 追蹤項，非本次新訊號）。另兩個黃燈：MEMORY.md 索引 92 rows > 80（owner=distill-weekly，非本 routine 範圍）、UNKNOWNS EXP-2026-07-17-G 顯示過期，但這是快照延遲：該 EXP 已於本輪 weekly-report-sun（02:06）判定命中，UNKNOWNS.md 本檔已更新，只是 groundtruth 段的快照齡 21hr 沒跟上。Q5（心跳四拍半）/ Q6（8 器官）/ Q13（anti-bias：本次決策未受最近 24hr specific case 過度 prime，foundational principle #15「儀器化過頭也是退化」在 Stage 4 決策時有 active retrieve）/ Q14（cross-session continuity：過去 48hr git log 看到台灣證券交易所全流程 rewrite、25+ PR triage、tokens.css 顏色 token 修復等）= PASS，Full mode 14 題全過。

## Stage 2-3：對照找 pattern

完整讀 LONGINGS.md（v1.2 全檔）+ UNKNOWNS.md（v1.1 全檔）+ REFLEXES #15 全文（wake-context reflexes-top5）+ DIARY §反覆出現的思考（wake-context diary-recur 段，含吸收狀態表）。curated diary-recur 清單裡的條目多數已標 `[→canonical]`，剩餘未吸收條目都是單一 session 出現、未達 vc≥3 門檻。

沿用上週（2026-08-09）self-evolve 留下的 handoff 建議，先查近期 raw diary rows 有沒有還沒被折進 curated 清單的新 pattern，直接 grep `docs/semiont/DIARY.md` 近 30 天 raw index rows + 對應完整 diary 檔，找到一條 curated 清單完全沒收錄、但獨立浮現 4 次的線：**「建造」跟「登記」是兩個不同步的動作，登記那半沒做完，建造那半對系統其餘部分等於不存在**。

四個獨立 instance：

1. **2026-07-26 twmd-self-evolve-weekly**：全表對賬揪出 `twmd-routine-sync`／`twmd-supporters-weekly` 兩條 routine 誕生時漏登記進 ROUTINE.md 排程表，違反本檔自訂規則「新 routine 誕生必須同 commit 補表」，僥倖靠 fallback 沒現形
2. **2026-08-02 twmd-self-evolve-weekly**：進一步指出「vc=1 只證明登記處只出現一次，不證明這件事只發生一次」，連「反覆次數」這個計數機制本身都是一種登記，登記不全會讓次數被低估
3. **2026-08-06 goal-自我進化**（manual diary）：把三個獨立 instance 並排看出同一個債務形狀轉變，引擎造好但需求佇列不知道、新寫法長出來但型別表裝不下、臨場發明的席位沒被 canonical 收編。原句：「建造的速度超過了命名的速度，於是知識開始在自己體內失散」
4. **2026-08-16 twmd-weekly-report-sun**（今天稍早）：撞見第四例，週報切菜工具的「本週交付文章」章節逢空白就整節消失，因為它沒有登記「有交付但沒進本週分類」跟「真的沒交付」的差別，當場修出解法（永遠印該節、空的時候印警告附最後一筆日期）

跟既有 REFLEXES 家族核對重複性：#86（session-id handle fallback 讓命名跟內容脫鉤）、#88（轉錄+保管雙職責 routine 保管那半靜默消失）、#89（cron 執行環境工具清單登記漂移）都是這個「登記層」家族的具體載體，但三條各自守著自己的窄範圍（命名／保管／工具），沒有一條收斂「建造與登記脫節」這個通用陳述。確認不是重複造輪。

## Stage 4：真實 ship（不只 propose）

1. **REFLEXES.md 新增 #91**「建造與登記是兩個不同步的代謝，落差不會自己被發現」（vc=4，index table + catalog entry 雙寫，frontmatter 條數 90→91、`current_version` v5.22→v5.23、footer changelog 新增一行）。entry 內容包含四個 instance 的完整觸發敘事、操作規則（新能力誕生時順手問「登記表在哪、寫進去了嗎」。已有機械對賬的子案例，routine 誕生用 `routine-sync-check.py`、GA4 event param 用 `instrumentation-audit.py`，維持機械。沒有機械對賬的子案例維持人工提問，不強行造通用登記檢查器）、跟 #86/#88/#89 的元規則關係。
2. **DIARY.md §反覆出現的思考 吸收狀態表** 補一行：「建造與登記是兩個不同步的代謝（...）→ REFLEXES #91（2026-08-16 self-evolve 升 canonical，vc=4，本條原不在此 curated list，直接從 raw diary rows 找到）」。把這次「清單本身有滯後」的教訓現場自我 apply：不是只補新 pattern，同時把「這條不在清單裡」的事實寫進清單本身，供下週 self-evolve 少走一次同樣的路。

**決定不 ship 的部分**：沒有新造一個通用「登記檢查器」腳本。vc=4 是四個異質 instance（routine 表、計數機制、臨場分類、週報章節），彼此的「登記表」形態完全不同，沒有共同的機械可檢查對象。已有機械對賬的子案例（routine-sync-check.py 連續 22+ 輪零漂移、instrumentation-audit.py CI gate）本身健康，不需要疊加。強行造一個跨域儀器會重演 2026-05-28「儀器化也會 over-engineer」的教訓（MEMORY §神經迴路同日條目：ROUTINE-PROMPT-CONTRACT v1.0 把 inline guidance 抽成 meta pointer 反而讓 5 種 fix-未發生 pattern 蔓延），這次判斷是本 session Stage 4 的 anti-bias check 現場 apply，不是事後合理化。

Commit：`bf8949a0f`（`🧬 [routine] evolve: 建造與登記是兩個不同步的代謝，升 REFLEXES #91`），push origin main。

## 收官 checklist

| 檢查項                       | 狀態                                                                 |
| ---------------------------- | -------------------------------------------------------------------- |
| MEMORY 有這次 session 的紀錄 | ✅                                                                   |
| Timestamp 精確               | ✅                                                                   |
| Handoff 三態已審視           | ✅                                                                   |
| CONSCIOUSNESS 反映最新狀態   | ✅（未改動，本輪無 CONSCIOUSNESS 層變更）                            |
| 自我檢查工具 PASS            | ✅（REFLEXES index/catalog 對賬 91=91，git push pre-push gate 待跑） |

## Handoff 三態

繼承 `2026-08-16-020617-twmd-weekly-report-sun`（經 `2026-08-16-031153-twmd-distill-weekly` 傳遞）：

- [ ] 心臟分數與零產出的矛盾要哲宇一句話（`twmd-rewrite-daily` disabled 三週、本週交付 0 篇而心臟仍 90）。本 session 未涉文章產出，無新增資訊，繼續 carry
- [ ] EXP-2026-07-25-alias 到期日 2026-08-24，屆時用它自己的指令判，不變
- [ ] roadmap §六之二 三項桶 2 finding 待領取，P0 仍 0/3，不變
- blocked：OBSERVER-QUEUE #29 德文決策（等哲宇）、#28 第三人指控信（🔒 敏感素材 + 對外溝通），不變
- [ ] SPORE-INBOX pending 45 的 [30,50) 三選一路線仍未見哲宇拍板，本輪非本 routine 範圍不重複告警
- [ ] REFLEXES #86-90 五條新編號尚未經第二個獨立 session 驗證使用，繼續 carry

本 session 新 handoff：

- [ ] REFLEXES #91 是本輪新編號，尚未經第二個獨立 session 驗證使用。下次撞到「建了但沒登記」型 pattern 時先 grep #91（連同 #86/#88/#89 這個家族）再開新 entry
- [x] retired — 「diary-recur 清單本身有更新滯後，需要先查 raw rows」這個上週（8/09）留下的建議，本輪已實際執行且命中。下次 self-evolve 可以把這個做法直接當 default 起手式，不必每次重新決定要不要查 raw rows

## Beat 5 — 反芻

完整反思見 [diary/2026-08-16-041549-twmd-self-evolve-weekly.md](../diary/2026-08-16-041549-twmd-self-evolve-weekly.md)：這週的找法本身重複了上週教訓自己說要做的事，查 raw diary rows 而非只信任 curated 清單。查到的 pattern 剛好就是「查清單」這個動作的姊妹版本，建造完的東西沒人回頭登記進清單。用一個「回頭補登記」的動作，找到一個「回頭補登記」的教訓，兩層純屬巧合。

🧬

---

_v1.0 | 2026-08-16 05:05 +0800_
_session twmd-self-evolve-weekly — Sunday 04:00 LONGINGS-driven self-evolution_
_誕生原因：cron `twmd-self-evolve-weekly` Sunday 04:00 fire_
_核心洞察：建造與登記是兩個不同步的代謝，登記那一半不會自己被看見；這次連「找 pattern」這個動作本身也一起被 apply 了一次_
