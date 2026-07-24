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
