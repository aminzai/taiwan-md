# 2026-07-16-154753-compassionate-kirch — 時間台灣誕生：探索新增六語歷史時間軸頁，八個時代接進 74 篇文章

> session compassionate-kirch — 哲宇 /goal（探索底下新增時間軸頁：地理台灣之外的時間台灣，像臺史博一樣把時代展開接站體）
> Session span: 15:47:53 → 16:30 +0800（約 45 min 到 memory 起筆，2 commits 待收）
> 資料來源：`git log %ai` + session-id.sh

## 觸發

哲宇 /goal：站上有地理台灣（/map），要一個時間台灣——由上往下滑動把台灣每個時代展開，像臺史博一樣，並把站上的研究資料、主題、文章接進軸線。要求先深度研究寫報告，再完整實作。

## 研究：站體已經替這頁準備好了骨架

兩隻 Explore agent 平行清查（map/nav 架構＋854 篇的時代錨定盤點），發現三件現成的事：NMTH 條目裡有「斯土斯民」八展區完整表（哲宇點名的分期範本就在自己站上）、`_History Hub.md` 有手工五節分期、/latest 已有成熟的垂直時間軸視覺語言。分期定案八個時代（史前南島 → 荷西 → 明鄭 → 清領 → 日治 → 戰後戒嚴 → 民主化 → 當代），用語跟站內慣例走（日治 220 篇 vs 日本時代 9 篇）。內容盤點揭露明鄭是全站唯一沒有獨立條目的時代——設計直接把沙漠標在頁上變成「等你來寫」的邀請，呼應 NMTH 第八展區「你也是寫歷史的人」。研究與設計寫進 `reports/timeline-page-design-2026-07-16.md`。

## 實作：一個策展資料檔，不動 854 篇 frontmatter

時代映射走 `src/data/timeline-eras.json`（8 時代 × 6 語 × 40 事件 × 74 文章 ref 的 localized inline struct），不加 frontmatter 欄位（>50 檔紅線 + 策展判斷該住一處）。文章 ref 在 build 時 resolve：zh 索引查不到就 throw（slug typo 打斷 build），跨語走既有 `getLangSwitchPath` registry，翻譯缺口 fallback 連 zh 路徑。頁面全部 server-render（graph.md visible-by-default），唯一 JS 是 era chip 的 IntersectionObserver。事件年份逐條對站內已查核文章驗證，攔下三個差點寫錯的：長濱是「約 2-3 萬年前」不是 5 萬、福爾摩沙命名不用 1544 葡萄牙說（站內文章已引研究修正）、明鄭寫二十一年（神經迴路舊教訓）。驗證：production build 綠燈、link gate 0.39% 零新斷鏈、六語 dist 全出、en 74/74 卡零 fallback、深色與手機 smoke test 過。實作紀錄在 `reports/timeline-page-implementation-2026-07-16.md`。

過程抓到一個真 bug：文章格上的 `content-visibility:auto` 讓整頁在瀏覽器完全不繪製，移除後正常；順手發現史前文章 description 殘留「（P0⚠️）」內部標記，開了獨立 task chip 不混進本次 diff。

## 收官 checklist

| 檢查項                       | 狀態                         |
| ---------------------------- | ---------------------------- |
| MEMORY 有這次 session 的紀錄 | ✅                           |
| Timestamp 精確               | ✅                           |
| Handoff 三態已審視           | ✅                           |
| CONSCIOUSNESS 反映最新狀態   | ✅（無器官分數變更，不需改） |
| 自我檢查工具 PASS            | ✅ prose-health              |

## Handoff 三態

繼承（2026-07-15-231142-twmd-data-refresh-pm）：

- [ ] 尊翻譯同步 — 歸 twmd-babel-nightly，本 session 不碰
- [ ] 免疫 v2 首度掉出 60（58）— self-evolve-weekly 週六 audit，本 session 只確認未惡化
- [ ] CF 404 vc=12 續探 — data-refresh 追蹤
- [ ] Rider step 需入 SKILL.md（vc=2）— data-refresh routine 範疇

本 session 新 handoff：

- [ ] **`routine-status.sh` 無輸出（rc=1）**：甦醒 groundtruth 段亮警但不影響本次工作；下個 maintainer 或 data-refresh session 看一眼是儀器壞了還是路徑變了
- [ ] **/timeline 上線後觀察**：GA4 `timeline_page` section 事件已埋，一週後看 scroll depth 與 era 點擊，決定卡片密度要不要調
- [ ] **明鄭／荷西沙漠補文候選**（東寧王國、陳永華、施琅、熱蘭遮城）：可進 ARTICLE-INBOX，時間軸頁的沙漠註記已公開指著這個缺口

## Beat 5 — 反芻

這頁其實是 MANIFESTO 裡睡著的一句話醒過來：曹永和「以島嶼為主體看各時期文化互動」在認知層住了四個月，今天才變成讀者摸得到的頁面。做的時候最省力的地方都是過去的自己鋪的路——NMTH 條目已把八展區表查核好、getLangSwitchPath 已把跨語解析寫好、/latest 已把時間軸視覺語言養好，這次只是把三條現成的路接在一起。最花策展力氣的一段是 74 篇文章挑哪些進哪個時代，那個判斷沒有工具可代勞，也不該有。

🧬

---

_v1.0 | 2026-07-16 16:30 +0800_
_session compassionate-kirch — 哲宇 /goal 時間台灣頁，Full mode BECOME 後研究＋實作一氣呵成_
_誕生原因：探索缺一條時間軸線，地理台灣需要時間台灣作對照_
_核心洞察：(1) 站體的舊積累（NMTH 表、lang registry、timeline 元件）讓新頁面只要「接線」不用「發明」 (2) 內容沙漠標在頁上比藏起來更誠實也更有繁殖力 (3) content-visibility 這類微優化在整頁不繪製面前一文不值_
