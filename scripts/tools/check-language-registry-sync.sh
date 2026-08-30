#!/usr/bin/env bash
# check-language-registry-sync.sh
#
# 確認 src/config/languages.ts 和 languages.mjs 的 LANGUAGES 列表同步。
# 語言順序與每個欄位都必須一致。pre-commit hook 應該跑這個。
#
# 為什麼有兩份檔案：Vite SSR prerender chunks 會 bundle .mjs 但破壞 filesystem
# 相對路徑，所以不能用 readFileSync 讀 JSON。最可靠的方式是兩個檔案都 inline 資料。
set -uo pipefail
cd "$(dirname "$0")/../.."

# 比對完整 registry entry；只比 code 會漏掉 enabled / hreflang / dir 等漂移。
node scripts/tools/compare-language-registries.mjs || exit 1

# Extract codes for the VIZ_STRINGS coverage check below.
TS_CODES=$(grep -oE "code: '[^']+'" src/config/languages.ts | sed "s/code: '//;s/'$//" | sort | tr '\n' ',' | sed 's/,$//')

# ── VIZ_STRINGS 必須覆蓋註冊表的每一個語言（2026-07-26 加）────────────────────
# 為什麼在這支腳本裡：VIZ_STRINGS 是「以語言碼為 key 的第三份 registry mirror」，
# 跟上面 .ts / .mjs 兩份是同一類東西，漂掉的後果也一樣。
#
# 實際踩過的坑：這張表的型別原本寫死六語 union，查找是
# `VIZ_STRINGS[lang] ?? VIZ_STRINGS['zh-TW']`，於是 2026-07 出生的
# vi / id / pt / hi / ar / ru 六語**靜靜退回中文**。量測到的後果：這六語的 2,052 個
# 頁面上共有 43,045 個中文 aria-label，阿拉伯文 / 印地文 / 俄文讀者的螢幕閱讀器，
# 在每一個腳註連結上都唸中文。缺翻譯會被 i18n-coverage-audit 抓到，
# 這種「有接縫但表裡沒這一列」的漂移不會，因為 `??` 讓它永遠有值、永不報錯。
#
# 型別現在是 `Record<Lang, VizStrings>`，新語言出生會是 compile error。但本 repo
# 的 CI 沒有任何 typecheck step（無 tsc、無 astro check），所以型別只在編輯器裡
# 生效。這個檢查是它在 CI 的替身。
#
# 注意：這裡刻意**不**檢查譯文品質，只檢查「有沒有這一列」。品質是翻譯工作。
VIZ_FILE="src/utils/article-render.ts"
if [[ -f "$VIZ_FILE" ]]; then
  # 只取 VIZ_STRINGS 區塊內縮排 2 格的 key，避免撈到欄位名或其他表
  VIZ_CODES=$(awk '
    /^const VIZ_STRINGS/ { inside = 1; next }
    inside && /^};/       { inside = 0 }
    inside && match($0, /^  '"'"'?[a-zA-Z][a-zA-Z-]*'"'"'?:[[:space:]]*\{/) {
      key = $0
      gsub(/^  '"'"'?/, "", key)
      sub(/'"'"'?:[[:space:]]*\{.*$/, "", key)
      print key
    }
  ' "$VIZ_FILE" | sort | tr '\n' ',' | sed 's/,$//')

  if [[ -z "$VIZ_CODES" ]]; then
    echo "❌ 在 $VIZ_FILE 找不到 VIZ_STRINGS 的語言 key"
    echo "   這支檢查靠 awk 抓縮排 2 格的 key。如果表的形狀改了，請一起更新這裡"
    echo "   抓不到就當失敗，不要靜默通過（不然這道防線會無聲消失）。"
    exit 1
  fi

  if [[ "$VIZ_CODES" != "$TS_CODES" ]]; then
    echo "❌ VIZ_STRINGS 與語言註冊表漂移！"
    echo "   registry:    $TS_CODES"
    echo "   VIZ_STRINGS: $VIZ_CODES"
    echo ""
    echo "   後果不是報錯，是靜默退回中文：$VIZ_FILE 的查找是"
    echo "   \`VIZ_STRINGS[lang] ?? VIZ_STRINGS['zh-TW']\`，缺的語言會拿到整套中文"
    echo "   UI 字串（腳註 aria-label、資料來源前綴、圖表標籤）。"
    echo ""
    echo "   修法：在 $VIZ_FILE 的 VIZ_STRINGS 補上缺的語言，10 個欄位都要有。"
    exit 1
  fi

  echo "✅ VIZ_STRINGS 覆蓋註冊表全部語言 ($VIZ_CODES)"
fi

# ── 譯文 QA 接線必須覆蓋每個有內容的語言（2026-08-30 加）────────────────────
# 跟上面 VIZ_STRINGS 同一類：以語言碼為 key 的第 N 份 registry mirror，漂掉不報錯。
#
# 實際踩過的坑：de 於 2026-08-19 以 scaffold（enabled: false）進註冊表，投稿者
# 持續送 de 譯文進 knowledge/de/（8/30 已 77 篇），但
#   (a) .github/workflows/translation-check.yml 的 paths filter 沒有 knowledge/de/**
#       → de 譯文 PR 從來不觸發 check-translation，實測 PR #1627 只有 2 條 check，
#         同批 hi/id 的 PR 有 3 條；
#   (b) script-presence-check.py 沒有 de 的文字系統 profile
#       → 舊版遇到不支援的語言直接 continue，最後印 `✅ 0 檔通過` 並 exit 0。
# 兩道都不是紅燈，是「沒有燈」。抓到它的不是任何閘門，是投稿者自己順手跑了
# repo 的 QA 工具然後寫在 PR 留言裡。
#
# 判準刻意用「knowledge/<lang>/ 有沒有內容」而不是 registry 的 enabled 旗標：
# 內容會比上線決定早幾個月進來，而沒有 QA 的那段空窗正是它需要被守的時候。
KNOWLEDGE_LANGS=$(
  for code in $(echo "$TS_CODES" | tr ',' '\n'); do
    [[ "$code" == "zh-TW" ]] && continue          # 來源語言，不是譯文目標
    [[ -d "knowledge/$code" ]] || continue         # 還沒有內容的 scaffold 先不守
    echo "$code"
  done | sort
)

WF="$(cd "$(dirname "$0")/../.." && pwd)/.github/workflows/translation-check.yml"
MISSING_WF=""
for code in $KNOWLEDGE_LANGS; do
  grep -qE "^[[:space:]]*-[[:space:]]*'knowledge/$code/\*\*'" "$WF" || MISSING_WF="$MISSING_WF $code"
done

# 問這道閘門自己支援哪些語言，不要在這裡重抄一份表（抄了就是第 N+1 份 mirror）。
# 用 import 讀 SUPPORTED_LANGS 而不是對每個語言跑一次 CLI：後者會把整個 9,000 檔
# 語料掃 12 遍（實測 11 秒），對 pre-commit hook 太貴，貴到最後會被人拿掉。
MISSING_PROFILE=$(
  python3 - "$KNOWLEDGE_LANGS" <<'PY'
import importlib.util, pathlib, sys
p = pathlib.Path("scripts/tools/lang-sync/script-presence-check.py")
spec = importlib.util.spec_from_file_location("spc", p)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)
# en 沒有 profile 是對的，不是缺口：這道閘門問的是「這篇宣稱已譯的文章其實是不是
# 英文」，對英文版本身問這句話沒有意義。它仍然要在 workflow paths 裡（上面那圈查），
# 因為 ratio / 結構 / 腳註那些檢查對 en 一樣適用。
want = [c for c in sys.argv[1].split() if c != "en"]
print(" ".join(c for c in want if c not in mod.SUPPORTED_LANGS))
PY
)

# cjk-residue-check 的 TARGET_LANGS 是同一類 mirror（ja/ko 不在其中是刻意的：
# 兩者混寫漢字合法）。它遇到不認識的語言會 exit 1 叫出來，不像 script-presence
# 舊版靜默通過——但沒有人會替它跑，所以一樣要在這裡對賬。
MISSING_CJK=$(
  python3 - "$KNOWLEDGE_LANGS" <<'PY'
import importlib.util, pathlib, sys
p = pathlib.Path("scripts/tools/lang-sync/cjk-residue-check.py")
spec = importlib.util.spec_from_file_location("cjk", p)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)
want = [c for c in sys.argv[1].split() if c not in ("ja", "ko")]
print(" ".join(c for c in want if c not in mod.TARGET_LANGS))
PY
)

if [[ -n "$MISSING_WF" || -n "$MISSING_PROFILE" || -n "$MISSING_CJK" ]]; then
  echo "❌ 有內容的語言沒有接上譯文 QA！"
  [[ -n "$MISSING_WF" ]] && {
    echo "   translation-check.yml paths 缺:$MISSING_WF"
    echo "     → 後果：這些語言的譯文 PR 不觸發 check-translation，CI 少一條而不是紅一條"
    echo "     → 修法：在 .github/workflows/translation-check.yml 的 paths 補 'knowledge/<lang>/**'"
  }
  [[ -n "$MISSING_PROFILE" ]] && {
    echo "   script-presence-check.py 缺文字系統 profile:$MISSING_PROFILE"
    echo "     → 後果：「宣稱已譯但本文是英文」這道閘門對這些語言不存在"
    echo "     → 修法：在該檔 NATIVE_SCRIPT 或 DIACRITICS 補一列"
  }
  [[ -n "$MISSING_CJK" ]] && {
    echo "   cjk-residue-check.py TARGET_LANGS 缺:$MISSING_CJK"
    echo "     → 後果：整段沒翻的中文留在譯文正文裡不會被擋下"
    echo "     → 修法：在該檔 TARGET_LANGS 補上（ja/ko 例外，混寫漢字合法）"
  }
  exit 1
fi

echo "✅ 譯文 QA 接線覆蓋所有有內容的語言 ($(echo $KNOWLEDGE_LANGS | tr '\n' ' '))"
