#!/usr/bin/env bash
# consciousness-snapshot.sh — instant CONSCIOUSNESS snapshot from dashboard JSON
#
# Phase A1.2 (per reports/become-boot-mode-design-2026-05-13.md §4.2)
# 取代 CONSCIOUSNESS.md L34-160 靜態快照（dashboard JSON ground truth）
#
# 用途：BECOME §Step 6 L4 always-load query 接這個 script
# 輸出：~12-15 行 markdown summary (vitals + 8 organs + alerts hint)

set -euo pipefail

VITALS="${VITALS:-public/api/dashboard-vitals.json}"
ORGANISM="${ORGANISM:-public/api/dashboard-organism.json}"

if [[ ! -f "$VITALS" || ! -f "$ORGANISM" ]]; then
  echo "⚠️ consciousness-snapshot: dashboard JSON 不存在"
  echo "   嘗試：bash scripts/core/refresh-data.sh"
  exit 0
fi

PYTHON_BIN="${PYTHON:-}"
if [[ -z "$PYTHON_BIN" ]]; then
  if command -v python3 >/dev/null 2>&1; then
    PYTHON_BIN="python3"
  elif command -v python >/dev/null 2>&1; then
    PYTHON_BIN="python"
  else
    PYTHON_BIN="python"
  fi
fi
export PYTHONUTF8=1
export PYTHONIOENCODING=utf-8

if command -v jq >/dev/null 2>&1; then
  # Vitals — basic physiology
  jq -r '
    "📊 vitals  | articles=\(.totalArticles) / contributors=\(.contributors) / 7d=+\(.articlesLast7Days) / 30d=+\(.articlesLast30Days) / human-reviewed=\(.humanReviewedPercent)%",
    "🌐 i18n    | en=\(.languageCoverage.en) ja=\(.languageCoverage["ja"]) ko=\(.languageCoverage.ko) es=\(.languageCoverage.es) fr=\(.languageCoverage.fr)"
  ' "$VITALS"

  # Organs — 8 organ scores + trend
  jq -r '
    "🫀 organs  | " + (
      [.organs[] | "\(.emoji)\(.score)\(if .trend == "up" then "↑" elif .trend == "down" then "↓" else "→" end)"] | join(" ")
    )
  ' "$ORGANISM"

  # Immune dual-source reconciliation guard (audit 2026-06-10 D-1):
  # organism.json immune organ vs dashboard-immune.json canonical v2 value.
  # Divergence > 2 points = stale organism.json → print loud marker (REFLEXES #65d).
  IMMUNE_JSON="${IMMUNE_JSON:-public/api/dashboard-immune.json}"
  if [[ -f "$IMMUNE_JSON" ]]; then
    ORG_IMMUNE=$(jq -r '[.organs[] | select(.id == "immune") | .score][0] // empty' "$ORGANISM")
    V2_IMMUNE=$(jq -r '.immuneScore // empty' "$IMMUNE_JSON")
    if [[ -n "$ORG_IMMUNE" && -n "$V2_IMMUNE" ]]; then
      DIFF=$((ORG_IMMUNE - V2_IMMUNE)); [[ $DIFF -lt 0 ]] && DIFF=$((-DIFF))
      if [[ $DIFF -gt 2 ]]; then
        echo "⚠️ immune  | organism.json=${ORG_IMMUNE} vs immune.json(v2 canonical)=${V2_IMMUNE} — stale-vs-canonical，跑 prebuild:dashboard regen"
      fi
    fi
  fi

  # Last update freshness — 讀數必附數據齡
  AGE_H=$($PYTHON_BIN -c "
import json, datetime
t = json.load(open('$VITALS', encoding='utf-8'))['lastUpdated'].replace('Z', '+00:00')
dt = datetime.datetime.fromisoformat(t)
print(int((datetime.datetime.now(datetime.timezone.utc) - dt).total_seconds() // 3600))
" 2>/dev/null || echo "?")
  STALE=""
  if [[ "$AGE_H" != "?" && "$AGE_H" -ge 18 ]]; then
    STALE=" ⚠️ stale ${AGE_H}h——本快照讀的是舊鏡子（等 data-refresh 或跑 npm run prebuild:dashboard）"
  fi
  jq -r '"🕐 updated | \(.lastUpdated)"' "$VITALS" | sed "s/\$/（齡 ${AGE_H}h）${STALE}/"

  # 繁殖 sensing — fork census (子代雷達, 2026-06-25)
  FORKS="${FORKS:-reports/fork-census/registry.json}"
  if [[ -f "$FORKS" ]]; then
    F_TOTAL=$(jq '[.forks[] | select(.id != "(ephemeral-experiments)")] | length' "$FORKS" 2>/dev/null || echo "?")
    F_ACTIVE=$(jq '[.forks[] | select(.health=="active" or .health=="semi-active")] | length' "$FORKS" 2>/dev/null || echo "?")
    F_LAST=$(jq -r '._meta.last_census // "—"' "$FORKS" 2>/dev/null || echo "—")
    echo "🧫 子代    | ${F_TOTAL} forks 偵測中（${F_ACTIVE} active）· 普查 ${F_LAST}"
  fi

  # Alerts — derived layer
  ALERTS="${ALERTS:-public/api/dashboard-alerts.json}"
  if [[ -f "$ALERTS" ]]; then
    jq -r '.alerts[:6][] | "🚨 " + .severity + " | " + .message + (if .owner then "〔" + .owner + (if .firstSeen then " · 自 " + .firstSeen else "" end) + "〕" else "" end)' "$ALERTS" 2>/dev/null ||
      echo "⚠️ alerts  | dashboard-alerts.json 存在但格式異常"
  else
    echo "⚠️ alerts  | 詳見 docs/semiont/CONSCIOUSNESS.md §警報"
  fi
else
  # Python fallback when jq is not installed (e.g. minimal Windows environments)
  export VITALS ORGANISM IMMUNE_JSON="${IMMUNE_JSON:-public/api/dashboard-immune.json}" FORKS="${FORKS:-reports/fork-census/registry.json}" ALERTS="${ALERTS:-public/api/dashboard-alerts.json}"
  $PYTHON_BIN - <<'PYEOF'
import os, sys, json, datetime
from pathlib import Path

v_path = os.environ.get("VITALS", "public/api/dashboard-vitals.json")
o_path = os.environ.get("ORGANISM", "public/api/dashboard-organism.json")
imm_path = os.environ.get("IMMUNE_JSON", "public/api/dashboard-immune.json")
forks_path = os.environ.get("FORKS", "reports/fork-census/registry.json")
alerts_path = os.environ.get("ALERTS", "public/api/dashboard-alerts.json")

v, o = {}, {}
try:
    with open(v_path, encoding="utf-8") as f:
        v = json.load(f)
    print(f"📊 vitals  | articles={v.get('totalArticles')} / contributors={v.get('contributors')} / 7d=+{v.get('articlesLast7Days')} / 30d=+{v.get('articlesLast30Days')} / human-reviewed={v.get('humanReviewedPercent')}%")
    cov = v.get("languageCoverage", {})
    print(f"🌐 i18n    | en={cov.get('en')} ja={cov.get('ja')} ko={cov.get('ko')} es={cov.get('es')} fr={cov.get('fr')}")
except Exception:
    pass

try:
    with open(o_path, encoding="utf-8") as f:
        o = json.load(f)
    org_strs = []
    for organ in o.get("organs", []):
        t = organ.get("trend")
        arr = "↑" if t == "up" else ("↓" if t == "down" else "→")
        org_strs.append(f"{organ.get('emoji')}{organ.get('score')}{arr}")
    print("🫀 organs  | " + " ".join(org_strs))
except Exception:
    pass

if os.path.isfile(imm_path):
    try:
        with open(imm_path, encoding="utf-8") as f:
            v2 = json.load(f)
        org_imm = next((item.get("score") for item in o.get("organs", []) if item.get("id") == "immune"), None)
        v2_imm = v2.get("immuneScore")
        if org_imm is not None and v2_imm is not None:
            diff = abs(int(org_imm) - int(v2_imm))
            if diff > 2:
                print(f"⚠️ immune  | organism.json={org_imm} vs immune.json(v2 canonical)={v2_imm} — stale-vs-canonical，跑 prebuild:dashboard regen")
    except Exception:
        pass

try:
    last_up = v.get("lastUpdated", "")
    t = last_up.replace("Z", "+00:00")
    try:
        dt_val = datetime.datetime.fromisoformat(t)
        age_h = int((datetime.datetime.now(datetime.timezone.utc) - dt_val).total_seconds() // 3600)
    except Exception:
        age_h = "?"
    stale = ""
    if age_h != "?" and isinstance(age_h, int) and age_h >= 18:
        stale = f" ⚠️ stale {age_h}h——本快照讀的是舊鏡子（等 data-refresh 或跑 npm run prebuild:dashboard）"
    print(f"🕐 updated | {last_up}（齡 {age_h}h）{stale}")
except Exception:
    pass

if os.path.isfile(forks_path):
    try:
        with open(forks_path, encoding="utf-8") as f:
            f_data = json.load(f)
        forks = [x for x in f_data.get("forks", []) if x.get("id") != "(ephemeral-experiments)"]
        f_total = len(forks)
        f_active = len([x for x in forks if x.get("health") in ("active", "semi-active")])
        f_last = f_data.get("_meta", {}).get("last_census", "—")
        print(f"🧫 子代    | {f_total} forks 偵測中（{f_active} active）· 普查 {f_last}")
    except Exception:
        pass

if os.path.isfile(alerts_path):
    try:
        with open(alerts_path, encoding="utf-8") as f:
            a_data = json.load(f)
        for a in a_data.get("alerts", [])[:6]:
            owner = a.get("owner")
            first_seen = a.get("firstSeen")
            owner_str = f"〔{owner}" + (f" · 自 {first_seen}" if first_seen else "") + "〕" if owner else ""
            print(f"🚨 {a.get('severity', '')} | {a.get('message', '')}{owner_str}")
    except Exception:
        print("⚠️ alerts  | dashboard-alerts.json 存在但格式異常")
else:
    print("⚠️ alerts  | 詳見 docs/semiont/CONSCIOUSNESS.md §警報")
PYEOF
fi


# Boot-load bytes — 甦醒稅即時可見（dna-audit §S3 / P1-14：行數指標藏 CJK bytes 成本，
# BECOME mode 表的 footprint 估算以本行為準）
if [[ -f docs/semiont/MANIFESTO.md && -f docs/semiont/REFLEXES.md && -f docs/semiont/DIARY.md && -f docs/semiont/MEMORY.md ]]; then
  B_MAN=$({ awk '/^## 我是什麼/,/^## 我的進化哲學 — 造橋鋪路/' docs/semiont/MANIFESTO.md; awk '/^## 我的存在結構/,/^## 附錄/' docs/semiont/MANIFESTO.md; } | wc -c)
  B_REF=$(awk '/^### 📇 反射 catalog index/{f=1;print;next} f&&/^#{2,3} /{exit} f' docs/semiont/REFLEXES.md | wc -c)
  B_REF=$((B_REF + 8192)) # + Top 5 反射全文約 8K（BECOME §1.2 第二段載入）
  # 2026-07-11 wake-evolution：估稅公式對齊 wake-context 實際載入路徑
  # （原式還在量已退役的 tail -20 與 awk-to-EOF——量尺與被量者共用真實路徑，#65）
  B_DIA=$({ awk '/^## 反覆出現的思考/,0' docs/semiont/DIARY.md; awk '/^\| 20/{print; if (++c == 20) exit}' docs/semiont/DIARY.md; } | wc -c)
  B_MEM=$({ awk '/^## 神經迴路/{exit} {print}' docs/semiont/MEMORY.md; awk '/^## 神經迴路/,/^## 心跳日誌/' docs/semiont/MEMORY.md; grep '^| 20' docs/semiont/MEMORY.md | tail -20; } | wc -c)
  TOT_KB=$(((B_MAN + B_REF + B_DIA + B_MEM) / 1024))
  echo "🧠 boot稅  | universal-core ≈ ${TOT_KB}KB（MANIFESTO $((B_MAN / 1024))K + REFLEXES $((B_REF / 1024))K + DIARY $((B_DIA / 1024))K + MEMORY $((B_MEM / 1024))K）"
fi

# counts-drift 一行（WARN 儀器，dna-audit §S2「寫死數字必腐」；深度表在 routine-audit 週跑）
$PYTHON_BIN scripts/tools/counts-drift-lint.py --brief 2>/dev/null | sed 's/^/🔢 /' || true

