#!/usr/bin/env python3
"""relink-dead-by-zh-position.py — 譯文裡的死站內連結，照 zh 原文同一個位置的連結找回條目。

為什麼要這支（2026-09-29 babel-nightly）：`internal-link-check.py` 量得出譯文的死連結
（上線時 785 條，2026-09-28 夜班再量約 860 條），但沒有工具修得回去。死法幾乎全是同一種：
模型把 slug 當成可以翻譯的文字——ko `/people/허우샤오셴`、vi `/people/hàn-quốc-dự`、
en `/people/shen-pei-yang`、ja `/History/台湾民主化`。`cross_link_localizer` 只認得中文
slug 與已知譯文，看到這些編出來的 slug 一律判 no-translation 跳過，這是它該有的保守。

能救回來的線索在 zh 原文：譯文的站內連結跟 zh 的站內連結通常一條對一條、順序相同
（09-29 抽五篇 ko／vi／en／ja，數量全部相等、逐條對得上）。所以：

判準（保守，對不上就不動）：
  1. 站內連結的定義、「死」的定義一律用 `internal-link-check.py` 的（`check_file`），
     不另寫一份——兩套判準會分歧（BABEL-VORTEX-LOOP §儀器化第 1 條）
  2. 譯文與 zh 的站內連結（扣掉圖片與靜態資產）**數量必須相等**才配對；不等就整篇不動，
     因為順序一錯，會把連結接到另一個人身上，比 404 更糟（讀者不會發現）
  3. 配對到的兩條，**分類段必須相同**（不分大小寫、剝掉語言前綴）——第二道保險，擋住
     數量碰巧相等但中間插了一條、錯開一格的情況
  4. zh 那條自己也是死的 → 來源端問題，不動（修 zh 會讓十二語轉 stale，歸寫作席位）
  5. zh 那條活著 → 交給 `cross_link_localizer.localize_url` 換成該語言的網址；換出來的
     網址也要活著才採用。換不出來就保留 zh 原路徑（internal-link-check 的建議：至少讀得到
     中文版，好過 404）
  6. 只改死連結。活著但指向 zh 頁的連結是 OBSERVER-QUEUE #89 的範圍，不在這支

用法：
  python3 relink-dead-by-zh-position.py <譯文...>          # dry-run，列出每一條
  python3 relink-dead-by-zh-position.py --lang vi          # 整個語言 dry-run
  python3 relink-dead-by-zh-position.py --all --summary    # 全庫各語統計
  python3 relink-dead-by-zh-position.py --apply <譯文...>  # 只改這些檔
"""
from __future__ import annotations

import argparse
import re
import importlib.util
import sys
import urllib.parse
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import cross_link_localizer as C  # noqa: E402

_spec = importlib.util.spec_from_file_location("ilc", HERE / "internal-link-check.py")
ILC = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ILC)

REPO = ILC.REPO
KNOWLEDGE = ILC.KNOWLEDGE
LANGS = ILC.LANGS


def internal_links(text: str) -> list[tuple[int, int, str]]:
    """(start, end, url) — 跟 check_file 同一個 regex、同一個資產排除。"""
    out = []
    for m in ILC.LINK.finditer(text):
        url = m.group(1)
        if ILC.ASSET.match(url.split("#")[0].split("?")[0]):
            continue
        out.append((m.start(1), m.end(1), url))
    return out


_LOOSE_LINK = re.compile(r"\]\((/[^)]*)\)")
_WIKILINK = re.compile(r"\[\[[^\]]+\]\]")


def uncounted_links(text: str, n_strict: int, is_zh: bool) -> int:
    """嚴格 regex 看不到、但在另一側會變成站內連結的數量（2026-10-01 babel-nightly）。

    兩種會讓配對錯開一格而數量碰巧相等：網址帶空白（`/politics/2026 九合一選舉`，
    嚴格 regex 不收）、zh 的 [[wikilink]]（譯文會寫成一般 markdown 連結）。里長帳簿 pt
    版兩種各一：pt 與 zh 各數到 3 條「相等」，實際 pt 4 條、zh 3+1 條，第二條死連結
    被接到選舉條目，而分類段全是 politics，第二道保險擋不住。"""
    loose = sum(1 for m in _LOOSE_LINK.finditer(text)
                if not ILC.ASSET.match(m.group(1).split("#")[0].split("?")[0]))
    extra = loose - n_strict
    if is_zh:
        extra += len(_WIKILINK.findall(text))
    return extra


def category(url: str) -> str | None:
    seg = [urllib.parse.unquote(s) for s in url.split("#")[0].split("?")[0].strip("/").split("/") if s]
    if seg and seg[0] in LANGS:
        seg = seg[1:]
    return seg[0].lower() if seg else None


def plan_file(f: Path, idx, loc) -> tuple[list[tuple[str, str, str]], list[tuple[str, str]]]:
    """回傳 (fixes[(舊, 新, 依據)], skipped[(舊, 原因)])。"""
    dead = {u for u, _ in ILC.check_file(f, idx)}
    if not dead:
        return [], []
    src = ILC._zh_source(f)
    if not src or not src.exists():
        return [], [(u, "找不到 zh 來源") for u in sorted(dead)]
    t_text = f.read_text(encoding="utf-8")
    z_text = src.read_text(encoding="utf-8")
    t_links = internal_links(t_text)
    z_links = internal_links(z_text)
    t_extra = uncounted_links(t_text, len(t_links), is_zh=False)
    z_extra = uncounted_links(z_text, len(z_links), is_zh=True)
    if t_extra or z_extra:
        return [], [(u, f"有嚴格 regex 數不到的連結（譯文 +{t_extra}／zh +{z_extra}，空白網址或 wikilink），順序不可信，不配對")
                    for u in sorted(dead)]
    if len(t_links) != len(z_links):
        return [], [(u, f"站內連結數不等（譯文 {len(t_links)}／zh {len(z_links)}），不配對") for u in sorted(dead)]
    z_dead = {u for u, _ in ILC.check_file(src, idx)}
    lang = f.relative_to(KNOWLEDGE).parts[0]
    fixes, skipped = [], []
    for (_, _, tu), (_, _, zu) in zip(t_links, z_links):
        key = tu.split("#")[0].split("?")[0]
        if key not in dead:
            continue
        if category(tu) != category(zu):
            skipped.append((tu, f"分類段對不上 zh 同位置的 {zu}"))
            continue
        if zu.split("#")[0].split("?")[0] in z_dead:
            skipped.append((tu, f"zh 同位置 {zu} 自己也是死的（來源端）"))
            continue
        new, status = C.localize_url(zu, lang, loc)
        if new and not _is_dead(new, idx):
            fixes.append((tu, new, f"zh {zu} → {status}"))
        else:
            fixes.append((tu, zu, "該語言沒有譯文，保留 zh 原路徑"))
    return fixes, skipped


def _is_dead(url: str, idx) -> bool:
    # 跟 check_file 同一套索引與規則，只是吃單一網址而不是整個檔案
    per_lang, zh = idx
    seg = [urllib.parse.unquote(s) for s in url.split("#")[0].split("?")[0].strip("/").split("/") if s]
    if len(seg) < 2:
        return False
    if seg[0] in LANGS:
        if seg[1] != seg[1].lower():
            return True
        return (seg[1].lower(), seg[-1].lower()) not in per_lang.get(seg[0], set())
    return (seg[0].lower(), seg[-1]) not in zh


def apply_file(f: Path, fixes) -> int:
    text = f.read_text(encoding="utf-8")
    table = {}
    for old, new, _ in fixes:
        table.setdefault(old, new)
    n = 0

    def sub(m):
        nonlocal n
        url = m.group(1)
        if url in table:
            n += 1
            return m.group(0).replace("(" + url + ")", "(" + table[url] + ")")
        return m.group(0)

    new_text = ILC.LINK.sub(sub, text)
    if new_text != text:
        f.write_text(new_text, encoding="utf-8")
    return n


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("files", nargs="*")
    ap.add_argument("--lang")
    ap.add_argument("--all", action="store_true")
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--summary", action="store_true", help="只印各語統計")
    a = ap.parse_args()
    if a.apply and (a.all or a.lang):
        ap.error("--apply 只收明列的檔案：全語言改寫超過 50 檔，屬 §自主權邊界，要先有人拍板")

    targets = [Path(x).resolve() for x in a.files]
    if a.lang:
        targets += sorted((KNOWLEDGE / a.lang).rglob("*.md"))
    if a.all:
        for l in sorted(LANGS):
            if (KNOWLEDGE / l).exists():
                targets += sorted((KNOWLEDGE / l).rglob("*.md"))
    if not targets:
        ap.error("要給檔案，或 --lang / --all")

    idx = ILC._index()
    loc = C.load_index()
    stat = Counter()
    files_fixable = Counter()
    for f in targets:
        fixes, skipped = plan_file(f, idx, loc)
        lang = f.relative_to(KNOWLEDGE).parts[0]
        stat[(lang, "fix")] += sum(1 for x in fixes if not x[2].startswith("該語言沒有"))
        stat[(lang, "zh-fallback")] += sum(1 for x in fixes if x[2].startswith("該語言沒有"))
        stat[(lang, "skip")] += len(skipped)
        if fixes:
            files_fixable[lang] += 1
        if not a.summary and (fixes or skipped):
            print(f"== {f.relative_to(REPO)}")
            for old, new, why in fixes:
                print(f"   FIX  {old} → {new}  （{why}）")
            for old, why in skipped:
                print(f"   SKIP {old}  （{why}）")
        if a.apply and fixes:
            n = apply_file(f, fixes)
            print(f"   ✏️  改了 {n} 處")

    langs = sorted({l for l, _ in stat})
    print("\n語言  可修  退回zh  不動  可修檔數")
    for l in langs:
        print(f"{l:4}  {stat[(l,'fix')]:4}  {stat[(l,'zh-fallback')]:6}  {stat[(l,'skip')]:4}  {files_fixable[l]:6}")
    print(f"合計  {sum(v for (l,k),v in stat.items() if k=='fix')}  "
          f"{sum(v for (l,k),v in stat.items() if k=='zh-fallback')}  "
          f"{sum(v for (l,k),v in stat.items() if k=='skip')}  {sum(files_fixable.values())}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
