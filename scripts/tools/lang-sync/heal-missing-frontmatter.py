#!/usr/bin/env python3
"""heal-missing-frontmatter.py — 把譯文漏掉的 zh frontmatter 欄位補回去。

## 為什麼有這支

`verify-translation.py` 用 PASSTHROUGH／TRANSLATED 兩張**白名單**檢查
frontmatter，清單外的欄位掉了完全沒人知道。而白名單擋不住「新欄位誕生
之後沒人記得加進來」這件事——`sporeLinks`（2026-06-10 誕生）、
`researchReport`、`relatedDiary`、`imageSource`、`imageLicense` 五個欄位
都是後來長出來的，實測全站譯文 231-1187 篇都帶著它們，也就是說**慣例
是要帶**，掉了就是缺陷。

2026-07-31 一晚撞三次：Haiku 把 `[[wikilink]]` 拆成純文字、Sonnet 兩篇
各掉 `sporeLinks`，三個閘門全綠，全靠人工逐檔比對接住。手工做到第三次
就該變工具（本專案 §儀器化第 2 條：判準是次數不是難度）。

配套：`verify-translation.py` 已加 §14b「zh 有、譯文沒有的欄位」硬檢查
負責**偵測**；這支負責**修復**。偵測與修復分開，是因為偵測要能擋 commit，
修復要能批次跑（REFLEXES #58：儀器化 detection ≠ remediation）。

## 判準（刻意保守）

只補「zh 有值、譯文整個欄位不存在」的情況。**不動**已存在但值不同的欄位
（翻譯本來就會不同），**不刪**譯文多出來的欄位（EN_ONLY 那組本來就該多）。
插入位置固定在 `translatedFrom:` 之前，跟現有譯文的排版慣例一致。

用法：
  heal-missing-frontmatter.py --lang vi                # 掃某語言（dry-run）
  heal-missing-frontmatter.py --lang vi --apply        # 實際寫入
  heal-missing-frontmatter.py --file knowledge/vi/... --apply
  heal-missing-frontmatter.py --all                    # 全語言 dry-run 盤點
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent.parent.parent
KN = REPO / "knowledge"

# 譯文本來就該多出來的欄位，不算「漏」
TRANSLATION_ONLY = {
    "translatedFrom", "sourceCommitSha", "sourceContentHash",
    "sourceBodyHash", "translatedAt", "translatedFromInferred",
}


def split_fm(text: str):
    """回 (frontmatter 原文, body)；非 frontmatter 開頭回 (None, text)。"""
    if not text.startswith("---\n"):
        return None, text
    end = text.find("\n---", 3)
    if end == -1:
        return None, text
    return text[4:end + 1], text[end + 4:]


def top_level_keys(fm: str) -> set[str]:
    return set(re.findall(r"^([A-Za-z_][\w-]*):", fm, re.M))


def extract_block(fm: str, key: str) -> str | None:
    """抓出某個 top-level 欄位的完整區塊（含多行 list / nested map）。"""
    m = re.search(rf"^{re.escape(key)}:.*(?:\n(?:[ \t]+.*|)$)*", fm, re.M)
    if not m:
        return None
    block = m.group(0)
    # 去掉尾端連續空行，避免插入後產生空隙
    return block.rstrip("\n") + "\n"


def heal(zh_path: Path, tr_path: Path, apply: bool) -> list[str]:
    zh_fm, _ = split_fm(zh_path.read_text(encoding="utf-8"))
    tr_text = tr_path.read_text(encoding="utf-8")
    tr_fm, tr_body = split_fm(tr_text)
    if zh_fm is None or tr_fm is None:
        return []

    missing = [
        k for k in top_level_keys(zh_fm)
        if k not in top_level_keys(tr_fm) and k not in TRANSLATION_ONLY
    ]
    if not missing:
        return []

    blocks = []
    for k in sorted(missing):
        b = extract_block(zh_fm, k)
        if b:
            blocks.append(b)
    if not blocks:
        return []

    add = "".join(blocks)
    # 插在 translatedFrom 之前（metadata 區塊之前），對齊現有譯文排版
    if re.search(r"^translatedFrom:", tr_fm, re.M):
        new_fm = re.sub(r"^(translatedFrom:)", add + r"\1", tr_fm, count=1, flags=re.M)
    else:
        new_fm = tr_fm.rstrip("\n") + "\n" + add
    if apply:
        tr_path.write_text(f"---\n{new_fm}---{tr_body}", encoding="utf-8")
    return sorted(missing)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--lang")
    ap.add_argument("--file")
    ap.add_argument("--all", action="store_true")
    ap.add_argument("--apply", action="store_true")
    args = ap.parse_args()

    tmap = json.loads((KN / "_translations.json").read_text(encoding="utf-8"))
    if args.file:
        rel = str(Path(args.file).resolve().relative_to(KN))
        pairs = [(rel, tmap[rel])] if rel in tmap else []
    else:
        pairs = [
            (tp, zh) for tp, zh in tmap.items()
            if args.all or (args.lang and tp.startswith(f"{args.lang}/"))
        ]

    healed, per_field = 0, {}
    for tp, zh in sorted(pairs):
        zp, tpath = KN / zh, KN / tp
        if not zp.exists() or not tpath.exists():
            continue
        got = heal(zp, tpath, args.apply)
        if got:
            healed += 1
            for g in got:
                per_field[g] = per_field.get(g, 0) + 1
            if healed <= 15:
                print(f"  {'修復' if args.apply else '缺'} {tp} ← {got}")

    verb = "已修復" if args.apply else "待修復（dry-run，加 --apply 才寫入）"
    print(f"\n{verb}: {healed} 檔 / 掃描 {len(pairs)} 對")
    for f, n in sorted(per_field.items(), key=lambda x: -x[1]):
        print(f"   {f:18} {n} 檔")
    return 0


if __name__ == "__main__":
    sys.exit(main())
