#!/usr/bin/env python3
"""heal-frontmatter-types.py — 把譯文 frontmatter 裡被壓成字串的巢狀欄位還原成 zh 同形。

誕生 2026-09-22 twmd-babel-nightly：structured／patch 引擎的 render_scalar 對 dict 曾
fallthrough 成 `'{...}'`（Python repr 一整行）、None 變 `'None'`，上站 1,140 份譯文的
`rationale` 因此是一行字串（12 份是 'None'）。rationale 是 zh 編輯部的 passthrough
mapping，正確值就是 zh 的值，所以這支工具不需要模型：從 translatedFrom 找回 zh，
用引擎修好的 render_scalar 重新渲染那一個欄位，其他一個字元不動。

    python3 scripts/tools/lang-sync/heal-frontmatter-types.py --lang ko            # dry-run 印前 10 筆
    python3 scripts/tools/lang-sync/heal-frontmatter-types.py --lang ko --apply    # 落地
    python3 scripts/tools/lang-sync/heal-frontmatter-types.py --lang all --apply --skip-dirty

--skip-dirty 跳過 git 工作樹裡已被改動的檔（並行 dispatcher 在途的譯文），不跟它搶寫。
"""
from __future__ import annotations

import argparse
import re
import subprocess
import sys
from importlib import import_module
from pathlib import Path

import yaml

SCRIPT_DIR = Path(__file__).resolve().parent
REPO = SCRIPT_DIR.parent.parent.parent
KNOWLEDGE = REPO / "knowledge"
sys.path.insert(0, str(SCRIPT_DIR))
_st = import_module("structured-translate")

FIELDS = ["rationale"]
BAD_LINE_RE = re.compile(r"""^(?P<key>[A-Za-z_]+):\s*(?P<val>["']\{.*|["']None["']\s*|["']\[.*)$""")
LANG_DIRS = [d.name for d in KNOWLEDGE.iterdir() if d.is_dir() and len(d.name) == 2]


def split_fm(text: str):
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        return None, None, None
    return m.group(1), text[m.end():], m


def dirty_paths() -> set[str]:
    r = subprocess.run(["git", "status", "--porcelain", "--", "knowledge"], cwd=REPO,
                       capture_output=True, text=True)
    out = set()
    for line in r.stdout.splitlines():
        if len(line) > 3:
            out.add(line[3:].strip().split(" -> ")[-1])
    return out


def heal_file(path: Path, apply: bool) -> tuple[str, str]:
    """回傳 (狀態, 說明)。狀態：healed / would-heal / skip / error。"""
    text = path.read_text(encoding="utf-8")
    fm_text, body, m = split_fm(text)
    if fm_text is None:
        return "skip", "no frontmatter"
    lines = fm_text.split("\n")
    hits = [(i, BAD_LINE_RE.match(l)) for i, l in enumerate(lines)]
    hits = [(i, mm) for i, mm in hits if mm and mm.group("key") in FIELDS]
    if not hits:
        return "skip", "clean"
    try:
        fm = yaml.safe_load(fm_text) or {}
    except yaml.YAMLError as e:
        return "error", f"yaml: {e}"
    zh_rel = fm.get("translatedFrom")
    if not zh_rel or not (KNOWLEDGE / zh_rel).exists():
        return "error", f"zh source missing: {zh_rel}"
    zh_fm, _ = _st.parse_zh_frontmatter((KNOWLEDGE / zh_rel).read_text(encoding="utf-8"))
    changed = []
    for i, mm in hits:
        key = mm.group("key")
        if key not in zh_fm:
            # zh 已經沒有這個欄位——譯文那行本來就不該存在，整行移除
            lines[i] = None
            changed.append(f"{key}: removed (zh has none)")
            continue
        lines[i] = f"{key}:{_st.render_scalar(zh_fm[key])}" if isinstance(zh_fm[key], dict) \
            else f"{key}: {_st.render_scalar(zh_fm[key])}"
        changed.append(f"{key}: {type(zh_fm[key]).__name__}")
    new_fm = "\n".join(l for l in lines if l is not None)
    # 守恆：新 frontmatter 必須能 parse，且該欄位值 == zh 的值
    parsed = yaml.safe_load(new_fm)
    for i, mm in hits:
        key = mm.group("key")
        if key in zh_fm and parsed.get(key) != zh_fm[key]:
            return "error", f"{key} mismatch after render"
    if apply:
        path.write_text(f"---\n{new_fm}\n---\n{body}", encoding="utf-8")
        return "healed", "; ".join(changed)
    return "would-heal", "; ".join(changed)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--lang", required=True, help="語言代碼或 all")
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--skip-dirty", action="store_true")
    ap.add_argument("--limit", type=int, default=0, help="dry-run 時最多印幾筆（0=全部）")
    args = ap.parse_args()
    langs = LANG_DIRS if args.lang == "all" else [args.lang]
    dirty = dirty_paths() if args.skip_dirty else set()
    totals = {"healed": 0, "would-heal": 0, "skip": 0, "error": 0, "dirty-skip": 0}
    healed_paths: list[str] = []
    for lang in langs:
        for p in sorted((KNOWLEDGE / lang).rglob("*.md")):
            rel = str(p.relative_to(REPO))
            if rel in dirty:
                totals["dirty-skip"] += 1
                continue
            status, note = heal_file(p, args.apply)
            totals[status] += 1
            if status in ("healed", "would-heal", "error"):
                shown = totals["healed"] + totals["would-heal"] + totals["error"]
                if not args.limit or shown <= args.limit:
                    print(f"{status:10} {rel}  — {note}")
                if status == "healed":
                    healed_paths.append(rel)
    print("\n" + "  ".join(f"{k}={v}" for k, v in totals.items()))
    if healed_paths:
        out = REPO / ".taiwanmd" / "heal-frontmatter-types.paths"
        out.write_text("\n".join(healed_paths) + "\n", encoding="utf-8")
        print(f"落地路徑清單 → {out.relative_to(REPO)}（精確路徑 stage 用）")
    return 1 if totals["error"] else 0


if __name__ == "__main__":
    sys.exit(main())
