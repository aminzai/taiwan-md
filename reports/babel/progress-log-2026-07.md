# 巴別塔同步進度日誌

> 每次更新增補一段（producer: `progress-snapshot.py`，資料源同目錄 `progress-*.jsonl`）。fresh=最新 / stale=可讀待刷新 / missing=無頁面。

## 2026-07-24T17:43:00+08:00（zh 總數 862）

| 語言 | fresh | stale | missing | 覆蓋率 | Δfresh | Δmissing |
| ---- | ----: | ----: | ------: | -----: | -----: | -------: |
| en   |   715 |   119 |      28 |  96.8% |      — |        — |
| ja   |   700 |   156 |       6 |  99.3% |      — |        — |
| ko   |   700 |   159 |       3 |  99.7% |      — |        — |
| es   |   704 |   154 |       4 |  99.5% |      — |        — |
| fr   |   701 |   161 |       0 | 100.0% |      — |        — |
| vi   |    45 |    11 |     806 |   6.5% |      — |        — |
| id   |    54 |    13 |     795 |   7.8% |      — |        — |
| pt   |    38 |    15 |     809 |   6.1% |      — |        — |
| hi   |    36 |    13 |     813 |   5.7% |      — |        — |

總缺口（stale+missing）：**4065**

產線：run-p1-v3（mac qwen35b classic 五語）＋ fleet 3090（id/hi）＋ 4090（vi/pt）三條 bash dispatcher。

## 2026-07-24T18:07:00+08:00（zh 總數 862）

| 語言 | fresh | stale | missing | 覆蓋率 | Δfresh | Δmissing |
| ---- | ----: | ----: | ------: | -----: | -----: | -------: |
| en   |   716 |   112 |      34 |  96.1% |     +1 |       +6 |
| ja   |   700 |   156 |       6 |  99.3% |      · |        · |
| ko   |   700 |   159 |       3 |  99.7% |      · |        · |
| es   |   704 |   154 |       4 |  99.5% |      · |        · |
| fr   |   701 |   161 |       0 | 100.0% |      · |        · |
| vi   |    43 |    11 |     808 |   6.3% |     -2 |       +2 |
| id   |    55 |    13 |     794 |   7.9% |     +1 |       -1 |
| pt   |    38 |    15 |     809 |   6.1% |      · |        · |
| hi   |    36 |    13 |     813 |   5.7% |      · |        · |

總缺口（stale+missing）：**4065**（＝0 vs 上一筆）

## 2026-07-24T21:24:00+08:00（zh 總數 862）

| 語言 | fresh | stale | missing | 覆蓋率 | Δfresh | Δmissing |
| ---- | ----: | ----: | ------: | -----: | -----: | -------: |
| en   |   724 |   104 |      34 |  96.1% |     +8 |        · |
| ja   |   700 |   156 |       6 |  99.3% |      · |        · |
| ko   |   700 |   159 |       3 |  99.7% |      · |        · |
| es   |   704 |   155 |       3 |  99.7% |      · |       -1 |
| fr   |   701 |   161 |       0 | 100.0% |      · |        · |
| vi   |    55 |    16 |     791 |   8.2% |    +12 |      -17 |
| id   |    63 |    12 |     787 |   8.7% |     +8 |       -7 |
| pt   |    40 |    16 |     806 |   6.5% |     +2 |       -3 |
| hi   |    38 |    13 |     811 |   5.9% |     +2 |       -2 |

總缺口（stale+missing）：**4033**（▼32 vs 上一筆）

hreflang 九語修復＋Politics registry 修復 push（087570575）；免費模型校準 5/10 過（nemotron-550b/gemma-4-31b/laguna-xs/gpt-oss-20b/north-mini-code）。

## 2026-07-24T22:00:00+08:00（zh 總數 862）

| 語言 | fresh | stale | missing | 覆蓋率 | Δfresh | Δmissing |
| ---- | ----: | ----: | ------: | -----: | -----: | -------: |
| en   |   724 |   104 |      34 |  96.1% |      · |        · |
| ja   |   700 |   156 |       6 |  99.3% |      · |        · |
| ko   |   700 |   159 |       3 |  99.7% |      · |        · |
| es   |   704 |   155 |       3 |  99.7% |      · |        · |
| fr   |   701 |   161 |       0 | 100.0% |      · |        · |
| vi   |    55 |    16 |     791 |   8.2% |      · |        · |
| id   |    64 |    14 |     784 |   9.0% |     +1 |       -3 |
| pt   |    44 |    16 |     802 |   7.0% |     +4 |       -4 |
| hi   |    48 |    12 |     802 |   7.0% |    +10 |       -9 |

總缺口（stale+missing）：**4018**（▼15 vs 上一筆）

babel-dispatch.py 統一調度器上線：classic 線汰換 bash、另開雲端 free-model track；en 誤殺救回 49 篇；cjk-leak-check 全形括號假陽性修復。

## 2026-07-24T22:17:07+08:00（zh 總數 862）

| 語言 | fresh | stale | missing | 覆蓋率 | Δfresh | Δmissing |
| ---- | ----: | ----: | ------: | -----: | -----: | -------: |
| en   |   724 |   104 |      34 |  96.1% |      · |        · |
| ja   |   700 |   156 |       6 |  99.3% |      · |        · |
| ko   |   700 |   159 |       3 |  99.7% |      · |        · |
| es   |   704 |   155 |       3 |  99.7% |      · |        · |
| fr   |   701 |   161 |       0 | 100.0% |      · |        · |
| vi   |    55 |    16 |     791 |   8.2% |      · |        · |
| id   |    65 |    14 |     783 |   9.2% |     +1 |       -1 |
| pt   |    45 |    15 |     802 |   7.0% |     +1 |        · |
| hi   |    44 |    12 |     806 |   6.5% |     -4 |       +4 |

總缺口（stale+missing）：**4020**（▲2 vs 上一筆）

ja/ko marker 假陽性家族修復（的/了/一個/淘汰 出表＋引述豁免）；existence-aware redirects 讓 CI 復綠。

## 2026-07-24T22:20:32+08:00（zh 總數 862）

| 語言 | fresh | stale | missing | 覆蓋率 | Δfresh | Δmissing |
| ---- | ----: | ----: | ------: | -----: | -----: | -------: |
| en   |   724 |   104 |      34 |  96.1% |      · |        · |
| ja   |   700 |   156 |       6 |  99.3% |      · |        · |
| ko   |   700 |   159 |       3 |  99.7% |      · |        · |
| es   |   704 |   155 |       3 |  99.7% |      · |        · |
| fr   |   701 |   161 |       0 | 100.0% |      · |        · |
| vi   |    55 |    16 |     791 |   8.2% |      · |        · |
| id   |    65 |    14 |     783 |   9.2% |      · |        · |
| pt   |    47 |    15 |     800 |   7.2% |     +2 |       -2 |
| hi   |    47 |    11 |     804 |   6.7% |     +3 |       -2 |

總缺口（stale+missing）：**4015**（▼5 vs 上一筆）

產線：classic 92129（qwen35b 五語）＋ fleet 3090/4090 ＋ 雲端 roster（nemo 14 ok 主力、laguna 3 ok、gemma31 429 全凍）；書名號豁免＋隔離存證上線。

## 2026-07-24T22:22:01+08:00（zh 總數 862）

| 語言 | fresh | stale | missing | 覆蓋率 | Δfresh | Δmissing |
| ---- | ----: | ----: | ------: | -----: | -----: | -------: |
| en   |   724 |   104 |      34 |  96.1% |      · |        · |
| ja   |   700 |   156 |       6 |  99.3% |      · |        · |
| ko   |   700 |   159 |       3 |  99.7% |      · |        · |
| es   |   704 |   155 |       3 |  99.7% |      · |        · |
| fr   |   701 |   161 |       0 | 100.0% |      · |        · |
| vi   |    55 |    16 |     791 |   8.2% |      · |        · |
| id   |    65 |    14 |     783 |   9.2% |      · |        · |
| pt   |    47 |    15 |     800 |   7.2% |      · |        · |
| hi   |    47 |    11 |     804 |   6.7% |      · |        · |

總缺口（stale+missing）：**4015**（＝0 vs 上一筆）

**節點／worker**（ok/fail 為累計；Δ為對上一筆）

| 節點               |  ok | fail | Δok | 平均秒 | 主要 fail                          |
| ------------------ | --: | ---: | --: | -----: | ---------------------------------- |
| fleet:desktop-3090 |  30 |  111 |   — |      — | verify=1×34；verify=None×32        |
| fleet:laptop-4090  |  17 |   77 |   — |      — | health×42；verify=None×24          |
| worker:gemma31     |   1 |   22 |   — |    2.2 | no output written by tra×22        |
| worker:laguna      |   3 |   10 |   — |  318.3 | no output written by tra×7；leak×1 |
| worker:mac         |   2 |   20 |   — |  304.9 | leak×14；verify=1×5                |
| worker:nemo        |  18 |   68 |   — |  139.2 | leak×52；verify=1×9                |

endpoint 探活：mac-m4max 🟢、desktop-3090 🟢、laptop-4090 🟢

節點紀錄首航（哲宇 directive：fleet 每節點運作狀況跟分析也入 repo）。

## 2026-07-25T00:05:44+08:00（zh 總數 862）

| 語言 | fresh | stale | missing | 覆蓋率 | Δfresh | Δmissing |
| ---- | ----: | ----: | ------: | -----: | -----: | -------: |
| en   |   724 |   104 |      34 |  96.1% |      · |        · |
| ja   |   700 |   156 |       6 |  99.3% |      · |        · |
| ko   |   700 |   159 |       3 |  99.7% |      · |        · |
| es   |   705 |   155 |       2 |  99.8% |     +1 |       -1 |
| fr   |   701 |   161 |       0 | 100.0% |      · |        · |
| vi   |    61 |    16 |     785 |   8.9% |     +6 |       -6 |
| id   |    75 |    14 |     773 |  10.3% |    +10 |      -10 |
| pt   |    67 |    14 |     781 |   9.4% |    +20 |      -19 |
| hi   |    66 |    10 |     786 |   8.8% |    +19 |      -18 |

總缺口（stale+missing）：**3959**（▼56 vs 上一筆）

**節點／worker**（ok/fail 為累計；Δ為對上一筆）

| 節點               |  ok | fail | Δok | 平均秒 | 主要 fail                              |
| ------------------ | --: | ---: | --: | -----: | -------------------------------------- |
| fleet:desktop-3090 |  37 |  138 |  +7 |      — | health×45；verify=1×43                 |
| fleet:laptop-4090  |  20 |   90 |  +3 |      — | health×53；verify=None×24              |
| worker:gemma31     |   1 |   34 |   · |    2.2 | no output written by tra×34            |
| worker:laguna      |  14 |   15 | +11 |  266.9 | no output written by tra×9；verify=3×3 |
| worker:mac         |   4 |   39 |  +2 |  357.8 | leak×24；verify=1×11                   |
| worker:nemo        |  35 |   99 | +17 |  136.1 | leak×73；verify=1×13                   |
| worker:nemo2       |  16 |   15 |   — |  122.5 | leak×11；verify=1×3                    |

endpoint 探活：mac-m4max 🟢、desktop-3090 🟢、laptop-4090 🟢

儲值後首個整點：雲端 track 4 worker 觀察 throughput；classic qwen＋fleet 3090/4090 續跑。

## 2026-07-25T01:30:35+08:00（zh 總數 862）

| 語言 | fresh | stale | missing | 覆蓋率 | Δfresh | Δmissing |
| ---- | ----: | ----: | ------: | -----: | -----: | -------: |
| en   |   724 |   104 |      34 |  96.1% |      · |        · |
| ja   |   700 |   156 |       6 |  99.3% |      · |        · |
| ko   |   703 |   156 |       3 |  99.7% |     +3 |        · |
| es   |   707 |   153 |       2 |  99.8% |     +2 |        · |
| fr   |   704 |   158 |       0 | 100.0% |     +3 |        · |
| vi   |    64 |    16 |     782 |   9.3% |     +3 |       -3 |
| id   |    87 |    14 |     761 |  11.7% |    +12 |      -12 |
| pt   |    92 |    11 |     759 |  11.9% |    +25 |      -22 |
| hi   |    91 |     8 |     763 |  11.5% |    +25 |      -23 |
| ar   |     0 |     0 |     862 |   0.0% |      — |        — |
| ru   |     0 |     0 |     862 |   0.0% |      — |        — |

總缺口（stale+missing）：**5610**（▲1651 vs 上一筆）

**節點／worker**（ok/fail 為累計；Δ為對上一筆）

| 節點               |  ok | fail | Δok | 平均秒 | 主要 fail                               |
| ------------------ | --: | ---: | --: | -----: | --------------------------------------- |
| fleet:desktop-3090 |  44 |  155 |  +7 |      — | health×50；verify=1×46                  |
| fleet:laptop-4090  |  24 |  108 |  +4 |      — | health×67；verify=None×24               |
| worker:gemma31     |   1 |   34 |   · |    2.2 | no output written by tra×34             |
| worker:laguna      |  16 |   25 |  +2 |  249.4 | no output written by tra×12；verify=3×4 |
| worker:mac         |  13 |   56 |  +9 |  158.0 | leak×30；verify=1×17                    |
| worker:nemo        |  52 |  121 | +17 |  131.4 | leak×90；verify=1×15                    |
| worker:nemo2       |  32 |   39 | +16 |  129.4 | leak×33；verify=1×5                     |
| worker:nemo3       |  12 |   21 |   — |  109.6 | leak×14；verify=1×3                     |
| worker:oss20       |   5 |    4 |   — |  415.8 | verify=1×2；no output written by tra×1  |

endpoint 探活：mac-m4max 🟢、desktop-3090 🟢、laptop-4090 🟢

重啟後接手：四產線存活（cloud 9954 五 worker／classic 92129／fleet 95808+95809），ar/ru scaffold 已進 registry 與 status 面，出生子代續跑 Stage 2 校準。

## 2026-07-25T01:34:52+08:00（zh 總數 862）

| 語言 | fresh | stale | missing | 覆蓋率 | Δfresh | Δmissing |
| ---- | ----: | ----: | ------: | -----: | -----: | -------: |
| en   |   724 |   104 |      34 |  96.1% |      · |        · |
| ja   |   700 |   156 |       6 |  99.3% |      · |        · |
| ko   |   703 |   156 |       3 |  99.7% |      · |        · |
| es   |   707 |   153 |       2 |  99.8% |      · |        · |
| fr   |   704 |   158 |       0 | 100.0% |      · |        · |
| vi   |    64 |    16 |     782 |   9.3% |      · |        · |
| id   |    87 |    14 |     761 |  11.7% |      · |        · |
| pt   |    92 |    11 |     759 |  11.9% |      · |        · |
| hi   |    92 |     8 |     762 |  11.6% |     +1 |       -1 |
| ar   |     0 |     0 |     862 |   0.0% |      · |        · |
| ru   |     0 |     0 |     862 |   0.0% |      · |        · |

總缺口（stale+missing）：**5609**（▼1 vs 上一筆）

**節點／worker**（ok/fail 為累計；Δ為對上一筆）

| 節點               |  ok | fail | Δok | 平均秒 | 主要 fail                               |
| ------------------ | --: | ---: | --: | -----: | --------------------------------------- |
| fleet:desktop-3090 |  44 |  155 |   · |      — | health×50；verify=1×46                  |
| fleet:laptop-4090  |  24 |  108 |   · |      — | health×67；verify=None×24               |
| worker:gemma31     |   1 |   34 |   · |    2.2 | no output written by tra×34             |
| worker:laguna      |  16 |   26 |   · |  249.4 | no output written by tra×13；verify=3×4 |
| worker:mac         |  13 |   56 |   · |  158.0 | leak×30；verify=1×17                    |
| worker:nemo        |  52 |  122 |   · |  131.4 | leak×91；verify=1×15                    |
| worker:nemo2       |  32 |   39 |   · |  129.4 | leak×33；verify=1×5                     |
| worker:nemo3       |  13 |   22 |  +1 |  108.8 | leak×14；verify=1×4                     |
| worker:oss20       |   5 |    4 |   · |  415.8 | verify=1×2；no output written by tra×1  |

endpoint 探活：mac-m4max 🟢、desktop-3090 🟢、laptop-4090 🟢

（babel-pulse 常駐儀器自動快照）

## 2026-07-25T01:35:31+08:00（zh 總數 862）

| 語言 | fresh | stale | missing | 覆蓋率 | Δfresh | Δmissing |
| ---- | ----: | ----: | ------: | -----: | -----: | -------: |
| en   |   724 |   104 |      34 |  96.1% |      · |        · |
| ja   |   700 |   156 |       6 |  99.3% |      · |        · |
| ko   |   703 |   156 |       3 |  99.7% |      · |        · |
| es   |   707 |   153 |       2 |  99.8% |      · |        · |
| fr   |   704 |   158 |       0 | 100.0% |      · |        · |
| vi   |    64 |    16 |     782 |   9.3% |      · |        · |
| id   |    87 |    14 |     761 |  11.7% |      · |        · |
| pt   |    93 |    11 |     758 |  12.1% |     +1 |       -1 |
| hi   |    92 |     8 |     762 |  11.6% |      · |        · |
| ar   |     0 |     0 |     862 |   0.0% |      · |        · |
| ru   |     0 |     0 |     862 |   0.0% |      · |        · |

總缺口（stale+missing）：**5608**（▼1 vs 上一筆）

**節點／worker**（ok/fail 為累計；Δ為對上一筆）

| 節點               |  ok | fail | Δok | 平均秒 | 主要 fail                               |
| ------------------ | --: | ---: | --: | -----: | --------------------------------------- |
| fleet:desktop-3090 |  44 |  155 |   · |      — | health×50；verify=1×46                  |
| fleet:laptop-4090  |  24 |  108 |   · |      — | health×67；verify=None×24               |
| worker:gemma31     |   1 |   34 |   · |    2.2 | no output written by tra×34             |
| worker:laguna      |  16 |   26 |   · |  249.4 | no output written by tra×13；verify=3×4 |
| worker:mac         |  13 |   56 |   · |  158.0 | leak×30；verify=1×17                    |
| worker:nemo        |  52 |  122 |   · |  131.4 | leak×91；verify=1×15                    |
| worker:nemo2       |  33 |   39 |  +1 |  131.3 | leak×33；verify=1×5                     |
| worker:nemo3       |  13 |   22 |   · |  108.8 | leak×14；verify=1×4                     |
| worker:oss20       |   5 |    4 |   · |  415.8 | verify=1×2；no output written by tra×1  |

endpoint 探活：mac-m4max 🟢、desktop-3090 🟢、laptop-4090 🟢

（babel-pulse 常駐儀器自動快照）

## 2026-07-25T01:50:45+08:00（zh 總數 862）

| 語言 | fresh | stale | missing | 覆蓋率 | Δfresh | Δmissing |
| ---- | ----: | ----: | ------: | -----: | -----: | -------: |
| en   |   724 |   104 |      34 |  96.1% |      · |        · |
| ja   |   700 |   156 |       6 |  99.3% |      · |        · |
| ko   |   703 |   156 |       3 |  99.7% |      · |        · |
| es   |   707 |   153 |       2 |  99.8% |      · |        · |
| fr   |   704 |   158 |       0 | 100.0% |      · |        · |
| vi   |    64 |    16 |     782 |   9.3% |      · |        · |
| id   |    86 |    14 |     762 |  11.6% |     -1 |       +1 |
| pt   |    94 |    11 |     757 |  12.2% |     +1 |       -1 |
| hi   |    97 |     8 |     757 |  12.2% |     +5 |       -5 |
| ar   |     0 |     0 |     862 |   0.0% |      · |        · |
| ru   |     0 |     0 |     862 |   0.0% |      · |        · |

總缺口（stale+missing）：**5603**（▼5 vs 上一筆）

**節點／worker**（ok/fail 為累計；Δ為對上一筆）

| 節點               |  ok | fail | Δok | 平均秒 | 主要 fail                               |
| ------------------ | --: | ---: | --: | -----: | --------------------------------------- |
| fleet:desktop-3090 |  45 |  158 |  +1 |      — | health×51；verify=1×46                  |
| fleet:laptop-4090  |  25 |  114 |  +1 |      — | health×73；verify=None×24               |
| worker:gemma31     |   1 |   34 |   · |    2.2 | no output written by tra×34             |
| worker:laguna      |  16 |   27 |   · |  249.4 | no output written by tra×14；verify=3×4 |
| worker:mac         |  13 |   56 |   · |  158.0 | leak×30；verify=1×17                    |
| worker:nemo        |  53 |  130 |  +1 |  131.0 | leak×97；verify=1×17                    |
| worker:nemo2       |  35 |   43 |  +2 |  137.4 | leak×36；verify=1×6                     |
| worker:nemo3       |  17 |   24 |  +4 |  131.0 | leak×16；verify=1×4                     |
| worker:oss20       |   6 |    4 |  +1 |  521.4 | verify=1×2；no output written by tra×1  |

endpoint 探活：mac-m4max 🟢、desktop-3090 🟢、laptop-4090 🟢

（babel-pulse 常駐儀器自動快照）

## 2026-07-25T02:06:16+08:00（zh 總數 862）

| 語言 | fresh | stale | missing | 覆蓋率 | Δfresh | Δmissing |
| ---- | ----: | ----: | ------: | -----: | -----: | -------: |
| en   |   724 |   104 |      34 |  96.1% |      · |        · |
| ja   |   700 |   156 |       6 |  99.3% |      · |        · |
| ko   |   703 |   156 |       3 |  99.7% |      · |        · |
| es   |   707 |   153 |       2 |  99.8% |      · |        · |
| fr   |   704 |   158 |       0 | 100.0% |      · |        · |
| vi   |    64 |    16 |     782 |   9.3% |      · |        · |
| id   |    93 |    14 |     755 |  12.4% |     +7 |       -7 |
| pt   |   100 |    11 |     751 |  12.9% |     +6 |       -6 |
| hi   |   101 |     8 |     753 |  12.6% |     +4 |       -4 |
| ar   |     0 |     0 |     862 |   0.0% |      · |        · |
| ru   |     0 |     0 |     862 |   0.0% |      · |        · |

總缺口（stale+missing）：**5586**（▼17 vs 上一筆）

**節點／worker**（ok/fail 為累計；Δ為對上一筆）

| 節點               |  ok | fail | Δok | 平均秒 | 主要 fail                               |
| ------------------ | --: | ---: | --: | -----: | --------------------------------------- |
| fleet:desktop-3090 |  45 |  158 |   · |      — | health×51；verify=1×46                  |
| fleet:laptop-4090  |  26 |  117 |  +1 |      — | health×76；verify=None×24               |
| worker:gemma31     |   1 |   34 |   · |    2.2 | no output written by tra×34             |
| worker:laguna      |  16 |   27 |   · |  249.4 | no output written by tra×14；verify=3×4 |
| worker:mac         |  13 |   58 |   · |  158.0 | leak×31；verify=1×17                    |
| worker:nemo        |  56 |  134 |  +3 |  133.4 | leak×100；verify=1×18                   |
| worker:nemo2       |  40 |   46 |  +5 |  131.1 | leak×37；verify=1×8                     |
| worker:nemo3       |  20 |   27 |  +3 |  125.9 | leak×18；verify=1×4                     |
| worker:oss20       |   7 |    5 |  +1 |  492.0 | verify=1×2；leak×2                      |

endpoint 探活：local 🟢、laptop-4090 🟢、laptop-5090 🔴、desktop-3090 🟢、mac-m4max 🟢

（babel-pulse 常駐儀器自動快照）

## 2026-07-25T02:21:52+08:00（zh 總數 862）

| 語言 | fresh | stale | missing | 覆蓋率 | Δfresh | Δmissing |
| ---- | ----: | ----: | ------: | -----: | -----: | -------: |
| en   |   724 |   104 |      34 |  96.1% |      · |        · |
| ja   |   700 |   156 |       6 |  99.3% |      · |        · |
| ko   |   703 |   156 |       3 |  99.7% |      · |        · |
| es   |   707 |   153 |       2 |  99.8% |      · |        · |
| fr   |   704 |   158 |       0 | 100.0% |      · |        · |
| vi   |    64 |    16 |     782 |   9.3% |      · |        · |
| id   |    92 |    13 |     757 |  12.2% |     -1 |       +2 |
| pt   |   103 |    11 |     748 |  13.2% |     +3 |       -3 |
| hi   |   104 |     8 |     750 |  13.0% |     +3 |       -3 |
| ar   |     0 |     0 |     862 |   0.0% |      · |        · |
| ru   |     0 |     0 |     862 |   0.0% |      · |        · |

總缺口（stale+missing）：**5581**（▼5 vs 上一筆）

**節點／worker**（ok/fail 為累計；Δ為對上一筆）

| 節點               |  ok | fail | Δok | 平均秒 | 主要 fail                              |
| ------------------ | --: | ---: | --: | -----: | -------------------------------------- |
| fleet:desktop-3090 |  48 |  164 |  +3 |      — | health×55；verify=1×47                 |
| fleet:laptop-4090  |  26 |  117 |   · |      — | health×76；verify=None×24              |
| worker:gemma31     |   1 |   34 |   · |    2.2 | no output written by tra×34            |
| worker:laguna      |  16 |   29 |   · |  249.4 | no output written by tra×14；leak×5    |
| worker:mac         |  14 |   59 |  +1 |  182.8 | leak×31；verify=1×18                   |
| worker:nemo        |  59 |  140 |  +3 |  132.3 | leak×106；verify=1×18                  |
| worker:nemo2       |  42 |   51 |  +2 |  128.6 | leak×39；verify=1×10                   |
| worker:nemo3       |  20 |   33 |   · |  125.9 | leak×20；verify=1×6                    |
| worker:oss20       |   8 |    6 |  +1 |  497.5 | no output written by tra×2；verify=1×2 |

endpoint 探活：local 🟢、laptop-4090 🟢、laptop-5090 🔴、desktop-3090 🟢、mac-m4max 🟢

（babel-pulse 常駐儀器自動快照）

## 2026-07-25T02:31:51+08:00（zh 總數 862）

| 語言 | fresh | stale | missing | 覆蓋率 | Δfresh | Δmissing |
| ---- | ----: | ----: | ------: | -----: | -----: | -------: |
| en   |   724 |   104 |      34 |  96.1% |      · |        · |
| ja   |   700 |   156 |       6 |  99.3% |      · |        · |
| ko   |   703 |   156 |       3 |  99.7% |      · |        · |
| es   |   707 |   153 |       2 |  99.8% |      · |        · |
| fr   |   704 |   158 |       0 | 100.0% |      · |        · |
| vi   |    67 |    16 |     779 |   9.6% |     +3 |       -3 |
| id   |    95 |    12 |     755 |  12.4% |     +3 |       -2 |
| pt   |   105 |    11 |     746 |  13.5% |     +2 |       -2 |
| hi   |   104 |     8 |     750 |  13.0% |      · |        · |
| ar   |     0 |     0 |     862 |   0.0% |      · |        · |
| ru   |     0 |     0 |     862 |   0.0% |      · |        · |

總缺口（stale+missing）：**5573**（▼8 vs 上一筆）

**節點／worker**（ok/fail 為累計；Δ為對上一筆）

| 節點               |  ok | fail | Δok | 平均秒 | 主要 fail                           |
| ------------------ | --: | ---: | --: | -----: | ----------------------------------- |
| fleet:desktop-3090 |  48 |  164 |   · |      — | health×55；verify=1×47              |
| fleet:laptop-4090  |  26 |  117 |   · |      — | health×76；verify=None×24           |
| worker:gemma31     |   1 |   34 |   · |    2.2 | no output written by tra×34         |
| worker:laguna      |  16 |   30 |   · |  249.4 | no output written by tra×15；leak×5 |
| worker:mac         |  15 |   60 |  +1 |  196.8 | leak×32；verify=1×18                |
| worker:nemo        |  59 |  145 |   · |  132.3 | leak×108；verify=1×20               |
| worker:nemo2       |  43 |   53 |  +1 |  131.2 | leak×39；verify=1×11                |
| worker:nemo3       |  22 |   38 |  +2 |  121.7 | leak×22；verify=1×9                 |
| worker:oss20       |   8 |    7 |   · |  497.5 | leak×3；no output written by tra×2  |

endpoint 探活：local 🟢、laptop-4090 🟢、laptop-5090 🔴、desktop-3090 🟢、mac-m4max 🟢

（babel-pulse 常駐儀器自動快照）

## 2026-07-25T02:37:15+08:00（zh 總數 862）

| 語言 | fresh | stale | missing | 覆蓋率 | Δfresh | Δmissing |
| ---- | ----: | ----: | ------: | -----: | -----: | -------: |
| en   |   724 |   104 |      34 |  96.1% |      · |        · |
| ja   |   700 |   156 |       6 |  99.3% |      · |        · |
| ko   |   703 |   156 |       3 |  99.7% |      · |        · |
| es   |   707 |   153 |       2 |  99.8% |      · |        · |
| fr   |   704 |   158 |       0 | 100.0% |      · |        · |
| vi   |    65 |    16 |     781 |   9.4% |     -2 |       +2 |
| id   |    97 |    11 |     754 |  12.5% |     +2 |       -1 |
| pt   |   106 |    11 |     745 |  13.6% |     +1 |       -1 |
| hi   |   104 |     8 |     750 |  13.0% |      · |        · |
| ar   |     0 |     0 |     862 |   0.0% |      · |        · |
| ru   |     0 |     0 |     862 |   0.0% |      · |        · |

總缺口（stale+missing）：**5572**（▼1 vs 上一筆）

**節點／worker**（ok/fail 為累計；Δ為對上一筆）

| 節點               |  ok | fail | Δok | 平均秒 | 主要 fail                           |
| ------------------ | --: | ---: | --: | -----: | ----------------------------------- |
| fleet:desktop-3090 |  48 |  164 |   · |      — | health×55；verify=1×47              |
| fleet:laptop-4090  |  26 |  122 |   · |      — | health×81；verify=None×24           |
| worker:gemma31     |   1 |   34 |   · |    2.2 | no output written by tra×34         |
| worker:laguna      |  17 |   30 |  +1 |  248.5 | no output written by tra×15；leak×5 |
| worker:mac         |  15 |   61 |   · |  196.8 | leak×33；verify=1×18                |
| worker:nemo        |  59 |  148 |   · |  132.3 | leak×109；verify=1×21               |
| worker:nemo2       |  44 |   56 |  +1 |  132.4 | leak×42；verify=1×11                |
| worker:nemo3       |  22 |   39 |   · |  121.7 | leak×22；verify=1×10                |
| worker:oss20       |   8 |    7 |   · |  497.5 | leak×3；no output written by tra×2  |

endpoint 探活：local 🟢、laptop-4090 🟢、laptop-5090 🔴、desktop-3090 🟢、mac-m4max 🟢

（babel-pulse 常駐儀器自動快照）

## 2026-07-25T02:52:30+08:00（zh 總數 862）

| 語言 | fresh | stale | missing | 覆蓋率 | Δfresh | Δmissing |
| ---- | ----: | ----: | ------: | -----: | -----: | -------: |
| en   |   724 |   104 |      34 |  96.1% |      · |        · |
| ja   |   700 |   156 |       6 |  99.3% |      · |        · |
| ko   |   703 |   156 |       3 |  99.7% |      · |        · |
| es   |   707 |   153 |       2 |  99.8% |      · |        · |
| fr   |   704 |   158 |       0 | 100.0% |      · |        · |
| vi   |    67 |    16 |     779 |   9.6% |     +2 |       -2 |
| id   |    94 |    11 |     757 |  12.2% |     -3 |       +3 |
| pt   |   109 |    11 |     742 |  13.9% |     +3 |       -3 |
| hi   |   105 |     8 |     749 |  13.1% |     +1 |       -1 |
| ar   |     0 |     0 |     862 |   0.0% |      · |        · |
| ru   |     0 |     0 |     862 |   0.0% |      · |        · |

總缺口（stale+missing）：**5569**（▼3 vs 上一筆）

**節點／worker**（ok/fail 為累計；Δ為對上一筆）

| 節點               |  ok | fail | Δok | 平均秒 | 主要 fail                           |
| ------------------ | --: | ---: | --: | -----: | ----------------------------------- |
| fleet:desktop-3090 |  48 |  172 |   · |      — | health×57；verify=1×52              |
| fleet:laptop-4090  |  26 |  122 |   · |      — | health×81；verify=None×24           |
| worker:gemma31     |   1 |   34 |   · |    2.2 | no output written by tra×34         |
| worker:laguna      |  18 |   31 |  +1 |  263.8 | no output written by tra×15；leak×5 |
| worker:mac         |  15 |   65 |   · |  196.8 | leak×35；verify=1×20                |
| worker:nemo        |  61 |  152 |  +2 |  135.7 | leak×112；verify=1×22               |
| worker:nemo2       |  46 |   63 |  +2 |  131.0 | leak×45；verify=1×13                |
| worker:nemo3       |  23 |   46 |  +1 |  118.5 | leak×27；verify=1×10                |
| worker:oss20       |   8 |    8 |   · |  497.5 | no output written by tra×3；leak×3  |

endpoint 探活：local 🟢、laptop-4090 🟢、laptop-5090 🔴、desktop-3090 🟢、mac-m4max 🟢

（babel-pulse 常駐儀器自動快照）

## 2026-07-25T03:07:59+08:00（zh 總數 862）

| 語言 | fresh | stale | missing | 覆蓋率 | Δfresh | Δmissing |
| ---- | ----: | ----: | ------: | -----: | -----: | -------: |
| en   |   724 |   104 |      34 |  96.1% |      · |        · |
| ja   |   700 |   156 |       6 |  99.3% |      · |        · |
| ko   |   703 |   156 |       3 |  99.7% |      · |        · |
| es   |   707 |   153 |       2 |  99.8% |      · |        · |
| fr   |   704 |   158 |       0 | 100.0% |      · |        · |
| vi   |    67 |    16 |     779 |   9.6% |      · |        · |
| id   |    95 |    11 |     756 |  12.3% |     +1 |       -1 |
| pt   |   112 |    11 |     739 |  14.3% |     +3 |       -3 |
| hi   |   106 |     8 |     748 |  13.2% |     +1 |       -1 |
| ar   |     0 |     0 |     862 |   0.0% |      · |        · |
| ru   |     0 |     0 |     862 |   0.0% |      · |        · |

總缺口（stale+missing）：**5564**（▼5 vs 上一筆）

**節點／worker**（ok/fail 為累計；Δ為對上一筆）

| 節點               |  ok | fail | Δok | 平均秒 | 主要 fail                               |
| ------------------ | --: | ---: | --: | -----: | --------------------------------------- |
| fleet:desktop-3090 |  48 |  172 |   · |      — | health×57；verify=1×52                  |
| fleet:laptop-4090  |  26 |  125 |   · |      — | health×83；verify=None×24               |
| worker:gemma31     |   1 |   34 |   · |    2.2 | no output written by tra×34             |
| worker:laguna      |  19 |   32 |  +1 |  263.0 | no output written by tra×15；verify=3×5 |
| worker:mac         |  15 |   68 |   · |  196.8 | leak×37；verify=1×20                    |
| worker:nemo        |  62 |  160 |  +1 |  134.5 | leak×115；verify=1×26                   |
| worker:nemo2       |  48 |   68 |  +2 |  129.6 | leak×47；verify=1×16                    |
| worker:nemo3       |  24 |   53 |  +1 |  117.1 | leak×32；verify=1×11                    |
| worker:oss20       |   8 |    9 |   · |  497.5 | leak×4；no output written by tra×3      |

endpoint 探活：local 🟢、laptop-4090 🟢、laptop-5090 🔴、desktop-3090 🟢、mac-m4max 🟢

（babel-pulse 常駐儀器自動快照）

## 2026-07-25T03:23:32+08:00（zh 總數 862）

| 語言 | fresh | stale | missing | 覆蓋率 | Δfresh | Δmissing |
| ---- | ----: | ----: | ------: | -----: | -----: | -------: |
| en   |   724 |   104 |      34 |  96.1% |      · |        · |
| ja   |   700 |   156 |       6 |  99.3% |      · |        · |
| ko   |   703 |   156 |       3 |  99.7% |      · |        · |
| es   |   707 |   153 |       2 |  99.8% |      · |        · |
| fr   |   704 |   158 |       0 | 100.0% |      · |        · |
| vi   |    67 |    16 |     779 |   9.6% |      · |        · |
| id   |    96 |     9 |     757 |  12.2% |     +1 |       +1 |
| pt   |   119 |    11 |     732 |  15.1% |     +7 |       -7 |
| hi   |   110 |     8 |     744 |  13.7% |     +4 |       -4 |
| ar   |     0 |     0 |     862 |   0.0% |      · |        · |
| ru   |     0 |     0 |     862 |   0.0% |      · |        · |

總缺口（stale+missing）：**5552**（▼12 vs 上一筆）

**節點／worker**（ok/fail 為累計；Δ為對上一筆）

| 節點               |  ok | fail | Δok | 平均秒 | 主要 fail                               |
| ------------------ | --: | ---: | --: | -----: | --------------------------------------- |
| fleet:desktop-3090 |  48 |  180 |   · |      — | health×60；verify=1×55                  |
| fleet:laptop-4090  |  26 |  125 |   · |      — | health×83；verify=None×24               |
| worker:gemma31     |   1 |   34 |   · |    2.2 | no output written by tra×34             |
| worker:laguna      |  20 |   34 |  +1 |  253.2 | no output written by tra×15；verify=3×5 |
| worker:mac         |  15 |   72 |   · |  196.8 | leak×41；verify=1×20                    |
| worker:nemo        |  67 |  166 |  +5 |  131.2 | leak×119；verify=1×28                   |
| worker:nemo2       |  52 |   75 |  +4 |  125.0 | leak×52；verify=1×18                    |
| worker:nemo3       |  27 |   57 |  +3 |  115.8 | leak×32；verify=1×14                    |
| worker:oss20       |   8 |   11 |   · |  497.5 | leak×5；no output written by tra×3      |

endpoint 探活：local 🟢、laptop-4090 🔴、laptop-5090 🔴、desktop-3090 🟢、mac-m4max 🟢

（babel-pulse 常駐儀器自動快照）

## 2026-07-25T03:39:05+08:00（zh 總數 862）

| 語言 | fresh | stale | missing | 覆蓋率 | Δfresh | Δmissing |
| ---- | ----: | ----: | ------: | -----: | -----: | -------: |
| en   |   724 |   104 |      34 |  96.1% |      · |        · |
| ja   |   700 |   156 |       6 |  99.3% |      · |        · |
| ko   |   703 |   156 |       3 |  99.7% |      · |        · |
| es   |   707 |   153 |       2 |  99.8% |      · |        · |
| fr   |   704 |   158 |       0 | 100.0% |      · |        · |
| vi   |    68 |    16 |     778 |   9.7% |     +1 |       -1 |
| id   |   101 |     8 |     753 |  12.6% |     +5 |       -4 |
| pt   |   121 |    11 |     730 |  15.3% |     +2 |       -2 |
| hi   |   110 |     8 |     744 |  13.7% |      · |        · |
| ar   |     0 |     0 |     862 |   0.0% |      · |        · |
| ru   |     0 |     0 |     862 |   0.0% |      · |        · |

總缺口（stale+missing）：**5544**（▼8 vs 上一筆）

**節點／worker**（ok/fail 為累計；Δ為對上一筆）

| 節點               |  ok | fail | Δok | 平均秒 | 主要 fail                               |
| ------------------ | --: | ---: | --: | -----: | --------------------------------------- |
| fleet:desktop-3090 |  48 |  180 |   · |      — | health×60；verify=1×55                  |
| fleet:laptop-4090  |  26 |  125 |   · |      — | health×83；verify=None×24               |
| worker:gemma31     |   1 |   34 |   · |    2.2 | no output written by tra×34             |
| worker:laguna      |  22 |   35 |  +2 |  259.6 | no output written by tra×16；verify=3×5 |
| worker:mac         |  15 |   77 |   · |  196.8 | leak×43；verify=1×22                    |
| worker:nemo        |  67 |  174 |   · |  131.2 | leak×123；verify=1×32                   |
| worker:nemo2       |  53 |   80 |  +1 |  125.9 | leak×54；verify=1×19                    |
| worker:nemo3       |  28 |   64 |  +1 |  114.8 | leak×37；verify=1×15                    |
| worker:oss20       |   9 |   12 |  +1 |  511.3 | leak×6；no output written by tra×3      |

endpoint 探活：local 🟢、laptop-4090 🔴、laptop-5090 🔴、desktop-3090 🟢、mac-m4max 🟢

（babel-pulse 常駐儀器自動快照）

## 2026-07-25T03:54:40+08:00（zh 總數 862）

| 語言 | fresh | stale | missing | 覆蓋率 | Δfresh | Δmissing |
| ---- | ----: | ----: | ------: | -----: | -----: | -------: |
| en   |   724 |   104 |      34 |  96.1% |      · |        · |
| ja   |   700 |   156 |       6 |  99.3% |      · |        · |
| ko   |   703 |   156 |       3 |  99.7% |      · |        · |
| es   |   707 |   153 |       2 |  99.8% |      · |        · |
| fr   |   704 |   158 |       0 | 100.0% |      · |        · |
| vi   |    70 |     8 |     784 |   9.0% |     +2 |       +6 |
| id   |    99 |     7 |     756 |  12.3% |     -2 |       +3 |
| pt   |   123 |    10 |     729 |  15.4% |     +2 |       -1 |
| hi   |   111 |     8 |     743 |  13.8% |     +1 |       -1 |
| ar   |     0 |     0 |     862 |   0.0% |      · |        · |
| ru   |     0 |     0 |     862 |   0.0% |      · |        · |

總缺口（stale+missing）：**5541**（▼3 vs 上一筆）

**節點／worker**（ok/fail 為累計；Δ為對上一筆）

| 節點               |  ok | fail | Δok | 平均秒 | 主要 fail                               |
| ------------------ | --: | ---: | --: | -----: | --------------------------------------- |
| fleet:desktop-3090 |  48 |  188 |   · |      — | health×64；verify=1×58                  |
| fleet:laptop-4090  |  27 |  134 |  +1 |      — | health×83；verify=None×24               |
| worker:gemma31     |   1 |   34 |   · |    2.2 | no output written by tra×34             |
| worker:laguna      |  22 |   37 |   · |  259.6 | no output written by tra×16；verify=3×5 |
| worker:mac         |  15 |   80 |   · |  196.8 | leak×46；verify=1×22                    |
| worker:nemo        |  67 |  179 |   · |  131.2 | leak×126；verify=1×33                   |
| worker:nemo2       |  55 |   86 |  +2 |  125.6 | leak×57；verify=1×20                    |
| worker:nemo3       |  30 |   68 |  +2 |  122.1 | leak×38；verify=1×17                    |
| worker:oss20       |   9 |   12 |   · |  511.3 | leak×6；no output written by tra×3      |

endpoint 探活：local 🟢、laptop-4090 🟢、laptop-5090 🔴、desktop-3090 🟢、mac-m4max 🟢

（babel-pulse 常駐儀器自動快照）

## 2026-07-25T04:10:04+08:00（zh 總數 862）

| 語言 | fresh | stale | missing | 覆蓋率 | Δfresh | Δmissing |
| ---- | ----: | ----: | ------: | -----: | -----: | -------: |
| en   |   724 |   104 |      34 |  96.1% |      · |        · |
| ja   |   700 |   156 |       6 |  99.3% |      · |        · |
| ko   |   703 |   156 |       3 |  99.7% |      · |        · |
| es   |   707 |   153 |       2 |  99.8% |      · |        · |
| fr   |   704 |   158 |       0 | 100.0% |      · |        · |
| vi   |    72 |     8 |     782 |   9.3% |     +2 |       -2 |
| id   |   101 |     6 |     755 |  12.4% |     +2 |       -1 |
| pt   |   127 |    10 |     725 |  15.9% |     +4 |       -4 |
| hi   |   114 |     8 |     740 |  14.2% |     +3 |       -3 |
| ar   |     0 |     0 |     862 |   0.0% |      · |        · |
| ru   |     0 |     0 |     862 |   0.0% |      · |        · |

總缺口（stale+missing）：**5530**（▼11 vs 上一筆）

**節點／worker**（ok/fail 為累計；Δ為對上一筆）

| 節點               |  ok | fail | Δok | 平均秒 | 主要 fail                               |
| ------------------ | --: | ---: | --: | -----: | --------------------------------------- |
| fleet:desktop-3090 |  48 |  188 |   · |      — | health×64；verify=1×58                  |
| fleet:laptop-4090  |  27 |  134 |   · |      — | health×83；verify=None×24               |
| worker:gemma31     |   1 |   34 |   · |    2.2 | no output written by tra×34             |
| worker:laguna      |  23 |   39 |  +1 |  254.3 | no output written by tra×17；verify=1×6 |
| worker:mac         |  15 |   82 |   · |  196.8 | leak×46；verify=1×23                    |
| worker:nemo        |  70 |  184 |  +3 |  130.3 | leak×128；verify=1×35                   |
| worker:nemo2       |  59 |   93 |  +4 |  122.8 | leak×62；verify=1×22                    |
| worker:nemo3       |  31 |   75 |  +1 |  121.4 | leak×41；verify=1×20                    |
| worker:oss20       |  10 |   14 |  +1 |  480.6 | leak×6；no output written by tra×5      |

endpoint 探活：local 🟢、laptop-4090 🟢、laptop-5090 🔴、desktop-3090 🟢、mac-m4max 🟢

（babel-pulse 常駐儀器自動快照）

## 2026-07-25T04:25:32+08:00（zh 總數 862）

| 語言 | fresh | stale | missing | 覆蓋率 | Δfresh | Δmissing |
| ---- | ----: | ----: | ------: | -----: | -----: | -------: |
| en   |   724 |   104 |      34 |  96.1% |      · |        · |
| ja   |   700 |   156 |       6 |  99.3% |      · |        · |
| ko   |   703 |   156 |       3 |  99.7% |      · |        · |
| es   |   707 |   153 |       2 |  99.8% |      · |        · |
| fr   |   704 |   158 |       0 | 100.0% |      · |        · |
| vi   |    73 |     8 |     781 |   9.4% |     +1 |       -1 |
| id   |   103 |     7 |     752 |  12.8% |     +2 |       -3 |
| pt   |   132 |    10 |     720 |  16.5% |     +5 |       -5 |
| hi   |   117 |     8 |     737 |  14.5% |     +3 |       -3 |
| ar   |     0 |     0 |     862 |   0.0% |      · |        · |
| ru   |     0 |     0 |     862 |   0.0% |      · |        · |

總缺口（stale+missing）：**5519**（▼11 vs 上一筆）

**節點／worker**（ok/fail 為累計；Δ為對上一筆）

| 節點               |  ok | fail | Δok | 平均秒 | 主要 fail                               |
| ------------------ | --: | ---: | --: | -----: | --------------------------------------- |
| fleet:desktop-3090 |  49 |  193 |  +1 |      — | health×67；verify=1×60                  |
| fleet:laptop-4090  |  27 |  134 |   · |      — | health×83；verify=None×24               |
| worker:gemma31     |   1 |   34 |   · |    2.2 | no output written by tra×34             |
| worker:laguna      |  25 |   40 |  +2 |  260.9 | no output written by tra×18；verify=1×6 |
| worker:mac         |  16 |   85 |  +1 |  208.6 | leak×48；verify=1×24                    |
| worker:nemo        |  74 |  190 |  +4 |  127.9 | leak×131；verify=1×38                   |
| worker:nemo2       |  61 |  101 |  +2 |  120.5 | leak×67；verify=1×24                    |
| worker:nemo3       |  33 |   86 |  +2 |  117.8 | leak×47；verify=1×23                    |
| worker:oss20       |  12 |   15 |  +2 |  432.0 | leak×7；no output written by tra×5      |

endpoint 探活：local 🟢、laptop-4090 🟢、laptop-5090 🔴、desktop-3090 🟢、mac-m4max 🟢

（babel-pulse 常駐儀器自動快照）

## 2026-07-25T04:40:56+08:00（zh 總數 862）

| 語言 | fresh | stale | missing | 覆蓋率 | Δfresh | Δmissing |
| ---- | ----: | ----: | ------: | -----: | -----: | -------: |
| en   |   724 |   104 |      34 |  96.1% |      · |        · |
| ja   |   700 |   156 |       6 |  99.3% |      · |        · |
| ko   |   703 |   156 |       3 |  99.7% |      · |        · |
| es   |   707 |   153 |       2 |  99.8% |      · |        · |
| fr   |   704 |   158 |       0 | 100.0% |      · |        · |
| vi   |    73 |     8 |     781 |   9.4% |      · |        · |
| id   |   105 |     6 |     751 |  12.9% |     +2 |       -1 |
| pt   |   134 |    10 |     718 |  16.7% |     +2 |       -2 |
| hi   |   119 |     8 |     735 |  14.7% |     +2 |       -2 |
| ar   |     0 |     0 |     862 |   0.0% |      · |        · |
| ru   |     0 |     0 |     862 |   0.0% |      · |        · |

總缺口（stale+missing）：**5513**（▼6 vs 上一筆）

**節點／worker**（ok/fail 為累計；Δ為對上一筆）

| 節點               |  ok | fail | Δok | 平均秒 | 主要 fail                               |
| ------------------ | --: | ---: | --: | -----: | --------------------------------------- |
| fleet:desktop-3090 |  49 |  193 |   · |      — | health×67；verify=1×60                  |
| fleet:laptop-4090  |  27 |  134 |   · |      — | health×83；verify=None×24               |
| worker:gemma31     |   1 |   34 |   · |    2.2 | no output written by tra×34             |
| worker:laguna      |  26 |   42 |  +1 |  255.5 | no output written by tra×18；verify=3×6 |
| worker:mac         |  16 |   88 |   · |  208.6 | leak×49；verify=1×24                    |
| worker:nemo        |  74 |  197 |   · |  127.9 | leak×134；verify=1×41                   |
| worker:nemo2       |  61 |  109 |   · |  120.5 | leak×71；verify=1×26                    |
| worker:nemo3       |  35 |   91 |  +2 |  122.5 | leak×50；verify=1×23                    |
| worker:oss20       |  13 |   16 |  +1 |  433.3 | leak×8；no output written by tra×5      |

endpoint 探活：local 🟢、laptop-4090 🟢、laptop-5090 🔴、desktop-3090 🟢、mac-m4max 🟢

（babel-pulse 常駐儀器自動快照）

## 2026-07-25T04:56:29+08:00（zh 總數 862）

| 語言 | fresh | stale | missing | 覆蓋率 | Δfresh | Δmissing |
| ---- | ----: | ----: | ------: | -----: | -----: | -------: |
| en   |   724 |   104 |      34 |  96.1% |      · |        · |
| ja   |   701 |   156 |       5 |  99.4% |     +1 |       -1 |
| ko   |   703 |   156 |       3 |  99.7% |      · |        · |
| es   |   707 |   153 |       2 |  99.8% |      · |        · |
| fr   |   704 |   158 |       0 | 100.0% |      · |        · |
| vi   |    74 |     8 |     780 |   9.5% |     +1 |       -1 |
| id   |   105 |     6 |     751 |  12.9% |      · |        · |
| pt   |   138 |    10 |     714 |  17.2% |     +4 |       -4 |
| hi   |   122 |     8 |     732 |  15.1% |     +3 |       -3 |
| ar   |     0 |     0 |     862 |   0.0% |      · |        · |
| ru   |     0 |     0 |     862 |   0.0% |      · |        · |

總缺口（stale+missing）：**5504**（▼9 vs 上一筆）

**節點／worker**（ok/fail 為累計；Δ為對上一筆）

| 節點               |  ok | fail | Δok | 平均秒 | 主要 fail                               |
| ------------------ | --: | ---: | --: | -----: | --------------------------------------- |
| fleet:desktop-3090 |  49 |  199 |   · |      — | health×70；verify=1×62                  |
| fleet:laptop-4090  |  27 |  134 |   · |      — | health×83；verify=None×24               |
| worker:gemma31     |   1 |   34 |   · |    2.2 | no output written by tra×34             |
| worker:laguna      |  26 |   44 |   · |  255.5 | no output written by tra×19；verify=1×7 |
| worker:mac         |  17 |   90 |  +1 |  213.3 | leak×50；verify=1×24                    |
| worker:nemo        |  77 |  203 |  +3 |  126.1 | leak×136；verify=1×42                   |
| worker:nemo2       |  62 |  118 |  +1 |  119.6 | leak×80；verify=1×26                    |
| worker:nemo3       |  40 |   94 |  +5 |  119.7 | leak×52；verify=1×24                    |
| worker:oss20       |  14 |   17 |  +1 |  443.9 | leak×8；no output written by tra×6      |

endpoint 探活：local 🟢、laptop-4090 🟢、laptop-5090 🔴、desktop-3090 🟢、mac-m4max 🟢

（babel-pulse 常駐儀器自動快照）

## 2026-07-25T05:06:16+08:00（zh 總數 862）

| 語言 | fresh | stale | missing | 覆蓋率 | Δfresh | Δmissing |
| ---- | ----: | ----: | ------: | -----: | -----: | -------: |
| en   |   724 |   104 |      34 |  96.1% |      · |        · |
| ja   |   701 |   156 |       5 |  99.4% |      · |        · |
| ko   |   703 |   156 |       3 |  99.7% |      · |        · |
| es   |   707 |   153 |       2 |  99.8% |      · |        · |
| fr   |   704 |   158 |       0 | 100.0% |      · |        · |
| vi   |    74 |     8 |     780 |   9.5% |      · |        · |
| id   |   105 |     6 |     751 |  12.9% |      · |        · |
| pt   |   140 |    10 |     712 |  17.4% |     +2 |       -2 |
| hi   |   124 |     8 |     730 |  15.3% |     +2 |       -2 |
| ar   |     1 |     0 |     861 |   0.1% |     +1 |       -1 |
| ru   |     1 |     0 |     861 |   0.1% |     +1 |       -1 |

總缺口（stale+missing）：**5498**（▼6 vs 上一筆）

**節點／worker**（ok/fail 為累計；Δ為對上一筆）

| 節點               |  ok | fail | Δok | 平均秒 | 主要 fail                               |
| ------------------ | --: | ---: | --: | -----: | --------------------------------------- |
| fleet:desktop-3090 |  49 |  199 |   · |      — | health×70；verify=1×62                  |
| fleet:laptop-4090  |  27 |  134 |   · |      — | health×83；verify=None×24               |
| worker:gemma31     |   1 |   34 |   · |    2.2 | no output written by tra×34             |
| worker:laguna      |  26 |   44 |   · |  255.5 | no output written by tra×19；verify=1×7 |
| worker:mac         |  18 |   90 |  +1 |  225.6 | leak×50；verify=1×24                    |
| worker:nemo        |  79 |  204 |  +2 |  127.9 | leak×137；verify=1×42                   |
| worker:nemo2       |  64 |  121 |  +2 |  118.5 | leak×82；verify=1×27                    |
| worker:nemo3       |  42 |   97 |  +2 |  117.7 | leak×54；verify=1×24                    |
| worker:oss20       |  14 |   17 |   · |  443.9 | leak×8；no output written by tra×6      |

endpoint 探活：local 🟢、laptop-4090 🟢、laptop-5090 🔴、desktop-3090 🟢、mac-m4max 🟢

（babel-pulse 常駐儀器自動快照）

## 2026-07-25T05:11:54+08:00（zh 總數 862）

| 語言 | fresh | stale | missing | 覆蓋率 | Δfresh | Δmissing |
| ---- | ----: | ----: | ------: | -----: | -----: | -------: |
| en   |   724 |   104 |      34 |  96.1% |      · |        · |
| ja   |   701 |   156 |       5 |  99.4% |      · |        · |
| ko   |   703 |   156 |       3 |  99.7% |      · |        · |
| es   |   707 |   153 |       2 |  99.8% |      · |        · |
| fr   |   704 |   158 |       0 | 100.0% |      · |        · |
| vi   |    74 |     8 |     780 |   9.5% |      · |        · |
| id   |   107 |     6 |     749 |  13.1% |     +2 |       -2 |
| pt   |   142 |    10 |     710 |  17.6% |     +2 |       -2 |
| hi   |   124 |     8 |     730 |  15.3% |      · |        · |
| ar   |     3 |     0 |     859 |   0.3% |     +2 |       -2 |
| ru   |     3 |     0 |     859 |   0.3% |     +2 |       -2 |

總缺口（stale+missing）：**5490**（▼8 vs 上一筆）

**節點／worker**（ok/fail 為累計；Δ為對上一筆）

| 節點               |  ok | fail | Δok | 平均秒 | 主要 fail                               |
| ------------------ | --: | ---: | --: | -----: | --------------------------------------- |
| fleet:desktop-3090 |  49 |  199 |   · |      — | health×70；verify=1×62                  |
| fleet:laptop-4090  |  27 |  134 |   · |      — | health×83；verify=None×24               |
| worker:gemma31     |   1 |   34 |   · |    2.2 | no output written by tra×34             |
| worker:laguna      |  26 |   45 |   · |  255.5 | no output written by tra×19；verify=3×7 |
| worker:mac         |  18 |   90 |   · |  225.6 | leak×50；verify=1×24                    |
| worker:nemo        |  79 |  207 |   · |  127.9 | leak×138；verify=1×42                   |
| worker:nemo2       |  66 |  122 |  +2 |  118.4 | leak×82；verify=1×27                    |
| worker:nemo3       |  45 |   99 |  +3 |  114.2 | leak×56；verify=1×24                    |
| worker:oss20       |  15 |   17 |  +1 |  452.2 | leak×8；no output written by tra×6      |

endpoint 探活：local 🟢、laptop-4090 🟢、laptop-5090 🔴、desktop-3090 🟢、mac-m4max 🟢

（babel-pulse 常駐儀器自動快照）

## 2026-07-25T05:27:22+08:00（zh 總數 862）

| 語言 | fresh | stale | missing | 覆蓋率 | Δfresh | Δmissing |
| ---- | ----: | ----: | ------: | -----: | -----: | -------: |
| en   |   724 |   104 |      34 |  96.1% |      · |        · |
| ja   |   701 |   156 |       5 |  99.4% |      · |        · |
| ko   |   703 |   156 |       3 |  99.7% |      · |        · |
| es   |   708 |   152 |       2 |  99.8% |     +1 |        · |
| fr   |   705 |   157 |       0 | 100.0% |     +1 |        · |
| vi   |    74 |     8 |     780 |   9.5% |      · |        · |
| id   |   110 |     5 |     747 |  13.3% |     +3 |       -2 |
| pt   |   144 |    10 |     708 |  17.9% |     +2 |       -2 |
| hi   |   128 |     8 |     726 |  15.8% |     +4 |       -4 |
| ar   |     8 |     0 |     854 |   0.9% |     +5 |       -5 |
| ru   |     9 |     0 |     853 |   1.0% |     +6 |       -6 |

總缺口（stale+missing）：**5468**（▼22 vs 上一筆）

**節點／worker**（ok/fail 為累計；Δ為對上一筆）

| 節點               |  ok | fail | Δok | 平均秒 | 主要 fail                               |
| ------------------ | --: | ---: | --: | -----: | --------------------------------------- |
| fleet:desktop-3090 |  50 |  205 |  +1 |      — | health×71；verify=1×66                  |
| fleet:laptop-4090  |  27 |  134 |   · |      — | health×83；verify=None×24               |
| worker:gemma31     |   1 |   34 |   · |    2.2 | no output written by tra×34             |
| worker:laguna      |  29 |   47 |  +3 |  252.0 | no output written by tra×20；verify=1×8 |
| worker:mac         |  20 |   91 |  +2 |  260.1 | leak×51；verify=1×24                    |
| worker:nemo        |  84 |  213 |  +5 |  125.8 | leak×144；verify=1×42                   |
| worker:nemo2       |  74 |  124 |  +8 |  116.5 | leak×84；verify=1×27                    |
| worker:nemo3       |  49 |  105 |  +4 |  112.9 | leak×61；verify=1×24                    |
| worker:oss20       |  16 |   18 |  +1 |  449.4 | leak×9；no output written by tra×6      |

endpoint 探活：local 🟢、laptop-4090 🟢、laptop-5090 🔴、desktop-3090 🟢、mac-m4max 🟢

（babel-pulse 常駐儀器自動快照）

## 2026-07-25T05:42:48+08:00（zh 總數 862）

| 語言 | fresh | stale | missing | 覆蓋率 | Δfresh | Δmissing |
| ---- | ----: | ----: | ------: | -----: | -----: | -------: |
| en   |   724 |   104 |      34 |  96.1% |      · |        · |
| ja   |   701 |   156 |       5 |  99.4% |      · |        · |
| ko   |   703 |   156 |       3 |  99.7% |      · |        · |
| es   |   708 |   152 |       2 |  99.8% |      · |        · |
| fr   |   705 |   157 |       0 | 100.0% |      · |        · |
| vi   |    74 |     8 |     780 |   9.5% |      · |        · |
| id   |   115 |     5 |     742 |  13.9% |     +5 |       -5 |
| pt   |   151 |    10 |     701 |  18.7% |     +7 |       -7 |
| hi   |   132 |     8 |     722 |  16.2% |     +4 |       -4 |
| ar   |    13 |     0 |     849 |   1.5% |     +5 |       -5 |
| ru   |    17 |     0 |     845 |   2.0% |     +8 |       -8 |

總缺口（stale+missing）：**5439**（▼29 vs 上一筆）

**節點／worker**（ok/fail 為累計；Δ為對上一筆）

| 節點               |  ok | fail | Δok | 平均秒 | 主要 fail                               |
| ------------------ | --: | ---: | --: | -----: | --------------------------------------- |
| fleet:desktop-3090 |  50 |  205 |   · |      — | health×71；verify=1×66                  |
| fleet:laptop-4090  |  27 |  134 |   · |      — | health×83；verify=None×24               |
| worker:gemma31     |   1 |   34 |   · |    2.2 | no output written by tra×34             |
| worker:laguna      |  32 |   49 |  +3 |  239.5 | no output written by tra×21；verify=1×8 |
| worker:mac         |  20 |   95 |   · |  260.1 | leak×54；verify=1×24                    |
| worker:nemo        |  93 |  221 |  +9 |  118.2 | leak×150；verify=1×44                   |
| worker:nemo2       |  82 |  129 |  +8 |  112.8 | leak×88；verify=1×28                    |
| worker:nemo3       |  54 |  109 |  +5 |  110.8 | leak×64；verify=1×25                    |
| worker:oss20       |  18 |   20 |  +2 |  419.1 | leak×11；no output written by tra×6     |

endpoint 探活：local 🟢、laptop-4090 🟢、laptop-5090 🔴、desktop-3090 🟢、mac-m4max 🟢

（babel-pulse 常駐儀器自動快照）

## 2026-07-25T05:58:15+08:00（zh 總數 862）

| 語言 | fresh | stale | missing | 覆蓋率 | Δfresh | Δmissing |
| ---- | ----: | ----: | ------: | -----: | -----: | -------: |
| en   |   724 |   104 |      34 |  96.1% |      · |        · |
| ja   |   701 |   156 |       5 |  99.4% |      · |        · |
| ko   |   703 |   156 |       3 |  99.7% |      · |        · |
| es   |   708 |   152 |       2 |  99.8% |      · |        · |
| fr   |   705 |   157 |       0 | 100.0% |      · |        · |
| vi   |    75 |     8 |     779 |   9.6% |     +1 |       -1 |
| id   |   124 |     4 |     734 |  14.8% |     +9 |       -8 |
| pt   |   155 |    10 |     697 |  19.1% |     +4 |       -4 |
| hi   |   136 |     8 |     718 |  16.7% |     +4 |       -4 |
| ar   |    15 |     0 |     847 |   1.7% |     +2 |       -2 |
| ru   |    19 |     0 |     843 |   2.2% |     +2 |       -2 |

總缺口（stale+missing）：**5417**（▼22 vs 上一筆）

**節點／worker**（ok/fail 為累計；Δ為對上一筆）

| 節點               |  ok | fail | Δok | 平均秒 | 主要 fail                                |
| ------------------ | --: | ---: | --: | -----: | ---------------------------------------- |
| fleet:desktop-3090 |  50 |  205 |   · |      — | health×71；verify=1×66                   |
| fleet:laptop-4090  |  27 |  134 |   · |      — | health×83；verify=None×24                |
| worker:gemma31     |   1 |   34 |   · |    2.2 | no output written by tra×34              |
| worker:laguna      |  34 |   51 |  +2 |  234.3 | no output written by tra×21；verify=1×10 |
| worker:mac         |  20 |   98 |   · |  260.1 | leak×55；verify=1×24                     |
| worker:nemo        |  99 |  223 |  +6 |  117.1 | leak×152；verify=1×44                    |
| worker:nemo2       |  85 |  133 |  +3 |  114.5 | leak×91；verify=1×28                     |
| worker:nemo3       |  60 |  112 |  +6 |  112.2 | leak×67；verify=1×25                     |
| worker:oss20       |  18 |   21 |   · |  419.1 | leak×11；no output written by tra×6      |

endpoint 探活：local 🟢、laptop-4090 🟢、laptop-5090 🔴、desktop-3090 🟢、mac-m4max 🟢

（babel-pulse 常駐儀器自動快照）

## 2026-07-25T06:13:42+08:00（zh 總數 862）

| 語言 | fresh | stale | missing | 覆蓋率 | Δfresh | Δmissing |
| ---- | ----: | ----: | ------: | -----: | -----: | -------: |
| en   |   724 |   104 |      34 |  96.1% |      · |        · |
| ja   |   701 |   156 |       5 |  99.4% |      · |        · |
| ko   |   703 |   156 |       3 |  99.7% |      · |        · |
| es   |   709 |   151 |       2 |  99.8% |     +1 |        · |
| fr   |   705 |   157 |       0 | 100.0% |      · |        · |
| vi   |    76 |     8 |     778 |   9.7% |     +1 |       -1 |
| id   |   119 |     3 |     740 |  14.2% |     -5 |       +6 |
| pt   |   159 |    10 |     693 |  19.6% |     +4 |       -4 |
| hi   |   137 |     8 |     717 |  16.8% |     +1 |       -1 |
| ar   |    19 |     0 |     843 |   2.2% |     +4 |       -4 |
| ru   |    22 |     0 |     840 |   2.6% |     +3 |       -3 |

總缺口（stale+missing）：**5408**（▼9 vs 上一筆）

**節點／worker**（ok/fail 為累計；Δ為對上一筆）

| 節點               |  ok | fail | Δok | 平均秒 | 主要 fail                                |
| ------------------ | --: | ---: | --: | -----: | ---------------------------------------- |
| fleet:desktop-3090 |  50 |  213 |   · |      — | health×74；verify=1×68                   |
| fleet:laptop-4090  |  27 |  134 |   · |      — | health×83；verify=None×24                |
| worker:gemma31     |   1 |   34 |   · |    2.2 | no output written by tra×34              |
| worker:laguna      |  35 |   52 |  +1 |  236.4 | no output written by tra×21；verify=1×11 |
| worker:mac         |  21 |  101 |  +1 |  255.4 | leak×58；verify=1×24                     |
| worker:nemo        | 104 |  226 |  +5 |  119.6 | leak×155；verify=1×44                    |
| worker:nemo2       |  88 |  139 |  +3 |  115.4 | leak×95；verify=1×29                     |
| worker:nemo3       |  64 |  117 |  +4 |  110.3 | leak×70；verify=1×26                     |
| worker:oss20       |  18 |   23 |   · |  419.1 | leak×11；no output written by tra×7      |

endpoint 探活：local 🟢、laptop-4090 🟢、laptop-5090 🔴、desktop-3090 🟢、mac-m4max 🟢

（babel-pulse 常駐儀器自動快照）

## 2026-07-25T06:41:17+08:00（zh 總數 862）

| 語言 | fresh | stale | missing | 覆蓋率 | Δfresh | Δmissing |
| ---- | ----: | ----: | ------: | -----: | -----: | -------: |
| en   |   724 |   104 |      34 |  96.1% |      · |        · |
| ja   |   702 |   155 |       5 |  99.4% |     +1 |        · |
| ko   |   704 |   155 |       3 |  99.7% |     +1 |        · |
| es   |   710 |   150 |       2 |  99.8% |     +1 |        · |
| fr   |   706 |   156 |       0 | 100.0% |     +1 |        · |
| vi   |    77 |     8 |     777 |   9.9% |     +1 |       -1 |
| id   |   120 |     3 |     739 |  14.3% |     +1 |       -1 |
| pt   |   164 |    10 |     688 |  20.2% |     +5 |       -5 |
| hi   |   140 |     8 |     714 |  17.2% |     +3 |       -3 |
| ar   |    21 |     0 |     841 |   2.4% |     +2 |       -2 |
| ru   |    29 |     0 |     833 |   3.4% |     +7 |       -7 |

總缺口（stale+missing）：**5385**（▼23 vs 上一筆）

**節點／worker**（ok/fail 為累計；Δ為對上一筆）

| 節點               |  ok | fail | Δok | 平均秒 | 主要 fail                                |
| ------------------ | --: | ---: | --: | -----: | ---------------------------------------- |
| fleet:desktop-3090 |  51 |  220 |  +1 |      — | health×75；verify=1×74                   |
| fleet:laptop-4090  |  27 |  134 |   · |      — | health×83；verify=None×24                |
| worker:gemma31     |   1 |   34 |   · |    2.2 | no output written by tra×34              |
| worker:laguna      |  38 |   53 |  +3 |  231.8 | no output written by tra×21；verify=1×11 |
| worker:mac         |  25 |  106 |  +4 |  248.4 | leak×60；verify=1×24                     |
| worker:nemo        | 108 |  230 |  +4 |  119.5 | leak×158；verify=1×44                    |
| worker:nemo2       |  95 |  143 |  +7 |  112.8 | leak×97；verify=1×29                     |
| worker:nemo3       |  70 |  123 |  +6 |  108.3 | leak×74；verify=1×27                     |
| worker:oss20       |  19 |   25 |  +1 |  416.7 | leak×12；no output written by tra×7      |

endpoint 探活：local 🟢、laptop-4090 🟢、laptop-5090 🔴、desktop-3090 🟢、mac-m4max 🟢

（babel-pulse 常駐儀器自動快照）

## 2026-07-25T06:44:36+08:00（zh 總數 862）

| 語言 | fresh | stale | missing | 覆蓋率 | Δfresh | Δmissing |
| ---- | ----: | ----: | ------: | -----: | -----: | -------: |
| en   |   724 |   104 |      34 |  96.1% |      · |        · |
| ja   |   702 |   155 |       5 |  99.4% |      · |        · |
| ko   |   705 |   154 |       3 |  99.7% |     +1 |        · |
| es   |   710 |   150 |       2 |  99.8% |      · |        · |
| fr   |   706 |   156 |       0 | 100.0% |      · |        · |
| vi   |    77 |     8 |     777 |   9.9% |      · |        · |
| id   |   120 |     3 |     739 |  14.3% |      · |        · |
| pt   |   165 |    10 |     687 |  20.3% |     +1 |       -1 |
| hi   |   144 |     8 |     710 |  17.6% |     +4 |       -4 |
| ar   |    23 |     0 |     839 |   2.7% |     +2 |       -2 |
| ru   |    31 |     0 |     831 |   3.6% |     +2 |       -2 |

總缺口（stale+missing）：**5375**（▼10 vs 上一筆）

**節點／worker**（ok/fail 為累計；Δ為對上一筆）

| 節點               |  ok | fail | Δok | 平均秒 | 主要 fail                                |
| ------------------ | --: | ---: | --: | -----: | ---------------------------------------- |
| fleet:desktop-3090 |  51 |  220 |   · |      — | health×75；verify=1×74                   |
| fleet:laptop-4090  |  27 |  134 |   · |      — | health×83；verify=None×24                |
| worker:gemma31     |   1 |   34 |   · |    2.2 | no output written by tra×34              |
| worker:laguna      |  38 |   54 |   · |  231.8 | no output written by tra×22；verify=1×11 |
| worker:mac         |  26 |  107 |  +1 |  245.4 | leak×61；verify=1×24                     |
| worker:nemo        | 110 |  232 |  +2 |  118.8 | leak×158；verify=1×44                    |
| worker:nemo2       |  97 |  145 |  +2 |  111.7 | leak×99；verify=1×29                     |
| worker:nemo3       |  72 |  125 |  +2 |  106.4 | leak×76；verify=1×27                     |
| worker:oss20       |  19 |   26 |   · |  416.7 | leak×12；no output written by tra×8      |

endpoint 探活：local 🟢、laptop-4090 🟢、laptop-5090 🔴、desktop-3090 🟢、mac-m4max 🟢

（babel-pulse 常駐儀器自動快照）

## 2026-07-25T07:00:01+08:00（zh 總數 862）

| 語言 | fresh | stale | missing | 覆蓋率 | Δfresh | Δmissing |
| ---- | ----: | ----: | ------: | -----: | -----: | -------: |
| en   |   724 |   104 |      34 |  96.1% |      · |        · |
| ja   |   703 |   154 |       5 |  99.4% |     +1 |        · |
| ko   |   705 |   154 |       3 |  99.7% |      · |        · |
| es   |   710 |   150 |       2 |  99.8% |      · |        · |
| fr   |   706 |   156 |       0 | 100.0% |      · |        · |
| vi   |    77 |     8 |     777 |   9.9% |      · |        · |
| id   |   125 |     3 |     734 |  14.8% |     +5 |       -5 |
| pt   |   170 |    10 |     682 |  20.9% |     +5 |       -5 |
| hi   |   145 |     7 |     710 |  17.6% |     +1 |        · |
| ar   |    28 |     0 |     834 |   3.2% |     +5 |       -5 |
| ru   |    37 |     0 |     825 |   4.3% |     +6 |       -6 |

總缺口（stale+missing）：**5352**（▼23 vs 上一筆）

**節點／worker**（ok/fail 為累計；Δ為對上一筆）

| 節點               |  ok | fail | Δok | 平均秒 | 主要 fail                                |
| ------------------ | --: | ---: | --: | -----: | ---------------------------------------- |
| fleet:desktop-3090 |  51 |  229 |   · |      — | health×80；verify=1×76                   |
| fleet:laptop-4090  |  27 |  134 |   · |      — | health×83；verify=None×24                |
| worker:gemma31     |   1 |   34 |   · |    2.2 | no output written by tra×34              |
| worker:laguna      |  41 |   55 |  +3 |  231.5 | no output written by tra×23；verify=1×11 |
| worker:mac         |  28 |  113 |  +2 |  235.7 | leak×62；verify=1×26                     |
| worker:nemo        | 119 |  236 |  +9 |  114.9 | leak×161；verify=1×45                    |
| worker:nemo2       | 101 |  151 |  +4 |  110.3 | leak×104；verify=1×30                    |
| worker:nemo3       |  79 |  130 |  +7 |  103.3 | leak×80；verify=1×28                     |
| worker:oss20       |  21 |   29 |  +2 |  397.0 | leak×13；no output written by tra×8      |

endpoint 探活：local 🟢、laptop-4090 🟢、laptop-5090 🔴、desktop-3090 🟢、mac-m4max 🟢

（babel-pulse 常駐儀器自動快照）

## 2026-07-25T07:46:28+08:00（zh 總數 862）

| 語言 | fresh | stale | missing | 覆蓋率 | Δfresh | Δmissing |
| ---- | ----: | ----: | ------: | -----: | -----: | -------: |
| en   |   724 |   104 |      34 |  96.1% |      · |        · |
| ja   |   704 |   153 |       5 |  99.4% |      · |        · |
| ko   |   705 |   154 |       3 |  99.7% |      · |        · |
| es   |   711 |   149 |       2 |  99.8% |      · |        · |
| fr   |   709 |   153 |       0 | 100.0% |     +2 |        · |
| vi   |    81 |     8 |     773 |  10.3% |      · |        · |
| id   |   132 |     3 |     727 |  15.7% |     +1 |       -1 |
| pt   |   179 |    10 |     673 |  21.9% |     +2 |       -2 |
| hi   |   157 |     6 |     699 |  18.9% |     +4 |       -4 |
| ar   |    41 |     0 |     821 |   4.8% |     +4 |       -4 |
| ru   |    51 |     0 |     811 |   5.9% |     +2 |       -2 |

總缺口（stale+missing）：**5288**（▼15 vs 上一筆）

**節點／worker**（ok/fail 為累計；Δ為對上一筆）

| 節點               |  ok | fail | Δok | 平均秒 | 主要 fail                                |
| ------------------ | --: | ---: | --: | -----: | ---------------------------------------- |
| fleet:desktop-3090 |  51 |  236 |   · |      — | health×83；verify=1×78                   |
| fleet:laptop-4090  |  27 |  134 |   · |      — | health×83；verify=None×24                |
| worker:gemma31     |   1 |   34 |   · |    2.2 | no output written by tra×34              |
| worker:laguna      |  47 |   58 |  +1 |  226.3 | no output written by tra×25；verify=1×11 |
| worker:mac         |  37 |  121 |  +3 |  216.3 | leak×64；verify=1×30                     |
| worker:nemo        | 139 |  248 |  +4 |  111.2 | leak×169；verify=1×46                    |
| worker:nemo2       | 116 |  164 |  +4 |  108.8 | leak×116；verify=1×30                    |
| worker:nemo3       |  95 |  143 |  +3 |  100.5 | leak×88；verify=1×30                     |
| worker:oss20       |  22 |   35 |   · |  390.4 | leak×16；no output written by tra×8      |

endpoint 探活：local 🟢、laptop-4090 🟢、laptop-5090 🔴、desktop-3090 🟢、mac-m4max 🟢

（babel-pulse 常駐儀器自動快照）

## 2026-07-25T07:47:14+08:00（zh 總數 862）

| 語言 | fresh | stale | missing | 覆蓋率 | Δfresh | Δmissing |
| ---- | ----: | ----: | ------: | -----: | -----: | -------: |
| en   |   724 |   104 |      34 |  96.1% |      · |        · |
| ja   |   704 |   153 |       5 |  99.4% |      · |        · |
| ko   |   705 |   154 |       3 |  99.7% |      · |        · |
| es   |   712 |   148 |       2 |  99.8% |     +1 |        · |
| fr   |   709 |   153 |       0 | 100.0% |      · |        · |
| vi   |    81 |     8 |     773 |  10.3% |      · |        · |
| id   |   132 |     3 |     727 |  15.7% |      · |        · |
| pt   |   180 |    10 |     672 |  22.0% |     +1 |       -1 |
| hi   |   160 |     6 |     696 |  19.3% |     +3 |       -3 |
| ar   |    42 |     0 |     820 |   4.9% |     +1 |       -1 |
| ru   |    53 |     0 |     809 |   6.1% |     +2 |       -2 |

總缺口（stale+missing）：**5280**（▼8 vs 上一筆）

**節點／worker**（ok/fail 為累計；Δ為對上一筆）

| 節點               |  ok | fail | Δok | 平均秒 | 主要 fail                                |
| ------------------ | --: | ---: | --: | -----: | ---------------------------------------- |
| fleet:desktop-3090 |  51 |  236 |   · |      — | health×83；verify=1×78                   |
| fleet:laptop-4090  |  27 |  134 |   · |      — | health×83；verify=None×24                |
| worker:gemma31     |   1 |   34 |   · |    2.2 | no output written by tra×34              |
| worker:laguna      |  47 |   58 |   · |  226.3 | no output written by tra×25；verify=1×11 |
| worker:mac         |  38 |  121 |  +1 |  212.7 | leak×64；verify=1×30                     |
| worker:nemo        | 139 |  248 |   · |  111.2 | leak×169；verify=1×46                    |
| worker:nemo2       | 116 |  165 |   · |  108.8 | leak×117；verify=1×30                    |
| worker:nemo3       |  95 |  144 |   · |  100.5 | leak×89；verify=1×30                     |
| worker:oss20       |  22 |   35 |   · |  390.4 | leak×16；no output written by tra×8      |

endpoint 探活：local 🟢、laptop-4090 🟢、laptop-5090 🔴、desktop-3090 🟢、mac-m4max 🟢

（babel-pulse 常駐儀器自動快照）

## 2026-07-25T08:01:41+08:00（zh 總數 862）

| 語言 | fresh | stale | missing | 覆蓋率 | Δfresh | Δmissing |
| ---- | ----: | ----: | ------: | -----: | -----: | -------: |
| en   |   724 |   104 |      34 |  96.1% |      · |        · |
| ja   |   708 |   149 |       5 |  99.4% |     +4 |        · |
| ko   |   705 |   154 |       3 |  99.7% |      · |        · |
| es   |   712 |   148 |       2 |  99.8% |      · |        · |
| fr   |   709 |   153 |       0 | 100.0% |      · |        · |
| vi   |    81 |     8 |     773 |  10.3% |      · |        · |
| id   |   133 |     3 |     726 |  15.8% |     +1 |       -1 |
| pt   |   181 |    10 |     671 |  22.2% |     +1 |       -1 |
| hi   |   158 |     5 |     699 |  18.9% |     -2 |       +3 |
| ar   |    43 |     0 |     819 |   5.0% |     +1 |       -1 |
| ru   |    55 |     0 |     807 |   6.4% |     +2 |       -2 |

總缺口（stale+missing）：**5273**（▼7 vs 上一筆）

**節點／worker**（ok/fail 為累計；Δ為對上一筆）

| 節點               |  ok | fail | Δok | 平均秒 | 主要 fail                                |
| ------------------ | --: | ---: | --: | -----: | ---------------------------------------- |
| fleet:desktop-3090 |  52 |  244 |  +1 |      — | health×87；verify=1×81                   |
| fleet:laptop-4090  |  27 |  134 |   · |      — | health×83；verify=None×24                |
| worker:gemma31     |   1 |   34 |   · |    2.2 | no output written by tra×34              |
| worker:laguna      |  48 |   60 |  +1 |  223.7 | no output written by tra×25；verify=1×13 |
| worker:mac         |  43 |  123 |  +5 |  197.6 | leak×64；verify=1×30                     |
| worker:nemo        | 142 |  253 |  +3 |  110.6 | leak×173；verify=1×47                    |
| worker:nemo2       | 117 |  171 |  +1 |  108.6 | leak×122；verify=1×31                    |
| worker:nemo3       |  97 |  149 |  +2 |  100.1 | leak×92；verify=1×31                     |
| worker:oss20       |  22 |   36 |   · |  390.4 | leak×16；no output written by tra×8      |

endpoint 探活：local 🟢、laptop-4090 🟢、laptop-5090 🔴、desktop-3090 🟢、mac-m4max 🟢

（babel-pulse 常駐儀器自動快照）

## 2026-07-25T08:54:20+08:00（zh 總數 863）

| 語言 | fresh | stale | missing | 覆蓋率 | Δfresh | Δmissing |
| ---- | ----: | ----: | ------: | -----: | -----: | -------: |
| en   |   723 |   105 |      35 |  95.9% |     -1 |       +1 |
| ja   |   707 |   150 |       6 |  99.3% |     -1 |       +1 |
| ko   |   704 |   155 |       4 |  99.5% |     -1 |       +1 |
| es   |   711 |   149 |       3 |  99.7% |     -1 |       +1 |
| fr   |   708 |   154 |       1 |  99.9% |     -1 |       +1 |
| vi   |    83 |     8 |     772 |  10.5% |     +2 |       -1 |
| id   |   143 |     3 |     717 |  16.9% |    +10 |       -9 |
| pt   |   197 |    10 |     656 |  24.0% |    +16 |      -15 |
| hi   |   165 |     6 |     692 |  19.8% |     +7 |       -7 |
| ar   |    62 |     0 |     801 |   7.2% |    +19 |      -18 |
| ru   |    72 |     0 |     791 |   8.3% |    +17 |      -16 |

總缺口（stale+missing）：**5218**（▼55 vs 上一筆）

**節點／worker**（ok/fail 為累計；Δ為對上一筆）

| 節點               |  ok | fail | Δok | 平均秒 | 主要 fail                                |
| ------------------ | --: | ---: | --: | -----: | ---------------------------------------- |
| fleet:desktop-3090 |  53 |  258 |  +1 |      — | health×93；verify=1×83                   |
| fleet:laptop-4090  |  27 |  134 |   · |      — | health×83；verify=None×24                |
| worker:gemma31     |   1 |   34 |   · |    2.2 | no output written by tra×34              |
| worker:laguna      |  57 |   64 |  +9 |  223.6 | no output written by tra×29；verify=1×13 |
| worker:mac         |  43 |  123 |   · |  197.6 | leak×64；verify=1×30                     |
| worker:nemo        | 163 |  266 | +21 |  107.5 | leak×185；verify=1×47                    |
| worker:nemo2       | 139 |  189 | +22 |  103.4 | leak×134；verify=1×34                    |
| worker:nemo3       | 117 |  168 | +20 |   97.8 | leak×105；verify=1×35                    |
| worker:oss20       |  23 |   39 |  +1 |  409.3 | leak×17；verify=1×10                     |

endpoint 探活：local 🟢、laptop-4090 🟢、laptop-5090 🔴、desktop-3090 🟢、mac-m4max 🟢

（babel-pulse 常駐儀器自動快照）

## 2026-07-25T09:02:45+08:00（zh 總數 863）

| 語言 | fresh | stale | missing | 覆蓋率 | Δfresh | Δmissing |
| ---- | ----: | ----: | ------: | -----: | -----: | -------: |
| en   |   723 |   105 |      35 |  95.9% |      · |        · |
| ja   |   707 |   150 |       6 |  99.3% |      · |        · |
| ko   |   704 |   155 |       4 |  99.5% |      · |        · |
| es   |   711 |   149 |       3 |  99.7% |      · |        · |
| fr   |   708 |   154 |       1 |  99.9% |      · |        · |
| vi   |    83 |     8 |     772 |  10.5% |      · |        · |
| id   |   144 |     3 |     716 |  17.0% |     +1 |       -1 |
| pt   |   198 |    10 |     655 |  24.1% |     +1 |       -1 |
| hi   |   167 |     6 |     690 |  20.0% |     +2 |       -2 |
| ar   |    63 |     0 |     800 |   7.3% |     +1 |       -1 |
| ru   |    75 |     0 |     788 |   8.7% |     +3 |       -3 |

總缺口（stale+missing）：**5210**（▼8 vs 上一筆）

**節點／worker**（ok/fail 為累計；Δ為對上一筆）

| 節點               |  ok | fail | Δok | 平均秒 | 主要 fail                                |
| ------------------ | --: | ---: | --: | -----: | ---------------------------------------- |
| fleet:desktop-3090 |  53 |  258 |   · |      — | health×93；verify=1×83                   |
| fleet:laptop-4090  |  27 |  134 |   · |      — | health×83；verify=None×24                |
| worker:gemma31     |   1 |   34 |   · |    2.2 | no output written by tra×34              |
| worker:laguna      |  59 |   65 |  +2 |  222.7 | no output written by tra×29；verify=1×13 |
| worker:mac         |  43 |  125 |   · |  197.6 | leak×66；verify=1×30                     |
| worker:nemo        | 163 |  270 |   · |  107.5 | leak×188；verify=1×48                    |
| worker:nemo2       | 141 |  193 |  +2 |  103.0 | leak×138；verify=1×34                    |
| worker:nemo3       | 120 |  170 |  +3 |   98.1 | leak×106；verify=1×35                    |
| worker:oss20       |  23 |   40 |   · |  409.3 | leak×17；verify=1×10                     |

endpoint 探活：local 🟢、laptop-4090 🟢、laptop-5090 🔴、desktop-3090 🟢、mac-m4max 🟢

（babel-pulse 常駐儀器自動快照）

## 2026-07-25T10:00:54+08:00（zh 總數 863）

| 語言 | fresh | stale | missing | 覆蓋率 | Δfresh | Δmissing |
| ---- | ----: | ----: | ------: | -----: | -----: | -------: |
| en   |   722 |   106 |      35 |  95.9% |     -1 |        · |
| ja   |   706 |   151 |       6 |  99.3% |     -1 |        · |
| ko   |   703 |   156 |       4 |  99.5% |     -1 |        · |
| es   |   710 |   150 |       3 |  99.7% |     -1 |        · |
| fr   |   707 |   155 |       1 |  99.9% |     -1 |        · |
| vi   |    88 |     9 |     766 |  11.2% |     +5 |       -6 |
| id   |   153 |     4 |     706 |  18.2% |     +9 |      -10 |
| pt   |   206 |    11 |     646 |  25.1% |     +8 |       -9 |
| hi   |   180 |     5 |     678 |  21.4% |    +13 |      -12 |
| ar   |    74 |     0 |     789 |   8.6% |    +11 |      -11 |
| ru   |    88 |     0 |     775 |  10.2% |    +13 |      -13 |

總缺口（stale+missing）：**5156**（▼54 vs 上一筆）

**節點／worker**（ok/fail 為累計；Δ為對上一筆）

| 節點               |  ok | fail | Δok | 平均秒 | 主要 fail                                |
| ------------------ | --: | ---: | --: | -----: | ---------------------------------------- |
| fleet:desktop-3090 |  54 |  271 |  +1 |      — | health×97；verify=1×87                   |
| fleet:laptop-4090  |  27 |  134 |   · |      — | health×83；verify=None×24                |
| worker:gemma31     |   1 |   34 |   · |    2.2 | no output written by tra×34              |
| worker:laguna      |  71 |   70 | +12 |  215.6 | no output written by tra×31；verify=1×15 |
| worker:mac         |  45 |  135 |  +2 |  205.3 | leak×71；verify=1×33                     |
| worker:nemo        | 190 |  284 | +27 |  102.7 | leak×198；verify=1×49                    |
| worker:nemo2       | 154 |  209 | +13 |   99.6 | leak×151；verify=1×35                    |
| worker:nemo3       | 129 |  195 |  +9 |   97.6 | leak×119；verify=1×40                    |
| worker:oss20       |  24 |   44 |  +1 |  410.6 | leak×20；verify=1×11                     |

endpoint 探活：local 🟢、laptop-4090 🟢、laptop-5090 🔴、desktop-3090 🟢、mac-m4max 🟢

（babel-pulse 常駐儀器自動快照）

## 2026-07-25T10:04:25+08:00（zh 總數 863）

| 語言 | fresh | stale | missing | 覆蓋率 | Δfresh | Δmissing |
| ---- | ----: | ----: | ------: | -----: | -----: | -------: |
| en   |   722 |   106 |      35 |  95.9% |      · |        · |
| ja   |   706 |   151 |       6 |  99.3% |      · |        · |
| ko   |   703 |   156 |       4 |  99.5% |      · |        · |
| es   |   710 |   150 |       3 |  99.7% |      · |        · |
| fr   |   707 |   155 |       1 |  99.9% |      · |        · |
| vi   |    88 |     9 |     766 |  11.2% |      · |        · |
| id   |   156 |     4 |     703 |  18.5% |     +3 |       -3 |
| pt   |   207 |    11 |     645 |  25.3% |     +1 |       -1 |
| hi   |   181 |     5 |     677 |  21.6% |     +1 |       -1 |
| ar   |    75 |     0 |     788 |   8.7% |     +1 |       -1 |
| ru   |    89 |     0 |     774 |  10.3% |     +1 |       -1 |

總缺口（stale+missing）：**5149**（▼7 vs 上一筆）

**節點／worker**（ok/fail 為累計；Δ為對上一筆）

| 節點               |  ok | fail | Δok | 平均秒 | 主要 fail                                |
| ------------------ | --: | ---: | --: | -----: | ---------------------------------------- |
| fleet:desktop-3090 |  54 |  271 |   · |      — | health×97；verify=1×87                   |
| fleet:laptop-4090  |  27 |  134 |   · |      — | health×83；verify=None×24                |
| worker:gemma31     |   1 |   34 |   · |    2.2 | no output written by tra×34              |
| worker:laguna      |  74 |   70 |  +3 |  209.4 | no output written by tra×31；verify=1×15 |
| worker:mac         |  45 |  136 |   · |  205.3 | leak×72；verify=1×33                     |
| worker:nemo        | 190 |  285 |   · |  102.7 | leak×199；verify=1×49                    |
| worker:nemo2       | 156 |  210 |  +2 |   98.7 | leak×151；verify=1×36                    |
| worker:nemo3       | 130 |  196 |  +1 |   97.5 | leak×120；verify=1×40                    |
| worker:oss20       |  24 |   45 |   · |  410.6 | leak×20；verify=1×11                     |

endpoint 探活：local 🟢、laptop-4090 🟢、laptop-5090 🔴、desktop-3090 🟢、mac-m4max 🟢

（babel-pulse 常駐儀器自動快照）

## 2026-07-25T10:35:30+08:00（zh 總數 863）

| 語言 | fresh | stale | missing | 覆蓋率 | Δfresh | Δmissing |
| ---- | ----: | ----: | ------: | -----: | -----: | -------: |
| en   |   722 |   106 |      35 |  95.9% |      · |        · |
| ja   |   706 |   151 |       6 |  99.3% |      · |        · |
| ko   |   702 |   157 |       4 |  99.5% |     -1 |        · |
| es   |   710 |   150 |       3 |  99.7% |      · |        · |
| fr   |   707 |   155 |       1 |  99.9% |      · |        · |
| vi   |    89 |     9 |     765 |  11.4% |     +1 |       -1 |
| id   |   160 |     4 |     699 |  19.0% |     +4 |       -4 |
| pt   |   216 |    11 |     636 |  26.3% |     +9 |       -9 |
| hi   |   185 |     5 |     673 |  22.0% |     +4 |       -4 |
| ar   |    81 |     0 |     782 |   9.4% |     +6 |       -6 |
| ru   |    95 |     0 |     768 |  11.0% |     +6 |       -6 |

總缺口（stale+missing）：**5120**（▼29 vs 上一筆）

**節點／worker**（ok/fail 為累計；Δ為對上一筆）

| 節點               |  ok | fail | Δok | 平均秒 | 主要 fail                                |
| ------------------ | --: | ---: | --: | -----: | ---------------------------------------- |
| fleet:desktop-3090 |  55 |  286 |  +1 |      — | health×106；verify=1×89                  |
| fleet:laptop-4090  |  27 |  134 |   · |      — | health×83；verify=None×24                |
| worker:gemma31     |   1 |   34 |   · |    2.2 | no output written by tra×34              |
| worker:laguna      |  79 |   72 |  +5 |  208.4 | no output written by tra×33；verify=1×15 |
| worker:mac         |  45 |  144 |   · |  205.3 | leak×77；verify=1×34                     |
| worker:nemo        | 197 |  296 |  +7 |  102.0 | leak×208；verify=1×49                    |
| worker:nemo2       | 169 |  217 | +13 |   99.1 | leak×158；verify=1×36                    |
| worker:nemo3       | 137 |  208 |  +7 |   96.8 | leak×129；verify=1×41                    |
| worker:oss20       |  25 |   47 |  +1 |  407.7 | leak×21；verify=1×11                     |

endpoint 探活：local 🟢、laptop-4090 🟢、laptop-5090 🔴、desktop-3090 🟢、mac-m4max 🟢

（babel-pulse 常駐儀器自動快照）

## 2026-07-25T10:50:56+08:00（zh 總數 863）

| 語言 | fresh | stale | missing | 覆蓋率 | Δfresh | Δmissing |
| ---- | ----: | ----: | ------: | -----: | -----: | -------: |
| en   |   722 |   106 |      35 |  95.9% |      · |        · |
| ja   |   706 |   151 |       6 |  99.3% |      · |        · |
| ko   |   702 |   157 |       4 |  99.5% |      · |        · |
| es   |   710 |   150 |       3 |  99.7% |      · |        · |
| fr   |   707 |   155 |       1 |  99.9% |      · |        · |
| vi   |    89 |     9 |     765 |  11.4% |      · |        · |
| id   |   161 |     4 |     698 |  19.1% |     +1 |       -1 |
| pt   |   218 |    11 |     634 |  26.5% |     +2 |       -2 |
| hi   |   192 |     4 |     667 |  22.7% |     +7 |       -6 |
| ar   |    85 |     0 |     778 |   9.8% |     +4 |       -4 |
| ru   |    97 |     0 |     766 |  11.2% |     +2 |       -2 |

總缺口（stale+missing）：**5104**（▼16 vs 上一筆）

**節點／worker**（ok/fail 為累計；Δ為對上一筆）

| 節點               |  ok | fail | Δok | 平均秒 | 主要 fail                                |
| ------------------ | --: | ---: | --: | -----: | ---------------------------------------- |
| fleet:desktop-3090 |  55 |  286 |   · |      — | health×106；verify=1×89                  |
| fleet:laptop-4090  |  27 |  134 |   · |      — | health×83；verify=None×24                |
| worker:gemma31     |   1 |   34 |   · |    2.2 | no output written by tra×34              |
| worker:laguna      |  79 |   74 |   · |  208.4 | no output written by tra×35；verify=1×15 |
| worker:mac         |  45 |  144 |   · |  205.3 | leak×77；verify=1×34                     |
| worker:nemo        | 199 |  299 |  +2 |  101.8 | leak×208；verify=1×50                    |
| worker:nemo2       | 172 |  219 |  +3 |   98.9 | leak×160；verify=1×36                    |
| worker:nemo3       | 142 |  210 |  +5 |   96.0 | leak×130；verify=1×42                    |
| worker:oss20       |  26 |   47 |  +1 |  404.1 | leak×21；verify=1×11                     |

endpoint 探活：local 🟢、laptop-4090 🟢、laptop-5090 🔴、desktop-3090 🟢、mac-m4max 🟢

（babel-pulse 常駐儀器自動快照）

## 2026-07-25T11:06:12+08:00（zh 總數 863）

| 語言 | fresh | stale | missing | 覆蓋率 | Δfresh | Δmissing |
| ---- | ----: | ----: | ------: | -----: | -----: | -------: |
| en   |   721 |   107 |      35 |  95.9% |     -1 |        · |
| ja   |   705 |   152 |       6 |  99.3% |     -1 |        · |
| ko   |   701 |   158 |       4 |  99.5% |     -1 |        · |
| es   |   709 |   151 |       3 |  99.7% |     -1 |        · |
| fr   |   706 |   156 |       1 |  99.9% |     -1 |        · |
| vi   |    90 |    10 |     763 |  11.6% |     +1 |       -2 |
| id   |   165 |     5 |     693 |  19.7% |     +4 |       -5 |
| pt   |   222 |    12 |     629 |  27.1% |     +4 |       -5 |
| hi   |   190 |     5 |     668 |  22.6% |     -2 |       +1 |
| ar   |    89 |     1 |     773 |  10.4% |     +4 |       -5 |
| ru   |    96 |     1 |     766 |  11.2% |     -1 |        · |

總缺口（stale+missing）：**5099**（▼5 vs 上一筆）

**節點／worker**（ok/fail 為累計；Δ為對上一筆）

| 節點               |  ok | fail | Δok | 平均秒 | 主要 fail                                |
| ------------------ | --: | ---: | --: | -----: | ---------------------------------------- |
| fleet:desktop-3090 |  55 |  292 |   · |      — | health×110；verify=1×90                  |
| fleet:laptop-4090  |  27 |  134 |   · |      — | health×83；verify=None×24                |
| worker:gemma31     |   1 |   34 |   · |    2.2 | no output written by tra×34              |
| worker:laguna      |  81 |   77 |  +2 |  206.2 | no output written by tra×36；verify=1×15 |
| worker:mac         |  45 |  144 |   · |  205.3 | leak×77；verify=1×34                     |
| worker:nemo        | 204 |  304 |  +5 |  100.5 | leak×213；verify=1×50                    |
| worker:nemo2       | 178 |  223 |  +6 |   97.8 | leak×163；verify=1×37                    |
| worker:nemo3       | 147 |  213 |  +5 |   96.3 | leak×133；verify=1×42                    |
| worker:oss20       |  26 |   49 |   · |  404.1 | leak×21；verify=1×12                     |

endpoint 探活：local 🟢、laptop-4090 🟢、laptop-5090 🔴、desktop-3090 🟢、mac-m4max 🟢

（babel-pulse 常駐儀器自動快照）

## 2026-07-25T11:21:31+08:00（zh 總數 863）

| 語言 | fresh | stale | missing | 覆蓋率 | Δfresh | Δmissing |
| ---- | ----: | ----: | ------: | -----: | -----: | -------: |
| en   |   721 |   107 |      35 |  95.9% |      · |        · |
| ja   |   705 |   152 |       6 |  99.3% |      · |        · |
| ko   |   701 |   158 |       4 |  99.5% |      · |        · |
| es   |   709 |   151 |       3 |  99.7% |      · |        · |
| fr   |   706 |   156 |       1 |  99.9% |      · |        · |
| vi   |    91 |    10 |     762 |  11.7% |     +1 |       -1 |
| id   |   174 |     5 |     684 |  20.7% |     +9 |       -9 |
| pt   |   228 |     9 |     626 |  27.5% |     +6 |       -3 |
| hi   |   194 |     5 |     664 |  23.1% |     +4 |       -4 |
| ar   |    94 |     1 |     768 |  11.0% |     +5 |       -5 |
| ru   |   100 |     1 |     762 |  11.7% |     +4 |       -4 |

總缺口（stale+missing）：**5070**（▼29 vs 上一筆）

**節點／worker**（ok/fail 為累計；Δ為對上一筆）

| 節點               |  ok | fail | Δok | 平均秒 | 主要 fail                                |
| ------------------ | --: | ---: | --: | -----: | ---------------------------------------- |
| fleet:desktop-3090 |  55 |  292 |   · |      — | health×110；verify=1×90                  |
| fleet:laptop-4090  |  27 |  137 |   · |      — | health×83；verify=None×24                |
| worker:gemma31     |   1 |   34 |   · |    2.2 | no output written by tra×34              |
| worker:laguna      |  82 |   80 |  +1 |  205.7 | no output written by tra×36；verify=1×15 |
| worker:mac         |  45 |  144 |   · |  205.3 | leak×77；verify=1×34                     |
| worker:nemo        | 210 |  310 |  +6 |   99.5 | leak×218；verify=1×51                    |
| worker:nemo2       | 187 |  229 |  +9 |   96.4 | leak×168；verify=1×38                    |
| worker:nemo3       | 154 |  220 |  +7 |   94.5 | leak×139；verify=1×42                    |
| worker:oss20       |  26 |   52 |   · |  404.1 | leak×23；verify=1×12                     |

endpoint 探活：local 🟢、laptop-4090 🟢、laptop-5090 🔴、desktop-3090 🟢、mac-m4max 🟢

（babel-pulse 常駐儀器自動快照）

## 2026-07-25T11:36:58+08:00（zh 總數 863）

| 語言 | fresh | stale | missing | 覆蓋率 | Δfresh | Δmissing |
| ---- | ----: | ----: | ------: | -----: | -----: | -------: |
| en   |   721 |   107 |      35 |  95.9% |      · |        · |
| ja   |   705 |   152 |       6 |  99.3% |      · |        · |
| ko   |   701 |   158 |       4 |  99.5% |      · |        · |
| es   |   709 |   151 |       3 |  99.7% |      · |        · |
| fr   |   706 |   156 |       1 |  99.9% |      · |        · |
| vi   |    93 |    10 |     760 |  11.9% |     +2 |       -2 |
| id   |   171 |     5 |     687 |  20.4% |     -3 |       +3 |
| pt   |   230 |     9 |     624 |  27.7% |     +2 |       -2 |
| hi   |   195 |     5 |     663 |  23.2% |     +1 |       -1 |
| ar   |   101 |     1 |     761 |  11.8% |     +7 |       -7 |
| ru   |   104 |     1 |     758 |  12.2% |     +4 |       -4 |

總缺口（stale+missing）：**5057**（▼13 vs 上一筆）

**節點／worker**（ok/fail 為累計；Δ為對上一筆）

| 節點               |  ok | fail | Δok | 平均秒 | 主要 fail                                |
| ------------------ | --: | ---: | --: | -----: | ---------------------------------------- |
| fleet:desktop-3090 |  55 |  302 |   · |      — | health×114；verify=1×93                  |
| fleet:laptop-4090  |  27 |  137 |   · |      — | health×83；verify=None×24                |
| worker:gemma31     |   1 |   34 |   · |    2.2 | no output written by tra×34              |
| worker:laguna      |  84 |   82 |  +2 |  204.8 | no output written by tra×38；verify=1×15 |
| worker:mac         |  45 |  144 |   · |  205.3 | leak×77；verify=1×34                     |
| worker:nemo        | 214 |  314 |  +4 |   99.5 | leak×221；verify=1×51                    |
| worker:nemo2       | 193 |  235 |  +6 |   95.5 | leak×172；verify=1×38                    |
| worker:nemo3       | 161 |  222 |  +7 |   94.7 | leak×141；verify=1×42                    |
| worker:oss20       |  27 |   53 |  +1 |  403.3 | leak×24；verify=1×12                     |

endpoint 探活：local 🟢、laptop-4090 🟢、laptop-5090 🔴、desktop-3090 🟢、mac-m4max 🟢

（babel-pulse 常駐儀器自動快照）

## 2026-07-25T11:52:46+08:00（zh 總數 863）

| 語言 | fresh | stale | missing | 覆蓋率 | Δfresh | Δmissing |
| ---- | ----: | ----: | ------: | -----: | -----: | -------: |
| en   |   721 |   107 |      35 |  95.9% |      · |        · |
| ja   |   705 |   152 |       6 |  99.3% |      · |        · |
| ko   |   701 |   158 |       4 |  99.5% |      · |        · |
| es   |   709 |   151 |       3 |  99.7% |      · |        · |
| fr   |   706 |   156 |       1 |  99.9% |      · |        · |
| vi   |    94 |    10 |     759 |  12.1% |     +1 |       -1 |
| id   |   179 |     5 |     679 |  21.3% |     +8 |       -8 |
| pt   |   234 |     9 |     620 |  28.2% |     +4 |       -4 |
| hi   |   198 |     5 |     660 |  23.5% |     +3 |       -3 |
| ar   |   104 |     1 |     758 |  12.2% |     +3 |       -3 |
| ru   |   107 |     1 |     755 |  12.5% |     +3 |       -3 |

總缺口（stale+missing）：**5035**（▼22 vs 上一筆）

**節點／worker**（ok/fail 為累計；Δ為對上一筆）

| 節點               |  ok | fail | Δok | 平均秒 | 主要 fail                                |
| ------------------ | --: | ---: | --: | -----: | ---------------------------------------- |
| fleet:desktop-3090 |  55 |  302 |   · |      — | health×114；verify=1×93                  |
| fleet:laptop-4090  |  27 |  137 |   · |      — | health×83；verify=None×24                |
| worker:gemma31     |   1 |   34 |   · |    2.2 | no output written by tra×34              |
| worker:laguna      |  87 |   85 |  +3 |  201.4 | no output written by tra×39；verify=1×16 |
| worker:mac         |  45 |  144 |   · |  205.3 | leak×77；verify=1×34                     |
| worker:nemo        | 218 |  319 |  +4 |  100.1 | leak×226；verify=1×51                    |
| worker:nemo2       | 200 |  238 |  +7 |   95.2 | leak×174；verify=1×38                    |
| worker:nemo3       | 164 |  229 |  +3 |   94.6 | leak×143；verify=1×42                    |
| worker:oss20       |  27 |   54 |   · |  403.3 | leak×24；verify=1×12                     |

endpoint 探活：local 🟢、laptop-4090 🟢、laptop-5090 🔴、desktop-3090 🟢、mac-m4max 🟢

（babel-pulse 常駐儀器自動快照）

## 2026-07-25T12:00:10+08:00（zh 總數 863）

| 語言 | fresh | stale | missing | 覆蓋率 | Δfresh | Δmissing |
| ---- | ----: | ----: | ------: | -----: | -----: | -------: |
| en   |   721 |   107 |      35 |  95.9% |      · |        · |
| ja   |   705 |   152 |       6 |  99.3% |      · |        · |
| ko   |   701 |   158 |       4 |  99.5% |      · |        · |
| es   |   709 |   151 |       3 |  99.7% |      · |        · |
| fr   |   706 |   156 |       1 |  99.9% |      · |        · |
| vi   |    94 |    10 |     759 |  12.1% |      · |        · |
| id   |   175 |     5 |     683 |  20.9% |     -4 |       +4 |
| pt   |   236 |     9 |     618 |  28.4% |     +2 |       -2 |
| hi   |   198 |     5 |     660 |  23.5% |      · |        · |
| ar   |   105 |     1 |     757 |  12.3% |     +1 |       -1 |
| ru   |   110 |     1 |     752 |  12.9% |     +3 |       -3 |

總缺口（stale+missing）：**5033**（▼2 vs 上一筆）

**節點／worker**（ok/fail 為累計；Δ為對上一筆）

| 節點               |  ok | fail | Δok | 平均秒 | 主要 fail                                |
| ------------------ | --: | ---: | --: | -----: | ---------------------------------------- |
| fleet:desktop-3090 |  55 |  310 |   · |      — | health×118；verify=1×96                  |
| fleet:laptop-4090  |  27 |  137 |   · |      — | health×83；verify=None×24                |
| worker:gemma31     |   1 |   34 |   · |    2.2 | no output written by tra×34              |
| worker:laguna      |  88 |   87 |  +1 |  199.8 | no output written by tra×41；verify=1×16 |
| worker:mac         |  45 |  144 |   · |  205.3 | leak×77；verify=1×34                     |
| worker:nemo        | 221 |  323 |  +3 |   99.5 | leak×229；verify=1×51                    |
| worker:nemo2       | 202 |  240 |  +2 |   95.0 | leak×176；verify=1×38                    |
| worker:nemo3       | 167 |  232 |  +3 |   94.5 | leak×146；verify=1×42                    |
| worker:oss20       |  27 |   55 |   · |  403.3 | leak×25；verify=1×12                     |

endpoint 探活：local 🟢、laptop-4090 🟢、laptop-5090 🔴、desktop-3090 🟢、mac-m4max 🟢

（babel-pulse 常駐儀器自動快照）

## 2026-07-25T12:08:20+08:00（zh 總數 863）

| 語言 | fresh | stale | missing | 覆蓋率 | Δfresh | Δmissing |
| ---- | ----: | ----: | ------: | -----: | -----: | -------: |
| en   |   721 |   107 |      35 |  95.9% |      · |        · |
| ja   |   705 |   152 |       6 |  99.3% |      · |        · |
| ko   |   701 |   158 |       4 |  99.5% |      · |        · |
| es   |   709 |   151 |       3 |  99.7% |      · |        · |
| fr   |   706 |   156 |       1 |  99.9% |      · |        · |
| vi   |    96 |    10 |     757 |  12.3% |     +2 |       -2 |
| id   |   178 |     5 |     680 |  21.2% |     +3 |       -3 |
| pt   |   238 |     9 |     616 |  28.6% |     +2 |       -2 |
| hi   |   199 |     5 |     659 |  23.6% |     +1 |       -1 |
| ar   |   105 |     1 |     757 |  12.3% |      · |        · |
| ru   |   112 |     1 |     750 |  13.1% |     +2 |       -2 |

總缺口（stale+missing）：**5023**（▼10 vs 上一筆）

**節點／worker**（ok/fail 為累計；Δ為對上一筆）

| 節點               |  ok | fail | Δok | 平均秒 | 主要 fail                                |
| ------------------ | --: | ---: | --: | -----: | ---------------------------------------- |
| fleet:desktop-3090 |  55 |  310 |   · |      — | health×118；verify=1×96                  |
| fleet:laptop-4090  |  27 |  137 |   · |      — | health×83；verify=None×24                |
| worker:gemma31     |   1 |   34 |   · |    2.2 | no output written by tra×34              |
| worker:laguna      |  92 |   87 |  +4 |  195.2 | no output written by tra×41；verify=1×16 |
| worker:mac         |  45 |  144 |   · |  205.3 | leak×77；verify=1×34                     |
| worker:nemo        | 223 |  326 |  +2 |   99.3 | leak×231；verify=1×52                    |
| worker:nemo2       | 203 |  244 |  +1 |   94.8 | leak×179；verify=1×39                    |
| worker:nemo3       | 167 |  234 |   · |   94.5 | leak×148；verify=1×42                    |
| worker:oss20       |  27 |   55 |   · |  403.3 | leak×25；verify=1×12                     |

endpoint 探活：local 🟢、laptop-4090 🟢、laptop-5090 🔴、desktop-3090 🟢、mac-m4max 🟢

（babel-pulse 常駐儀器自動快照）

## 2026-07-25T12:24:17+08:00（zh 總數 863）

| 語言 | fresh | stale | missing | 覆蓋率 | Δfresh | Δmissing |
| ---- | ----: | ----: | ------: | -----: | -----: | -------: |
| en   |   721 |   107 |      35 |  95.9% |      · |        · |
| ja   |   705 |   152 |       6 |  99.3% |      · |        · |
| ko   |   701 |   158 |       4 |  99.5% |      · |        · |
| es   |   709 |   151 |       3 |  99.7% |      · |        · |
| fr   |   706 |   156 |       1 |  99.9% |      · |        · |
| vi   |    97 |    10 |     756 |  12.4% |     +1 |       -1 |
| id   |   185 |     5 |     673 |  22.0% |     +7 |       -7 |
| pt   |   242 |     9 |     612 |  29.1% |     +4 |       -4 |
| hi   |   200 |     5 |     658 |  23.8% |     +1 |       -1 |
| ar   |   107 |     1 |     755 |  12.5% |     +2 |       -2 |
| ru   |   116 |     1 |     746 |  13.6% |     +4 |       -4 |

總缺口（stale+missing）：**5004**（▼19 vs 上一筆）

**節點／worker**（ok/fail 為累計；Δ為對上一筆）

| 節點               |  ok | fail | Δok | 平均秒 | 主要 fail                                |
| ------------------ | --: | ---: | --: | -----: | ---------------------------------------- |
| fleet:desktop-3090 |  55 |  310 |   · |      — | health×118；verify=1×96                  |
| fleet:laptop-4090  |  27 |  137 |   · |      — | health×83；verify=None×24                |
| worker:gemma31     |   1 |   34 |   · |    2.2 | no output written by tra×34              |
| worker:laguna      |  93 |   91 |  +1 |  194.1 | no output written by tra×44；verify=1×16 |
| worker:mac         |  45 |  145 |   · |  205.3 | leak×78；verify=1×34                     |
| worker:nemo        | 229 |  328 |  +6 |   98.9 | leak×233；verify=1×52                    |
| worker:nemo2       | 206 |  247 |  +3 |   94.2 | leak×181；verify=1×39                    |
| worker:nemo3       | 172 |  239 |  +5 |   93.6 | leak×153；verify=1×42                    |
| worker:oss20       |  28 |   56 |  +1 |  402.6 | leak×25；verify=1×13                     |

endpoint 探活：local 🟢、laptop-4090 🟢、laptop-5090 🔴、desktop-3090 🟢、mac-m4max 🟢

（babel-pulse 常駐儀器自動快照）

## 2026-07-25T12:39:47+08:00（zh 總數 863）

| 語言 | fresh | stale | missing | 覆蓋率 | Δfresh | Δmissing |
| ---- | ----: | ----: | ------: | -----: | -----: | -------: |
| en   |   721 |   107 |      35 |  95.9% |      · |        · |
| ja   |   706 |   152 |       5 |  99.4% |     +1 |       -1 |
| ko   |   701 |   158 |       4 |  99.5% |      · |        · |
| es   |   709 |   151 |       3 |  99.7% |      · |        · |
| fr   |   706 |   156 |       1 |  99.9% |      · |        · |
| vi   |    98 |    10 |     755 |  12.5% |     +1 |       -1 |
| id   |   183 |     4 |     676 |  21.7% |     -2 |       +3 |
| pt   |   248 |     9 |     606 |  29.8% |     +6 |       -6 |
| hi   |   203 |     5 |     655 |  24.1% |     +3 |       -3 |
| ar   |   111 |     1 |     751 |  13.0% |     +4 |       -4 |
| ru   |   122 |     1 |     740 |  14.3% |     +6 |       -6 |

總缺口（stale+missing）：**4985**（▼19 vs 上一筆）

**節點／worker**（ok/fail 為累計；Δ為對上一筆）

| 節點               |  ok | fail | Δok | 平均秒 | 主要 fail                                |
| ------------------ | --: | ---: | --: | -----: | ---------------------------------------- |
| fleet:desktop-3090 |  56 |  318 |  +1 |      — | health×119；verify=1×100                 |
| fleet:laptop-4090  |  27 |  137 |   · |      — | health×83；verify=None×24                |
| worker:gemma31     |   1 |   34 |   · |    2.2 | no output written by tra×34              |
| worker:laguna      |  98 |   93 |  +5 |  189.1 | no output written by tra×46；verify=1×16 |
| worker:mac         |  46 |  146 |  +1 |  211.7 | leak×79；verify=1×34                     |
| worker:nemo        | 234 |  336 |  +5 |   98.5 | leak×239；verify=1×53                    |
| worker:nemo2       | 212 |  252 |  +6 |   93.3 | leak×184；verify=1×39                    |
| worker:nemo3       | 177 |  244 |  +5 |   92.6 | leak×156；verify=1×43                    |
| worker:oss20       |  29 |   57 |  +1 |  413.9 | leak×25；verify=1×13                     |

endpoint 探活：local 🟢、laptop-4090 🟢、laptop-5090 🔴、desktop-3090 🟢、mac-m4max 🟢

（babel-pulse 常駐儀器自動快照）

## 2026-07-25T12:55:21+08:00（zh 總數 863）

| 語言 | fresh | stale | missing | 覆蓋率 | Δfresh | Δmissing |
| ---- | ----: | ----: | ------: | -----: | -----: | -------: |
| en   |   721 |   107 |      35 |  95.9% |      · |        · |
| ja   |   706 |   152 |       5 |  99.4% |      · |        · |
| ko   |   702 |   157 |       4 |  99.5% |     +1 |        · |
| es   |   710 |   151 |       2 |  99.8% |     +1 |       -1 |
| fr   |   706 |   156 |       1 |  99.9% |      · |        · |
| vi   |    99 |    10 |     754 |  12.6% |     +1 |       -1 |
| id   |   187 |     4 |     672 |  22.1% |     +4 |       -4 |
| pt   |   253 |     9 |     601 |  30.4% |     +5 |       -5 |
| hi   |   206 |     5 |     652 |  24.4% |     +3 |       -3 |
| ar   |   117 |     1 |     745 |  13.7% |     +6 |       -6 |
| ru   |   126 |     1 |     736 |  14.7% |     +4 |       -4 |

總缺口（stale+missing）：**4960**（▼25 vs 上一筆）

**節點／worker**（ok/fail 為累計；Δ為對上一筆）

| 節點                |  ok | fail | Δok | 平均秒 | 主要 fail                                |
| ------------------- | --: | ---: | --: | -----: | ---------------------------------------- |
| fleet:desktop-3090  |  56 |  318 |   · |      — | health×119；verify=1×100                 |
| fleet:laptop-4090   |  27 |  137 |   · |      — | health×83；verify=None×24                |
| worker:desktop30901 |   1 |    1 |   — |  251.2 | health×1                                 |
| worker:desktop30902 |   0 |    1 |   — |      — | health×1                                 |
| worker:gemma31      |   1 |   34 |   · |    2.2 | no output written by tra×34              |
| worker:laguna       |  99 |   93 |  +1 |  187.6 | no output written by tra×46；verify=1×16 |
| worker:mac          |  46 |  147 |   · |  211.7 | leak×80；verify=1×34                     |
| worker:nemo         | 240 |  345 |  +6 |   97.3 | leak×245；verify=1×54                    |
| worker:nemo2        | 216 |  259 |  +4 |   92.5 | leak×191；verify=1×39                    |
| worker:nemo3        | 181 |  247 |  +4 |   92.7 | leak×159；verify=1×43                    |
| worker:oss20        |  30 |   57 |  +1 |  410.4 | leak×25；verify=1×13                     |

endpoint 探活：local 🟢、laptop-4090 🟢、laptop-5090 🔴、desktop-3090 🟢、mac-m4max 🟢

（babel-pulse 常駐儀器自動快照）

## 2026-07-25T13:11:10+08:00（zh 總數 863）

| 語言 | fresh | stale | missing | 覆蓋率 | Δfresh | Δmissing |
| ---- | ----: | ----: | ------: | -----: | -----: | -------: |
| en   |   721 |   107 |      35 |  95.9% |      · |        · |
| ja   |   707 |   151 |       5 |  99.4% |     +1 |        · |
| ko   |   702 |   157 |       4 |  99.5% |      · |        · |
| es   |   710 |   151 |       2 |  99.8% |      · |        · |
| fr   |   706 |   156 |       1 |  99.9% |      · |        · |
| vi   |    99 |    10 |     754 |  12.6% |      · |        · |
| id   |   192 |     4 |     667 |  22.7% |     +5 |       -5 |
| pt   |   256 |     9 |     598 |  30.7% |     +3 |       -3 |
| hi   |   210 |     5 |     648 |  24.9% |     +4 |       -4 |
| ar   |   122 |     1 |     740 |  14.3% |     +5 |       -5 |
| ru   |   131 |     1 |     731 |  15.3% |     +5 |       -5 |

總缺口（stale+missing）：**4937**（▼23 vs 上一筆）

**節點／worker**（ok/fail 為累計；Δ為對上一筆）

| 節點                |  ok | fail | Δok | 平均秒 | 主要 fail                                |
| ------------------- | --: | ---: | --: | -----: | ---------------------------------------- |
| fleet:desktop-3090  |  56 |  318 |   · |      — | health×119；verify=1×100                 |
| fleet:laptop-4090   |  27 |  137 |   · |      — | health×83；verify=None×24                |
| worker:desktop30901 |   2 |    3 |  +1 |  257.1 | health×3                                 |
| worker:desktop30902 |   1 |    4 |  +1 |  280.6 | health×3；verify=3×1                     |
| worker:gemma31      |   1 |   34 |   · |    2.2 | no output written by tra×34              |
| worker:laguna       |  99 |   96 |   · |  187.6 | no output written by tra×48；verify=1×16 |
| worker:laptop40901  |   1 |    0 |   — |  900.2 | —                                        |
| worker:laptop40902  |   0 |    1 |   — |      — | verify=1×1                               |
| worker:mac          |  46 |  150 |   · |  211.7 | leak×83；verify=1×34                     |
| worker:nemo         | 248 |  356 |  +8 |   97.6 | leak×256；verify=1×54                    |
| worker:nemo2        | 223 |  270 |  +7 |   92.7 | leak×198；verify=1×40                    |
| worker:nemo3        | 185 |  253 |  +4 |   92.8 | leak×164；verify=1×43                    |
| worker:oss20        |  30 |   58 |   · |  410.4 | leak×25；verify=1×13                     |

endpoint 探活：local 🟢、laptop-4090 🟢、laptop-5090 🔴、desktop-3090 🟢、mac-m4max 🟢

（babel-pulse 常駐儀器自動快照）

## 2026-07-25T13:26:42+08:00（zh 總數 863）

| 語言 | fresh | stale | missing | 覆蓋率 | Δfresh | Δmissing |
| ---- | ----: | ----: | ------: | -----: | -----: | -------: |
| en   |   723 |   106 |      34 |  96.1% |     +2 |       -1 |
| ja   |   708 |   150 |       5 |  99.4% |     +1 |        · |
| ko   |   702 |   157 |       4 |  99.5% |      · |        · |
| es   |   710 |   151 |       2 |  99.8% |      · |        · |
| fr   |   707 |   155 |       1 |  99.9% |     +1 |        · |
| vi   |   100 |    10 |     753 |  12.7% |     +1 |       -1 |
| id   |   192 |     4 |     667 |  22.7% |      · |        · |
| pt   |   261 |     9 |     593 |  31.3% |     +5 |       -5 |
| hi   |   213 |     5 |     645 |  25.3% |     +3 |       -3 |
| ar   |   125 |     1 |     737 |  14.6% |     +3 |       -3 |
| ru   |   135 |     1 |     727 |  15.8% |     +4 |       -4 |

總缺口（stale+missing）：**4917**（▼20 vs 上一筆）

**節點／worker**（ok/fail 為累計；Δ為對上一筆）

| 節點                |  ok | fail | Δok | 平均秒 | 主要 fail                                |
| ------------------- | --: | ---: | --: | -----: | ---------------------------------------- |
| fleet:desktop-3090  |  56 |  325 |   · |      — | health×123；verify=1×102                 |
| fleet:laptop-4090   |  27 |  137 |   · |      — | health×83；verify=None×24                |
| worker:desktop30901 |   5 |    3 |  +3 |  301.2 | health×3                                 |
| worker:desktop30902 |   3 |    5 |  +2 |  304.3 | health×4；verify=3×1                     |
| worker:gemma31      |   1 |   34 |   · |    2.2 | no output written by tra×34              |
| worker:laguna       | 100 |   99 |  +1 |  186.8 | no output written by tra×51；verify=1×16 |
| worker:laptop40901  |   2 |    0 |  +1 |  900.2 | —                                        |
| worker:laptop40902  |   1 |    1 |  +1 |  900.4 | verify=1×1                               |
| worker:mac          |  46 |  152 |   · |  211.7 | leak×85；verify=1×34                     |
| worker:nemo         | 254 |  369 |  +6 |   98.1 | leak×265；verify=1×58                    |
| worker:nemo2        | 230 |  286 |  +7 |   93.6 | leak×209；verify=1×42                    |
| worker:nemo3        | 190 |  261 |  +5 |   92.0 | leak×168；verify=1×45                    |
| worker:oss20        |  31 |   59 |  +1 |  461.8 | leak×25；verify=1×13                     |

endpoint 探活：local 🟢、laptop-4090 🟢、laptop-5090 🔴、desktop-3090 🟢、mac-m4max 🟢

（babel-pulse 常駐儀器自動快照）

## 2026-07-25T13:40:45+08:00（zh 總數 863）

| 語言 | fresh | stale | missing | 覆蓋率 | Δfresh | Δmissing |
| ---- | ----: | ----: | ------: | -----: | -----: | -------: |
| en   |   723 |   106 |      34 |  96.1% |      · |        · |
| ja   |   709 |   149 |       5 |  99.4% |     +1 |        · |
| ko   |   703 |   156 |       4 |  99.5% |     +1 |        · |
| es   |   712 |   149 |       2 |  99.8% |     +2 |        · |
| fr   |   707 |   155 |       1 |  99.9% |      · |        · |
| vi   |   100 |    10 |     753 |  12.7% |      · |        · |
| id   |   194 |     3 |     666 |  22.8% |     +2 |       -1 |
| pt   |   267 |     9 |     587 |  32.0% |     +6 |       -6 |
| hi   |   216 |     5 |     642 |  25.6% |     +3 |       -3 |
| ar   |   128 |     1 |     734 |  14.9% |     +3 |       -3 |
| ru   |   139 |     1 |     723 |  16.2% |     +4 |       -4 |

總缺口（stale+missing）：**4895**（▼22 vs 上一筆）

**節點／worker**（ok/fail 為累計；Δ為對上一筆）

| 節點                |  ok | fail | Δok | 平均秒 | 主要 fail                                |
| ------------------- | --: | ---: | --: | -----: | ---------------------------------------- |
| fleet:desktop-3090  |  56 |  325 |   · |      — | health×123；verify=1×102                 |
| fleet:laptop-4090   |  27 |  137 |   · |      — | health×83；verify=None×24                |
| worker:desktop30901 |   6 |    3 |  +1 |  319.8 | health×3                                 |
| worker:desktop30902 |   4 |    5 |  +1 |  331.9 | health×4；verify=3×1                     |
| worker:gemma31      |   1 |   34 |   · |    2.2 | no output written by tra×34              |
| worker:laguna       | 101 |  100 |  +1 |  186.8 | no output written by tra×51；verify=1×16 |
| worker:laptop40901  |   3 |    0 |  +1 |  900.3 | —                                        |
| worker:laptop40902  |   2 |    1 |  +1 |  900.3 | verify=1×1                               |
| worker:mac          |  47 |  153 |  +1 |  211.9 | leak×86；verify=1×34                     |
| worker:nemo         | 260 |  377 |  +6 |   98.9 | leak×272；verify=1×58                    |
| worker:nemo2        | 236 |  294 |  +6 |   94.2 | leak×215；verify=1×42                    |
| worker:nemo3        | 194 |  266 |  +4 |   91.8 | leak×173；verify=1×45                    |
| worker:oss20        |  32 |   60 |  +1 |  460.4 | leak×25；verify=1×13                     |

endpoint 探活：local 🟢、laptop-4090 🟢、laptop-5090 🔴、desktop-3090 🟢、mac-m4max 🟢

（babel-pulse 常駐儀器自動快照）

## 2026-07-25T13:41:58+08:00（zh 總數 863）

| 語言 | fresh | stale | missing | 覆蓋率 | Δfresh | Δmissing |
| ---- | ----: | ----: | ------: | -----: | -----: | -------: |
| en   |   723 |   106 |      34 |  96.1% |      · |        · |
| ja   |   709 |   149 |       5 |  99.4% |      · |        · |
| ko   |   703 |   156 |       4 |  99.5% |      · |        · |
| es   |   712 |   149 |       2 |  99.8% |      · |        · |
| fr   |   707 |   155 |       1 |  99.9% |      · |        · |
| vi   |   101 |    10 |     752 |  12.9% |     +1 |       -1 |
| id   |   194 |     3 |     666 |  22.8% |      · |        · |
| pt   |   267 |     9 |     587 |  32.0% |      · |        · |
| hi   |   216 |     5 |     642 |  25.6% |      · |        · |
| ar   |   128 |     1 |     734 |  14.9% |      · |        · |
| ru   |   139 |     1 |     723 |  16.2% |      · |        · |

總缺口（stale+missing）：**4894**（▼1 vs 上一筆）

**節點／worker**（ok/fail 為累計；Δ為對上一筆）

| 節點                |  ok | fail | Δok | 平均秒 | 主要 fail                                |
| ------------------- | --: | ---: | --: | -----: | ---------------------------------------- |
| fleet:desktop-3090  |  56 |  325 |   · |      — | health×123；verify=1×102                 |
| fleet:laptop-4090   |  27 |  137 |   · |      — | health×83；verify=None×24                |
| worker:desktop30901 |   6 |    3 |   · |  319.8 | health×3                                 |
| worker:desktop30902 |   4 |    5 |   · |  331.9 | health×4；verify=3×1                     |
| worker:gemma31      |   1 |   34 |   · |    2.2 | no output written by tra×34              |
| worker:laguna       | 101 |  100 |   · |  186.8 | no output written by tra×51；verify=1×16 |
| worker:laptop40901  |   3 |    0 |   · |  900.3 | —                                        |
| worker:laptop40902  |   2 |    1 |   · |  900.3 | verify=1×1                               |
| worker:mac          |  47 |  154 |   · |  211.9 | leak×87；verify=1×34                     |
| worker:nemo         | 260 |  377 |   · |   98.9 | leak×272；verify=1×58                    |
| worker:nemo2        | 236 |  294 |   · |   94.2 | leak×215；verify=1×42                    |
| worker:nemo3        | 194 |  266 |   · |   91.8 | leak×173；verify=1×45                    |
| worker:oss20        |  32 |   61 |   · |  460.4 | leak×26；verify=1×13                     |

endpoint 探活：local 🟢、laptop-4090 🟢、laptop-5090 🔴、desktop-3090 🟢、mac-m4max 🟢

（babel-pulse 常駐儀器自動快照）

## 2026-07-25T13:50:24+08:00（zh 總數 863）

| 語言 | fresh | stale | missing | 覆蓋率 | Δfresh | Δmissing |
| ---- | ----: | ----: | ------: | -----: | -----: | -------: |
| en   |   723 |   106 |      34 |  96.1% |      · |        · |
| ja   |   710 |   148 |       5 |  99.4% |     +1 |        · |
| ko   |   704 |   155 |       4 |  99.5% |     +1 |        · |
| es   |   713 |   148 |       2 |  99.8% |     +1 |        · |
| fr   |   707 |   155 |       1 |  99.9% |      · |        · |
| vi   |   103 |    10 |     750 |  13.1% |     +2 |       -2 |
| id   |   196 |     3 |     664 |  23.1% |     +2 |       -2 |
| pt   |   270 |     9 |     584 |  32.3% |     +3 |       -3 |
| hi   |   217 |     5 |     641 |  25.7% |     +1 |       -1 |
| ar   |   129 |     1 |     733 |  15.1% |     +1 |       -1 |
| ru   |   142 |     1 |     720 |  16.6% |     +3 |       -3 |

總缺口（stale+missing）：**4879**（▼15 vs 上一筆）

**節點／worker**（ok/fail 為累計；Δ為對上一筆）

| 節點                |  ok | fail | Δok | 平均秒 | 主要 fail                                |
| ------------------- | --: | ---: | --: | -----: | ---------------------------------------- |
| fleet:desktop-3090  |  56 |  325 |   · |      — | health×123；verify=1×102                 |
| fleet:laptop-4090   |  27 |  137 |   · |      — | health×83；verify=None×24                |
| worker:desktop30901 |   8 |    3 |  +2 |  361.6 | health×3                                 |
| worker:desktop30902 |   6 |    5 |  +2 |  361.2 | health×4；verify=3×1                     |
| worker:gemma31      |   1 |   34 |   · |    2.2 | no output written by tra×34              |
| worker:laguna       | 101 |  102 |   · |  186.8 | no output written by tra×52；verify=1×16 |
| worker:laptop40901  |   3 |    1 |   · |  900.3 | no output written by tra×1               |
| worker:laptop40902  |   3 |    1 |  +1 |  900.3 | verify=1×1                               |
| worker:mac          |  47 |  155 |   · |  211.9 | leak×87；verify=1×34                     |
| worker:nemo         | 264 |  382 |  +4 |   99.7 | leak×275；verify=1×58                    |
| worker:nemo2        | 237 |  302 |  +1 |   94.3 | leak×220；verify=1×42                    |
| worker:nemo3        | 197 |  266 |  +3 |   92.4 | leak×173；verify=1×45                    |
| worker:oss20        |  32 |   61 |   · |  460.4 | leak×26；verify=1×13                     |

endpoint 探活：local 🟢、laptop-4090 🟢、laptop-5090 🔴、desktop-3090 🟢、mac-m4max 🟢

（babel-pulse 常駐儀器自動快照）

## 2026-07-25T13:57:33+08:00（zh 總數 863）

| 語言 | fresh | stale | missing | 覆蓋率 | Δfresh | Δmissing |
| ---- | ----: | ----: | ------: | -----: | -----: | -------: |
| en   |   723 |   106 |      34 |  96.1% |      · |        · |
| ja   |   710 |   148 |       5 |  99.4% |      · |        · |
| ko   |   706 |   154 |       3 |  99.7% |     +2 |       -1 |
| es   |   714 |   147 |       2 |  99.8% |     +1 |        · |
| fr   |   707 |   155 |       1 |  99.9% |      · |        · |
| vi   |   103 |    10 |     750 |  13.1% |      · |        · |
| id   |   197 |     3 |     663 |  23.2% |     +1 |       -1 |
| pt   |   272 |     9 |     582 |  32.6% |     +2 |       -2 |
| hi   |   218 |     5 |     640 |  25.8% |     +1 |       -1 |
| ar   |   131 |     1 |     731 |  15.3% |     +2 |       -2 |
| ru   |   144 |     1 |     718 |  16.8% |     +2 |       -2 |

總缺口（stale+missing）：**4868**（▼11 vs 上一筆）

**節點／worker**（ok/fail 為累計；Δ為對上一筆）

| 節點                |  ok | fail | Δok | 平均秒 | 主要 fail                                |
| ------------------- | --: | ---: | --: | -----: | ---------------------------------------- |
| fleet:desktop-3090  |  56 |  325 |   · |      — | health×123；verify=1×102                 |
| fleet:laptop-4090   |  27 |  137 |   · |      — | health×83；verify=None×24                |
| worker:desktop30901 |   9 |    3 |  +1 |  349.5 | health×3                                 |
| worker:desktop30902 |   7 |    5 |  +1 |  349.0 | health×4；verify=3×1                     |
| worker:gemma31      |   1 |   34 |   · |    2.2 | no output written by tra×34              |
| worker:laguna       | 101 |  103 |   · |  186.8 | no output written by tra×53；verify=1×16 |
| worker:laptop40901  |   3 |    1 |   · |  900.3 | no output written by tra×1               |
| worker:laptop40902  |   3 |    1 |   · |  900.3 | verify=1×1                               |
| worker:mac          |  47 |  155 |   · |  211.9 | leak×87；verify=1×34                     |
| worker:nemo         | 267 |  385 |  +3 |   99.8 | leak×277；verify=1×59                    |
| worker:nemo2        | 240 |  303 |  +3 |   94.6 | leak×221；verify=1×42                    |
| worker:nemo3        | 197 |  266 |   · |   92.4 | leak×173；verify=1×45                    |
| worker:oss20        |  32 |   61 |   · |  460.4 | leak×26；verify=1×13                     |

endpoint 探活：local 🟢、laptop-4090 🟢、laptop-5090 🔴、desktop-3090 🟢、mac-m4max 🟢

（babel-pulse 常駐儀器自動快照）

## 2026-07-25T14:13:03+08:00（zh 總數 863）

| 語言 | fresh | stale | missing | 覆蓋率 | Δfresh | Δmissing |
| ---- | ----: | ----: | ------: | -----: | -----: | -------: |
| en   |   723 |   106 |      34 |  96.1% |      · |        · |
| ja   |   710 |   148 |       5 |  99.4% |      · |        · |
| ko   |   706 |   154 |       3 |  99.7% |      · |        · |
| es   |   714 |   147 |       2 |  99.8% |      · |        · |
| fr   |   707 |   155 |       1 |  99.9% |      · |        · |
| vi   |   103 |    10 |     750 |  13.1% |      · |        · |
| id   |   198 |     3 |     662 |  23.3% |     +1 |       -1 |
| pt   |   273 |     9 |     581 |  32.7% |     +1 |       -1 |
| hi   |   218 |     5 |     640 |  25.8% |      · |        · |
| ar   |   133 |     1 |     729 |  15.5% |     +2 |       -2 |
| ru   |   145 |     1 |     717 |  16.9% |     +1 |       -1 |

總缺口（stale+missing）：**4863**（▼5 vs 上一筆）

**節點／worker**（ok/fail 為累計；Δ為對上一筆）

| 節點                |  ok | fail | Δok | 平均秒 | 主要 fail                                |
| ------------------- | --: | ---: | --: | -----: | ---------------------------------------- |
| fleet:desktop-3090  |  56 |  325 |   · |      — | health×123；verify=1×102                 |
| fleet:laptop-4090   |  27 |  137 |   · |      — | health×83；verify=None×24                |
| worker:d3090        |   1 |    0 |   — |  900.2 | —                                        |
| worker:desktop30901 |   9 |    4 |   · |  349.5 | health×3；verify=4×1                     |
| worker:desktop30902 |   8 |    5 |  +1 |  417.9 | health×4；verify=3×1                     |
| worker:gemma31      |   1 |   34 |   · |    2.2 | no output written by tra×34              |
| worker:l4090        |   1 |    0 |   — |  900.2 | —                                        |
| worker:laguna       | 102 |  104 |  +1 |  191.0 | no output written by tra×54；verify=1×16 |
| worker:laptop40901  |   4 |    1 |  +1 |  900.3 | no output written by tra×1               |
| worker:laptop40902  |   4 |    1 |  +1 |  900.3 | verify=1×1                               |
| worker:mac          |  48 |  157 |  +1 |  215.7 | leak×88；verify=1×35                     |
| worker:nemo         | 269 |  390 |  +2 |  100.7 | leak×282；verify=1×59                    |
| worker:nemo2        | 243 |  308 |  +3 |   96.9 | leak×224；verify=1×43                    |
| worker:nemo3        | 197 |  267 |   · |   92.4 | leak×173；verify=1×45                    |
| worker:oss20        |  32 |   62 |   · |  460.4 | leak×26；verify=1×13                     |

endpoint 探活：local 🟢、laptop-4090 🟢、laptop-5090 🔴、desktop-3090 🟢、mac-m4max 🟢

（babel-pulse 常駐儀器自動快照）

## 2026-07-25T14:28:30+08:00（zh 總數 863）

| 語言 | fresh | stale | missing | 覆蓋率 | Δfresh | Δmissing |
| ---- | ----: | ----: | ------: | -----: | -----: | -------: |
| en   |   723 |   106 |      34 |  96.1% |      · |        · |
| ja   |   710 |   148 |       5 |  99.4% |      · |        · |
| ko   |   706 |   154 |       3 |  99.7% |      · |        · |
| es   |   714 |   147 |       2 |  99.8% |      · |        · |
| fr   |   707 |   155 |       1 |  99.9% |      · |        · |
| vi   |   103 |    10 |     750 |  13.1% |      · |        · |
| id   |   199 |     3 |     661 |  23.4% |     +1 |       -1 |
| pt   |   278 |     9 |     576 |  33.3% |     +5 |       -5 |
| hi   |   218 |     5 |     640 |  25.8% |      · |        · |
| ar   |   135 |     1 |     727 |  15.8% |     +2 |       -2 |
| ru   |   146 |     1 |     716 |  17.0% |     +1 |       -1 |

總缺口（stale+missing）：**4854**（▼9 vs 上一筆）

**節點／worker**（ok/fail 為累計；Δ為對上一筆）

| 節點                |  ok | fail | Δok | 平均秒 | 主要 fail                                |
| ------------------- | --: | ---: | --: | -----: | ---------------------------------------- |
| fleet:desktop-3090  |  56 |  325 |   · |      — | health×123；verify=1×102                 |
| fleet:laptop-4090   |  27 |  137 |   · |      — | health×83；verify=None×24                |
| worker:d3090        |   2 |    0 |  +1 |  900.2 | —                                        |
| worker:desktop30901 |  10 |    4 |  +1 |  404.6 | health×3；verify=4×1                     |
| worker:desktop30902 |   9 |    5 |  +1 |  471.5 | health×4；verify=3×1                     |
| worker:gemma31      |   1 |   34 |   · |    2.2 | no output written by tra×34              |
| worker:l4090        |   1 |    1 |   · |  900.2 | no output written by tra×1               |
| worker:laguna       | 103 |  107 |  +1 |  190.4 | no output written by tra×55；verify=1×16 |
| worker:laptop40901  |   4 |    2 |   · |  900.3 | no output written by tra×1；health×1     |
| worker:laptop40902  |   4 |    2 |   · |  900.3 | verify=1×1；leak×1                       |
| worker:mac          |  49 |  158 |  +1 |  218.3 | leak×89；verify=1×35                     |
| worker:nemo         | 274 |  395 |  +5 |  101.1 | leak×283；verify=1×59                    |
| worker:nemo2        | 248 |  315 |  +5 |   96.6 | leak×229；verify=1×43                    |
| worker:nemo3        | 198 |  268 |  +1 |   94.5 | leak×173；verify=1×46                    |
| worker:oss20        |  32 |   64 |   · |  460.4 | leak×27；verify=1×14                     |

endpoint 探活：local 🟢、laptop-4090 🟢、laptop-5090 🔴、desktop-3090 🟢、mac-m4max 🟢

（babel-pulse 常駐儀器自動快照）

## 2026-07-25T14:44:10+08:00（zh 總數 863）

| 語言 | fresh | stale | missing | 覆蓋率 | Δfresh | Δmissing |
| ---- | ----: | ----: | ------: | -----: | -----: | -------: |
| en   |   723 |   106 |      34 |  96.1% |      · |        · |
| ja   |   710 |   148 |       5 |  99.4% |      · |        · |
| ko   |   707 |   153 |       3 |  99.7% |     +1 |        · |
| es   |   715 |   146 |       2 |  99.8% |     +1 |        · |
| fr   |   707 |   155 |       1 |  99.9% |      · |        · |
| vi   |   103 |    10 |     750 |  13.1% |      · |        · |
| id   |   200 |     3 |     660 |  23.5% |     +1 |       -1 |
| pt   |   277 |     9 |     577 |  33.1% |     -1 |       +1 |
| hi   |   219 |     5 |     639 |  26.0% |     +1 |       -1 |
| ar   |   136 |     1 |     726 |  15.9% |     +1 |       -1 |
| ru   |   147 |     1 |     715 |  17.1% |     +1 |       -1 |

總缺口（stale+missing）：**4849**（▼5 vs 上一筆）

**節點／worker**（ok/fail 為累計；Δ為對上一筆）

| 節點                |  ok | fail | Δok | 平均秒 | 主要 fail                                |
| ------------------- | --: | ---: | --: | -----: | ---------------------------------------- |
| fleet:desktop-3090  |  56 |  325 |   · |      — | health×123；verify=1×102                 |
| fleet:laptop-4090   |  27 |  137 |   · |      — | health×83；verify=None×24                |
| worker:d3090        |   2 |    1 |   · |  900.2 | health×1                                 |
| worker:desktop30901 |  11 |    4 |  +1 |  449.6 | health×3；verify=4×1                     |
| worker:desktop30902 |  10 |    5 |  +1 |  514.3 | health×4；verify=3×1                     |
| worker:gemma31      |   1 |   34 |   · |    2.2 | no output written by tra×34              |
| worker:l4090        |   1 |    2 |   · |  900.2 | no output written by tra×2               |
| worker:laguna       | 103 |  108 |   · |  190.4 | no output written by tra×55；verify=1×16 |
| worker:laptop40901  |   6 |    2 |  +2 |  894.2 | no output written by tra×1；health×1     |
| worker:laptop40902  |   5 |    2 |  +1 |  900.3 | verify=1×1；leak×1                       |
| worker:mac          |  51 |  158 |  +2 |  224.0 | leak×89；verify=1×35                     |
| worker:nemo         | 279 |  401 |  +5 |  101.2 | leak×288；verify=1×59                    |
| worker:nemo2        | 251 |  322 |  +3 |   97.2 | leak×233；verify=1×43                    |
| worker:nemo3        | 199 |  270 |  +1 |   96.1 | leak×173；verify=1×47                    |
| worker:oss20        |  32 |   66 |   · |  460.4 | leak×29；verify=1×14                     |

endpoint 探活：local 🟢、laptop-4090 🟢、laptop-5090 🔴、desktop-3090 🟢、mac-m4max 🟢

（babel-pulse 常駐儀器自動快照）

## 2026-07-25T14:52:48+08:00（zh 總數 863）

| 語言 | fresh | stale | missing | 覆蓋率 | Δfresh | Δmissing |
| ---- | ----: | ----: | ------: | -----: | -----: | -------: |
| en   |   723 |   106 |      34 |  96.1% |      · |        · |
| ja   |   710 |   148 |       5 |  99.4% |      · |        · |
| ko   |   707 |   153 |       3 |  99.7% |      · |        · |
| es   |   715 |   146 |       2 |  99.8% |      · |        · |
| fr   |   707 |   155 |       1 |  99.9% |      · |        · |
| vi   |   103 |    10 |     750 |  13.1% |      · |        · |
| id   |   201 |     3 |     659 |  23.6% |     +1 |       -1 |
| pt   |   279 |     9 |     575 |  33.4% |     +2 |       -2 |
| hi   |   221 |     5 |     637 |  26.2% |     +2 |       -2 |
| ar   |   137 |     1 |     725 |  16.0% |     +1 |       -1 |
| ru   |   148 |     1 |     714 |  17.3% |     +1 |       -1 |

總缺口（stale+missing）：**4842**（▼7 vs 上一筆）

**節點／worker**（ok/fail 為累計；Δ為對上一筆）

| 節點                |  ok | fail | Δok | 平均秒 | 主要 fail                                |
| ------------------- | --: | ---: | --: | -----: | ---------------------------------------- |
| fleet:desktop-3090  |  56 |  325 |   · |      — | health×123；verify=1×102                 |
| fleet:laptop-4090   |  27 |  137 |   · |      — | health×83；verify=None×24                |
| worker:d3090        |   2 |    2 |   · |  900.2 | health×1；no output written by tra×1     |
| worker:desktop30901 |  11 |    4 |   · |  449.6 | health×3；verify=4×1                     |
| worker:desktop30902 |  10 |    6 |   · |  514.3 | health×4；verify=3×1                     |
| worker:gemma31      |   1 |   34 |   · |    2.2 | no output written by tra×34              |
| worker:l4090        |   1 |    3 |   · |  900.2 | no output written by tra×2；leak×1       |
| worker:laguna       | 104 |  108 |  +1 |  192.1 | no output written by tra×55；verify=1×16 |
| worker:laptop40901  |   6 |    2 |   · |  894.2 | no output written by tra×1；health×1     |
| worker:laptop40902  |   5 |    3 |   · |  900.3 | leak×2；verify=1×1                       |
| worker:mac          |  51 |  159 |   · |  224.0 | leak×90；verify=1×35                     |
| worker:nemo         | 282 |  404 |  +3 |  102.6 | leak×289；verify=1×59                    |
| worker:nemo2        | 252 |  330 |  +1 |   99.2 | leak×238；verify=1×45                    |
| worker:nemo3        | 201 |  270 |  +2 |   96.8 | leak×173；verify=1×47                    |
| worker:oss20        |  32 |   66 |   · |  460.4 | leak×29；verify=1×14                     |

endpoint 探活：local 🟢、laptop-4090 🟢、laptop-5090 🔴、desktop-3090 🟢、mac-m4max 🟢

（babel-pulse 常駐儀器自動快照）

## 2026-07-25T14:59:48+08:00（zh 總數 863）

| 語言 | fresh | stale | missing | 覆蓋率 | Δfresh | Δmissing |
| ---- | ----: | ----: | ------: | -----: | -----: | -------: |
| en   |   723 |   106 |      34 |  96.1% |      · |        · |
| ja   |   710 |   148 |       5 |  99.4% |      · |        · |
| ko   |   707 |   153 |       3 |  99.7% |      · |        · |
| es   |   715 |   146 |       2 |  99.8% |      · |        · |
| fr   |   707 |   155 |       1 |  99.9% |      · |        · |
| vi   |   102 |    10 |     751 |  13.0% |     -1 |       +1 |
| id   |   201 |     3 |     659 |  23.6% |      · |        · |
| pt   |   280 |     9 |     574 |  33.5% |     +1 |       -1 |
| hi   |   222 |     5 |     636 |  26.3% |     +1 |       -1 |
| ar   |   137 |     1 |     725 |  16.0% |      · |        · |
| ru   |   150 |     1 |     712 |  17.5% |     +2 |       -2 |

總缺口（stale+missing）：**4839**（▼3 vs 上一筆）

**節點／worker**（ok/fail 為累計；Δ為對上一筆）

| 節點                |  ok | fail | Δok | 平均秒 | 主要 fail                                |
| ------------------- | --: | ---: | --: | -----: | ---------------------------------------- |
| fleet:desktop-3090  |  56 |  325 |   · |      — | health×123；verify=1×102                 |
| fleet:laptop-4090   |  27 |  137 |   · |      — | health×83；verify=None×24                |
| worker:d3090        |   2 |    2 |   · |  900.2 | health×1；no output written by tra×1     |
| worker:desktop30901 |  11 |    5 |   · |  449.6 | health×3；verify=4×1                     |
| worker:desktop30902 |  10 |    6 |   · |  514.3 | health×4；verify=3×1                     |
| worker:gemma31      |   1 |   34 |   · |    2.2 | no output written by tra×34              |
| worker:l4090        |   1 |    3 |   · |  900.2 | no output written by tra×2；leak×1       |
| worker:laguna       | 105 |  109 |  +1 |  194.5 | no output written by tra×56；verify=1×16 |
| worker:laptop40901  |   7 |    2 |  +1 |  895.1 | no output written by tra×1；health×1     |
| worker:laptop40902  |   5 |    3 |   · |  900.3 | leak×2；verify=1×1                       |
| worker:mac          |  51 |  160 |   · |  224.0 | leak×90；verify=1×35                     |
| worker:nemo         | 283 |  407 |  +1 |  102.6 | leak×291；verify=1×59                    |
| worker:nemo2        | 252 |  333 |   · |   99.2 | leak×240；verify=1×45                    |
| worker:nemo3        | 202 |  271 |  +1 |   97.0 | leak×174；verify=1×47                    |
| worker:oss20        |  33 |   66 |  +1 |  480.8 | leak×29；verify=1×14                     |

endpoint 探活：local 🟢、laptop-4090 🟢、laptop-5090 🔴、desktop-3090 🟢、mac-m4max 🟢

（babel-pulse 常駐儀器自動快照）

## 2026-07-25T15:15:32+08:00（zh 總數 863）

| 語言 | fresh | stale | missing | 覆蓋率 | Δfresh | Δmissing |
| ---- | ----: | ----: | ------: | -----: | -----: | -------: |
| en   |   723 |   106 |      34 |  96.1% |      · |        · |
| ja   |   710 |   148 |       5 |  99.4% |      · |        · |
| ko   |   707 |   153 |       3 |  99.7% |      · |        · |
| es   |   715 |   146 |       2 |  99.8% |      · |        · |
| fr   |   707 |   155 |       1 |  99.9% |      · |        · |
| vi   |   103 |    10 |     750 |  13.1% |     +1 |       -1 |
| id   |   201 |     3 |     659 |  23.6% |      · |        · |
| pt   |   282 |     9 |     572 |  33.7% |     +2 |       -2 |
| hi   |   221 |     5 |     637 |  26.2% |     -1 |       +1 |
| ar   |   137 |     1 |     725 |  16.0% |      · |        · |
| ru   |   151 |     1 |     711 |  17.6% |     +1 |       -1 |

總缺口（stale+missing）：**4836**（▼3 vs 上一筆）

**節點／worker**（ok/fail 為累計；Δ為對上一筆）

| 節點                |  ok | fail | Δok | 平均秒 | 主要 fail                                |
| ------------------- | --: | ---: | --: | -----: | ---------------------------------------- |
| fleet:desktop-3090  |  56 |  325 |   · |      — | health×123；verify=1×102                 |
| fleet:laptop-4090   |  27 |  137 |   · |      — | health×83；verify=None×24                |
| worker:d3090        |   2 |    3 |   · |  900.2 | no output written by tra×2；health×1     |
| worker:desktop30901 |  11 |    6 |   · |  449.6 | health×3；verify=4×1                     |
| worker:desktop30902 |  11 |    6 |  +1 |  549.4 | health×4；verify=3×1                     |
| worker:gemma31      |   1 |   34 |   · |    2.2 | no output written by tra×34              |
| worker:l4090        |   1 |    4 |   · |  900.2 | no output written by tra×3；leak×1       |
| worker:laguna       | 106 |  110 |  +1 |  198.7 | no output written by tra×57；verify=1×16 |
| worker:laptop40901  |   7 |    3 |   · |  895.1 | health×2；no output written by tra×1     |
| worker:laptop40902  |   5 |    4 |   · |  900.3 | leak×3；verify=1×1                       |
| worker:mac          |  52 |  161 |  +1 |  231.6 | leak×90；verify=1×36                     |
| worker:nemo         | 284 |  417 |  +1 |  102.6 | leak×294；verify=1×59                    |
| worker:nemo2        | 255 |  342 |  +3 |   99.5 | leak×246；verify=1×45                    |
| worker:nemo3        | 203 |  272 |  +1 |   99.7 | leak×174；verify=1×47                    |
| worker:oss20        |  33 |   67 |   · |  480.8 | leak×29；verify=1×14                     |

endpoint 探活：local 🟢、laptop-4090 🟢、laptop-5090 🔴、desktop-3090 🟢、mac-m4max 🟢

（babel-pulse 常駐儀器自動快照）

## 2026-07-25T15:31:17+08:00（zh 總數 863）

| 語言 | fresh | stale | missing | 覆蓋率 | Δfresh | Δmissing |
| ---- | ----: | ----: | ------: | -----: | -----: | -------: |
| en   |   724 |   106 |      33 |  96.2% |     +1 |       -1 |
| ja   |   710 |   148 |       5 |  99.4% |      · |        · |
| ko   |   707 |   153 |       3 |  99.7% |      · |        · |
| es   |   715 |   146 |       2 |  99.8% |      · |        · |
| fr   |   707 |   155 |       1 |  99.9% |      · |        · |
| vi   |   103 |    10 |     750 |  13.1% |      · |        · |
| id   |   201 |     3 |     659 |  23.6% |      · |        · |
| pt   |   282 |     9 |     572 |  33.7% |      · |        · |
| hi   |   221 |     5 |     637 |  26.2% |      · |        · |
| ar   |   138 |     1 |     724 |  16.1% |     +1 |       -1 |
| ru   |   152 |     1 |     710 |  17.7% |     +1 |       -1 |

總缺口（stale+missing）：**4833**（▼3 vs 上一筆）

**節點／worker**（ok/fail 為累計；Δ為對上一筆）

| 節點                |  ok | fail | Δok | 平均秒 | 主要 fail                                |
| ------------------- | --: | ---: | --: | -----: | ---------------------------------------- |
| fleet:desktop-3090  |  56 |  325 |   · |      — | health×123；verify=1×102                 |
| fleet:laptop-4090   |  27 |  137 |   · |      — | health×83；verify=None×24                |
| worker:d3090        |   2 |    3 |   · |  900.2 | no output written by tra×2；health×1     |
| worker:desktop30901 |  12 |    6 |  +1 |  487.2 | health×3；verify=4×1                     |
| worker:desktop30902 |  11 |    7 |   · |  549.4 | health×5；verify=3×1                     |
| worker:gemma31      |   1 |   34 |   · |    2.2 | no output written by tra×34              |
| worker:l4090        |   1 |    4 |   · |  900.2 | no output written by tra×3；leak×1       |
| worker:laguna       | 107 |  111 |  +1 |  202.8 | no output written by tra×58；verify=1×16 |
| worker:laptop40901  |   8 |    3 |  +1 |  853.5 | health×2；no output written by tra×1     |
| worker:laptop40902  |   6 |    5 |  +1 |  900.3 | leak×4；verify=1×1                       |
| worker:mac          |  53 |  161 |  +1 |  233.4 | leak×90；verify=1×36                     |
| worker:nemo         | 289 |  426 |  +5 |  101.9 | leak×299；verify=1×61                    |
| worker:nemo2        | 258 |  353 |  +3 |   99.5 | leak×254；verify=1×46                    |
| worker:nemo3        | 204 |  273 |  +1 |   99.7 | leak×174；verify=1×47                    |
| worker:oss20        |  33 |   68 |   · |  480.8 | leak×30；verify=1×14                     |

endpoint 探活：local 🟢、laptop-4090 🟢、laptop-5090 🔴、desktop-3090 🟢、mac-m4max 🟢

（babel-pulse 常駐儀器自動快照）

## 2026-07-25T15:43:29+08:00（zh 總數 863）

| 語言 | fresh | stale | missing | 覆蓋率 | Δfresh | Δmissing |
| ---- | ----: | ----: | ------: | -----: | -----: | -------: |
| en   |   724 |   106 |      33 |  96.2% |      · |        · |
| ja   |   710 |   148 |       5 |  99.4% |      · |        · |
| ko   |   707 |   153 |       3 |  99.7% |      · |        · |
| es   |   715 |   146 |       2 |  99.8% |      · |        · |
| fr   |   707 |   155 |       1 |  99.9% |      · |        · |
| vi   |   103 |    10 |     750 |  13.1% |      · |        · |
| id   |   201 |     3 |     659 |  23.6% |      · |        · |
| pt   |   283 |     9 |     571 |  33.8% |     +1 |       -1 |
| hi   |   221 |     5 |     637 |  26.2% |      · |        · |
| ar   |   138 |     1 |     724 |  16.1% |      · |        · |
| ru   |   154 |     1 |     708 |  18.0% |     +2 |       -2 |

總缺口（stale+missing）：**4830**（▼3 vs 上一筆）

**節點／worker**（ok/fail 為累計；Δ為對上一筆）

| 節點                |  ok | fail | Δok | 平均秒 | 主要 fail                                |
| ------------------- | --: | ---: | --: | -----: | ---------------------------------------- |
| fleet:desktop-3090  |  56 |  325 |   · |      — | health×123；verify=1×102                 |
| fleet:laptop-4090   |  27 |  137 |   · |      — | health×83；verify=None×24                |
| worker:d3090        |   3 |    3 |  +1 |  900.2 | no output written by tra×2；health×1     |
| worker:desktop30901 |  12 |    7 |   · |  487.2 | health×3；leak×2                         |
| worker:desktop30902 |  11 |    8 |   · |  549.4 | health×5；leak×2                         |
| worker:gemma31      |   1 |   34 |   · |    2.2 | no output written by tra×34              |
| worker:l4090        |   2 |    4 |  +1 |  900.2 | no output written by tra×3；leak×1       |
| worker:laguna       | 107 |  111 |   · |  202.8 | no output written by tra×58；verify=1×16 |
| worker:laptop40901  |   9 |    3 |  +1 |  858.7 | health×2；no output written by tra×1     |
| worker:laptop40902  |   6 |    6 |   · |  900.3 | leak×4；verify=1×1                       |
| worker:mac          |  54 |  163 |  +1 |  238.6 | leak×92；verify=1×36                     |
| worker:nemo         | 289 |  428 |   · |  101.9 | leak×299；verify=1×61                    |
| worker:nemo2        | 258 |  355 |   · |   99.5 | leak×255；verify=1×46                    |
| worker:nemo3        | 205 |  274 |  +1 |   99.8 | leak×174；verify=1×47                    |
| worker:oss20        |  34 |   69 |  +1 |  488.1 | leak×30；verify=1×14                     |

endpoint 探活：local 🟢、laptop-4090 🟢、laptop-5090 🔴、desktop-3090 🟢、mac-m4max 🟢

（babel-pulse 常駐儀器自動快照）

## 2026-07-25T15:46:56+08:00（zh 總數 864）

| 語言 | fresh | stale | missing | 覆蓋率 | Δfresh | Δmissing |
| ---- | ----: | ----: | ------: | -----: | -----: | -------: |
| en   |   722 |   108 |      34 |  96.1% |     -2 |       +1 |
| ja   |   708 |   150 |       6 |  99.3% |     -2 |       +1 |
| ko   |   705 |   155 |       4 |  99.5% |     -2 |       +1 |
| es   |   713 |   148 |       3 |  99.7% |     -2 |       +1 |
| fr   |   705 |   157 |       2 |  99.8% |     -2 |       +1 |
| vi   |   103 |    10 |     751 |  13.1% |      · |       +1 |
| id   |   202 |     3 |     659 |  23.7% |     +1 |        · |
| pt   |   283 |     9 |     572 |  33.8% |      · |       +1 |
| hi   |   221 |     5 |     638 |  26.2% |      · |       +1 |
| ar   |   138 |     1 |     725 |  16.1% |      · |       +1 |
| ru   |   154 |     1 |     709 |  17.9% |      · |       +1 |

總缺口（stale+missing）：**4850**（▲20 vs 上一筆）

**節點／worker**（ok/fail 為累計；Δ為對上一筆）

| 節點                |  ok | fail | Δok | 平均秒 | 主要 fail                                |
| ------------------- | --: | ---: | --: | -----: | ---------------------------------------- |
| fleet:desktop-3090  |  56 |  325 |   · |      — | health×123；verify=1×102                 |
| fleet:laptop-4090   |  27 |  137 |   · |      — | health×83；verify=None×24                |
| worker:d3090        |   3 |    3 |   · |  900.2 | no output written by tra×2；health×1     |
| worker:desktop30901 |  12 |    7 |   · |  487.2 | health×3；leak×2                         |
| worker:desktop30902 |  11 |    8 |   · |  549.4 | health×5；leak×2                         |
| worker:gemma31      |   1 |   34 |   · |    2.2 | no output written by tra×34              |
| worker:l4090        |   2 |    4 |   · |  900.2 | no output written by tra×3；leak×1       |
| worker:laguna       | 107 |  111 |   · |  202.8 | no output written by tra×58；verify=1×16 |
| worker:laptop40901  |   9 |    3 |   · |  858.7 | health×2；no output written by tra×1     |
| worker:laptop40902  |   6 |    6 |   · |  900.3 | leak×4；verify=1×1                       |
| worker:mac          |  54 |  164 |   · |  238.6 | leak×92；verify=1×36                     |
| worker:nemo         | 289 |  429 |   · |  101.9 | leak×300；verify=1×61                    |
| worker:nemo2        | 258 |  355 |   · |   99.5 | leak×255；verify=1×46                    |
| worker:nemo3        | 205 |  274 |   · |   99.8 | leak×174；verify=1×47                    |
| worker:oss20        |  34 |   69 |   · |  488.1 | leak×30；verify=1×14                     |

endpoint 探活：local 🟢、laptop-4090 🟢、laptop-5090 🔴、desktop-3090 🟢、mac-m4max 🟢

（babel-pulse 常駐儀器自動快照）

## 2026-07-25T16:02:37+08:00（zh 總數 864）

| 語言 | fresh | stale | missing | 覆蓋率 | Δfresh | Δmissing |
| ---- | ----: | ----: | ------: | -----: | -----: | -------: |
| en   |   722 |   108 |      34 |  96.1% |      · |        · |
| ja   |   708 |   150 |       6 |  99.3% |      · |        · |
| ko   |   705 |   155 |       4 |  99.5% |      · |        · |
| es   |   713 |   148 |       3 |  99.7% |      · |        · |
| fr   |   705 |   157 |       2 |  99.8% |      · |        · |
| vi   |   103 |    10 |     751 |  13.1% |      · |        · |
| id   |   202 |     3 |     659 |  23.7% |      · |        · |
| pt   |   286 |     9 |     569 |  34.1% |     +3 |       -3 |
| hi   |   223 |     5 |     636 |  26.4% |     +2 |       -2 |
| ar   |   141 |     1 |     722 |  16.4% |     +3 |       -3 |
| ru   |   159 |     1 |     704 |  18.5% |     +5 |       -5 |

總缺口（stale+missing）：**4837**（▼13 vs 上一筆）

**節點／worker**（ok/fail 為累計；Δ為對上一筆）

| 節點                |  ok | fail | Δok | 平均秒 | 主要 fail                                |
| ------------------- | --: | ---: | --: | -----: | ---------------------------------------- |
| fleet:desktop-3090  |  56 |  325 |   · |      — | health×123；verify=1×102                 |
| fleet:laptop-4090   |  27 |  137 |   · |      — | health×83；verify=None×24                |
| worker:d3090        |   3 |    4 |   · |  900.2 | no output written by tra×2；verify=4×1   |
| worker:desktop30901 |  12 |    8 |   · |  487.2 | health×3；verify=4×2                     |
| worker:desktop30902 |  11 |    9 |   · |  549.4 | health×5；leak×3                         |
| worker:gemma31      |   1 |   34 |   · |    2.2 | no output written by tra×34              |
| worker:l4090        |   2 |    5 |   · |  900.2 | no output written by tra×4；leak×1       |
| worker:laguna       | 107 |  112 |   · |  202.8 | no output written by tra×59；verify=1×16 |
| worker:laptop40901  |  10 |    3 |  +1 |  862.8 | health×2；no output written by tra×1     |
| worker:laptop40902  |   7 |    6 |  +1 |  900.3 | leak×4；verify=1×1                       |
| worker:mac          |  54 |  166 |   · |  238.6 | leak×94；verify=1×36                     |
| worker:nemo         | 295 |  441 |  +6 |  102.0 | leak×309；verify=1×61                    |
| worker:nemo2        | 261 |  367 |  +3 |   99.9 | leak×265；verify=1×47                    |
| worker:nemo3        | 210 |  281 |  +5 |   98.9 | leak×179；verify=1×48                    |
| worker:oss20        |  34 |   70 |   · |  488.1 | leak×30；verify=1×14                     |

endpoint 探活：local 🟢、laptop-4090 🟢、laptop-5090 🔴、desktop-3090 🟢、mac-m4max 🟢

（babel-pulse 常駐儀器自動快照）

## 2026-07-25T16:18:23+08:00（zh 總數 864）

| 語言 | fresh | stale | missing | 覆蓋率 | Δfresh | Δmissing |
| ---- | ----: | ----: | ------: | -----: | -----: | -------: |
| en   |   722 |   108 |      34 |  96.1% |      · |        · |
| ja   |   708 |   150 |       6 |  99.3% |      · |        · |
| ko   |   705 |   155 |       4 |  99.5% |      · |        · |
| es   |   713 |   148 |       3 |  99.7% |      · |        · |
| fr   |   705 |   157 |       2 |  99.8% |      · |        · |
| vi   |   103 |    10 |     751 |  13.1% |      · |        · |
| id   |   202 |     3 |     659 |  23.7% |      · |        · |
| pt   |   291 |     9 |     564 |  34.7% |     +5 |       -5 |
| hi   |   227 |     5 |     632 |  26.9% |     +4 |       -4 |
| ar   |   145 |     1 |     718 |  16.9% |     +4 |       -4 |
| ru   |   163 |     1 |     700 |  19.0% |     +4 |       -4 |

總缺口（stale+missing）：**4820**（▼17 vs 上一筆）

**節點／worker**（ok/fail 為累計；Δ為對上一筆）

| 節點                |  ok | fail | Δok | 平均秒 | 主要 fail                                |
| ------------------- | --: | ---: | --: | -----: | ---------------------------------------- |
| fleet:desktop-3090  |  56 |  325 |   · |      — | health×123；verify=1×102                 |
| fleet:laptop-4090   |  27 |  137 |   · |      — | health×83；verify=None×24                |
| worker:d3090        |   4 |    4 |  +1 |  900.2 | no output written by tra×2；verify=4×1   |
| worker:desktop30901 |  13 |    8 |  +1 |  519.0 | health×3；verify=4×2                     |
| worker:desktop30902 |  11 |   10 |   · |  549.4 | health×6；leak×3                         |
| worker:gemma31      |   1 |   34 |   · |    2.2 | no output written by tra×34              |
| worker:l4090        |   3 |    5 |  +1 |  900.3 | no output written by tra×4；leak×1       |
| worker:laguna       | 107 |  114 |   · |  202.8 | no output written by tra×61；verify=1×16 |
| worker:laptop40901  |  10 |    4 |   · |  862.8 | health×2；no output written by tra×1     |
| worker:laptop40902  |   7 |    7 |   · |  900.3 | leak×4；health×2                         |
| worker:mac          |  54 |  170 |   · |  238.6 | leak×96；verify=1×37                     |
| worker:nemo         | 304 |  450 |  +9 |  102.4 | leak×316；verify=1×63                    |
| worker:nemo2        | 265 |  378 |  +4 |  100.5 | leak×274；verify=1×48                    |
| worker:nemo3        | 216 |  287 |  +6 |   99.2 | leak×183；verify=1×48                    |
| worker:oss20        |  35 |   73 |  +1 |  477.8 | leak×30；no output written by tra×14     |

endpoint 探活：local 🟢、laptop-4090 🟢、laptop-5090 🔴、desktop-3090 🟢、mac-m4max 🟢

（babel-pulse 常駐儀器自動快照）

## 2026-07-25T16:33:56+08:00（zh 總數 864）

| 語言 | fresh | stale | missing | 覆蓋率 | Δfresh | Δmissing |
| ---- | ----: | ----: | ------: | -----: | -----: | -------: |
| en   |   722 |   108 |      34 |  96.1% |      · |        · |
| ja   |   708 |   150 |       6 |  99.3% |      · |        · |
| ko   |   705 |   155 |       4 |  99.5% |      · |        · |
| es   |   713 |   148 |       3 |  99.7% |      · |        · |
| fr   |   705 |   157 |       2 |  99.8% |      · |        · |
| vi   |   103 |    10 |     751 |  13.1% |      · |        · |
| id   |   203 |     3 |     658 |  23.8% |     +1 |       -1 |
| pt   |   298 |     9 |     557 |  35.5% |     +7 |       -7 |
| hi   |   231 |     5 |     628 |  27.3% |     +4 |       -4 |
| ar   |   149 |     1 |     714 |  17.4% |     +4 |       -4 |
| ru   |   166 |     1 |     697 |  19.3% |     +3 |       -3 |

總缺口（stale+missing）：**4801**（▼19 vs 上一筆）

**節點／worker**（ok/fail 為累計；Δ為對上一筆）

| 節點                |  ok | fail | Δok | 平均秒 | 主要 fail                                |
| ------------------- | --: | ---: | --: | -----: | ---------------------------------------- |
| fleet:desktop-3090  |  56 |  325 |   · |      — | health×123；verify=1×102                 |
| fleet:laptop-4090   |  27 |  137 |   · |      — | health×83；verify=None×24                |
| worker:d3090        |   4 |    5 |   · |  900.2 | no output written by tra×3；verify=4×1   |
| worker:desktop30901 |  13 |    9 |   · |  519.0 | health×3；leak×3                         |
| worker:desktop30902 |  12 |   10 |  +1 |  578.7 | health×6；leak×3                         |
| worker:gemma31      |   1 |   34 |   · |    2.2 | no output written by tra×34              |
| worker:l4090        |   3 |    6 |   · |  900.3 | no output written by tra×5；leak×1       |
| worker:laguna       | 107 |  114 |   · |  202.8 | no output written by tra×61；verify=1×16 |
| worker:laptop40901  |  10 |    5 |   · |  862.8 | health×2；no output written by tra×1     |
| worker:laptop40902  |   8 |    7 |  +1 |  900.3 | leak×4；health×2                         |
| worker:mac          |  54 |  174 |   · |  238.6 | leak×99；verify=1×37                     |
| worker:nemo         | 307 |  461 |  +3 |  102.3 | leak×324；verify=1×65                    |
| worker:nemo2        | 273 |  388 |  +8 |  102.1 | leak×284；verify=1×48                    |
| worker:nemo3        | 220 |  293 |  +4 |   98.5 | leak×187；verify=1×49                    |
| worker:oss20        |  36 |   74 |  +1 |  470.4 | leak×31；no output written by tra×14     |

endpoint 探活：local 🟢、laptop-4090 🟢、laptop-5090 🔴、desktop-3090 🟢、mac-m4max 🟢

（babel-pulse 常駐儀器自動快照）

## 2026-07-25T16:47:43+08:00（zh 總數 864）

| 語言 | fresh | stale | missing | 覆蓋率 | Δfresh | Δmissing |
| ---- | ----: | ----: | ------: | -----: | -----: | -------: |
| en   |   722 |   108 |      34 |  96.1% |      · |        · |
| ja   |   708 |   150 |       6 |  99.3% |      · |        · |
| ko   |   705 |   155 |       4 |  99.5% |      · |        · |
| es   |   714 |   147 |       3 |  99.7% |     +1 |        · |
| fr   |   705 |   157 |       2 |  99.8% |      · |        · |
| vi   |   103 |    10 |     751 |  13.1% |      · |        · |
| id   |   204 |     3 |     657 |  24.0% |     +1 |       -1 |
| pt   |   299 |     9 |     556 |  35.6% |     +1 |       -1 |
| hi   |   232 |     5 |     627 |  27.4% |     +1 |       -1 |
| ar   |   153 |     1 |     710 |  17.8% |     +4 |       -4 |
| ru   |   170 |     1 |     693 |  19.8% |     +4 |       -4 |

總缺口（stale+missing）：**4789**（▼12 vs 上一筆）

**節點／worker**（ok/fail 為累計；Δ為對上一筆）

| 節點                |  ok | fail | Δok | 平均秒 | 主要 fail                                |
| ------------------- | --: | ---: | --: | -----: | ---------------------------------------- |
| fleet:desktop-3090  |  56 |  325 |   · |      — | health×123；verify=1×102                 |
| fleet:laptop-4090   |  27 |  137 |   · |      — | health×83；verify=None×24                |
| worker:d3090        |   4 |    6 |   · |  900.2 | no output written by tra×3；verify=4×1   |
| worker:desktop30901 |  13 |   10 |   · |  519.0 | health×4；leak×3                         |
| worker:desktop30902 |  12 |   11 |   · |  578.7 | health×7；leak×3                         |
| worker:gemma31      |   1 |   34 |   · |    2.2 | no output written by tra×34              |
| worker:l4090        |   3 |    7 |   · |  900.3 | no output written by tra×5；health×1     |
| worker:laguna       | 107 |  114 |   · |  202.8 | no output written by tra×61；verify=1×16 |
| worker:laptop40901  |  10 |    6 |   · |  862.8 | health×2；leak×2                         |
| worker:laptop40902  |   9 |    7 |  +1 |  900.3 | leak×4；health×2                         |
| worker:mac          |  55 |  175 |  +1 |  240.5 | leak×99；verify=1×37                     |
| worker:nemo         | 312 |  469 |  +5 |  102.6 | leak×331；verify=1×65                    |
| worker:nemo2        | 275 |  401 |  +2 |  101.9 | leak×293；health×49                      |
| worker:nemo3        | 226 |  296 |  +6 |   98.1 | leak×189；verify=1×49                    |
| worker:oss20        |  36 |   75 |   · |  470.4 | leak×32；no output written by tra×14     |

endpoint 探活：local 🟢、laptop-4090 🟢、laptop-5090 🔴、desktop-3090 🟢、mac-m4max 🟢

（babel-pulse 常駐儀器自動快照）

## 2026-07-25T16:49:47+08:00（zh 總數 864）

| 語言 | fresh | stale | missing | 覆蓋率 | Δfresh | Δmissing |
| ---- | ----: | ----: | ------: | -----: | -----: | -------: |
| en   |   722 |   108 |      34 |  96.1% |      · |        · |
| ja   |   708 |   150 |       6 |  99.3% |      · |        · |
| ko   |   705 |   155 |       4 |  99.5% |      · |        · |
| es   |   714 |   147 |       3 |  99.7% |      · |        · |
| fr   |   706 |   156 |       2 |  99.8% |     +1 |        · |
| vi   |   103 |    10 |     751 |  13.1% |      · |        · |
| id   |   205 |     3 |     656 |  24.1% |     +1 |       -1 |
| pt   |   299 |     9 |     556 |  35.6% |      · |        · |
| hi   |   232 |     5 |     627 |  27.4% |      · |        · |
| ar   |   153 |     1 |     710 |  17.8% |      · |        · |
| ru   |   170 |     1 |     693 |  19.8% |      · |        · |

總缺口（stale+missing）：**4787**（▼2 vs 上一筆）

**節點／worker**（ok/fail 為累計；Δ為對上一筆）

| 節點                |  ok | fail | Δok | 平均秒 | 主要 fail                                |
| ------------------- | --: | ---: | --: | -----: | ---------------------------------------- |
| fleet:desktop-3090  |  56 |  325 |   · |      — | health×123；verify=1×102                 |
| fleet:laptop-4090   |  27 |  137 |   · |      — | health×83；verify=None×24                |
| worker:d3090        |   4 |    7 |   · |  900.2 | no output written by tra×4；verify=4×1   |
| worker:desktop30901 |  13 |   10 |   · |  519.0 | health×4；leak×3                         |
| worker:desktop30902 |  12 |   11 |   · |  578.7 | health×7；leak×3                         |
| worker:gemma31      |   1 |   34 |   · |    2.2 | no output written by tra×34              |
| worker:l4090        |   3 |    8 |   · |  900.3 | no output written by tra×6；health×1     |
| worker:laguna       | 107 |  114 |   · |  202.8 | no output written by tra×61；verify=1×16 |
| worker:laptop40901  |  10 |    6 |   · |  862.8 | health×2；leak×2                         |
| worker:laptop40902  |   9 |    7 |   · |  900.3 | leak×4；health×2                         |
| worker:mac          |  56 |  175 |  +1 |  242.9 | leak×99；verify=1×37                     |
| worker:nemo         | 313 |  471 |  +1 |  102.8 | leak×333；verify=1×65                    |
| worker:nemo2        | 275 |  403 |   · |  101.9 | leak×295；health×49                      |
| worker:nemo3        | 226 |  297 |   · |   98.1 | leak×189；verify=1×49                    |
| worker:oss20        |  36 |   77 |   · |  470.4 | leak×33；no output written by tra×15     |

endpoint 探活：local 🟢、laptop-4090 🟢、laptop-5090 🔴、desktop-3090 🟢、mac-m4max 🟢

（babel-pulse 常駐儀器自動快照）

## 2026-07-25T17:05:33+08:00（zh 總數 864）

| 語言 | fresh | stale | missing | 覆蓋率 | Δfresh | Δmissing |
| ---- | ----: | ----: | ------: | -----: | -----: | -------: |
| en   |   722 |   108 |      34 |  96.1% |      · |        · |
| ja   |   708 |   150 |       6 |  99.3% |      · |        · |
| ko   |   705 |   155 |       4 |  99.5% |      · |        · |
| es   |   714 |   147 |       3 |  99.7% |      · |        · |
| fr   |   706 |   156 |       2 |  99.8% |      · |        · |
| vi   |   104 |    10 |     750 |  13.2% |     +1 |       -1 |
| id   |   205 |     3 |     656 |  24.1% |      · |        · |
| pt   |   303 |     9 |     552 |  36.1% |     +4 |       -4 |
| hi   |   235 |     5 |     624 |  27.8% |     +3 |       -3 |
| ar   |   152 |     1 |     711 |  17.7% |     -1 |       +1 |
| ru   |   174 |     1 |     689 |  20.3% |     +4 |       -4 |

總缺口（stale+missing）：**4776**（▼11 vs 上一筆）

**節點／worker**（ok/fail 為累計；Δ為對上一筆）

| 節點                |  ok | fail | Δok | 平均秒 | 主要 fail                                |
| ------------------- | --: | ---: | --: | -----: | ---------------------------------------- |
| fleet:desktop-3090  |  56 |  325 |   · |      — | health×123；verify=1×102                 |
| fleet:laptop-4090   |  27 |  137 |   · |      — | health×83；verify=None×24                |
| worker:d3090        |   4 |    8 |   · |  900.2 | no output written by tra×4；verify=4×2   |
| worker:desktop30901 |  14 |   10 |  +1 |  546.2 | health×4；leak×3                         |
| worker:desktop30902 |  13 |   11 |  +1 |  603.4 | health×7；leak×3                         |
| worker:gemma31      |   1 |   34 |   · |    2.2 | no output written by tra×34              |
| worker:l4090        |   3 |    9 |   · |  900.3 | no output written by tra×7；health×1     |
| worker:laguna       | 108 |  116 |  +1 |  204.3 | no output written by tra×61；verify=1×17 |
| worker:laptop40901  |  10 |    7 |   · |  862.8 | health×3；leak×2                         |
| worker:laptop40902  |   9 |    8 |   · |  900.3 | leak×4；health×2                         |
| worker:mac          |  57 |  177 |  +1 |  243.7 | leak×100；verify=1×37                    |
| worker:nemo         | 317 |  480 |  +4 |  103.5 | leak×339；verify=1×65                    |
| worker:nemo2        | 280 |  412 |  +5 |  102.8 | leak×302；health×51                      |
| worker:nemo3        | 228 |  304 |  +2 |   98.0 | leak×194；verify=1×49                    |
| worker:oss20        |  37 |   80 |  +1 |  470.9 | leak×33；no output written by tra×17     |

endpoint 探活：local 🟢、laptop-4090 🟢、laptop-5090 🔴、desktop-3090 🟢、mac-m4max 🟢

（babel-pulse 常駐儀器自動快照）

## 2026-07-25T17:21:14+08:00（zh 總數 864）

| 語言 | fresh | stale | missing | 覆蓋率 | Δfresh | Δmissing |
| ---- | ----: | ----: | ------: | -----: | -----: | -------: |
| en   |   722 |   108 |      34 |  96.1% |      · |        · |
| ja   |   708 |   150 |       6 |  99.3% |      · |        · |
| ko   |   705 |   155 |       4 |  99.5% |      · |        · |
| es   |   714 |   147 |       3 |  99.7% |      · |        · |
| fr   |   706 |   156 |       2 |  99.8% |      · |        · |
| vi   |   104 |    10 |     750 |  13.2% |      · |        · |
| id   |   206 |     3 |     655 |  24.2% |     +1 |       -1 |
| pt   |   303 |     9 |     552 |  36.1% |      · |        · |
| hi   |   235 |     5 |     624 |  27.8% |      · |        · |
| ar   |   153 |     1 |     710 |  17.8% |     +1 |       -1 |
| ru   |   175 |     1 |     688 |  20.4% |     +1 |       -1 |

總缺口（stale+missing）：**4773**（▼3 vs 上一筆）

**節點／worker**（ok/fail 為累計；Δ為對上一筆）

| 節點                |  ok | fail | Δok | 平均秒 | 主要 fail                                |
| ------------------- | --: | ---: | --: | -----: | ---------------------------------------- |
| fleet:desktop-3090  |  56 |  325 |   · |      — | health×123；verify=1×102                 |
| fleet:laptop-4090   |  27 |  137 |   · |      — | health×83；verify=None×24                |
| worker:d3090        |   5 |    8 |  +1 |  900.2 | no output written by tra×4；verify=4×2   |
| worker:desktop30901 |  14 |   11 |   · |  546.2 | health×5；leak×3                         |
| worker:desktop30902 |  13 |   12 |   · |  603.4 | health×7；leak×3                         |
| worker:gemma31      |   1 |   34 |   · |    2.2 | no output written by tra×34              |
| worker:l4090        |   3 |   10 |   · |  900.3 | no output written by tra×7；leak×2       |
| worker:laguna       | 108 |  117 |   · |  204.3 | no output written by tra×61；verify=1×17 |
| worker:laptop40901  |  11 |    7 |  +1 |  866.2 | health×3；leak×2                         |
| worker:laptop40902  |  10 |    8 |  +1 |  900.3 | leak×4；health×2                         |
| worker:mac          |  58 |  180 |  +1 |  250.0 | leak×102；verify=1×37                    |
| worker:nemo         | 320 |  491 |  +3 |  103.7 | leak×345；verify=1×67                    |
| worker:nemo2        | 284 |  421 |  +4 |  103.7 | leak×308；health×53                      |
| worker:nemo3        | 230 |  305 |  +2 |   98.4 | leak×194；verify=1×50                    |
| worker:oss20        |  38 |   83 |  +1 |  474.3 | leak×34；no output written by tra×17     |

endpoint 探活：local 🟢、laptop-4090 🟢、laptop-5090 🔴、desktop-3090 🟢、mac-m4max 🟢

（babel-pulse 常駐儀器自動快照）

## 2026-07-25T17:36:51+08:00（zh 總數 864）

| 語言 | fresh | stale | missing | 覆蓋率 | Δfresh | Δmissing |
| ---- | ----: | ----: | ------: | -----: | -----: | -------: |
| en   |   722 |   108 |      34 |  96.1% |      · |        · |
| ja   |   708 |   150 |       6 |  99.3% |      · |        · |
| ko   |   705 |   155 |       4 |  99.5% |      · |        · |
| es   |   714 |   147 |       3 |  99.7% |      · |        · |
| fr   |   707 |   155 |       2 |  99.8% |     +1 |        · |
| vi   |   104 |    10 |     750 |  13.2% |      · |        · |
| id   |   206 |     3 |     655 |  24.2% |      · |        · |
| pt   |   305 |     9 |     550 |  36.3% |     +2 |       -2 |
| hi   |   237 |     5 |     622 |  28.0% |     +2 |       -2 |
| ar   |   159 |     1 |     704 |  18.5% |     +6 |       -6 |
| ru   |   176 |     1 |     687 |  20.5% |     +1 |       -1 |

總缺口（stale+missing）：**4761**（▼12 vs 上一筆）

**節點／worker**（ok/fail 為累計；Δ為對上一筆）

| 節點                |  ok | fail | Δok | 平均秒 | 主要 fail                                |
| ------------------- | --: | ---: | --: | -----: | ---------------------------------------- |
| fleet:desktop-3090  |  56 |  325 |   · |      — | health×123；verify=1×102                 |
| fleet:laptop-4090   |  27 |  137 |   · |      — | health×83；verify=None×24                |
| worker:d3090        |   6 |    8 |  +1 |  900.2 | no output written by tra×4；verify=4×2   |
| worker:desktop30901 |  15 |   11 |  +1 |  569.8 | health×5；leak×3                         |
| worker:desktop30902 |  13 |   13 |   · |  603.4 | health×8；leak×3                         |
| worker:gemma31      |   1 |   34 |   · |    2.2 | no output written by tra×34              |
| worker:l4090        |   3 |   11 |   · |  900.3 | no output written by tra×8；leak×2       |
| worker:laguna       | 110 |  118 |  +2 |  204.4 | no output written by tra×61；verify=1×17 |
| worker:laptop40901  |  11 |    8 |   · |  866.2 | health×4；leak×2                         |
| worker:laptop40902  |  11 |    8 |  +1 |  900.3 | leak×4；health×2                         |
| worker:mac          |  59 |  184 |  +1 |  250.4 | leak×105；verify=1×37                    |
| worker:nemo         | 323 |  503 |  +3 |  103.8 | leak×353；verify=1×67                    |
| worker:nemo2        | 288 |  428 |  +4 |  105.5 | leak×311；health×56                      |
| worker:nemo3        | 234 |  305 |  +4 |   99.0 | leak×194；verify=1×50                    |
| worker:oss20        |  40 |   87 |  +2 |  472.0 | leak×36；no output written by tra×18     |

endpoint 探活：local 🟢、laptop-4090 🟢、laptop-5090 🔴、desktop-3090 🟢、mac-m4max 🟢

（babel-pulse 常駐儀器自動快照）

## 2026-07-25T17:52:41+08:00（zh 總數 864）

| 語言 | fresh | stale | missing | 覆蓋率 | Δfresh | Δmissing |
| ---- | ----: | ----: | ------: | -----: | -----: | -------: |
| en   |   722 |   108 |      34 |  96.1% |      · |        · |
| ja   |   708 |   150 |       6 |  99.3% |      · |        · |
| ko   |   706 |   154 |       4 |  99.5% |     +1 |        · |
| es   |   714 |   147 |       3 |  99.7% |      · |        · |
| fr   |   707 |   155 |       2 |  99.8% |      · |        · |
| vi   |   107 |    10 |     747 |  13.5% |     +3 |       -3 |
| id   |   207 |     3 |     654 |  24.3% |     +1 |       -1 |
| pt   |   307 |     9 |     548 |  36.6% |     +2 |       -2 |
| hi   |   239 |     5 |     620 |  28.2% |     +2 |       -2 |
| ar   |   160 |     1 |     703 |  18.6% |     +1 |       -1 |
| ru   |   182 |     1 |     681 |  21.2% |     +6 |       -6 |

總缺口（stale+missing）：**4745**（▼16 vs 上一筆）

**節點／worker**（ok/fail 為累計；Δ為對上一筆）

| 節點                |  ok | fail | Δok | 平均秒 | 主要 fail                                |
| ------------------- | --: | ---: | --: | -----: | ---------------------------------------- |
| fleet:desktop-3090  |  56 |  325 |   · |      — | health×123；verify=1×102                 |
| fleet:laptop-4090   |  27 |  137 |   · |      — | health×83；verify=None×24                |
| worker:d3090        |   6 |    9 |   · |  900.2 | no output written by tra×5；verify=4×2   |
| worker:desktop30901 |  15 |   12 |   · |  569.8 | health×5；verify=4×3                     |
| worker:desktop30902 |  14 |   14 |  +1 |  624.6 | health×8；leak×4                         |
| worker:gemma31      |   1 |   34 |   · |    2.2 | no output written by tra×34              |
| worker:l4090        |   3 |   12 |   · |  900.3 | no output written by tra×9；leak×2       |
| worker:laguna       | 111 |  121 |  +1 |  203.1 | no output written by tra×62；verify=1×17 |
| worker:laptop40901  |  12 |    9 |  +1 |  869.1 | health×5；leak×2                         |
| worker:laptop40902  |  11 |    9 |   · |  900.3 | leak×4；verify=1×2                       |
| worker:mac          |  60 |  186 |  +1 |  250.5 | leak×105；verify=1×39                    |
| worker:nemo         | 334 |  516 | +11 |  102.7 | leak×363；verify=1×68                    |
| worker:nemo2        | 292 |  442 |  +4 |  105.4 | leak×320；health×59                      |
| worker:nemo3        | 237 |  312 |  +3 |   99.1 | leak×198；verify=1×52                    |
| worker:oss20        |  42 |   87 |  +2 |  469.4 | leak×36；no output written by tra×18     |

endpoint 探活：local 🟢、laptop-4090 🟢、laptop-5090 🔴、desktop-3090 🟢、mac-m4max 🟢

（babel-pulse 常駐儀器自動快照）

## 2026-07-25T17:53:47+08:00（zh 總數 864）

| 語言 | fresh | stale | missing | 覆蓋率 | Δfresh | Δmissing |
| ---- | ----: | ----: | ------: | -----: | -----: | -------: |
| en   |   722 |   108 |      34 |  96.1% |      · |        · |
| ja   |   708 |   150 |       6 |  99.3% |      · |        · |
| ko   |   706 |   154 |       4 |  99.5% |      · |        · |
| es   |   714 |   147 |       3 |  99.7% |      · |        · |
| fr   |   707 |   155 |       2 |  99.8% |      · |        · |
| vi   |   106 |    10 |     748 |  13.4% |     -1 |       +1 |
| id   |   207 |     3 |     654 |  24.3% |      · |        · |
| pt   |   308 |     9 |     547 |  36.7% |     +1 |       -1 |
| hi   |   240 |     5 |     619 |  28.4% |     +1 |       -1 |
| ar   |   158 |     1 |     705 |  18.4% |     -2 |       +2 |
| ru   |   182 |     1 |     681 |  21.2% |      · |        · |

總缺口（stale+missing）：**4746**（▲1 vs 上一筆）

**節點／worker**（ok/fail 為累計；Δ為對上一筆）

| 節點                |  ok | fail | Δok | 平均秒 | 主要 fail                                |
| ------------------- | --: | ---: | --: | -----: | ---------------------------------------- |
| fleet:desktop-3090  |  56 |  325 |   · |      — | health×123；verify=1×102                 |
| fleet:laptop-4090   |  27 |  137 |   · |      — | health×83；verify=None×24                |
| worker:d3090        |   6 |    9 |   · |  900.2 | no output written by tra×5；verify=4×2   |
| worker:desktop30901 |  15 |   12 |   · |  569.8 | health×5；verify=4×3                     |
| worker:desktop30902 |  14 |   14 |   · |  624.6 | health×8；leak×4                         |
| worker:gemma31      |   1 |   34 |   · |    2.2 | no output written by tra×34              |
| worker:l4090        |   3 |   12 |   · |  900.3 | no output written by tra×9；leak×2       |
| worker:laguna       | 111 |  121 |   · |  203.1 | no output written by tra×62；verify=1×17 |
| worker:laptop40901  |  12 |    9 |   · |  869.1 | health×5；leak×2                         |
| worker:laptop40902  |  11 |    9 |   · |  900.3 | leak×4；verify=1×2                       |
| worker:mac          |  60 |  186 |   · |  250.5 | leak×105；verify=1×39                    |
| worker:nemo         | 335 |  518 |  +1 |  102.5 | leak×365；verify=1×68                    |
| worker:nemo2        | 293 |  443 |  +1 |  105.2 | leak×321；health×59                      |
| worker:nemo3        | 237 |  312 |   · |   99.1 | leak×198；verify=1×52                    |
| worker:oss20        |  43 |   88 |  +1 |  461.8 | leak×37；no output written by tra×18     |

endpoint 探活：local 🟢、laptop-4090 🟢、laptop-5090 🔴、desktop-3090 🟢、mac-m4max 🟢

（babel-pulse 常駐儀器自動快照）

## 2026-07-25T18:08:18+08:00（zh 總數 864）

| 語言 | fresh | stale | missing | 覆蓋率 | Δfresh | Δmissing |
| ---- | ----: | ----: | ------: | -----: | -----: | -------: |
| en   |   722 |   108 |      34 |  96.1% |      · |        · |
| ja   |   709 |   149 |       6 |  99.3% |     +1 |        · |
| ko   |   706 |   154 |       4 |  99.5% |      · |        · |
| es   |   714 |   147 |       3 |  99.7% |      · |        · |
| fr   |   708 |   154 |       2 |  99.8% |     +1 |        · |
| vi   |   106 |    10 |     748 |  13.4% |      · |        · |
| id   |   209 |     3 |     652 |  24.5% |     +2 |       -2 |
| pt   |   311 |     9 |     544 |  37.0% |     +3 |       -3 |
| hi   |   244 |     5 |     615 |  28.8% |     +4 |       -4 |
| ar   |   161 |     1 |     702 |  18.8% |     +3 |       -3 |
| ru   |   185 |     1 |     678 |  21.5% |     +3 |       -3 |

總缺口（stale+missing）：**4729**（▼17 vs 上一筆）

**節點／worker**（ok/fail 為累計；Δ為對上一筆）

| 節點                |  ok | fail | Δok | 平均秒 | 主要 fail                                |
| ------------------- | --: | ---: | --: | -----: | ---------------------------------------- |
| fleet:desktop-3090  |  56 |  325 |   · |      — | health×123；verify=1×102                 |
| fleet:laptop-4090   |  27 |  137 |   · |      — | health×83；verify=None×24                |
| worker:d3090        |   6 |   10 |   · |  900.2 | no output written by tra×6；verify=4×2   |
| worker:desktop30901 |  15 |   13 |   · |  569.8 | health×5；verify=4×3                     |
| worker:desktop30902 |  14 |   15 |   · |  624.6 | health×8；leak×4                         |
| worker:gemma31      |   1 |   34 |   · |    2.2 | no output written by tra×34              |
| worker:l4090        |   3 |   13 |   · |  900.3 | no output written by tra×10；leak×2      |
| worker:laguna       | 112 |  123 |  +1 |  203.0 | no output written by tra×62；verify=1×18 |
| worker:laptop40901  |  13 |    9 |  +1 |  871.5 | health×5；leak×2                         |
| worker:laptop40902  |  12 |    9 |  +1 |  900.3 | leak×4；verify=1×2                       |
| worker:mac          |  63 |  188 |  +3 |  252.2 | leak×106；verify=1×39                    |
| worker:nemo         | 339 |  528 |  +4 |  101.9 | leak×371；verify=1×69                    |
| worker:nemo2        | 298 |  456 |  +5 |  105.1 | leak×334；health×59                      |
| worker:nemo3        | 243 |  315 |  +6 |   99.4 | leak×200；verify=1×53                    |
| worker:oss20        |  43 |   92 |   · |  461.8 | leak×38；no output written by tra×19     |

endpoint 探活：local 🟢、laptop-4090 🟢、laptop-5090 🔴、desktop-3090 🟢、mac-m4max 🟢

（babel-pulse 常駐儀器自動快照）

## 2026-07-25T18:23:58+08:00（zh 總數 864）

| 語言 | fresh | stale | missing | 覆蓋率 | Δfresh | Δmissing |
| ---- | ----: | ----: | ------: | -----: | -----: | -------: |
| en   |   722 |   108 |      34 |  96.1% |      · |        · |
| ja   |   709 |   149 |       6 |  99.3% |      · |        · |
| ko   |   706 |   154 |       4 |  99.5% |      · |        · |
| es   |   714 |   147 |       3 |  99.7% |      · |        · |
| fr   |   709 |   153 |       2 |  99.8% |     +1 |        · |
| vi   |   107 |    10 |     747 |  13.5% |     +1 |       -1 |
| id   |   210 |     3 |     651 |  24.7% |     +1 |       -1 |
| pt   |   314 |     9 |     541 |  37.4% |     +3 |       -3 |
| hi   |   245 |     5 |     614 |  28.9% |     +1 |       -1 |
| ar   |   161 |     1 |     702 |  18.8% |      · |        · |
| ru   |   186 |     1 |     677 |  21.6% |     +1 |       -1 |

總缺口（stale+missing）：**4721**（▼8 vs 上一筆）

**節點／worker**（ok/fail 為累計；Δ為對上一筆）

| 節點                |  ok | fail | Δok | 平均秒 | 主要 fail                                |
| ------------------- | --: | ---: | --: | -----: | ---------------------------------------- |
| fleet:desktop-3090  |  56 |  325 |   · |      — | health×123；verify=1×102                 |
| fleet:laptop-4090   |  27 |  137 |   · |      — | health×83；verify=None×24                |
| worker:d3090        |   6 |   11 |   · |  900.2 | no output written by tra×6；verify=4×2   |
| worker:desktop30901 |  16 |   13 |  +1 |  590.5 | health×5；verify=4×3                     |
| worker:desktop30902 |  15 |   15 |  +1 |  641.8 | health×8；leak×4                         |
| worker:gemma31      |   1 |   34 |   · |    2.2 | no output written by tra×34              |
| worker:l4090        |   3 |   13 |   · |  900.3 | no output written by tra×10；leak×2      |
| worker:laguna       | 114 |  125 |  +2 |  204.2 | no output written by tra×63；verify=1×19 |
| worker:laptop40901  |  14 |    9 |  +1 |  873.5 | health×5；leak×2                         |
| worker:laptop40902  |  12 |   10 |   · |  900.3 | leak×5；verify=1×2                       |
| worker:mac          |  65 |  190 |  +2 |  248.0 | leak×107；verify=1×39                    |
| worker:nemo         | 340 |  536 |  +1 |  102.0 | leak×377；verify=1×69                    |
| worker:nemo2        | 300 |  466 |  +2 |  105.8 | leak×341；health×61                      |
| worker:nemo3        | 244 |  321 |  +1 |   99.4 | leak×205；verify=1×53                    |
| worker:oss20        |  46 |   92 |  +3 |  455.5 | leak×38；no output written by tra×19     |

endpoint 探活：local 🟢、laptop-4090 🟢、laptop-5090 🔴、desktop-3090 🟢、mac-m4max 🟢

（babel-pulse 常駐儀器自動快照）

## 2026-07-25T18:39:38+08:00（zh 總數 864）

| 語言 | fresh | stale | missing | 覆蓋率 | Δfresh | Δmissing |
| ---- | ----: | ----: | ------: | -----: | -----: | -------: |
| en   |   722 |   108 |      34 |  96.1% |      · |        · |
| ja   |   709 |   149 |       6 |  99.3% |      · |        · |
| ko   |   706 |   154 |       4 |  99.5% |      · |        · |
| es   |   714 |   147 |       3 |  99.7% |      · |        · |
| fr   |   709 |   153 |       2 |  99.8% |      · |        · |
| vi   |   108 |    10 |     746 |  13.7% |     +1 |       -1 |
| id   |   212 |     3 |     649 |  24.9% |     +2 |       -2 |
| pt   |   313 |     9 |     542 |  37.3% |     -1 |       +1 |
| hi   |   248 |     5 |     611 |  29.3% |     +3 |       -3 |
| ar   |   165 |     1 |     698 |  19.2% |     +4 |       -4 |
| ru   |   188 |     1 |     675 |  21.9% |     +2 |       -2 |

總缺口（stale+missing）：**4710**（▼11 vs 上一筆）

**節點／worker**（ok/fail 為累計；Δ為對上一筆）

| 節點                |  ok | fail | Δok | 平均秒 | 主要 fail                                |
| ------------------- | --: | ---: | --: | -----: | ---------------------------------------- |
| fleet:desktop-3090  |  56 |  325 |   · |      — | health×123；verify=1×102                 |
| fleet:laptop-4090   |  27 |  137 |   · |      — | health×83；verify=None×24                |
| worker:d3090        |   6 |   12 |   · |  900.2 | no output written by tra×6；verify=4×2   |
| worker:desktop30901 |  17 |   14 |  +1 |  608.7 | health×6；verify=4×3                     |
| worker:desktop30902 |  15 |   16 |   · |  641.8 | health×8；leak×4                         |
| worker:gemma31      |   1 |   34 |   · |    2.2 | no output written by tra×34              |
| worker:l4090        |   3 |   13 |   · |  900.3 | no output written by tra×10；leak×2      |
| worker:laguna       | 116 |  125 |  +2 |  207.6 | no output written by tra×63；verify=1×19 |
| worker:laptop40901  |  14 |   10 |   · |  873.5 | health×6；leak×2                         |
| worker:laptop40902  |  12 |   11 |   · |  900.3 | leak×5；verify=1×2                       |
| worker:mac          |  66 |  194 |  +1 |  247.9 | leak×111；verify=1×39                    |
| worker:nemo         | 342 |  550 |  +2 |  102.2 | leak×386；health×70                      |
| worker:nemo2        | 303 |  478 |  +3 |  105.7 | leak×346；health×68                      |
| worker:nemo3        | 249 |  327 |  +5 |   99.6 | leak×210；verify=1×53                    |
| worker:oss20        |  48 |   94 |  +2 |  450.1 | leak×38；no output written by tra×20     |

endpoint 探活：local 🟢、laptop-4090 🟢、laptop-5090 🔴、desktop-3090 🟢、mac-m4max 🟢

（babel-pulse 常駐儀器自動快照）

## 2026-07-25T18:54:58+08:00（zh 總數 864）

| 語言 | fresh | stale | missing | 覆蓋率 | Δfresh | Δmissing |
| ---- | ----: | ----: | ------: | -----: | -----: | -------: |
| en   |   722 |   108 |      34 |  96.1% |      · |        · |
| ja   |   709 |   149 |       6 |  99.3% |      · |        · |
| ko   |   706 |   154 |       4 |  99.5% |      · |        · |
| es   |   714 |   147 |       3 |  99.7% |      · |        · |
| fr   |   709 |   153 |       2 |  99.8% |      · |        · |
| vi   |   108 |    10 |     746 |  13.7% |      · |        · |
| id   |   212 |     3 |     649 |  24.9% |      · |        · |
| pt   |   317 |     9 |     538 |  37.7% |     +4 |       -4 |
| hi   |   250 |     5 |     609 |  29.5% |     +2 |       -2 |
| ar   |   166 |     1 |     697 |  19.3% |     +1 |       -1 |
| ru   |   191 |     1 |     672 |  22.2% |     +3 |       -3 |

總缺口（stale+missing）：**4700**（▼10 vs 上一筆）

**節點／worker**（ok/fail 為累計；Δ為對上一筆）

| 節點                |  ok | fail | Δok | 平均秒 | 主要 fail                                |
| ------------------- | --: | ---: | --: | -----: | ---------------------------------------- |
| fleet:desktop-3090  |  56 |  325 |   · |      — | health×123；verify=1×102                 |
| fleet:laptop-4090   |  27 |  137 |   · |      — | health×83；verify=None×24                |
| worker:d3090        |   6 |   13 |   · |  900.2 | no output written by tra×7；verify=4×2   |
| worker:desktop30901 |  18 |   14 |  +1 |  624.9 | health×6；verify=4×3                     |
| worker:desktop30902 |  15 |   17 |   · |  641.8 | health×9；leak×4                         |
| worker:gemma31      |   1 |   34 |   · |    2.2 | no output written by tra×34              |
| worker:l4090        |   4 |   13 |  +1 |  900.2 | no output written by tra×10；leak×2      |
| worker:laguna       | 116 |  126 |   · |  207.6 | no output written by tra×63；verify=1×19 |
| worker:laptop40901  |  15 |   10 |  +1 |  875.3 | health×6；leak×2                         |
| worker:laptop40902  |  13 |   11 |  +1 |  900.3 | leak×5；verify=1×2                       |
| worker:mac          |  67 |  200 |  +1 |  245.8 | leak×115；verify=1×39                    |
| worker:nemo         | 345 |  560 |  +3 |  102.2 | leak×392；health×72                      |
| worker:nemo2        | 306 |  486 |  +3 |  105.6 | leak×354；health×68                      |
| worker:nemo3        | 251 |  334 |  +2 |   99.6 | leak×213；verify=1×54                    |
| worker:oss20        |  49 |   95 |  +1 |  452.4 | leak×38；no output written by tra×21     |

endpoint 探活：local 🟢、laptop-4090 🟢、laptop-5090 🔴、desktop-3090 🟢、mac-m4max 🟢

（babel-pulse 常駐儀器自動快照）

## 2026-07-25T18:56:42+08:00（zh 總數 864）

| 語言 | fresh | stale | missing | 覆蓋率 | Δfresh | Δmissing |
| ---- | ----: | ----: | ------: | -----: | -----: | -------: |
| en   |   722 |   108 |      34 |  96.1% |      · |        · |
| ja   |   709 |   149 |       6 |  99.3% |      · |        · |
| ko   |   706 |   154 |       4 |  99.5% |      · |        · |
| es   |   714 |   147 |       3 |  99.7% |      · |        · |
| fr   |   709 |   153 |       2 |  99.8% |      · |        · |
| vi   |   108 |    10 |     746 |  13.7% |      · |        · |
| id   |   212 |     3 |     649 |  24.9% |      · |        · |
| pt   |   318 |     9 |     537 |  37.8% |     +1 |       -1 |
| hi   |   250 |     5 |     609 |  29.5% |      · |        · |
| ar   |   167 |     1 |     696 |  19.4% |     +1 |       -1 |
| ru   |   191 |     1 |     672 |  22.2% |      · |        · |

總缺口（stale+missing）：**4698**（▼2 vs 上一筆）

**節點／worker**（ok/fail 為累計；Δ為對上一筆）

| 節點                |  ok | fail | Δok | 平均秒 | 主要 fail                                |
| ------------------- | --: | ---: | --: | -----: | ---------------------------------------- |
| fleet:desktop-3090  |  56 |  325 |   · |      — | health×123；verify=1×102                 |
| fleet:laptop-4090   |  27 |  137 |   · |      — | health×83；verify=None×24                |
| worker:d3090        |   6 |   13 |   · |  900.2 | no output written by tra×7；verify=4×2   |
| worker:desktop30901 |  18 |   14 |   · |  624.9 | health×6；verify=4×3                     |
| worker:desktop30902 |  15 |   17 |   · |  641.8 | health×9；leak×4                         |
| worker:gemma31      |   1 |   34 |   · |    2.2 | no output written by tra×34              |
| worker:l4090        |   4 |   13 |   · |  900.2 | no output written by tra×10；leak×2      |
| worker:laguna       | 116 |  126 |   · |  207.6 | no output written by tra×63；verify=1×19 |
| worker:laptop40901  |  15 |   10 |   · |  875.3 | health×6；leak×2                         |
| worker:laptop40902  |  13 |   11 |   · |  900.3 | leak×5；verify=1×2                       |
| worker:mac          |  67 |  200 |   · |  245.8 | leak×115；verify=1×39                    |
| worker:nemo         | 345 |  561 |   · |  102.2 | leak×393；health×72                      |
| worker:nemo2        | 306 |  488 |   · |  105.6 | leak×355；health×68                      |
| worker:nemo3        | 252 |  334 |  +1 |   99.8 | leak×213；verify=1×54                    |
| worker:oss20        |  49 |   97 |   · |  452.4 | leak×39；no output written by tra×22     |

endpoint 探活：local 🟢、laptop-4090 🟢、laptop-5090 🔴、desktop-3090 🟢、mac-m4max 🟢

（babel-pulse 常駐儀器自動快照）

## 2026-07-25T19:10:30+08:00（zh 總數 864）

| 語言 | fresh | stale | missing | 覆蓋率 | Δfresh | Δmissing |
| ---- | ----: | ----: | ------: | -----: | -----: | -------: |
| en   |   722 |   108 |      34 |  96.1% |      · |        · |
| ja   |   710 |   148 |       6 |  99.3% |     +1 |        · |
| ko   |   708 |   152 |       4 |  99.5% |     +2 |        · |
| es   |   714 |   147 |       3 |  99.7% |      · |        · |
| fr   |   709 |   153 |       2 |  99.8% |      · |        · |
| vi   |   108 |    10 |     746 |  13.7% |      · |        · |
| id   |   212 |     3 |     649 |  24.9% |      · |        · |
| pt   |   320 |     9 |     535 |  38.1% |     +2 |       -2 |
| hi   |   250 |     5 |     609 |  29.5% |      · |        · |
| ar   |   169 |     1 |     694 |  19.7% |     +2 |       -2 |
| ru   |   192 |     1 |     671 |  22.3% |     +1 |       -1 |

總缺口（stale+missing）：**4690**（▼8 vs 上一筆）

**節點／worker**（ok/fail 為累計；Δ為對上一筆）

| 節點                |  ok | fail | Δok | 平均秒 | 主要 fail                                |
| ------------------- | --: | ---: | --: | -----: | ---------------------------------------- |
| fleet:desktop-3090  |  56 |  325 |   · |      — | health×123；verify=1×102                 |
| fleet:laptop-4090   |  27 |  137 |   · |      — | health×83；verify=None×24                |
| worker:d3090        |   6 |   14 |   · |  900.2 | no output written by tra×8；verify=4×2   |
| worker:desktop30901 |  19 |   14 |  +1 |  637.6 | health×6；verify=4×3                     |
| worker:desktop30902 |  15 |   18 |   · |  641.8 | health×9；leak×4                         |
| worker:gemma31      |   1 |   34 |   · |    2.2 | no output written by tra×34              |
| worker:l4090        |   4 |   14 |   · |  900.2 | no output written by tra×10；leak×3      |
| worker:laguna       | 117 |  127 |  +1 |  211.0 | no output written by tra×64；verify=1×19 |
| worker:laptop40901  |  16 |   10 |  +1 |  872.5 | health×6；leak×2                         |
| worker:laptop40902  |  13 |   12 |   · |  900.3 | leak×5；health×3                         |
| worker:mac          |  68 |  204 |  +1 |  245.9 | leak×117；verify=1×40                    |
| worker:nemo         | 347 |  569 |  +2 |  102.6 | leak×399；health×74                      |
| worker:nemo2        | 308 |  494 |  +2 |  105.7 | leak×359；health×69                      |
| worker:nemo3        | 253 |  336 |  +1 |   99.7 | leak×215；verify=1×54                    |
| worker:oss20        |  50 |   99 |  +1 |  446.9 | leak×39；no output written by tra×23     |

endpoint 探活：local 🟢、laptop-4090 🟢、laptop-5090 🔴、desktop-3090 🟢、mac-m4max 🟢

（babel-pulse 常駐儀器自動快照）

## 2026-07-25T19:33:22+08:00（zh 總數 864）

| 語言 | fresh | stale | missing | 覆蓋率 | Δfresh | Δmissing |
| ---- | ----: | ----: | ------: | -----: | -----: | -------: |
| en   |   722 |   108 |      34 |  96.1% |      · |        · |
| ja   |   710 |   148 |       6 |  99.3% |      · |        · |
| ko   |   708 |   152 |       4 |  99.5% |      · |        · |
| es   |   715 |   146 |       3 |  99.7% |     +1 |        · |
| fr   |   710 |   152 |       2 |  99.8% |     +1 |        · |
| vi   |   108 |    10 |     746 |  13.7% |      · |        · |
| id   |   214 |     3 |     647 |  25.1% |     +2 |       -2 |
| pt   |   322 |     9 |     533 |  38.3% |     +2 |       -2 |
| hi   |   253 |     5 |     606 |  29.9% |     +3 |       -3 |
| ar   |   173 |     1 |     690 |  20.1% |     +4 |       -4 |
| ru   |   197 |     1 |     666 |  22.9% |     +5 |       -5 |

總缺口（stale+missing）：**4672**（▼18 vs 上一筆）

**節點／worker**（ok/fail 為累計；Δ為對上一筆）

| 節點                |  ok | fail | Δok | 平均秒 | 主要 fail                                |
| ------------------- | --: | ---: | --: | -----: | ---------------------------------------- |
| fleet:desktop-3090  |  56 |  325 |   · |      — | health×123；verify=1×102                 |
| fleet:laptop-4090   |  27 |  137 |   · |      — | health×83；verify=None×24                |
| worker:d3090        |   6 |   15 |   · |  900.2 | no output written by tra×9；verify=4×2   |
| worker:desktop30901 |  20 |   17 |  +1 |  610.2 | health×8；leak×4                         |
| worker:desktop30902 |  16 |   21 |  +1 |  613.5 | health×10；leak×5                        |
| worker:gemma31      |   1 |   34 |   · |    2.2 | no output written by tra×34              |
| worker:l4090        |   5 |   14 |  +1 |  900.3 | no output written by tra×10；leak×3      |
| worker:laguna       | 117 |  128 |   · |  211.0 | no output written by tra×65；verify=1×19 |
| worker:laptop40901  |  16 |   12 |   · |  872.5 | health×7；leak×2                         |
| worker:laptop40902  |  14 |   13 |  +1 |  893.8 | leak×5；health×4                         |
| worker:mac          |  71 |  207 |  +3 |  243.2 | leak×120；verify=1×40                    |
| worker:nemo         | 353 |  583 |  +6 |  103.4 | leak×409；health×74                      |
| worker:nemo2        | 312 |  503 |  +4 |  106.7 | leak×364；health×71                      |
| worker:nemo3        | 257 |  344 |  +4 |   99.7 | leak×221；verify=1×55                    |
| worker:oss20        |  51 |  100 |  +1 |  443.5 | leak×40；no output written by tra×23     |

endpoint 探活：local 🟢、laptop-4090 🟢、laptop-5090 🔴、desktop-3090 🟢、mac-m4max 🟢

⚙️ 哲宇 19:3x 暫停 mouhouse babel routine 避免兩機翻譯衝突——本指揮部（mac+l4090+d3090+OpenRouter 池）單機作業中；mouhouse 恢復時 Stage 0 git pull 會自動繼承今日全部工具進化

## 2026-07-25T19:41:44+08:00（zh 總數 864）

| 語言 | fresh | stale | missing | 覆蓋率 | Δfresh | Δmissing |
| ---- | ----: | ----: | ------: | -----: | -----: | -------: |
| en   |   722 |   108 |      34 |  96.1% |      · |        · |
| ja   |   710 |   148 |       6 |  99.3% |      · |        · |
| ko   |   708 |   152 |       4 |  99.5% |      · |        · |
| es   |   715 |   146 |       3 |  99.7% |      · |        · |
| fr   |   710 |   152 |       2 |  99.8% |      · |        · |
| vi   |   108 |    10 |     746 |  13.7% |      · |        · |
| id   |   214 |     3 |     647 |  25.1% |      · |        · |
| pt   |   322 |     9 |     533 |  38.3% |      · |        · |
| hi   |   255 |     5 |     604 |  30.1% |     +2 |       -2 |
| ar   |   174 |     1 |     689 |  20.3% |     +1 |       -1 |
| ru   |   197 |     1 |     666 |  22.9% |      · |        · |

總缺口（stale+missing）：**4669**（▼3 vs 上一筆）

**節點／worker**（ok/fail 為累計；Δ為對上一筆）

| 節點                |  ok | fail | Δok | 平均秒 | 主要 fail                                |
| ------------------- | --: | ---: | --: | -----: | ---------------------------------------- |
| fleet:desktop-3090  |  56 |  325 |   · |      — | health×123；verify=1×102                 |
| fleet:laptop-4090   |  27 |  137 |   · |      — | health×83；verify=None×24                |
| worker:d3090        |   6 |   15 |   · |  900.2 | no output written by tra×9；verify=4×2   |
| worker:desktop30901 |  20 |   17 |   · |  610.2 | health×8；leak×4                         |
| worker:desktop30902 |  16 |   21 |   · |  613.5 | health×10；leak×5                        |
| worker:gemma31      |   1 |   34 |   · |    2.2 | no output written by tra×34              |
| worker:l4090        |   5 |   14 |   · |  900.3 | no output written by tra×10；leak×3      |
| worker:laguna       | 117 |  129 |   · |  211.0 | no output written by tra×66；verify=1×19 |
| worker:laptop40901  |  16 |   12 |   · |  872.5 | health×7；leak×2                         |
| worker:laptop40902  |  14 |   13 |   · |  893.8 | leak×5；health×4                         |
| worker:mac          |  71 |  208 |   · |  243.2 | leak×121；verify=1×40                    |
| worker:nemo         | 353 |  585 |   · |  103.4 | leak×410；health×74                      |
| worker:nemo2        | 314 |  506 |  +2 |  107.2 | leak×365；health×71                      |
| worker:nemo3        | 258 |  345 |  +1 |   99.6 | leak×222；verify=1×55                    |
| worker:oss20        |  51 |  102 |   · |  443.5 | leak×41；no output written by tra×24     |

endpoint 探活：local 🟢、laptop-4090 🟢、laptop-5090 🔴、desktop-3090 🟢、mac-m4max 🟢

（babel-pulse 常駐儀器自動快照）

## 2026-07-25T19:57:29+08:00（zh 總數 864）

| 語言 | fresh | stale | missing | 覆蓋率 | Δfresh | Δmissing |
| ---- | ----: | ----: | ------: | -----: | -----: | -------: |
| en   |   722 |   108 |      34 |  96.1% |      · |        · |
| ja   |   710 |   148 |       6 |  99.3% |      · |        · |
| ko   |   708 |   152 |       4 |  99.5% |      · |        · |
| es   |   715 |   146 |       3 |  99.7% |      · |        · |
| fr   |   710 |   152 |       2 |  99.8% |      · |        · |
| vi   |   108 |    10 |     746 |  13.7% |      · |        · |
| id   |   214 |     3 |     647 |  25.1% |      · |        · |
| pt   |   326 |     9 |     529 |  38.8% |     +4 |       -4 |
| hi   |   256 |     5 |     603 |  30.2% |     +1 |       -1 |
| ar   |   177 |     1 |     686 |  20.6% |     +3 |       -3 |
| ru   |   200 |     1 |     663 |  23.3% |     +3 |       -3 |

總缺口（stale+missing）：**4658**（▼11 vs 上一筆）

**節點／worker**（ok/fail 為累計；Δ為對上一筆）

| 節點                |  ok | fail | Δok | 平均秒 | 主要 fail                                |
| ------------------- | --: | ---: | --: | -----: | ---------------------------------------- |
| fleet:desktop-3090  |  56 |  325 |   · |      — | health×123；verify=1×102                 |
| fleet:laptop-4090   |  27 |  137 |   · |      — | health×83；verify=None×24                |
| worker:d3090        |   7 |   16 |  +1 |  900.2 | no output written by tra×10；verify=4×2  |
| worker:desktop30901 |  20 |   17 |   · |  610.2 | health×8；leak×4                         |
| worker:desktop30902 |  16 |   21 |   · |  613.5 | health×10；leak×5                        |
| worker:gemma31      |   1 |   34 |   · |    2.2 | no output written by tra×34              |
| worker:l4090        |   6 |   15 |  +1 |  900.2 | no output written by tra×11；leak×3      |
| worker:laguna       | 117 |  131 |   · |  211.0 | no output written by tra×68；verify=1×19 |
| worker:laptop40901  |  16 |   13 |   · |  872.5 | health×8；leak×2                         |
| worker:laptop40902  |  15 |   13 |  +1 |  894.2 | leak×5；health×4                         |
| worker:mac          |  72 |  211 |  +1 |  246.4 | leak×122；verify=1×40                    |
| worker:nemo         | 356 |  590 |  +3 |  105.0 | leak×414；health×75                      |
| worker:nemo2        | 319 |  513 |  +5 |  107.4 | leak×371；health×71                      |
| worker:nemo3        | 258 |  349 |   · |   99.6 | leak×225；verify=1×55                    |
| worker:oss20        |  54 |  104 |  +3 |  433.8 | leak×42；no output written by tra×24     |

endpoint 探活：local 🟢、laptop-4090 🟢、laptop-5090 🔴、desktop-3090 🟢、mac-m4max 🟢

（babel-pulse 常駐儀器自動快照）

## 2026-07-25T20:13:12+08:00（zh 總數 864）

| 語言 | fresh | stale | missing | 覆蓋率 | Δfresh | Δmissing |
| ---- | ----: | ----: | ------: | -----: | -----: | -------: |
| en   |   722 |   108 |      34 |  96.1% |      · |        · |
| ja   |   710 |   148 |       6 |  99.3% |      · |        · |
| ko   |   708 |   152 |       4 |  99.5% |      · |        · |
| es   |   715 |   146 |       3 |  99.7% |      · |        · |
| fr   |   710 |   152 |       2 |  99.8% |      · |        · |
| vi   |   108 |    10 |     746 |  13.7% |      · |        · |
| id   |   214 |     3 |     647 |  25.1% |      · |        · |
| pt   |   330 |     9 |     525 |  39.2% |     +4 |       -4 |
| hi   |   258 |     5 |     601 |  30.4% |     +2 |       -2 |
| ar   |   182 |     1 |     681 |  21.2% |     +5 |       -5 |
| ru   |   201 |     1 |     662 |  23.4% |     +1 |       -1 |

總缺口（stale+missing）：**4646**（▼12 vs 上一筆）

**節點／worker**（ok/fail 為累計；Δ為對上一筆）

| 節點                |  ok | fail | Δok | 平均秒 | 主要 fail                                |
| ------------------- | --: | ---: | --: | -----: | ---------------------------------------- |
| fleet:desktop-3090  |  56 |  325 |   · |      — | health×123；verify=1×102                 |
| fleet:laptop-4090   |  27 |  137 |   · |      — | health×83；verify=None×24                |
| worker:d3090        |   8 |   16 |  +1 |  900.2 | no output written by tra×10；verify=4×2  |
| worker:desktop30901 |  20 |   18 |   · |  610.2 | health×9；leak×4                         |
| worker:desktop30902 |  16 |   22 |   · |  613.5 | health×10；leak×5                        |
| worker:gemma31      |   1 |   34 |   · |    2.2 | no output written by tra×34              |
| worker:l4090        |   6 |   16 |   · |  900.2 | no output written by tra×11；leak×4      |
| worker:laguna       | 117 |  131 |   · |  211.0 | no output written by tra×68；verify=1×19 |
| worker:laptop40901  |  16 |   14 |   · |  872.5 | health×9；leak×2                         |
| worker:laptop40902  |  15 |   14 |   · |  894.2 | leak×5；health×5                         |
| worker:mac          |  73 |  212 |  +1 |  251.6 | leak×123；verify=1×40                    |
| worker:nemo         | 361 |  597 |  +5 |  104.9 | leak×419；health×76                      |
| worker:nemo2        | 322 |  519 |  +3 |  107.6 | leak×376；health×71                      |
| worker:nemo3        | 261 |  352 |  +3 |   99.5 | leak×226；verify=1×55                    |
| worker:oss20        |  55 |  108 |  +1 |  433.9 | leak×43；no output written by tra×24     |

endpoint 探活：local 🟢、laptop-4090 🟢、laptop-5090 🔴、desktop-3090 🟢、mac-m4max 🟢

（babel-pulse 常駐儀器自動快照）

## 2026-07-25T20:28:48+08:00（zh 總數 864）

| 語言 | fresh | stale | missing | 覆蓋率 | Δfresh | Δmissing |
| ---- | ----: | ----: | ------: | -----: | -----: | -------: |
| en   |   722 |   108 |      34 |  96.1% |      · |        · |
| ja   |   711 |   148 |       5 |  99.4% |     +1 |       -1 |
| ko   |   708 |   152 |       4 |  99.5% |      · |        · |
| es   |   715 |   146 |       3 |  99.7% |      · |        · |
| fr   |   710 |   152 |       2 |  99.8% |      · |        · |
| vi   |   109 |    10 |     745 |  13.8% |     +1 |       -1 |
| id   |   214 |     3 |     647 |  25.1% |      · |        · |
| pt   |   332 |     9 |     523 |  39.5% |     +2 |       -2 |
| hi   |   260 |     5 |     599 |  30.7% |     +2 |       -2 |
| ar   |   183 |     1 |     680 |  21.3% |     +1 |       -1 |
| ru   |   203 |     1 |     660 |  23.6% |     +2 |       -2 |

總缺口（stale+missing）：**4637**（▼9 vs 上一筆）

**節點／worker**（ok/fail 為累計；Δ為對上一筆）

| 節點                |  ok | fail | Δok | 平均秒 | 主要 fail                                |
| ------------------- | --: | ---: | --: | -----: | ---------------------------------------- |
| fleet:desktop-3090  |  56 |  325 |   · |      — | health×123；verify=1×102                 |
| fleet:laptop-4090   |  27 |  137 |   · |      — | health×83；verify=None×24                |
| worker:d3090        |   8 |   17 |   · |  900.2 | no output written by tra×10；verify=4×3  |
| worker:desktop30901 |  21 |   19 |  +1 |  624.0 | health×10；leak×4                        |
| worker:desktop30902 |  16 |   23 |   · |  613.5 | health×10；verify=1×6                    |
| worker:gemma31      |   1 |   34 |   · |    2.2 | no output written by tra×34              |
| worker:l4090        |   6 |   17 |   · |  900.2 | no output written by tra×11；leak×4      |
| worker:laguna       | 117 |  131 |   · |  211.0 | no output written by tra×68；verify=1×19 |
| worker:laptop40901  |  17 |   14 |  +1 |  874.1 | health×9；leak×2                         |
| worker:laptop40902  |  15 |   15 |   · |  894.2 | leak×6；health×5                         |
| worker:mac          |  74 |  214 |  +1 |  252.4 | leak×125；verify=1×40                    |
| worker:nemo         | 367 |  605 |  +6 |  105.2 | leak×424；health×79                      |
| worker:nemo2        | 324 |  530 |  +2 |  107.6 | leak×384；health×72                      |
| worker:nemo3        | 263 |  356 |  +2 |   99.6 | leak×230；verify=1×55                    |
| worker:oss20        |  56 |  110 |  +1 |  430.9 | leak×43；no output written by tra×26     |

endpoint 探活：local 🟢、laptop-4090 🟢、laptop-5090 🔴、desktop-3090 🟢、mac-m4max 🟢

（babel-pulse 常駐儀器自動快照）

## 2026-07-25T20:28:59+08:00（zh 總數 864）

| 語言 | fresh | stale | missing | 覆蓋率 | Δfresh | Δmissing |
| ---- | ----: | ----: | ------: | -----: | -----: | -------: |
| en   |   722 |   108 |      34 |  96.1% |      · |        · |
| ja   |   711 |   148 |       5 |  99.4% |     +1 |       -1 |
| ko   |   708 |   152 |       4 |  99.5% |      · |        · |
| es   |   715 |   146 |       3 |  99.7% |      · |        · |
| fr   |   710 |   152 |       2 |  99.8% |      · |        · |
| vi   |   109 |    10 |     745 |  13.8% |     +1 |       -1 |
| id   |   214 |     3 |     647 |  25.1% |      · |        · |
| pt   |   332 |     9 |     523 |  39.5% |     +2 |       -2 |
| hi   |   260 |     5 |     599 |  30.7% |     +2 |       -2 |
| ar   |   183 |     1 |     680 |  21.3% |     +1 |       -1 |
| ru   |   203 |     1 |     660 |  23.6% |     +2 |       -2 |

總缺口（stale+missing）：**4637**（▼9 vs 上一筆）

**節點／worker**（ok/fail 為累計；Δ為對上一筆）

| 節點                |  ok | fail | Δok | 平均秒 | 主要 fail                                |
| ------------------- | --: | ---: | --: | -----: | ---------------------------------------- |
| fleet:desktop-3090  |  56 |  325 |   · |      — | health×123；verify=1×102                 |
| fleet:laptop-4090   |  27 |  137 |   · |      — | health×83；verify=None×24                |
| worker:d3090        |   8 |   17 |   · |  900.2 | no output written by tra×10；verify=4×3  |
| worker:desktop30901 |  21 |   19 |  +1 |  624.0 | health×10；leak×4                        |
| worker:desktop30902 |  16 |   23 |   · |  613.5 | health×10；verify=1×6                    |
| worker:gemma31      |   1 |   34 |   · |    2.2 | no output written by tra×34              |
| worker:l4090        |   6 |   17 |   · |  900.2 | no output written by tra×11；leak×4      |
| worker:laguna       | 117 |  131 |   · |  211.0 | no output written by tra×68；verify=1×19 |
| worker:laptop40901  |  17 |   14 |  +1 |  874.1 | health×9；leak×2                         |
| worker:laptop40902  |  15 |   15 |   · |  894.2 | leak×6；health×5                         |
| worker:mac          |  74 |  214 |  +1 |  252.4 | leak×125；verify=1×40                    |
| worker:nemo         | 367 |  606 |  +6 |  105.2 | leak×425；health×79                      |
| worker:nemo2        | 324 |  530 |  +2 |  107.6 | leak×384；health×72                      |
| worker:nemo3        | 263 |  356 |  +2 |   99.6 | leak×230；verify=1×55                    |
| worker:oss20        |  56 |  110 |  +1 |  430.9 | leak×43；no output written by tra×26     |

endpoint 探活：local 🟢、laptop-4090 🟢、laptop-5090 🔴、desktop-3090 🟢、mac-m4max 🟢

（babel-pulse 常駐儀器自動快照）

## 2026-07-25T20:44:46+08:00（zh 總數 864）

| 語言 | fresh | stale | missing | 覆蓋率 | Δfresh | Δmissing |
| ---- | ----: | ----: | ------: | -----: | -----: | -------: |
| en   |   722 |   108 |      34 |  96.1% |      · |        · |
| ja   |   712 |   147 |       5 |  99.4% |     +1 |        · |
| ko   |   708 |   152 |       4 |  99.5% |      · |        · |
| es   |   715 |   146 |       3 |  99.7% |      · |        · |
| fr   |   710 |   152 |       2 |  99.8% |      · |        · |
| vi   |   111 |    10 |     743 |  14.0% |     +2 |       -2 |
| id   |   214 |     3 |     647 |  25.1% |      · |        · |
| pt   |   334 |     9 |     521 |  39.7% |     +2 |       -2 |
| hi   |   264 |     5 |     595 |  31.1% |     +4 |       -4 |
| ar   |   186 |     1 |     677 |  21.6% |     +3 |       -3 |
| ru   |   206 |     1 |     657 |  24.0% |     +3 |       -3 |

總缺口（stale+missing）：**4622**（▼15 vs 上一筆）

**節點／worker**（ok/fail 為累計；Δ為對上一筆）

| 節點                |  ok | fail | Δok | 平均秒 | 主要 fail                                |
| ------------------- | --: | ---: | --: | -----: | ---------------------------------------- |
| fleet:desktop-3090  |  56 |  325 |   · |      — | health×123；verify=1×102                 |
| fleet:laptop-4090   |  27 |  137 |   · |      — | health×83；verify=None×24                |
| worker:d3090        |   8 |   18 |   · |  900.2 | no output written by tra×10；verify=4×4  |
| worker:desktop30901 |  21 |   19 |   · |  624.0 | health×10；leak×4                        |
| worker:desktop30902 |  16 |   23 |   · |  613.5 | health×10；verify=1×6                    |
| worker:gemma31      |   1 |   34 |   · |    2.2 | no output written by tra×34              |
| worker:l4090        |   6 |   18 |   · |  900.2 | no output written by tra×11；leak×5      |
| worker:laguna       | 117 |  133 |   · |  211.0 | no output written by tra×69；verify=1×19 |
| worker:laptop40901  |  17 |   14 |   · |  874.1 | health×9；leak×2                         |
| worker:laptop40902  |  15 |   15 |   · |  894.2 | leak×6；health×5                         |
| worker:mac          |  75 |  217 |  +1 |  253.9 | leak×126；verify=1×41                    |
| worker:nemo         | 369 |  609 |  +2 |  105.4 | leak×426；health×81                      |
| worker:nemo2        | 327 |  535 |  +3 |  107.8 | leak×387；health×74                      |
| worker:nemo3        | 268 |  360 |  +5 |   99.5 | leak×233；verify=1×55                    |
| worker:oss20        |  57 |  112 |  +1 |  435.0 | leak×44；no output written by tra×27     |

endpoint 探活：local 🟢、laptop-4090 🟢、laptop-5090 🔴、desktop-3090 🟢、mac-m4max 🟢

（babel-pulse 常駐儀器自動快照）

## 2026-07-25T21:00:14+08:00（zh 總數 864）

| 語言 | fresh | stale | missing | 覆蓋率 | Δfresh | Δmissing |
| ---- | ----: | ----: | ------: | -----: | -----: | -------: |
| en   |   722 |   108 |      34 |  96.1% |      · |        · |
| ja   |   712 |   147 |       5 |  99.4% |      · |        · |
| ko   |   708 |   152 |       4 |  99.5% |      · |        · |
| es   |   715 |   146 |       3 |  99.7% |      · |        · |
| fr   |   710 |   152 |       2 |  99.8% |      · |        · |
| vi   |   111 |    10 |     743 |  14.0% |      · |        · |
| id   |   214 |     3 |     647 |  25.1% |      · |        · |
| pt   |   337 |     9 |     518 |  40.0% |     +3 |       -3 |
| hi   |   264 |     5 |     595 |  31.1% |      · |        · |
| ar   |   188 |     1 |     675 |  21.9% |     +2 |       -2 |
| ru   |   207 |     1 |     656 |  24.1% |     +1 |       -1 |

總缺口（stale+missing）：**4616**（▼6 vs 上一筆）

**節點／worker**（ok/fail 為累計；Δ為對上一筆）

| 節點                |  ok | fail | Δok | 平均秒 | 主要 fail                                |
| ------------------- | --: | ---: | --: | -----: | ---------------------------------------- |
| fleet:desktop-3090  |  56 |  325 |   · |      — | health×123；verify=1×102                 |
| fleet:laptop-4090   |  27 |  137 |   · |      — | health×83；verify=None×24                |
| worker:d3090        |   8 |   19 |   · |  900.2 | no output written by tra×11；verify=4×4  |
| worker:desktop30901 |  21 |   19 |   · |  624.0 | health×10；leak×4                        |
| worker:desktop30902 |  16 |   23 |   · |  613.5 | health×10；verify=1×6                    |
| worker:gemma31      |   1 |   34 |   · |    2.2 | no output written by tra×34              |
| worker:l4090        |   6 |   19 |   · |  900.2 | no output written by tra×11；leak×6      |
| worker:laguna       | 117 |  134 |   · |  211.0 | no output written by tra×70；verify=1×19 |
| worker:laptop40901  |  17 |   14 |   · |  874.1 | health×9；leak×2                         |
| worker:laptop40902  |  15 |   15 |   · |  894.2 | leak×6；health×5                         |
| worker:mac          |  75 |  221 |   · |  253.9 | leak×129；verify=1×41                    |
| worker:nemo         | 372 |  614 |  +3 |  105.5 | leak×428；health×84                      |
| worker:nemo2        | 329 |  542 |  +2 |  107.8 | leak×393；health×74                      |
| worker:nemo3        | 270 |  367 |  +2 |   99.1 | leak×236；verify=1×55                    |
| worker:oss20        |  57 |  113 |   · |  435.0 | leak×44；no output written by tra×28     |

endpoint 探活：local 🟢、laptop-4090 🟢、laptop-5090 🔴、desktop-3090 🟢、mac-m4max 🟢

（babel-pulse 常駐儀器自動快照）

## 2026-07-25T21:15:51+08:00（zh 總數 864）

| 語言 | fresh | stale | missing | 覆蓋率 | Δfresh | Δmissing |
| ---- | ----: | ----: | ------: | -----: | -----: | -------: |
| en   |   722 |   108 |      34 |  96.1% |      · |        · |
| ja   |   712 |   147 |       5 |  99.4% |      · |        · |
| ko   |   708 |   152 |       4 |  99.5% |      · |        · |
| es   |   715 |   146 |       3 |  99.7% |      · |        · |
| fr   |   710 |   152 |       2 |  99.8% |      · |        · |
| vi   |   111 |    10 |     743 |  14.0% |      · |        · |
| id   |   214 |     3 |     647 |  25.1% |      · |        · |
| pt   |   337 |     9 |     518 |  40.0% |      · |        · |
| hi   |   264 |     5 |     595 |  31.1% |      · |        · |
| ar   |   187 |     1 |     676 |  21.8% |     -1 |       +1 |
| ru   |   210 |     1 |     653 |  24.4% |     +3 |       -3 |

總缺口（stale+missing）：**4614**（▼2 vs 上一筆）

**節點／worker**（ok/fail 為累計；Δ為對上一筆）

| 節點                |  ok | fail | Δok | 平均秒 | 主要 fail                                |
| ------------------- | --: | ---: | --: | -----: | ---------------------------------------- |
| fleet:desktop-3090  |  56 |  325 |   · |      — | health×123；verify=1×102                 |
| fleet:laptop-4090   |  27 |  137 |   · |      — | health×83；verify=None×24                |
| worker:d3090        |   8 |   20 |   · |  900.2 | no output written by tra×11；verify=4×5  |
| worker:desktop30901 |  21 |   19 |   · |  624.0 | health×10；leak×4                        |
| worker:desktop30902 |  16 |   23 |   · |  613.5 | health×10；verify=1×6                    |
| worker:gemma31      |   1 |   34 |   · |    2.2 | no output written by tra×34              |
| worker:l4090        |   7 |   19 |  +1 |  900.2 | no output written by tra×11；leak×6      |
| worker:laguna       | 117 |  135 |   · |  211.0 | no output written by tra×71；verify=1×19 |
| worker:laptop40901  |  17 |   14 |   · |  874.1 | health×9；leak×2                         |
| worker:laptop40902  |  15 |   15 |   · |  894.2 | leak×6；health×5                         |
| worker:mac          |  75 |  224 |   · |  253.9 | leak×131；verify=1×41                    |
| worker:nemo         | 374 |  619 |  +2 |  105.8 | leak×430；health×86                      |
| worker:nemo2        | 329 |  548 |   · |  107.8 | leak×396；health×77                      |
| worker:nemo3        | 272 |  373 |  +2 |   99.2 | leak×240；verify=1×56                    |
| worker:oss20        |  57 |  116 |   · |  435.0 | leak×45；no output written by tra×28     |

endpoint 探活：local 🟢、laptop-4090 🟢、laptop-5090 🔴、desktop-3090 🟢、mac-m4max 🟢

（babel-pulse 常駐儀器自動快照）

## 2026-07-25T21:31:27+08:00（zh 總數 864）

| 語言 | fresh | stale | missing | 覆蓋率 | Δfresh | Δmissing |
| ---- | ----: | ----: | ------: | -----: | -----: | -------: |
| en   |   722 |   108 |      34 |  96.1% |      · |        · |
| ja   |   712 |   147 |       5 |  99.4% |      · |        · |
| ko   |   709 |   151 |       4 |  99.5% |     +1 |        · |
| es   |   715 |   146 |       3 |  99.7% |      · |        · |
| fr   |   710 |   152 |       2 |  99.8% |      · |        · |
| vi   |   112 |    10 |     742 |  14.1% |     +1 |       -1 |
| id   |   214 |     3 |     647 |  25.1% |      · |        · |
| pt   |   336 |     9 |     519 |  39.9% |     -1 |       +1 |
| hi   |   266 |     5 |     593 |  31.4% |     +2 |       -2 |
| ar   |   190 |     1 |     673 |  22.1% |     +3 |       -3 |
| ru   |   211 |     1 |     652 |  24.5% |     +1 |       -1 |

總缺口（stale+missing）：**4607**（▼7 vs 上一筆）

**節點／worker**（ok/fail 為累計；Δ為對上一筆）

| 節點                |  ok | fail | Δok | 平均秒 | 主要 fail                                |
| ------------------- | --: | ---: | --: | -----: | ---------------------------------------- |
| fleet:desktop-3090  |  56 |  325 |   · |      — | health×123；verify=1×102                 |
| fleet:laptop-4090   |  27 |  137 |   · |      — | health×83；verify=None×24                |
| worker:d3090        |   8 |   21 |   · |  900.2 | no output written by tra×11；verify=4×5  |
| worker:desktop30901 |  21 |   19 |   · |  624.0 | health×10；leak×4                        |
| worker:desktop30902 |  16 |   23 |   · |  613.5 | health×10；verify=1×6                    |
| worker:gemma31      |   1 |   34 |   · |    2.2 | no output written by tra×34              |
| worker:l4090        |   8 |   20 |  +1 |  900.2 | no output written by tra×11；leak×7      |
| worker:laguna       | 117 |  135 |   · |  211.0 | no output written by tra×71；verify=1×19 |
| worker:laptop40901  |  17 |   14 |   · |  874.1 | health×9；leak×2                         |
| worker:laptop40902  |  15 |   15 |   · |  894.2 | leak×6；health×5                         |
| worker:mac          |  77 |  227 |  +2 |  254.6 | leak×132；verify=1×41                    |
| worker:nemo         | 376 |  623 |  +2 |  105.9 | leak×430；health×87                      |
| worker:nemo2        | 331 |  553 |  +2 |  107.9 | leak×398；health×79                      |
| worker:nemo3        | 274 |  379 |  +2 |   99.4 | leak×244；verify=1×56                    |
| worker:oss20        |  57 |  118 |   · |  435.0 | leak×45；no output written by tra×28     |

endpoint 探活：local 🟢、laptop-4090 🟢、laptop-5090 🔴、desktop-3090 🟢、mac-m4max 🟢

（babel-pulse 常駐儀器自動快照）

## 2026-07-25T21:32:42+08:00（zh 總數 864）

| 語言 | fresh | stale | missing | 覆蓋率 | Δfresh | Δmissing |
| ---- | ----: | ----: | ------: | -----: | -----: | -------: |
| en   |   722 |   108 |      34 |  96.1% |      · |        · |
| ja   |   712 |   147 |       5 |  99.4% |      · |        · |
| ko   |   709 |   151 |       4 |  99.5% |      · |        · |
| es   |   715 |   146 |       3 |  99.7% |      · |        · |
| fr   |   710 |   152 |       2 |  99.8% |      · |        · |
| vi   |   112 |    10 |     742 |  14.1% |      · |        · |
| id   |   214 |     3 |     647 |  25.1% |      · |        · |
| pt   |   336 |     9 |     519 |  39.9% |      · |        · |
| hi   |   266 |     5 |     593 |  31.4% |      · |        · |
| ar   |   190 |     1 |     673 |  22.1% |      · |        · |
| ru   |   211 |     1 |     652 |  24.5% |      · |        · |

總缺口（stale+missing）：**4607**（＝0 vs 上一筆）

**節點／worker**（ok/fail 為累計；Δ為對上一筆）

| 節點                |  ok | fail | Δok | 平均秒 | 主要 fail                                |
| ------------------- | --: | ---: | --: | -----: | ---------------------------------------- |
| fleet:desktop-3090  |  56 |  325 |   · |      — | health×123；verify=1×102                 |
| fleet:laptop-4090   |  27 |  137 |   · |      — | health×83；verify=None×24                |
| worker:d3090        |   8 |   21 |   · |  900.2 | no output written by tra×11；verify=4×5  |
| worker:desktop30901 |  21 |   19 |   · |  624.0 | health×10；leak×4                        |
| worker:desktop30902 |  16 |   23 |   · |  613.5 | health×10；verify=1×6                    |
| worker:gemma31      |   1 |   34 |   · |    2.2 | no output written by tra×34              |
| worker:l4090        |   8 |   20 |   · |  900.2 | no output written by tra×11；leak×7      |
| worker:laguna       | 117 |  135 |   · |  211.0 | no output written by tra×71；verify=1×19 |
| worker:laptop40901  |  17 |   14 |   · |  874.1 | health×9；leak×2                         |
| worker:laptop40902  |  15 |   15 |   · |  894.2 | leak×6；health×5                         |
| worker:mac          |  77 |  227 |   · |  254.6 | leak×132；verify=1×41                    |
| worker:nemo         | 376 |  623 |   · |  105.9 | leak×430；health×87                      |
| worker:nemo2        | 331 |  553 |   · |  107.9 | leak×398；health×79                      |
| worker:nemo3        | 274 |  380 |   · |   99.4 | leak×245；verify=1×56                    |
| worker:oss20        |  57 |  118 |   · |  435.0 | leak×45；no output written by tra×28     |

endpoint 探活：local 🟢、laptop-4090 🟢、laptop-5090 🔴、desktop-3090 🟢、mac-m4max 🟢

（babel-pulse 常駐儀器自動快照）

## 2026-07-25T21:47:04+08:00（zh 總數 864）

| 語言 | fresh | stale | missing | 覆蓋率 | Δfresh | Δmissing |
| ---- | ----: | ----: | ------: | -----: | -----: | -------: |
| en   |   722 |   108 |      34 |  96.1% |      · |        · |
| ja   |   712 |   147 |       5 |  99.4% |      · |        · |
| ko   |   709 |   151 |       4 |  99.5% |      · |        · |
| es   |   715 |   146 |       3 |  99.7% |      · |        · |
| fr   |   710 |   152 |       2 |  99.8% |      · |        · |
| vi   |   112 |    10 |     742 |  14.1% |      · |        · |
| id   |   214 |     3 |     647 |  25.1% |      · |        · |
| pt   |   335 |     9 |     520 |  39.8% |     -1 |       +1 |
| hi   |   266 |     5 |     593 |  31.4% |      · |        · |
| ar   |   191 |     1 |     672 |  22.2% |     +1 |       -1 |
| ru   |   213 |     1 |     650 |  24.8% |     +2 |       -2 |

總缺口（stale+missing）：**4605**（▼2 vs 上一筆）

**節點／worker**（ok/fail 為累計；Δ為對上一筆）

| 節點                |  ok | fail | Δok | 平均秒 | 主要 fail                                |
| ------------------- | --: | ---: | --: | -----: | ---------------------------------------- |
| fleet:desktop-3090  |  56 |  325 |   · |      — | health×123；verify=1×102                 |
| fleet:laptop-4090   |  27 |  137 |   · |      — | health×83；verify=None×24                |
| worker:d3090        |   8 |   21 |   · |  900.2 | no output written by tra×11；verify=4×5  |
| worker:desktop30901 |  21 |   19 |   · |  624.0 | health×10；leak×4                        |
| worker:desktop30902 |  16 |   23 |   · |  613.5 | health×10；verify=1×6                    |
| worker:gemma31      |   1 |   34 |   · |    2.2 | no output written by tra×34              |
| worker:l4090        |   8 |   20 |   · |  900.2 | no output written by tra×11；leak×7      |
| worker:laguna       | 117 |  136 |   · |  211.0 | no output written by tra×72；verify=1×19 |
| worker:laptop40901  |  17 |   14 |   · |  874.1 | health×9；leak×2                         |
| worker:laptop40902  |  15 |   15 |   · |  894.2 | leak×6；health×5                         |
| worker:mac          |  77 |  231 |   · |  254.6 | leak×134；verify=1×42                    |
| worker:nemo         | 376 |  625 |   · |  105.9 | leak×431；health×87                      |
| worker:nemo2        | 332 |  555 |  +1 |  107.8 | leak×398；health×80                      |
| worker:nemo3        | 274 |  381 |   · |   99.4 | leak×245；verify=1×56                    |
| worker:oss20        |  59 |  118 |  +2 |  430.8 | leak×45；no output written by tra×28     |

endpoint 探活：local 🟢、laptop-4090 🟢、laptop-5090 🔴、desktop-3090 🟢、mac-m4max 🟢

（babel-pulse 常駐儀器自動快照）

## 2026-07-25T22:02:45+08:00（zh 總數 864）

| 語言 | fresh | stale | missing | 覆蓋率 | Δfresh | Δmissing |
| ---- | ----: | ----: | ------: | -----: | -----: | -------: |
| en   |   722 |   108 |      34 |  96.1% |      · |        · |
| ja   |   712 |   147 |       5 |  99.4% |      · |        · |
| ko   |   709 |   151 |       4 |  99.5% |      · |        · |
| es   |   715 |   146 |       3 |  99.7% |      · |        · |
| fr   |   710 |   152 |       2 |  99.8% |      · |        · |
| vi   |   112 |    10 |     742 |  14.1% |      · |        · |
| id   |   214 |     3 |     647 |  25.1% |      · |        · |
| pt   |   335 |     9 |     520 |  39.8% |      · |        · |
| hi   |   266 |     5 |     593 |  31.4% |      · |        · |
| ar   |   191 |     1 |     672 |  22.2% |      · |        · |
| ru   |   213 |     1 |     650 |  24.8% |      · |        · |

總缺口（stale+missing）：**4605**（＝0 vs 上一筆）

**節點／worker**（ok/fail 為累計；Δ為對上一筆）

| 節點                |  ok | fail | Δok | 平均秒 | 主要 fail                                |
| ------------------- | --: | ---: | --: | -----: | ---------------------------------------- |
| fleet:desktop-3090  |  56 |  325 |   · |      — | health×123；verify=1×102                 |
| fleet:laptop-4090   |  27 |  137 |   · |      — | health×83；verify=None×24                |
| worker:d3090        |   9 |   21 |  +1 |  900.2 | no output written by tra×11；verify=4×5  |
| worker:desktop30901 |  21 |   19 |   · |  624.0 | health×10；leak×4                        |
| worker:desktop30902 |  16 |   23 |   · |  613.5 | health×10；verify=1×6                    |
| worker:gemma31      |   1 |   34 |   · |    2.2 | no output written by tra×34              |
| worker:l4090        |   9 |   20 |  +1 |  900.2 | no output written by tra×11；leak×7      |
| worker:laguna       | 117 |  137 |   · |  211.0 | no output written by tra×73；verify=1×19 |
| worker:laptop40901  |  17 |   14 |   · |  874.1 | health×9；leak×2                         |
| worker:laptop40902  |  15 |   15 |   · |  894.2 | leak×6；health×5                         |
| worker:mac          |  78 |  233 |  +1 |  256.8 | leak×134；verify=1×43                    |
| worker:nemo         | 377 |  629 |  +1 |  106.0 | leak×434；health×88                      |
| worker:nemo2        | 333 |  557 |  +1 |  108.3 | leak×400；health×80                      |
| worker:nemo3        | 274 |  384 |   · |   99.4 | leak×247；verify=1×56                    |
| worker:oss20        |  59 |  119 |   · |  430.8 | leak×45；no output written by tra×28     |

endpoint 探活：local 🟢、laptop-4090 🟢、laptop-5090 🔴、desktop-3090 🟢、mac-m4max 🟢

（babel-pulse 常駐儀器自動快照）
