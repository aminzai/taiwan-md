#!/usr/bin/env python3
"""
build-rewrite-single-file.py — 從 REWRITE-PIPELINE.md v9 薄索引 ＋ 全部
REWRITE-STAGE-*.md contract 重組生成單檔閱讀版
docs/pipelines/REWRITE-PIPELINE-單檔案型完整流程.md。

背景（2026-09-05 哲宇拍板）：v9.0（2026-07-16）把 REWRITE-PIPELINE 拆成薄索引
＋多個 stage contract，那才是 SSOT。單檔版只是給「想一次讀完整條產線」的人
或 session 用的重組閱讀版，**不再手改**——改 v9 來源後重跑本工具。歷史上最
後一版手寫單檔（v8.0，2026-07-15，拆檔前）存檔在
docs/pipelines/archive/REWRITE-PIPELINE-v8.0-single-file-2026-07-15.md，本工具
不動它。

排序依據：檢查過所有 REWRITE-STAGE-*.md 的 frontmatter（截至本工具寫成時的
v9.7，磁碟上實際 11 個檔案——注意薄索引跨檔案職責分工表寫的「× 10」已經跟
實際份數脫鉤，是尚未被 counts-drift-lint.py 抓到的既有 drift，本工具不修
那句話，只是不採信那個數字），沒有任何機械可判定順序的欄位（無 `order` /
`stage_order`）——因此順序來源＝薄索引「Stage contract 派發表」表格
「Contract 檔」欄逐列出現順序，**份數永遠現算，不寫死**。同一檔案連續出現
兩次只取第一次（例如 Stage 3 contract 承載派發表順序 9 與 9b 兩列，只算一
次）。若未來有人在 stage frontmatter 加上機械順序欄位，這支工具的排序來源
需要一併更新（目前只讀派發表）。

Usage:
    python3 scripts/tools/build-rewrite-single-file.py
        重新生成並寫入 docs/pipelines/REWRITE-PIPELINE-單檔案型完整流程.md

    python3 scripts/tools/build-rewrite-single-file.py --check
        只驗證磁碟上的單檔閱讀版是否仍與「重新生成的結果」一致（忽略
        generated_at 時間戳），不一致 → 印訊息 + exit 1。給 pre-commit 用。

    python3 scripts/tools/build-rewrite-single-file.py --pipelines-dir DIR --out FILE
        覆寫來源目錄與輸出路徑（測試 / 除錯用）。
"""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from datetime import datetime
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent.parent
DEFAULT_PIPELINES_DIR = REPO_ROOT / "docs" / "pipelines"
INDEX_FILENAME = "REWRITE-PIPELINE.md"
OUT_FILENAME = "REWRITE-PIPELINE-單檔案型完整流程.md"
ARCHIVE_NOTE_PATH = "archive/REWRITE-PIPELINE-v8.0-single-file-2026-07-15.md"

DISPATCH_HEADING_MARKER = "Stage contract 派發表"

GENERATED_DOC_TITLE = "REWRITE-PIPELINE 單檔案型完整流程"
GENERATED_DESCRIPTION = (
    "文章改寫流程單檔閱讀版（工具生成，不要手改）— 依 REWRITE-PIPELINE.md 派發表"
    "順序，串接十個 REWRITE-STAGE-*.md contract 自動重組；SSOT 仍是 v9 拆檔版，"
    "本檔僅供一次讀完整條產線之用"
)

INTRO_TEMPLATE = (
    "> **本檔由工具生成，不要手改**——改 v9 來源"
    "（[REWRITE-PIPELINE.md](REWRITE-PIPELINE.md) 或任一 `REWRITE-STAGE-*.md`）"
    "後重跑 `python3 scripts/tools/build-rewrite-single-file.py` 重新生成。"
    f"歷史 v8.0 快照在 [{ARCHIVE_NOTE_PATH}]({ARCHIVE_NOTE_PATH})。"
)


# ---------------------------------------------------------------------------
# frontmatter 解析（純 stdlib，只需要純量欄位 + 切出 body，跟
# check-canonical-frontmatter.py 的 parse_frontmatter 同款簡化版）
# ---------------------------------------------------------------------------


def parse_frontmatter(text: str) -> tuple[dict[str, object], str]:
    """回傳 (frontmatter 欄位 dict, body 全文)。body 不含開頭 frontmatter 區塊。"""
    if not text.startswith("---\n"):
        raise ValueError("frontmatter 缺開頭 --- 分隔線")
    end = text.find("\n---\n", 4)
    if end == -1:
        raise ValueError("frontmatter 缺結尾 --- 分隔線")
    fm_text = text[4:end]
    body = text[end + len("\n---\n") :]

    fields: dict[str, object] = {}
    current_list: list[str] | None = None
    for line in fm_text.split("\n"):
        if not line.strip():
            continue
        if line.startswith("  - ") or line.startswith("  -"):
            if current_list is not None:
                current_list.append(line.lstrip(" -").strip().strip("'\""))
            continue
        m = re.match(r"^([a-zA-Z_][a-zA-Z0-9_]*):\s*(.*)$", line)
        if not m:
            continue
        key, val = m.group(1), m.group(2).strip()
        if val == "":
            current_list = []
            fields[key] = current_list
        elif val == "[]":
            fields[key] = []
            current_list = None
        else:
            fields[key] = val.strip("'\"")
            current_list = None
    return fields, body


def yaml_single_quote(s: str) -> str:
    """把字串包成 YAML single-quoted scalar（撇號用 '' 逃脫）。"""
    return "'" + s.replace("'", "''") + "'"


# ---------------------------------------------------------------------------
# 派發表順序抽取
# ---------------------------------------------------------------------------


def extract_dispatch_order(index_text: str) -> list[str]:
    """從薄索引「Stage contract 派發表」表格的『Contract 檔』欄，依表格列出
    現順序抽出 contract 檔名清單（連續重複只算一次；只認同目錄相對連結，排
    除表格上方說明段落裡指到 reports/ 等其他目錄的連結）。
    """
    lines = index_text.split("\n")
    start = None
    for i, ln in enumerate(lines):
        if ln.lstrip().startswith("#") and DISPATCH_HEADING_MARKER in ln:
            start = i
            break
    if start is None:
        raise ValueError(f"薄索引找不到派發表區塊（heading 需含「{DISPATCH_HEADING_MARKER}」）")

    link_re = re.compile(r"\(([^)\s]+\.md)(?:#[^)]*)?\)")
    order: list[str] = []
    for ln in lines[start + 1 :]:
        stripped = ln.lstrip()
        if stripped.startswith("#"):
            break  # 下一個 heading，派發表區塊結束
        if not stripped.startswith("|"):
            continue  # 只認表格列，跳過區塊上方/下方的說明文字連結
        for m in link_re.finditer(ln):
            target = m.group(1)
            if "/" in target:
                continue  # 跨目錄連結（如 ../../reports/x.md）不是 contract 檔
            if not order or order[-1] != target:
                order.append(target)

    if not order:
        raise ValueError("派發表區塊內找不到任何 contract 檔連結")
    return order


# ---------------------------------------------------------------------------
# git 資訊
# ---------------------------------------------------------------------------


def git_short_hash(path: Path) -> str:
    """path 最後一次變動的 commit 短 hash；非 git repo / 未 commit → 'uncommitted'。"""
    try:
        result = subprocess.run(
            ["git", "log", "-1", "--format=%h", "--", path.name],
            cwd=path.parent,
            capture_output=True,
            text=True,
            timeout=10,
        )
    except Exception:
        return "uncommitted"
    h = result.stdout.strip()
    return h if result.returncode == 0 and h else "uncommitted"


# ---------------------------------------------------------------------------
# 標題降級（H1→H2，其餘各降一級）
#
# 刻意不做 fenced code block 例外：contract 內有幾處用 ``` 區塊示範「研究報
# 告 / 佇列腳本長什麼樣」，裡面也有 `# 標題` 字樣。這支工具的任務是機械文字
# 轉換不是理解 markdown 語意——統一整份 body 逐級降級，範例區塊的相對階層
# 關係仍然完整保留（只是絕對層級一起 +1），換來的是全篇唯一一個真正的 H1
# （single-file 驗收條件：`grep -c '^# '` 全篇應為 1）。
# ---------------------------------------------------------------------------

_HEADING_RE = re.compile(r"^(#{1,6})(\s.*)$")


def demote_headings(body: str) -> str:
    out_lines: list[str] = []
    for ln in body.split("\n"):
        m = _HEADING_RE.match(ln)
        if m:
            new_level = min(len(m.group(1)) + 1, 6)
            ln = "#" * new_level + m.group(2)
        out_lines.append(ln)
    return "\n".join(out_lines)


def load_stage_body(path: Path) -> str:
    text = path.read_text(encoding="utf-8")
    _fields, body = parse_frontmatter(text)
    return body.strip("\n")


# ---------------------------------------------------------------------------
# 組裝
# ---------------------------------------------------------------------------


def build(pipelines_dir: Path, generated_at: str | None = None) -> str:
    index_path = pipelines_dir / INDEX_FILENAME
    if not index_path.exists():
        raise FileNotFoundError(f"找不到薄索引：{index_path}")
    index_text = index_path.read_text(encoding="utf-8")
    index_fields, _ = parse_frontmatter(index_text)
    order = extract_dispatch_order(index_text)

    current_version = str(index_fields.get("current_version", "unknown")) + "-single"
    last_updated = str(index_fields.get("last_updated", ""))
    last_session = str(index_fields.get("last_session", ""))

    generated_from: list[str] = [f"{INDEX_FILENAME}@{git_short_hash(index_path)}"]
    sections: list[str] = []
    for filename in order:
        stage_path = pipelines_dir / filename
        if not stage_path.exists():
            raise FileNotFoundError(f"派發表引用的 contract 檔不存在：{filename}")
        h = git_short_hash(stage_path)
        generated_from.append(f"{filename}@{h}")
        body = demote_headings(load_stage_body(stage_path))
        sections.append(f"<!-- ==== source: {filename} @ {h} ==== -->\n\n{body}")

    if generated_at is None:
        generated_at = datetime.now().astimezone().isoformat(timespec="seconds")

    fm: list[str] = ["---"]
    fm.append(f"title: {yaml_single_quote(GENERATED_DOC_TITLE)}")
    fm.append(f"description: {yaml_single_quote(GENERATED_DESCRIPTION)}")
    fm.append("type: 'pipeline-canonical'")
    fm.append("status: 'canonical'")
    fm.append(f"current_version: {yaml_single_quote(current_version)}")
    fm.append(f"last_updated: {last_updated}" if last_updated else "last_updated: ''")
    fm.append(f"last_session: {yaml_single_quote(last_session)}")
    fm.append("generated_from:")
    for g in generated_from:
        fm.append(f"  - {yaml_single_quote(g)}")
    fm.append(f"generated_at: {yaml_single_quote(generated_at)}")
    fm.append("---")

    doc = (
        "\n".join(fm)
        + "\n\n"
        + f"# {GENERATED_DOC_TITLE}\n\n"
        + INTRO_TEMPLATE
        + "\n\n"
        + "\n\n---\n\n".join(sections)
        + "\n"
    )
    return doc


def normalize_for_diff(text: str) -> str:
    """比對用正規化：抹掉每次生成都會變動的 generated_at，避免 --check 假陽性。"""
    return re.sub(r"^generated_at: '.*'$", "generated_at: '<GENERATED>'", text, flags=re.MULTILINE)


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--pipelines-dir",
        default=str(DEFAULT_PIPELINES_DIR),
        help="薄索引 + stage contract 所在目錄（預設 docs/pipelines/）",
    )
    parser.add_argument(
        "--out",
        default=None,
        help="輸出檔路徑（預設 <pipelines-dir>/" + OUT_FILENAME + "）",
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="只驗證磁碟版本是否過期（忽略 generated_at），不一致則 exit 1",
    )
    args = parser.parse_args(argv)

    pipelines_dir = Path(args.pipelines_dir).resolve()
    out_path = Path(args.out).resolve() if args.out else pipelines_dir / OUT_FILENAME

    try:
        new_content = build(pipelines_dir)
    except Exception as e:  # noqa: BLE001 — CLI 邊界，統一轉成人讀錯誤訊息
        print(f"❌ 生成失敗：{e}", file=sys.stderr)
        return 1

    if args.check:
        if not out_path.exists():
            print(f"❌ 單檔閱讀版過期，請重跑：{out_path} 不存在")
            return 1
        disk_content = out_path.read_text(encoding="utf-8")
        if normalize_for_diff(disk_content) != normalize_for_diff(new_content):
            print("❌ 單檔閱讀版過期，請重跑：python3 scripts/tools/build-rewrite-single-file.py")
            print(f"   （輸出路徑：{out_path}）")
            return 1
        print(f"✅ {out_path} 是最新的")
        return 0

    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(new_content, encoding="utf-8")
    print(f"✅ 生成完成：{out_path}（{len(new_content.splitlines())} 行）")
    return 0


if __name__ == "__main__":
    sys.exit(main())
