"""整篇引擎（openrouter-translate.py build_translation_prompt）frontmatter scaffold 的欄位所有權。

2026-09-22：zh 有 imageAlt 的 48 篇在 whole 引擎永遠過不了 verify 第 13 檢查——scaffold 沒列
imageAlt，模型從 zh 全文照抄；tags 在 scaffold 寫 preserve、系統規則寫 translate 互相矛盾。
"""
import importlib.util
from pathlib import Path

MODULE_PATH = Path(__file__).resolve().parents[1] / "scripts" / "tools" / "lang-sync" / "openrouter-translate.py"
SPEC = importlib.util.spec_from_file_location("openrouter_translate", MODULE_PATH)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC and SPEC.loader
SPEC.loader.exec_module(MODULE)

ZH = """---
title: '台灣貓眼：一條光'
description: '台灣貓眼指花蓮豐田一帶臺灣閃玉中呈現 chatoyancy 的材料。'
date: 2026-08-22
category: 'Culture'
tags: ['台灣貓眼', '台灣玉']
subcategory: '工藝與美學'
rationale:
  why_this_hook: '從一條會隨光線移動的亮帶切入。'
  whats_excluded: '不寫珠寶投資建議。'
image: '/article-images/culture/x.webp'
imageAlt: '花蓮縣的山地景觀'
imageCredit: 'Ken Marshall / Wikimedia Commons'
---

正文。
"""


def _scaffold_lines(lang="ko"):
    article = {"frontmatter_placeholder": {"translatedFrom": "Culture/貓眼石.md"}}
    result = MODULE.build_translation_prompt(article, ZH, lang)
    user = result[1]
    return [l for l in user.split("\n") if l.startswith(("imageAlt:", "tags:", "image:", "imageCredit:", "rationale:", "subcategory:")) and "<" in l]


def test_scaffold_translates_image_alt_and_tags_but_preserves_paths_and_rationale():
    lines = {l.split(":")[0]: l for l in _scaffold_lines()}
    assert "translate" in lines["imageAlt"]
    assert "translate" in lines["tags"] and "preserve" not in lines["tags"]
    assert "preserve" in lines["image"]
    assert "preserve" in lines["imageCredit"]
    assert "preserve" in lines["subcategory"]
    assert "rationale" in lines and "VERBATIM" in lines["rationale"] and "flatten" in lines["rationale"]


def test_system_prompt_names_image_alt_as_translated_field():
    article = {"frontmatter_placeholder": {}}
    system = MODULE.build_translation_prompt(article, ZH, "fr")[0]
    assert "`imageAlt`: translate" in system
    assert "`rationale`" in system
