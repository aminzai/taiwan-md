# 2026-07-30-093643-twmd-flywheel-watch

✅ BECOME ack: mode=micro / Q14=PASS

routine `twmd-flywheel-watch` @ 09:36，跑在指揮部（commander-macbook）。工作只有一件：從飛輪外面看它還活著沒有。

---

## 判定：飛輪在轉，六條日更全部留痕

`git fetch origin`（不 pull）後跑 `python3 scripts/tools/flywheel-watch.py`，首跑 exit=0 / severity=ok。24 小時窗口（origin/main）commit 161 筆，其中 `[routine]` 標記 12 筆。逐條回 git log 對過訊息，不只讀工具的分類欄：

| 時間  | routine                 | 產出                                                         |
| ----- | ----------------------- | ------------------------------------------------------------ |
| 05:33 | twmd-embeddings-nightly | bge-m3 12 語 8391 向量，0 fail                               |
| 05:38 | twmd-routine-sync       | 17 條全 in-sync，零漂移第五日                                |
| 06:14 | twmd-data-refresh-am    | 14 步全綠，文章 869，live dump rider 例行續跑                |
| 06:43 | twmd-spore-harvest-am   | 6 events，鎢供應鏈觸及 479K 續平                             |
| 07:09 | twmd-feedback-triage    | 隊列空，同步 2 則維護者回覆進 git 主權層                     |
| 08:41 | twmd-maintainer-daily   | 7 個 PR 收 6 個，1 篇超過 50 檔留哲宇拍板，4 篇新美食文 heal |

其餘一百四十多筆是 vortex-babel 產線在指揮部這台連續跑（十語 unified dispatcher 加每小時脈搏快照），不屬 routine 飛輪。

停用中的四條（spore-pick / spore-publish / babel-nightly / rewrite-daily）在 SSOT 都標了 ⏸️，沒有一條被誤報成靜默，這一 cycle 的 SSOT 跟 live 對得上。

maintainer 那篇超過 50 檔的 PR 留給哲宇，是 §自主權邊界 命中時該有的預設姿態（REFLEXES #79），不是拖延。

---

## 工具在量錯層：它讀的是這台多久沒 pull

首跑報 `live 狀態 dump 齡 27.3 小時`，跟 6/14 才跑過 rider 的事實對不起來。追下去發現 origin/main 上的 dump 是今天 06:15 打的，齡 3.3 小時。27.3 小時是本機工作樹那份的齡。

病根在儀器自己的檔頭：它宣告「唯一資訊來源是 `origin/main` 的 commit 紀錄」，實際上四份判斷素材裡只有 commit log 讀 origin，排程表 SSOT、MEMORY 索引、live dump 三份都讀本機工作樹。而這條 routine 的 hard gate 明文禁止 `git pull`（指揮部這台常有平行產線在動工作樹），所以那三份必然落後，落後多久取決於這台上次 pull 是什麼時候。今天工作樹落後 origin 41 個 commit，剛好整整一天。

今天沒越過 48 小時門檻所以沒亮燈。再多落後一天就會對著一個健康的飛輪亮假黃燈，而假黃燈正是 7/28 那盞真黃燈（OBSERVER-QUEUE #22）要人去分辨的東西。7/28 那次查證過是真的（origin 上的 dump 當時確實停在 7/26 02:11），判定沒錯，但用的尺本身站不住。

**修法**：三份素材一律改用 `git show origin/main:` 讀（`read_from_origin`，讀不到才退回工作樹並在 stderr 說一聲）。閾值一個字沒動，改的是讓儀器跟它自己寫在檔頭的契約對齊。

修完 dogfood 一次，當場多還回一把本來就該有的尺：

- `live 狀態 dump 齡 3.3 小時`（原本 27.3）
- **`有動靜（只留收官索引）：twmd-embeddings-nightly, twmd-maintainer-am, twmd-routine-sync`** —— 這三條在修之前完全不出現。第二把尺（MEMORY 索引列的 session-id handle）是 7/26 為了接住「跑完了但 commit 沒帶 taskId」才加的，但它讀的索引在這台永遠慢一天，等於從加進來那天起就沒真的運作過。今天靠第三道退路（commit 內文提到 taskId）才沒誤報。

儀器只看見存在、看不見缺席，這次連「一把尺從沒生效過」也是缺席的一種。對應 REFLEXES #82（訊號別選代理）＋ #69（每層自評都需要外部尺）。

### 順手記一條沒升級的觀察

今天 maintainer 的索引 handle 寫成 `twmd-maintainer-am`，排程器上的 taskId 是 `twmd-maintainer-daily`，兩者對不起來，第二把尺因此接不到它（昨天同一條寫的是 `-daily`）。名字的替身這個家族又出現一次，只是這回發生在寫入端而非讀取端。vc=1 且今天有退路兜住，先記不升級。

---

## Handoff 三態

- [ ] **OBSERVER-QUEUE #22 續 pending**：rider hard gate 仍未進 skill，維持待決不動。但今天要補一句給下一個接手的人：#22 的判準是「dump 是不是 owner 自己打的」，**齡的數字在這台一直是不可信的**，今天才修好。7/27–7/28 那兩次讀數要重新理解為「工作樹落後」加「真的沒跑」兩件事疊在一起
- [ ] **flywheel-watch 第二把尺剛復活，明後天回頭看一次**：`只留收官索引` 那行如果持續有內容，代表尺真的在運作。如果又空了，就是別的地方還在讀舊 ref
- [ ] **給下一個 cycle：收官後工具會把「本條 routine 自己」報成靜默，那不是警報**。改讀 origin 之後，本 cycle 的 commit 要等這台 rebase 完才會到 origin，工具看不到自己剛打的那一筆。這台 main 落後 origin 41 個 commit，平行 babel 產線在動工作樹，這條 routine 不 rebase 也不 push（commit 留著讓下一次 rebase 帶走，昨天那筆就是這樣進 origin 的）。判準：`silent` 裡只有 `twmd-flywheel-watch` 一條 = 綠燈
- 無 blocked

---

_session 2026-07-30-093643-twmd-flywheel-watch — cron @ 09:30 指揮部。不碰營運機排程、不 pull、只 commit 本 routine 自己的三個檔（工作樹有 7 檔 babel 平行產線產出，全程不碰；本機 main 落後 origin 41 個 commit，索引列會跟今天另外六列在 rebase 時同處併入，兩邊都保留）。_
