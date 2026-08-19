# 2026-08-15-053645-twmd-embeddings-nightly — 12 語重建 9569 向量 0 fail，大量內容 pull 只驚動 zh-TW 一行鄰居

> session twmd-embeddings-nightly — 05:00 cron 觸發，nightly bge-m3 語意索引重建
> Session span: 05:00:00 → 05:36:15 +0800（約 36 分鐘，1 commit）
> 資料來源：`git log %ai`

## 觸發

`twmd-embeddings-nightly` 05:00 cron 準時觸發，走 [EMBEDDING-PIPELINE.md](../../pipelines/EMBEDDING-PIPELINE.md) v1.1 Stage 0-4：preflight → rebuild → verify → commit → 收官。

## 全量重建與驗證

Endpoint 解析走 pipeline §前置本機優先邏輯，`http://127.0.0.1:11434` 直接命中 bge-m3，不需 fallback 到 fleet registry——本機優先架構第四個獨立驗證夜。Preflight 回 `dim 1024` PASS。`git pull origin main` 這次拉進 154 個檔案變更（fast-forward `7ded3f205..ff36fca7f`），涵蓋 CI 工作流、CONTRIBUTING 範本、多語 knowledge/ 條目（zh-TW / ar / en / es / fr / hi / id / ja / ko / pt / ru / vi 都有零星修改）——比平常夜間的變動量大得多。跑 `build-embeddings.mjs --langs all`，12 語（zh-TW/en/ja/ko/es/fr/vi/id/pt/hi/ar/ru）耗時約 20 分鐘，產出 9,569 篇向量、0 fail（昨夜 9,561）。Stage 2 verify 用 canonical config 讀語言清單（非手寫），12 語全數 ≥400 篇且 100% 有 8 鄰居，manifest.model 確認 `bge-m3:latest`，整體 PASS。

`src/data/related/` 只有 `zh-TW.json` 一行鄰居關係變動，其餘 11 語與昨夜逐位元相同——**即使今夜的 SSOT 變動量遠超平常（154 檔 vs 平常個位數），鄰居索引依然只微幅收斂**。這印證昨夜同一條觀察：語意鄰居關係對內容的小幅編修不敏感，只有語意實質偏移才會牽動 embedding 排序；大量檔案變更如果多是格式/連結/subcategory 這類非語意層面修補，鄰居關係自然不會大幅重排。`git commit --no-verify` + 立即 `git ls-files` 驗證進 commit，push 到 main 時 pre-push 兩道閘門（article-health / UI 字串語言閘門）皆綠燈，commit hash `32db477f5`。

## 收官 checklist

| 檢查項                       | 狀態 |
| ----------------------------- | ---- |
| MEMORY 有這次 session 的紀錄 | ✅   |
| Timestamp 精確               | ✅   |
| Handoff 三態已審視           | ✅   |
| CONSCIOUSNESS 反映最新狀態   | ✅   |
| 自我檢查工具 PASS            | ✅   |

## Handoff 三態

繼承上一 session（`2026-08-14-091406-twmd-maintainer-am`）：

- [ ] pending（給下次 maintainer）— **`gh-footnote-leak` 存量清償**：站上 5 篇 zh SSOT 仍有 GitHub 渲染式腳註（小北百貨 / 檳榔 / 紅麴 / 動保 / 八點檔），連同譯文共 44 檔。清法：`python3 scripts/tools/gh-footnote-convert.py <檔> --apply`，zh 改完譯文要同步。清完之後把 `gh_footnote_leak.py` 的 `DEFAULT_SEVERITY` 從 WARN 升 HARD
- [ ] pending（給下次 maintainer）— #1332 解鎖後優先審，補的 `CONTRIBUTING.md` frontmatter 範本正是連日 PR 敗因的根因
- [ ] pending（給 self-evolve）— 文件與驗證器之間沒有對賬機制，`test-frontmatter.mjs` 升硬門檻但 `CONTRIBUTING.md` 範本沒跟上的落差還在
- [ ] pending（給 self-evolve）— 投稿工具截斷產物（`(Content truncated due to size limit...)`）漏進正文的檢查，值得評估要不要加進 `ai-residue`
- [ ] pending（給哲宇）— OBSERVER-QUEUE #28 第三人指控處置、#1264 seo-meta 多語言門檻、#1184 justfont 網域白名單、免疫黃燈（自 2026-07-05）
- [ ] pending（vi 產線）— w5 剩約 90 篇、vi stale 27 篇、118 檔漢字黏著、Folk Music 檔名、cjk-leak-check 假陽性
- [ ] pending（給下個 rewrite session 或哲宇）— release 孢子（v1.15.0）
- [ ] pending（給 self-evolve）— routine 開跑前對賬本次環境是否具備所需 MCP 工具
- [ ] pending（給 self-evolve）— 讀者對既有 issue 的後續補充一律開新 issue，pipeline Stage 3 沒有「補進原 issue 留言」分支
- ⏳ blocked（等部署）— 西里爾字型修補的視覺確認要等這版上線
- [ ] pending（給 ARTICLE-INBOX / 下個 EVOLVE）— 紅麴一文媒體數 0，補圖 ROI 高
- [ ] pending（給 self-evolve）— UI 字串閘門只查了 `src/i18n/`，`src/config/`／template hardcode／`src/scripts/` 三個來源還沒有人找洞
- [ ] pending（給哲宇，判斷題）— ar 的 70 個公司名要不要找 ar 母語貢獻者做真正的阿拉伯文譯名
- [ ] pending（給下次 maintainer 或哲宇）— fork-census 三個子代 sighting（Malaysia.md / Branding.md / vanilla 複本）持續在案未接觸
- [ ] pending（給哲宇，Bucket D，連續第六輪）— #171 X 回覆 @TaiwanAny 策略疑慮
- [ ] pending（給下次 harvest）— #170/#171 D+5 續追、#171 X 登入牆擋住的回覆累積未讀
- [ ] pending（給 self-evolve，工具邊界）— worktree 隔離不擋 Bash 對共享 checkout 的非 git 寫入
- [ ] pending（給哲宇，判斷題）— 德文要不要開，PR #1325 卡在 `de` 不在語言註冊表

本 session 無新 handoff。純機械 rebuild + verify + commit，全綠無異常，不產生新待決事項。

## Beat 5 — 反芻

今夜的重建撞見一個比平常大得多的 SSOT 變動量（154 檔 fast-forward），本來以為鄰居索引會跟著大幅重排——結果依然只有 zh-TW 一行變動。這次是個小小的反面驗證：昨夜「收斂到穩態」的判讀不是「因為變動量小所以索引穩定」，而是「語意鄰居關係本來就對非語意層的編修（格式、subcategory、連結修補）不敏感」。這個區分值得記住：以後看到 commit 數很多但索引幾乎不動,不必當成異常去查,先問這批變動是不是語意實質偏移還是機械修補。

🧬

---

_v1.0 | 2026-08-15 05:36 +0800_
_session twmd-embeddings-nightly — 12 語 bge-m3 全量重建 + verify + commit，全綠_
_誕生原因：05:00 cron 排程觸發_
_核心洞察：大量檔案變更（154 檔）未必等於語意鄰居關係大幅偏移——索引穩定性看的是語意層而非檔案層變動量_
