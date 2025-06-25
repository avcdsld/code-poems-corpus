"""c.py

C言語パーサープラグイン for tree-sitter
"""

from typing import Dict, Any, Optional
from tree_sitter import Language, Parser
import tree_sitter_c as tsc


# C言語のLanguageオブジェクトを作成
C_LANGUAGE = Language(tsc.language())


class CParser:
    """C言語パーサー"""
    
    def __init__(self):
        self._parser = Parser()
        self._parser.language = C_LANGUAGE
    
    def parse(self, code: str) -> Dict[str, Any]:
        """C言語コードをパース"""
        
        # バイト文字列に変換
        code_bytes = code.encode('utf-8')
        
        # パース実行
        tree = self._parser.parse(code_bytes)
        
        # ASTを辞書形式に変換
        return self._node_to_dict(tree.root_node, code_bytes)
    
    def _node_to_dict(self, node, source_bytes: bytes) -> Dict[str, Any]:
        """tree-sitterノードを辞書に変換"""
        
        result = {
            'type': node.type,
            'start': [node.start_point.row, node.start_point.column],
            'end': [node.end_point.row, node.end_point.column],
            'text': source_bytes[node.start_byte:node.end_byte].decode('utf-8', errors='replace'),
            'children': []
        }
        
        # 子ノードを再帰的に処理
        for child in node.children:
            result['children'].append(self._node_to_dict(child, source_bytes))
        
        return result
    
    def get_language_info(self) -> Dict[str, Any]:
        """言語情報を取得"""
        return {
            'name': 'C',
            'extensions': ['.c', '.h'],
            'tree_sitter_language': 'c'
        }


def create_parser() -> CParser:
    """Cパーサーを作成"""
    return CParser()


def parse_c_code(code: str) -> Dict[str, Any]:
    """C言語コードをパース（便利関数）"""
    parser = create_parser()
    return parser.parse(code)