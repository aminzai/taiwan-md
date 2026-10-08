"""tests/test_npm_audit_sweep.py — npm-audit-sweep.sh 兩個解析器的邊界。

這支工具的存在理由是 LESSONS `external-advisory-reddens-a-gate-and-not-our-code-
becomes-a-reason-not-to-act`（vc=3）：CI 的 contracts job 有四道 `npm audit`
用 `&&` 串著，第一道紅了後面三道不會跑，於是當班看到的永遠只有第一個路徑，
修好它紅燈就移到下一格。

兩件事必須被測住：
  1. 路徑清單從 workflow 解析，不寫死 — CI 多一道 audit 時工具跟著變
     （REFLEXES #83 兩把尺）。
  2. 解析失敗要印 PARSE_FAIL，不能回一個乾淨的 0
     （REFLEXES #85：「不知道」要有自己的符號）。
"""

from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
LIB = REPO / "scripts/tools/lib"


def _load(name, filename):
    spec = importlib.util.spec_from_file_location(name, LIB / filename)
    module = importlib.util.module_from_spec(spec)
    assert spec and spec.loader
    spec.loader.exec_module(module)
    return module


PARSER = _load("parse_audit_paths", "parse-audit-paths.py")
SUMMARIZER_PATH = LIB / "summarize-npm-audit.py"


# ── 路徑解析 ──────────────────────────────────────────────────────


def test_parses_the_real_workflow_in_order():
    """對真正那份 workflow 解析出四道 audit，順序跟 CI 一致。"""
    workflow = REPO / ".github/workflows/engineering-checks.yml"
    found = PARSER.parse(workflow.read_text(encoding="utf-8"))
    assert found == [
        ".",
        "docs/semiont/harvest/ui",
        "docs/semiont/harvest/backend",
        "workers/mcp",
    ]


def test_step_without_working_directory_is_repo_root():
    found = PARSER.parse(
        "jobs:\n"
        "  contracts:\n"
        "    steps:\n"
        "      - run: npm audit --audit-level=high\n"
    )
    assert found == ["."]


def test_working_directory_is_scoped_to_its_own_step():
    """下一個 step 的 working-directory 不能被前一道 audit 認領。"""
    found = PARSER.parse(
        "jobs:\n"
        "  contracts:\n"
        "    steps:\n"
        "      - run: npm audit --audit-level=high\n"
        "      - run: npm test\n"
        "        working-directory: some/app\n"
    )
    assert found == ["."]


def test_a_new_audit_step_shows_up_without_touching_the_tool():
    found = PARSER.parse(
        "jobs:\n"
        "  contracts:\n"
        "    steps:\n"
        "      - run: npm audit --audit-level=high\n"
        "      - run: npm ci && npm audit --audit-level=high\n"
        "        working-directory: a/one\n"
        "      - run: npm audit --audit-level=high\n"
        "        working-directory: b/two\n"
    )
    assert found == [".", "a/one", "b/two"]


def test_steps_without_npm_audit_are_ignored():
    found = PARSER.parse(
        "jobs:\n"
        "  contracts:\n"
        "    steps:\n"
        "      - run: npm ci --ignore-scripts --no-audit\n"
        "      - run: npm run build\n"
    )
    assert found == []


def test_quoted_working_directory_is_unquoted():
    found = PARSER.parse(
        "jobs:\n"
        "  contracts:\n"
        "    steps:\n"
        '      - run: npm audit --audit-level=high\n'
        '        working-directory: "quoted/app"\n'
    )
    assert found == ["quoted/app"]


# ── audit JSON 收斂 ───────────────────────────────────────────────


def _summarize(payload):
    proc = subprocess.run(
        [sys.executable, str(SUMMARIZER_PATH)],
        input=payload,
        capture_output=True,
        text=True,
    )
    return proc.stdout.splitlines(), proc.returncode


def _vuln(severity, fix_available):
    return {"severity": severity, "fixAvailable": fix_available}


def test_clean_audit_reports_zero():
    lines, code = _summarize(json.dumps({"vulnerabilities": {}}))
    assert code == 0
    assert lines[0] == "OK 0 0 0"


def test_counts_header_matches_detail_rows():
    """表頭的條數要等於明細行數 — 第一版少印最後一條卻照報總數。"""
    payload = json.dumps(
        {
            "vulnerabilities": {
                "braces": _vuln("high", {"name": "tailwindcss", "version": "4.3.3", "isSemVerMajor": True}),
                "fast-glob": _vuln("high", True),
                "seroval": _vuln("critical", True),
            }
        }
    )
    lines, code = _summarize(payload)
    assert code == 0
    status, highs, crits, blocked = lines[0].split()
    assert (status, highs, crits, blocked) == ("OK", "2", "1", "1")
    assert len(lines) - 1 == int(highs) + int(crits)


def test_semver_major_fix_is_flagged_as_a_decision():
    payload = json.dumps(
        {
            "vulnerabilities": {
                "tailwindcss": _vuln(
                    "high", {"name": "tailwindcss", "version": "4.3.3", "isSemVerMajor": True}
                )
            }
        }
    )
    lines, _ = _summarize(payload)
    assert lines[0] == "OK 1 0 1"
    assert lines[1] == "high\ttailwindcss\tMAJOR(tailwindcss@4.3.3)"


def test_non_major_fix_is_this_shifts_work():
    payload = json.dumps({"vulnerabilities": {"sharp": _vuln("high", True)}})
    lines, _ = _summarize(payload)
    assert lines[0] == "OK 1 0 0"
    assert lines[1] == "high\tsharp\tminor"


def test_no_fix_available_counts_as_blocked():
    payload = json.dumps({"vulnerabilities": {"braces": _vuln("high", False)}})
    lines, _ = _summarize(payload)
    assert lines[0] == "OK 1 0 1"
    assert lines[1] == "high\tbraces\tnone"


def test_moderate_and_low_are_below_the_gate():
    payload = json.dumps(
        {
            "vulnerabilities": {
                "sprintf-js": _vuln("moderate", True),
                "something": _vuln("low", True),
            }
        }
    )
    lines, _ = _summarize(payload)
    assert lines[0] == "OK 0 0 0"
    assert len(lines) == 1


def test_unparseable_input_says_parse_fail_not_zero():
    """離線或 npm 改格式時，要印 PARSE_FAIL 而不是一個看起來像全綠的 0。"""
    lines, code = _summarize("not json at all")
    assert code == 1
    assert lines[0] == "PARSE_FAIL"
