import importlib.util
import re
import sys
from pathlib import Path

import yaml


LANG_SYNC_DIR = Path(__file__).resolve().parents[1] / "scripts" / "tools" / "lang-sync"
sys.path.insert(0, str(LANG_SYNC_DIR))
SPEC = importlib.util.spec_from_file_location("translate_tag_split", LANG_SYNC_DIR / "translate.py")
TR = importlib.util.module_from_spec(SPEC)
assert SPEC and SPEC.loader
SPEC.loader.exec_module(TR)

ZH = ("---\ntitle: '泰雅族'\ndescription: 'D0'\ntags: ['泰雅族', '紋面', '染織', 'gaga', '文化復興']\n"
      "---\n\n# 泰雅族\n\n正文一段。\n")


def _whole_engine_tags(tags_line: str, lang: str) -> list:
    system, user, ctx = TR.armor_pre({"frontmatter_placeholder": {"translatedFrom": "Culture/泰雅族.md"}}, ZH, lang)
    body = re.search(r"```markdown\n(.*?)\n```", user, re.S).group(1)
    out = f"===TITLE===\nT\n===DESC===\nD\n===TAGS===\n{tags_line}\n===BODY===\n" + body
    res, err = TR.armor_post(out, ctx, {"frontmatter_placeholder": {"translatedFrom": "Culture/泰雅族.md"}})
    assert err is None
    return yaml.safe_load(res.split("\n---")[0][4:])["tags"]


def test_arabic_comma_tags_stay_five_tags():
    # 2026-09-27 盤點：ar 438 篇的 tags 是一個字串包著整張清單，因為只切 ASCII 逗號
    tags = _whole_engine_tags("شعب أتايال، وشم الوجه، النسيج، gaga، النهضة الثقافية", "ar")
    assert tags == ["شعب أتايال", "وشم الوجه", "النسيج", "gaga", "النهضة الثقافية"]


def test_japanese_ideographic_comma_tags_stay_five_tags():
    # ja〈泰雅族〉實例：['タイヤル族、紋面、染織、gaga、文化復興']
    tags = _whole_engine_tags("タイヤル族、紋面、染織、gaga、文化復興", "ja")
    assert len(tags) == 5 and tags[0] == "タイヤル族"


def test_ascii_comma_output_is_unchanged():
    assert _whole_engine_tags("Atayal, facial tattoo, weaving, gaga, cultural revival", "en") == [
        "Atayal", "facial tattoo", "weaving", "gaga", "cultural revival"]


def test_a_single_tag_keeps_its_own_comma():
    # zh 只有一個標籤時，譯文標籤裡帶的逗號是內容，不拆
    assert TR.split_tags("台北، تايوان", 1) == ["台北، تايوان"]
    assert TR.split_tags("Taipei, Taiwan", 1) == ["Taipei, Taiwan"]
