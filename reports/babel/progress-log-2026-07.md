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

## 2026-07-25T22:18:26+08:00（zh 總數 864）

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
| hi   |   268 |     5 |     591 |  31.6% |     +2 |       -2 |
| ar   |   192 |     1 |     671 |  22.3% |     +1 |       -1 |
| ru   |   216 |     1 |     647 |  25.1% |     +3 |       -3 |

總缺口（stale+missing）：**4599**（▼6 vs 上一筆）

**節點／worker**（ok/fail 為累計；Δ為對上一筆）

| 節點                |  ok | fail | Δok | 平均秒 | 主要 fail                                |
| ------------------- | --: | ---: | --: | -----: | ---------------------------------------- |
| fleet:desktop-3090  |  56 |  325 |   · |      — | health×123；verify=1×102                 |
| fleet:laptop-4090   |  27 |  137 |   · |      — | health×83；verify=None×24                |
| worker:d3090        |   9 |   22 |   · |  900.2 | no output written by tra×12；verify=4×5  |
| worker:desktop30901 |  21 |   19 |   · |  624.0 | health×10；leak×4                        |
| worker:desktop30902 |  16 |   23 |   · |  613.5 | health×10；verify=1×6                    |
| worker:gemma31      |   1 |   34 |   · |    2.2 | no output written by tra×34              |
| worker:l4090        |   9 |   21 |   · |  900.2 | no output written by tra×12；leak×7      |
| worker:laguna       | 117 |  138 |   · |  211.0 | no output written by tra×74；verify=1×19 |
| worker:laptop40901  |  17 |   14 |   · |  874.1 | health×9；leak×2                         |
| worker:laptop40902  |  15 |   15 |   · |  894.2 | leak×6；health×5                         |
| worker:mac          |  78 |  236 |   · |  256.8 | leak×135；verify=1×45                    |
| worker:nemo         | 377 |  633 |   · |  106.0 | leak×436；health×89                      |
| worker:nemo2        | 334 |  560 |  +1 |  108.3 | leak×402；health×80                      |
| worker:nemo3        | 277 |  387 |  +3 |   99.5 | leak×249；verify=1×56                    |
| worker:oss20        |  60 |  120 |  +1 |  428.5 | leak×45；no output written by tra×29     |

endpoint 探活：local 🟢、laptop-4090 🟢、laptop-5090 🔴、desktop-3090 🟢、mac-m4max 🟢

（babel-pulse 常駐儀器自動快照）

## 2026-07-25T22:33:51+08:00（zh 總數 864）

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
| hi   |   269 |     5 |     590 |  31.7% |     +1 |       -1 |
| ar   |   195 |     1 |     668 |  22.7% |     +3 |       -3 |
| ru   |   219 |     1 |     644 |  25.5% |     +3 |       -3 |

總缺口（stale+missing）：**4592**（▼7 vs 上一筆）

**節點／worker**（ok/fail 為累計；Δ為對上一筆）

| 節點                |  ok | fail | Δok | 平均秒 | 主要 fail                                |
| ------------------- | --: | ---: | --: | -----: | ---------------------------------------- |
| fleet:desktop-3090  |  56 |  325 |   · |      — | health×123；verify=1×102                 |
| fleet:laptop-4090   |  27 |  137 |   · |      — | health×83；verify=None×24                |
| worker:d3090        |  10 |   22 |  +1 |  900.2 | no output written by tra×12；verify=4×5  |
| worker:desktop30901 |  21 |   19 |   · |  624.0 | health×10；leak×4                        |
| worker:desktop30902 |  16 |   23 |   · |  613.5 | health×10；verify=1×6                    |
| worker:gemma31      |   1 |   34 |   · |    2.2 | no output written by tra×34              |
| worker:l4090        |   9 |   22 |   · |  900.2 | no output written by tra×12；leak×8      |
| worker:laguna       | 117 |  138 |   · |  211.0 | no output written by tra×74；verify=1×19 |
| worker:laptop40901  |  17 |   14 |   · |  874.1 | health×9；leak×2                         |
| worker:laptop40902  |  15 |   15 |   · |  894.2 | leak×6；health×5                         |
| worker:mac          |  78 |  239 |   · |  256.8 | leak×138；verify=1×45                    |
| worker:nemo         | 379 |  636 |  +2 |  106.1 | leak×437；health×91                      |
| worker:nemo2        | 335 |  563 |  +1 |  108.4 | leak×403；health×80                      |
| worker:nemo3        | 279 |  390 |  +2 |   99.5 | leak×251；verify=1×56                    |
| worker:oss20        |  61 |  120 |  +1 |  433.8 | leak×45；no output written by tra×29     |

endpoint 探活：local 🟢、laptop-4090 🟢、laptop-5090 🔴、desktop-3090 🟢、mac-m4max 🟢

（babel-pulse 常駐儀器自動快照）

## 2026-07-25T22:36:39+08:00（zh 總數 864）

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
| hi   |   270 |     5 |     589 |  31.8% |     +1 |       -1 |
| ar   |   195 |     1 |     668 |  22.7% |      · |        · |
| ru   |   220 |     1 |     643 |  25.6% |     +1 |       -1 |

總缺口（stale+missing）：**4590**（▼2 vs 上一筆）

**節點／worker**（ok/fail 為累計；Δ為對上一筆）

| 節點                |  ok | fail | Δok | 平均秒 | 主要 fail                                |
| ------------------- | --: | ---: | --: | -----: | ---------------------------------------- |
| fleet:desktop-3090  |  56 |  325 |   · |      — | health×123；verify=1×102                 |
| fleet:laptop-4090   |  27 |  137 |   · |      — | health×83；verify=None×24                |
| worker:d3090        |  10 |   23 |   · |  900.2 | no output written by tra×13；verify=4×5  |
| worker:desktop30901 |  21 |   19 |   · |  624.0 | health×10；leak×4                        |
| worker:desktop30902 |  16 |   23 |   · |  613.5 | health×10；verify=1×6                    |
| worker:gemma31      |   1 |   34 |   · |    2.2 | no output written by tra×34              |
| worker:l4090        |   9 |   23 |   · |  900.2 | no output written by tra×13；leak×8      |
| worker:laguna       | 117 |  139 |   · |  211.0 | no output written by tra×74；verify=1×20 |
| worker:laptop40901  |  17 |   14 |   · |  874.1 | health×9；leak×2                         |
| worker:laptop40902  |  15 |   15 |   · |  894.2 | leak×6；health×5                         |
| worker:mac          |  78 |  240 |   · |  256.8 | leak×138；verify=1×45                    |
| worker:nemo         | 379 |  637 |   · |  106.1 | leak×437；health×91                      |
| worker:nemo2        | 337 |  563 |  +2 |  108.2 | leak×403；health×80                      |
| worker:nemo3        | 279 |  392 |   · |   99.5 | leak×253；verify=1×56                    |
| worker:oss20        |  61 |  120 |   · |  433.8 | leak×45；no output written by tra×29     |

endpoint 探活：local 🟢、laptop-4090 🟢、laptop-5090 🔴、desktop-3090 🟢、mac-m4max 🟢

（babel-pulse 常駐儀器自動快照）

## 2026-07-25T22:49:23+08:00（zh 總數 864）

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
| hi   |   271 |     5 |     588 |  31.9% |     +1 |       -1 |
| ar   |   197 |     1 |     666 |  22.9% |     +2 |       -2 |
| ru   |   222 |     1 |     641 |  25.8% |     +2 |       -2 |

總缺口（stale+missing）：**4585**（▼5 vs 上一筆）

**節點／worker**（ok/fail 為累計；Δ為對上一筆）

| 節點                |  ok | fail | Δok | 平均秒 | 主要 fail                                |
| ------------------- | --: | ---: | --: | -----: | ---------------------------------------- |
| fleet:desktop-3090  |  56 |  325 |   · |      — | health×123；verify=1×102                 |
| fleet:laptop-4090   |  27 |  137 |   · |      — | health×83；verify=None×24                |
| worker:d3090        |  10 |   24 |   · |  900.2 | no output written by tra×13；verify=4×5  |
| worker:desktop30901 |  21 |   19 |   · |  624.0 | health×10；leak×4                        |
| worker:desktop30902 |  16 |   23 |   · |  613.5 | health×10；verify=1×6                    |
| worker:gemma31      |   1 |   34 |   · |    2.2 | no output written by tra×34              |
| worker:l4090        |   9 |   24 |   · |  900.2 | no output written by tra×13；leak×8      |
| worker:laguna       | 117 |  140 |   · |  211.0 | no output written by tra×75；verify=1×20 |
| worker:laptop40901  |  17 |   14 |   · |  874.1 | health×9；leak×2                         |
| worker:laptop40902  |  15 |   15 |   · |  894.2 | leak×6；health×5                         |
| worker:mac          |  78 |  242 |   · |  256.8 | leak×138；verify=1×46                    |
| worker:nemo         | 380 |  641 |  +1 |  106.0 | leak×439；health×93                      |
| worker:nemo2        | 338 |  565 |  +1 |  108.3 | leak×403；health×80                      |
| worker:nemo3        | 281 |  394 |  +2 |   99.9 | leak×254；verify=1×56                    |
| worker:oss20        |  62 |  121 |  +1 |  429.2 | leak×45；no output written by tra×30     |

endpoint 探活：local 🟢、laptop-4090 🟢、laptop-5090 🔴、desktop-3090 🟢、mac-m4max 🟢

（babel-pulse 常駐儀器自動快照）

## 2026-07-25T23:04:53+08:00（zh 總數 864）

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
| hi   |   274 |     5 |     585 |  32.3% |     +3 |       -3 |
| ar   |   200 |     1 |     663 |  23.3% |     +3 |       -3 |
| ru   |   224 |     1 |     639 |  26.0% |     +2 |       -2 |

總缺口（stale+missing）：**4577**（▼8 vs 上一筆）

**節點／worker**（ok/fail 為累計；Δ為對上一筆）

| 節點                |  ok | fail | Δok | 平均秒 | 主要 fail                                |
| ------------------- | --: | ---: | --: | -----: | ---------------------------------------- |
| fleet:desktop-3090  |  56 |  325 |   · |      — | health×123；verify=1×102                 |
| fleet:laptop-4090   |  27 |  137 |   · |      — | health×83；verify=None×24                |
| worker:d3090        |  10 |   25 |   · |  900.2 | no output written by tra×14；verify=4×5  |
| worker:desktop30901 |  21 |   19 |   · |  624.0 | health×10；leak×4                        |
| worker:desktop30902 |  16 |   23 |   · |  613.5 | health×10；verify=1×6                    |
| worker:gemma31      |   1 |   34 |   · |    2.2 | no output written by tra×34              |
| worker:l4090        |   9 |   25 |   · |  900.2 | no output written by tra×14；leak×8      |
| worker:laguna       | 118 |  142 |  +1 |  210.1 | no output written by tra×75；verify=1×20 |
| worker:laptop40901  |  17 |   14 |   · |  874.1 | health×9；leak×2                         |
| worker:laptop40902  |  15 |   15 |   · |  894.2 | leak×6；health×5                         |
| worker:mac          |  78 |  246 |   · |  256.8 | leak×140；verify=1×47                    |
| worker:nemo         | 382 |  644 |  +2 |  106.3 | leak×440；health×94                      |
| worker:nemo2        | 338 |  568 |   · |  108.3 | leak×403；health×81                      |
| worker:nemo3        | 284 |  399 |  +3 |   99.9 | leak×254；verify=1×56                    |
| worker:oss20        |  64 |  121 |  +2 |  432.6 | leak×45；no output written by tra×30     |

endpoint 探活：local 🟢、laptop-4090 🟢、laptop-5090 🔴、desktop-3090 🟢、mac-m4max 🟢

（babel-pulse 常駐儀器自動快照）

## 2026-07-25T23:51:50+08:00（zh 總數 865）

| 語言 | fresh | stale | missing | 覆蓋率 | Δfresh | Δmissing |
| ---- | ----: | ----: | ------: | -----: | -----: | -------: |
| en   |   721 |   109 |      35 |  96.0% |     -1 |       +1 |
| ja   |   712 |   147 |       6 |  99.3% |      · |       +1 |
| ko   |   709 |   151 |       5 |  99.4% |      · |       +1 |
| es   |   715 |   146 |       4 |  99.5% |      · |       +1 |
| fr   |   710 |   152 |       3 |  99.7% |      · |       +1 |
| vi   |   111 |    11 |     743 |  14.1% |     -1 |       +1 |
| id   |   213 |     4 |     648 |  25.1% |     -1 |       +1 |
| pt   |   335 |    10 |     520 |  39.9% |      · |        · |
| hi   |   276 |     6 |     583 |  32.6% |     +2 |       -2 |
| ar   |   205 |     1 |     659 |  23.8% |     +5 |       -4 |
| ru   |   231 |     1 |     633 |  26.8% |     +7 |       -6 |

總缺口（stale+missing）：**4577**（＝0 vs 上一筆）

**節點／worker**（ok/fail 為累計；Δ為對上一筆）

| 節點                |  ok | fail | Δok | 平均秒 | 主要 fail                               |
| ------------------- | --: | ---: | --: | -----: | --------------------------------------- |
| fleet:desktop-3090  |  56 |  325 |   · |      — | health×123；verify=1×102                |
| fleet:laptop-4090   |  27 |  137 |   · |      — | health×83；verify=None×24               |
| worker:d3090        |  12 |   26 |  +2 |  900.2 | no output written by tra×14；verify=4×5 |
| worker:desktop30901 |  21 |   19 |   · |  624.0 | health×10；leak×4                       |
| worker:desktop30902 |  16 |   23 |   · |  613.5 | health×10；verify=1×6                   |
| worker:gemma31      |   1 |   34 |   · |    2.2 | no output written by tra×34             |
| worker:l4090        |  11 |   28 |  +2 |  848.0 | no output written by tra×16；leak×8     |
| worker:laguna       | 118 |  148 |   · |  210.1 | no output written by tra×78；health×22  |
| worker:laptop40901  |  17 |   14 |   · |  874.1 | health×9；leak×2                        |
| worker:laptop40902  |  15 |   15 |   · |  894.2 | leak×6；health×5                        |
| worker:mac          |  81 |  255 |  +3 |  261.4 | leak×145；verify=1×48                   |
| worker:nemo         | 385 |  659 |  +3 |  107.1 | leak×448；health×98                     |
| worker:nemo2        | 346 |  582 |  +8 |  108.6 | leak×410；health×83                     |
| worker:nemo3        | 289 |  410 |  +5 |  100.6 | leak×258；verify=1×57                   |
| worker:oss20        |  66 |  123 |  +2 |  441.1 | leak×45；no output written by tra×30    |

endpoint 探活：local 🟢、laptop-4090 🟢、laptop-5090 🔴、desktop-3090 🟢、mac-m4max 🟢

（babel-pulse 常駐儀器自動快照）

## 2026-07-26T00:07:21+08:00（zh 總數 865）

| 語言 | fresh | stale | missing | 覆蓋率 | Δfresh | Δmissing |
| ---- | ----: | ----: | ------: | -----: | -----: | -------: |
| en   |   721 |   109 |      35 |  96.0% |      · |        · |
| ja   |   712 |   147 |       6 |  99.3% |      · |        · |
| ko   |   709 |   151 |       5 |  99.4% |      · |        · |
| es   |   715 |   146 |       4 |  99.5% |      · |        · |
| fr   |   710 |   152 |       3 |  99.7% |      · |        · |
| vi   |   111 |    11 |     743 |  14.1% |      · |        · |
| id   |   213 |     4 |     648 |  25.1% |      · |        · |
| pt   |   335 |    10 |     520 |  39.9% |      · |        · |
| hi   |   278 |     6 |     581 |  32.8% |     +2 |       -2 |
| ar   |   208 |     1 |     656 |  24.2% |     +3 |       -3 |
| ru   |   232 |     1 |     632 |  26.9% |     +1 |       -1 |

總缺口（stale+missing）：**4571**（▼6 vs 上一筆）

**節點／worker**（ok/fail 為累計；Δ為對上一筆）

| 節點                |  ok | fail | Δok | 平均秒 | 主要 fail                               |
| ------------------- | --: | ---: | --: | -----: | --------------------------------------- |
| fleet:desktop-3090  |  56 |  325 |   · |      — | health×123；verify=1×102                |
| fleet:laptop-4090   |  27 |  137 |   · |      — | health×83；verify=None×24               |
| worker:d3090        |  12 |   27 |   · |  900.2 | no output written by tra×15；verify=4×5 |
| worker:desktop30901 |  21 |   19 |   · |  624.0 | health×10；leak×4                       |
| worker:desktop30902 |  16 |   23 |   · |  613.5 | health×10；verify=1×6                   |
| worker:gemma31      |   1 |   34 |   · |    2.2 | no output written by tra×34             |
| worker:l4090        |  11 |   29 |   · |  848.0 | no output written by tra×16；leak×9     |
| worker:laguna       | 118 |  150 |   · |  210.1 | no output written by tra×80；health×22  |
| worker:laptop40901  |  17 |   14 |   · |  874.1 | health×9；leak×2                        |
| worker:laptop40902  |  15 |   15 |   · |  894.2 | leak×6；health×5                        |
| worker:mac          |  81 |  260 |   · |  261.4 | leak×149；verify=1×48                   |
| worker:nemo         | 388 |  664 |  +3 |  107.6 | leak×453；health×98                     |
| worker:nemo2        | 349 |  587 |  +3 |  108.5 | leak×414；health×83                     |
| worker:nemo3        | 289 |  413 |   · |  100.6 | leak×260；verify=1×57                   |
| worker:oss20        |  66 |  124 |   · |  441.1 | leak×45；no output written by tra×30    |

endpoint 探活：local 🟢、laptop-4090 🟢、laptop-5090 🔴、desktop-3090 🟢、mac-m4max 🟢

（babel-pulse 常駐儀器自動快照）

## 2026-07-26T00:22:51+08:00（zh 總數 865）

| 語言 | fresh | stale | missing | 覆蓋率 | Δfresh | Δmissing |
| ---- | ----: | ----: | ------: | -----: | -----: | -------: |
| en   |   721 |   109 |      35 |  96.0% |      · |        · |
| ja   |   712 |   147 |       6 |  99.3% |      · |        · |
| ko   |   709 |   151 |       5 |  99.4% |      · |        · |
| es   |   715 |   146 |       4 |  99.5% |      · |        · |
| fr   |   711 |   151 |       3 |  99.7% |     +1 |        · |
| vi   |   112 |    17 |     736 |  14.9% |     +1 |       -7 |
| id   |   212 |    11 |     642 |  25.8% |     -1 |       -6 |
| pt   |   338 |    12 |     515 |  40.5% |     +3 |       -5 |
| hi   |   278 |     7 |     580 |  32.9% |      · |       -1 |
| ar   |   209 |     1 |     655 |  24.3% |     +1 |       -1 |
| ru   |   233 |     1 |     631 |  27.1% |     +1 |       -1 |

總缺口（stale+missing）：**4565**（▼6 vs 上一筆）

**節點／worker**（ok/fail 為累計；Δ為對上一筆）

| 節點                |  ok | fail | Δok | 平均秒 | 主要 fail                               |
| ------------------- | --: | ---: | --: | -----: | --------------------------------------- |
| fleet:desktop-3090  |  56 |  325 |   · |      — | health×123；verify=1×102                |
| fleet:laptop-4090   |  27 |  137 |   · |      — | health×83；verify=None×24               |
| worker:d3090        |  12 |   28 |   · |  900.2 | no output written by tra×16；verify=4×5 |
| worker:desktop30901 |  21 |   19 |   · |  624.0 | health×10；leak×4                       |
| worker:desktop30902 |  16 |   23 |   · |  613.5 | health×10；verify=1×6                   |
| worker:gemma31      |   1 |   34 |   · |    2.2 | no output written by tra×34             |
| worker:l4090        |  11 |   31 |   · |  848.0 | no output written by tra×18；leak×9     |
| worker:laguna       | 119 |  151 |  +1 |  214.2 | no output written by tra×80；health×23  |
| worker:laptop40901  |  17 |   14 |   · |  874.1 | health×9；leak×2                        |
| worker:laptop40902  |  15 |   15 |   · |  894.2 | leak×6；health×5                        |
| worker:mac          |  82 |  266 |  +1 |  260.4 | leak×151；verify=1×50                   |
| worker:nemo         | 390 |  667 |  +2 |  107.6 | leak×453；health×101                    |
| worker:nemo2        | 350 |  589 |  +1 |  108.7 | leak×415；health×83                     |
| worker:nemo3        | 291 |  416 |  +2 |  100.2 | leak×262；verify=1×58                   |
| worker:oss20        |  67 |  124 |  +1 |  452.5 | leak×45；no output written by tra×30    |

endpoint 探活：local 🟢、laptop-4090 🟢、laptop-5090 🔴、desktop-3090 🟢、mac-m4max 🟢

（babel-pulse 常駐儀器自動快照）

## 2026-07-26T00:38:22+08:00（zh 總數 865）

| 語言 | fresh | stale | missing | 覆蓋率 | Δfresh | Δmissing |
| ---- | ----: | ----: | ------: | -----: | -----: | -------: |
| en   |   721 |   109 |      35 |  96.0% |      · |        · |
| ja   |   712 |   147 |       6 |  99.3% |      · |        · |
| ko   |   709 |   151 |       5 |  99.4% |      · |        · |
| es   |   715 |   146 |       4 |  99.5% |      · |        · |
| fr   |   711 |   151 |       3 |  99.7% |      · |        · |
| vi   |   113 |    17 |     735 |  15.0% |     +1 |       -1 |
| id   |   213 |    11 |     641 |  25.9% |     +1 |       -1 |
| pt   |   341 |    12 |     512 |  40.8% |     +3 |       -3 |
| hi   |   280 |     7 |     578 |  33.2% |     +2 |       -2 |
| ar   |   211 |     1 |     653 |  24.5% |     +2 |       -2 |
| ru   |   236 |     1 |     628 |  27.4% |     +3 |       -3 |

總缺口（stale+missing）：**4553**（▼12 vs 上一筆）

**節點／worker**（ok/fail 為累計；Δ為對上一筆）

| 節點                |  ok | fail | Δok | 平均秒 | 主要 fail                               |
| ------------------- | --: | ---: | --: | -----: | --------------------------------------- |
| fleet:desktop-3090  |  56 |  325 |   · |      — | health×123；verify=1×102                |
| fleet:laptop-4090   |  27 |  137 |   · |      — | health×83；verify=None×24               |
| worker:d3090        |  12 |   29 |   · |  900.2 | no output written by tra×17；verify=4×5 |
| worker:desktop30901 |  21 |   19 |   · |  624.0 | health×10；leak×4                       |
| worker:desktop30902 |  16 |   23 |   · |  613.5 | health×10；verify=1×6                   |
| worker:gemma31      |   1 |   34 |   · |    2.2 | no output written by tra×34             |
| worker:l4090        |  11 |   32 |   · |  848.0 | no output written by tra×18；leak×10    |
| worker:laguna       | 122 |  151 |  +3 |  214.6 | no output written by tra×80；health×23  |
| worker:laptop40901  |  17 |   14 |   · |  874.1 | health×9；leak×2                        |
| worker:laptop40902  |  15 |   15 |   · |  894.2 | leak×6；health×5                        |
| worker:mac          |  83 |  269 |  +1 |  259.0 | leak×152；verify=1×51                   |
| worker:nemo         | 394 |  673 |  +4 |  107.7 | leak×457；health×102                    |
| worker:nemo2        | 351 |  592 |  +1 |  108.6 | leak×416；health×84                     |
| worker:nemo3        | 294 |  420 |  +3 |  100.3 | leak×263；verify=1×58                   |
| worker:oss20        |  67 |  127 |   · |  452.5 | leak×45；no output written by tra×32    |

endpoint 探活：local 🟢、laptop-4090 🟢、laptop-5090 🔴、desktop-3090 🟢、mac-m4max 🟢

（babel-pulse 常駐儀器自動快照）

## 2026-07-26T00:53:51+08:00（zh 總數 865）

| 語言 | fresh | stale | missing | 覆蓋率 | Δfresh | Δmissing |
| ---- | ----: | ----: | ------: | -----: | -----: | -------: |
| en   |   721 |   109 |      35 |  96.0% |      · |        · |
| ja   |   712 |   147 |       6 |  99.3% |      · |        · |
| ko   |   709 |   151 |       5 |  99.4% |      · |        · |
| es   |   715 |   146 |       4 |  99.5% |      · |        · |
| fr   |   712 |   150 |       3 |  99.7% |     +1 |        · |
| vi   |   115 |    17 |     733 |  15.3% |     +2 |       -2 |
| id   |   216 |    11 |     638 |  26.2% |     +3 |       -3 |
| pt   |   344 |    12 |     509 |  41.2% |     +3 |       -3 |
| hi   |   282 |     7 |     576 |  33.4% |     +2 |       -2 |
| ar   |   213 |     1 |     651 |  24.7% |     +2 |       -2 |
| ru   |   240 |     1 |     624 |  27.9% |     +4 |       -4 |

總缺口（stale+missing）：**4536**（▼17 vs 上一筆）

**節點／worker**（ok/fail 為累計；Δ為對上一筆）

| 節點                |  ok | fail | Δok | 平均秒 | 主要 fail                               |
| ------------------- | --: | ---: | --: | -----: | --------------------------------------- |
| fleet:desktop-3090  |  56 |  325 |   · |      — | health×123；verify=1×102                |
| fleet:laptop-4090   |  27 |  137 |   · |      — | health×83；verify=None×24               |
| worker:d3090        |  12 |   29 |   · |  900.2 | no output written by tra×17；verify=4×5 |
| worker:desktop30901 |  21 |   19 |   · |  624.0 | health×10；leak×4                       |
| worker:desktop30902 |  16 |   23 |   · |  613.5 | health×10；verify=1×6                   |
| worker:gemma31      |   1 |   34 |   · |    2.2 | no output written by tra×34             |
| worker:l4090        |  11 |   33 |   · |  848.0 | no output written by tra×18；leak×10    |
| worker:laguna       | 126 |  153 |  +4 |  211.7 | no output written by tra×82；health×23  |
| worker:laptop40901  |  17 |   14 |   · |  874.1 | health×9；leak×2                        |
| worker:laptop40902  |  15 |   15 |   · |  894.2 | leak×6；health×5                        |
| worker:mac          |  85 |  275 |  +2 |  257.1 | leak×153；verify=1×53                   |
| worker:nemo         | 396 |  680 |  +2 |  107.5 | leak×462；health×102                    |
| worker:nemo2        | 355 |  596 |  +4 |  108.4 | leak×418；health×85                     |
| worker:nemo3        | 301 |  421 |  +7 |  101.2 | leak×264；verify=1×58                   |
| worker:oss20        |  68 |  129 |  +1 |  449.5 | leak×47；no output written by tra×32    |

endpoint 探活：local 🟢、laptop-4090 🟢、laptop-5090 🔴、desktop-3090 🟢、mac-m4max 🟢

（babel-pulse 常駐儀器自動快照）

## 2026-07-26T01:09:19+08:00（zh 總數 865）

| 語言 | fresh | stale | missing | 覆蓋率 | Δfresh | Δmissing |
| ---- | ----: | ----: | ------: | -----: | -----: | -------: |
| en   |   721 |   109 |      35 |  96.0% |      · |        · |
| ja   |   712 |   147 |       6 |  99.3% |      · |        · |
| ko   |   710 |   150 |       5 |  99.4% |     +1 |        · |
| es   |   715 |   146 |       4 |  99.5% |      · |        · |
| fr   |   712 |   150 |       3 |  99.7% |      · |        · |
| vi   |   115 |    17 |     733 |  15.3% |      · |        · |
| id   |   218 |    11 |     636 |  26.5% |     +2 |       -2 |
| pt   |   347 |    12 |     506 |  41.5% |     +3 |       -3 |
| hi   |   285 |     7 |     573 |  33.8% |     +3 |       -3 |
| ar   |   216 |     1 |     648 |  25.1% |     +3 |       -3 |
| ru   |   243 |     1 |     621 |  28.2% |     +3 |       -3 |

總缺口（stale+missing）：**4521**（▼15 vs 上一筆）

**節點／worker**（ok/fail 為累計；Δ為對上一筆）

| 節點                |  ok | fail | Δok | 平均秒 | 主要 fail                               |
| ------------------- | --: | ---: | --: | -----: | --------------------------------------- |
| fleet:desktop-3090  |  56 |  325 |   · |      — | health×123；verify=1×102                |
| fleet:laptop-4090   |  27 |  137 |   · |      — | health×83；verify=None×24               |
| worker:d3090        |  12 |   29 |   · |  900.2 | no output written by tra×17；verify=4×5 |
| worker:desktop30901 |  21 |   19 |   · |  624.0 | health×10；leak×4                       |
| worker:desktop30902 |  16 |   23 |   · |  613.5 | health×10；verify=1×6                   |
| worker:gemma31      |   1 |   34 |   · |    2.2 | no output written by tra×34             |
| worker:l4090        |  11 |   34 |   · |  848.0 | no output written by tra×19；leak×10    |
| worker:laguna       | 126 |  155 |   · |  211.7 | no output written by tra×83；health×24  |
| worker:laptop40901  |  17 |   14 |   · |  874.1 | health×9；leak×2                        |
| worker:laptop40902  |  15 |   15 |   · |  894.2 | leak×6；health×5                        |
| worker:mac          |  88 |  280 |  +3 |  252.1 | leak×153；verify=1×54                   |
| worker:nemo         | 400 |  684 |  +4 |  107.6 | leak×465；health×103                    |
| worker:nemo2        | 357 |  600 |  +2 |  108.5 | leak×421；health×85                     |
| worker:nemo3        | 306 |  425 |  +5 |  100.7 | leak×267；verify=1×58                   |
| worker:oss20        |  69 |  130 |  +1 |  449.9 | leak×48；no output written by tra×32    |

endpoint 探活：local 🟢、laptop-4090 🟢、laptop-5090 🔴、desktop-3090 🟢、mac-m4max 🟢

（babel-pulse 常駐儀器自動快照）

## 2026-07-26T01:55:39+08:00（zh 總數 865）

| 語言 | fresh | stale | missing | 覆蓋率 | Δfresh | Δmissing |
| ---- | ----: | ----: | ------: | -----: | -----: | -------: |
| en   |   721 |   109 |      35 |  96.0% |      · |        · |
| ja   |   713 |   146 |       6 |  99.3% |     +1 |        · |
| ko   |   710 |   150 |       5 |  99.4% |      · |        · |
| es   |   716 |   145 |       4 |  99.5% |     +1 |        · |
| fr   |   713 |   149 |       3 |  99.7% |     +1 |        · |
| vi   |   116 |    17 |     732 |  15.4% |     +1 |       -1 |
| id   |   223 |    11 |     631 |  27.1% |     +5 |       -5 |
| pt   |   353 |    12 |     500 |  42.2% |     +6 |       -6 |
| hi   |   287 |     7 |     571 |  34.0% |     +2 |       -2 |
| ar   |   221 |     1 |     643 |  25.7% |     +5 |       -5 |
| ru   |   248 |     1 |     616 |  28.8% |     +5 |       -5 |

總缺口（stale+missing）：**4494**（▼27 vs 上一筆）

**節點／worker**（ok/fail 為累計；Δ為對上一筆）

| 節點                |  ok | fail | Δok | 平均秒 | 主要 fail                              |
| ------------------- | --: | ---: | --: | -----: | -------------------------------------- |
| fleet:desktop-3090  |  56 |  325 |   · |      — | health×123；verify=1×102               |
| fleet:laptop-4090   |  27 |  137 |   · |      — | health×83；verify=None×24              |
| worker:d3090        |  12 |   33 |   · |  900.2 | no output written by tra×20；leak×5    |
| worker:desktop30901 |  21 |   19 |   · |  624.0 | health×10；leak×4                      |
| worker:desktop30902 |  16 |   23 |   · |  613.5 | health×10；verify=1×6                  |
| worker:gemma31      |   1 |   34 |   · |    2.2 | no output written by tra×34            |
| worker:l4090        |  11 |   37 |   · |  848.0 | no output written by tra×19；leak×10   |
| worker:laguna       | 128 |  160 |  +2 |  211.4 | no output written by tra×87；health×24 |
| worker:laptop40901  |  17 |   14 |   · |  874.1 | health×9；leak×2                       |
| worker:laptop40902  |  15 |   15 |   · |  894.2 | leak×6；health×5                       |
| worker:mac          |  95 |  293 |  +7 |  241.7 | leak×156；verify=1×55                  |
| worker:nemo         | 408 |  700 |  +8 |  108.1 | leak×472；health×109                   |
| worker:nemo2        | 363 |  616 |  +6 |  108.5 | leak×432；health×87                    |
| worker:nemo3        | 314 |  441 |  +8 |  101.0 | leak×280；verify=1×60                  |
| worker:oss20        |  69 |  137 |   · |  449.9 | leak×51；no output written by tra×33   |

endpoint 探活：local 🟢、laptop-4090 🟢、laptop-5090 🔴、desktop-3090 🟢、mac-m4max 🟢

（babel-pulse 常駐儀器自動快照）

## 2026-07-26T02:11:06+08:00（zh 總數 865）

| 語言 | fresh | stale | missing | 覆蓋率 | Δfresh | Δmissing |
| ---- | ----: | ----: | ------: | -----: | -----: | -------: |
| en   |   721 |   109 |      35 |  96.0% |      · |        · |
| ja   |   714 |   145 |       6 |  99.3% |     +1 |        · |
| ko   |   711 |   149 |       5 |  99.4% |     +1 |        · |
| es   |   716 |   145 |       4 |  99.5% |      · |        · |
| fr   |   713 |   149 |       3 |  99.7% |      · |        · |
| vi   |   118 |    17 |     730 |  15.6% |     +2 |       -2 |
| id   |   223 |    11 |     631 |  27.1% |      · |        · |
| pt   |   357 |    12 |     496 |  42.7% |     +4 |       -4 |
| hi   |   287 |     7 |     571 |  34.0% |      · |        · |
| ar   |   221 |     1 |     643 |  25.7% |      · |        · |
| ru   |   249 |     1 |     615 |  28.9% |     +1 |       -1 |

總缺口（stale+missing）：**4485**（▼9 vs 上一筆）

**節點／worker**（ok/fail 為累計；Δ為對上一筆）

| 節點                |  ok | fail | Δok | 平均秒 | 主要 fail                              |
| ------------------- | --: | ---: | --: | -----: | -------------------------------------- |
| fleet:desktop-3090  |  56 |  325 |   · |      — | health×123；verify=1×102               |
| fleet:laptop-4090   |  27 |  137 |   · |      — | health×83；verify=None×24              |
| worker:d3090        |  12 |   33 |   · |  900.2 | no output written by tra×20；leak×5    |
| worker:desktop30901 |  21 |   19 |   · |  624.0 | health×10；leak×4                      |
| worker:desktop30902 |  16 |   23 |   · |  613.5 | health×10；verify=1×6                  |
| worker:gemma31      |   1 |   34 |   · |    2.2 | no output written by tra×34            |
| worker:l4090        |  11 |   38 |   · |  848.0 | no output written by tra×19；leak×10   |
| worker:laguna       | 129 |  161 |  +1 |  211.6 | no output written by tra×88；health×24 |
| worker:laptop40901  |  17 |   14 |   · |  874.1 | health×9；leak×2                       |
| worker:laptop40902  |  15 |   15 |   · |  894.2 | leak×6；health×5                       |
| worker:mac          |  99 |  299 |  +4 |  235.2 | leak×159；verify=1×55                  |
| worker:nemo         | 408 |  703 |   · |  108.1 | leak×473；health×111                   |
| worker:nemo2        | 364 |  620 |  +1 |  108.4 | leak×436；health×87                    |
| worker:nemo3        | 317 |  443 |  +3 |  101.0 | leak×281；verify=1×60                  |
| worker:oss20        |  69 |  138 |   · |  449.9 | leak×51；no output written by tra×34   |

endpoint 探活：local 🟢、laptop-4090 🟢、laptop-5090 🔴、desktop-3090 🟢、mac-m4max 🟢

（babel-pulse 常駐儀器自動快照）

## 2026-07-26T02:26:35+08:00（zh 總數 865）

| 語言 | fresh | stale | missing | 覆蓋率 | Δfresh | Δmissing |
| ---- | ----: | ----: | ------: | -----: | -----: | -------: |
| en   |   721 |   109 |      35 |  96.0% |      · |        · |
| ja   |   715 |   144 |       6 |  99.3% |     +1 |        · |
| ko   |   713 |   147 |       5 |  99.4% |     +2 |        · |
| es   |   717 |   145 |       3 |  99.7% |     +1 |       -1 |
| fr   |   713 |   149 |       3 |  99.7% |      · |        · |
| vi   |   119 |    17 |     729 |  15.7% |     +1 |       -1 |
| id   |   223 |    11 |     631 |  27.1% |      · |        · |
| pt   |   362 |    12 |     491 |  43.2% |     +5 |       -5 |
| hi   |   287 |     7 |     571 |  34.0% |      · |        · |
| ar   |   223 |     1 |     641 |  25.9% |     +2 |       -2 |
| ru   |   252 |     1 |     612 |  29.2% |     +3 |       -3 |

總缺口（stale+missing）：**4470**（▼15 vs 上一筆）

**節點／worker**（ok/fail 為累計；Δ為對上一筆）

| 節點                |  ok | fail | Δok | 平均秒 | 主要 fail                              |
| ------------------- | --: | ---: | --: | -----: | -------------------------------------- |
| fleet:desktop-3090  |  56 |  325 |   · |      — | health×123；verify=1×102               |
| fleet:laptop-4090   |  27 |  137 |   · |      — | health×83；verify=None×24              |
| worker:d3090        |  12 |   33 |   · |  900.2 | no output written by tra×20；leak×5    |
| worker:desktop30901 |  21 |   19 |   · |  624.0 | health×10；leak×4                      |
| worker:desktop30902 |  16 |   23 |   · |  613.5 | health×10；verify=1×6                  |
| worker:gemma31      |   1 |   34 |   · |    2.2 | no output written by tra×34            |
| worker:l4090        |  11 |   39 |   · |  848.0 | no output written by tra×19；leak×10   |
| worker:laguna       | 129 |  162 |   · |  211.6 | no output written by tra×89；health×24 |
| worker:laptop40901  |  17 |   14 |   · |  874.1 | health×9；leak×2                       |
| worker:laptop40902  |  15 |   15 |   · |  894.2 | leak×6；health×5                       |
| worker:mac          | 105 |  302 |  +6 |  226.7 | leak×160；verify=1×56                  |
| worker:nemo         | 414 |  705 |  +6 |  107.9 | leak×475；health×111                   |
| worker:nemo2        | 367 |  623 |  +3 |  109.1 | leak×439；health×87                    |
| worker:nemo3        | 318 |  451 |  +1 |  101.2 | leak×287；verify=1×61                  |
| worker:oss20        |  69 |  139 |   · |  449.9 | leak×52；no output written by tra×34   |

endpoint 探活：local 🟢、laptop-4090 🟢、laptop-5090 🔴、desktop-3090 🟢、mac-m4max 🟢

（babel-pulse 常駐儀器自動快照）

## 2026-07-26T02:41:58+08:00（zh 總數 865）

| 語言 | fresh | stale | missing | 覆蓋率 | Δfresh | Δmissing |
| ---- | ----: | ----: | ------: | -----: | -----: | -------: |
| en   |   721 |   109 |      35 |  96.0% |      · |        · |
| ja   |   715 |   144 |       6 |  99.3% |      · |        · |
| ko   |   713 |   147 |       5 |  99.4% |      · |        · |
| es   |   717 |   145 |       3 |  99.7% |      · |        · |
| fr   |   714 |   148 |       3 |  99.7% |     +1 |        · |
| vi   |   120 |    17 |     728 |  15.8% |     +1 |       -1 |
| id   |   225 |    11 |     629 |  27.3% |     +2 |       -2 |
| pt   |   366 |    12 |     487 |  43.7% |     +4 |       -4 |
| hi   |   289 |     7 |     569 |  34.2% |     +2 |       -2 |
| ar   |   226 |     1 |     638 |  26.2% |     +3 |       -3 |
| ru   |   257 |     1 |     607 |  29.8% |     +5 |       -5 |

總缺口（stale+missing）：**4452**（▼18 vs 上一筆）

**節點／worker**（ok/fail 為累計；Δ為對上一筆）

| 節點                |  ok | fail | Δok | 平均秒 | 主要 fail                              |
| ------------------- | --: | ---: | --: | -----: | -------------------------------------- |
| fleet:desktop-3090  |  56 |  325 |   · |      — | health×123；verify=1×102               |
| fleet:laptop-4090   |  27 |  137 |   · |      — | health×83；verify=None×24              |
| worker:d3090        |  12 |   34 |   · |  900.2 | no output written by tra×21；leak×5    |
| worker:desktop30901 |  21 |   19 |   · |  624.0 | health×10；leak×4                      |
| worker:desktop30902 |  16 |   23 |   · |  613.5 | health×10；verify=1×6                  |
| worker:gemma31      |   1 |   34 |   · |    2.2 | no output written by tra×34            |
| worker:l4090        |  11 |   40 |   · |  848.0 | no output written by tra×20；leak×10   |
| worker:laguna       | 130 |  164 |  +1 |  212.0 | no output written by tra×90；health×24 |
| worker:laptop40901  |  17 |   14 |   · |  874.1 | health×9；leak×2                       |
| worker:laptop40902  |  15 |   15 |   · |  894.2 | leak×6；health×5                       |
| worker:mac          | 109 |  306 |  +4 |  221.2 | leak×161；verify=1×57                  |
| worker:nemo         | 419 |  708 |  +5 |  107.8 | leak×478；health×111                   |
| worker:nemo2        | 370 |  629 |  +3 |  108.8 | leak×443；health×88                    |
| worker:nemo3        | 324 |  454 |  +6 |  101.1 | leak×289；verify=1×61                  |
| worker:oss20        |  69 |  141 |   · |  449.9 | leak×53；no output written by tra×34   |

endpoint 探活：local 🟢、laptop-4090 🟢、laptop-5090 🔴、desktop-3090 🟢、mac-m4max 🟢

（babel-pulse 常駐儀器自動快照）

## 2026-07-26T02:54:35+08:00（zh 總數 865）

| 語言 | fresh | stale | missing | 覆蓋率 | Δfresh | Δmissing |
| ---- | ----: | ----: | ------: | -----: | -----: | -------: |
| en   |   721 |   109 |      35 |  96.0% |      · |        · |
| ja   |   716 |   143 |       6 |  99.3% |     +1 |        · |
| ko   |   713 |   147 |       5 |  99.4% |      · |        · |
| es   |   717 |   145 |       3 |  99.7% |      · |        · |
| fr   |   714 |   148 |       3 |  99.7% |      · |        · |
| vi   |   121 |    17 |     727 |  16.0% |     +1 |       -1 |
| id   |   227 |    11 |     627 |  27.5% |     +2 |       -2 |
| pt   |   372 |    12 |     481 |  44.4% |     +6 |       -6 |
| hi   |   291 |     7 |     567 |  34.5% |     +2 |       -2 |
| ar   |   228 |     1 |     636 |  26.5% |     +2 |       -2 |
| ru   |   258 |     1 |     606 |  29.9% |     +1 |       -1 |

總缺口（stale+missing）：**4437**（▼15 vs 上一筆）

**節點／worker**（ok/fail 為累計；Δ為對上一筆）

| 節點                |  ok | fail | Δok | 平均秒 | 主要 fail                              |
| ------------------- | --: | ---: | --: | -----: | -------------------------------------- |
| fleet:desktop-3090  |  56 |  325 |   · |      — | health×123；verify=1×102               |
| fleet:laptop-4090   |  27 |  137 |   · |      — | health×83；verify=None×24              |
| worker:d3090        |  12 |   34 |   · |  900.2 | no output written by tra×21；leak×5    |
| worker:desktop30901 |  21 |   19 |   · |  624.0 | health×10；leak×4                      |
| worker:desktop30902 |  16 |   23 |   · |  613.5 | health×10；verify=1×6                  |
| worker:gemma31      |   1 |   34 |   · |    2.2 | no output written by tra×34            |
| worker:l4090        |  12 |   40 |  +1 |  852.4 | no output written by tra×20；leak×10   |
| worker:laguna       | 130 |  165 |   · |  212.0 | no output written by tra×90；health×24 |
| worker:laptop40901  |  17 |   14 |   · |  874.1 | health×9；leak×2                       |
| worker:laptop40902  |  15 |   15 |   · |  894.2 | leak×6；health×5                       |
| worker:mac          | 116 |  309 |  +7 |  211.8 | leak×162；verify=1×57                  |
| worker:nemo         | 422 |  714 |  +3 |  107.7 | leak×483；health×111                   |
| worker:nemo2        | 373 |  633 |  +3 |  108.7 | leak×445；health×89                    |
| worker:nemo3        | 328 |  459 |  +4 |  100.9 | leak×294；verify=1×61                  |
| worker:oss20        |  69 |  142 |   · |  449.9 | leak×54；no output written by tra×34   |

endpoint 探活：local 🟢、laptop-4090 🟢、laptop-5090 🔴、desktop-3090 🟢、mac-m4max 🟢

（babel-pulse 常駐儀器自動快照）

## 2026-07-26T02:57:21+08:00（zh 總數 865）

| 語言 | fresh | stale | missing | 覆蓋率 | Δfresh | Δmissing |
| ---- | ----: | ----: | ------: | -----: | -----: | -------: |
| en   |   721 |   109 |      35 |  96.0% |      · |        · |
| ja   |   716 |   143 |       6 |  99.3% |      · |        · |
| ko   |   714 |   146 |       5 |  99.4% |     +1 |        · |
| es   |   717 |   145 |       3 |  99.7% |      · |        · |
| fr   |   715 |   147 |       3 |  99.7% |     +1 |        · |
| vi   |   121 |    17 |     727 |  16.0% |      · |        · |
| id   |   228 |    11 |     626 |  27.6% |     +1 |       -1 |
| pt   |   372 |    12 |     481 |  44.4% |      · |        · |
| hi   |   292 |     7 |     566 |  34.6% |     +1 |       -1 |
| ar   |   228 |     1 |     636 |  26.5% |      · |        · |
| ru   |   258 |     1 |     606 |  29.9% |      · |        · |

總缺口（stale+missing）：**4433**（▼4 vs 上一筆）

**節點／worker**（ok/fail 為累計；Δ為對上一筆）

| 節點                |  ok | fail | Δok | 平均秒 | 主要 fail                              |
| ------------------- | --: | ---: | --: | -----: | -------------------------------------- |
| fleet:desktop-3090  |  56 |  325 |   · |      — | health×123；verify=1×102               |
| fleet:laptop-4090   |  27 |  137 |   · |      — | health×83；verify=None×24              |
| worker:d3090        |  12 |   35 |   · |  900.2 | no output written by tra×22；leak×5    |
| worker:desktop30901 |  21 |   19 |   · |  624.0 | health×10；leak×4                      |
| worker:desktop30902 |  16 |   23 |   · |  613.5 | health×10；verify=1×6                  |
| worker:gemma31      |   1 |   34 |   · |    2.2 | no output written by tra×34            |
| worker:l4090        |  12 |   40 |   · |  852.4 | no output written by tra×20；leak×10   |
| worker:laguna       | 131 |  165 |  +1 |  212.3 | no output written by tra×90；health×24 |
| worker:laptop40901  |  17 |   14 |   · |  874.1 | health×9；leak×2                       |
| worker:laptop40902  |  15 |   15 |   · |  894.2 | leak×6；health×5                       |
| worker:mac          | 118 |  309 |  +2 |  209.8 | leak×162；verify=1×57                  |
| worker:nemo         | 422 |  715 |   · |  107.7 | leak×484；health×111                   |
| worker:nemo2        | 373 |  635 |   · |  108.7 | leak×445；health×89                    |
| worker:nemo3        | 329 |  461 |  +1 |  100.7 | leak×296；verify=1×61                  |
| worker:oss20        |  69 |  143 |   · |  449.9 | leak×55；no output written by tra×34   |

endpoint 探活：local 🟢、laptop-4090 🟢、laptop-5090 🔴、desktop-3090 🟢、mac-m4max 🟢

（babel-pulse 常駐儀器自動快照）

## 2026-07-26T03:12:44+08:00（zh 總數 865）

| 語言 | fresh | stale | missing | 覆蓋率 | Δfresh | Δmissing |
| ---- | ----: | ----: | ------: | -----: | -----: | -------: |
| en   |   721 |   109 |      35 |  96.0% |      · |        · |
| ja   |   716 |   143 |       6 |  99.3% |      · |        · |
| ko   |   715 |   145 |       5 |  99.4% |     +1 |        · |
| es   |   717 |   145 |       3 |  99.7% |      · |        · |
| fr   |   716 |   146 |       3 |  99.7% |     +1 |        · |
| vi   |   123 |    17 |     725 |  16.2% |     +2 |       -2 |
| id   |   230 |    11 |     624 |  27.9% |     +2 |       -2 |
| pt   |   375 |    12 |     478 |  44.7% |     +3 |       -3 |
| hi   |   293 |     7 |     565 |  34.7% |     +1 |       -1 |
| ar   |   229 |     1 |     635 |  26.6% |     +1 |       -1 |
| ru   |   260 |     1 |     604 |  30.2% |     +2 |       -2 |

總缺口（stale+missing）：**4420**（▼13 vs 上一筆）

**節點／worker**（ok/fail 為累計；Δ為對上一筆）

| 節點                |  ok | fail | Δok | 平均秒 | 主要 fail                              |
| ------------------- | --: | ---: | --: | -----: | -------------------------------------- |
| fleet:desktop-3090  |  56 |  325 |   · |      — | health×123；verify=1×102               |
| fleet:laptop-4090   |  27 |  137 |   · |      — | health×83；verify=None×24              |
| worker:d3090        |  12 |   36 |   · |  900.2 | no output written by tra×22；leak×5    |
| worker:desktop30901 |  21 |   19 |   · |  624.0 | health×10；leak×4                      |
| worker:desktop30902 |  16 |   23 |   · |  613.5 | health×10；verify=1×6                  |
| worker:gemma31      |   1 |   34 |   · |    2.2 | no output written by tra×34            |
| worker:l4090        |  13 |   40 |  +1 |  856.0 | no output written by tra×20；leak×10   |
| worker:laguna       | 131 |  166 |   · |  212.3 | no output written by tra×91；health×24 |
| worker:laptop40901  |  17 |   14 |   · |  874.1 | health×9；leak×2                       |
| worker:laptop40902  |  15 |   15 |   · |  894.2 | leak×6；health×5                       |
| worker:mac          | 126 |  316 |  +8 |  200.0 | leak×163；verify=1×57                  |
| worker:nemo         | 424 |  720 |  +2 |  107.5 | leak×488；health×112                   |
| worker:nemo2        | 374 |  641 |  +1 |  108.8 | leak×448；health×92                    |
| worker:nemo3        | 331 |  465 |  +2 |  100.7 | leak×298；verify=1×61                  |
| worker:oss20        |  69 |  147 |   · |  449.9 | leak×56；no output written by tra×37   |

endpoint 探活：local 🟢、laptop-4090 🟢、laptop-5090 🔴、desktop-3090 🟢、mac-m4max 🟢

（babel-pulse 常駐儀器自動快照）

## 2026-07-26T03:28:13+08:00（zh 總數 865）

| 語言 | fresh | stale | missing | 覆蓋率 | Δfresh | Δmissing |
| ---- | ----: | ----: | ------: | -----: | -----: | -------: |
| en   |   721 |   109 |      35 |  96.0% |      · |        · |
| ja   |   717 |   142 |       6 |  99.3% |     +1 |        · |
| ko   |   715 |   145 |       5 |  99.4% |      · |        · |
| es   |   717 |   145 |       3 |  99.7% |      · |        · |
| fr   |   716 |   146 |       3 |  99.7% |      · |        · |
| vi   |   123 |    17 |     725 |  16.2% |      · |        · |
| id   |   230 |    11 |     624 |  27.9% |      · |        · |
| pt   |   379 |    12 |     474 |  45.2% |     +4 |       -4 |
| hi   |   294 |     7 |     564 |  34.8% |     +1 |       -1 |
| ar   |   231 |     1 |     633 |  26.8% |     +2 |       -2 |
| ru   |   262 |     1 |     602 |  30.4% |     +2 |       -2 |

總缺口（stale+missing）：**4410**（▼10 vs 上一筆）

**節點／worker**（ok/fail 為累計；Δ為對上一筆）

| 節點                |  ok | fail | Δok | 平均秒 | 主要 fail                              |
| ------------------- | --: | ---: | --: | -----: | -------------------------------------- |
| fleet:desktop-3090  |  56 |  325 |   · |      — | health×123；verify=1×102               |
| fleet:laptop-4090   |  27 |  137 |   · |      — | health×83；verify=None×24              |
| worker:d3090        |  12 |   37 |   · |  900.2 | no output written by tra×23；leak×5    |
| worker:desktop30901 |  21 |   19 |   · |  624.0 | health×10；leak×4                      |
| worker:desktop30902 |  16 |   23 |   · |  613.5 | health×10；verify=1×6                  |
| worker:gemma31      |   1 |   34 |   · |    2.2 | no output written by tra×34            |
| worker:l4090        |  13 |   41 |   · |  856.0 | no output written by tra×20；leak×10   |
| worker:laguna       | 131 |  168 |   · |  212.3 | no output written by tra×93；health×24 |
| worker:laptop40901  |  17 |   14 |   · |  874.1 | health×9；leak×2                       |
| worker:laptop40902  |  15 |   15 |   · |  894.2 | leak×6；health×5                       |
| worker:mac          | 129 |  327 |  +3 |  196.2 | leak×164；verify=1×58                  |
| worker:nemo         | 426 |  728 |  +2 |  107.4 | leak×492；health×114                   |
| worker:nemo2        | 379 |  646 |  +5 |  108.5 | leak×453；health×92                    |
| worker:nemo3        | 333 |  467 |  +2 |  101.2 | leak×300；verify=1×61                  |
| worker:oss20        |  69 |  147 |   · |  449.9 | leak×56；no output written by tra×37   |

endpoint 探活：local 🟢、laptop-4090 🟢、laptop-5090 🔴、desktop-3090 🟢、mac-m4max 🟢

（babel-pulse 常駐儀器自動快照）

## 2026-07-26T03:43:33+08:00（zh 總數 865）

| 語言 | fresh | stale | missing | 覆蓋率 | Δfresh | Δmissing |
| ---- | ----: | ----: | ------: | -----: | -----: | -------: |
| en   |   721 |   109 |      35 |  96.0% |      · |        · |
| ja   |   717 |   142 |       6 |  99.3% |      · |        · |
| ko   |   715 |   145 |       5 |  99.4% |      · |        · |
| es   |   717 |   145 |       3 |  99.7% |      · |        · |
| fr   |   716 |   146 |       3 |  99.7% |      · |        · |
| vi   |   123 |    17 |     725 |  16.2% |      · |        · |
| id   |   231 |    11 |     623 |  28.0% |     +1 |       -1 |
| pt   |   381 |    12 |     472 |  45.4% |     +2 |       -2 |
| hi   |   295 |     7 |     563 |  34.9% |     +1 |       -1 |
| ar   |   233 |     1 |     631 |  27.1% |     +2 |       -2 |
| ru   |   263 |     1 |     601 |  30.5% |     +1 |       -1 |

總缺口（stale+missing）：**4403**（▼7 vs 上一筆）

**節點／worker**（ok/fail 為累計；Δ為對上一筆）

| 節點                |  ok | fail | Δok | 平均秒 | 主要 fail                              |
| ------------------- | --: | ---: | --: | -----: | -------------------------------------- |
| fleet:desktop-3090  |  56 |  325 |   · |      — | health×123；verify=1×102               |
| fleet:laptop-4090   |  27 |  137 |   · |      — | health×83；verify=None×24              |
| worker:d3090        |  13 |   37 |  +1 |  900.2 | no output written by tra×23；leak×5    |
| worker:desktop30901 |  21 |   19 |   · |  624.0 | health×10；leak×4                      |
| worker:desktop30902 |  16 |   23 |   · |  613.5 | health×10；verify=1×6                  |
| worker:gemma31      |   1 |   34 |   · |    2.2 | no output written by tra×34            |
| worker:l4090        |  16 |   44 |  +3 |  753.0 | no output written by tra×23；leak×10   |
| worker:laguna       | 131 |  168 |   · |  212.3 | no output written by tra×93；health×24 |
| worker:laptop40901  |  17 |   14 |   · |  874.1 | health×9；leak×2                       |
| worker:laptop40902  |  15 |   15 |   · |  894.2 | leak×6；health×5                       |
| worker:mac          | 132 |  330 |  +3 |  192.8 | leak×164；health×60                    |
| worker:nemo         | 429 |  735 |  +3 |  107.4 | leak×498；health×114                   |
| worker:nemo2        | 382 |  652 |  +3 |  108.4 | leak×458；health×93                    |
| worker:nemo3        | 334 |  475 |  +1 |  101.2 | leak×302；health×67                    |
| worker:oss20        |  69 |  147 |   · |  449.9 | leak×56；no output written by tra×37   |

endpoint 探活：local 🟢、laptop-4090 🔴、laptop-5090 🔴、desktop-3090 🟢、mac-m4max 🟢

（babel-pulse 常駐儀器自動快照）

## 2026-07-26T03:56:32+08:00（zh 總數 865）

| 語言 | fresh | stale | missing | 覆蓋率 | Δfresh | Δmissing |
| ---- | ----: | ----: | ------: | -----: | -----: | -------: |
| en   |   721 |   109 |      35 |  96.0% |      · |        · |
| ja   |   717 |   142 |       6 |  99.3% |      · |        · |
| ko   |   715 |   145 |       5 |  99.4% |      · |        · |
| es   |   718 |   144 |       3 |  99.7% |     +1 |        · |
| fr   |   717 |   145 |       3 |  99.7% |     +1 |        · |
| vi   |   123 |    17 |     725 |  16.2% |      · |        · |
| id   |   231 |    11 |     623 |  28.0% |      · |        · |
| pt   |   381 |    12 |     472 |  45.4% |      · |        · |
| hi   |   295 |     7 |     563 |  34.9% |      · |        · |
| ar   |   233 |     1 |     631 |  27.1% |      · |        · |
| ru   |   265 |     1 |     599 |  30.8% |     +2 |       -2 |

總缺口（stale+missing）：**4399**（▼4 vs 上一筆）

**節點／worker**（ok/fail 為累計；Δ為對上一筆）

| 節點                |  ok | fail | Δok | 平均秒 | 主要 fail                              |
| ------------------- | --: | ---: | --: | -----: | -------------------------------------- |
| fleet:desktop-3090  |  56 |  325 |   · |      — | health×123；verify=1×102               |
| fleet:laptop-4090   |  27 |  137 |   · |      — | health×83；verify=None×24              |
| worker:d3090        |  13 |   38 |   · |  900.2 | no output written by tra×23；leak×6    |
| worker:desktop30901 |  21 |   19 |   · |  624.0 | health×10；leak×4                      |
| worker:desktop30902 |  16 |   23 |   · |  613.5 | health×10；verify=1×6                  |
| worker:gemma31      |   1 |   34 |   · |    2.2 | no output written by tra×34            |
| worker:l4090        |  16 |   44 |   · |  753.0 | no output written by tra×23；leak×10   |
| worker:laguna       | 131 |  168 |   · |  212.3 | no output written by tra×93；health×24 |
| worker:laptop40901  |  17 |   14 |   · |  874.1 | health×9；leak×2                       |
| worker:laptop40902  |  15 |   15 |   · |  894.2 | leak×6；health×5                       |
| worker:mac          | 135 |  330 |  +3 |  195.1 | leak×164；health×60                    |
| worker:nemo         | 430 |  739 |  +1 |  107.3 | leak×502；health×114                   |
| worker:nemo2        | 382 |  658 |   · |  108.4 | leak×461；health×93                    |
| worker:nemo3        | 334 |  478 |   · |  101.2 | leak×304；health×68                    |
| worker:oss20        |  70 |  148 |  +1 |  448.3 | leak×57；no output written by tra×37   |

endpoint 探活：local 🟢、laptop-4090 🔴、laptop-5090 🔴、desktop-3090 🟢、mac-m4max 🟢

（babel-pulse 常駐儀器自動快照）

## 2026-07-26T03:59:06+08:00（zh 總數 865）

| 語言 | fresh | stale | missing | 覆蓋率 | Δfresh | Δmissing |
| ---- | ----: | ----: | ------: | -----: | -----: | -------: |
| en   |   721 |   109 |      35 |  96.0% |      · |        · |
| ja   |   717 |   142 |       6 |  99.3% |      · |        · |
| ko   |   715 |   145 |       5 |  99.4% |      · |        · |
| es   |   718 |   144 |       3 |  99.7% |      · |        · |
| fr   |   717 |   145 |       3 |  99.7% |      · |        · |
| vi   |   123 |    17 |     725 |  16.2% |      · |        · |
| id   |   231 |    11 |     623 |  28.0% |      · |        · |
| pt   |   381 |    12 |     472 |  45.4% |      · |        · |
| hi   |   296 |     7 |     562 |  35.0% |     +1 |       -1 |
| ar   |   233 |     1 |     631 |  27.1% |      · |        · |
| ru   |   265 |     1 |     599 |  30.8% |      · |        · |

總缺口（stale+missing）：**4398**（▼1 vs 上一筆）

**節點／worker**（ok/fail 為累計；Δ為對上一筆）

| 節點                |  ok | fail | Δok | 平均秒 | 主要 fail                              |
| ------------------- | --: | ---: | --: | -----: | -------------------------------------- |
| fleet:desktop-3090  |  56 |  325 |   · |      — | health×123；verify=1×102               |
| fleet:laptop-4090   |  27 |  137 |   · |      — | health×83；verify=None×24              |
| worker:d3090        |  13 |   38 |   · |  900.2 | no output written by tra×23；leak×6    |
| worker:desktop30901 |  21 |   19 |   · |  624.0 | health×10；leak×4                      |
| worker:desktop30902 |  16 |   23 |   · |  613.5 | health×10；verify=1×6                  |
| worker:gemma31      |   1 |   34 |   · |    2.2 | no output written by tra×34            |
| worker:l4090        |  16 |   44 |   · |  753.0 | no output written by tra×23；leak×10   |
| worker:laguna       | 131 |  168 |   · |  212.3 | no output written by tra×93；health×24 |
| worker:laptop40901  |  17 |   14 |   · |  874.1 | health×9；leak×2                       |
| worker:laptop40902  |  15 |   15 |   · |  894.2 | leak×6；health×5                       |
| worker:mac          | 135 |  330 |   · |  195.1 | leak×164；health×60                    |
| worker:nemo         | 430 |  739 |   · |  107.3 | leak×502；health×114                   |
| worker:nemo2        | 382 |  658 |   · |  108.4 | leak×461；health×93                    |
| worker:nemo3        | 334 |  479 |   · |  101.2 | leak×304；health×69                    |
| worker:oss20        |  71 |  148 |  +1 |  446.7 | leak×57；no output written by tra×37   |

endpoint 探活：local 🟢、laptop-4090 🔴、laptop-5090 🔴、desktop-3090 🟢、mac-m4max 🟢

（babel-pulse 常駐儀器自動快照）

## 2026-07-26T04:14:35+08:00（zh 總數 865）

| 語言 | fresh | stale | missing | 覆蓋率 | Δfresh | Δmissing |
| ---- | ----: | ----: | ------: | -----: | -----: | -------: |
| en   |   721 |   109 |      35 |  96.0% |      · |        · |
| ja   |   717 |   142 |       6 |  99.3% |      · |        · |
| ko   |   715 |   145 |       5 |  99.4% |      · |        · |
| es   |   718 |   144 |       3 |  99.7% |      · |        · |
| fr   |   718 |   144 |       3 |  99.7% |     +1 |        · |
| vi   |   125 |    17 |     723 |  16.4% |     +2 |       -2 |
| id   |   235 |    11 |     619 |  28.4% |     +4 |       -4 |
| pt   |   385 |    12 |     468 |  45.9% |     +4 |       -4 |
| hi   |   300 |     7 |     558 |  35.5% |     +4 |       -4 |
| ar   |   237 |     1 |     627 |  27.5% |     +4 |       -4 |
| ru   |   268 |     1 |     596 |  31.1% |     +3 |       -3 |

總缺口（stale+missing）：**4376**（▼22 vs 上一筆）

**節點／worker**（ok/fail 為累計；Δ為對上一筆）

| 節點                |  ok | fail | Δok | 平均秒 | 主要 fail                              |
| ------------------- | --: | ---: | --: | -----: | -------------------------------------- |
| fleet:desktop-3090  |  56 |  325 |   · |      — | health×123；verify=1×102               |
| fleet:laptop-4090   |  27 |  137 |   · |      — | health×83；verify=None×24              |
| worker:d3090        |  13 |   39 |   · |  900.2 | no output written by tra×24；leak×6    |
| worker:desktop30901 |  21 |   19 |   · |  624.0 | health×10；leak×4                      |
| worker:desktop30902 |  16 |   23 |   · |  613.5 | health×10；verify=1×6                  |
| worker:gemma31      |   1 |   34 |   · |    2.2 | no output written by tra×34            |
| worker:l4090        |  16 |   47 |   · |  753.0 | no output written by tra×26；leak×10   |
| worker:laguna       | 132 |  169 |  +1 |  213.1 | no output written by tra×94；health×24 |
| worker:laptop40901  |  17 |   14 |   · |  874.1 | health×9；leak×2                       |
| worker:laptop40902  |  15 |   15 |   · |  894.2 | leak×6；health×5                       |
| worker:mac          | 137 |  331 |  +2 |  196.1 | leak×164；health×60                    |
| worker:nemo         | 437 |  743 |  +7 |  106.7 | leak×506；health×114                   |
| worker:nemo2        | 388 |  659 |  +6 |  108.7 | leak×461；health×93                    |
| worker:nemo3        | 341 |  482 |  +7 |  101.0 | leak×307；health×69                    |
| worker:oss20        |  72 |  149 |  +1 |  445.0 | leak×57；no output written by tra×38   |

endpoint 探活：local 🟢、laptop-4090 🔴、laptop-5090 🔴、desktop-3090 🟢、mac-m4max 🟢

（babel-pulse 常駐儀器自動快照）

## 2026-07-26T04:30:01+08:00（zh 總數 865）

| 語言 | fresh | stale | missing | 覆蓋率 | Δfresh | Δmissing |
| ---- | ----: | ----: | ------: | -----: | -----: | -------: |
| en   |   721 |   109 |      35 |  96.0% |      · |        · |
| ja   |   717 |   142 |       6 |  99.3% |      · |        · |
| ko   |   715 |   145 |       5 |  99.4% |      · |        · |
| es   |   718 |   144 |       3 |  99.7% |      · |        · |
| fr   |   719 |   143 |       3 |  99.7% |     +1 |        · |
| vi   |   125 |    17 |     723 |  16.4% |      · |        · |
| id   |   237 |    11 |     617 |  28.7% |     +2 |       -2 |
| pt   |   392 |    12 |     461 |  46.7% |     +7 |       -7 |
| hi   |   305 |     7 |     553 |  36.1% |     +5 |       -5 |
| ar   |   240 |     1 |     624 |  27.9% |     +3 |       -3 |
| ru   |   272 |     1 |     592 |  31.6% |     +4 |       -4 |

總缺口（stale+missing）：**4354**（▼22 vs 上一筆）

**節點／worker**（ok/fail 為累計；Δ為對上一筆）

| 節點                |  ok | fail | Δok | 平均秒 | 主要 fail                              |
| ------------------- | --: | ---: | --: | -----: | -------------------------------------- |
| fleet:desktop-3090  |  56 |  325 |   · |      — | health×123；verify=1×102               |
| fleet:laptop-4090   |  27 |  137 |   · |      — | health×83；verify=None×24              |
| worker:d3090        |  13 |   40 |   · |  900.2 | no output written by tra×25；leak×6    |
| worker:desktop30901 |  21 |   19 |   · |  624.0 | health×10；leak×4                      |
| worker:desktop30902 |  16 |   23 |   · |  613.5 | health×10；verify=1×6                  |
| worker:gemma31      |   1 |   34 |   · |    2.2 | no output written by tra×34            |
| worker:l4090        |  16 |   47 |   · |  753.0 | no output written by tra×26；leak×10   |
| worker:laguna       | 133 |  170 |  +1 |  215.9 | no output written by tra×94；health×24 |
| worker:laptop40901  |  17 |   14 |   · |  874.1 | health×9；leak×2                       |
| worker:laptop40902  |  15 |   15 |   · |  894.2 | leak×6；health×5                       |
| worker:mac          | 138 |  334 |  +1 |  196.7 | leak×166；health×60                    |
| worker:nemo         | 442 |  748 |  +5 |  106.6 | leak×509；health×116                   |
| worker:nemo2        | 394 |  662 |  +6 |  108.4 | leak×464；health×93                    |
| worker:nemo3        | 347 |  487 |  +6 |  100.5 | leak×312；health×69                    |
| worker:oss20        |  73 |  149 |  +1 |  445.2 | leak×57；no output written by tra×38   |

endpoint 探活：local 🟢、laptop-4090 🔴、laptop-5090 🔴、desktop-3090 🟢、mac-m4max 🟢

（babel-pulse 常駐儀器自動快照）

## 2026-07-26T04:45:20+08:00（zh 總數 865）

| 語言 | fresh | stale | missing | 覆蓋率 | Δfresh | Δmissing |
| ---- | ----: | ----: | ------: | -----: | -----: | -------: |
| en   |   721 |   109 |      35 |  96.0% |      · |        · |
| ja   |   717 |   142 |       6 |  99.3% |      · |        · |
| ko   |   715 |   145 |       5 |  99.4% |      · |        · |
| es   |   718 |   144 |       3 |  99.7% |      · |        · |
| fr   |   719 |   143 |       3 |  99.7% |      · |        · |
| vi   |   127 |    17 |     721 |  16.6% |     +2 |       -2 |
| id   |   242 |    11 |     612 |  29.2% |     +5 |       -5 |
| pt   |   396 |    12 |     457 |  47.2% |     +4 |       -4 |
| hi   |   309 |     7 |     549 |  36.5% |     +4 |       -4 |
| ar   |   245 |     1 |     619 |  28.4% |     +5 |       -5 |
| ru   |   277 |     1 |     587 |  32.1% |     +5 |       -5 |

總缺口（stale+missing）：**4329**（▼25 vs 上一筆）

**節點／worker**（ok/fail 為累計；Δ為對上一筆）

| 節點                |  ok | fail | Δok | 平均秒 | 主要 fail                              |
| ------------------- | --: | ---: | --: | -----: | -------------------------------------- |
| fleet:desktop-3090  |  56 |  325 |   · |      — | health×123；verify=1×102               |
| fleet:laptop-4090   |  27 |  137 |   · |      — | health×83；verify=None×24              |
| worker:d3090        |  13 |   41 |   · |  900.2 | no output written by tra×26；leak×6    |
| worker:desktop30901 |  21 |   19 |   · |  624.0 | health×10；leak×4                      |
| worker:desktop30902 |  16 |   23 |   · |  613.5 | health×10；verify=1×6                  |
| worker:gemma31      |   1 |   34 |   · |    2.2 | no output written by tra×34            |
| worker:l4090        |  16 |   50 |   · |  753.0 | no output written by tra×29；leak×10   |
| worker:laguna       | 136 |  171 |  +3 |  216.2 | no output written by tra×95；health×24 |
| worker:laptop40901  |  17 |   14 |   · |  874.1 | health×9；leak×2                       |
| worker:laptop40902  |  15 |   15 |   · |  894.2 | leak×6；health×5                       |
| worker:mac          | 138 |  338 |   · |  196.7 | leak×170；health×60                    |
| worker:nemo         | 446 |  753 |  +4 |  106.5 | leak×513；health×116                   |
| worker:nemo2        | 402 |  666 |  +8 |  107.6 | leak×465；health×94                    |
| worker:nemo3        | 354 |  492 |  +7 |   99.6 | leak×315；health×69                    |
| worker:oss20        |  76 |  150 |  +3 |  435.5 | leak×57；no output written by tra×38   |

endpoint 探活：local 🟢、laptop-4090 🔴、laptop-5090 🔴、desktop-3090 🟢、mac-m4max 🟢

（babel-pulse 常駐儀器自動快照）

## 2026-07-26T04:58:39+08:00（zh 總數 865）

| 語言 | fresh | stale | missing | 覆蓋率 | Δfresh | Δmissing |
| ---- | ----: | ----: | ------: | -----: | -----: | -------: |
| en   |   721 |   109 |      35 |  96.0% |      · |        · |
| ja   |   717 |   142 |       6 |  99.3% |      · |        · |
| ko   |   715 |   145 |       5 |  99.4% |      · |        · |
| es   |   718 |   144 |       3 |  99.7% |      · |        · |
| fr   |   719 |   143 |       3 |  99.7% |      · |        · |
| vi   |   127 |    17 |     721 |  16.6% |      · |        · |
| id   |   243 |    11 |     611 |  29.4% |     +1 |       -1 |
| pt   |   397 |    12 |     456 |  47.3% |     +1 |       -1 |
| hi   |   310 |     7 |     548 |  36.6% |     +1 |       -1 |
| ar   |   246 |     1 |     618 |  28.6% |     +1 |       -1 |
| ru   |   279 |     1 |     585 |  32.4% |     +2 |       -2 |

總缺口（stale+missing）：**4323**（▼6 vs 上一筆）

**節點／worker**（ok/fail 為累計；Δ為對上一筆）

| 節點                |  ok | fail | Δok | 平均秒 | 主要 fail                              |
| ------------------- | --: | ---: | --: | -----: | -------------------------------------- |
| fleet:desktop-3090  |  56 |  325 |   · |      — | health×123；verify=1×102               |
| fleet:laptop-4090   |  27 |  137 |   · |      — | health×83；verify=None×24              |
| worker:d3090        |  13 |   41 |   · |  900.2 | no output written by tra×26；leak×6    |
| worker:desktop30901 |  21 |   19 |   · |  624.0 | health×10；leak×4                      |
| worker:desktop30902 |  16 |   23 |   · |  613.5 | health×10；verify=1×6                  |
| worker:gemma31      |   1 |   34 |   · |    2.2 | no output written by tra×34            |
| worker:l4090        |  16 |   50 |   · |  753.0 | no output written by tra×29；leak×10   |
| worker:laguna       | 136 |  172 |   · |  216.2 | no output written by tra×96；health×24 |
| worker:laptop40901  |  17 |   14 |   · |  874.1 | health×9；leak×2                       |
| worker:laptop40902  |  15 |   15 |   · |  894.2 | leak×6；health×5                       |
| worker:mac          | 139 |  340 |  +1 |  196.8 | leak×170；health×61                    |
| worker:nemo         | 448 |  756 |  +2 |  106.7 | leak×514；health×118                   |
| worker:nemo2        | 403 |  669 |  +1 |  107.5 | leak×467；health×95                    |
| worker:nemo3        | 356 |  495 |  +2 |   99.6 | leak×318；health×69                    |
| worker:oss20        |  76 |  151 |   · |  435.5 | leak×57；no output written by tra×39   |

endpoint 探活：local 🟢、laptop-4090 🔴、laptop-5090 🔴、desktop-3090 🟢、mac-m4max 🟢

（babel-pulse 常駐儀器自動快照）

## 2026-07-26T05:00:49+08:00（zh 總數 865）

| 語言 | fresh | stale | missing | 覆蓋率 | Δfresh | Δmissing |
| ---- | ----: | ----: | ------: | -----: | -----: | -------: |
| en   |   721 |   109 |      35 |  96.0% |      · |        · |
| ja   |   717 |   142 |       6 |  99.3% |      · |        · |
| ko   |   715 |   145 |       5 |  99.4% |      · |        · |
| es   |   718 |   144 |       3 |  99.7% |      · |        · |
| fr   |   719 |   143 |       3 |  99.7% |      · |        · |
| vi   |   127 |    17 |     721 |  16.6% |      · |        · |
| id   |   243 |    11 |     611 |  29.4% |      · |        · |
| pt   |   399 |    12 |     454 |  47.5% |     +2 |       -2 |
| hi   |   311 |     7 |     547 |  36.8% |     +1 |       -1 |
| ar   |   246 |     1 |     618 |  28.6% |      · |        · |
| ru   |   279 |     1 |     585 |  32.4% |      · |        · |

總缺口（stale+missing）：**4320**（▼3 vs 上一筆）

**節點／worker**（ok/fail 為累計；Δ為對上一筆）

| 節點                |  ok | fail | Δok | 平均秒 | 主要 fail                              |
| ------------------- | --: | ---: | --: | -----: | -------------------------------------- |
| fleet:desktop-3090  |  56 |  325 |   · |      — | health×123；verify=1×102               |
| fleet:laptop-4090   |  27 |  137 |   · |      — | health×83；verify=None×24              |
| worker:d3090        |  13 |   41 |   · |  900.2 | no output written by tra×26；leak×6    |
| worker:desktop30901 |  21 |   19 |   · |  624.0 | health×10；leak×4                      |
| worker:desktop30902 |  16 |   23 |   · |  613.5 | health×10；verify=1×6                  |
| worker:gemma31      |   1 |   34 |   · |    2.2 | no output written by tra×34            |
| worker:l4090        |  16 |   50 |   · |  753.0 | no output written by tra×29；leak×10   |
| worker:laguna       | 136 |  172 |   · |  216.2 | no output written by tra×96；health×24 |
| worker:laptop40901  |  17 |   14 |   · |  874.1 | health×9；leak×2                       |
| worker:laptop40902  |  15 |   15 |   · |  894.2 | leak×6；health×5                       |
| worker:mac          | 140 |  340 |  +1 |  196.6 | leak×170；health×61                    |
| worker:nemo         | 449 |  756 |  +1 |  106.8 | leak×514；health×118                   |
| worker:nemo2        | 403 |  669 |   · |  107.5 | leak×467；health×95                    |
| worker:nemo3        | 357 |  495 |  +1 |  100.0 | leak×318；health×69                    |
| worker:oss20        |  76 |  151 |   · |  435.5 | leak×57；no output written by tra×39   |

endpoint 探活：local 🟢、laptop-4090 🔴、laptop-5090 🔴、desktop-3090 🟢、mac-m4max 🟢

（babel-pulse 常駐儀器自動快照）

## 2026-07-26T05:16:20+08:00（zh 總數 865）

| 語言 | fresh | stale | missing | 覆蓋率 | Δfresh | Δmissing |
| ---- | ----: | ----: | ------: | -----: | -----: | -------: |
| en   |   721 |   109 |      35 |  96.0% |      · |        · |
| ja   |   717 |   142 |       6 |  99.3% |      · |        · |
| ko   |   716 |   144 |       5 |  99.4% |     +1 |        · |
| es   |   719 |   143 |       3 |  99.7% |     +1 |        · |
| fr   |   719 |   143 |       3 |  99.7% |      · |        · |
| vi   |   127 |    17 |     721 |  16.6% |      · |        · |
| id   |   243 |    11 |     611 |  29.4% |      · |        · |
| pt   |   400 |    12 |     453 |  47.6% |     +1 |       -1 |
| hi   |   311 |     7 |     547 |  36.8% |      · |        · |
| ar   |   247 |     1 |     617 |  28.7% |     +1 |       -1 |
| ru   |   281 |     1 |     583 |  32.6% |     +2 |       -2 |

總缺口（stale+missing）：**4314**（▼6 vs 上一筆）

**節點／worker**（ok/fail 為累計；Δ為對上一筆）

| 節點                |  ok | fail | Δok | 平均秒 | 主要 fail                              |
| ------------------- | --: | ---: | --: | -----: | -------------------------------------- |
| fleet:desktop-3090  |  56 |  325 |   · |      — | health×123；verify=1×102               |
| fleet:laptop-4090   |  27 |  137 |   · |      — | health×83；verify=None×24              |
| worker:d3090        |  13 |   41 |   · |  900.2 | no output written by tra×26；leak×6    |
| worker:desktop30901 |  21 |   19 |   · |  624.0 | health×10；leak×4                      |
| worker:desktop30902 |  16 |   23 |   · |  613.5 | health×10；verify=1×6                  |
| worker:gemma31      |   1 |   34 |   · |    2.2 | no output written by tra×34            |
| worker:l4090        |  16 |   53 |   · |  753.0 | no output written by tra×32；leak×10   |
| worker:laguna       | 136 |  173 |   · |  216.2 | no output written by tra×97；health×24 |
| worker:laptop40901  |  17 |   14 |   · |  874.1 | health×9；leak×2                       |
| worker:laptop40902  |  15 |   15 |   · |  894.2 | leak×6；health×5                       |
| worker:mac          | 142 |  344 |  +2 |  196.4 | leak×172；health×62                    |
| worker:nemo         | 450 |  760 |  +1 |  107.3 | leak×515；health×119                   |
| worker:nemo2        | 404 |  673 |  +1 |  107.6 | leak×468；health×95                    |
| worker:nemo3        | 359 |  498 |  +2 |  100.0 | leak×318；health×69                    |
| worker:oss20        |  76 |  152 |   · |  435.5 | leak×57；no output written by tra×40   |

endpoint 探活：local 🟢、laptop-4090 🔴、laptop-5090 🔴、desktop-3090 🟢、mac-m4max 🟢

（babel-pulse 常駐儀器自動快照）

## 2026-07-26T05:31:50+08:00（zh 總數 865）

| 語言 | fresh | stale | missing | 覆蓋率 | Δfresh | Δmissing |
| ---- | ----: | ----: | ------: | -----: | -----: | -------: |
| en   |   721 |   109 |      35 |  96.0% |      · |        · |
| ja   |   717 |   142 |       6 |  99.3% |      · |        · |
| ko   |   716 |   144 |       5 |  99.4% |      · |        · |
| es   |   719 |   143 |       3 |  99.7% |      · |        · |
| fr   |   719 |   143 |       3 |  99.7% |      · |        · |
| vi   |   127 |    17 |     721 |  16.6% |      · |        · |
| id   |   243 |    11 |     611 |  29.4% |      · |        · |
| pt   |   400 |    12 |     453 |  47.6% |      · |        · |
| hi   |   313 |     7 |     545 |  37.0% |     +2 |       -2 |
| ar   |   247 |     1 |     617 |  28.7% |      · |        · |
| ru   |   282 |     1 |     582 |  32.7% |     +1 |       -1 |

總缺口（stale+missing）：**4311**（▼3 vs 上一筆）

**節點／worker**（ok/fail 為累計；Δ為對上一筆）

| 節點                |  ok | fail | Δok | 平均秒 | 主要 fail                              |
| ------------------- | --: | ---: | --: | -----: | -------------------------------------- |
| fleet:desktop-3090  |  56 |  325 |   · |      — | health×123；verify=1×102               |
| fleet:laptop-4090   |  27 |  137 |   · |      — | health×83；verify=None×24              |
| worker:d3090        |  13 |   41 |   · |  900.2 | no output written by tra×26；leak×6    |
| worker:desktop30901 |  21 |   19 |   · |  624.0 | health×10；leak×4                      |
| worker:desktop30902 |  16 |   23 |   · |  613.5 | health×10；verify=1×6                  |
| worker:gemma31      |   1 |   34 |   · |    2.2 | no output written by tra×34            |
| worker:l4090        |  18 |   57 |  +2 |  670.5 | no output written by tra×35；leak×11   |
| worker:laguna       | 137 |  173 |  +1 |  219.0 | no output written by tra×97；health×24 |
| worker:laptop40901  |  17 |   14 |   · |  874.1 | health×9；leak×2                       |
| worker:laptop40902  |  15 |   15 |   · |  894.2 | leak×6；health×5                       |
| worker:mac          | 143 |  347 |  +1 |  195.8 | leak×175；health×62                    |
| worker:nemo         | 450 |  763 |   · |  107.3 | leak×515；health×121                   |
| worker:nemo2        | 405 |  675 |  +1 |  107.7 | leak×468；health×95                    |
| worker:nemo3        | 359 |  502 |   · |  100.0 | leak×319；health×69                    |
| worker:oss20        |  77 |  153 |  +1 |  434.2 | leak×57；no output written by tra×41   |

endpoint 探活：local 🟢、laptop-4090 🔴、laptop-5090 🔴、desktop-3090 🟢、mac-m4max 🟢

（babel-pulse 常駐儀器自動快照）

## 2026-07-26T05:47:22+08:00（zh 總數 865）

| 語言 | fresh | stale | missing | 覆蓋率 | Δfresh | Δmissing |
| ---- | ----: | ----: | ------: | -----: | -----: | -------: |
| en   |   721 |   109 |      35 |  96.0% |      · |        · |
| ja   |   717 |   142 |       6 |  99.3% |      · |        · |
| ko   |   716 |   144 |       5 |  99.4% |      · |        · |
| es   |   719 |   143 |       3 |  99.7% |      · |        · |
| fr   |   719 |   143 |       3 |  99.7% |      · |        · |
| vi   |   127 |    17 |     721 |  16.6% |      · |        · |
| id   |   243 |    11 |     611 |  29.4% |      · |        · |
| pt   |   401 |    12 |     452 |  47.7% |     +1 |       -1 |
| hi   |   313 |     7 |     545 |  37.0% |      · |        · |
| ar   |   249 |     1 |     615 |  28.9% |     +2 |       -2 |
| ru   |   284 |     1 |     580 |  32.9% |     +2 |       -2 |

總缺口（stale+missing）：**4306**（▼5 vs 上一筆）

**節點／worker**（ok/fail 為累計；Δ為對上一筆）

| 節點                |  ok | fail | Δok | 平均秒 | 主要 fail                              |
| ------------------- | --: | ---: | --: | -----: | -------------------------------------- |
| fleet:desktop-3090  |  56 |  325 |   · |      — | health×123；verify=1×102               |
| fleet:laptop-4090   |  27 |  137 |   · |      — | health×83；verify=None×24              |
| worker:d3090        |  14 |   41 |  +1 |  900.2 | no output written by tra×26；leak×6    |
| worker:desktop30901 |  21 |   19 |   · |  624.0 | health×10；leak×4                      |
| worker:desktop30902 |  16 |   23 |   · |  613.5 | health×10；verify=1×6                  |
| worker:gemma31      |   1 |   34 |   · |    2.2 | no output written by tra×34            |
| worker:l4090        |  18 |   57 |   · |  670.5 | no output written by tra×35；leak×11   |
| worker:laguna       | 137 |  175 |   · |  219.0 | no output written by tra×98；health×25 |
| worker:laptop40901  |  17 |   14 |   · |  874.1 | health×9；leak×2                       |
| worker:laptop40902  |  15 |   15 |   · |  894.2 | leak×6；health×5                       |
| worker:mac          | 144 |  351 |  +1 |  196.3 | leak×177；health×63                    |
| worker:nemo         | 452 |  768 |  +2 |  107.2 | leak×517；health×121                   |
| worker:nemo2        | 406 |  678 |  +1 |  107.6 | leak×469；health×95                    |
| worker:nemo3        | 361 |  507 |  +2 |   99.7 | leak×320；health×70                    |
| worker:oss20        |  77 |  154 |   · |  434.2 | leak×57；no output written by tra×41   |

endpoint 探活：local 🟢、laptop-4090 🔴、laptop-5090 🔴、desktop-3090 🟢、mac-m4max 🟢

（babel-pulse 常駐儀器自動快照）

## 2026-07-26T06:03:00+08:00（zh 總數 865）

| 語言 | fresh | stale | missing | 覆蓋率 | Δfresh | Δmissing |
| ---- | ----: | ----: | ------: | -----: | -----: | -------: |
| en   |   721 |   109 |      35 |  96.0% |      · |        · |
| ja   |   717 |   142 |       6 |  99.3% |      · |        · |
| ko   |   716 |   144 |       5 |  99.4% |      · |        · |
| es   |   719 |   143 |       3 |  99.7% |      · |        · |
| fr   |   719 |   143 |       3 |  99.7% |      · |        · |
| vi   |   127 |    17 |     721 |  16.6% |      · |        · |
| id   |   243 |    11 |     611 |  29.4% |      · |        · |
| pt   |   401 |    12 |     452 |  47.7% |      · |        · |
| hi   |   315 |     7 |     543 |  37.2% |     +2 |       -2 |
| ar   |   250 |     1 |     614 |  29.0% |     +1 |       -1 |
| ru   |   284 |     1 |     580 |  32.9% |      · |        · |

總缺口（stale+missing）：**4303**（▼3 vs 上一筆）

**節點／worker**（ok/fail 為累計；Δ為對上一筆）

| 節點                |  ok | fail | Δok | 平均秒 | 主要 fail                              |
| ------------------- | --: | ---: | --: | -----: | -------------------------------------- |
| fleet:desktop-3090  |  56 |  325 |   · |      — | health×123；verify=1×102               |
| fleet:laptop-4090   |  27 |  137 |   · |      — | health×83；verify=None×24              |
| worker:d3090        |  14 |   43 |   · |  900.2 | no output written by tra×28；leak×6    |
| worker:desktop30901 |  21 |   19 |   · |  624.0 | health×10；leak×4                      |
| worker:desktop30902 |  16 |   23 |   · |  613.5 | health×10；verify=1×6                  |
| worker:gemma31      |   1 |   34 |   · |    2.2 | no output written by tra×34            |
| worker:l4090        |  18 |   62 |   · |  670.5 | no output written by tra×38；leak×12   |
| worker:laguna       | 138 |  176 |  +1 |  218.2 | no output written by tra×99；health×25 |
| worker:laptop40901  |  17 |   14 |   · |  874.1 | health×9；leak×2                       |
| worker:laptop40902  |  15 |   15 |   · |  894.2 | leak×6；health×5                       |
| worker:mac          | 144 |  354 |   · |  196.3 | leak×178；health×64                    |
| worker:nemo         | 452 |  771 |   · |  107.2 | leak×517；health×122                   |
| worker:nemo2        | 407 |  685 |  +1 |  107.7 | leak×473；health×95                    |
| worker:nemo3        | 362 |  515 |  +1 |   99.6 | leak×325；health×71                    |
| worker:oss20        |  77 |  155 |   · |  434.2 | leak×57；no output written by tra×42   |

endpoint 探活：local 🟢、laptop-4090 🔴、laptop-5090 🔴、desktop-3090 🟢、mac-m4max 🟢

（babel-pulse 常駐儀器自動快照）

## 2026-07-26T06:34:04+08:00（zh 總數 865）

| 語言 | fresh | stale | missing | 覆蓋率 | Δfresh | Δmissing |
| ---- | ----: | ----: | ------: | -----: | -----: | -------: |
| en   |   721 |   109 |      35 |  96.0% |      · |        · |
| ja   |   718 |   141 |       6 |  99.3% |     +1 |        · |
| ko   |   716 |   144 |       5 |  99.4% |      · |        · |
| es   |   719 |   143 |       3 |  99.7% |      · |        · |
| fr   |   719 |   143 |       3 |  99.7% |      · |        · |
| vi   |   127 |    17 |     721 |  16.6% |      · |        · |
| id   |   243 |    11 |     611 |  29.4% |      · |        · |
| pt   |   401 |    12 |     452 |  47.7% |      · |        · |
| hi   |   315 |     7 |     543 |  37.2% |      · |        · |
| ar   |   255 |     1 |     609 |  29.6% |     +5 |       -5 |
| ru   |   292 |     1 |     572 |  33.9% |     +8 |       -8 |

總缺口（stale+missing）：**4289**（▼14 vs 上一筆）

**節點／worker**（ok/fail 為累計；Δ為對上一筆）

| 節點                |  ok | fail | Δok | 平均秒 | 主要 fail                               |
| ------------------- | --: | ---: | --: | -----: | --------------------------------------- |
| fleet:desktop-3090  |  56 |  325 |   · |      — | health×123；verify=1×102                |
| fleet:laptop-4090   |  27 |  137 |   · |      — | health×83；verify=None×24               |
| worker:d3090        |  14 |   45 |   · |  900.2 | no output written by tra×29；leak×7     |
| worker:desktop30901 |  21 |   19 |   · |  624.0 | health×10；leak×4                       |
| worker:desktop30902 |  16 |   23 |   · |  613.5 | health×10；verify=1×6                   |
| worker:gemma31      |   1 |   34 |   · |    2.2 | no output written by tra×34             |
| worker:l4090        |  19 |   67 |  +1 |  635.8 | no output written by tra×41；leak×14    |
| worker:laguna       | 140 |  181 |  +2 |  217.1 | no output written by tra×102；health×26 |
| worker:laptop40901  |  17 |   14 |   · |  874.1 | health×9；leak×2                        |
| worker:laptop40902  |  15 |   15 |   · |  894.2 | leak×6；health×5                        |
| worker:mac          | 145 |  362 |  +1 |  196.7 | leak×181；health×65                     |
| worker:nemo         | 455 |  784 |  +3 |  106.8 | leak×522；health×125                    |
| worker:nemo2        | 409 |  696 |  +2 |  107.5 | leak×477；health×97                     |
| worker:nemo3        | 367 |  528 |  +5 |   98.9 | leak×331；health×73                     |
| worker:oss20        |  78 |  159 |  +1 |  435.0 | leak×58；no output written by tra×44    |

endpoint 探活：local 🟢、laptop-4090 🔴、laptop-5090 🔴、desktop-3090 🟢、mac-m4max 🟢

（babel-pulse 常駐儀器自動快照）

## 2026-07-26T06:49:34+08:00（zh 總數 865）

| 語言 | fresh | stale | missing | 覆蓋率 | Δfresh | Δmissing |
| ---- | ----: | ----: | ------: | -----: | -----: | -------: |
| en   |   721 |   109 |      35 |  96.0% |      · |        · |
| ja   |   718 |   141 |       6 |  99.3% |      · |        · |
| ko   |   716 |   144 |       5 |  99.4% |      · |        · |
| es   |   719 |   143 |       3 |  99.7% |      · |        · |
| fr   |   719 |   143 |       3 |  99.7% |      · |        · |
| vi   |   127 |    17 |     721 |  16.6% |      · |        · |
| id   |   243 |    11 |     611 |  29.4% |      · |        · |
| pt   |   401 |    12 |     452 |  47.7% |      · |        · |
| hi   |   315 |     7 |     543 |  37.2% |      · |        · |
| ar   |   257 |     1 |     607 |  29.8% |     +2 |       -2 |
| ru   |   293 |     1 |     571 |  34.0% |     +1 |       -1 |

總缺口（stale+missing）：**4286**（▼3 vs 上一筆）

**節點／worker**（ok/fail 為累計；Δ為對上一筆）

| 節點                |  ok | fail | Δok | 平均秒 | 主要 fail                               |
| ------------------- | --: | ---: | --: | -----: | --------------------------------------- |
| fleet:desktop-3090  |  56 |  325 |   · |      — | health×123；verify=1×102                |
| fleet:laptop-4090   |  27 |  137 |   · |      — | health×83；verify=None×24               |
| worker:d3090        |  15 |   45 |  +1 |  900.2 | no output written by tra×29；leak×7     |
| worker:desktop30901 |  21 |   19 |   · |  624.0 | health×10；leak×4                       |
| worker:desktop30902 |  16 |   23 |   · |  613.5 | health×10；verify=1×6                   |
| worker:gemma31      |   1 |   34 |   · |    2.2 | no output written by tra×34             |
| worker:l4090        |  19 |   67 |   · |  635.8 | no output written by tra×41；leak×14    |
| worker:laguna       | 141 |  183 |  +1 |  219.0 | no output written by tra×103；health×26 |
| worker:laptop40901  |  17 |   14 |   · |  874.1 | health×9；leak×2                        |
| worker:laptop40902  |  15 |   15 |   · |  894.2 | leak×6；health×5                        |
| worker:mac          | 146 |  368 |  +1 |  195.8 | leak×183；health×67                     |
| worker:nemo         | 456 |  792 |  +1 |  106.7 | leak×526；health×128                    |
| worker:nemo2        | 409 |  703 |   · |  107.5 | leak×479；health×100                    |
| worker:nemo3        | 368 |  537 |  +1 |   99.0 | leak×337；health×76                     |
| worker:oss20        |  78 |  161 |   · |  435.0 | leak×58；no output written by tra×45    |

endpoint 探活：local 🟢、laptop-4090 🔴、laptop-5090 🔴、desktop-3090 🟢、mac-m4max 🟢

（babel-pulse 常駐儀器自動快照）

## 2026-07-26T07:05:02+08:00（zh 總數 865）

| 語言 | fresh | stale | missing | 覆蓋率 | Δfresh | Δmissing |
| ---- | ----: | ----: | ------: | -----: | -----: | -------: |
| en   |   721 |   109 |      35 |  96.0% |      · |        · |
| ja   |   719 |   140 |       6 |  99.3% |     +1 |        · |
| ko   |   716 |   144 |       5 |  99.4% |      · |        · |
| es   |   719 |   143 |       3 |  99.7% |      · |        · |
| fr   |   719 |   143 |       3 |  99.7% |      · |        · |
| vi   |   127 |    17 |     721 |  16.6% |      · |        · |
| id   |   244 |    11 |     610 |  29.5% |     +1 |       -1 |
| pt   |   403 |    12 |     450 |  48.0% |     +2 |       -2 |
| hi   |   315 |     7 |     543 |  37.2% |      · |        · |
| ar   |   259 |     1 |     605 |  30.1% |     +2 |       -2 |
| ru   |   295 |     1 |     569 |  34.2% |     +2 |       -2 |

總缺口（stale+missing）：**4278**（▼8 vs 上一筆）

**節點／worker**（ok/fail 為累計；Δ為對上一筆）

| 節點                |  ok | fail | Δok | 平均秒 | 主要 fail                               |
| ------------------- | --: | ---: | --: | -----: | --------------------------------------- |
| fleet:desktop-3090  |  56 |  325 |   · |      — | health×123；verify=1×102                |
| fleet:laptop-4090   |  27 |  137 |   · |      — | health×83；verify=None×24               |
| worker:d3090        |  15 |   46 |   · |  900.2 | no output written by tra×29；leak×7     |
| worker:desktop30901 |  21 |   19 |   · |  624.0 | health×10；leak×4                       |
| worker:desktop30902 |  16 |   23 |   · |  613.5 | health×10；verify=1×6                   |
| worker:gemma31      |   1 |   34 |   · |    2.2 | no output written by tra×34             |
| worker:l4090        |  19 |   70 |   · |  635.8 | no output written by tra×44；leak×14    |
| worker:laguna       | 141 |  185 |   · |  219.0 | no output written by tra×104；health×26 |
| worker:laptop40901  |  17 |   14 |   · |  874.1 | health×9；leak×2                        |
| worker:laptop40902  |  15 |   15 |   · |  894.2 | leak×6；health×5                        |
| worker:mac          | 148 |  373 |  +2 |  194.6 | leak×187；health×67                     |
| worker:nemo         | 459 |  798 |  +3 |  106.3 | leak×526；health×132                    |
| worker:nemo2        | 412 |  710 |  +3 |  107.1 | leak×483；health×102                    |
| worker:nemo3        | 369 |  542 |  +1 |   98.9 | leak×341；health×76                     |
| worker:oss20        |  78 |  163 |   · |  435.0 | leak×58；no output written by tra×45    |

endpoint 探活：local 🟢、laptop-4090 🔴、laptop-5090 🔴、desktop-3090 🟢、mac-m4max 🟢

（babel-pulse 常駐儀器自動快照）

## 2026-07-26T07:36:00+08:00（zh 總數 865）

| 語言 | fresh | stale | missing | 覆蓋率 | Δfresh | Δmissing |
| ---- | ----: | ----: | ------: | -----: | -----: | -------: |
| en   |   721 |   109 |      35 |  96.0% |      · |        · |
| ja   |   719 |   140 |       6 |  99.3% |      · |        · |
| ko   |   716 |   144 |       5 |  99.4% |      · |        · |
| es   |   719 |   143 |       3 |  99.7% |      · |        · |
| fr   |   719 |   143 |       3 |  99.7% |      · |        · |
| vi   |   127 |    17 |     721 |  16.6% |      · |        · |
| id   |   247 |    11 |     607 |  29.8% |     +3 |       -3 |
| pt   |   410 |    12 |     443 |  48.8% |     +7 |       -7 |
| hi   |   317 |     7 |     541 |  37.5% |     +2 |       -2 |
| ar   |   266 |     1 |     598 |  30.9% |     +7 |       -7 |
| ru   |   302 |     1 |     562 |  35.0% |     +7 |       -7 |

總缺口（stale+missing）：**4252**（▼26 vs 上一筆）

**節點／worker**（ok/fail 為累計；Δ為對上一筆）

| 節點                |  ok | fail | Δok | 平均秒 | 主要 fail                               |
| ------------------- | --: | ---: | --: | -----: | --------------------------------------- |
| fleet:desktop-3090  |  56 |  325 |   · |      — | health×123；verify=1×102                |
| fleet:laptop-4090   |  27 |  137 |   · |      — | health×83；verify=None×24               |
| worker:d3090        |  16 |   47 |  +1 |  900.2 | no output written by tra×29；leak×7     |
| worker:desktop30901 |  21 |   19 |   · |  624.0 | health×10；leak×4                       |
| worker:desktop30902 |  16 |   23 |   · |  613.5 | health×10；verify=1×6                   |
| worker:gemma31      |   1 |   34 |   · |    2.2 | no output written by tra×34             |
| worker:l4090        |  19 |   77 |   · |  635.8 | no output written by tra×48；leak×15    |
| worker:laguna       | 144 |  191 |  +3 |  217.4 | no output written by tra×106；health×29 |
| worker:laptop40901  |  17 |   14 |   · |  874.1 | health×9；leak×2                        |
| worker:laptop40902  |  15 |   15 |   · |  894.2 | leak×6；health×5                        |
| worker:mac          | 150 |  383 |  +2 |  195.3 | leak×192；health×68                     |
| worker:nemo         | 468 |  814 |  +9 |  105.6 | leak×534；health×138                    |
| worker:nemo2        | 414 |  726 |  +2 |  106.9 | leak×490；health×109                    |
| worker:nemo3        | 378 |  557 |  +9 |   98.4 | leak×352；health×77                     |
| worker:oss20        |  81 |  166 |  +3 |  431.0 | leak×59；no output written by tra×46    |

endpoint 探活：local 🟢、laptop-4090 🔴、laptop-5090 🔴、desktop-3090 🟢、mac-m4max 🟢

（babel-pulse 常駐儀器自動快照）

## 2026-07-26T07:51:22+08:00（zh 總數 865）

| 語言 | fresh | stale | missing | 覆蓋率 | Δfresh | Δmissing |
| ---- | ----: | ----: | ------: | -----: | -----: | -------: |
| en   |   721 |   109 |      35 |  96.0% |      · |        · |
| ja   |   719 |   140 |       6 |  99.3% |      · |        · |
| ko   |   716 |   144 |       5 |  99.4% |      · |        · |
| es   |   719 |   143 |       3 |  99.7% |      · |        · |
| fr   |   720 |   142 |       3 |  99.7% |     +1 |        · |
| vi   |   129 |    17 |     719 |  16.9% |     +2 |       -2 |
| id   |   249 |    11 |     605 |  30.1% |     +2 |       -2 |
| pt   |   413 |    12 |     440 |  49.1% |     +3 |       -3 |
| hi   |   318 |     7 |     540 |  37.6% |     +1 |       -1 |
| ar   |   269 |     1 |     595 |  31.2% |     +3 |       -3 |
| ru   |   303 |     1 |     561 |  35.1% |     +1 |       -1 |

總缺口（stale+missing）：**4239**（▼13 vs 上一筆）

**節點／worker**（ok/fail 為累計；Δ為對上一筆）

| 節點                |  ok | fail | Δok | 平均秒 | 主要 fail                               |
| ------------------- | --: | ---: | --: | -----: | --------------------------------------- |
| fleet:desktop-3090  |  56 |  325 |   · |      — | health×123；verify=1×102                |
| fleet:laptop-4090   |  27 |  137 |   · |      — | health×83；verify=None×24               |
| worker:d3090        |  17 |   47 |  +1 |  900.2 | no output written by tra×29；leak×7     |
| worker:desktop30901 |  21 |   19 |   · |  624.0 | health×10；leak×4                       |
| worker:desktop30902 |  16 |   23 |   · |  613.5 | health×10；verify=1×6                   |
| worker:gemma31      |   1 |   34 |   · |    2.2 | no output written by tra×34             |
| worker:l4090        |  19 |   77 |   · |  635.8 | no output written by tra×48；leak×15    |
| worker:laguna       | 145 |  193 |  +1 |  218.4 | no output written by tra×107；health×30 |
| worker:laptop40901  |  17 |   14 |   · |  874.1 | health×9；leak×2                        |
| worker:laptop40902  |  15 |   15 |   · |  894.2 | leak×6；health×5                        |
| worker:mac          | 155 |  387 |  +5 |  192.0 | leak×194；health×69                     |
| worker:nemo         | 469 |  820 |  +1 |  105.5 | leak×537；health×139                    |
| worker:nemo2        | 416 |  734 |  +2 |  106.8 | leak×495；health×111                    |
| worker:nemo3        | 381 |  563 |  +3 |   98.4 | leak×356；health×78                     |
| worker:oss20        |  82 |  168 |  +1 |  428.5 | leak×59；no output written by tra×47    |

endpoint 探活：local 🟢、laptop-4090 🔴、laptop-5090 🔴、desktop-3090 🟢、mac-m4max 🟢

（babel-pulse 常駐儀器自動快照）

## 2026-07-26T08:06:38+08:00（zh 總數 865）

| 語言 | fresh | stale | missing | 覆蓋率 | Δfresh | Δmissing |
| ---- | ----: | ----: | ------: | -----: | -----: | -------: |
| en   |   721 |   109 |      35 |  96.0% |      · |        · |
| ja   |   720 |   139 |       6 |  99.3% |     +1 |        · |
| ko   |   717 |   143 |       5 |  99.4% |     +1 |        · |
| es   |   719 |   143 |       3 |  99.7% |      · |        · |
| fr   |   721 |   141 |       3 |  99.7% |     +1 |        · |
| vi   |   129 |    17 |     719 |  16.9% |      · |        · |
| id   |   251 |    11 |     603 |  30.3% |     +2 |       -2 |
| pt   |   417 |    12 |     436 |  49.6% |     +4 |       -4 |
| hi   |   319 |     7 |     539 |  37.7% |     +1 |       -1 |
| ar   |   271 |     1 |     593 |  31.4% |     +2 |       -2 |
| ru   |   304 |     1 |     560 |  35.3% |     +1 |       -1 |

總缺口（stale+missing）：**4226**（▼13 vs 上一筆）

**節點／worker**（ok/fail 為累計；Δ為對上一筆）

| 節點                |  ok | fail | Δok | 平均秒 | 主要 fail                               |
| ------------------- | --: | ---: | --: | -----: | --------------------------------------- |
| fleet:desktop-3090  |  56 |  325 |   · |      — | health×123；verify=1×102                |
| fleet:laptop-4090   |  27 |  137 |   · |      — | health×83；verify=None×24               |
| worker:d3090        |  18 |   47 |  +1 |  900.2 | no output written by tra×29；leak×7     |
| worker:desktop30901 |  21 |   19 |   · |  624.0 | health×10；leak×4                       |
| worker:desktop30902 |  16 |   23 |   · |  613.5 | health×10；verify=1×6                   |
| worker:gemma31      |   1 |   34 |   · |    2.2 | no output written by tra×34             |
| worker:l4090        |  46 |  120 | +27 |  268.6 | no output written by tra×66；health×20  |
| worker:laguna       | 145 |  196 |   · |  218.4 | no output written by tra×109；health×31 |
| worker:laptop40901  |  17 |   14 |   · |  874.1 | health×9；leak×2                        |
| worker:laptop40902  |  15 |   15 |   · |  894.2 | leak×6；health×5                        |
| worker:mac          | 159 |  397 |  +4 |  188.7 | leak×197；health×75                     |
| worker:nemo         | 474 |  824 |  +5 |  105.4 | leak×538；health×142                    |
| worker:nemo2        | 418 |  740 |  +2 |  106.8 | leak×496；health×114                    |
| worker:nemo3        | 383 |  568 |  +2 |   98.3 | leak×359；health×79                     |
| worker:oss20        |  82 |  169 |   · |  428.5 | leak×60；no output written by tra×47    |

endpoint 探活：local 🟢、laptop-4090 🔴、laptop-5090 🔴、desktop-3090 🟢、mac-m4max 🟢

（babel-pulse 常駐儀器自動快照）

## 2026-07-26T08:22:01+08:00（zh 總數 865）

| 語言 | fresh | stale | missing | 覆蓋率 | Δfresh | Δmissing |
| ---- | ----: | ----: | ------: | -----: | -----: | -------: |
| en   |   721 |   109 |      35 |  96.0% |      · |        · |
| ja   |   720 |   139 |       6 |  99.3% |      · |        · |
| ko   |   717 |   143 |       5 |  99.4% |      · |        · |
| es   |   719 |   143 |       3 |  99.7% |      · |        · |
| fr   |   721 |   141 |       3 |  99.7% |      · |        · |
| vi   |   129 |    17 |     719 |  16.9% |      · |        · |
| id   |   252 |    11 |     602 |  30.4% |     +1 |       -1 |
| pt   |   417 |    12 |     436 |  49.6% |      · |        · |
| hi   |   321 |     7 |     537 |  37.9% |     +2 |       -2 |
| ar   |   274 |     1 |     590 |  31.8% |     +3 |       -3 |
| ru   |   305 |     1 |     559 |  35.4% |     +1 |       -1 |

總缺口（stale+missing）：**4219**（▼7 vs 上一筆）

**節點／worker**（ok/fail 為累計；Δ為對上一筆）

| 節點                |  ok | fail | Δok | 平均秒 | 主要 fail                               |
| ------------------- | --: | ---: | --: | -----: | --------------------------------------- |
| fleet:desktop-3090  |  56 |  325 |   · |      — | health×123；verify=1×102                |
| fleet:laptop-4090   |  27 |  137 |   · |      — | health×83；verify=None×24               |
| worker:d3090        |  19 |   47 |  +1 |  900.2 | no output written by tra×29；leak×7     |
| worker:desktop30901 |  21 |   19 |   · |  624.0 | health×10；leak×4                       |
| worker:desktop30902 |  16 |   23 |   · |  613.5 | health×10；verify=1×6                   |
| worker:gemma31      |   1 |   34 |   · |    2.2 | no output written by tra×34             |
| worker:l4090        |  49 |  126 |  +3 |  252.7 | no output written by tra×70；health×21  |
| worker:laguna       | 145 |  197 |   · |  218.4 | no output written by tra×110；health×31 |
| worker:laptop40901  |  17 |   14 |   · |  874.1 | health×9；leak×2                        |
| worker:laptop40902  |  15 |   15 |   · |  894.2 | leak×6；health×5                        |
| worker:mac          | 159 |  399 |   · |  188.7 | leak×199；health×75                     |
| worker:nemo         | 475 |  827 |  +1 |  105.3 | leak×541；health×142                    |
| worker:nemo2        | 420 |  745 |  +2 |  106.8 | leak×500；health×115                    |
| worker:nemo3        | 387 |  572 |  +4 |   98.2 | leak×360；health×79                     |
| worker:oss20        |  82 |  171 |   · |  428.5 | leak×60；no output written by tra×48    |

endpoint 探活：local 🟢、laptop-4090 🔴、laptop-5090 🔴、desktop-3090 🟢、mac-m4max 🟢

（babel-pulse 常駐儀器自動快照）

## 2026-07-26T08:24:36+08:00（zh 總數 865）

| 語言 | fresh | stale | missing | 覆蓋率 | Δfresh | Δmissing |
| ---- | ----: | ----: | ------: | -----: | -----: | -------: |
| en   |   721 |   109 |      35 |  96.0% |      · |        · |
| ja   |   720 |   139 |       6 |  99.3% |      · |        · |
| ko   |   717 |   143 |       5 |  99.4% |      · |        · |
| es   |   719 |   143 |       3 |  99.7% |      · |        · |
| fr   |   721 |   141 |       3 |  99.7% |      · |        · |
| vi   |   129 |    17 |     719 |  16.9% |      · |        · |
| id   |   252 |    11 |     602 |  30.4% |      · |        · |
| pt   |   417 |    12 |     436 |  49.6% |      · |        · |
| hi   |   321 |     7 |     537 |  37.9% |      · |        · |
| ar   |   274 |     1 |     590 |  31.8% |      · |        · |
| ru   |   306 |     1 |     558 |  35.5% |     +1 |       -1 |

總缺口（stale+missing）：**4218**（▼1 vs 上一筆）

**節點／worker**（ok/fail 為累計；Δ為對上一筆）

| 節點                |  ok | fail | Δok | 平均秒 | 主要 fail                               |
| ------------------- | --: | ---: | --: | -----: | --------------------------------------- |
| fleet:desktop-3090  |  56 |  325 |   · |      — | health×123；verify=1×102                |
| fleet:laptop-4090   |  27 |  137 |   · |      — | health×83；verify=None×24               |
| worker:d3090        |  19 |   47 |   · |  900.2 | no output written by tra×29；leak×7     |
| worker:desktop30901 |  21 |   19 |   · |  624.0 | health×10；leak×4                       |
| worker:desktop30902 |  16 |   23 |   · |  613.5 | health×10；verify=1×6                   |
| worker:gemma31      |   1 |   34 |   · |    2.2 | no output written by tra×34             |
| worker:l4090        |  49 |  126 |   · |  252.7 | no output written by tra×70；health×21  |
| worker:laguna       | 145 |  197 |   · |  218.4 | no output written by tra×110；health×31 |
| worker:laptop40901  |  17 |   14 |   · |  874.1 | health×9；leak×2                        |
| worker:laptop40902  |  15 |   15 |   · |  894.2 | leak×6；health×5                        |
| worker:mac          | 159 |  399 |   · |  188.7 | leak×199；health×75                     |
| worker:nemo         | 475 |  828 |   · |  105.3 | leak×541；health×143                    |
| worker:nemo2        | 420 |  747 |   · |  106.8 | leak×502；health×115                    |
| worker:nemo3        | 388 |  572 |  +1 |   98.2 | leak×360；health×79                     |
| worker:oss20        |  82 |  171 |   · |  428.5 | leak×60；no output written by tra×48    |

endpoint 探活：local 🟢、laptop-4090 🔴、laptop-5090 🔴、desktop-3090 🟢、mac-m4max 🟢

（babel-pulse 常駐儀器自動快照）

## 2026-07-26T08:37:36+08:00（zh 總數 865）

| 語言 | fresh | stale | missing | 覆蓋率 | Δfresh | Δmissing |
| ---- | ----: | ----: | ------: | -----: | -----: | -------: |
| en   |   721 |   109 |      35 |  96.0% |      · |        · |
| ja   |   720 |   139 |       6 |  99.3% |      · |        · |
| ko   |   717 |   143 |       5 |  99.4% |      · |        · |
| es   |   719 |   143 |       3 |  99.7% |      · |        · |
| fr   |   721 |   141 |       3 |  99.7% |      · |        · |
| vi   |   129 |    17 |     719 |  16.9% |      · |        · |
| id   |   252 |    11 |     602 |  30.4% |      · |        · |
| pt   |   417 |    12 |     436 |  49.6% |      · |        · |
| hi   |   321 |     7 |     537 |  37.9% |      · |        · |
| ar   |   274 |     1 |     590 |  31.8% |      · |        · |
| ru   |   306 |     1 |     558 |  35.5% |      · |        · |

總缺口（stale+missing）：**4218**（＝0 vs 上一筆）

**節點／worker**（ok/fail 為累計；Δ為對上一筆）

| 節點                |  ok | fail | Δok | 平均秒 | 主要 fail                               |
| ------------------- | --: | ---: | --: | -----: | --------------------------------------- |
| fleet:desktop-3090  |  56 |  325 |   · |      — | health×123；verify=1×102                |
| fleet:laptop-4090   |  27 |  137 |   · |      — | health×83；verify=None×24               |
| worker:d3090        |  19 |   48 |   · |  900.2 | no output written by tra×29；leak×8     |
| worker:desktop30901 |  21 |   19 |   · |  624.0 | health×10；leak×4                       |
| worker:desktop30902 |  16 |   23 |   · |  613.5 | health×10；verify=1×6                   |
| worker:gemma31      |   1 |   34 |   · |    2.2 | no output written by tra×34             |
| worker:l4090        |  49 |  126 |   · |  252.7 | no output written by tra×70；health×21  |
| worker:laguna       | 145 |  197 |   · |  218.4 | no output written by tra×110；health×31 |
| worker:laptop40901  |  17 |   14 |   · |  874.1 | health×9；leak×2                        |
| worker:laptop40902  |  15 |   15 |   · |  894.2 | leak×6；health×5                        |
| worker:mac          | 159 |  402 |   · |  188.7 | leak×200；health×76                     |
| worker:nemo         | 475 |  834 |   · |  105.3 | leak×544；health×145                    |
| worker:nemo2        | 420 |  750 |   · |  106.8 | leak×504；health×115                    |
| worker:nemo3        | 388 |  574 |   · |   98.2 | leak×361；health×79                     |
| worker:oss20        |  82 |  172 |   · |  428.5 | leak×60；no output written by tra×48    |

endpoint 探活：local 🟢、laptop-4090 🔴、laptop-5090 🔴、desktop-3090 🟢、mac-m4max 🟢

（babel-pulse 常駐儀器自動快照）

## 2026-07-26T08:53:04+08:00（zh 總數 865）

| 語言 | fresh | stale | missing | 覆蓋率 | Δfresh | Δmissing |
| ---- | ----: | ----: | ------: | -----: | -----: | -------: |
| en   |   721 |   109 |      35 |  96.0% |      · |        · |
| ja   |   720 |   139 |       6 |  99.3% |      · |        · |
| ko   |   717 |   143 |       5 |  99.4% |      · |        · |
| es   |   719 |   143 |       3 |  99.7% |      · |        · |
| fr   |   722 |   140 |       3 |  99.7% |     +1 |        · |
| vi   |   129 |    17 |     719 |  16.9% |      · |        · |
| id   |   253 |    11 |     601 |  30.5% |     +1 |       -1 |
| pt   |   418 |    12 |     435 |  49.7% |     +1 |       -1 |
| hi   |   322 |     7 |     536 |  38.0% |     +1 |       -1 |
| ar   |   274 |     1 |     590 |  31.8% |      · |        · |
| ru   |   306 |     1 |     558 |  35.5% |      · |        · |

總缺口（stale+missing）：**4214**（▼4 vs 上一筆）

**節點／worker**（ok/fail 為累計；Δ為對上一筆）

| 節點                |  ok | fail | Δok | 平均秒 | 主要 fail                               |
| ------------------- | --: | ---: | --: | -----: | --------------------------------------- |
| fleet:desktop-3090  |  56 |  325 |   · |      — | health×123；verify=1×102                |
| fleet:laptop-4090   |  27 |  137 |   · |      — | health×83；verify=None×24               |
| worker:d3090        |  19 |   49 |   · |  900.2 | no output written by tra×30；leak×8     |
| worker:desktop30901 |  21 |   19 |   · |  624.0 | health×10；leak×4                       |
| worker:desktop30902 |  16 |   23 |   · |  613.5 | health×10；verify=1×6                   |
| worker:gemma31      |   1 |   34 |   · |    2.2 | no output written by tra×34             |
| worker:l4090        |  51 |  136 |  +2 |  243.2 | no output written by tra×77；leak×21    |
| worker:laguna       | 145 |  197 |   · |  218.4 | no output written by tra×110；health×31 |
| worker:laptop40901  |  17 |   14 |   · |  874.1 | health×9；leak×2                        |
| worker:laptop40902  |  15 |   15 |   · |  894.2 | leak×6；health×5                        |
| worker:mac          | 161 |  405 |  +2 |  190.2 | leak×203；health×76                     |
| worker:nemo         | 475 |  836 |   · |  105.3 | leak×545；health×145                    |
| worker:nemo2        | 421 |  752 |  +1 |  106.7 | leak×504；health×115                    |
| worker:nemo3        | 389 |  575 |  +1 |   98.1 | leak×362；health×79                     |
| worker:oss20        |  82 |  173 |   · |  428.5 | leak×60；no output written by tra×49    |

endpoint 探活：local 🟢、laptop-4090 🔴、laptop-5090 🔴、desktop-3090 🟢、mac-m4max 🟢

（babel-pulse 常駐儀器自動快照）

## 2026-07-26T09:08:32+08:00（zh 總數 865）

| 語言 | fresh | stale | missing | 覆蓋率 | Δfresh | Δmissing |
| ---- | ----: | ----: | ------: | -----: | -----: | -------: |
| en   |   721 |   109 |      35 |  96.0% |      · |        · |
| ja   |   720 |   139 |       6 |  99.3% |      · |        · |
| ko   |   717 |   143 |       5 |  99.4% |      · |        · |
| es   |   719 |   143 |       3 |  99.7% |      · |        · |
| fr   |   722 |   140 |       3 |  99.7% |      · |        · |
| vi   |   129 |    17 |     719 |  16.9% |      · |        · |
| id   |   255 |    11 |     599 |  30.8% |     +2 |       -2 |
| pt   |   420 |    12 |     433 |  49.9% |     +2 |       -2 |
| hi   |   324 |     7 |     534 |  38.3% |     +2 |       -2 |
| ar   |   276 |     1 |     588 |  32.0% |     +2 |       -2 |
| ru   |   308 |     1 |     556 |  35.7% |     +2 |       -2 |

總缺口（stale+missing）：**4204**（▼10 vs 上一筆）

**節點／worker**（ok/fail 為累計；Δ為對上一筆）

| 節點                |  ok | fail | Δok | 平均秒 | 主要 fail                               |
| ------------------- | --: | ---: | --: | -----: | --------------------------------------- |
| fleet:desktop-3090  |  56 |  325 |   · |      — | health×123；verify=1×102                |
| fleet:laptop-4090   |  27 |  137 |   · |      — | health×83；verify=None×24               |
| worker:d3090        |  19 |   50 |   · |  900.2 | no output written by tra×31；leak×8     |
| worker:desktop30901 |  21 |   19 |   · |  624.0 | health×10；leak×4                       |
| worker:desktop30902 |  16 |   23 |   · |  613.5 | health×10；verify=1×6                   |
| worker:gemma31      |   1 |   34 |   · |    2.2 | no output written by tra×34             |
| worker:l4090        |  51 |  136 |   · |  243.2 | no output written by tra×77；leak×21    |
| worker:laguna       | 146 |  198 |  +1 |  219.8 | no output written by tra×111；health×31 |
| worker:laptop40901  |  17 |   14 |   · |  874.1 | health×9；leak×2                        |
| worker:laptop40902  |  15 |   15 |   · |  894.2 | leak×6；health×5                        |
| worker:mac          | 163 |  409 |  +2 |  189.8 | leak×204；health×77                     |
| worker:nemo         | 476 |  845 |  +1 |  105.3 | leak×548；health×147                    |
| worker:nemo2        | 423 |  759 |  +2 |  106.6 | leak×508；health×116                    |
| worker:nemo3        | 393 |  582 |  +4 |   98.0 | leak×365；health×83                     |
| worker:oss20        |  82 |  174 |   · |  428.5 | leak×60；no output written by tra×50    |

endpoint 探活：local 🟢、laptop-4090 🔴、laptop-5090 🔴、desktop-3090 🟢、mac-m4max 🟢

（babel-pulse 常駐儀器自動快照）

## 2026-07-26T09:23:57+08:00（zh 總數 865）

| 語言 | fresh | stale | missing | 覆蓋率 | Δfresh | Δmissing |
| ---- | ----: | ----: | ------: | -----: | -----: | -------: |
| en   |   721 |   109 |      35 |  96.0% |      · |        · |
| ja   |   721 |   138 |       6 |  99.3% |     +1 |        · |
| ko   |   717 |   143 |       5 |  99.4% |      · |        · |
| es   |   720 |   142 |       3 |  99.7% |     +1 |        · |
| fr   |   722 |   140 |       3 |  99.7% |      · |        · |
| vi   |   130 |    17 |     718 |  17.0% |     +1 |       -1 |
| id   |   255 |    11 |     599 |  30.8% |      · |        · |
| pt   |   423 |    12 |     430 |  50.3% |     +3 |       -3 |
| hi   |   325 |     7 |     533 |  38.4% |     +1 |       -1 |
| ar   |   280 |     1 |     584 |  32.5% |     +4 |       -4 |
| ru   |   313 |     1 |     551 |  36.3% |     +5 |       -5 |

總缺口（stale+missing）：**4188**（▼16 vs 上一筆）

**節點／worker**（ok/fail 為累計；Δ為對上一筆）

| 節點                |  ok | fail | Δok | 平均秒 | 主要 fail                               |
| ------------------- | --: | ---: | --: | -----: | --------------------------------------- |
| fleet:desktop-3090  |  56 |  325 |   · |      — | health×123；verify=1×102                |
| fleet:laptop-4090   |  27 |  137 |   · |      — | health×83；verify=None×24               |
| worker:d3090        |  19 |   51 |   · |  900.2 | no output written by tra×32；leak×8     |
| worker:desktop30901 |  21 |   19 |   · |  624.0 | health×10；leak×4                       |
| worker:desktop30902 |  16 |   23 |   · |  613.5 | health×10；verify=1×6                   |
| worker:gemma31      |   1 |   34 |   · |    2.2 | no output written by tra×34             |
| worker:l4090        |  53 |  145 |  +2 |  234.4 | no output written by tra×82；leak×25    |
| worker:laguna       | 149 |  200 |  +3 |  219.0 | no output written by tra×111；health×32 |
| worker:laptop40901  |  17 |   14 |   · |  874.1 | health×9；leak×2                        |
| worker:laptop40902  |  15 |   15 |   · |  894.2 | leak×6；health×5                        |
| worker:mac          | 166 |  413 |  +3 |  188.5 | leak×207；health×77                     |
| worker:nemo         | 480 |  853 |  +4 |  104.7 | leak×554；health×147                    |
| worker:nemo2        | 426 |  769 |  +3 |  106.4 | leak×514；health×118                    |
| worker:nemo3        | 396 |  587 |  +3 |   98.5 | leak×368；health×85                     |
| worker:oss20        |  83 |  174 |  +1 |  432.7 | leak×60；no output written by tra×50    |

endpoint 探活：local 🟢、laptop-4090 🔴、laptop-5090 🔴、desktop-3090 🟢、mac-m4max 🟢

（babel-pulse 常駐儀器自動快照）

## 2026-07-26T09:32:40+08:00（zh 總數 865）

| 語言 | fresh | stale | missing | 覆蓋率 | Δfresh | Δmissing |
| ---- | ----: | ----: | ------: | -----: | -----: | -------: |
| en   |   721 |   109 |      35 |  96.0% |      · |        · |
| ja   |   721 |   138 |       6 |  99.3% |      · |        · |
| ko   |   717 |   143 |       5 |  99.4% |      · |        · |
| es   |   720 |   142 |       3 |  99.7% |      · |        · |
| fr   |   722 |   140 |       3 |  99.7% |      · |        · |
| vi   |   130 |    17 |     718 |  17.0% |      · |        · |
| id   |   259 |    11 |     595 |  31.2% |     +4 |       -4 |
| pt   |   425 |    12 |     428 |  50.5% |     +2 |       -2 |
| hi   |   329 |     7 |     529 |  38.8% |     +4 |       -4 |
| ar   |   284 |     1 |     580 |  32.9% |     +4 |       -4 |
| ru   |   315 |     1 |     549 |  36.5% |     +2 |       -2 |

總缺口（stale+missing）：**4172**（▼16 vs 上一筆）

**節點／worker**（ok/fail 為累計；Δ為對上一筆）

| 節點                |  ok | fail | Δok | 平均秒 | 主要 fail                               |
| ------------------- | --: | ---: | --: | -----: | --------------------------------------- |
| fleet:desktop-3090  |  56 |  325 |   · |      — | health×123；verify=1×102                |
| fleet:laptop-4090   |  27 |  137 |   · |      — | health×83；verify=None×24               |
| worker:d3090        |  19 |   51 |   · |  900.2 | no output written by tra×32；leak×8     |
| worker:desktop30901 |  21 |   19 |   · |  624.0 | health×10；leak×4                       |
| worker:desktop30902 |  16 |   23 |   · |  613.5 | health×10；verify=1×6                   |
| worker:gemma31      |   1 |   34 |   · |    2.2 | no output written by tra×34             |
| worker:l4090        |  53 |  145 |   · |  234.4 | no output written by tra×82；leak×25    |
| worker:laguna       | 151 |  200 |  +2 |  219.0 | no output written by tra×111；health×32 |
| worker:laptop40901  |  17 |   14 |   · |  874.1 | health×9；leak×2                        |
| worker:laptop40902  |  15 |   15 |   · |  894.2 | leak×6；health×5                        |
| worker:mac          | 167 |  416 |  +1 |  187.9 | leak×207；health×79                     |
| worker:nemo         | 484 |  856 |  +4 |  104.3 | leak×555；health×148                    |
| worker:nemo2        | 430 |  773 |  +4 |  105.9 | leak×517；health×118                    |
| worker:nemo3        | 400 |  590 |  +4 |   98.1 | leak×368；health×85                     |
| worker:oss20        |  83 |  174 |   · |  432.7 | leak×60；no output written by tra×50    |

endpoint 探活：local 🟢、laptop-4090 🔴、laptop-5090 🔴、desktop-3090 🟢、mac-m4max 🟢

（babel-pulse 常駐儀器自動快照）

## 2026-07-26T09:39:18+08:00（zh 總數 865）

| 語言 | fresh | stale | missing | 覆蓋率 | Δfresh | Δmissing |
| ---- | ----: | ----: | ------: | -----: | -----: | -------: |
| en   |   721 |   109 |      35 |  96.0% |      · |        · |
| ja   |   721 |   138 |       6 |  99.3% |      · |        · |
| ko   |   717 |   143 |       5 |  99.4% |      · |        · |
| es   |   720 |   142 |       3 |  99.7% |      · |        · |
| fr   |   722 |   140 |       3 |  99.7% |      · |        · |
| vi   |   130 |    17 |     718 |  17.0% |      · |        · |
| id   |   259 |    11 |     595 |  31.2% |      · |        · |
| pt   |   426 |    12 |     427 |  50.6% |     +1 |       -1 |
| hi   |   330 |     7 |     528 |  39.0% |     +1 |       -1 |
| ar   |   285 |     1 |     579 |  33.1% |     +1 |       -1 |
| ru   |   315 |     1 |     549 |  36.5% |      · |        · |

總缺口（stale+missing）：**4169**（▼3 vs 上一筆）

**節點／worker**（ok/fail 為累計；Δ為對上一筆）

| 節點                |  ok | fail | Δok | 平均秒 | 主要 fail                               |
| ------------------- | --: | ---: | --: | -----: | --------------------------------------- |
| fleet:desktop-3090  |  56 |  325 |   · |      — | health×123；verify=1×102                |
| fleet:laptop-4090   |  27 |  137 |   · |      — | health×83；verify=None×24               |
| worker:d3090        |  19 |   51 |   · |  900.2 | no output written by tra×32；leak×8     |
| worker:desktop30901 |  21 |   19 |   · |  624.0 | health×10；leak×4                       |
| worker:desktop30902 |  16 |   23 |   · |  613.5 | health×10；verify=1×6                   |
| worker:gemma31      |   1 |   34 |   · |    2.2 | no output written by tra×34             |
| worker:l4090        |  53 |  145 |   · |  234.4 | no output written by tra×82；leak×25    |
| worker:laguna       | 151 |  201 |   · |  219.0 | no output written by tra×111；health×32 |
| worker:laptop40901  |  17 |   14 |   · |  874.1 | health×9；leak×2                        |
| worker:laptop40902  |  15 |   15 |   · |  894.2 | leak×6；health×5                        |
| worker:mac          | 167 |  420 |   · |  187.9 | leak×210；health×79                     |
| worker:nemo         | 485 |  857 |  +1 |  104.6 | leak×555；health×148                    |
| worker:nemo2        | 430 |  774 |   · |  105.9 | leak×518；health×118                    |
| worker:nemo3        | 402 |  592 |  +2 |   98.1 | leak×368；health×85                     |
| worker:oss20        |  83 |  175 |   · |  432.7 | leak×60；no output written by tra×50    |

endpoint 探活：local 🟢、laptop-4090 🔴、laptop-5090 🔴、desktop-3090 🟢、mac-m4max 🟢

（babel-pulse 常駐儀器自動快照）

## 2026-07-26T09:54:44+08:00（zh 總數 865）

| 語言 | fresh | stale | missing | 覆蓋率 | Δfresh | Δmissing |
| ---- | ----: | ----: | ------: | -----: | -----: | -------: |
| en   |   721 |   109 |      35 |  96.0% |      · |        · |
| ja   |   722 |   137 |       6 |  99.3% |     +1 |        · |
| ko   |   718 |   142 |       5 |  99.4% |     +1 |        · |
| es   |   720 |   142 |       3 |  99.7% |      · |        · |
| fr   |   722 |   140 |       3 |  99.7% |      · |        · |
| vi   |   131 |    17 |     717 |  17.1% |     +1 |       -1 |
| id   |   259 |    11 |     595 |  31.2% |      · |        · |
| pt   |   427 |    12 |     426 |  50.8% |     +1 |       -1 |
| hi   |   332 |     7 |     526 |  39.2% |     +2 |       -2 |
| ar   |   288 |     1 |     576 |  33.4% |     +3 |       -3 |
| ru   |   316 |     1 |     548 |  36.6% |     +1 |       -1 |

總缺口（stale+missing）：**4159**（▼10 vs 上一筆）

**節點／worker**（ok/fail 為累計；Δ為對上一筆）

| 節點                |  ok | fail | Δok | 平均秒 | 主要 fail                               |
| ------------------- | --: | ---: | --: | -----: | --------------------------------------- |
| fleet:desktop-3090  |  56 |  325 |   · |      — | health×123；verify=1×102                |
| fleet:laptop-4090   |  27 |  137 |   · |      — | health×83；verify=None×24               |
| worker:d3090        |  19 |   51 |   · |  900.2 | no output written by tra×32；leak×8     |
| worker:desktop30901 |  21 |   19 |   · |  624.0 | health×10；leak×4                       |
| worker:desktop30902 |  16 |   23 |   · |  613.5 | health×10；verify=1×6                   |
| worker:gemma31      |   1 |   34 |   · |    2.2 | no output written by tra×34             |
| worker:l4090        |  53 |  149 |   · |  234.4 | no output written by tra×85；leak×25    |
| worker:laguna       | 153 |  202 |  +2 |  219.1 | no output written by tra×112；health×32 |
| worker:laptop40901  |  17 |   14 |   · |  874.1 | health×9；leak×2                        |
| worker:laptop40902  |  15 |   15 |   · |  894.2 | leak×6；health×5                        |
| worker:mac          | 170 |  425 |  +3 |  186.9 | leak×212；health×82                     |
| worker:nemo         | 487 |  864 |  +2 |  104.5 | leak×560；health×148                    |
| worker:nemo2        | 432 |  782 |  +2 |  105.8 | leak×521；health×123                    |
| worker:nemo3        | 402 |  593 |   · |   98.1 | leak×368；health×85                     |
| worker:oss20        |  84 |  175 |  +1 |  438.1 | leak×60；no output written by tra×50    |

endpoint 探活：local 🟢、laptop-4090 🔴、laptop-5090 🔴、desktop-3090 🟢、mac-m4max 🟢

（babel-pulse 常駐儀器自動快照）

## 2026-07-26T10:10:13+08:00（zh 總數 865）

| 語言 | fresh | stale | missing | 覆蓋率 | Δfresh | Δmissing |
| ---- | ----: | ----: | ------: | -----: | -----: | -------: |
| en   |   721 |   109 |      35 |  96.0% |      · |        · |
| ja   |   723 |   136 |       6 |  99.3% |     +1 |        · |
| ko   |   719 |   141 |       5 |  99.4% |     +1 |        · |
| es   |   721 |   141 |       3 |  99.7% |     +1 |        · |
| fr   |   722 |   140 |       3 |  99.7% |      · |        · |
| vi   |   131 |    17 |     717 |  17.1% |      · |        · |
| id   |   259 |    11 |     595 |  31.2% |      · |        · |
| pt   |   427 |    12 |     426 |  50.8% |      · |        · |
| hi   |   333 |     7 |     525 |  39.3% |     +1 |       -1 |
| ar   |   290 |     1 |     574 |  33.6% |     +2 |       -2 |
| ru   |   317 |     1 |     547 |  36.8% |     +1 |       -1 |

總缺口（stale+missing）：**4152**（▼7 vs 上一筆）

**節點／worker**（ok/fail 為累計；Δ為對上一筆）

| 節點                |  ok | fail | Δok | 平均秒 | 主要 fail                               |
| ------------------- | --: | ---: | --: | -----: | --------------------------------------- |
| fleet:desktop-3090  |  56 |  325 |   · |      — | health×123；verify=1×102                |
| fleet:laptop-4090   |  27 |  137 |   · |      — | health×83；verify=None×24               |
| worker:d3090        |  19 |   52 |   · |  900.2 | no output written by tra×33；leak×8     |
| worker:desktop30901 |  21 |   19 |   · |  624.0 | health×10；leak×4                       |
| worker:desktop30902 |  16 |   23 |   · |  613.5 | health×10；verify=1×6                   |
| worker:gemma31      |   1 |   34 |   · |    2.2 | no output written by tra×34             |
| worker:l4090        |  53 |  149 |   · |  234.4 | no output written by tra×85；leak×25    |
| worker:laguna       | 153 |  204 |   · |  219.1 | no output written by tra×113；health×32 |
| worker:laptop40901  |  17 |   14 |   · |  874.1 | health×9；leak×2                        |
| worker:laptop40902  |  15 |   15 |   · |  894.2 | leak×6；health×5                        |
| worker:mac          | 173 |  429 |  +3 |  185.2 | leak×213；health×83                     |
| worker:nemo         | 489 |  870 |  +2 |  104.7 | leak×561；health×150                    |
| worker:nemo2        | 434 |  790 |  +2 |  105.7 | leak×523；health×126                    |
| worker:nemo3        | 402 |  593 |   · |   98.1 | leak×368；health×85                     |
| worker:oss20        |  84 |  176 |   · |  438.1 | leak×61；no output written by tra×50    |

endpoint 探活：local 🟢、laptop-4090 🔴、laptop-5090 🔴、desktop-3090 🟢、mac-m4max 🟢

（babel-pulse 常駐儀器自動快照）

## 2026-07-26T10:25:45+08:00（zh 總數 865）

| 語言 | fresh | stale | missing | 覆蓋率 | Δfresh | Δmissing |
| ---- | ----: | ----: | ------: | -----: | -----: | -------: |
| en   |   721 |   109 |      35 |  96.0% |      · |        · |
| ja   |   723 |   136 |       6 |  99.3% |      · |        · |
| ko   |   719 |   141 |       5 |  99.4% |      · |        · |
| es   |   721 |   141 |       3 |  99.7% |      · |        · |
| fr   |   724 |   138 |       3 |  99.7% |     +2 |        · |
| vi   |   133 |    17 |     715 |  17.3% |     +2 |       -2 |
| id   |   260 |    11 |     594 |  31.3% |     +1 |       -1 |
| pt   |   429 |    12 |     424 |  51.0% |     +2 |       -2 |
| hi   |   333 |     7 |     525 |  39.3% |      · |        · |
| ar   |   290 |     1 |     574 |  33.6% |      · |        · |
| ru   |   317 |     1 |     547 |  36.8% |      · |        · |

總缺口（stale+missing）：**4145**（▼7 vs 上一筆）

**節點／worker**（ok/fail 為累計；Δ為對上一筆）

| 節點                |  ok | fail | Δok | 平均秒 | 主要 fail                               |
| ------------------- | --: | ---: | --: | -----: | --------------------------------------- |
| fleet:desktop-3090  |  56 |  325 |   · |      — | health×123；verify=1×102                |
| fleet:laptop-4090   |  27 |  137 |   · |      — | health×83；verify=None×24               |
| worker:d3090        |  20 |   53 |  +1 |  900.2 | no output written by tra×34；leak×8     |
| worker:desktop30901 |  21 |   19 |   · |  624.0 | health×10；leak×4                       |
| worker:desktop30902 |  16 |   23 |   · |  613.5 | health×10；verify=1×6                   |
| worker:gemma31      |   1 |   34 |   · |    2.2 | no output written by tra×34             |
| worker:l4090        |  53 |  152 |   · |  234.4 | no output written by tra×88；leak×25    |
| worker:laguna       | 155 |  205 |  +2 |  220.2 | no output written by tra×113；health×33 |
| worker:laptop40901  |  17 |   14 |   · |  874.1 | health×9；leak×2                        |
| worker:laptop40902  |  15 |   15 |   · |  894.2 | leak×6；health×5                        |
| worker:mac          | 175 |  438 |  +2 |  184.3 | leak×219；health×85                     |
| worker:nemo         | 491 |  877 |  +2 |  104.6 | leak×564；health×151                    |
| worker:nemo2        | 434 |  799 |   · |  105.7 | leak×527；health×131                    |
| worker:nemo3        | 403 |  601 |  +1 |   98.1 | leak×370；health×90                     |
| worker:oss20        |  84 |  178 |   · |  438.1 | leak×62；no output written by tra×51    |

endpoint 探活：local 🟢、laptop-4090 🔴、laptop-5090 🔴、desktop-3090 🟢、mac-m4max 🟢

（babel-pulse 常駐儀器自動快照）

## 2026-07-26T10:34:47+08:00（zh 總數 865）

| 語言 | fresh | stale | missing | 覆蓋率 | Δfresh | Δmissing |
| ---- | ----: | ----: | ------: | -----: | -----: | -------: |
| en   |   721 |   109 |      35 |  96.0% |      · |        · |
| ja   |   724 |   135 |       6 |  99.3% |     +1 |        · |
| ko   |   719 |   141 |       5 |  99.4% |      · |        · |
| es   |   722 |   140 |       3 |  99.7% |     +1 |        · |
| fr   |   724 |   138 |       3 |  99.7% |      · |        · |
| vi   |   134 |    17 |     714 |  17.5% |     +1 |       -1 |
| id   |   260 |    11 |     594 |  31.3% |      · |        · |
| pt   |   429 |    12 |     424 |  51.0% |      · |        · |
| hi   |   334 |     7 |     524 |  39.4% |     +1 |       -1 |
| ar   |   290 |     1 |     574 |  33.6% |      · |        · |
| ru   |   317 |     1 |     547 |  36.8% |      · |        · |

總缺口（stale+missing）：**4141**（▼4 vs 上一筆）

**節點／worker**（ok/fail 為累計；Δ為對上一筆）

| 節點                |  ok | fail | Δok | 平均秒 | 主要 fail                               |
| ------------------- | --: | ---: | --: | -----: | --------------------------------------- |
| fleet:desktop-3090  |  56 |  325 |   · |      — | health×123；verify=1×102                |
| fleet:laptop-4090   |  27 |  137 |   · |      — | health×83；verify=None×24               |
| worker:d3090        |  20 |   53 |   · |  900.2 | no output written by tra×34；leak×8     |
| worker:desktop30901 |  21 |   19 |   · |  624.0 | health×10；leak×4                       |
| worker:desktop30902 |  16 |   23 |   · |  613.5 | health×10；verify=1×6                   |
| worker:gemma31      |   1 |   34 |   · |    2.2 | no output written by tra×34             |
| worker:l4090        |  53 |  152 |   · |  234.4 | no output written by tra×88；leak×25    |
| worker:laguna       | 155 |  206 |   · |  220.2 | no output written by tra×114；health×33 |
| worker:laptop40901  |  17 |   14 |   · |  874.1 | health×9；leak×2                        |
| worker:laptop40902  |  15 |   15 |   · |  894.2 | leak×6；health×5                        |
| worker:mac          | 178 |  443 |  +3 |  182.2 | leak×222；health×87                     |
| worker:nemo         | 491 |  879 |   · |  104.6 | leak×564；health×153                    |
| worker:nemo2        | 434 |  800 |   · |  105.7 | leak×527；health×131                    |
| worker:nemo3        | 403 |  603 |   · |   98.1 | leak×371；health×90                     |
| worker:oss20        |  85 |  178 |  +1 |  436.8 | leak×62；no output written by tra×51    |

endpoint 探活：local 🟢、laptop-4090 🔴、laptop-5090 🔴、desktop-3090 🟢、mac-m4max 🟢

（babel-pulse 常駐儀器自動快照）

## 2026-07-26T10:41:17+08:00（zh 總數 865）

| 語言 | fresh | stale | missing | 覆蓋率 | Δfresh | Δmissing |
| ---- | ----: | ----: | ------: | -----: | -----: | -------: |
| en   |   721 |   109 |      35 |  96.0% |      · |        · |
| ja   |   724 |   135 |       6 |  99.3% |      · |        · |
| ko   |   719 |   141 |       5 |  99.4% |      · |        · |
| es   |   722 |   140 |       3 |  99.7% |      · |        · |
| fr   |   724 |   138 |       3 |  99.7% |      · |        · |
| vi   |   134 |    17 |     714 |  17.5% |      · |        · |
| id   |   261 |    11 |     593 |  31.4% |     +1 |       -1 |
| pt   |   431 |    12 |     422 |  51.2% |     +2 |       -2 |
| hi   |   334 |     7 |     524 |  39.4% |      · |        · |
| ar   |   290 |     1 |     574 |  33.6% |      · |        · |
| ru   |   318 |     1 |     546 |  36.9% |     +1 |       -1 |

總缺口（stale+missing）：**4137**（▼4 vs 上一筆）

**節點／worker**（ok/fail 為累計；Δ為對上一筆）

| 節點                |  ok | fail | Δok | 平均秒 | 主要 fail                               |
| ------------------- | --: | ---: | --: | -----: | --------------------------------------- |
| fleet:desktop-3090  |  56 |  325 |   · |      — | health×123；verify=1×102                |
| fleet:laptop-4090   |  27 |  137 |   · |      — | health×83；verify=None×24               |
| worker:d3090        |  20 |   53 |   · |  900.2 | no output written by tra×34；leak×8     |
| worker:desktop30901 |  21 |   19 |   · |  624.0 | health×10；leak×4                       |
| worker:desktop30902 |  16 |   23 |   · |  613.5 | health×10；verify=1×6                   |
| worker:gemma31      |   1 |   34 |   · |    2.2 | no output written by tra×34             |
| worker:l4090        |  55 |  156 |  +2 |  226.3 | no output written by tra×91；leak×26    |
| worker:laguna       | 155 |  206 |   · |  220.2 | no output written by tra×114；health×33 |
| worker:laptop40901  |  17 |   14 |   · |  874.1 | health×9；leak×2                        |
| worker:laptop40902  |  15 |   15 |   · |  894.2 | leak×6；health×5                        |
| worker:mac          | 178 |  445 |   · |  182.2 | leak×223；health×88                     |
| worker:nemo         | 492 |  880 |  +1 |  104.5 | leak×565；health×153                    |
| worker:nemo2        | 435 |  802 |  +1 |  105.5 | leak×529；health×131                    |
| worker:nemo3        | 406 |  603 |  +3 |   98.1 | leak×371；health×90                     |
| worker:oss20        |  85 |  179 |   · |  436.8 | leak×62；no output written by tra×51    |

endpoint 探活：local 🟢、laptop-4090 🔴、laptop-5090 🔴、desktop-3090 🟢、mac-m4max 🟢

（babel-pulse 常駐儀器自動快照）

## 2026-07-26T10:56:49+08:00（zh 總數 865）

| 語言 | fresh | stale | missing | 覆蓋率 | Δfresh | Δmissing |
| ---- | ----: | ----: | ------: | -----: | -----: | -------: |
| en   |   721 |   109 |      35 |  96.0% |      · |        · |
| ja   |   724 |   135 |       6 |  99.3% |      · |        · |
| ko   |   719 |   141 |       5 |  99.4% |      · |        · |
| es   |   722 |   140 |       3 |  99.7% |      · |        · |
| fr   |   724 |   138 |       3 |  99.7% |      · |        · |
| vi   |   135 |    17 |     713 |  17.6% |     +1 |       -1 |
| id   |   264 |    11 |     590 |  31.8% |     +3 |       -3 |
| pt   |   435 |    12 |     418 |  51.7% |     +4 |       -4 |
| hi   |   336 |     7 |     522 |  39.7% |     +2 |       -2 |
| ar   |   295 |     1 |     569 |  34.2% |     +5 |       -5 |
| ru   |   323 |     1 |     541 |  37.5% |     +5 |       -5 |

總缺口（stale+missing）：**4117**（▼20 vs 上一筆）

**節點／worker**（ok/fail 為累計；Δ為對上一筆）

| 節點                |  ok | fail | Δok | 平均秒 | 主要 fail                               |
| ------------------- | --: | ---: | --: | -----: | --------------------------------------- |
| fleet:desktop-3090  |  56 |  325 |   · |      — | health×123；verify=1×102                |
| fleet:laptop-4090   |  27 |  137 |   · |      — | health×83；verify=None×24               |
| worker:d3090        |  21 |   53 |  +1 |  900.2 | no output written by tra×34；leak×8     |
| worker:desktop30901 |  21 |   19 |   · |  624.0 | health×10；leak×4                       |
| worker:desktop30902 |  16 |   23 |   · |  613.5 | health×10；verify=1×6                   |
| worker:gemma31      |   1 |   34 |   · |    2.2 | no output written by tra×34             |
| worker:l4090        |  55 |  156 |   · |  226.3 | no output written by tra×91；leak×26    |
| worker:laguna       | 156 |  207 |  +1 |  219.2 | no output written by tra×115；health×33 |
| worker:laptop40901  |  17 |   14 |   · |  874.1 | health×9；leak×2                        |
| worker:laptop40902  |  15 |   15 |   · |  894.2 | leak×6；health×5                        |
| worker:mac          | 179 |  447 |  +1 |  183.0 | leak×225；health×88                     |
| worker:nemo         | 496 |  883 |  +4 |  104.2 | leak×565；health×153                    |
| worker:nemo2        | 439 |  808 |  +4 |  105.3 | leak×533；health×132                    |
| worker:nemo3        | 413 |  608 |  +7 |   97.8 | leak×374；health×90                     |
| worker:oss20        |  87 |  179 |  +2 |  436.5 | leak×62；no output written by tra×51    |

endpoint 探活：local 🟢、laptop-4090 🔴、laptop-5090 🔴、desktop-3090 🟢、mac-m4max 🟢

（babel-pulse 常駐儀器自動快照）

## 2026-07-26T11:12:41+08:00（zh 總數 865）

| 語言 | fresh | stale | missing | 覆蓋率 | Δfresh | Δmissing |
| ---- | ----: | ----: | ------: | -----: | -----: | -------: |
| en   |   721 |   109 |      35 |  96.0% |      · |        · |
| ja   |   724 |   135 |       6 |  99.3% |      · |        · |
| ko   |   719 |   141 |       5 |  99.4% |      · |        · |
| es   |   723 |   139 |       3 |  99.7% |     +1 |        · |
| fr   |   724 |   138 |       3 |  99.7% |      · |        · |
| vi   |   135 |    17 |     713 |  17.6% |      · |        · |
| id   |   269 |    11 |     585 |  32.4% |     +5 |       -5 |
| pt   |   441 |    12 |     412 |  52.4% |     +6 |       -6 |
| hi   |   337 |     7 |     521 |  39.8% |     +1 |       -1 |
| ar   |   299 |     1 |     565 |  34.7% |     +4 |       -4 |
| ru   |   327 |     1 |     537 |  37.9% |     +4 |       -4 |

總缺口（stale+missing）：**4096**（▼21 vs 上一筆）

**節點／worker**（ok/fail 為累計；Δ為對上一筆）

| 節點                |  ok | fail | Δok | 平均秒 | 主要 fail                               |
| ------------------- | --: | ---: | --: | -----: | --------------------------------------- |
| fleet:desktop-3090  |  56 |  325 |   · |      — | health×123；verify=1×102                |
| fleet:laptop-4090   |  27 |  137 |   · |      — | health×83；verify=None×24               |
| worker:d3090        |  21 |   54 |   · |  900.2 | no output written by tra×35；leak×8     |
| worker:desktop30901 |  21 |   19 |   · |  624.0 | health×10；leak×4                       |
| worker:desktop30902 |  16 |   23 |   · |  613.5 | health×10；verify=1×6                   |
| worker:gemma31      |   1 |   34 |   · |    2.2 | no output written by tra×34             |
| worker:l4090        |  55 |  159 |   · |  226.3 | no output written by tra×94；leak×26    |
| worker:laguna       | 158 |  208 |  +2 |  221.0 | no output written by tra×116；health×33 |
| worker:laptop40901  |  17 |   14 |   · |  874.1 | health×9；leak×2                        |
| worker:laptop40902  |  15 |   15 |   · |  894.2 | leak×6；health×5                        |
| worker:mac          | 180 |  449 |  +1 |  183.5 | leak×227；health×88                     |
| worker:nemo         | 501 |  888 |  +5 |  104.0 | leak×568；health×153                    |
| worker:nemo2        | 447 |  816 |  +8 |  104.3 | leak×536；health×134                    |
| worker:nemo3        | 419 |  613 |  +6 |   97.0 | leak×377；health×90                     |
| worker:oss20        |  87 |  180 |   · |  436.5 | leak×62；no output written by tra×52    |

endpoint 探活：local 🟢、laptop-4090 🔴、laptop-5090 🔴、desktop-3090 🟢、mac-m4max 🟢

（babel-pulse 常駐儀器自動快照）

## 2026-07-26T11:28:16+08:00（zh 總數 868）

| 語言 | fresh | stale | missing | 覆蓋率 | Δfresh | Δmissing |
| ---- | ----: | ----: | ------: | -----: | -----: | -------: |
| en   |   720 |   110 |      38 |  95.6% |     -1 |       +3 |
| ja   |   723 |   136 |       9 |  99.0% |     -1 |       +3 |
| ko   |   718 |   142 |       8 |  99.1% |     -1 |       +3 |
| es   |   722 |   140 |       6 |  99.3% |     -1 |       +3 |
| fr   |   723 |   139 |       6 |  99.3% |     -1 |       +3 |
| vi   |   135 |    17 |     716 |  17.5% |      · |       +3 |
| id   |   270 |    11 |     587 |  32.4% |     +1 |       +2 |
| pt   |   440 |    13 |     415 |  52.2% |     -1 |       +3 |
| hi   |   338 |     8 |     522 |  39.9% |     +1 |       +1 |
| ar   |   301 |     2 |     565 |  34.9% |     +2 |        · |
| ru   |   327 |     2 |     539 |  37.9% |      · |       +2 |

總缺口（stale+missing）：**4131**（▲35 vs 上一筆）

**節點／worker**（ok/fail 為累計；Δ為對上一筆）

| 節點                |  ok | fail | Δok | 平均秒 | 主要 fail                               |
| ------------------- | --: | ---: | --: | -----: | --------------------------------------- |
| fleet:desktop-3090  |  56 |  325 |   · |      — | health×123；verify=1×102                |
| fleet:laptop-4090   |  27 |  137 |   · |      — | health×83；verify=None×24               |
| worker:d3090        |  22 |   54 |  +1 |  900.2 | no output written by tra×35；leak×8     |
| worker:desktop30901 |  21 |   19 |   · |  624.0 | health×10；leak×4                       |
| worker:desktop30902 |  16 |   23 |   · |  613.5 | health×10；verify=1×6                   |
| worker:gemma31      |   1 |   34 |   · |    2.2 | no output written by tra×34             |
| worker:l4090        |  55 |  159 |   · |  226.3 | no output written by tra×94；leak×26    |
| worker:laguna       | 159 |  209 |  +1 |  221.5 | no output written by tra×117；health×33 |
| worker:laguna2      |   0 |    1 |   — |      — | no output written by tra×1              |
| worker:laptop40901  |  17 |   14 |   · |  874.1 | health×9；leak×2                        |
| worker:laptop40902  |  15 |   15 |   · |  894.2 | leak×6；health×5                        |
| worker:mac          | 180 |  452 |   · |  183.5 | leak×230；health×88                     |
| worker:nemo         | 502 |  895 |  +1 |  103.8 | leak×570；health×155                    |
| worker:nemo2        | 449 |  828 |  +2 |  104.3 | leak×542；health×138                    |
| worker:nemo3        | 421 |  622 |  +2 |   96.7 | leak×382；health×92                     |
| worker:oss20        |  87 |  181 |   · |  436.5 | leak×62；no output written by tra×53    |

endpoint 探活：local 🟢、laptop-4090 🔴、laptop-5090 🔴、desktop-3090 🟢、mac-m4max 🟢

（babel-pulse 常駐儀器自動快照）

## 2026-07-26T11:43:47+08:00（zh 總數 868）

| 語言 | fresh | stale | missing | 覆蓋率 | Δfresh | Δmissing |
| ---- | ----: | ----: | ------: | -----: | -----: | -------: |
| en   |   720 |   110 |      38 |  95.6% |      · |        · |
| ja   |   723 |   136 |       9 |  99.0% |      · |        · |
| ko   |   718 |   142 |       8 |  99.1% |      · |        · |
| es   |   722 |   140 |       6 |  99.3% |      · |        · |
| fr   |   723 |   139 |       6 |  99.3% |      · |        · |
| vi   |   137 |    17 |     714 |  17.7% |     +2 |       -2 |
| id   |   272 |    11 |     585 |  32.6% |     +2 |       -2 |
| pt   |   443 |    13 |     412 |  52.5% |     +3 |       -3 |
| hi   |   341 |     8 |     519 |  40.2% |     +3 |       -3 |
| ar   |   303 |     2 |     563 |  35.1% |     +2 |       -2 |
| ru   |   330 |     2 |     536 |  38.2% |     +3 |       -3 |

總缺口（stale+missing）：**4116**（▼15 vs 上一筆）

**節點／worker**（ok/fail 為累計；Δ為對上一筆）

| 節點                |  ok | fail | Δok | 平均秒 | 主要 fail                               |
| ------------------- | --: | ---: | --: | -----: | --------------------------------------- |
| fleet:desktop-3090  |  56 |  325 |   · |      — | health×123；verify=1×102                |
| fleet:laptop-4090   |  27 |  137 |   · |      — | health×83；verify=None×24               |
| worker:d3090        |  22 |   55 |   · |  900.2 | no output written by tra×36；leak×8     |
| worker:desktop30901 |  21 |   19 |   · |  624.0 | health×10；leak×4                       |
| worker:desktop30902 |  16 |   23 |   · |  613.5 | health×10；verify=1×6                   |
| worker:gemma31      |   1 |   34 |   · |    2.2 | no output written by tra×34             |
| worker:l4090        |  55 |  162 |   · |  226.3 | no output written by tra×97；leak×26    |
| worker:laguna       | 160 |  210 |  +1 |  222.3 | no output written by tra×118；health×33 |
| worker:laguna2      |   1 |    2 |  +1 |  444.6 | no output written by tra×2              |
| worker:laptop40901  |  17 |   14 |   · |  874.1 | health×9；leak×2                        |
| worker:laptop40902  |  15 |   15 |   · |  894.2 | leak×6；health×5                        |
| worker:mac          | 182 |  454 |  +2 |  183.6 | leak×230；health×89                     |
| worker:nemo         | 509 |  898 |  +7 |  103.6 | leak×572；health×155                    |
| worker:nemo2        | 452 |  834 |  +3 |  104.5 | leak×544；health×140                    |
| worker:nemo3        | 422 |  629 |  +1 |   96.6 | leak×385；health×92                     |
| worker:oss20        |  87 |  183 |   · |  436.5 | leak×62；no output written by tra×54    |

endpoint 探活：local 🟢、laptop-4090 🔴、laptop-5090 🔴、desktop-3090 🟢、mac-m4max 🟢

（babel-pulse 常駐儀器自動快照）

## 2026-07-26T11:59:10+08:00（zh 總數 868）

| 語言 | fresh | stale | missing | 覆蓋率 | Δfresh | Δmissing |
| ---- | ----: | ----: | ------: | -----: | -----: | -------: |
| en   |   720 |   110 |      38 |  95.6% |      · |        · |
| ja   |   723 |   136 |       9 |  99.0% |      · |        · |
| ko   |   718 |   142 |       8 |  99.1% |      · |        · |
| es   |   722 |   140 |       6 |  99.3% |      · |        · |
| fr   |   723 |   139 |       6 |  99.3% |      · |        · |
| vi   |   138 |    17 |     713 |  17.9% |     +1 |       -1 |
| id   |   272 |    11 |     585 |  32.6% |      · |        · |
| pt   |   447 |    13 |     408 |  53.0% |     +4 |       -4 |
| hi   |   342 |     8 |     518 |  40.3% |     +1 |       -1 |
| ar   |   308 |     2 |     558 |  35.7% |     +5 |       -5 |
| ru   |   333 |     2 |     533 |  38.6% |     +3 |       -3 |

總缺口（stale+missing）：**4102**（▼14 vs 上一筆）

**節點／worker**（ok/fail 為累計；Δ為對上一筆）

| 節點                |  ok | fail | Δok | 平均秒 | 主要 fail                               |
| ------------------- | --: | ---: | --: | -----: | --------------------------------------- |
| fleet:desktop-3090  |  56 |  325 |   · |      — | health×123；verify=1×102                |
| fleet:laptop-4090   |  27 |  137 |   · |      — | health×83；verify=None×24               |
| worker:d3090        |  22 |   56 |   · |  900.2 | no output written by tra×36；leak×9     |
| worker:desktop30901 |  21 |   19 |   · |  624.0 | health×10；leak×4                       |
| worker:desktop30902 |  16 |   23 |   · |  613.5 | health×10；verify=1×6                   |
| worker:gemma31      |   1 |   34 |   · |    2.2 | no output written by tra×34             |
| worker:l4090        |  55 |  162 |   · |  226.3 | no output written by tra×97；leak×26    |
| worker:laguna       | 160 |  211 |   · |  222.3 | no output written by tra×119；health×33 |
| worker:laguna2      |   1 |    3 |   · |  444.6 | no output written by tra×3              |
| worker:laptop40901  |  17 |   14 |   · |  874.1 | health×9；leak×2                        |
| worker:laptop40902  |  15 |   15 |   · |  894.2 | leak×6；health×5                        |
| worker:mac          | 183 |  458 |  +1 |  183.7 | leak×233；health×90                     |
| worker:nemo         | 513 |  903 |  +4 |  103.6 | leak×576；health×155                    |
| worker:nemo2        | 456 |  837 |  +4 |  104.9 | leak×546；health×140                    |
| worker:nemo3        | 427 |  632 |  +5 |   96.7 | leak×386；health×92                     |
| worker:oss20        |  87 |  186 |   · |  436.5 | leak×62；no output written by tra×57    |

endpoint 探活：local 🟢、laptop-4090 🔴、laptop-5090 🔴、desktop-3090 🟢、mac-m4max 🟢

（babel-pulse 常駐儀器自動快照）

## 2026-07-26T12:14:37+08:00（zh 總數 868）

| 語言 | fresh | stale | missing | 覆蓋率 | Δfresh | Δmissing |
| ---- | ----: | ----: | ------: | -----: | -----: | -------: |
| en   |   720 |   110 |      38 |  95.6% |      · |        · |
| ja   |   723 |   136 |       9 |  99.0% |      · |        · |
| ko   |   718 |   142 |       8 |  99.1% |      · |        · |
| es   |   722 |   140 |       6 |  99.3% |      · |        · |
| fr   |   723 |   139 |       6 |  99.3% |      · |        · |
| vi   |   140 |    17 |     711 |  18.1% |     +2 |       -2 |
| id   |   272 |    11 |     585 |  32.6% |      · |        · |
| pt   |   451 |    13 |     404 |  53.5% |     +4 |       -4 |
| hi   |   343 |     8 |     517 |  40.4% |     +1 |       -1 |
| ar   |   309 |     2 |     557 |  35.8% |     +1 |       -1 |
| ru   |   334 |     2 |     532 |  38.7% |     +1 |       -1 |

總缺口（stale+missing）：**4093**（▼9 vs 上一筆）

**節點／worker**（ok/fail 為累計；Δ為對上一筆）

| 節點                |  ok | fail | Δok | 平均秒 | 主要 fail                               |
| ------------------- | --: | ---: | --: | -----: | --------------------------------------- |
| fleet:desktop-3090  |  56 |  325 |   · |      — | health×123；verify=1×102                |
| fleet:laptop-4090   |  27 |  137 |   · |      — | health×83；verify=None×24               |
| worker:d3090        |  22 |   58 |   · |  900.2 | no output written by tra×38；leak×9     |
| worker:desktop30901 |  21 |   19 |   · |  624.0 | health×10；leak×4                       |
| worker:desktop30902 |  16 |   23 |   · |  613.5 | health×10；verify=1×6                   |
| worker:gemma31      |   1 |   34 |   · |    2.2 | no output written by tra×34             |
| worker:l4090        |  56 |  167 |  +1 |  222.4 | no output written by tra×100；leak×28   |
| worker:laguna       | 160 |  212 |   · |  222.3 | no output written by tra×120；health×33 |
| worker:laguna2      |   3 |    4 |  +2 |  364.1 | no output written by tra×4              |
| worker:laptop40901  |  17 |   14 |   · |  874.1 | health×9；leak×2                        |
| worker:laptop40902  |  15 |   15 |   · |  894.2 | leak×6；health×5                        |
| worker:mac          | 184 |  461 |  +1 |  184.0 | leak×235；health×91                     |
| worker:nemo         | 513 |  907 |   · |  103.6 | leak×577；health×157                    |
| worker:nemo2        | 459 |  840 |  +3 |  104.9 | leak×547；health×142                    |
| worker:nemo3        | 430 |  633 |  +3 |   96.7 | leak×387；health×92                     |
| worker:oss20        |  87 |  188 |   · |  436.5 | leak×62；no output written by tra×59    |

endpoint 探活：local 🟢、laptop-4090 🔴、laptop-5090 🔴、desktop-3090 🟢、mac-m4max 🟢

（babel-pulse 常駐儀器自動快照）

## 2026-07-26T12:29:58+08:00（zh 總數 868）

| 語言 | fresh | stale | missing | 覆蓋率 | Δfresh | Δmissing |
| ---- | ----: | ----: | ------: | -----: | -----: | -------: |
| en   |   720 |   110 |      38 |  95.6% |      · |        · |
| ja   |   723 |   136 |       9 |  99.0% |      · |        · |
| ko   |   718 |   142 |       8 |  99.1% |      · |        · |
| es   |   722 |   140 |       6 |  99.3% |      · |        · |
| fr   |   723 |   139 |       6 |  99.3% |      · |        · |
| vi   |   142 |    17 |     709 |  18.3% |     +2 |       -2 |
| id   |   272 |    11 |     585 |  32.6% |      · |        · |
| pt   |   451 |    13 |     404 |  53.5% |      · |        · |
| hi   |   343 |     8 |     517 |  40.4% |      · |        · |
| ar   |   310 |     2 |     556 |  35.9% |     +1 |       -1 |
| ru   |   336 |     2 |     530 |  38.9% |     +2 |       -2 |

總缺口（stale+missing）：**4088**（▼5 vs 上一筆）

**節點／worker**（ok/fail 為累計；Δ為對上一筆）

| 節點                |  ok | fail | Δok | 平均秒 | 主要 fail                               |
| ------------------- | --: | ---: | --: | -----: | --------------------------------------- |
| fleet:desktop-3090  |  56 |  325 |   · |      — | health×123；verify=1×102                |
| fleet:laptop-4090   |  27 |  137 |   · |      — | health×83；verify=None×24               |
| worker:d3090        |  22 |   58 |   · |  900.2 | no output written by tra×38；leak×9     |
| worker:desktop30901 |  21 |   19 |   · |  624.0 | health×10；leak×4                       |
| worker:desktop30902 |  16 |   23 |   · |  613.5 | health×10；verify=1×6                   |
| worker:gemma31      |   1 |   34 |   · |    2.2 | no output written by tra×34             |
| worker:l4090        |  56 |  167 |   · |  222.4 | no output written by tra×100；leak×28   |
| worker:laguna       | 160 |  212 |   · |  222.3 | no output written by tra×120；health×33 |
| worker:laguna2      |   5 |    4 |  +2 |  403.3 | no output written by tra×4              |
| worker:laptop40901  |  17 |   14 |   · |  874.1 | health×9；leak×2                        |
| worker:laptop40902  |  15 |   15 |   · |  894.2 | leak×6；health×5                        |
| worker:mac          | 185 |  462 |  +1 |  183.8 | leak×236；health×91                     |
| worker:nemo         | 513 |  918 |   · |  103.6 | leak×581；health×160                    |
| worker:nemo2        | 461 |  848 |  +2 |  105.1 | leak×549；health×148                    |
| worker:nemo3        | 430 |  641 |   · |   96.7 | leak×389；health×96                     |
| worker:oss20        |  87 |  188 |   · |  436.5 | leak×62；no output written by tra×59    |

endpoint 探活：local 🟢、laptop-4090 🔴、laptop-5090 🔴、desktop-3090 🟢、mac-m4max 🟢

（babel-pulse 常駐儀器自動快照）

## 2026-07-26T12:45:15+08:00（zh 總數 868）

| 語言 | fresh | stale | missing | 覆蓋率 | Δfresh | Δmissing |
| ---- | ----: | ----: | ------: | -----: | -----: | -------: |
| en   |   720 |   110 |      38 |  95.6% |      · |        · |
| ja   |   723 |   136 |       9 |  99.0% |      · |        · |
| ko   |   718 |   142 |       8 |  99.1% |      · |        · |
| es   |   722 |   140 |       6 |  99.3% |      · |        · |
| fr   |   723 |   139 |       6 |  99.3% |      · |        · |
| vi   |   145 |    17 |     706 |  18.7% |     +3 |       -3 |
| id   |   272 |    11 |     585 |  32.6% |      · |        · |
| pt   |   451 |    13 |     404 |  53.5% |      · |        · |
| hi   |   344 |     8 |     516 |  40.6% |     +1 |       -1 |
| ar   |   311 |     2 |     555 |  36.1% |     +1 |       -1 |
| ru   |   338 |     2 |     528 |  39.2% |     +2 |       -2 |

總缺口（stale+missing）：**4081**（▼7 vs 上一筆）

**節點／worker**（ok/fail 為累計；Δ為對上一筆）

| 節點                |  ok | fail | Δok | 平均秒 | 主要 fail                               |
| ------------------- | --: | ---: | --: | -----: | --------------------------------------- |
| fleet:desktop-3090  |  56 |  325 |   · |      — | health×123；verify=1×102                |
| fleet:laptop-4090   |  27 |  137 |   · |      — | health×83；verify=None×24               |
| worker:d3090        |  22 |   58 |   · |  900.2 | no output written by tra×38；leak×9     |
| worker:desktop30901 |  21 |   19 |   · |  624.0 | health×10；leak×4                       |
| worker:desktop30902 |  16 |   23 |   · |  613.5 | health×10；verify=1×6                   |
| worker:gemma31      |   1 |   34 |   · |    2.2 | no output written by tra×34             |
| worker:l4090        |  56 |  167 |   · |  222.4 | no output written by tra×100；leak×28   |
| worker:laguna       | 161 |  212 |  +1 |  222.7 | no output written by tra×120；health×33 |
| worker:laguna2      |   7 |    5 |  +2 |  376.4 | no output written by tra×4；health×1    |
| worker:laptop40901  |  17 |   14 |   · |  874.1 | health×9；leak×2                        |
| worker:laptop40902  |  15 |   15 |   · |  894.2 | leak×6；health×5                        |
| worker:mac          | 185 |  462 |   · |  183.8 | leak×236；health×91                     |
| worker:nemo         | 515 |  928 |  +2 |  103.7 | leak×582；health×166                    |
| worker:nemo2        | 461 |  855 |   · |  105.1 | leak×551；health×150                    |
| worker:nemo3        | 432 |  650 |  +2 |   96.8 | leak×394；health×99                     |
| worker:oss20        |  87 |  189 |   · |  436.5 | leak×62；no output written by tra×59    |

endpoint 探活：local 🟢、laptop-4090 🔴、laptop-5090 🔴、desktop-3090 🟢、mac-m4max 🟢

（babel-pulse 常駐儀器自動快照）

## 2026-07-26T13:00:32+08:00（zh 總數 868）

| 語言 | fresh | stale | missing | 覆蓋率 | Δfresh | Δmissing |
| ---- | ----: | ----: | ------: | -----: | -----: | -------: |
| en   |   720 |   110 |      38 |  95.6% |      · |        · |
| ja   |   723 |   136 |       9 |  99.0% |      · |        · |
| ko   |   718 |   142 |       8 |  99.1% |      · |        · |
| es   |   722 |   140 |       6 |  99.3% |      · |        · |
| fr   |   723 |   139 |       6 |  99.3% |      · |        · |
| vi   |   151 |    17 |     700 |  19.4% |     +6 |       -6 |
| id   |   273 |    11 |     584 |  32.7% |     +1 |       -1 |
| pt   |   452 |    13 |     403 |  53.6% |     +1 |       -1 |
| hi   |   347 |     8 |     513 |  40.9% |     +3 |       -3 |
| ar   |   312 |     2 |     554 |  36.2% |     +1 |       -1 |
| ru   |   338 |     2 |     528 |  39.2% |      · |        · |

總缺口（stale+missing）：**4069**（▼12 vs 上一筆）

**節點／worker**（ok/fail 為累計；Δ為對上一筆）

| 節點                |  ok | fail | Δok | 平均秒 | 主要 fail                               |
| ------------------- | --: | ---: | --: | -----: | --------------------------------------- |
| fleet:desktop-3090  |  56 |  325 |   · |      — | health×123；verify=1×102                |
| fleet:laptop-4090   |  27 |  137 |   · |      — | health×83；verify=None×24               |
| worker:d3090        |  22 |   58 |   · |  900.2 | no output written by tra×38；leak×9     |
| worker:desktop30901 |  21 |   19 |   · |  624.0 | health×10；leak×4                       |
| worker:desktop30902 |  16 |   23 |   · |  613.5 | health×10；verify=1×6                   |
| worker:gemma31      |   1 |   34 |   · |    2.2 | no output written by tra×34             |
| worker:l4090        |  56 |  167 |   · |  222.4 | no output written by tra×100；leak×28   |
| worker:laguna       | 164 |  212 |  +3 |  224.1 | no output written by tra×120；health×33 |
| worker:laguna2      |  10 |    7 |  +3 |  324.0 | no output written by tra×5；health×1    |
| worker:laptop40901  |  17 |   14 |   · |  874.1 | health×9；leak×2                        |
| worker:laptop40902  |  15 |   15 |   · |  894.2 | leak×6；health×5                        |
| worker:mac          | 185 |  462 |   · |  183.8 | leak×236；health×91                     |
| worker:nemo         | 517 |  936 |  +2 |  103.4 | leak×585；health×168                    |
| worker:nemo2        | 464 |  861 |  +3 |  105.0 | leak×554；health×152                    |
| worker:nemo3        | 433 |  658 |  +1 |   96.6 | leak×396；health×101                    |
| worker:oss20        |  87 |  191 |   · |  436.5 | leak×62；no output written by tra×59    |

endpoint 探活：local 🟢、laptop-4090 🔴、laptop-5090 🔴、desktop-3090 🟢、mac-m4max 🟢

（babel-pulse 常駐儀器自動快照）

## 2026-07-26T13:31:25+08:00（zh 總數 868）

| 語言 | fresh | stale | missing | 覆蓋率 | Δfresh | Δmissing |
| ---- | ----: | ----: | ------: | -----: | -----: | -------: |
| en   |   721 |   110 |      37 |  95.7% |     +1 |       -1 |
| ja   |   723 |   136 |       9 |  99.0% |      · |        · |
| ko   |   718 |   142 |       8 |  99.1% |      · |        · |
| es   |   722 |   140 |       6 |  99.3% |      · |        · |
| fr   |   723 |   139 |       6 |  99.3% |      · |        · |
| vi   |   154 |    17 |     697 |  19.7% |     +3 |       -3 |
| id   |   274 |    11 |     583 |  32.8% |     +1 |       -1 |
| pt   |   455 |    13 |     400 |  53.9% |     +3 |       -3 |
| hi   |   348 |     8 |     512 |  41.0% |     +1 |       -1 |
| ar   |   317 |     2 |     549 |  36.8% |     +5 |       -5 |
| ru   |   342 |     2 |     524 |  39.6% |     +4 |       -4 |

總缺口（stale+missing）：**4051**（▼18 vs 上一筆）

**節點／worker**（ok/fail 為累計；Δ為對上一筆）

| 節點                |  ok | fail | Δok | 平均秒 | 主要 fail                               |
| ------------------- | --: | ---: | --: | -----: | --------------------------------------- |
| fleet:desktop-3090  |  56 |  325 |   · |      — | health×123；verify=1×102                |
| fleet:laptop-4090   |  27 |  137 |   · |      — | health×83；verify=None×24               |
| worker:d3090        |  22 |   58 |   · |  900.2 | no output written by tra×38；leak×9     |
| worker:desktop30901 |  21 |   19 |   · |  624.0 | health×10；leak×4                       |
| worker:desktop30902 |  16 |   23 |   · |  613.5 | health×10；verify=1×6                   |
| worker:gemma31      |   1 |   34 |   · |    2.2 | no output written by tra×34             |
| worker:l4090        |  67 |  184 | +11 |  188.4 | no output written by tra×106；leak×31   |
| worker:laguna       | 165 |  215 |  +1 |  224.7 | no output written by tra×122；health×34 |
| worker:laguna2      |  12 |    9 |  +2 |  332.9 | no output written by tra×7；health×1    |
| worker:laptop40901  |  17 |   14 |   · |  874.1 | health×9；leak×2                        |
| worker:laptop40902  |  15 |   15 |   · |  894.2 | leak×6；health×5                        |
| worker:mac          | 185 |  463 |   · |  183.8 | leak×237；health×91                     |
| worker:nemo         | 519 |  945 |  +2 |  103.5 | leak×588；health×172                    |
| worker:nemo2        | 470 |  871 |  +6 |  105.4 | leak×559；health×155                    |
| worker:nemo3        | 438 |  668 |  +5 |   96.8 | leak×397；health×107                    |
| worker:oss20        |  88 |  197 |  +1 |  436.1 | no output written by tra×63；leak×62    |

endpoint 探活：local 🟢、laptop-4090 🔴、laptop-5090 🔴、desktop-3090 🟢、mac-m4max 🟢

（babel-pulse 常駐儀器自動快照）

## 2026-07-26T13:46:56+08:00（zh 總數 868）

| 語言 | fresh | stale | missing | 覆蓋率 | Δfresh | Δmissing |
| ---- | ----: | ----: | ------: | -----: | -----: | -------: |
| en   |   721 |   110 |      37 |  95.7% |      · |        · |
| ja   |   723 |   136 |       9 |  99.0% |      · |        · |
| ko   |   719 |   142 |       7 |  99.2% |     +1 |       -1 |
| es   |   723 |   140 |       5 |  99.4% |     +1 |       -1 |
| fr   |   724 |   138 |       6 |  99.3% |     +1 |        · |
| vi   |   155 |    17 |     696 |  19.8% |     +1 |       -1 |
| id   |   274 |    11 |     583 |  32.8% |      · |        · |
| pt   |   457 |    13 |     398 |  54.1% |     +2 |       -2 |
| hi   |   348 |     8 |     512 |  41.0% |      · |        · |
| ar   |   319 |     2 |     547 |  37.0% |     +2 |       -2 |
| ru   |   344 |     2 |     522 |  39.9% |     +2 |       -2 |

總缺口（stale+missing）：**4041**（▼10 vs 上一筆）

**節點／worker**（ok/fail 為累計；Δ為對上一筆）

| 節點                |  ok | fail | Δok | 平均秒 | 主要 fail                               |
| ------------------- | --: | ---: | --: | -----: | --------------------------------------- |
| fleet:desktop-3090  |  56 |  325 |   · |      — | health×123；verify=1×102                |
| fleet:laptop-4090   |  27 |  137 |   · |      — | health×83；verify=None×24               |
| worker:d3090        |  22 |   58 |   · |  900.2 | no output written by tra×38；leak×9     |
| worker:desktop30901 |  21 |   19 |   · |  624.0 | health×10；leak×4                       |
| worker:desktop30902 |  16 |   23 |   · |  613.5 | health×10；verify=1×6                   |
| worker:gemma31      |   1 |   34 |   · |    2.2 | no output written by tra×34             |
| worker:l4090        |  85 |  194 | +18 |  151.0 | no output written by tra×106；leak×32   |
| worker:laguna       | 165 |  217 |   · |  224.7 | no output written by tra×122；health×35 |
| worker:laguna2      |  13 |   10 |  +1 |  339.2 | no output written by tra×8；health×1    |
| worker:laptop40901  |  17 |   14 |   · |  874.1 | health×9；leak×2                        |
| worker:laptop40902  |  15 |   15 |   · |  894.2 | leak×6；health×5                        |
| worker:mac          | 185 |  465 |   · |  183.8 | leak×239；health×91                     |
| worker:nemo         | 521 |  951 |  +2 |  103.4 | leak×590；health×174                    |
| worker:nemo2        | 473 |  877 |  +3 |  105.2 | leak×561；health×157                    |
| worker:nemo3        | 440 |  678 |  +2 |   96.8 | leak×400；health×112                    |
| worker:oss20        |  88 |  200 |   · |  436.1 | no output written by tra×64；leak×62    |

endpoint 探活：local 🟢、laptop-4090 🔴、laptop-5090 🔴、desktop-3090 🟢、mac-m4max 🟢

（babel-pulse 常駐儀器自動快照）

## 2026-07-26T14:02:25+08:00（zh 總數 868）

| 語言 | fresh | stale | missing | 覆蓋率 | Δfresh | Δmissing |
| ---- | ----: | ----: | ------: | -----: | -----: | -------: |
| en   |   721 |   110 |      37 |  95.7% |      · |        · |
| ja   |   723 |   136 |       9 |  99.0% |      · |        · |
| ko   |   719 |   142 |       7 |  99.2% |      · |        · |
| es   |   723 |   140 |       5 |  99.4% |      · |        · |
| fr   |   724 |   139 |       5 |  99.4% |      · |       -1 |
| vi   |   157 |    17 |     694 |  20.0% |     +2 |       -2 |
| id   |   276 |    11 |     581 |  33.1% |     +2 |       -2 |
| pt   |   458 |    13 |     397 |  54.3% |     +1 |       -1 |
| hi   |   350 |     8 |     510 |  41.2% |     +2 |       -2 |
| ar   |   323 |     2 |     543 |  37.4% |     +4 |       -4 |
| ru   |   347 |     2 |     519 |  40.2% |     +3 |       -3 |

總缺口（stale+missing）：**4027**（▼14 vs 上一筆）

**節點／worker**（ok/fail 為累計；Δ為對上一筆）

| 節點                |  ok | fail | Δok | 平均秒 | 主要 fail                               |
| ------------------- | --: | ---: | --: | -----: | --------------------------------------- |
| fleet:desktop-3090  |  56 |  325 |   · |      — | health×123；verify=1×102                |
| fleet:laptop-4090   |  27 |  137 |   · |      — | health×83；verify=None×24               |
| worker:d3090        |  23 |   58 |  +1 |  931.2 | no output written by tra×38；leak×9     |
| worker:desktop30901 |  21 |   19 |   · |  624.0 | health×10；leak×4                       |
| worker:desktop30902 |  16 |   23 |   · |  613.5 | health×10；verify=1×6                   |
| worker:gemma31      |   1 |   34 |   · |    2.2 | no output written by tra×34             |
| worker:l4090        |  85 |  194 |   · |  151.0 | no output written by tra×106；leak×32   |
| worker:laguna       | 165 |  220 |   · |  224.7 | no output written by tra×123；health×36 |
| worker:laguna2      |  15 |   10 |  +2 |  317.0 | no output written by tra×8；health×1    |
| worker:laptop40901  |  17 |   14 |   · |  874.1 | health×9；leak×2                        |
| worker:laptop40902  |  15 |   15 |   · |  894.2 | leak×6；health×5                        |
| worker:mac          | 188 |  466 |  +3 |  185.2 | leak×240；health×91                     |
| worker:nemo         | 523 |  956 |  +2 |  103.3 | leak×593；health×176                    |
| worker:nemo2        | 474 |  886 |  +1 |  105.0 | leak×564；health×162                    |
| worker:nemo3        | 443 |  683 |  +3 |   96.8 | leak×403；health×114                    |
| worker:oss20        |  90 |  200 |  +2 |  437.5 | no output written by tra×64；leak×62    |

endpoint 探活：local 🟢、laptop-4090 🔴、laptop-5090 🔴、desktop-3090 🟢、mac-m4max 🟢

（babel-pulse 常駐儀器自動快照）

## 2026-07-26T14:33:32+08:00（zh 總數 868）

| 語言 | fresh | stale | missing | 覆蓋率 | Δfresh | Δmissing |
| ---- | ----: | ----: | ------: | -----: | -----: | -------: |
| en   |   721 |   110 |      37 |  95.7% |      · |        · |
| ja   |   723 |   136 |       9 |  99.0% |      · |        · |
| ko   |   720 |   142 |       6 |  99.3% |     +1 |       -1 |
| es   |   724 |   140 |       4 |  99.5% |     +1 |       -1 |
| fr   |   725 |   139 |       4 |  99.5% |     +1 |       -1 |
| vi   |   160 |    17 |     691 |  20.4% |     +3 |       -3 |
| id   |   280 |    11 |     577 |  33.5% |     +4 |       -4 |
| pt   |   460 |    13 |     395 |  54.5% |     +2 |       -2 |
| hi   |   354 |     8 |     506 |  41.7% |     +4 |       -4 |
| ar   |   326 |     2 |     540 |  37.8% |     +3 |       -3 |
| ru   |   349 |     2 |     517 |  40.4% |     +2 |       -2 |

總缺口（stale+missing）：**4006**（▼21 vs 上一筆）

**節點／worker**（ok/fail 為累計；Δ為對上一筆）

| 節點                |  ok | fail | Δok | 平均秒 | 主要 fail                               |
| ------------------- | --: | ---: | --: | -----: | --------------------------------------- |
| fleet:desktop-3090  |  56 |  325 |   · |      — | health×123；verify=1×102                |
| fleet:laptop-4090   |  27 |  137 |   · |      — | health×83；verify=None×24               |
| worker:d3090        |  23 |   60 |   · |  931.2 | no output written by tra×40；leak×9     |
| worker:desktop30901 |  21 |   19 |   · |  624.0 | health×10；leak×4                       |
| worker:desktop30902 |  16 |   23 |   · |  613.5 | health×10；verify=1×6                   |
| worker:gemma31      |   1 |   34 |   · |    2.2 | no output written by tra×34             |
| worker:l4090        |  85 |  194 |   · |  151.0 | no output written by tra×106；leak×32   |
| worker:laguna       | 166 |  223 |  +1 |  224.7 | no output written by tra×126；health×36 |
| worker:laguna2      |  17 |   15 |  +2 |  293.8 | no output written by tra×12；health×2   |
| worker:laptop40901  |  17 |   14 |   · |  874.1 | health×9；leak×2                        |
| worker:laptop40902  |  15 |   15 |   · |  894.2 | leak×6；health×5                        |
| worker:mac          | 190 |  472 |  +2 |  186.8 | leak×243；health×93                     |
| worker:nemo         | 528 |  972 |  +5 |  103.4 | leak×597；health×182                    |
| worker:nemo2        | 478 |  899 |  +4 |  104.8 | leak×568；health×165                    |
| worker:nemo3        | 446 |  693 |  +3 |   96.9 | leak×406；health×118                    |
| worker:oss20        |  91 |  201 |  +1 |  446.5 | no output written by tra×65；leak×62    |

endpoint 探活：local 🟢、laptop-4090 🔴、laptop-5090 🔴、desktop-3090 🟢、mac-m4max 🟢

（babel-pulse 常駐儀器自動快照）

## 2026-07-26T14:48:57+08:00（zh 總數 868）

| 語言 | fresh | stale | missing | 覆蓋率 | Δfresh | Δmissing |
| ---- | ----: | ----: | ------: | -----: | -----: | -------: |
| en   |   721 |   110 |      37 |  95.7% |      · |        · |
| ja   |   724 |   136 |       8 |  99.1% |     +1 |       -1 |
| ko   |   722 |   142 |       4 |  99.5% |     +2 |       -2 |
| es   |   725 |   139 |       4 |  99.5% |     +1 |        · |
| fr   |   725 |   139 |       4 |  99.5% |      · |        · |
| vi   |   162 |    17 |     689 |  20.6% |     +2 |       -2 |
| id   |   283 |    11 |     574 |  33.9% |     +3 |       -3 |
| pt   |   460 |    13 |     395 |  54.5% |      · |        · |
| hi   |   356 |     8 |     504 |  41.9% |     +2 |       -2 |
| ar   |   327 |     2 |     539 |  37.9% |     +1 |       -1 |
| ru   |   351 |     2 |     515 |  40.7% |     +2 |       -2 |

總缺口（stale+missing）：**3992**（▼14 vs 上一筆）

**節點／worker**（ok/fail 為累計；Δ為對上一筆）

| 節點                |  ok | fail | Δok | 平均秒 | 主要 fail                               |
| ------------------- | --: | ---: | --: | -----: | --------------------------------------- |
| fleet:desktop-3090  |  56 |  325 |   · |      — | health×123；verify=1×102                |
| fleet:laptop-4090   |  27 |  137 |   · |      — | health×83；verify=None×24               |
| worker:d3090        |  23 |   61 |   · |  931.2 | no output written by tra×41；leak×9     |
| worker:desktop30901 |  21 |   19 |   · |  624.0 | health×10；leak×4                       |
| worker:desktop30902 |  16 |   23 |   · |  613.5 | health×10；verify=1×6                   |
| worker:gemma31      |   1 |   34 |   · |    2.2 | no output written by tra×34             |
| worker:l4090        |  85 |  194 |   · |  151.0 | no output written by tra×106；leak×32   |
| worker:laguna       | 166 |  224 |   · |  224.7 | no output written by tra×127；health×36 |
| worker:laguna2      |  18 |   16 |  +1 |  291.3 | no output written by tra×13；health×2   |
| worker:laptop40901  |  17 |   14 |   · |  874.1 | health×9；leak×2                        |
| worker:laptop40902  |  15 |   15 |   · |  894.2 | leak×6；health×5                        |
| worker:mac          | 191 |  473 |  +1 |  187.5 | leak×244；health×93                     |
| worker:nemo         | 532 |  977 |  +4 |  103.2 | leak×598；health×184                    |
| worker:nemo2        | 482 |  900 |  +4 |  105.8 | leak×568；health×166                    |
| worker:nemo3        | 447 |  700 |  +1 |   97.0 | leak×411；health×119                    |
| worker:oss20        |  92 |  202 |  +1 |  455.6 | no output written by tra×66；leak×62    |

endpoint 探活：local 🟢、laptop-4090 🔴、laptop-5090 🔴、desktop-3090 🟢、mac-m4max 🟢

（babel-pulse 常駐儀器自動快照）

## 2026-07-26T15:04:26+08:00（zh 總數 868）

| 語言 | fresh | stale | missing | 覆蓋率 | Δfresh | Δmissing |
| ---- | ----: | ----: | ------: | -----: | -----: | -------: |
| en   |   721 |   110 |      37 |  95.7% |      · |        · |
| ja   |   724 |   136 |       8 |  99.1% |      · |        · |
| ko   |   722 |   142 |       4 |  99.5% |      · |        · |
| es   |   724 |   140 |       4 |  99.5% |     -1 |        · |
| fr   |   726 |   139 |       3 |  99.7% |     +1 |       -1 |
| vi   |   162 |    17 |     689 |  20.6% |      · |        · |
| id   |   284 |    11 |     573 |  34.0% |     +1 |       -1 |
| pt   |   462 |    13 |     393 |  54.7% |     +2 |       -2 |
| hi   |   356 |     8 |     504 |  41.9% |      · |        · |
| ar   |   329 |     2 |     537 |  38.1% |     +2 |       -2 |
| ru   |   353 |     2 |     513 |  40.9% |     +2 |       -2 |

總缺口（stale+missing）：**3985**（▼7 vs 上一筆）

**節點／worker**（ok/fail 為累計；Δ為對上一筆）

| 節點                |  ok | fail | Δok | 平均秒 | 主要 fail                               |
| ------------------- | --: | ---: | --: | -----: | --------------------------------------- |
| fleet:desktop-3090  |  56 |  325 |   · |      — | health×123；verify=1×102                |
| fleet:laptop-4090   |  27 |  137 |   · |      — | health×83；verify=None×24               |
| worker:d3090        |  23 |   61 |   · |  931.2 | no output written by tra×41；leak×9     |
| worker:desktop30901 |  21 |   19 |   · |  624.0 | health×10；leak×4                       |
| worker:desktop30902 |  16 |   23 |   · |  613.5 | health×10；verify=1×6                   |
| worker:gemma31      |   1 |   34 |   · |    2.2 | no output written by tra×34             |
| worker:l4090        |  85 |  194 |   · |  151.0 | no output written by tra×106；leak×32   |
| worker:laguna       | 166 |  224 |   · |  224.7 | no output written by tra×127；health×36 |
| worker:laguna2      |  18 |   18 |   · |  291.3 | no output written by tra×14；health×2   |
| worker:laptop40901  |  17 |   14 |   · |  874.1 | health×9；leak×2                        |
| worker:laptop40902  |  15 |   15 |   · |  894.2 | leak×6；health×5                        |
| worker:mac          | 193 |  478 |  +2 |  186.6 | leak×247；health×93                     |
| worker:nemo         | 533 |  985 |  +1 |  103.2 | leak×602；health×187                    |
| worker:nemo2        | 484 |  903 |  +2 |  105.7 | leak×569；health×166                    |
| worker:nemo3        | 448 |  706 |  +1 |   96.9 | leak×413；health×121                    |
| worker:oss20        |  92 |  204 |   · |  455.6 | no output written by tra×67；leak×62    |

endpoint 探活：local 🟢、laptop-4090 🔴、laptop-5090 🔴、desktop-3090 🟢、mac-m4max 🟢

（babel-pulse 常駐儀器自動快照）

## 2026-07-26T15:20:00+08:00（zh 總數 868）

| 語言 | fresh | stale | missing | 覆蓋率 | Δfresh | Δmissing |
| ---- | ----: | ----: | ------: | -----: | -----: | -------: |
| en   |   721 |   110 |      37 |  95.7% |      · |        · |
| ja   |   725 |   135 |       8 |  99.1% |     +1 |        · |
| ko   |   723 |   141 |       4 |  99.5% |     +1 |        · |
| es   |   724 |   140 |       4 |  99.5% |      · |        · |
| fr   |   727 |   139 |       2 |  99.8% |     +1 |       -1 |
| vi   |   166 |    17 |     685 |  21.1% |     +4 |       -4 |
| id   |   284 |    11 |     573 |  34.0% |      · |        · |
| pt   |   463 |    13 |     392 |  54.8% |     +1 |       -1 |
| hi   |   357 |     8 |     503 |  42.1% |     +1 |       -1 |
| ar   |   332 |     2 |     534 |  38.5% |     +3 |       -3 |
| ru   |   355 |     2 |     511 |  41.1% |     +2 |       -2 |

總缺口（stale+missing）：**3971**（▼14 vs 上一筆）

**節點／worker**（ok/fail 為累計；Δ為對上一筆）

| 節點                |  ok | fail | Δok | 平均秒 | 主要 fail                               |
| ------------------- | --: | ---: | --: | -----: | --------------------------------------- |
| fleet:desktop-3090  |  56 |  325 |   · |      — | health×123；verify=1×102                |
| fleet:laptop-4090   |  27 |  137 |   · |      — | health×83；verify=None×24               |
| worker:d3090        |  23 |   61 |   · |  931.2 | no output written by tra×41；leak×9     |
| worker:desktop30901 |  21 |   19 |   · |  624.0 | health×10；leak×4                       |
| worker:desktop30902 |  16 |   23 |   · |  613.5 | health×10；verify=1×6                   |
| worker:gemma31      |   1 |   34 |   · |    2.2 | no output written by tra×34             |
| worker:l4090        |  85 |  195 |   · |  151.0 | no output written by tra×106；health×33 |
| worker:laguna       | 168 |  224 |  +2 |  223.6 | no output written by tra×127；health×36 |
| worker:laguna2      |  20 |   19 |  +2 |  310.2 | no output written by tra×15；health×2   |
| worker:laptop40901  |  17 |   14 |   · |  874.1 | health×9；leak×2                        |
| worker:laptop40902  |  15 |   15 |   · |  894.2 | leak×6；health×5                        |
| worker:mac          | 195 |  479 |  +2 |  188.1 | leak×248；health×93                     |
| worker:nemo         | 536 |  991 |  +3 |  103.1 | leak×604；health×188                    |
| worker:nemo2        | 486 |  906 |  +2 |  106.0 | leak×569；health×167                    |
| worker:nemo3        | 452 |  712 |  +4 |   96.9 | leak×414；health×124                    |
| worker:oss20        |  92 |  207 |   · |  455.6 | no output written by tra×67；leak×63    |

endpoint 探活：local 🟢、laptop-4090 🟢、laptop-5090 🔴、desktop-3090 🟢、mac-m4max 🟢

（babel-pulse 常駐儀器自動快照）

## 2026-07-26T15:28:56+08:00（zh 總數 868）

| 語言 | fresh | stale | missing | 覆蓋率 | Δfresh | Δmissing |
| ---- | ----: | ----: | ------: | -----: | -----: | -------: |
| en   |   721 |   110 |      37 |  95.7% |      · |        · |
| ja   |   725 |   135 |       8 |  99.1% |      · |        · |
| ko   |   723 |   141 |       4 |  99.5% |      · |        · |
| es   |   724 |   140 |       4 |  99.5% |      · |        · |
| fr   |   727 |   139 |       2 |  99.8% |      · |        · |
| vi   |   166 |    17 |     685 |  21.1% |      · |        · |
| id   |   284 |    11 |     573 |  34.0% |      · |        · |
| pt   |   465 |    13 |     390 |  55.1% |     +2 |       -2 |
| hi   |   357 |     8 |     503 |  42.1% |      · |        · |
| ar   |   332 |     2 |     534 |  38.5% |      · |        · |
| ru   |   359 |     2 |     507 |  41.6% |     +4 |       -4 |

總缺口（stale+missing）：**3965**（▼6 vs 上一筆）

**節點／worker**（ok/fail 為累計；Δ為對上一筆）

| 節點                |  ok | fail | Δok | 平均秒 | 主要 fail                               |
| ------------------- | --: | ---: | --: | -----: | --------------------------------------- |
| fleet:desktop-3090  |  56 |  325 |   · |      — | health×123；verify=1×102                |
| fleet:laptop-4090   |  27 |  137 |   · |      — | health×83；verify=None×24               |
| worker:d3090        |  23 |   61 |   · |  931.2 | no output written by tra×41；leak×9     |
| worker:desktop30901 |  21 |   19 |   · |  624.0 | health×10；leak×4                       |
| worker:desktop30902 |  16 |   23 |   · |  613.5 | health×10；verify=1×6                   |
| worker:gemma31      |   1 |   34 |   · |    2.2 | no output written by tra×34             |
| worker:l4090        |  86 |  196 |  +1 |  153.3 | no output written by tra×107；health×33 |
| worker:laguna       | 168 |  225 |   · |  223.6 | no output written by tra×128；health×36 |
| worker:laguna2      |  20 |   20 |   · |  310.2 | no output written by tra×16；health×2   |
| worker:laptop40901  |  17 |   14 |   · |  874.1 | health×9；leak×2                        |
| worker:laptop40902  |  15 |   15 |   · |  894.2 | leak×6；health×5                        |
| worker:mac          | 195 |  479 |   · |  188.1 | leak×248；health×93                     |
| worker:nemo         | 538 |  994 |  +2 |  103.0 | leak×604；health×190                    |
| worker:nemo2        | 487 |  908 |  +1 |  106.2 | leak×570；health×168                    |
| worker:nemo3        | 453 |  717 |  +1 |   97.0 | leak×415；health×126                    |
| worker:oss20        |  92 |  208 |   · |  455.6 | no output written by tra×67；leak×63    |

endpoint 探活：local 🟢、laptop-4090 🟢、laptop-5090 🔴、desktop-3090 🟢、mac-m4max 🟢

（babel-pulse 常駐儀器自動快照）

## 2026-07-26T15:35:32+08:00（zh 總數 868）

| 語言 | fresh | stale | missing | 覆蓋率 | Δfresh | Δmissing |
| ---- | ----: | ----: | ------: | -----: | -----: | -------: |
| en   |   721 |   110 |      37 |  95.7% |      · |        · |
| ja   |   725 |   135 |       8 |  99.1% |      · |        · |
| ko   |   723 |   141 |       4 |  99.5% |      · |        · |
| es   |   724 |   140 |       4 |  99.5% |      · |        · |
| fr   |   727 |   139 |       2 |  99.8% |      · |        · |
| vi   |   168 |    17 |     683 |  21.3% |     +2 |       -2 |
| id   |   285 |    11 |     572 |  34.1% |     +1 |       -1 |
| pt   |   467 |    13 |     388 |  55.3% |     +2 |       -2 |
| hi   |   358 |     8 |     502 |  42.2% |     +1 |       -1 |
| ar   |   333 |     2 |     533 |  38.6% |     +1 |       -1 |
| ru   |   360 |     2 |     506 |  41.7% |     +1 |       -1 |

總缺口（stale+missing）：**3957**（▼8 vs 上一筆）

**節點／worker**（ok/fail 為累計；Δ為對上一筆）

| 節點                |  ok | fail | Δok | 平均秒 | 主要 fail                               |
| ------------------- | --: | ---: | --: | -----: | --------------------------------------- |
| fleet:desktop-3090  |  56 |  325 |   · |      — | health×123；verify=1×102                |
| fleet:laptop-4090   |  27 |  137 |   · |      — | health×83；verify=None×24               |
| worker:d3090        |  23 |   61 |   · |  931.2 | no output written by tra×41；leak×9     |
| worker:desktop30901 |  21 |   19 |   · |  624.0 | health×10；leak×4                       |
| worker:desktop30902 |  16 |   23 |   · |  613.5 | health×10；verify=1×6                   |
| worker:gemma31      |   1 |   34 |   · |    2.2 | no output written by tra×34             |
| worker:l4090        |  86 |  198 |   · |  153.3 | no output written by tra×107；leak×33   |
| worker:laguna       | 170 |  226 |  +2 |  221.9 | no output written by tra×128；health×36 |
| worker:laguna2      |  20 |   20 |   · |  310.2 | no output written by tra×16；health×2   |
| worker:laptop40901  |  17 |   14 |   · |  874.1 | health×9；leak×2                        |
| worker:laptop40902  |  15 |   15 |   · |  894.2 | leak×6；health×5                        |
| worker:mac          | 195 |  481 |   · |  188.1 | leak×248；health×94                     |
| worker:nemo         | 538 |  997 |   · |  103.0 | leak×607；health×190                    |
| worker:nemo2        | 490 |  910 |  +3 |  105.9 | leak×571；health×169                    |
| worker:nemo3        | 455 |  718 |  +2 |   97.0 | leak×416；health×126                    |
| worker:nemo4        |   0 |    1 |   — |      — | leak×1                                  |
| worker:oss20        |  92 |  208 |   · |  455.6 | no output written by tra×67；leak×63    |

endpoint 探活：local 🟢、laptop-4090 🟢、laptop-5090 🔴、desktop-3090 🟢、mac-m4max 🟢

（babel-pulse 常駐儀器自動快照）

## 2026-07-26T15:50:52+08:00（zh 總數 868）

| 語言 | fresh | stale | missing | 覆蓋率 | Δfresh | Δmissing |
| ---- | ----: | ----: | ------: | -----: | -----: | -------: |
| en   |   721 |   110 |      37 |  95.7% |      · |        · |
| ja   |   726 |   134 |       8 |  99.1% |     +1 |        · |
| ko   |   723 |   141 |       4 |  99.5% |      · |        · |
| es   |   724 |   140 |       4 |  99.5% |      · |        · |
| fr   |   727 |   139 |       2 |  99.8% |      · |        · |
| vi   |   168 |    17 |     683 |  21.3% |      · |        · |
| id   |   285 |    11 |     572 |  34.1% |      · |        · |
| pt   |   469 |    13 |     386 |  55.5% |     +2 |       -2 |
| hi   |   360 |     8 |     500 |  42.4% |     +2 |       -2 |
| ar   |   335 |     2 |     531 |  38.8% |     +2 |       -2 |
| ru   |   362 |     2 |     504 |  41.9% |     +2 |       -2 |

總缺口（stale+missing）：**3948**（▼9 vs 上一筆）

**節點／worker**（ok/fail 為累計；Δ為對上一筆）

| 節點                |  ok | fail | Δok | 平均秒 | 主要 fail                               |
| ------------------- | --: | ---: | --: | -----: | --------------------------------------- |
| fleet:desktop-3090  |  56 |  325 |   · |      — | health×123；verify=1×102                |
| fleet:laptop-4090   |  27 |  137 |   · |      — | health×83；verify=None×24               |
| worker:d3090        |  23 |   62 |   · |  931.2 | no output written by tra×41；leak×9     |
| worker:desktop30901 |  21 |   19 |   · |  624.0 | health×10；leak×4                       |
| worker:desktop30902 |  16 |   23 |   · |  613.5 | health×10；verify=1×6                   |
| worker:gemma31      |   1 |   34 |   · |    2.2 | no output written by tra×34             |
| worker:l4090        |  86 |  202 |   · |  153.3 | no output written by tra×109；leak×34   |
| worker:laguna       | 170 |  227 |   · |  221.9 | no output written by tra×129；health×36 |
| worker:laguna2      |  20 |   21 |   · |  310.2 | no output written by tra×17；health×2   |
| worker:laguna3      |   0 |    1 |   — |      — | no output written by tra×1              |
| worker:laptop40901  |  17 |   14 |   · |  874.1 | health×9；leak×2                        |
| worker:laptop40902  |  15 |   15 |   · |  894.2 | leak×6；health×5                        |
| worker:mac          | 195 |  485 |   · |  188.1 | leak×251；health×95                     |
| worker:nemo         | 541 | 1005 |  +3 |  102.8 | leak×609；health×194                    |
| worker:nemo2        | 494 |  915 |  +4 |  105.8 | leak×574；health×169                    |
| worker:nemo3        | 456 |  725 |  +1 |   97.0 | leak×417；health×129                    |
| worker:nemo4        |   0 |    9 |   · |      — | leak×5；health×2                        |
| worker:oss20        |  92 |  208 |   · |  455.6 | no output written by tra×67；leak×63    |

endpoint 探活：local 🟢、laptop-4090 🟢、laptop-5090 🔴、desktop-3090 🟢、mac-m4max 🟢

（babel-pulse 常駐儀器自動快照）

## 2026-07-26T16:06:38+08:00（zh 總數 868）

| 語言 | fresh | stale | missing | 覆蓋率 | Δfresh | Δmissing |
| ---- | ----: | ----: | ------: | -----: | -----: | -------: |
| en   |   721 |   110 |      37 |  95.7% |      · |        · |
| ja   |   726 |   134 |       8 |  99.1% |      · |        · |
| ko   |   724 |   140 |       4 |  99.5% |     +1 |        · |
| es   |   724 |   140 |       4 |  99.5% |      · |        · |
| fr   |   727 |   139 |       2 |  99.8% |      · |        · |
| vi   |   168 |    17 |     683 |  21.3% |      · |        · |
| id   |   285 |    11 |     572 |  34.1% |      · |        · |
| pt   |   469 |    13 |     386 |  55.5% |      · |        · |
| hi   |   360 |     8 |     500 |  42.4% |      · |        · |
| ar   |   338 |     2 |     528 |  39.2% |     +3 |       -3 |
| ru   |   362 |     2 |     504 |  41.9% |      · |        · |

總缺口（stale+missing）：**3944**（▼4 vs 上一筆）

**節點／worker**（ok/fail 為累計；Δ為對上一筆）

| 節點                |  ok | fail | Δok | 平均秒 | 主要 fail                               |
| ------------------- | --: | ---: | --: | -----: | --------------------------------------- |
| fleet:desktop-3090  |  56 |  325 |   · |      — | health×123；verify=1×102                |
| fleet:laptop-4090   |  27 |  137 |   · |      — | health×83；verify=None×24               |
| worker:d3090        |  23 |   62 |   · |  931.2 | no output written by tra×41；leak×9     |
| worker:desktop30901 |  21 |   19 |   · |  624.0 | health×10；leak×4                       |
| worker:desktop30902 |  16 |   23 |   · |  613.5 | health×10；verify=1×6                   |
| worker:gemma31      |   1 |   34 |   · |    2.2 | no output written by tra×34             |
| worker:l4090        |  89 |  205 |  +3 |  153.4 | no output written by tra×110；health×36 |
| worker:laguna       | 170 |  229 |   · |  221.9 | no output written by tra×131；health×36 |
| worker:laguna2      |  20 |   24 |   · |  310.2 | no output written by tra×19；health×3   |
| worker:laguna3      |   0 |    2 |   · |      — | no output written by tra×2              |
| worker:laptop40901  |  17 |   14 |   · |  874.1 | health×9；leak×2                        |
| worker:laptop40902  |  15 |   15 |   · |  894.2 | leak×6；health×5                        |
| worker:mac          | 195 |  489 |   · |  188.1 | leak×254；health×96                     |
| worker:nemo         | 542 | 1009 |  +1 |  103.1 | leak×611；health×194                    |
| worker:nemo2        | 494 |  921 |   · |  105.8 | leak×578；health×169                    |
| worker:nemo3        | 457 |  732 |  +1 |   97.2 | leak×420；health×131                    |
| worker:nemo4        |   1 |   13 |  +1 |  124.4 | leak×5；health×4                        |
| worker:oss20        |  92 |  208 |   · |  455.6 | no output written by tra×67；leak×63    |

endpoint 探活：local 🟢、laptop-4090 🟢、laptop-5090 🔴、desktop-3090 🟢、mac-m4max 🟢

（babel-pulse 常駐儀器自動快照）
<<<<<<< HEAD

## 2026-07-26T16:22:41+08:00（zh 總數 868）

| 語言 | fresh | stale | missing | 覆蓋率 | Δfresh | Δmissing |
| ---- | ----: | ----: | ------: | -----: | -----: | -------: |
| en   |   721 |   110 |      37 |  95.7% |      · |        · |
| ja   |   726 |   134 |       8 |  99.1% |      · |        · |
| ko   |   724 |   140 |       4 |  99.5% |      · |        · |
| es   |   725 |   139 |       4 |  99.5% |     +1 |        · |
| fr   |   728 |   138 |       2 |  99.8% |     +1 |        · |
| vi   |   169 |    17 |     682 |  21.4% |     +1 |       -1 |
| id   |   286 |    11 |     571 |  34.2% |     +1 |       -1 |
| pt   |   469 |    13 |     386 |  55.5% |      · |        · |
| hi   |   361 |     8 |     499 |  42.5% |     +1 |       -1 |
| ar   |   339 |     2 |     527 |  39.3% |     +1 |       -1 |
| ru   |   364 |     2 |     502 |  42.2% |     +2 |       -2 |

總缺口（stale+missing）：**3936**（▼8 vs 上一筆）

**節點／worker**（ok/fail 為累計；Δ為對上一筆）

| 節點                |  ok | fail | Δok | 平均秒 | 主要 fail                               |
| ------------------- | --: | ---: | --: | -----: | --------------------------------------- |
| fleet:desktop-3090  |  56 |  325 |   · |      — | health×123；verify=1×102                |
| fleet:laptop-4090   |  27 |  137 |   · |      — | health×83；verify=None×24               |
| worker:d3090        |  24 |   62 |  +1 |  967.4 | no output written by tra×41；leak×9     |
| worker:desktop30901 |  21 |   19 |   · |  624.0 | health×10；leak×4                       |
| worker:desktop30902 |  16 |   23 |   · |  613.5 | health×10；verify=1×6                   |
| worker:gemma31      |   1 |   34 |   · |    2.2 | no output written by tra×34             |
| worker:l4090        |  97 |  208 |  +8 |  147.9 | no output written by tra×110；health×37 |
| worker:laguna       | 170 |  229 |   · |  221.9 | no output written by tra×131；health×36 |
| worker:laguna2      |  21 |   26 |  +1 |  305.1 | no output written by tra×20；health×3   |
| worker:laguna3      |   0 |    3 |   · |      — | no output written by tra×3              |
| worker:laptop40901  |  17 |   14 |   · |  874.1 | health×9；leak×2                        |
| worker:laptop40902  |  15 |   15 |   · |  894.2 | leak×6；health×5                        |
| worker:mac          | 197 |  490 |  +2 |  189.3 | leak×255；health×96                     |
| worker:nemo         | 542 | 1014 |   · |  103.1 | leak×612；health×195                    |
| worker:nemo2        | 495 |  926 |  +1 |  105.8 | leak×579；health×170                    |
| worker:nemo3        | 458 |  735 |  +1 |   97.8 | leak×421；health×132                    |
| worker:nemo4        |   3 |   19 |  +2 |  118.2 | leak×6；health×6                        |
| worker:oss20        |  92 |  208 |   · |  455.6 | no output written by tra×67；leak×63    |

endpoint 探活：local 🟢、laptop-4090 🟢、laptop-5090 🔴、desktop-3090 🟢、mac-m4max 🟢

（babel-pulse 常駐儀器自動快照）

## 2026-07-26T16:30:42+08:00（zh 總數 868）

| 語言 | fresh | stale | missing | 覆蓋率 | Δfresh | Δmissing |
| ---- | ----: | ----: | ------: | -----: | -----: | -------: |
| en   |   721 |   110 |      37 |  95.7% |      · |        · |
| ja   |   726 |   134 |       8 |  99.1% |      · |        · |
| ko   |   724 |   140 |       4 |  99.5% |      · |        · |
| es   |   725 |   139 |       4 |  99.5% |      · |        · |
| fr   |   729 |   137 |       2 |  99.8% |     +1 |        · |
| vi   |   170 |    17 |     681 |  21.5% |     +1 |       -1 |
| id   |   286 |    11 |     571 |  34.2% |      · |        · |
| pt   |   470 |    13 |     385 |  55.6% |     +1 |       -1 |
| hi   |   361 |     8 |     499 |  42.5% |      · |        · |
| ar   |   340 |     2 |     526 |  39.4% |     +1 |       -1 |
| ru   |   367 |     2 |     499 |  42.5% |     +3 |       -3 |

總缺口（stale+missing）：**3929**（▼7 vs 上一筆）

**節點／worker**（ok/fail 為累計；Δ為對上一筆）

| 節點                |  ok | fail | Δok | 平均秒 | 主要 fail                               |
| ------------------- | --: | ---: | --: | -----: | --------------------------------------- |
| fleet:desktop-3090  |  56 |  325 |   · |      — | health×123；verify=1×102                |
| fleet:laptop-4090   |  27 |  137 |   · |      — | health×83；verify=None×24               |
| worker:d3090        |  24 |   62 |   · |  967.4 | no output written by tra×41；leak×9     |
| worker:desktop30901 |  21 |   19 |   · |  624.0 | health×10；leak×4                       |
| worker:desktop30902 |  16 |   23 |   · |  613.5 | health×10；verify=1×6                   |
| worker:gemma31      |   1 |   34 |   · |    2.2 | no output written by tra×34             |
| worker:l4090        |  97 |  211 |   · |  147.9 | no output written by tra×110；health×40 |
| worker:laguna       | 170 |  229 |   · |  221.9 | no output written by tra×131；health×36 |
| worker:laguna2      |  22 |   26 |  +1 |  314.1 | no output written by tra×20；health×3   |
| worker:laguna3      |   0 |    3 |   · |      — | no output written by tra×3              |
| worker:laptop40901  |  17 |   14 |   · |  874.1 | health×9；leak×2                        |
| worker:laptop40902  |  15 |   15 |   · |  894.2 | leak×6；health×5                        |
| worker:mac          | 197 |  490 |   · |  189.3 | leak×255；health×96                     |
| worker:nemo         | 543 | 1017 |  +1 |  103.1 | leak×612；health×197                    |
| worker:nemo2        | 496 |  929 |  +1 |  105.8 | leak×579；health×172                    |
| worker:nemo3        | 459 |  736 |  +1 |   97.7 | leak×421；health×132                    |
| worker:nemo4        |   4 |   19 |  +1 |  103.7 | leak×6；health×6                        |
| worker:oss20        |  92 |  208 |   · |  455.6 | no output written by tra×67；leak×63    |

endpoint 探活：local 🟢、laptop-4090 🟢、laptop-5090 🔴、desktop-3090 🟢、mac-m4max 🟢

# （babel-pulse 常駐儀器自動快照）

> > > > > > > origin/main

## 2026-07-26T16:32:52+08:00（zh 總數 868）

| 語言 | fresh | stale | missing | 覆蓋率 | Δfresh | Δmissing |
| ---- | ----: | ----: | ------: | -----: | -----: | -------: |
| en   |   721 |   110 |      37 |  95.7% |      · |        · |
| ja   |   726 |   134 |       8 |  99.1% |      · |        · |
| ko   |   725 |   139 |       4 |  99.5% |     +1 |        · |
| es   |   725 |   139 |       4 |  99.5% |      · |        · |
| fr   |   729 |   137 |       2 |  99.8% |      · |        · |
| vi   |   170 |    17 |     681 |  21.5% |      · |        · |
| id   |   287 |    11 |     570 |  34.3% |     +1 |       -1 |
| pt   |   471 |    13 |     384 |  55.8% |     +1 |       -1 |
| hi   |   361 |     8 |     499 |  42.5% |      · |        · |
| ar   |   341 |     2 |     525 |  39.5% |     +1 |       -1 |
| ru   |   367 |     2 |     499 |  42.5% |      · |        · |

總缺口（stale+missing）：**3925**（▼4 vs 上一筆）

**節點／worker**（ok/fail 為累計；Δ為對上一筆）

| 節點                |  ok | fail | Δok | 平均秒 | 主要 fail                               |
| ------------------- | --: | ---: | --: | -----: | --------------------------------------- |
| fleet:desktop-3090  |  56 |  325 |   · |      — | health×123；verify=1×102                |
| fleet:laptop-4090   |  27 |  137 |   · |      — | health×83；verify=None×24               |
| worker:d3090        |  24 |   62 |   · |  967.4 | no output written by tra×41；leak×9     |
| worker:desktop30901 |  21 |   19 |   · |  624.0 | health×10；leak×4                       |
| worker:desktop30902 |  16 |   23 |   · |  613.5 | health×10；verify=1×6                   |
| worker:gemma31      |   1 |   34 |   · |    2.2 | no output written by tra×34             |
| worker:l4090        |  99 |  211 |  +2 |  146.9 | no output written by tra×110；health×40 |
| worker:laguna       | 171 |  229 |  +1 |  221.9 | no output written by tra×131；health×36 |
| worker:laguna2      |  22 |   26 |   · |  314.1 | no output written by tra×20；health×3   |
| worker:laguna3      |   0 |    3 |   · |      — | no output written by tra×3              |
| worker:laptop40901  |  17 |   14 |   · |  874.1 | health×9；leak×2                        |
| worker:laptop40902  |  15 |   15 |   · |  894.2 | leak×6；health×5                        |
| worker:mac          | 197 |  490 |   · |  189.3 | leak×255；health×96                     |
| worker:nemo         | 543 | 1017 |   · |  103.1 | leak×612；health×197                    |
| worker:nemo2        | 497 |  929 |  +1 |  105.9 | leak×579；health×172                    |
| worker:nemo3        | 461 |  736 |  +2 |   97.6 | leak×421；health×132                    |
| worker:nemo4        |   4 |   19 |   · |  103.7 | leak×6；health×6                        |
| worker:oss20        |  92 |  208 |   · |  455.6 | no output written by tra×67；leak×63    |

endpoint 探活：local 🟢、laptop-4090 🟢、laptop-5090 🔴、desktop-3090 🟢、mac-m4max 🟢

（babel-pulse 常駐儀器自動快照）

## 2026-07-26T16:38:30+08:00（zh 總數 868）

| 語言 | fresh | stale | missing | 覆蓋率 | Δfresh | Δmissing |
| ---- | ----: | ----: | ------: | -----: | -----: | -------: |
| en   |   721 |   110 |      37 |  95.7% |      · |        · |
| ja   |   726 |   134 |       8 |  99.1% |      · |        · |
| ko   |   725 |   139 |       4 |  99.5% |      · |        · |
| es   |   725 |   139 |       4 |  99.5% |      · |        · |
| fr   |   729 |   137 |       2 |  99.8% |      · |        · |
| vi   |   171 |    17 |     680 |  21.7% |     +1 |       -1 |
| id   |   287 |    11 |     570 |  34.3% |      · |        · |
| pt   |   471 |    13 |     384 |  55.8% |      · |        · |
| hi   |   361 |     8 |     499 |  42.5% |      · |        · |
| ar   |   341 |     2 |     525 |  39.5% |      · |        · |
| ru   |   369 |     2 |     497 |  42.7% |     +2 |       -2 |

總缺口（stale+missing）：**3922**（▼3 vs 上一筆）

**節點／worker**（ok/fail 為累計；Δ為對上一筆）

| 節點                |  ok | fail | Δok | 平均秒 | 主要 fail                               |
| ------------------- | --: | ---: | --: | -----: | --------------------------------------- |
| fleet:desktop-3090  |  56 |  325 |   · |      — | health×123；verify=1×102                |
| fleet:laptop-4090   |  27 |  137 |   · |      — | health×83；verify=None×24               |
| worker:d3090        |  24 |   62 |   · |  967.4 | no output written by tra×41；leak×9     |
| worker:desktop30901 |  21 |   19 |   · |  624.0 | health×10；leak×4                       |
| worker:desktop30902 |  16 |   23 |   · |  613.5 | health×10；verify=1×6                   |
| worker:gemma31      |   1 |   34 |   · |    2.2 | no output written by tra×34             |
| worker:l4090        |  99 |  212 |   · |  146.9 | no output written by tra×110；health×41 |
| worker:laguna       | 171 |  230 |   · |  221.9 | no output written by tra×131；health×36 |
| worker:laguna2      |  22 |   27 |   · |  314.1 | no output written by tra×20；health×4   |
| worker:laguna3      |   0 |    3 |   · |      — | no output written by tra×3              |
| worker:laptop40901  |  17 |   14 |   · |  874.1 | health×9；leak×2                        |
| worker:laptop40902  |  15 |   15 |   · |  894.2 | leak×6；health×5                        |
| worker:mac          | 197 |  491 |   · |  189.3 | leak×256；health×96                     |
| worker:nemo         | 543 | 1018 |   · |  103.1 | leak×612；health×197                    |
| worker:nemo2        | 497 |  931 |   · |  105.9 | leak×579；health×174                    |
| worker:nemo3        | 463 |  737 |  +2 |   97.8 | leak×422；health×132                    |
| worker:nemo4        |   4 |   21 |   · |  103.7 | leak×7；health×7                        |
| worker:oss20        |  92 |  208 |   · |  455.6 | no output written by tra×67；leak×63    |

endpoint 探活：local 🟢、laptop-4090 🟢、laptop-5090 🔴、desktop-3090 🟢、mac-m4max 🟢

（babel-pulse 常駐儀器自動快照）

## 2026-07-26T16:40:29+08:00（zh 總數 868）

| 語言 | fresh | stale | missing | 覆蓋率 | Δfresh | Δmissing |
| ---- | ----: | ----: | ------: | -----: | -----: | -------: |
| en   |   721 |   110 |      37 |  95.7% |      · |        · |
| ja   |   726 |   134 |       8 |  99.1% |      · |        · |
| ko   |   725 |   139 |       4 |  99.5% |      · |        · |
| es   |   726 |   138 |       4 |  99.5% |     +1 |        · |
| fr   |   729 |   137 |       2 |  99.8% |      · |        · |
| vi   |   172 |    17 |     679 |  21.8% |     +1 |       -1 |
| id   |   287 |    11 |     570 |  34.3% |      · |        · |
| pt   |   471 |    13 |     384 |  55.8% |      · |        · |
| hi   |   361 |     8 |     499 |  42.5% |      · |        · |
| ar   |   342 |     2 |     524 |  39.6% |     +1 |       -1 |
| ru   |   369 |     2 |     497 |  42.7% |      · |        · |

總缺口（stale+missing）：**3919**（▼3 vs 上一筆）

**節點／worker**（ok/fail 為累計；Δ為對上一筆）

| 節點                |  ok | fail | Δok | 平均秒 | 主要 fail                               |
| ------------------- | --: | ---: | --: | -----: | --------------------------------------- |
| fleet:desktop-3090  |  56 |  325 |   · |      — | health×123；verify=1×102                |
| fleet:laptop-4090   |  27 |  137 |   · |      — | health×83；verify=None×24               |
| worker:d3090        |  24 |   62 |   · |  967.4 | no output written by tra×41；leak×9     |
| worker:desktop30901 |  21 |   19 |   · |  624.0 | health×10；leak×4                       |
| worker:desktop30902 |  16 |   23 |   · |  613.5 | health×10；verify=1×6                   |
| worker:gemma31      |   1 |   34 |   · |    2.2 | no output written by tra×34             |
| worker:l4090        |  99 |  212 |   · |  146.9 | no output written by tra×110；health×41 |
| worker:laguna       | 171 |  230 |   · |  221.9 | no output written by tra×131；health×36 |
| worker:laguna2      |  22 |   27 |   · |  314.1 | no output written by tra×20；health×4   |
| worker:laguna3      |   1 |    3 |  +1 |  104.2 | no output written by tra×3              |
| worker:laptop40901  |  17 |   14 |   · |  874.1 | health×9；leak×2                        |
| worker:laptop40902  |  15 |   15 |   · |  894.2 | leak×6；health×5                        |
| worker:mac          | 197 |  491 |   · |  189.3 | leak×256；health×96                     |
| worker:nemo         | 543 | 1019 |   · |  103.1 | leak×612；health×198                    |
| worker:nemo2        | 498 |  931 |  +1 |  105.9 | leak×579；health×174                    |
| worker:nemo3        | 463 |  738 |   · |   97.8 | leak×422；health×133                    |
| worker:nemo4        |   4 |   22 |   · |  103.7 | health×8；leak×7                        |
| worker:oss20        |  92 |  208 |   · |  455.6 | no output written by tra×67；leak×63    |

endpoint 探活：local 🟢、laptop-4090 🟢、laptop-5090 🔴、desktop-3090 🟢、mac-m4max 🟢

（babel-pulse 常駐儀器自動快照）
