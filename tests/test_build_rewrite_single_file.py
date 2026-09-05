"""
test_build_rewrite_single_file.py — scripts/tools/build-rewrite-single-file.py 單元測試

覆蓋（2026-09-05 v9 SSOT 拍板，單檔閱讀版改工具生成）：

1. 順序：兩個假 contract 依薄索引「Stage contract 派發表」表格列出現順序串接，
   而不是檔名字母序（用 B/A 反著命名的假檔，字母序會排錯，用來確認真的是照
   表格順序而非檔名排序）。
2. 派發表同一檔案連續出現兩次（模擬真實案例 Stage 3 contract 承載順序 9/9b）
   只取一次，不重複串接。
3. 標題降級：contract 的 H1 降成 H2、其餘標題各降一級，且刻意不做 fenced
   code block 例外——全篇（含假標題範例）逐級 +1 後，`grep -c '^# '`
   應該恰好剩 1（唯一真正的文件 H1），呼應驗收條件。
4. `--check` 過期偵測：磁碟版本被人手改（或來源 contract 被改而沒重新生
   成）後，`--check` 要能抓到並回傳非 0；重新生成後 `--check` 轉綠。
5. `--check` 不因每次生成都不同的 `generated_at` 時間戳而誤判過期
   （純呼叫 build() 兩次比較，不落地也不判斷 exit code）。
"""

from __future__ import annotations

import importlib.util
import re
from pathlib import Path

MODULE_PATH = (
    Path(__file__).resolve().parents[1]
    / "scripts"
    / "tools"
    / "build-rewrite-single-file.py"
)
SPEC = importlib.util.spec_from_file_location("build_rewrite_single_file", MODULE_PATH)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC and SPEC.loader
SPEC.loader.exec_module(MODULE)


FAKE_INDEX = """---
title: 'FAKE-REWRITE-PIPELINE'
description: 'fake thin index for testing'
type: 'pipeline-canonical'
status: 'canonical'
current_version: 'v1.3'
last_updated: 2026-01-01
last_session: 'fake-session-for-test'
---

# FAKE-REWRITE-PIPELINE — 假薄索引

一段跟正文無關的說明，內含一個指到別的目錄的連結
[reports/somewhere.md](../../reports/somewhere.md)——這個連結不該被當成
contract 檔算進派發順序（它有 `/`，也不在表格列裡）。

## 🗂️ Stage contract 派發表（fake）

| 順序 | Stage   | Contract 檔                            | 執行者 | gate |
| ---- | ------- | --------------------------------------- | ------ | ---- |
| 1    | Stage 甲 | [FAKE-STAGE-B.md](FAKE-STAGE-B.md)     | x      | y    |
| 2    | Stage 乙 | [FAKE-STAGE-A.md](FAKE-STAGE-A.md)     | x      | y    |
| 2b   | Stage 乙 收尾 | [FAKE-STAGE-A.md §尾段](FAKE-STAGE-A.md) | x | y |

## 下一節（派發表區塊到此結束，不該再被掃進去）

[reports/other.md](../../reports/other.md) 也不該被算進去。
"""

FAKE_STAGE_B = """---
title: 'FAKE-STAGE-B'
description: 'fake stage contract B'
type: 'pipeline-sub-canonical'
status: 'canonical'
current_version: 'v1.0'
last_updated: 2026-01-01
last_session: 'fake'
parent_canonical: 'FAKE-REWRITE-PIPELINE.md'
---

# Stage 甲 contract — 這是 B

B 的內容第一段，含關鍵字 CONTENT_B_MARKER。

## B 的子標題

再深一層。
"""

FAKE_STAGE_A = """---
title: 'FAKE-STAGE-A'
description: 'fake stage contract A'
type: 'pipeline-sub-canonical'
status: 'canonical'
current_version: 'v1.0'
last_updated: 2026-01-01
last_session: 'fake'
parent_canonical: 'FAKE-REWRITE-PIPELINE.md'
---

# Stage 乙 contract — 這是 A

A 的內容第一段，含關鍵字 CONTENT_A_MARKER。

## A 的子標題

```bash
# 這是 fence 內的假標題示範，全篇不做 fence 例外，這行也要被降級
echo hi
```
"""


def _write_fake_pipeline(tmp_path: Path) -> Path:
    pipelines_dir = tmp_path / "docs" / "pipelines"
    pipelines_dir.mkdir(parents=True)
    (pipelines_dir / "REWRITE-PIPELINE.md").write_text(FAKE_INDEX, encoding="utf-8")
    (pipelines_dir / "FAKE-STAGE-B.md").write_text(FAKE_STAGE_B, encoding="utf-8")
    (pipelines_dir / "FAKE-STAGE-A.md").write_text(FAKE_STAGE_A, encoding="utf-8")
    return pipelines_dir


# ---------------------------------------------------------------------------
# extract_dispatch_order
# ---------------------------------------------------------------------------


def test_dispatch_order_follows_table_not_filename_alphabetical():
    order = MODULE.extract_dispatch_order(FAKE_INDEX)
    # 檔名字母序會是 [A, B]；派發表順序是 [B, A]——確認真的照表格走。
    assert order == ["FAKE-STAGE-B.md", "FAKE-STAGE-A.md"]


def test_dispatch_order_dedups_consecutive_repeat_row():
    order = MODULE.extract_dispatch_order(FAKE_INDEX)
    # FAKE-STAGE-A.md 在表格出現兩列（2 與 2b，模擬真實 Stage 3 contract 案例）
    # 只能算一次。
    assert order.count("FAKE-STAGE-A.md") == 1


def test_dispatch_order_excludes_cross_directory_links():
    order = MODULE.extract_dispatch_order(FAKE_INDEX)
    assert not any("reports" in f for f in order)
    assert len(order) == 2


# ---------------------------------------------------------------------------
# build(): 順序 + 標題降級 + 單一 H1
# ---------------------------------------------------------------------------


def test_build_concatenates_in_dispatch_order(tmp_path):
    pipelines_dir = _write_fake_pipeline(tmp_path)
    doc = MODULE.build(pipelines_dir, generated_at="2026-01-01T00:00:00+08:00")

    pos_b = doc.index("CONTENT_B_MARKER")
    pos_a = doc.index("CONTENT_A_MARKER")
    assert pos_b < pos_a, "B 在派發表排第一，內容應該先出現"


def test_build_demotes_headings_by_one_level_everywhere():
    pipelines_dir_marker = "docs/pipelines"  # noqa: F841 (只是註記, 用不到)

    import tempfile

    with tempfile.TemporaryDirectory() as td:
        pipelines_dir = _write_fake_pipeline(Path(td))
        doc = MODULE.build(pipelines_dir, generated_at="2026-01-01T00:00:00+08:00")

        # contract 原本的 H1「# Stage 甲 contract — 這是 B」要降成 H2
        assert "## Stage 甲 contract — 這是 B" in doc
        assert "## Stage 乙 contract — 這是 A" in doc
        # 原本的 H2「## B 的子標題」要降成 H3
        assert "### B 的子標題" in doc
        assert "### A 的子標題" in doc

        # 全篇只有一個真正的 H1（本檔自己的標題），刻意不做 fence 例外，
        # 所以 fence 內的假標題範例也一起被降級——這正是驗收條件
        # `grep -c '^# '` 應為 1 的來源。
        h1_lines = [ln for ln in doc.split("\n") if re.match(r"^# ", ln)]
        assert len(h1_lines) == 1, h1_lines
        # fence 內的假標題示範被降級成 H2，不再是裸 H1
        assert "## 這是 fence 內的假標題示範" in doc


def test_demote_headings_caps_at_h6():
    body = "###### 已經是 H6 了"
    out = MODULE.demote_headings(body)
    assert out == "###### 已經是 H6 了" or out.startswith("######")
    assert not out.startswith("#######")


# ---------------------------------------------------------------------------
# --check 過期偵測
# ---------------------------------------------------------------------------


def test_check_passes_right_after_generation(tmp_path, capsys):
    pipelines_dir = _write_fake_pipeline(tmp_path)
    out_path = pipelines_dir / "FAKE-SINGLE-FILE.md"

    rc = MODULE.main(
        ["--pipelines-dir", str(pipelines_dir), "--out", str(out_path)]
    )
    assert rc == 0
    assert out_path.exists()

    rc_check = MODULE.main(
        ["--pipelines-dir", str(pipelines_dir), "--out", str(out_path), "--check"]
    )
    assert rc_check == 0
    assert "是最新的" in capsys.readouterr().out


def test_check_detects_staleness_when_source_contract_changes(tmp_path, capsys):
    pipelines_dir = _write_fake_pipeline(tmp_path)
    out_path = pipelines_dir / "FAKE-SINGLE-FILE.md"

    assert MODULE.main(["--pipelines-dir", str(pipelines_dir), "--out", str(out_path)]) == 0

    # 改動來源 contract 但不重新生成 —— 單檔閱讀版現在過期了。
    (pipelines_dir / "FAKE-STAGE-A.md").write_text(
        FAKE_STAGE_A.replace("CONTENT_A_MARKER", "CONTENT_A_MARKER_CHANGED"),
        encoding="utf-8",
    )

    rc_check = MODULE.main(
        ["--pipelines-dir", str(pipelines_dir), "--out", str(out_path), "--check"]
    )
    assert rc_check == 1
    assert "過期" in capsys.readouterr().out

    # 重新生成後 --check 應該轉綠
    assert MODULE.main(["--pipelines-dir", str(pipelines_dir), "--out", str(out_path)]) == 0
    rc_check_after = MODULE.main(
        ["--pipelines-dir", str(pipelines_dir), "--out", str(out_path), "--check"]
    )
    assert rc_check_after == 0


def test_check_ignores_generated_at_timestamp_only_diff(tmp_path):
    pipelines_dir = _write_fake_pipeline(tmp_path)

    doc_1 = MODULE.build(pipelines_dir, generated_at="2026-01-01T00:00:00+08:00")
    doc_2 = MODULE.build(pipelines_dir, generated_at="2026-01-02T12:34:56+08:00")

    # 兩次生成除了 generated_at 之外內容完全一樣（沒有真的改任何來源）
    assert doc_1 != doc_2  # 時間戳確實不同
    assert MODULE.normalize_for_diff(doc_1) == MODULE.normalize_for_diff(doc_2)


def test_missing_index_raises_clear_error(tmp_path):
    empty_dir = tmp_path / "empty-pipelines"
    empty_dir.mkdir()
    try:
        MODULE.build(empty_dir)
        assert False, "應該要 raise（找不到薄索引）"
    except FileNotFoundError as e:
        assert "薄索引" in str(e)
