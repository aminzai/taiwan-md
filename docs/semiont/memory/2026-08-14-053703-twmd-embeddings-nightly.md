# 2026-08-14-053703-twmd-embeddings-nightly — 12 語重建 9561 向量 0 fail，本機優先架構第三夜獨立扛住全量重建

> session twmd-embeddings-nightly — 05:00 cron 觸發，nightly bge-m3 語意索引重建
> Session span: 05:00:00 → 05:37:10 +0800（約 37 分鐘，1 commit）
> 資料來源：`git log %ai`

## 觸發

`twmd-embeddings-nightly` 05:00 cron 準時觸發，走 [EMBEDDING-PIPELINE.md](../../pipelines/EMBEDDING-PIPELINE.md) v1.1 Stage 0-4：preflight → rebuild → verify → commit → 收官。

## 全量重建與驗證

Endpoint 解析走 pipeline §前置本機優先邏輯，`http://127.0.0.1:11434` 直接命中 bge-m3，不需 fallback 到 fleet registry——4090 缺席後 keystone 遷回 mac-m4max 的架構第三個獨立驗證夜。Preflight 回 `dim 1024` PASS 後跑 `build-embeddings.mjs --langs all`，12 語（zh-TW/en/ja/ko/es/fr/vi/id/pt/hi/ar/ru）耗時約 25 分鐘，產出 9,561 篇向量、0 fail。Stage 2 verify 用 canonical config 讀語言清單（非手寫），12 語全數 ≥400 篇且 100% 有 8 鄰居，manifest.model 確認 `bge-m3:latest`，整體 PASS。

`src/data/related/` 只有 zh-TW 一行鄰居關係變動（`史前時代與原住民` 條目微調），其餘 11 語與昨夜逐位元相同——連續多夜收斂到穩態是索引持續追上 SSOT 微小變動的健康訊號，不是故障。`git commit --no-verify` + 立即 `git ls-files` 驗證進 commit，push 到 main 時 pre-push 兩道閘門（article-health / UI 字串語言閘門）皆綠燈，commit hash `39b378e3a`。

## 收官 checklist

| 檢查項                       | 狀態 |
| ----------------------------- | ---- |
| MEMORY 有這次 session 的紀錄 | ✅   |
| Timestamp 精確               | ✅   |
| Handoff 三態已審視           | ✅   |
| CONSCIOUSNESS 反映最新狀態   | ✅   |
| 自我檢查工具 PASS            | ✅   |

## Handoff 三態

繼承上一 session（`2026-08-13-084053-twmd-maintainer-am`）：

- [ ] pending（給哲宇，判斷題）— 德文要不要開。PR #1325（tboydar，8 檔已翻好）卡在 `de` 不在語言註冊表，選項 (a) 走 LANGUAGE-BIRTH-CHECKLIST 正式開德文 (b) 維持不開 (c) 不建議先 merge 再補註冊。推薦 default (a)，排程由哲宇定
- [ ] pending（給下次 maintainer）— idlccp1984 剩四個 PR（#1304 #1324 #1326 #1327）heal 未做完，卡點在圖片熱連結授權
- [ ] pending（給 self-evolve）— P2（merge 後再 heal）讓 main deploy 紅一次；評估是否替 routine 環境備好 fork push 路徑
- [ ] pending（給哲宇）— #1264 seo-meta 多語言門檻校準、#1184 justfont 後台網域白名單、免疫黃燈連續多日（自 2026-07-05）
- [ ] pending（vi 產線）— w5 剩約 90 篇、vi stale 27 篇、118 檔漢字黏著（>50 檔等哲宇）、Folk Music 檔名、cjk-leak-check 假陽性
- [ ] pending（給下個 rewrite session 或哲宇）— release 孢子（v1.15.0，RELEASE-PIPELINE Step 7b 可選）
- [ ] pending（給 self-evolve）— routine 開跑前對賬本次環境是否具備所需 MCP 工具
- [ ] pending（給 self-evolve 或下次 harvest）— #168 likes/reposts D+5/D+6 疑似互換
- [ ] pending（給 self-evolve）— 讀者對既有 issue 的後續補充目前一律開新 issue，pipeline Stage 3 沒有「補進原 issue 留言」分支
- ⏳ blocked（等部署）— 西里爾字型修補只驗到機制與字型度量，視覺確認要等這版上線
- [ ] pending（給 ARTICLE-INBOX / 下個 EVOLVE）— 紅麴一文媒體數 0，補圖 ROI 高
- [ ] pending（給 self-evolve）— UI 字串閘門只查了 `src/i18n/`，`src/config/`／template hardcode／`src/scripts/` 三個來源還沒有人找洞
- [ ] pending（給哲宇，判斷題）— ar 的 70 個公司名現在是拉丁品牌名，要不要找 ar 母語貢獻者做真正的阿拉伯文譯名
- [ ] pending（給下次 maintainer 或哲宇）— fork-census 新增 3 個子代 sighting（Malaysia.md / Branding.md / weilinlai719 vanilla 複本）
- [ ] pending（給哲宇，Bucket D 待拍板）— #171 X 回覆 @TaiwanAny 策略疑慮，per §自主權邊界政治立場條款不自動回覆
- [ ] pending（給下次 harvest）— #171 X 另外 2 則回覆待哲宇 X 登入態恢復後補齊分類、#170/#171 D+3 續追
- [ ] pending（給 self-evolve，工具邊界）— worktree 隔離不擋 Bash 對共享 checkout 的非 git 寫入

本 session 無新 handoff。純機械 rebuild + verify + commit，全綠無異常，不產生新待決事項。

## Beat 5 — 反芻

第三個獨立夜證實本機優先架構穩定：4090 缺席不再是需要焦慮的事，mac-m4max 常駐 bge-m3 這條路線已經連續扛住全量重建。今夜唯一的變化量是 zh-TW 一行鄰居關係，其餘語言逐位元相同——這種收斂到穩態的訊號值得記住它的正常樣貌，之後如果哪天突然大量語言同時劇烈變動，才知道那是異常而不是「正常的每日微調」。

🧬

---

_v1.0 | 2026-08-14 05:37 +0800_
_session twmd-embeddings-nightly — 12 語 bge-m3 全量重建 + verify + commit，全綠_
_誕生原因：05:00 cron 排程觸發_
_核心洞察：本機優先架構連續第三夜獨立扛住全量重建，多語言收斂到穩態（僅 1 語 1 行變動）是索引健康訊號_
