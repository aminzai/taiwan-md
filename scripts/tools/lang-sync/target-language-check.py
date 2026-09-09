#!/usr/bin/env python3
"""
target-language-check.py — 譯文到底是不是它宣稱的那個語言。

為什麼需要這支：
  2026-09-09 一隻委派 agent 把 `Technology/Threads在台灣.md` 翻成**英文**寫進
  `knowledge/de/`，而委派層的六道閘全部放行——結構對靶 55/55、verify 17 pass、
  cjk-leak 0、cjk-adjacency 0、article-health hard=0。整套閘門量的都是形式
  （結構數字、中文殘留、網址一致、frontmatter 欄位），**沒有任何一道在問
  「這是不是目標語言」**。一篇英文譯文對所有既有檢查來說都是完美的德文譯文。

  這是 REFLEXES #69「形式閘門 ≠ 意義閘門」最基本的一格。它不會被讀者以外的
  任何東西抓到，而讀者抓到的時候，那篇已經在站上了。

判準為什麼是這樣：
  非拉丁書寫系統（ru/ar/hi/ja/ko）用字符集判定，因為書寫系統本身就是最強的
  訊號，不會誤判。拉丁字母語言（en/de/es/fr/pt/id/vi）彼此共用字母，只能靠
  功能詞（冠詞、介系詞、連接詞）——這些詞在任何一篇散文裡都必然大量出現，
  而且跨語言幾乎不重疊。用功能詞而不是內容詞，是因為內容詞會被專有名詞
  （台灣地名、人名、品牌）稀釋，而功能詞不會。

  刻意不引入 langdetect / fasttext 這類套件：多一個相依就是產線多一個會壞的
  地方，而這裡要判的只有十二個已知語言的二選一，功能詞表就夠了。

  分數低於門檻不代表一定錯——短文、清單體、程式碼密集的文章功能詞會偏少。
  所以輸出的是「最像哪個語言」加分差，讓呼叫端決定；只有在「判定語言 ≠ 目標
  語言且分差夠大」時才 hard fail。

用法：
  python3 scripts/tools/lang-sync/target-language-check.py knowledge/de/Foo/bar.md
  python3 scripts/tools/lang-sync/target-language-check.py --scan de        # 掃整個語言目錄
  python3 scripts/tools/lang-sync/target-language-check.py --scan all --json
"""
import argparse
import json
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent.parent.parent
KNOWLEDGE = REPO / "knowledge"

# 非拉丁語言：字符集即判準（範圍取自 Unicode block）
SCRIPT_RANGES = {
    "ru": r"[Ѐ-ӿ]",       # Cyrillic
    "ar": r"[؀-ۿ]",       # Arabic
    "hi": r"[ऀ-ॿ]",       # Devanagari
    "ko": r"[가-힯]",       # Hangul syllables
    "ja": r"[぀-ゟ゠-ヿ]",  # Hiragana + Katakana（漢字不算，會跟 zh 撞）
}

# 拉丁語言：功能詞。刻意只收冠詞/介系詞/連接詞/助動詞，不收內容詞。
FUNCTION_WORDS = {
    "en": {"the", "and", "of", "to", "in", "that", "is", "for", "with", "as", "was", "on", "are", "it", "this", "by", "from", "has", "but", "not"},
    "de": {"der", "die", "das", "und", "ist", "nicht", "von", "mit", "für", "den", "dem", "ein", "eine", "auch", "sich", "wurde", "werden", "auf", "im", "des", "zu", "als", "aber", "durch", "über"},
    "es": {"de", "la", "el", "que", "en", "los", "del", "se", "las", "por", "con", "una", "para", "es", "más", "como", "pero", "sus", "al", "lo"},
    "fr": {"de", "la", "le", "les", "des", "et", "en", "un", "une", "du", "que", "pour", "dans", "qui", "est", "sur", "par", "au", "aux", "plus"},
    "pt": {"de", "que", "do", "da", "em", "para", "com", "uma", "os", "as", "no", "na", "por", "mais", "dos", "das", "foi", "ao", "como", "mas"},
    "id": {"yang", "dan", "di", "ini", "itu", "dengan", "untuk", "dari", "pada", "tidak", "dalam", "adalah", "akan", "juga", "oleh", "sebagai", "ke", "atau", "telah", "para"},
    "vi": {"của", "và", "là", "các", "có", "được", "trong", "người", "những", "một", "cho", "với", "để", "không", "này", "đã", "khi", "về", "từ", "tại"},
}

LATIN_LANGS = set(FUNCTION_WORDS)
ALL_LANGS = sorted(set(SCRIPT_RANGES) | LATIN_LANGS)

# 判定語言 ≠ 目標語言時，領先幅度要多大才算 hard fail。
# 設 1.5 倍而不是「只要領先就 fail」：es/pt、id/vi 這幾組功能詞有零星重疊，
# 短文上會出現接近的分數，那種情況該給人看不該直接擋。
FAIL_RATIO = 1.5
MIN_TOKENS = 80  # 低於這個字數的正文不判（清單體、極短文）


def body_of(text: str) -> str:
    """去掉 frontmatter 與程式碼區塊——它們的語言跟譯文語言無關。"""
    if text.startswith("---"):
        parts = text.split("---", 2)
        if len(parts) >= 3:
            text = parts[2]
    text = re.sub(r"```.*?```", " ", text, flags=re.S)
    text = re.sub(r"`[^`]*`", " ", text)
    text = re.sub(r"https?://\S+", " ", text)          # 網址裡的英文單字會污染判定
    text = re.sub(r"\[\^[^\]]*\]:?", " ", text)
    return text


def score(text: str) -> dict[str, float]:
    """回傳每個語言的分數。非拉丁看字符佔比，拉丁看功能詞佔比，兩者都正規化到 0-1。"""
    body = body_of(text)
    out: dict[str, float] = {}
    total_chars = max(len(body), 1)
    for lang, pat in SCRIPT_RANGES.items():
        out[lang] = len(re.findall(pat, body)) / total_chars

    words = re.findall(r"[a-zA-ZÀ-ÿĀ-žА-яÀ-ɏ]+", body.lower())
    n = len(words)
    if n >= MIN_TOKENS:
        for lang, fw in FUNCTION_WORDS.items():
            out[lang] = sum(1 for w in words if w in fw) / n
    else:
        for lang in FUNCTION_WORDS:
            out.setdefault(lang, 0.0)
    return out


def judge(path: Path, target: str) -> dict:
    text = path.read_text(encoding="utf-8", errors="replace")
    body = body_of(text)
    words = re.findall(r"[a-zA-ZÀ-ÿĀ-žÀ-ɏ]+", body.lower())
    scores = score(text)
    ranked = sorted(scores.items(), key=lambda kv: kv[1], reverse=True)
    best, best_s = ranked[0]
    tgt_s = scores.get(target, 0.0)

    verdict = "ok"
    if len(words) < MIN_TOKENS and target in LATIN_LANGS:
        verdict = "skip-too-short"
    elif best == target:
        verdict = "ok"
    elif tgt_s == 0 or best_s > tgt_s * FAIL_RATIO:
        verdict = "fail"
    else:
        verdict = "warn"
    return {
        "path": str(path.relative_to(REPO)),
        "target": target,
        "detected": best,
        "verdict": verdict,
        "target_score": round(tgt_s, 4),
        "detected_score": round(best_s, 4),
        "tokens": len(words),
    }


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("paths", nargs="*", help="譯文檔案路徑（語言從 knowledge/<lang>/ 推得）")
    ap.add_argument("--scan", help="掃整個語言目錄；'all' 掃全部")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    targets: list[tuple[Path, str]] = []
    if args.scan:
        langs = ALL_LANGS if args.scan == "all" else args.scan.split(",")
        for lang in langs:
            d = KNOWLEDGE / lang
            if not d.is_dir():
                continue
            for p in sorted(d.rglob("*.md")):
                if p.name.startswith("_"):
                    continue
                targets.append((p, lang))
    for raw in args.paths:
        p = Path(raw)
        if not p.is_absolute():
            p = REPO / raw
        try:
            lang = p.relative_to(KNOWLEDGE).parts[0]
        except ValueError:
            sys.exit(f"❌ {raw} 不在 knowledge/ 底下，推不出目標語言")
        targets.append((p, lang))

    if not targets:
        sys.exit("用法：給檔案路徑，或 --scan <lang|all>")

    results = [judge(p, lang) for p, lang in targets]
    fails = [r for r in results if r["verdict"] == "fail"]
    warns = [r for r in results if r["verdict"] == "warn"]

    if args.json:
        print(json.dumps({"results": results, "fail": len(fails), "warn": len(warns)}, ensure_ascii=False, indent=1))
    else:
        for r in fails:
            print(f"❌ {r['path']}\n   目標 {r['target']}（{r['target_score']}）但看起來是 {r['detected']}（{r['detected_score']}）")
        for r in warns:
            print(f"⚠️  {r['path']}: 目標 {r['target']}({r['target_score']}) vs 最像 {r['detected']}({r['detected_score']}) — 分數接近，請人看")
        print(f"\n{len(fails)} fail / {len(warns)} warn / {len(results)} 檔")

    sys.exit(1 if fails else 0)


if __name__ == "__main__":
    main()
