#!/usr/bin/env bash
# translation-ratio-check.sh — 翻譯 PR 審核第一道檢查
#
# 用法:
#   bash scripts/tools/translation-ratio-check.sh --pr 367
#   bash scripts/tools/translation-ratio-check.sh knowledge/ja/Society/article.md [...]
#   bash scripts/tools/translation-ratio-check.sh --all-ja
#
# 作用：
#   比對翻譯檔案跟 translatedFrom 指向的中文 SSOT 字數比率，
#   識別「摘要式翻譯」（AI 工具的預設行為）造成的內容截斷。
#
# 健全 ratio 範圍（2026-04-11 實測基準）：
#   zh → en:  2.20-3.50  (<1.50 = TRUNCATED)
#   zh → ja:  1.10-1.50  (<0.80 = TRUNCATED)
#   zh → ko:  1.20-1.65  (<0.85 = TRUNCATED)
#   zh → es/fr/de: 2.0-4.0  (<1.5 = TRUNCATED)
#
# 來源：2026-04-11 session α 審核 27 個翻譯 PR 的實戰經驗

set -o pipefail
cd "$(git rev-parse --show-toplevel 2>/dev/null || pwd)"

RED='\033[0;31m'; YEL='\033[0;33m'; GRN='\033[0;32m'
BLU='\033[0;34m'; DIM='\033[0;90m'; RST='\033[0m'

# Parse args
MODE="files"
PR_NUM=""
FILES=()

if [[ "${1:-}" == "--pr" ]] && [[ -n "${2:-}" ]]; then
  MODE="pr"
  PR_NUM="$2"
elif [[ "${1:-}" == --all-* ]]; then
  # 2026-07-25 泛化：原本只硬編碼 --all-ja 與 --all-en，其他語言傳進來會被
  # 當成檔名（FILES=("--all-ar")）→ 找不到檔案 → 假 FAIL 1/1。新語言出生時
  # 沒人會想到這裡也寫死了語言（神經迴路：新語言出生時感知系統不會自動更新）。
  MODE="all-lang"
  ALL_LANG="${1#--all-}"
elif [[ "${1:-}" == "--help" ]] || [[ -z "${1:-}" ]]; then
  grep "^#" "$0" | head -25
  exit 0
else
  FILES=("$@")
fi

# Collect files (bash 3 compatible — no mapfile)
if [[ "$MODE" == "pr" ]]; then
  while IFS= read -r line; do
    [[ -n "$line" ]] && FILES+=("$line")
  done < <(gh pr diff "$PR_NUM" --name-only 2>/dev/null | grep "^knowledge/" | grep -v "_translations.json")
  if [[ ${#FILES[@]:-0} -eq 0 ]]; then
    echo -e "${RED}❌ 無法取得 PR #$PR_NUM 的檔案清單${RST}"
    exit 1
  fi
  # 2026-08-27 修：--pr 模式以前只拿檔名，然後對「本機工作樹」open() 它。
  # 但翻譯 PR 幾乎都是新增檔案，那些路徑在 main 上本來就不存在 → 每一個
  # 新翻譯 PR 都穩定回 MISSING → ❌ FAIL「TRUNCATED translations require rework」。
  # MEMORY §神經迴路 指名本工具是「翻譯審核第一道檢查」，所以這條假 FAIL
  # 是照著 SOP 走就會撞到的。實測 #1600/#1601/#1602 三篇 ratio 分別 1.50/3.69/3.25
  # 全在 band 內，工具卻三篇都判 FAIL。
  # 修法：把 PR 內容取進暫存區（路徑結構不變，語言偵測與 translatedFrom 解析照舊），
  # 譯文讀暫存區、zh 源仍讀 main 工作樹 —— 被量的是 PR 的內容，量尺是 main 的。
  # 同 MAINTAINER-PIPELINE §診斷紀律「把 PR 的內容檔帶進 main 樹跑」。
  PR_STAGE="$(mktemp -d)"
  trap 'rm -rf "$PR_STAGE"' EXIT
  git fetch origin "pull/$PR_NUM/head:refs/twmd/ratio-pr$PR_NUM" -f -q 2>/dev/null || true
  for _f in "${FILES[@]}"; do
    mkdir -p "$PR_STAGE/$(dirname "$_f")"
    git show "refs/twmd/ratio-pr$PR_NUM:$_f" > "$PR_STAGE/$_f" 2>/dev/null || rm -f "$PR_STAGE/$_f"
  done
  git update-ref -d "refs/twmd/ratio-pr$PR_NUM" 2>/dev/null || true
elif [[ "$MODE" == "all-lang" ]]; then
  if [[ ! -d "knowledge/$ALL_LANG" ]]; then
    echo -e "${RED}❌ knowledge/$ALL_LANG 不存在（語言代碼打錯？）${RST}"
    exit 1
  fi
  while IFS= read -r line; do
    FILES+=("$line")
  done < <(find "knowledge/$ALL_LANG/" -name '*.md' ! -name '_*' 2>/dev/null | sort)
  if [[ ${#FILES[@]:-0} -eq 0 ]]; then
    echo -e "${YEL:-}⚠️  knowledge/$ALL_LANG 沒有譯文${RST}"
    exit 0
  fi
fi

# Run Python for accurate character counting (handles unicode properly)
python3 <<PYEOF
import re, sys, os, json

files = [$(printf '"%s",' "${FILES[@]}")]
files = [f for f in files if f]

# --pr 模式下譯文的實體在暫存區（見上方 shell 段註解）；zh 源一律讀 main 工作樹。
PR_STAGE = "${PR_STAGE:-}"

def resolve(path):
    """譯文優先讀 PR 暫存區，讀不到再退回工作樹。"""
    if PR_STAGE:
        staged = os.path.join(PR_STAGE, path)
        if os.path.exists(staged):
            return staged
    return path

def get_body(content):
    m = re.match(r'^---\n.*?\n---\n(.*)', content, re.DOTALL)
    return m.group(1) if m else content

def detect_lang(path):
    m = re.match(r'knowledge/([a-z]{2,5})/', path)
    if not m: return 'zh'
    return m.group(1)

# Healthy ratio ranges — SSOT 是 scripts/tools/lang-sync/ratio-bands.json
# (OBSERVER-QUEUE #19，2026-08-06 收斂)。以下 _FALLBACK_RANGES 只在 JSON
# 讀不到時（fresh-clone / 部分 checkout）當備援，數值與 JSON 逐字同步，
# 別在這裡改數字——改 JSON。
#
# 教訓（2026-07-25 ru 校準）：本表單位是「字元比」不是 bytes 比——首次定案時
# 用 bytes 算差了 1.5 倍（西里爾 2 bytes/char vs 中文 3），band 訂太緊而把
# 健康譯文全報 LONG。新語言定 band 一律用本工具自己的輸出，不另外算。
_FALLBACK_RANGES = {
    'en':    (1.50, 2.20, 3.50),   # (truncated_below, healthy_min, healthy_max)
    'ja':    (0.80, 1.10, 1.50),
    'ko':    (0.85, 1.20, 1.65),
    'es':    (1.50, 2.00, 4.00),
    'fr':    (1.50, 2.00, 4.00),
    'de':    (1.50, 2.00, 4.00),
    'vi':    (1.50, 2.00, 4.30),  # 2026-07-18 Stage 2 校準定案（實測 2.31-3.81，n=3）
    'id':    (1.50, 2.00, 4.30),  # 2026-07-18 Stage 2 校準定案（實測 2.32-3.58，n=3）
    'pt':    (1.50, 2.00, 4.30),  # 2026-07-18 Stage 2 校準定案（實測 2.44-3.97，n=4）
    'hi':    (1.50, 2.00, 4.00),  # 2026-07-18 Stage 2 校準定案（實測 2.20-3.38，n=3；天城文預想較緊湊被實測推翻）
    'ar':    (1.50, 2.00, 3.30),  # 2026-07-25 Stage 3 首批定案（本工具字元比實測
                                  # 2.08-2.95 中位 2.65，n=21）
    'ru':    (1.60, 2.20, 3.90),  # 2026-07-25 Stage 3 首批定案（字元比實測
                                  # 2.31-3.74 中位 2.93，n=29；俄語詞長，上限最高）
    'zh-TW': (0.95, 1.00, 1.00),
}
_FALLBACK_DEFAULT = (0.55, 0.70, 1.30)

_BANDS_JSON_PATH = "scripts/tools/lang-sync/ratio-bands.json"
try:
    with open(_BANDS_JSON_PATH, encoding='utf-8') as _fh:
        _bands_doc = json.load(_fh)
    RANGES = {}
    for _lang, _b in _bands_doc['bands'].items():
        if _lang == '_default':
            continue
        RANGES[_lang] = (_b['truncated_below'], _b['healthy_min'], _b['healthy_max'])
    _default_band = _bands_doc['bands']['_default']
    DEFAULT_RANGE = (_default_band['truncated_below'], _default_band['healthy_min'], _default_band['healthy_max'])
except Exception as _e:
    print(f"⚠️  無法讀取 {_BANDS_JSON_PATH}（{_e}），fallback 用內嵌舊表", file=sys.stderr)
    RANGES = _FALLBACK_RANGES
    DEFAULT_RANGE = _FALLBACK_DEFAULT

PASS = 0
WARN = 0
FAIL = 0
results = []

for f in files:
    f_real = resolve(f)
    if not os.path.exists(f_real):
        results.append((f, 'MISSING', None, None, None))
        FAIL += 1
        continue

    lang = detect_lang(f)
    if lang == 'zh' or lang == 'zh-TW':
        # Skip zh source files in scanning mode
        continue

    with open(f_real, encoding='utf-8') as fh:
        content = fh.read()

    # Find translatedFrom
    m = re.search(r"translatedFrom:\s*['\"]?([^'\"\n]+)", content)
    if not m:
        results.append((f, 'NO_TRANSLATED_FROM', None, None, None))
        WARN += 1
        continue

    zh_rel = m.group(1).strip()
    zh_path = f"knowledge/{zh_rel}"
    if not os.path.exists(zh_path):
        results.append((f, 'ZH_MISSING', zh_rel, None, None))
        FAIL += 1
        continue

    with open(zh_path, encoding='utf-8') as fh:
        zh_content = fh.read()

    zh_body = get_body(zh_content)
    tr_body = get_body(content)

    if not zh_body:
        results.append((f, 'ZH_EMPTY_BODY', zh_rel, None, None))
        WARN += 1
        continue

    ratio = len(tr_body) / len(zh_body)

    # Section / footnote / url check
    zh_secs = len(re.findall(r'^## ', zh_content, re.M))
    tr_secs = len(re.findall(r'^## ', content, re.M))
    zh_fns = len(re.findall(r'^\[\^[\w-]+\]:', zh_content, re.M))
    tr_fns = len(re.findall(r'^\[\^[\w-]+\]:', content, re.M))
    zh_urls = zh_content.count('http')
    tr_urls = content.count('http')

    extra_info = {
        'secs': f"{zh_secs}→{tr_secs}",
        'fns': f"{zh_fns}→{tr_fns}",
        'urls': f"{zh_urls}→{tr_urls}",
    }

    # Determine verdict
    trunc, healthy_min, healthy_max = RANGES.get(lang, DEFAULT_RANGE)

    if ratio < trunc:
        verdict = 'TRUNCATED'
        FAIL += 1
    elif ratio < healthy_min:
        verdict = 'THIN'
        WARN += 1
    elif ratio > healthy_max:
        verdict = 'LONG'
        WARN += 1
    elif zh_urls >= 3 and tr_urls == 0:
        verdict = 'NO_URLS'
        WARN += 1
    elif tr_urls < zh_urls * 0.5 and zh_urls >= 5:
        verdict = 'URL_LOSS'
        WARN += 1
    elif zh_secs > 0 and tr_secs < zh_secs:
        verdict = f'MISSING_SECTIONS({zh_secs-tr_secs})'
        WARN += 1
    else:
        verdict = 'OK'
        PASS += 1

    results.append((f, verdict, zh_rel, ratio, extra_info))

# Print report
print()
print(f"{'File':<60} {'Ratio':>6}  {'Verdict':<20} {'Structure'}")
print("─" * 120)
for f, verdict, zh_rel, ratio, info in results:
    short = os.path.basename(f)[:58]
    if ratio is None:
        print(f"{short:<60} {'—':>6}  {verdict:<20} —")
        continue
    color = ''
    if verdict == 'OK':
        color = '\033[0;32m'  # green
    elif verdict in ('THIN', 'LONG', 'URL_LOSS', 'NO_URLS') or 'MISSING_SECTIONS' in verdict:
        color = '\033[0;33m'  # yellow
    else:
        color = '\033[0;31m'  # red
    reset = '\033[0m'
    s = f"secs={info['secs']} fns={info['fns']} urls={info['urls']}" if info else ''
    print(f"{short:<60} {ratio:>5.2f}  {color}{verdict:<20}{reset} {s}")

print()
print(f"\033[0;90m{'─'*120}\033[0m")
total = PASS + WARN + FAIL
if FAIL > 0:
    print(f"\033[0;31m❌ FAIL\033[0m: {FAIL} / {total}  (TRUNCATED translations require rework)")
elif WARN > 0:
    print(f"\033[0;33m⚠️  WARN\033[0m: {WARN} / {total}  (acceptable for merge + follow-up)")
else:
    print(f"\033[0;32m✅ PASS\033[0m: {PASS} / {total}")
print()

sys.exit(1 if FAIL > 0 else 0)
PYEOF
