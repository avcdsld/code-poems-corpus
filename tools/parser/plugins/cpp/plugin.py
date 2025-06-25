"""C++ language parser plugin for tree-sitter."""

from typing import Dict, List, Any
from tree_sitter import Parser
from tree_sitter_languages import get_language

from tools.parser.parse_corpus import ParserPlugin

CPP_LANGUAGE = get_language("cpp")


class Plugin(ParserPlugin):
    """C++ language parser plugin."""
    
    extensions = ['.cpp', '.cc', '.cxx', '.c++', '.hpp', '.hh', '.hxx', '.h++']
    
    def __init__(self):
        self._parser = Parser()
        self._parser.set_language(CPP_LANGUAGE)
    
    def tokenise(self, code: str) -> List[Dict]:
        """Tokenize C++ code using tree-sitter."""
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
    
    def parse_ast(self, code: str) -> Dict[str, Any]:
        """Parse C++ code into AST using tree-sitter."""
        tree = self._parser.parse(code.encode())
        return self._to_dict(tree.root_node, code)
    
    def _to_dict(self, node, src: str):
        """Convert tree-sitter node to dictionary."""
        d: Dict[str, Any] = {
            "type": node.type,
            "start": node.start_point,
            "end": node.end_point,
            "text": src[node.start_byte : node.end_byte],
            "children": []
        }
        for child in node.children:
            d["children"].append(self._to_dict(child, src))
        return d