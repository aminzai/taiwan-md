#!/usr/bin/env python3
"""
refresh-llms-txt.py — auto-refresh public/llms.txt content statistics

Reads dashboard-vitals.json + counts People articles + reads dashboard-i18n.json,
then patches the numerical lines in public/llms.txt in-place using regex replace.

Lines patched:
1. "- Total articles: ..."（整行重寫；語言清單吃 languages.mjs，不寫死）
2. "- N non-Chinese languages ... freshPct ..."（整行重寫；來源 dashboard-translations.json）
3. "People profiles: N+"
4. "Contributors: N"
5. "Average revisions per article: N"
6. "210+" appearing in `People (人物) — N+ profiles:`
7. 正文兩處語言數（"N non-Chinese-language projection" / "N non-zh languages"）與
   "auto-projects to xx/yy/... within" 的語言碼清單
8. "- Categories: N (...)"（從 knowledge/ 首字大寫的資料夾推導；原本停在 13 類，漏了 Politics）

2026-10-01 修正：(1) 語言原本寫死六語，站上已是十三語，AI crawler 讀到的是「6 languages」；
(2) freshPct 原本讀 dashboard-i18n.json，那是 UI 字串覆蓋率、格式從來沒有 languages 欄，
讀回空 dict 時這行就不改，於是從本檔誕生（2026-05-04）起一直停在五月的數字。
現在讀不到 freshPct 會在 stderr 明講，不再安靜沿用舊值。

Triggered from refresh-data.sh Step 2.95 (added 2026-05-04 per REFLEXES #43:
new dashboard-* generators must register in refresh-data.sh or go silent stale).

Usage:
  python3 scripts/tools/refresh-llms-txt.py [--check] [--dry-run]

  --check    exit 1 if llms.txt would change (CI gate)
  --dry-run  print diff without writing

Per REFLEXES #48 (mechanical first, LLM last) — this script is pure deterministic
regex replace, no LLM calls, runs in <100ms.
"""

import argparse
import json
import re
import sys
from pathlib import Path

# Windows cp950 console 強制 UTF-8（不影響 Linux/macOS）
if sys.stdout.encoding and sys.stdout.encoding.lower() not in ("utf-8", "utf8"):
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parent.parent.parent
LLMS_TXT = ROOT / "public" / "llms.txt"
VITALS_JSON = ROOT / "public" / "api" / "dashboard-vitals.json"
TRANSLATIONS_JSON = ROOT / "public" / "api" / "dashboard-translations.json"

sys.path.insert(0, str(ROOT / "scripts" / "tools" / "lang-sync"))
from langs import ENABLED_TRANSLATION_LANGS  # noqa: E402  語言清單 SSOT（languages.mjs）
PEOPLE_DIR = ROOT / "knowledge" / "People"


def count_people_articles() -> int:
    if not PEOPLE_DIR.is_dir():
        return 0
    return sum(1 for f in PEOPLE_DIR.glob("*.md") if not f.name.startswith("_"))


def round_to_tens(n: int) -> int:
    """Round down to nearest 10 for display (210+ not 213+)."""
    return (n // 10) * 10


def load_vitals() -> dict:
    if not VITALS_JSON.exists():
        print(f"⚠️  {VITALS_JSON} not found — run prebuild first", file=sys.stderr)
        sys.exit(2)
    return json.loads(VITALS_JSON.read_text(encoding="utf-8"))


def load_fresh_pct() -> dict:
    """Return {lang: freshPct} from dashboard-translations.json summary. 讀不到回空 dict。"""
    if not TRANSLATIONS_JSON.exists():
        return {}
    try:
        data = json.loads(TRANSLATIONS_JSON.read_text(encoding="utf-8"))
        # Schema: data['summary'] = {'en': {'freshPct': 100, ...}, 'zh-TW': {...}, ...}
        out = {}
        for lang, entry in (data.get("summary") or {}).items():
            pct = entry.get("freshPct") if isinstance(entry, dict) else None
            if lang != "zh-TW" and pct is not None:
                out[lang] = pct
        return out
    except (json.JSONDecodeError, AttributeError):
        return {}


def fmt_lang_freshpct(fresh: dict) -> str:
    """Build 'en 100% / ja 100% / ...' in registry order."""
    return " / ".join(
        f"{lang} {int(round(fresh[lang]))}%" for lang in ENABLED_TRANSLATION_LANGS if lang in fresh
    )


def patch_llms_txt(content: str, vitals: dict, fresh: dict, people_count: int) -> str:
    cov = vitals.get("languageCoverage", {})
    zh = cov.get("zh-TW", 0)
    langs = ENABLED_TRANSLATION_LANGS
    n = len(langs)
    total = zh + sum(cov.get(lang, 0) for lang in langs)
    contributors = vitals.get("contributors", 0)
    avg_rev = vitals.get("avgRevision", 0)

    # 1. Total articles line（整行重寫，舊的六語寫法與新寫法都吃得到）
    per_lang = " / ".join(f"{lang} {cov.get(lang, 0)}" for lang in langs)
    content = re.sub(
        r"^- Total articles: .*$",
        f"- Total articles: **{zh}** Chinese (SSOT), translated into {n} languages "
        f"({per_lang}) = {total:,} across {n + 1} languages",
        content,
        flags=re.MULTILINE,
    )

    # 2. Lang freshPct line（讀不到資料就不動，由 main 在 stderr 明講）
    fresh_str = fmt_lang_freshpct(fresh) if fresh else ""
    if fresh_str:
        content = re.sub(
            r"^- \d+ non-Chinese languages\b.*freshPct.*$",
            f"- {n} non-Chinese languages, real freshPct (share of translations matching "
            f"the current Chinese source version): {fresh_str}",
            content,
            flags=re.MULTILINE,
        )

    # 8. 分類清單：knowledge/ 底下首字大寫的資料夾就是分類（語言資料夾是小寫碼）
    cats = sorted(d.name for d in (ROOT / "knowledge").iterdir() if d.is_dir() and d.name[:1].isupper())
    if cats:
        content = re.sub(
            r"^- Categories: \d+ \([^)]*\)$",
            f"- Categories: {len(cats)} ({', '.join(cats)})",
            content,
            flags=re.MULTILINE,
        )

    # 7. 正文裡的語言數與語言碼清單
    content = re.sub(r"\b\d+ non-Chinese-language projection", f"{n} non-Chinese-language projection", content)
    content = re.sub(r"\b\d+ non-zh languages", f"{n} non-zh languages", content)
    content = re.sub(
        r"auto-projects to [a-z/-]+ within",
        f"auto-projects to {'/'.join(langs)} within",
        content,
    )

    # 3. People profiles
    rounded = round_to_tens(people_count)
    content = re.sub(
        r"People profiles: \d+\+",
        f"People profiles: {rounded}+",
        content,
    )
    # Also patch "People (人物) — N+ profiles:" line
    content = re.sub(
        r"People \(人物\) — \d+\+ profiles:",
        f"People (人物) — {rounded}+ profiles:",
        content,
    )

    # 4. Contributors
    content = re.sub(
        r"^- Contributors: \d+$",
        f"- Contributors: {contributors}",
        content,
        flags=re.MULTILINE,
    )

    # 5. Average revisions
    content = re.sub(
        r"Average revisions per article: [\d.]+",
        f"Average revisions per article: {avg_rev}",
        content,
    )

    return content


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="exit 1 if llms.txt would change (CI gate)")
    parser.add_argument("--dry-run", action="store_true", help="print diff without writing")
    args = parser.parse_args()

    if not LLMS_TXT.exists():
        print(f"❌ {LLMS_TXT} not found", file=sys.stderr)
        sys.exit(2)

    original = LLMS_TXT.read_text(encoding="utf-8")
    vitals = load_vitals()
    fresh = load_fresh_pct()
    if not fresh:
        print(
            f"⚠️  freshPct 讀不到（{TRANSLATIONS_JSON.relative_to(ROOT)} 缺檔或格式變了），"
            "llms.txt 的 freshPct 行保留舊值，這行現在是過期的",
            file=sys.stderr,
        )
    people = count_people_articles()
    updated = patch_llms_txt(original, vitals, fresh, people)

    if updated == original:
        print(f"✓ llms.txt 已是最新 (zh {vitals['languageCoverage']['zh-TW']} / contributors {vitals['contributors']} / People ~{round_to_tens(people)}+)")
        return 0

    if args.check:
        print(f"❌ llms.txt 過時 — 跑 python3 scripts/tools/refresh-llms-txt.py 修復", file=sys.stderr)
        return 1

    if args.dry_run:
        # Show first 5 changed lines for preview
        from difflib import unified_diff
        diff = unified_diff(
            original.splitlines(keepends=True),
            updated.splitlines(keepends=True),
            fromfile="llms.txt (current)",
            tofile="llms.txt (refreshed)",
            n=1,
        )
        sys.stdout.writelines(diff)
        return 0

    LLMS_TXT.write_text(updated, encoding="utf-8")
    cov = vitals["languageCoverage"]
    per_lang = " / ".join(f"{lang} {cov.get(lang, 0)}" for lang in ["zh-TW", *ENABLED_TRANSLATION_LANGS])
    print(f"✓ llms.txt refreshed: {per_lang} / contributors {vitals['contributors']} / People ~{round_to_tens(people)}+")
    return 0


if __name__ == "__main__":
    sys.exit(main())
