import importlib.util
from pathlib import Path


MODULE_PATH = (
    Path(__file__).resolve().parents[1]
    / "scripts"
    / "tools"
    / "lang-sync"
    / "structured-translate.py"
)
SPEC = importlib.util.spec_from_file_location("structured_translate", MODULE_PATH)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC and SPEC.loader
SPEC.loader.exec_module(MODULE)


def test_bisect_uses_paragraph_boundary_and_preserves_content():
    source = "第一段很短。\n\n第二段比較長，應該靠近中點。\n\n第三段收尾。"

    parts = MODULE._bisect_at_paragraph_boundary(source)

    assert len(parts) == 2
    assert "\n\n".join(parts) == source
    assert all(part.strip() for part in parts)


def test_bisect_refuses_single_paragraph():
    assert MODULE._bisect_at_paragraph_boundary("只有一段，不能從句中硬切。") == []
