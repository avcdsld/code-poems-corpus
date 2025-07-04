"""Java language parser plugin for tree-sitter."""

from typing import Dict, List, Any
from tree_sitter import Parser
from tree_sitter_languages import get_language

from .. import ParserPlugin

JAVA_LANGUAGE = get_language("java")


class Plugin(ParserPlugin):
    """Java language parser plugin."""
    
    extensions = ['.java', '.pde']
    
    def __init__(self):
        self._parser = Parser()
        self._parser.set_language(JAVA_LANGUAGE)
    
    def tokenise(self, code: str) -> List[Dict]:
        """Tokenize Java code using tree-sitter."""
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
                        text=code[node.start_byte:node.end_byte].decode(),
                        start=node.start_point,
                        end=node.end_point,
                    )
                )
            else:
                for child in node.children:
                    stack.append(cur.goto_first_child())
                    cur.goto_parent()
        return out

    def parse_ast(self, code: str) -> Dict:
        """Parse Java code into AST using tree-sitter."""
        tree = self._parser.parse(code.encode())
        
        def convert_node(node):
            result = {
                'type': node.type,
                'start': {'row': node.start_point[0], 'column': node.start_point[1]},
                'end': {'row': node.end_point[0], 'column': node.end_point[1]},
                'text': code[node.start_byte:node.end_byte]
            }
            
            if node.children:
                result['children'] = [convert_node(child) for child in node.children]
                
            return result
            
        return convert_node(tree.root_node)