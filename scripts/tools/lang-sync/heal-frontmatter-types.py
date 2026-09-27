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
--sync-passthrough 同時把 zh 的卡片圖四欄與 featured 同步進譯文（同步集刻意保守，見
SYNC_SCALAR_FIELDS 註解）。病根：zh 只改 frontmatter（例如把
Wikimedia 熱連結 cache 成 /article-images/）時 bodyHash 不變 → status 判 metadata-stale →
Tier 0b bump-source-sha 只 bump 三個 sha 欄位就標 fresh，passthrough 值留在舊的；2026-09-22
量到 261 份譯文 image 跟 zh 不同、179 份仍熱連結 Wikimedia（pre-commit image-health hard）。
bump-source-sha.py 從同日起 import 本檔的 sync_passthrough_fields()，新 bump 不再留這個洞。
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
# 同步集刻意保守：卡片圖四欄＋featured——這五個是站上直接顯示、zh 值對所有語言都權威、
# 而且 drift 會撞 pre-commit image-health hard 的欄位。date／readingTime／lastVerified／
# lastHumanReview／difficulty 雖也在 verify PASSTHROUGH，但對一份「body 還停在舊版」的
# stale 譯文提前抄 zh 的 lastVerified 等於替沒驗過的內容蓋章（#38 混維度），留給重翻路徑。
# author（署名）與 category（綁路徑）不碰。
SYNC_SCALAR_FIELDS = [
    "image", "imageCredit", "imageLicense", "imageSource", "featured",
]
SCALAR_LINE_RE = re.compile(r"^(?P<key>[A-Za-z_]+):(?P<rest>.*)$")
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


def sync_passthrough_fields(fm_lines: list[str], zh_fm: dict,
                            fields: list[str] = SYNC_SCALAR_FIELDS) -> tuple[list[str], list[str]]:
    """把 zh 的標量 passthrough 欄位同步進譯文 frontmatter 行陣列。回傳 (新行陣列, 變更說明)。
    只碰單行標量：zh 有、譯文值不同 → 覆寫；zh 沒有、譯文有 → 移除該行；zh 有、譯文沒有 → 補在
    translatedFrom 之前（沒有就補檔尾）。值一律用 render_scalar 渲染，跟引擎同一把尺。"""
    import yaml as _yaml
    changed: list[str] = []
    out = list(fm_lines)
    idx = {}
    for i, l in enumerate(out):
        m = SCALAR_LINE_RE.match(l)
        if m and not l.startswith((" ", "\t")):
            idx[m.group("key")] = i
    for key in fields:
        zh_has = key in zh_fm and zh_fm[key] is not None
        if key in idx:
            i = idx[key]
            try:
                cur = _yaml.safe_load(out[i])
                cur_val = cur.get(key) if isinstance(cur, dict) else None
            except _yaml.YAMLError:
                cur_val = object()
            if not zh_has:
                out[i] = None
                changed.append(f"{key}: removed (zh has none)")
            elif cur_val != zh_fm[key]:
                out[i] = _st.render_field(key, zh_fm[key])
                changed.append(f"{key}: synced")
        elif zh_has:
            line = _st.render_field(key, zh_fm[key])
            anchor = idx.get("translatedFrom")
            if anchor is not None:
                out.insert(anchor, line)
                idx = {k: (v + 1 if v >= anchor else v) for k, v in idx.items()}
            else:
                out.append(line)
            changed.append(f"{key}: added")
    return [l for l in out if l is not None], changed


def split_collapsed_tags(lines: list[str], tr_fm: dict, zh_fm: dict) -> tuple[list[str], str | None, str | None]:
    """--split-tags：譯文 tags 只有一個字串、裡面用分隔符包著整張清單，而 zh 有 ≥2 個標籤
    → 照 zh 的數量切開，換掉整個 tags 區塊。回傳 (新行陣列, 變更說明, 錯誤)。

    病根在整篇引擎只切 ASCII 逗號（translate.split_tags 2026-09-27 修掉），存量 ar 438、ja 14。
    切的規則跟引擎共用同一支 split_tags；切出來的數量對不上 zh 就不動，交給重翻。"""
    tr_tags, zh_tags = tr_fm.get("tags"), zh_fm.get("tags")
    if not (isinstance(tr_tags, list) and len(tr_tags) == 1 and isinstance(tr_tags[0], str)
            and isinstance(zh_tags, list) and len(zh_tags) >= 2):
        return lines, None, None
    translate = import_module("translate")  # 延遲載入：bump-source-sha 也 import 本檔
    parts = translate.split_tags(tr_tags[0], len(zh_tags))
    if len(parts) != len(zh_tags):
        return lines, None, f"tags 切出 {len(parts)} 個、zh 有 {len(zh_tags)} 個，要重翻"
    start = next(i for i, l in enumerate(lines) if l.startswith("tags:"))
    end = start + 1
    while end < len(lines) and (lines[end].startswith((" ", "\t")) or lines[end].strip() in ("[", "]")):
        end += 1
    return lines[:start] + [_st.render_field("tags", parts)] + lines[end:], f"tags: 1 → {len(parts)}", None


def heal_file(path: Path, apply: bool, sync_passthrough: bool = False,
              split_tags: bool = False) -> tuple[str, str]:
    """回傳 (狀態, 說明)。狀態：healed / would-heal / skip / error。"""
    text = path.read_text(encoding="utf-8")
    fm_text, body, m = split_fm(text)
    if fm_text is None:
        return "skip", "no frontmatter"
    lines = fm_text.split("\n")
    hits = [(i, BAD_LINE_RE.match(l)) for i, l in enumerate(lines)]
    hits = [(i, mm) for i, mm in hits if mm and mm.group("key") in FIELDS]
    if not hits and not sync_passthrough and not split_tags:
        return "skip", "clean"
    try:
        fm = yaml.safe_load(fm_text) or {}
    except yaml.YAMLError as e:
        return "error", f"yaml: {e}"
    zh_rel = fm.get("translatedFrom")
    if not zh_rel:
        return "skip", "not a translation (no translatedFrom — hub 檔)"
    if not (KNOWLEDGE / zh_rel).exists():
        return "error", f"zh source missing: {zh_rel}"
    zh_fm, _ = _st.parse_zh_frontmatter((KNOWLEDGE / zh_rel).read_text(encoding="utf-8"))
    changed = []
    if sync_passthrough:
        lines, pt_changed = sync_passthrough_fields(lines, zh_fm)
        changed.extend(pt_changed)
        # 行位移後重新定位 rationale 命中行
        hits = [(i, BAD_LINE_RE.match(l)) for i, l in enumerate(lines)]
        hits = [(i, mm) for i, mm in hits if mm and mm.group("key") in FIELDS]
        if not hits and not changed and not split_tags:
            return "skip", "clean"
    for i, mm in hits:
        key = mm.group("key")
        if key not in zh_fm:
            # zh 已經沒有這個欄位——譯文那行本來就不該存在，整行移除
            lines[i] = None
            changed.append(f"{key}: removed (zh has none)")
            continue
        lines[i] = _st.render_field(key, zh_fm[key])
        changed.append(f"{key}: {type(zh_fm[key]).__name__}")
    lines = [l for l in lines if l is not None]
    tag_parts = None
    if split_tags:
        lines, note, err = split_collapsed_tags(lines, fm, zh_fm)
        if err:
            return "error", err
        if note:
            changed.append(note)
            tag_parts = len(zh_fm["tags"])
    if not changed:
        return "skip", "clean"
    new_fm = "\n".join(lines)
    # 守恆：新 frontmatter 必須能 parse，且該欄位值 == zh 的值
    # 加尾端換行再 parse：檔案裡 frontmatter 後面接的是 "\n---"，block scalar `|` 的
    # clip 行為要看到那個換行才會保留最後一個 \n，跟實際落檔後的讀法一致。
    parsed = yaml.safe_load(new_fm + "\n")
    for i, mm in hits:
        key = mm.group("key")
        if key in zh_fm and parsed.get(key) != zh_fm[key]:
            return "error", f"{key} mismatch after render"
    if sync_passthrough:
        for key in SYNC_SCALAR_FIELDS:
            if zh_fm.get(key) is not None and parsed.get(key) != zh_fm[key]:
                return "error", f"{key} mismatch after sync"
    if tag_parts is not None:
        # 守恆：切完的標籤數等於 zh，且串回去跟原本那一個字串只差分隔符
        new_tags = parsed.get("tags")
        if not isinstance(new_tags, list) or len(new_tags) != tag_parts:
            return "error", "tags count mismatch after split"
        joined = re.sub(r"[\s,，、،;；]", "", "".join(new_tags))
        if joined != re.sub(r"[\s,，、،;；]", "", fm["tags"][0]):
            return "error", "tags content changed by split"
    if apply:
        path.write_text(f"---\n{new_fm}\n---\n{body}", encoding="utf-8")
        return "healed", "; ".join(changed)
    return "would-heal", "; ".join(changed)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--lang", required=True, help="語言代碼或 all")
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--skip-dirty", action="store_true")
    ap.add_argument("--sync-passthrough", action="store_true",
                    help="同時把 zh 的標量 passthrough 欄位（圖片四欄等）同步進譯文")
    ap.add_argument("--split-tags", action="store_true",
                    help="把擠成一個字串的 tags 照 zh 的數量切開（ar／ja 的阿拉伯逗號、頓號存量）")
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
            status, note = heal_file(p, args.apply, sync_passthrough=args.sync_passthrough,
                                     split_tags=args.split_tags)
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
