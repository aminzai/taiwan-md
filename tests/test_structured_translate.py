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


def test_extract_footnote_preserves_second_source_as_armored_desc():
    body = (
        "[^4]: [來源一](https://one.example/a) + "
        "[來源二](https://two.example/b) — 兩個來源共同支持。"
    )

    defs = MODULE.extract_footnote_defs(body)

    assert defs[0]["title"] == "來源一"
    assert defs[0]["url"] == "https://one.example/a"
    assert defs[0]["desc"] == "[來源二](@@LINK0@@) — 兩個來源共同支持。"
    assert defs[0]["_link_restore"] == [("@@LINK0@@", "https://two.example/b")]


def test_extract_footnote_recovers_nested_empty_link_source():
    body = (
        "[^2]: [Threads. 火燒島。取自 "
        "[](https://threads.example/post/1)) — 詳見原始連結。"
    )

    defs = MODULE.extract_footnote_defs(body)

    assert defs[0]["title"] == "Threads. 火燒島。取自"
    assert defs[0]["url"] == "https://threads.example/post/1"
    assert defs[0]["desc"] == "詳見原始連結。"


def test_normalize_footnote_batch_accepts_exact_id_mapping():
    batch = [{"n": "7"}, {"n": "9"}]
    data = {
        "9": {"title": "Nine", "desc": "D9"},
        "7": {"title": "Seven", "desc": "D7"},
    }

    assert MODULE.normalize_footnote_batch(data, batch) == [
        {"n": "7", "title": "Seven", "desc": "D7"},
        {"n": "9", "title": "Nine", "desc": "D9"},
    ]


def test_normalize_footnote_batch_rejects_missing_or_conflicting_ids():
    batch = [{"n": "7"}, {"n": "9"}]
    missing = {"7": {"title": "Seven", "desc": "D7"}}
    conflicting = {
        "7": {"n": "8", "title": "Seven", "desc": "D7"},
        "9": {"title": "Nine", "desc": "D9"},
    }

    assert MODULE.normalize_footnote_batch(missing, batch) is missing
    assert MODULE.normalize_footnote_batch(conflicting, batch) is conflicting


def test_normalize_footnote_batch_keeps_single_list_wrapper_support():
    batch = [{"n": "1"}]
    wrapped = {"translations": [{"n": "1", "title": "T", "desc": "D"}]}

    assert MODULE.normalize_footnote_batch(wrapped, batch) == wrapped["translations"]


def test_normalize_footnote_batch_accepts_single_exact_mapping_wrapper():
    batch = [{"n": "7"}, {"n": "9"}]
    wrapped = {
        "footnotes": {
            "9": {"title": "Nine", "desc": "D9"},
            "7": {"n": "7", "title": "Seven", "desc": "D7"},
        }
    }

    assert MODULE.normalize_footnote_batch(wrapped, batch) == [
        {"n": "7", "title": "Seven", "desc": "D7"},
        {"n": "9", "title": "Nine", "desc": "D9"},
    ]


def test_normalize_footnote_batch_rejects_inexact_mapping_wrapper():
    batch = [{"n": "7"}, {"n": "9"}]
    missing = {"footnotes": {"7": {"title": "Seven", "desc": "D7"}}}
    multi_wrapper = {
        "footnotes": {
            "7": {"title": "Seven", "desc": "D7"},
            "9": {"title": "Nine", "desc": "D9"},
        },
        "status": {},
    }

    assert MODULE.normalize_footnote_batch(missing, batch) is missing
    assert MODULE.normalize_footnote_batch(multi_wrapper, batch) is multi_wrapper


def test_footnote_batch_shape_rejects_single_record_salvaged_from_truncation():
    assert not MODULE.is_footnote_batch_response(
        {"n": "15", "title": "Only the tail survived", "desc": "Incomplete batch"}
    )
    assert MODULE.is_footnote_batch_response(
        {"footnotes": [{"n": "1", "title": "T", "desc": "D"}]}
    )
    assert MODULE.is_footnote_batch_response(
        {"1": {"title": "T", "desc": "D"}}
    )


def test_call_json_retries_when_parsed_json_has_wrong_shape():
    class Backend:
        def __init__(self):
            self.responses = [
                '{"n":"15","title":"tail","desc":"truncated"}',
                '[{"n":"1","title":"complete","desc":"batch"}]',
            ]

        def translate(self, *_args, **_kwargs):
            return self.responses.pop(0)

    metrics = {}
    result = MODULE.call_json(
        Backend(),
        "system",
        "user",
        max_tokens=100,
        timeout=1,
        max_attempts=2,
        metrics=metrics,
        label="phase-N-test",
        accept_data=MODULE.is_footnote_batch_response,
    )

    assert result == [{"n": "1", "title": "complete", "desc": "batch"}]
    assert [call["ok"] for call in metrics["calls"]] == [False, True]
    assert "JSON shape fail" in metrics["calls"][0]["error"]


def test_translate_footnotes_bisects_after_repeated_shape_failure():
    class Backend:
        def __init__(self):
            self.responses = [
                '{"n":"2","title":"tail","desc":"truncated"}',
                '{"n":"2","title":"tail","desc":"truncated again"}',
                '[{"n":"1","title":"One","desc":"D1"}]',
                '[{"n":"2","title":"Two","desc":"D2"}]',
            ]

        def translate(self, *_args, **_kwargs):
            return self.responses.pop(0)

    defs = [
        {"n": "1", "title": "一", "desc": "甲", "_link_restore": []},
        {"n": "2", "title": "二", "desc": "乙", "_link_restore": []},
    ]
    metrics = {}

    assert MODULE.translate_footnotes(defs, "hi", Backend(), metrics) == {
        "1": {"title": "One", "desc": "D1"},
        "2": {"title": "Two", "desc": "D2"},
    }
    assert [call["label"] for call in metrics["calls"]] == [
        "phase-N-batch0",
        "phase-N-batch0",
        "phase-N-batch0-split0",
        "phase-N-batch0-split1",
    ]


def test_validate_footnotes_rejects_markdown_in_translated_title():
    defs = [{"n": "1"}]
    translated = {"1": {"title": "[Source](broken)", "desc": "Description"}}

    assert MODULE.validate_footnotes(defs, translated) == [
        "footnote 1: title contains markdown/newline"
    ]


def test_translate_frontmatter_copies_subcategory_verbatim_from_zh():
    """subcategory 是分類頁的分群鍵（buildSubcategoryGroups 完全比對），譯文必須
    原樣保留 zh 值；2026-09-20 前 Phase F 會查 i18n 表或送模型翻，全庫 1,795 篇
    因此掉進「其他」組（OBSERVER-QUEUE #51）。"""
    class Backend:
        name = "stub"

        def translate(self, _system, user, **_kwargs):
            import json
            payload = json.loads(user)
            assert "subcategory" not in payload, "subcategory 不該再進 prompt"
            out = {k: f"vi:{v}" if isinstance(v, str) else [f"vi:{t}" for t in v]
                   for k, v in payload.items()}
            return json.dumps(out, ensure_ascii=False)

    zh_fm = {
        "title": "周蕙", "description": "歌手", "subcategory": "歌手",
        "category": "Music", "tags": ["a", "b"], "date": "2026-01-01",
    }
    block = MODULE.translate_frontmatter(zh_fm, "", "Music/周蕙.md", "vi", Backend(), {})
    assert "subcategory: '歌手'" in block
    assert "title: 'vi:周蕙'" in block


def test_extract_prose_footnote_keeps_whole_text_and_armors_links():
    """散文型腳註（出處前綴＋連結、句中連結、方括號時間碼）2026-09-21 前掉進裸
    URL 分支：title 切成 `報時光：[標題](`、URL 後的 desc 整段丟掉，組回是巢狀壞
    連結，再被 validate_footnotes 擋下——一夜 36 次 Phase N 全在此陣亡。"""
    body = (
        "[^1]: 報時光：[被周杰倫買走](https://time.udn.com/a) — 報導 TPA 奪冠。\n"
        "[^9]: 吳哲宇，演講逐字稿 [1:00:07]（未公開素材）。同場另見"
        "[活動官方頁](https://events.example/x)，講題為主權實作。\n"
        "[^3]: 散見於台灣飲食文化研究及地方誌。"
    )

    defs = MODULE.extract_footnote_defs(body)

    assert defs[0]["prose"] and defs[0]["title"] == "" and defs[0]["url"] == ""
    assert defs[0]["desc"] == "報時光：[被周杰倫買走](@@LINK0@@) — 報導 TPA 奪冠。"
    assert defs[0]["_link_restore"] == [("@@LINK0@@", "https://time.udn.com/a")]
    assert defs[1]["prose"]
    assert "[1:00:07]" in defs[1]["desc"] and "@@LINK0@@" in defs[1]["desc"]
    # 純文字、無方括號的舊路徑不變：整條當 title
    assert not defs[2]["prose"] and defs[2]["title"].startswith("散見於")


def test_prose_footnote_roundtrip_validates_and_assembles_verbatim_shape():
    body = "[^1]: 報時光：[被周杰倫買走](https://time.udn.com/a) — 報導 TPA 奪冠。"
    defs = MODULE.extract_footnote_defs(body)
    translated = {
        "1": {
            "title": "",
            "desc": "Time UDN: [Bought by Jay Chou](https://time.udn.com/a) — on TPA's win.",
        }
    }

    assert MODULE.validate_footnotes(defs, translated) == []
    assert MODULE.assemble_footnote_defs(defs, translated) == (
        "[^1]: Time UDN: [Bought by Jay Chou](https://time.udn.com/a) — on TPA's win."
    )
    assert MODULE.validate_footnotes(defs, {"1": {"title": "", "desc": " "}}) == [
        "footnote 1: prose footnote translated to empty"
    ]


def test_prose_footnote_ignores_model_supplied_title():
    """模型看到空 title 有時會自己補一個；組回去會多出原文沒有的字。"""
    body = "[^2]: 見[維基百科：BBS 在台灣](https://zh.wikipedia.org/wiki/BBS)。"
    defs = MODULE.extract_footnote_defs(body)
    import json

    class Backend:
        name = "stub"

        def translate(self, _system, user, **_kwargs):
            payload = json.loads(user)
            return json.dumps([
                {"n": p["n"], "title": "Invented Title", "desc": "See [Wikipedia: BBS in Taiwan](@@LINK0@@)."}
                for p in payload
            ], ensure_ascii=False)

    out = MODULE.translate_footnotes(defs, "en", Backend(), {"calls": []})

    assert out["2"]["title"] == ""
    assert out["2"]["desc"] == "See [Wikipedia: BBS in Taiwan](https://zh.wikipedia.org/wiki/BBS)."


def test_translate_frontmatter_translates_image_alt_instead_of_copying_zh():
    """verify-translation.py 第 13 檢查把 imageAlt 跟 title/description 同列
    「不得留原文」，但 2026-09-21 前本引擎把它當 passthrough 機械複製——zh 有
    imageAlt 的 48 篇在 structured 路徑永遠過不了閘（一夜 36 次）。"""
    class Backend:
        name = "stub"

        def translate(self, _system, user, **_kwargs):
            import json
            payload = json.loads(user)
            assert payload["imageAlt"] == "桐花祭開幕", "imageAlt 必須進 prompt"
            out = {k: f"vi:{v}" if isinstance(v, str) else [f"vi:{t}" for t in v]
                   for k, v in payload.items()}
            return json.dumps(out, ensure_ascii=False)

    zh_fm = {
        "title": "苗栗縣", "description": "客家", "category": "Geography",
        "image": "/img/miaoli.jpg", "imageAlt": "桐花祭開幕", "imageCredit": "CC",
        "tags": ["a"], "date": "2026-01-01",
    }
    block = MODULE.translate_frontmatter(zh_fm, "", "Geography/苗栗縣.md", "vi", Backend(), {})
    assert "imageAlt: 'vi:桐花祭開幕'" in block
    assert "image: /img/miaoli.jpg" in block or "image: '/img/miaoli.jpg'" in block
    assert "imageCredit: CC" in block or "imageCredit: 'CC'" in block
