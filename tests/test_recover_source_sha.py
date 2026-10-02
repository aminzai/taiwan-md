"""recover-source-sha.py 的答案卷是 c18e47390：2026-10-03 01:11 那一班逐篇用 git 歷史比對
雜湊，手工把 34 份譯文的 sourceCommitSha 改回真正翻譯的那一版。工具拿修補前的版本，
應該找回跟手工一樣的 sha，--check 應該對修補前亮紅、對修補後亮綠。"""
import importlib.util
import subprocess
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "recover_source_sha", ROOT / "scripts/tools/lang-sync/recover-source-sha.py"
)
RECOVER = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(RECOVER)

FIX = "c18e47390"
FILE = "knowledge/en/Technology/taiwan-software-industry-development.md"


def _git(*args):
    return subprocess.run(["git", *args], cwd=ROOT, capture_output=True, text=True)


pytestmark = pytest.mark.skipif(
    _git("rev-parse", "--is-shallow-repository").stdout.strip() != "false"
    or _git("cat-file", "-e", f"{FIX}^{{commit}}").returncode != 0,
    reason="需要完整歷史與 c18e47390",
)


def _prov(rev, tmp_path):
    p = tmp_path / f"{rev.replace('^', '_parent')}.md"
    p.write_text(_git("show", f"{rev}:{FILE}").stdout, encoding="utf-8")
    return RECOVER.read_provenance(p)


def test_recovers_the_hand_fixed_sha(tmp_path):
    before = _prov(f"{FIX}^", tmp_path)
    after = _prov(FIX, tmp_path)
    found, kind = RECOVER.recover(before)
    assert found[:7] == after["sha"][:7]
    assert kind


def test_check_flags_before_and_clears_after(tmp_path):
    assert RECOVER.check_current(_prov(f"{FIX}^", tmp_path)) != ""
    assert RECOVER.check_current(_prov(FIX, tmp_path)) == ""
