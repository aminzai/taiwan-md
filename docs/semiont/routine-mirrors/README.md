# Routine mirror canonical（宿主機之間的對齊面）

Routine 的 cron 指令面住在宿主機的 `~/.claude/scheduled-tasks/{task}/SKILL.md`，
不在 git 裡——飛輪 2026-07-24 遷居 mouhouse-macmini 之後，這變成一個**看不見的
漂移面**：SSOT（[ROUTINE.md](../ROUTINE.md)）改了，但每台宿主機的 mirror 各自
停在搬過去那天的版本，而 cron session 讀的是 mirror。

2026-07-25 實例：babel 的 mirror 寫死 `en/ja/ko/es/fr` 五語，半個月內語言長到
11 個，新六語在無人察覺下整批漏掉——`routine-sync-check.py` 比對的是 name 與
description，內文寫死的語言清單它看不到。

本目錄放**已對齊 SSOT 的 mirror 正本**。宿主機 pull 之後跑：

```bash
bash scripts/tools/sync-routine-mirrors.sh          # 對照差異
bash scripts/tools/sync-routine-mirrors.sh --apply  # 覆寫本機 mirror
```

目前收錄的是薄殼化過的那幾條；其餘 18 條仍是各機手維（債，逐條收）。
