#!/usr/bin/env python3
"""babel-origin-exclude.py — 產出「origin/main 那側已經做掉的翻譯」排除清單。

誕生：2026-09-18 twmd-babel-nightly。兩台機器（營運機 mouhouse 與開發機）各自
跑 babel，在 main 分岔（OBSERVER-QUEUE origin #68／本機 #56）期間翻同一批
stale／missing，knowledge/ 衝突面九天內從 172 檔長到 758 檔，本機單日 215 篇
產出裡 57 篇（27%）origin 也動過。origin 側心跳 session 的結論是「拍板前兩台
都別再跑 babel 存量」；本工具走另一條路——**不停產線，停重複**：把 origin/main
自分岔點以來新增／修改過的譯文，以及 origin 改過的 zh 原稿，全列成排除清單餵給
`babel-dispatch.py --exclude-file`，讓本機只翻 origin 沒有的檔。這批產出在推薦
方案 B（origin 版優先、分支只收 main 沒有的檔）底下會原樣保留，衝突面不再從
本機這側增長。

輸出格式（TSV，每行一條）：
    <lang>\t<zh_path>      只排這個語言的這篇（origin 已有較新譯文）
    *\t<zh_path>           全語言排除（origin 改過 zh 原稿，合併後本機譯文都會再變 stale）

用法：
    python3 scripts/tools/lang-sync/babel-origin-exclude.py            # 寫 .taiwanmd/babel-exclude.tsv
    python3 scripts/tools/lang-sync/babel-origin-exclude.py --dry-run  # 只印統計
    python3 scripts/tools/lang-sync/babel-origin-exclude.py --out PATH

需要先 `git fetch origin main`——本工具只讀 refs，不 fetch、不 merge、不碰 working tree。
"""
from __future__ import annotations

import argparse
import re
import subprocess
import sys
from collections import Counter
from pathlib import Path

REPO = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(REPO / "scripts" / "tools" / "lang-sync"))
from langs import ALL_TRANSLATION_LANGS  # noqa: E402

DEFAULT_OUT = REPO / ".taiwanmd" / "babel-exclude.tsv"
# 委派層認領清單（2026-09-24）：主 session 把一篇派給 Claude sub-agent 翻的那段
# 時間，dispatcher 不能也去碰它——對 missing 檔，dispatcher 失敗時的
# restore_head_or_quarantine 會把 agent 寫到一半的檔案移進隔離區。原本手寫進
# DEFAULT_OUT 的排除行最多活 90 分鐘（EXCLUDE_REFRESH_MIN 到期就被本工具重寫蓋掉），
# 而一篇 sonnet 委派要 20-50 分鐘，剛好卡在會被蓋掉的區間。認領寫在這個獨立檔，
# 每次重算都原樣併進輸出；交件驗收完由主 session 自己刪行。格式同輸出檔。
CLAIMS_FILE = REPO / ".taiwanmd" / "babel-exclude-claims.tsv"
TRANSLATED_FROM_RE = re.compile(r"^translatedFrom:\s*['\"]?(.+?)['\"]?\s*$", re.M)


def git(*args: str) -> str:
    return subprocess.run(["git", *args], cwd=REPO, check=True,
                          capture_output=True, text=True).stdout


def origin_changed_knowledge(remote_ref: str) -> tuple[str, list[str]]:
    base = git("merge-base", "HEAD", remote_ref).strip()
    names = git("diff", "--name-only", base, remote_ref, "--", "knowledge/").split("\n")
    return base, [n for n in names if n.strip()]


def read_translated_from(remote_ref: str, path: str) -> str | None:
    try:
        blob = subprocess.run(["git", "show", f"{remote_ref}:{path}"], cwd=REPO,
                              check=True, capture_output=True, text=True).stdout
    except subprocess.CalledProcessError:
        return None  # 在 origin 那側被刪除／隔離——沒有可對照的譯文，不排除
    head = blob[:4000]
    m = TRANSLATED_FROM_RE.search(head)
    return m.group(1).strip() if m else None


def build(remote_ref: str) -> tuple[str, list[tuple[str, str]], Counter]:
    base, changed = origin_changed_knowledge(remote_ref)
    rows: set[tuple[str, str]] = set()
    stats: Counter = Counter()
    for rel in changed:
        parts = rel.split("/")
        if len(parts) < 3 or not rel.endswith(".md"):
            stats["skipped-non-article"] += 1
            continue
        top = parts[1]
        if top in ALL_TRANSLATION_LANGS:
            zh = read_translated_from(remote_ref, rel)
            if not zh:
                stats["translation-unreadable"] += 1
                continue
            rows.add((top, zh))
            stats[f"lang:{top}"] += 1
        elif top[0].isupper():  # zh 原稿分類目錄（People/History/…）
            rows.add(("*", "/".join(parts[1:])))
            stats["zh-source"] += 1
        else:
            stats["skipped-other"] += 1
    return base, sorted(rows), stats


def read_claims(path: Path) -> list[tuple[str, str]]:
    """讀委派層認領清單（見 CLAIMS_FILE 註解）。檔案不存在就是沒有認領；
    空行與 # 開頭的註解行略過，格式不對的行印警告後略過，不讓一行手誤擋掉整份清單。"""
    if not path.exists():
        return []
    out: list[tuple[str, str]] = []
    for n, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        parts = line.split("\t")
        if len(parts) != 2 or not parts[1].endswith(".md"):
            print(f"  ⚠️ {path.name}:{n} 格式不對，略過：{line!r}", file=sys.stderr)
            continue
        out.append((parts[0], parts[1]))
    return out


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--remote-ref", default="origin/main")
    ap.add_argument("--out", type=Path, default=DEFAULT_OUT)
    ap.add_argument("--dry-run", action="store_true", help="只印統計，不寫檔")
    args = ap.parse_args()

    base, rows, stats = build(args.remote_ref)
    print(f"merge-base {base[:9]}  remote={args.remote_ref}")
    print(f"exclusions: {len(rows)} rows "
          f"(per-lang {sum(1 for l, _ in rows if l != '*')}, all-lang zh-source {sum(1 for l, _ in rows if l == '*')})")
    for k, v in sorted(stats.items()):
        print(f"  {k:26s} {v}")
    if args.dry_run:
        return
    args.out.parent.mkdir(parents=True, exist_ok=True)
    claims = read_claims(CLAIMS_FILE)
    if claims:
        print(f"  delegation claims (from {CLAIMS_FILE.name}): {len(claims)}")
    merged = sorted(set(rows) | set(claims))
    body = "\n".join(f"{lang}\t{zh}" for lang, zh in merged) + "\n"
    args.out.write_text(body, encoding="utf-8")
    print(f"wrote {args.out.relative_to(REPO)}")


if __name__ == "__main__":
    main()
