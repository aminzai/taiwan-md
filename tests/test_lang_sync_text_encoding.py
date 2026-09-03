"""lang-sync 的每一次文字讀寫都要自己講明編碼，不要問作業系統。

誕生：2026-09-03 maintainer-am。投稿者 stantheman0128（Windows 11，locale cp950）
回報 issue #1661 — `Path.read_text()` 不帶 encoding 時走系統預設編碼，讀 zh 正文
會 `UnicodeDecodeError`，寫回會把 UTF-8 文章存成 cp950。PR #1662 補齊了翻譯鏈上
的七支，本測試把同一條規則變成閘門，並在同一輪把整個目錄剩下的補完。

為什麼守整個目錄而不是列一份「會碰到中文的檔案」清單：那份清單要有人維護，而
會漂掉的正是它（REFLEXES #83 — 豁免清單各分支各自維護）。這裡的規則沒有例外，
因為對這些檔案來說明講 UTF-8 永遠是對的：JSON、金鑰、`.env`、文章正文都一樣。

在 macOS / Linux 上這條規則看不出差別——那正是它需要機器來守的原因，飛輪跑在
UTF-8 預設的機器上，破了也不會叫。
"""

import ast
import pathlib


LANG_SYNC = pathlib.Path(__file__).resolve().parents[1] / "scripts" / "tools" / "lang-sync"


def _calls_without_encoding(path: pathlib.Path) -> list[str]:
    tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
    offenders = []
    for node in ast.walk(tree):
        func = getattr(node, "func", None)
        if not isinstance(node, ast.Call) or not isinstance(func, ast.Attribute):
            continue
        if func.attr not in ("read_text", "write_text"):
            continue
        if any(kw.arg == "encoding" for kw in node.keywords):
            continue
        offenders.append(f"{path.name}:{node.lineno} .{func.attr}()")
    return offenders


def test_lang_sync_text_io_declares_utf8():
    offenders = []
    for path in sorted(LANG_SYNC.glob("*.py")):
        offenders += _calls_without_encoding(path)
    assert not offenders, (
        "這些讀寫沒有指定 encoding，在系統預設不是 UTF-8 的機器上（Windows cp950）"
        "讀中文正文會炸、寫回會存成別的編碼：\n  " + "\n  ".join(offenders)
    )
