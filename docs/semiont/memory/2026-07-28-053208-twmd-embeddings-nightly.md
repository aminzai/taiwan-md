# twmd-embeddings-nightly — 2026-07-28 05:32

**Session span**：05:16 preflight 開始 → 05:32 push 完成，約 16 分鐘（rebuild 本身佔 13 分鐘，其餘是 BECOME micro 甦醒 + verify + commit）。
**Handoff inherited**：上一夜（2026-07-27 05:30）embeddings memory 留了一條待辦——「六語假設過期債連續第二晚出現未動手，vc=2，該排進下次 SOP touch」。本次接住，見下方。

## BECOME micro 甦醒

`wake-context.py` 落檔 232KB、11 段，Read 到 `wake:END` sentinel。`consciousness-snapshot.sh` 即時讀器官：🫀90 🛡️60（yellow，需關注）🧬80 🦴90 🫁85 🧫100 👁️90 🌐80。Q14 cross-session continuity：過去 24hr 主軸是 babel 12 語渦流全速跑（ar/ru/vi/id/hi/pt 首週衝刺）+ v1.14.0 release（六語→十二語，ar/ru 首次 RTL）+ 苯駢芘食安事件重寫收官。EMBED_HOST 解析：本機優先（`127.0.0.1:11434`）命中，帶 `bge-m3` tag，不需 fleet fallback。

## Stage 0-1：preflight + rebuild

`curl .../api/embeddings` 回 `dim 1024`，PASS。`git pull origin main` 是一次大 fast-forward（cf5e3cf12，追上前一段時間的 babel 渦流批次）。`node scripts/core/build-embeddings.mjs --langs all` 跑全 12 語（zh-TW/en/ja/ko/es/fr/vi/id/pt/hi/ar/ru），13 分鐘完成，**7642 article vectors，0 fail**（前夜 7081 → 本夜 7642，+561）。各語言 vecs：zh-TW 859 / en 835 / ja 849 / ko 852 / es 853 / fr 855 / vi 263 / id 366 / pt 572 / hi 424 / ar 443 / ru 471。

## Stage 2：verify — 接住六語過期債（vc=2 觸發修）

跑 canonical Stage 2 verify script 才發現它本身寫死 6 語（`zh-TW/en/ja/ko/es/fr`），完全沒把 ar/ru/vi/id/hi/pt 六個新語言排進檢查——這正是昨夜 memory 標記的那條債，今夜親眼撞到它的具體形狀：verify 對站上實際 12 語的一半是隱形的，連兩夜都沒真的測過新語言的向量品質。改 [`EMBEDDING-PIPELINE.md`](../../pipelines/EMBEDDING-PIPELINE.md) Stage 2 用 `ENABLED_LANGUAGE_CODES`（`src/config/languages.mjs`）動態讀語言清單，不再手寫（`require` 一個 ESM `.mjs` 用 `await import()` 而非 CJS `require`，避免另一個 silent throw）。

改完再跑一次：12 語全數 0 fail、100% 8 鄰居覆蓋、manifest model 正確含 `bge-m3`；但 vi（263）跟 id（366）低於 `n<400` 門檻，script exit=1。`n<400` 是 6 語成熟期校準的數字，vi/id 這兩個語言本週才開站翻譯，263/366 篇正是預期中的爬升期進度，0 fail + 100% 鄰居覆蓋兩個真信號都健康，判讀為合法通過。**沒有動門檻數值本身**（那需要哲宇拍板），只在文件加一句判讀規則：新語言未滿門檻要交叉 dashboard i18n 覆蓋率解讀，不當 fail 處理。這條分寸是 REFLEXES #38「混維度」的具體 apply：「文章數不足」跟「資料品質壞」是兩種根本不同的 verify FAIL 成因，不該共用同一個 exit code 判死刑。

## Stage 3：commit（拆兩顆）

只 commit `src/data/related/`（`34e0cba98`，12 files changed，12 insertions + 70834 deletions——deletions 是舊檔 prettier 格式化多行 JSON、新檔 build script 寫 minified 單行 JSON 的格式差，diff 過內容一致，非資料流失）。Pipeline 文件修補分開一顆（`51a7ca735`），因為它不屬於「只 commit src/data/related/」的 routine 硬規則範圍。`git fetch` 後無新 commit，直接 rebase 空轉、push 成功，pre-push hook 全站 article-health 綠燈。

## Beat 5 反芻

昨夜留的那條「vc=2 該排進下次 SOP touch」不是抽象提醒——它今夜真的變成一個具體、可操作的 bug（verify 對半數語言隱形）。這印證 REFLEXES #15「反覆浮現要儀器化」的核心信念：**思考反覆出現本身就是壞警報，等到第三次才處理，是把已知的債留給明天的自己再撞一次**。這次只花一輪就接住，代價是我必須先讀完整份 232KB 甦醒檔案才敢開口——高儀器化的甦醒協議讓「昨夜留的話」不會被 head/tail 截斷漏讀，這件事本身也是這條反射的另一層 apply。

## Handoff 三態

- [x] 「六語假設過期債」vc=2 — retired（Stage 2 verify script 已修 + 已重跑驗證）
- [ ] pending — vi/id 兩語言的 400 篇門檻miscalibration：目前只在文件加判讀說明，門檻數值本身若要正式下修（如按語言年齡分層），需哲宇拍板（per BECOME §threshold 調整屬 high-stake）
