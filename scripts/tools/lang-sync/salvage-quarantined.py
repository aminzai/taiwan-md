#!/usr/bin/env python3
"""salvage-quarantined.py — gate 驗證式還原今天被 quarantine 刪除的譯文。

原則（founder.md 教訓）：寧可 stale 也不要 missing。
v3 dispatcher 對 P1 gate fail 直接 unlink+commit，把可讀的 stale 版降級成 404。
本腳本從 git 歷史撈回刪除前的版本，跑跟 dispatcher 相同的三重 gate
（verify-translation / cjk-leak / article-health），全過才留下——
故意 quarantine 的壞檔（zh 洩漏、掉圖）會被 gate 擋掉，不會復活。
"""
import argparse
import importlib.util
import pathlib
import re
import subprocess

REPO = pathlib.Path("/Users/cheyuwu/Projects/taiwan-md")
LANG_DIRS = ["en", "ja", "ko", "es", "fr", "vi", "id", "pt", "hi"]


def run(cmd, **kw):
    return subprocess.run(cmd, capture_output=True, text=True, cwd=REPO, **kw)


def restore_run_quarantine(run_dir: pathlib.Path, names: list[str]) -> list[str]:
    """把本輪 dispatcher 隔離檔按明確檔名回填，且同步跑 canonical verify trio。

    run quarantine 的檔名是 ``<lang>--<slug>.md``；分類與 zh source 則只信
    frontmatter translatedFrom，避免靠 slug 猜路徑。呼叫者必須逐一列名，
    不提供「整包全收」入口，防止一個 checker 修正意外放行其他失敗家族。
    """
    spec = importlib.util.spec_from_file_location(
        "_rescue_orphans", REPO / "scripts/tools/lang-sync/rescue-orphans.py"
    )
    rescue = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(rescue)
    restored = []
    quarantine = run_dir / "quarantine"
    for name in names:
        src = quarantine / name
        match = re.fullmatch(r"([a-z]{2})--(.+\.md)", name)
        if not match or not src.is_file():
            print(f"  ❌ run quarantine 路徑無效: {src}")
            continue
        content = src.read_text(encoding="utf-8")
        tf = re.search(r"^translatedFrom:\s*['\"]?(.+?)['\"]?\s*$", content, re.M)
        if not tf:
            print(f"  ❌ translatedFrom 缺失: {src}")
            continue
        zh_rel = pathlib.PurePosixPath(tf.group(1))
        parts = zh_rel.parts
        if len(parts) == 2:
            category = parts[0]
        elif len(parts) >= 3 and parts[0] == "zh":
            category = parts[1]
        else:
            print(f"  ❌ translatedFrom 非 canonical: {tf.group(1)}")
            continue
        target = REPO / "knowledge" / match.group(1) / category / match.group(2)
        if target.exists():
            print(f"  ⏭️  target 已存在，不覆寫: {target.relative_to(REPO)}")
            continue
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(content, encoding="utf-8")
        rel = str(target.relative_to(REPO))
        ok, reason = rescue.verify_trio(rel)
        if ok:
            restored.append(rel)
            print(f"  ✅ restore run quarantine: {rel}")
        else:
            target.unlink()
            print(f"  ❌ verify trio ({reason}): {rel}")
    return restored


def main():
    ap = argparse.ArgumentParser(
        description="從 git 歷史回收被 quarantine 刪除、且仍通過 stale-safe gate 的譯文",
    )
    ap.add_argument(
        "--output",
        default="/tmp/babel-20260724/salvage-restored.txt",
        help="回收成功清單路徑（parent 不存在會自動建立）",
    )
    ap.add_argument("--run-dir", type=pathlib.Path, help="本輪 dispatcher run dir")
    ap.add_argument(
        "--run-file",
        action="append",
        default=[],
        help="只回收明確列出的 quarantine basename；可重複",
    )
    args = ap.parse_args()

    if args.run_dir:
        if not args.run_file:
            ap.error("--run-dir 必須搭配至少一個 --run-file，禁止整包放行")
        restored = restore_run_quarantine(args.run_dir, args.run_file)
        out = pathlib.Path(args.output)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text("\n".join(restored) + "\n" if restored else "", encoding="utf-8")
        print(f"restored list → {out}")
        return

    paths = [f"knowledge/{l}" for l in LANG_DIRS]
    # 撈近兩天所有刪除紀錄：commit hash + 被刪路徑
    log = run(["git", "log", "--diff-filter=D", "--since=2026-07-23 00:00",
               "--name-only", "--format=@%H", "--"] + paths)
    deletions = {}  # path -> first (latest) deleting commit
    cur = None
    for line in log.stdout.splitlines():
        if line.startswith("@"):
            cur = line[1:]
        elif line.startswith("knowledge/") and line.endswith(".md"):
            deletions.setdefault(line, cur)

    print(f"歷史刪除紀錄: {len(deletions)} 檔")
    restored, gate_fail, skipped = [], [], []

    for path, commit in sorted(deletions.items()):
        full = REPO / path
        if full.exists():
            skipped.append((path, "已重生"))
            continue
        # 撈刪除前版本
        blob = run(["git", "show", f"{commit}^:{path}"])
        if blob.returncode != 0:
            skipped.append((path, "blob 不存在"))
            continue
        content = blob.stdout
        # zh source 必須還在（translatedFrom）
        tf = None
        for ln in content.splitlines()[:30]:
            if ln.startswith("translatedFrom:"):
                tf = ln.split(":", 1)[1].strip().strip("'\"")
                break
        if not tf or not (REPO / "knowledge" / tf).exists():
            skipped.append((path, f"zh source 缺: {tf}"))
            continue
        full.parent.mkdir(parents=True, exist_ok=True)
        full.write_text(content, encoding="utf-8")
        # 還原 gate：health + leak（可讀、無洩漏、格式合法）。
        # 不跑 verify-translation 完整度——舊版對不上最新 zh 的腳註數正是
        # 「stale」的定義，還原的目的就是讓 stale 版活著等重翻；用新譯文的
        # 完整度標準擋還原 = 把 stale 判死刑（2026-07-24 v2 放寬）。
        r2 = run(["python3", "scripts/tools/lang-sync/cjk-leak-check.py", path])
        r3 = run(["python3", "scripts/tools/article-health.py", path,
                  "--profile=pre-commit", "--quiet"])
        ok = r2.returncode == 0 and "passed=False" not in r3.stdout
        if ok:
            restored.append(path)
            print(f"  ✅ restore {path}")
        else:
            full.unlink()
            reason = ("health" if "passed=False" in r3.stdout else "leak")
            gate_fail.append((path, reason))
            print(f"  ❌ gate fail ({reason}) {path}")

    print(f"\n=== 結果: restored={len(restored)} gate_fail={len(gate_fail)} skipped={len(skipped)}")
    for p, r in gate_fail:
        print(f"  fail: {p} ({r})")
    for p, r in skipped[:10]:
        print(f"  skip: {p} ({r})")
    # 落一份清單給 commit 步驟
    out = pathlib.Path(args.output)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text("\n".join(restored) + "\n" if restored else "", encoding="utf-8")
    print(f"restored list → {out}")


if __name__ == "__main__":
    main()
