#!/usr/bin/env python3
"""
recover-source-sha.py — 依內容雜湊，在中文檔的 git 歷史裡找回譯文真正翻譯的那一版，
只改 `sourceCommitSha`，不動雜湊、不動正文。

為什麼要有這支（2026-10-03 semiont-heartbeat）：
  譯文 frontmatter 有兩組「我是照哪一版中文翻的」的紀錄——`sourceCommitSha` 與
  `sourceContentHash`／`sourceBodyHash`。兩組說的應該是同一版中文，但沒有任何東西
  在對賬：
  - 01:11 `c18e47390`：34 份譯文的 sha 指向中文修正**之後**的 commit，雜湊卻是修正
    **之前**的中文。status.py 遇到 sha 相同就判 fresh、不看雜湊，帶著舊錯的譯文一直
    顯示最新。當班逐篇用 git 歷史比對雜湊手工找回。
  - 同一晚 verify-translation.py 第 4 項升級（OBSERVER-QUEUE #65 (a)）量出 4 篇 sha
    解析不到任何 commit。
  兩件事的修法是同一個動作：拿譯文自己記的雜湊，回中文檔歷史裡找雜湊對得上的那個
  commit。`bump-source-sha.py` 是另一個方向（把 sha 與雜湊一起升到中文最新版，只在
  中文正文沒變時才誠實）；對 sha 錯掉的譯文用它，等於宣稱譯文是照今天的中文翻的。

比對規則：中文檔在某個 commit 的內容，用三種算法算雜湊，任一個等於譯文記的值就算
命中——status.py `body_hash_pure`（對 sourceBodyHash）、status.py `body_hash`（對
sourceContentHash）、整份檔含 frontmatter 的 sha256 前 16 碼（對 sourceContentHash，
OBSERVER-QUEUE #83 那 1,092 篇用的舊算法）。同一份內容常橫跨好幾個 commit（中間只改
frontmatter），取最新的那個：內容相同，哪一個都說得通，最新的離翻譯時點最近。

找不到就不改，印出「找不到」——那代表譯文記的雜湊本身也對不上任何一版中文，該讓
產線把它當 stale 重翻，不是再編一個 sha。

Usage:
  recover-source-sha.py knowledge/en/Technology/foo.md [...]   # 乾跑：印現值、找回值、命中方式
  recover-source-sha.py --apply knowledge/en/...               # 寫回 sourceCommitSha，再跑 verify 第 4 項
  recover-source-sha.py --check knowledge/en/...               # 只對賬：現有 sha 那一版中文的雜湊，對不對得上譯文記的雜湊

Exit codes: 0 全部找到（或 --check 全部一致）；1 有找不到／不一致的。
"""
import argparse
import hashlib
import importlib.util
import re
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent.parent.parent
HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:  # status.py imports its sibling `langs`
    sys.path.insert(0, str(HERE))


def _load(name: str, filename: str):
    spec = importlib.util.spec_from_file_location(name, HERE / filename)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


status_mod = _load("status_mod", "status.py")
verify_mod = _load("verify_mod", "verify-translation.py")

FIELD_RE = {
    "sha": re.compile(r"^sourceCommitSha:\s*['\"]?([^'\"\s]+)['\"]?\s*$", re.M),
    "from": re.compile(r"^translatedFrom:\s*['\"]?([^'\"\n]+?)['\"]?\s*$", re.M),
    "content": re.compile(r"^sourceContentHash:\s*['\"]?(sha256:[0-9a-f]+)['\"]?\s*$", re.M),
    "body": re.compile(r"^sourceBodyHash:\s*['\"]?(sha256:[0-9a-f]+)['\"]?\s*$", re.M),
}


def git(*args: str) -> str:
    r = subprocess.run(["git", *args], cwd=REPO, capture_output=True, text=True, timeout=60)
    return r.stdout if r.returncode == 0 else ""


def frontmatter(text: str) -> str:
    if not text.startswith("---"):
        return ""
    end = text.find("\n---", 3)
    return text[: end + 4] if end != -1 else ""


def read_provenance(path: Path) -> dict:
    fm = frontmatter(path.read_text(encoding="utf-8"))
    out = {}
    for key, rx in FIELD_RE.items():
        m = rx.search(fm)
        out[key] = m.group(1) if m else ""
    out["from"] = out["from"].replace("knowledge/", "")
    return out


def hashes_of(zh_text: str) -> dict:
    whole = "sha256:" + hashlib.sha256(zh_text.encode("utf-8")).hexdigest()[:16]
    return {
        "body_hash_pure": status_mod.body_hash_pure(zh_text),
        "body_hash": status_mod.body_hash(zh_text),
        "whole_file": whole,
    }


def _h16(value: str) -> str:
    """Recorded hashes come as 16 hex (status.py) or the full 64 (some July
    translations); compare on the 16-hex prefix status.py itself uses."""
    return value.split(":", 1)[-1][:16] if value else ""


def match_kind(prov: dict, h: dict) -> str:
    """Which recorded hash this zh version satisfies ('' = none)."""
    content, body = _h16(prov["content"]), _h16(prov["body"])
    if content and content == _h16(h["body_hash"]):
        return "sourceContentHash=body_hash"
    if body and body == _h16(h["body_hash_pure"]):
        return "sourceBodyHash=body_hash_pure"
    if content and content == _h16(h["whole_file"]):
        return "sourceContentHash=whole_file(#83)"
    return ""


def zh_history(zh_rel: str) -> list:
    """[(commit, path_at_commit)] newest first, following renames."""
    out = git("log", "--follow", "--format=C %H", "--name-only", "--", f"knowledge/{zh_rel}")
    rows, cur = [], None
    for line in out.splitlines():
        if line.startswith("C "):
            cur = line[2:].strip()
        elif line.strip() and cur:
            rows.append((cur, line.strip()))
            cur = None
    return rows


def recover(prov: dict) -> tuple:
    for commit, path in zh_history(prov["from"]):
        text = git("show", f"{commit}:{path}")
        if not text:
            continue
        kind = match_kind(prov, hashes_of(text))
        if kind:
            return commit[:9], kind
    return "", ""


def check_current(prov: dict) -> str:
    """'' if the current sha's zh version matches a recorded hash, else a reason."""
    sha = prov["sha"]
    if not sha or sha == "pre-toolkit":
        return "沒有可對賬的 sha"
    full = git("rev-parse", "--verify", "--quiet", f"{sha}^{{commit}}").strip()
    if not full:
        return f"{sha} 解析不到 commit"
    text = git("show", f"{full}:knowledge/{prov['from']}")
    if not text:
        for commit, path in zh_history(prov["from"]):
            if commit == full:
                text = git("show", f"{commit}:{path}")
                break
    if not text:
        return f"{sha} 這個 commit 裡沒有中文檔"
    if not (prov["content"] or prov["body"]):
        return "譯文沒有記雜湊，無從對賬"
    return "" if match_kind(prov, hashes_of(text)) else f"{sha} 那一版中文的雜湊對不上譯文記的雜湊"


def write_sha(path: Path, new_sha: str) -> None:
    text = path.read_text(encoding="utf-8")
    fm = frontmatter(text)
    new_fm, n = re.subn(r"^(sourceCommitSha:\s*)(['\"]?)[^'\"\s]+(['\"]?)\s*$",
                        lambda m: f"{m.group(1)}{m.group(2)}{new_sha}{m.group(3)}",
                        fm, count=1, flags=re.M)
    if n != 1:
        raise SystemExit(f"{path}: sourceCommitSha 行改寫失敗")
    path.write_text(new_fm + text[len(fm):], encoding="utf-8")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("files", nargs="+")
    mode = ap.add_mutually_exclusive_group()
    mode.add_argument("--apply", action="store_true")
    mode.add_argument("--check", action="store_true")
    args = ap.parse_args()

    bad = 0
    for f in args.files:
        path = (REPO / f) if not Path(f).is_absolute() else Path(f)
        prov = read_provenance(path)
        rel = path.relative_to(REPO) if str(path).startswith(str(REPO)) else path
        if not prov["from"]:
            print(f"⏩ {rel}: 沒有 translatedFrom，不是譯文")
            continue
        if args.check:
            reason = check_current(prov)
            print(f"{'✅' if not reason else '❌'} {rel}: {reason or prov['sha'] + ' 與雜湊一致'}")
            bad += bool(reason)
            continue
        found, kind = recover(prov)
        if not found:
            print(f"❌ {rel}: 中文檔歷史裡沒有任何一版的雜湊對得上譯文記的值（sha 現值 {prov['sha']}）——讓產線當 stale 重翻，不要編 sha")
            bad += 1
            continue
        same = found.startswith(prov["sha"]) or prov["sha"].startswith(found[:len(prov["sha"])])
        print(f"{'＝' if same else '→'} {rel}: {prov['sha']} → {found}（{kind}）")
        if args.apply and not same:
            write_sha(path, found)
            level, detail = verify_mod.source_sha_history_check(prov["from"], found)
            print(f"   verify 第 4 項：{level} {detail}")
            bad += level == "FAIL"
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
