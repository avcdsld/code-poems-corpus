"""python_displacement.py

Python言語サポート for 記号転位検出
"""

from typing import Dict, List, Any, Set

class PythonLanguageAdapter:
    """Python言語の記号転位検出アダプター"""
    
    def __init__(self):
        self.builtin_names = {
            # Python組み込み関数・型
            'print', 'len', 'range', 'str', 'int', 'float', 'bool', 'list', 'dict', 'set',
            'open', 'input', 'max', 'min', 'sum', 'abs', 'round', 'sorted', 'reversed',
            'enumerate', 'zip', 'map', 'filter', 'any', 'all', 'type', 'isinstance',
            'hasattr', 'getattr', 'setattr', 'dir', 'vars', 'globals', 'locals',
            'exec', 'eval', 'compile', '__import__', 'iter', 'next', 'chr', 'ord',
            
            # Python組み込み例外
            'Exception', 'ValueError', 'TypeError', 'KeyError', 'IndexError',
            'AttributeError', 'NameError', 'ImportError', 'IOError', 'OSError',
            
            # Python定数
            'True', 'False', 'None', '__name__', '__main__', '__file__', '__doc__',
            
            # よく使われる標準ライブラリ
            'sys', 'os', 're', 'math', 'random', 'datetime', 'json', 'csv'
        }
    
    def extract_declared_variables(self, ast_data: Dict[str, Any]) -> Set[str]:
        """Python ASTから宣言された変数を抽出"""
        declared_vars = set()
        declared_vars.update(self.builtin_names)  # 組み込み名前を事前登録
        
        self._collect_python_declarations(ast_data, declared_vars)
        return declared_vars
    
    def _collect_python_declarations(self, node: Dict[str, Any], declared_vars: Set[str]):
        """Python固有の宣言パターンを収集"""
        if not isinstance(node, dict):
            return
        
        node_type = node.get('type', '')
        
        # Python変数宣言パターン
        if node_type == 'assignment':
            # 代入文: x = value
            target = node.get('left', {})
            if target.get('type') == 'identifier':
                name = target.get('text')
                if name:
                    declared_vars.add(name)
        
        elif node_type == 'function_definition':
            # 関数定義: def func_name(params):
            name = node.get('name', {}).get('text')
            if name:
                declared_vars.add(name)
            
            # パラメータも追加
            params = node.get('parameters', {})
            self._collect_parameters(params, declared_vars)
        
        elif node_type == 'class_definition':
            # クラス定義: class ClassName:
            name = node.get('name', {}).get('text')
            if name:
                declared_vars.add(name)
        
        elif node_type == 'import_statement':
            # import文: import module, from module import name
            self._collect_imports(node, declared_vars)
        
        elif node_type == 'for_statement':
            # for文: for var in iterable:
            target = node.get('left', {})
            if target.get('type') == 'identifier':
                name = target.get('text')
                if name:
                    declared_vars.add(name)
        
        elif node_type == 'with_statement':
            # with文: with expr as var:
            alias = node.get('alias', {})
            if alias.get('type') == 'identifier':
                name = alias.get('text')
                if name:
                    declared_vars.add(name)
        
        elif node_type == 'except_clause':
            # except文: except Exception as e:
            alias = node.get('alias', {})
            if alias.get('type') == 'identifier':
                name = alias.get('text')
                if name:
                    declared_vars.add(name)
        
        # 子ノードを再帰的に処理
        for child in node.get('children', []):
            self._collect_python_declarations(child, declared_vars)
    
    def _collect_parameters(self, params_node: Dict[str, Any], declared_vars: Set[str]):
        """関数パラメータを収集"""
        if not isinstance(params_node, dict):
            return
        
        for child in params_node.get('children', []):
            if child.get('type') == 'identifier':
                name = child.get('text')
                if name:
                    declared_vars.add(name)
    
    def _collect_imports(self, import_node: Dict[str, Any], declared_vars: Set[str]):
        """import文から名前を収集"""
        if not isinstance(import_node, dict):
            return
        
        import_type = import_node.get('type')
        
        if import_type == 'import_statement':
            # import module
            for child in import_node.get('children', []):
                if child.get('type') == 'dotted_name':
                    # モジュール名の最初の部分を追加
                    first_part = self._get_first_identifier(child)
                    if first_part:
                        declared_vars.add(first_part)
        
        elif import_type == 'import_from_statement':
            # from module import name
            for child in import_node.get('children', []):
                if child.get('type') == 'import_list':
                    for imported in child.get('children', []):
                        if imported.get('type') == 'identifier':
                            name = imported.get('text')
                            if name and name != '*':
                                declared_vars.add(name)
    
    def _get_first_identifier(self, dotted_name: Dict[str, Any]) -> str:
        """dotted_nameから最初の識別子を取得"""
        if dotted_name.get('type') == 'identifier':
            return dotted_name.get('text', '')
        
        for child in dotted_name.get('children', []):
            if child.get('type') == 'identifier':
                return child.get('text', '')
        
        return ''
    
    def get_comment_patterns(self) -> List[str]:
        """Pythonコメントパターン"""
        return [r'#.*']
    
    def get_string_patterns(self) -> List[str]:
        """Python文字列パターン"""
        return [r'".*"', r"'.*'", r'""".*"""', r"'''.*'''"]
    
    def is_undeclared_error_type(self, error_type: str) -> bool:
        """Python実行時エラーが未宣言変数によるものか判定"""
        return error_type in ['NameError', 'AttributeError', 'ImportError', 'ModuleNotFoundError']


def create_python_adapter():
    """Python言語アダプター作成"""
    return PythonLanguageAdapter()