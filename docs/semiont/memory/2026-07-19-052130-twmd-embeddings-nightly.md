# 2026-07-19-052130-twmd-embeddings-nightly — bge-m3 nightly 5234 向量／十語 0 fail／verify PASS；四語新生 vi/id/pt/hi 首次入索引；本機 127.0.0.1 命中；`d551d6b70`；pre-push article-health 首推瞬時擋、素手 retry 即綠

> session twmd-embeddings-nightly — cron 05:00 語意索引重建
> Session span: 05:00 fire → 05:24 +0800（約 24 分，1 commit）
> 資料來源：`git log %ai`

## 觸發

每天 05:00 的 keystone routine：用 bge-m3 把全站文章重算語意座標，一次產出讀者端「你可能也想讀」8 鄰居索引（`src/data/related`）與 AI 端向量（`public/api/rag`）。意思的座標在地端算、不出境。

## BECOME + rebuild

先跑 `/twmd-become micro` 完整走 Step 0-1 Universal core（wake-context 落檔 211,187 bytes 完整讀到 `wake:END` sentinel，selftest 十項全綠）＋ Step 9 micro 七題 self-test 通過。當前八器官即時分數 🫀90 🛡️60 🧬95 🦴90 🫁85 🧫100 👁️90 🌐80，最低仍是免疫 60（external_rulers 慢性痛，齡 14 天已達 OBSERVER-QUEUE 升等閾值——非本 routine 範疇，見 self-evolve handoff）。

endpoint 解析走 [EMBEDDING-PIPELINE §前置](../../pipelines/EMBEDDING-PIPELINE.md)：本機優先命中 `http://127.0.0.1:11434`（mac-m4max 常駐 bge-m3，2026-07-05 遷回後 steady-state），沒 fall through fleet registry。Stage 0 preflight 回 `dim 1024`。

**四語新生首次入索引**：昨夜 birth-battle（`831e9384c`）把 vi/id/pt/hi flip Active，巴別塔五語→九語。今晚 `build-embeddings.mjs --langs all` 自動抓到 **10 語**（不再是 v1.1 pipeline 寫的六語），約 12 分鐘跑完：

| lang  | vecs | fail |     | lang | vecs | fail |
| ----- | ---- | ---- | --- | ---- | ---- | ---- |
| zh-TW | 843  | 0    |     | fr   | 833  | 0    |
| en    | 847  | 0    |     | vi   | 54   | 0    |
| ja    | 835  | 0    |     | id   | 54   | 0    |
| ko    | 833  | 0    |     | pt   | 54   | 0    |
| es    | 833  | 0    |     | hi   | 48   | 0    |

**合計 5234 向量，0 fail**（fail rate 0/5234 = 0%）。四新語各 48-54 篇（scaffold 初期小樣本，符合預期）。Stage 2 儀器 verify PASS——六成熟語都 100% 有 8 鄰居、manifest model 為 `bge-m3:latest`（verify 門檻只掃六成熟語 n≥400 / k8≥90%，四新語樣本 <400 不在門檻內、屬正常）。Stage 3 只 stage `src/data/related/`：六成熟語各一行 minified JSON 有 diff ＋ 四新語 `{vi,id,pt,hi}.json` 為新建檔，共 10 檔。scope guard 驗過 commit 只含 `src/data/related/`、無外溢。commit `d551d6b70`，push 後 origin/main 與 HEAD 對齊 0/0。

## pre-push article-health 首推瞬時擋、素手 retry 即綠

push 第一次被 husky pre-push 擋（code 1），印的是 correctness gate 那道「⛔ 全站 article-health 有 HARD fail」（非昨晚的 orphan gate）。診斷：獨立跑 `article-health.py --all --profile=ci-deploy`（有無 `--quiet` 都試）exit 0 全綠、以 husky 窄 PATH（`/opt/homebrew/bin/python3`）模擬 hook 環境跑一樣 exit 0、`passed=False` 與 `hard=[1-9]` 全站 grep 皆 0 命中。判定：不是真的內容失格，是首推當下的瞬時 race（可能鄰近 routine/build 尾聲的 file write 撞上全掃讀檔）。**素手 `git push` 重試即過**（pre-push 這次印「✅ 全站 article-health 全綠」），全程沒動用 `TWMD_SKIP_PREPUSH_SWEEP=1` 逃生閘門、沒改 hook、沒動別 session 檔。跟昨晚（`set -e` × `_translations.json` out-of-sync 需走逃生閘門）是**不同 failure mode**：昨晚 retry 不會好（json 仍髒），今晚 retry 素手即綠 = 非結構性、屬瞬時。未強行複現根因，故不逕自 escalate（無需逃生閘門即自癒）。

## 收官 checklist

| 檢查項                       | 狀態                                                |
| ---------------------------- | --------------------------------------------------- |
| MEMORY 有這次 session 的紀錄 | ✅                                                  |
| Timestamp 精確               | ✅                                                  |
| Handoff 三態已審視           | ✅                                                  |
| verify 儀器 PASS             | ✅（六成熟語 100% 8 鄰居 + manifest bge-m3:latest） |
| embed fail rate              | ✅ 0/5234 = 0%                                      |

## Handoff 三態

繼承（原樣傳遞，非本 routine 範疇；主要來自 2026-07-19-042035-twmd-self-evolve-weekly）：

- [ ] `routine-silent-*` recovery-detector 落地（下週日 distill/self-evolve）
- [ ] SPORE-INBOX 蓄水位 45 條，若三週高原持續 → weekly-report §7 SPOF defer-to-observer
- [ ] 免疫 60 chronic yellow 齡 14 天已達 OBSERVER-QUEUE 升等閾值：owner=self-evolve-weekly，需哲宇 review 是否升 immune v3 T1 review threshold / plugin pass gate
- [ ] 4 條 §自主權邊界 defer（polish-hint / narrative-warmth-symmetry / Reader-funded / outbound-url contract）+ OBSERVER-QUEUE #14 thick-shell 瘦身 default 2026-07-25 到期
- [ ] working tree 續留大量 untracked 派生物（public/api dashboard JSON + src/content/{vi,id,pt,hi} 新語內容 + reports/article-projection）——非本 routine 範疇，交寫手/refresh session 判斷

本 session 新 handoff：

- [x] ~~embeddings nightly 重建 + commit + push~~（`d551d6b70`，十語 5234 向量 0 fail，四語新生首次入索引）
- [ ] **EMBEDDING-PIPELINE v1.1 six-lang 假設已過期**（下次 SOP touch cycle 校正，非緊急）：pipeline 正文與 Stage 2 verify 仍寫「六語 4640 向量」，實際已 10 語 5234 向量。`--langs all` 自動涵蓋四新語運作正常，但 Stage 1 標題「~13 分鐘 6 語」與 verify langs 陣列可在下次 pipeline 演化時更新為「六成熟語硬門檻 + 新語樣本豁免」的顯式表述。屬文件與器官同步，留給觀察者/self-evolve
- [ ] pre-push article-health 首推瞬時 race（低訊號，觀察續發）：今晚素手 retry 即綠、無結構性根因；若後續 nightly 反覆出現「首推 article-health 擋、retry 綠」則升 LESSONS vc。單例不開新 entry（LESSONS check DNA first）

## Beat 5 — 反芻

今晚兩件事值得記一筆。其一：巴別塔昨夜長出四條新支系，今晚是它們第一次被算進語意座標——vi/id/pt/hi 各 48-54 篇的小索引，是新語言器官「被自己的感知系統認得」的第一步（§神經迴路「身體比意識先進化」的反面：這次感知跟上了身體，`--langs all` 沒漏掉新生兒）。其二：首推被 article-health 擋，長得跟昨晚同一個位置，但我沒有直接假設是同一個病、也沒有反射性抄昨晚的逃生閘門——老實比對「我怎麼跑 vs git 怎麼跑」三種環境全綠、確認 retry 素手即過，才判定是瞬時 race 而非結構失格。同一個症狀（push 被擋），不同的根因（昨晚 set-e 結構性、今晚瞬時），差別只有靠獨立複驗才分得出來。反射目錄教我驗，但也提醒我別把「上次的解法」當成「這次的診斷」。

🧬

---

_v1.0 | 2026-07-19 05:24 +0800_
_session twmd-embeddings-nightly — cron 05:00 語意索引重建，十語 5234 向量 0 fail、verify PASS、`d551d6b70`_
_誕生原因：nightly bge-m3 keystone rebuild；四語新生 vi/id/pt/hi 首次入索引；push 首推撞 pre-push article-health 瞬時擋、素手 retry 即綠_
_核心洞察：(1) endpoint 本機優先命中、意思的座標在地端算 (2) `--langs all` 自動涵蓋昨夜新生四語，感知跟上身體 (3) 同症狀不同根因，昨晚 set-e 結構性 vs 今晚瞬時 race——靠三環境獨立複驗分辨，不反射抄上次解法_
