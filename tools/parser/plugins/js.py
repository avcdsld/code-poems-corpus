from __future__ import annotations
from typing import Any, Dict, List

from tree_sitter import Parser
from tree_sitter_languages import get_language

from tools.parser.parse_corpus import ParserPlugin

JS_LANGUAGE = get_language("javascript")


class Plugin(ParserPlugin):
    extensions = [".js", ".mjs", ".cjs"]

    def __init__(self, *args, **kwargs):
        self._parser = Parser()
        self._parser.set_language(JS_LANGUAGE)

    # ── Token list (葉ノードのみ) ───────────────────────────
    def tokenise(self, code: str) -> List[Dict[str, Any]]:
        tree = self._parser.parse(code.encode())
        out: List[Dict[str, Any]] = []
        stack = [tree.walk()]
        while stack:
            cur = stack.pop()
            node = cur.node
            if node.child_count == 0:
                out.append(
                    dict(
                        type=node.type,
                        text=code[node.start_byte : node.end_byte],
                        start=node.start_point,
                        end=node.end_point,
                    )
                )
            else:
                for child in reversed(node.children):
                    stack.append(child.walk())
        return out

    # ── フル AST をネスト辞書で ───────────────────────────
    def parse_ast(self, code: str):
        tree = self._parser.parse(code.encode())
        return _to_dict(tree.root_node, code)


def _to_dict(node, src: str):
    d: Dict[str, Any] = {
        "type": node.type,
        "start": node.start_point,
        "end": node.end_point,
    }
    if node.child_count == 0:
        d["text"] = src[node.start_byte : node.end_byte]
    else:
        d["children"] = [_to_dict(c, src) for c in node.children]
    return d
