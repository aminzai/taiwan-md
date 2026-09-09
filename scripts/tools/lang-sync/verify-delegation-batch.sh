#!/usr/bin/env bash
# verify-delegation-batch.sh — 對委派層產出的整批譯文跑完整七道閘＋結構對靶。
#
# 為什麼要這支：委派層一輪動輒十幾二十篇，逐篇手打七道閘指令是重複勞動，而重複
# 勞動會讓人開始跳步——2026-09-09 那一輪裡，agent 自述「七道閘全過」實際有問題的
# 有四篇（tags 整排沒翻／URL multiset 不符／視覺化模組整塊中文／整篇翻成英文），
# 全靠主 session 獨立重驗抓到。REFLEXES #31：agent claim 是線索不是事實，而
# 「一律重驗」只有在重驗夠便宜的時候才守得住。
#
# 它做的事：對每個未 commit 的譯文，從路徑推出語言與 zh 來源，逐一跑
#   1 target-language-check（語言正確性，2026-09-09 新閘）
#   2 verify-translation（結構／URL multiset／frontmatter，exit 非 0 = 硬失敗）
#   3 cjk-leak-check
#   4 cjk-adjacency-check
#   5 article-health --profile=pre-commit
# 結構對靶（enrich --check）需要對應派工單，路徑因批次而異，交給呼叫端自己跑。
#
# 用法：
#   bash scripts/tools/lang-sync/verify-delegation-batch.sh          # 掃所有未 commit 譯文
#   bash scripts/tools/lang-sync/verify-delegation-batch.sh vi       # 只掃某語言
set -uo pipefail
cd "$(dirname "$0")/../../.." || exit 1

FILTER="${1:-}"
# 不用 mapfile：macOS 內建的是 bash 3.2，沒有那個 builtin（同族陷阱見
# BABEL-VORTEX-LOOP §v1.42 家族的 bash readonly builtin 那條）。
FILES=$(git status --short knowledge/ | awk '{print $2}' | grep '\.md$' || true)
[ -z "$FILES" ] && { echo "沒有未 commit 的譯文"; exit 0; }

# SOP §四保命規則 1 的儀器化：agent 還在寫的檔案不算成品。這條規則寫在
# canonical 裡，但 2026-09-09 同一個下午我自己違反了兩次——第一次把重派中的
# 一篇判成「結構沒對上」，第二次一口氣把六篇還在寫的判成失敗，得出 32% 失敗率
# 的假結論。靠自覺記得的規則會在忙的時候失守，所以改成工具直接跳過。
QUIET_SECS=${QUIET_SECS:-60}
NOW=$(date +%s)

pass=0; fail=0; skipped=0; needs_review=0; failed_list=()
for f in $FILES; do
  lang="${f#knowledge/}"; lang="${lang%%/*}"
  # zh-TW 來源自己也會出現在 git status 裡（例如修來源端的壞連結時）。它沒有
  # translatedFrom，本來會被判成「找不到 zh 來源」的假紅燈。語言碼是兩碼小寫，
  # 分類名不是——用這個分辨，不用維護分類白名單。
  case "$lang" in [a-z][a-z]) ;; *) continue ;; esac
  [ -n "$FILTER" ] && [ "$lang" != "$FILTER" ] && continue
  mtime=$(stat -f %m "$f" 2>/dev/null || stat -c %Y "$f" 2>/dev/null || echo 0)
  age=$((NOW - mtime))
  if [ "$age" -lt "$QUIET_SECS" ]; then
    printf "⏳ %-58s %s 秒前才寫過，還在施工，跳過\n" "${f#knowledge/}" "$age"
    skipped=$((skipped+1)); continue
  fi
  # 從譯文的 translatedFrom 找 zh 來源——比從檔名反推可靠，因為 slug 跟中文檔名
  # 本來就不對應（那正是 _slug-map 存在的理由）
  zh=$(grep -m1 "^translatedFrom:" "$f" | sed "s/^translatedFrom:[[:space:]]*//; s/^['\"]//; s/['\"]$//")
  if [ -z "$zh" ] || [ ! -f "knowledge/$zh" ]; then
    echo "❌ $f — 找不到 zh 來源（translatedFrom=${zh:-空}）"
    fail=$((fail+1)); failed_list+=("$f: no-source"); continue
  fi

  # 閘門分兩級。硬失敗＝沒有已知假陽性家族的那些（語言錯、結構／URL 不符、
  # article-health hard）——命中就是錯。需人審＝cjk-leak 與 cjk-adjacency，
  # 它們有一整族記錄在案的合法命中：引號裡的專有名詞原名（Podcast 名、Facebook
  # 社團名、專輯名）、括號內原名對照、參考資料區的中文來源標題、小寫品牌名。
  # 2026-09-09 實測：de 那批三篇被判 leak／adjacency 失敗，逐篇看全是這類——
  # 「違章女生」是 Podcast 名、「鳥類窗殺通報」是社團名、DailyView 是品牌名。
  # 儀器的工作是把要看的東西縮到最小，不是替判斷做裁決（MANIFESTO §14）。
  reasons=(); review=()
  python3 scripts/tools/lang-sync/target-language-check.py "$f" >/dev/null 2>&1 || reasons+=("wrong-language")
  # 判準跟 dispatcher 的 verify_one() 對齊：看 --json 的 fails（硬失敗數），不看
  # exit code——verify-translation 對 WARN 回 exit 2，用 exit code 會把
  # 「description 太長」算成失敗（REFLEXES #83 的兩把尺）。
  vfails=$(python3 scripts/tools/lang-sync/verify-translation.py "knowledge/$zh" "$f" --json 2>/dev/null \
           | python3 -c "import json,sys;d=json.load(sys.stdin);print(d.get('fails',-1))" 2>/dev/null | head -1)
  [ "${vfails:-x}" = "0" ] || reasons+=("verify=${vfails:-parse-error}")
  python3 scripts/tools/article-health.py "$f" --profile=pre-commit --quiet 2>&1 | grep -q "passed=False" && reasons+=("health")
  python3 scripts/tools/lang-sync/cjk-leak-check.py "$f" >/dev/null 2>&1 || review+=("leak")
  python3 scripts/tools/lang-sync/cjk-adjacency-check.py "$f" >/dev/null 2>&1 || review+=("adjacency")
  # 契約長到九道閘之後，這支只驗到第七道就等於「我的尺比契約短」——agent 交回的
  # 東西有一整類我量不到（2026-09-09 兩件都是這樣被漏掉的：站內連結指向中文頁、
  # 自創的英文 slug 指向不存在的頁面）。閘門加進契約時，重驗器要一起長。
  # --vs-source：只擋這一輪新造的死連結。zh 原文自己就連錯的（全庫 64 條 / 34 檔）
  # 會讓每個語言版本都紅燈，而那不是譯者的錯也不是重譯能修的——那批屬 OBSERVER-QUEUE #55
  # 的來源端存量。閘門紅得沒道理，人就會學會忽略它。
  python3 scripts/tools/lang-sync/internal-link-check.py --vs-source "$f" >/dev/null 2>&1 \
    || reasons+=("dead-links(譯者新造)")
  # 站內連結在地化是「補做」不是「檢查」：agent 漏跑的話這裡跑完就對了，但要記一筆，
  # 因為那代表它自述的第 8 道閘是假的（REFLEXES #31）。
  nloc=$(python3 - "$f" "$lang" <<'PYEOF' 2>/dev/null
import sys, pathlib
sys.path.insert(0, "scripts/tools/lang-sync")
from cross_link_localizer import load_index, localize_body
p = pathlib.Path(sys.argv[1]); t = p.read_text(encoding="utf-8")
new, n = localize_body(t, sys.argv[2], load_index())
if n: p.write_text(new, encoding="utf-8")
print(n)
PYEOF
)
  [ "${nloc:-0}" != "0" ] && review+=("agent漏跑在地化(已補${nloc}個)")
  grep -q "\[\[" "$f" && reasons+=("wikilink殘留")

  if [ ${#reasons[@]} -gt 0 ]; then
    fail=$((fail+1)); failed_list+=("$f: ${reasons[*]}")
    printf "❌ %-58s %s\n" "${f#currency/}" "${reasons[*]}"
  elif [ ${#review[@]} -gt 0 ]; then
    pass=$((pass+1)); needs_review=$((needs_review+1))
    printf "👀 %-58s %s — 人審（多半是引號裡的專有名詞原名）\n" "${f#knowledge/}" "${review[*]}"
  else
    pass=$((pass+1))
  fi
done

echo
echo "════ ${pass} 通過（含 ${needs_review} 需人審）/ ${fail} 失敗 / ${skipped} 施工中跳過（靜置 ${QUIET_SECS}s）════"
if [ $fail -gt 0 ]; then
  echo "失敗的不要 commit——修好或退回重做（SOP §四：低命中當場補、高命中退回重做）"
  exit 1
fi
