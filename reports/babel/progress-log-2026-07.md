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
