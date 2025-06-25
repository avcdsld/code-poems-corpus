"""java_displacement.py

Java言語サポート for 記号転位検出
"""

from typing import Dict, List, Any, Set

class JavaLanguageAdapter:
    """Java言語の記号転位検出アダプター"""
    
    def __init__(self):
        # Java言語キーワード
        self.java_keywords = {
            'abstract', 'assert', 'boolean', 'break', 'byte', 'case', 'catch',
            'char', 'class', 'const', 'continue', 'default', 'do', 'double',
            'else', 'enum', 'extends', 'final', 'finally', 'float', 'for',
            'goto', 'if', 'implements', 'import', 'instanceof', 'int', 'interface',
            'long', 'native', 'new', 'package', 'private', 'protected', 'public',
            'return', 'short', 'static', 'strictfp', 'super', 'switch', 'synchronized',
            'this', 'throw', 'throws', 'transient', 'try', 'void', 'volatile', 'while'
        }
        
        # Java基本型
        self.java_types = {
            'boolean', 'byte', 'char', 'short', 'int', 'long', 'float', 'double', 'void'
        }
        
        # Java標準ライブラリのよく使われるクラス
        self.java_standard_classes = {
            # java.lang
            'Object', 'String', 'StringBuffer', 'StringBuilder', 'System', 'Math',
            'Integer', 'Long', 'Float', 'Double', 'Boolean', 'Character', 'Byte', 'Short',
            'Thread', 'Runnable', 'Exception', 'RuntimeException', 'Error',
            'Class', 'ClassLoader', 'Enum', 'Throwable',
            # System members
            'out', 'in', 'err',
            
            # java.util
            'List', 'ArrayList', 'LinkedList', 'Vector', 'Stack',
            'Set', 'HashSet', 'TreeSet', 'LinkedHashSet',
            'Map', 'HashMap', 'TreeMap', 'LinkedHashMap', 'Hashtable',
            'Collection', 'Collections', 'Arrays', 'Iterator', 'Comparator',
            'Date', 'Calendar', 'Random', 'Scanner', 'StringTokenizer',
            'Optional', 'Stream',
            
            # java.io
            'File', 'FileInputStream', 'FileOutputStream', 'FileReader', 'FileWriter',
            'BufferedReader', 'BufferedWriter', 'PrintWriter', 'InputStream', 'OutputStream',
            'Reader', 'Writer', 'IOException',
            
            # 特殊な識別子
            'null', 'true', 'false'
        }
        
        # 標準的なメソッド名
        self.java_standard_methods = {
            'main', 'toString', 'equals', 'hashCode', 'compareTo', 'clone',
            'finalize', 'getClass', 'notify', 'notifyAll', 'wait',
            'println', 'print', 'printf', 'format',
            'length', 'size', 'isEmpty', 'contains', 'add', 'remove', 'get', 'set',
            'put', 'clear', 'iterator', 'hasNext', 'next'
        }
    
    def extract_declared_variables(self, ast_data: Dict[str, Any]) -> Set[str]:
        """Java ASTから宣言された変数・クラス・メソッドを抽出"""
        declared_vars = set()
        
        # 標準的な識別子を事前登録
        declared_vars.update(self.java_keywords)
        declared_vars.update(self.java_types)
        declared_vars.update(self.java_standard_classes)
        declared_vars.update(self.java_standard_methods)
        
        self._collect_java_declarations(ast_data, declared_vars)
        return declared_vars
    
    def _collect_java_declarations(self, node: Dict[str, Any], declared_vars: Set[str]):
        """Java固有の宣言パターンを収集"""
        if not isinstance(node, dict):
            return
        
        node_type = node.get('type', '')
        node_text = node.get('text', '')
        
        # クラス宣言
        if node_type == 'class_declaration':
            class_name = self._extract_class_name(node)
            if class_name:
                declared_vars.add(class_name)
        
        # インターフェース宣言
        elif node_type == 'interface_declaration':
            interface_name = self._extract_interface_name(node)
            if interface_name:
                declared_vars.add(interface_name)
        
        # メソッド宣言
        elif node_type == 'method_declaration':
            method_name = self._extract_method_name(node)
            if method_name:
                declared_vars.add(method_name)
            # メソッドパラメータも収集
            self._extract_method_parameters(node, declared_vars)
        
        # フィールド宣言
        elif node_type == 'field_declaration':
            self._extract_field_names(node, declared_vars)
        
        # ローカル変数宣言
        elif node_type == 'local_variable_declaration':
            self._extract_local_variable_names(node, declared_vars)
        
        # パラメータ
        elif node_type == 'formal_parameter':
            param_name = self._extract_parameter_name(node)
            if param_name:
                declared_vars.add(param_name)
        
        # import文からクラス名を抽出
        elif node_type == 'import_declaration':
            imported_class = self._extract_imported_class(node)
            if imported_class:
                declared_vars.add(imported_class)
        
        # 識別子（変数参照など）
        elif node_type == 'identifier':
            # 親ノードの型によっては宣言として扱う
            parent_type = node.get('parent_type', '')
            if parent_type in ['variable_declarator', 'formal_parameter']:
                declared_vars.add(node_text)
        
        # 子ノードを再帰的に処理
        for child in node.get('children', []):
            self._collect_java_declarations(child, declared_vars)
    
    def _extract_class_name(self, node: Dict[str, Any]) -> str:
        """クラス宣言からクラス名を抽出"""
        for child in node.get('children', []):
            if child.get('type') == 'identifier':
                return child.get('text', '')
        return ''
    
    def _extract_interface_name(self, node: Dict[str, Any]) -> str:
        """インターフェース宣言から名前を抽出"""
        for child in node.get('children', []):
            if child.get('type') == 'identifier':
                return child.get('text', '')
        return ''
    
    def _extract_method_name(self, node: Dict[str, Any]) -> str:
        """メソッド宣言からメソッド名を抽出"""
        for child in node.get('children', []):
            if child.get('type') == 'identifier':
                return child.get('text', '')
        return ''
    
    def _extract_method_parameters(self, node: Dict[str, Any], declared_vars: Set[str]):
        """メソッドのパラメータを抽出"""
        for child in node.get('children', []):
            if child.get('type') == 'formal_parameters':
                self._extract_from_formal_parameters(child, declared_vars)
    
    def _extract_from_formal_parameters(self, node: Dict[str, Any], declared_vars: Set[str]):
        """formal_parametersから各パラメータ名を抽出"""
        for child in node.get('children', []):
            if child.get('type') == 'formal_parameter':
                param_name = self._extract_parameter_name(child)
                if param_name:
                    declared_vars.add(param_name)
    
    def _extract_parameter_name(self, node: Dict[str, Any]) -> str:
        """パラメータから名前を抽出"""
        # formal_parameterの最後のidentifierが変数名
        identifiers = []
        self._collect_identifiers(node, identifiers)
        return identifiers[-1] if identifiers else ''
    
    def _extract_field_names(self, node: Dict[str, Any], declared_vars: Set[str]):
        """フィールド宣言から変数名を抽出"""
        for child in node.get('children', []):
            if child.get('type') == 'variable_declarator':
                var_name = self._extract_variable_name(child)
                if var_name:
                    declared_vars.add(var_name)
    
    def _extract_local_variable_names(self, node: Dict[str, Any], declared_vars: Set[str]):
        """ローカル変数宣言から変数名を抽出"""
        for child in node.get('children', []):
            if child.get('type') == 'variable_declarator':
                var_name = self._extract_variable_name(child)
                if var_name:
                    declared_vars.add(var_name)
    
    def _extract_variable_name(self, node: Dict[str, Any]) -> str:
        """variable_declaratorから変数名を抽出"""
        for child in node.get('children', []):
            if child.get('type') == 'identifier':
                return child.get('text', '')
        return ''
    
    def _extract_imported_class(self, node: Dict[str, Any]) -> str:
        """import文から最後のクラス名を抽出"""
        import_text = node.get('text', '')
        # import java.util.List; -> List
        if import_text.startswith('import') and import_text.endswith(';'):
            parts = import_text.replace('import', '').replace(';', '').strip().split('.')
            if parts and parts[-1] != '*':
                return parts[-1]
        return ''
    
    def _collect_identifiers(self, node: Dict[str, Any], identifiers: List[str]):
        """ノードから全識別子を収集"""
        if node.get('type') == 'identifier':
            identifiers.append(node.get('text', ''))
        
        for child in node.get('children', []):
            self._collect_identifiers(child, identifiers)
    
    def detect_poetic_java_patterns(self, ast_data: Dict[str, Any]) -> List[Dict[str, Any]]:
        """詩的なJavaパターンを検出"""
        poetic_patterns = []
        self._find_poetic_patterns(ast_data, poetic_patterns)
        return poetic_patterns
    
    def _find_poetic_patterns(self, node: Dict[str, Any], poetic_patterns: List[Dict[str, Any]]):
        """詩的パターンを探す"""
        if not isinstance(node, dict):
            return
        
        node_type = node.get('type', '')
        node_text = node.get('text', '')
        start_pos = node.get('start', [0, 0])
        end_pos = node.get('end', [0, 0])
        
        # クラス名での詩的表現
        if node_type == 'class_declaration':
            class_name = self._extract_class_name(node)
            if class_name and self._is_poetic_class_name(class_name):
                poetic_patterns.append({
                    'type': 'poetic_class_name',
                    'name': class_name,
                    'text': node_text,
                    'start': start_pos,
                    'end': end_pos,
                    'description': f"詩的クラス名: '{class_name}'"
                })
        
        # メソッド名での詩的表現
        elif node_type == 'method_declaration':
            method_name = self._extract_method_name(node)
            if method_name and self._is_poetic_method_name(method_name):
                poetic_patterns.append({
                    'type': 'poetic_method_name',
                    'name': method_name,
                    'text': node_text,
                    'start': start_pos,
                    'end': end_pos,
                    'description': f"詩的メソッド名: '{method_name}'"
                })
        
        # 子ノードを再帰的に処理
        for child in node.get('children', []):
            self._find_poetic_patterns(child, poetic_patterns)
    
    def _is_poetic_class_name(self, name: str) -> bool:
        """クラス名が詩的かどうか判定"""
        # 通常の技術的クラス名パターンではない場合
        technical_patterns = [
            'Controller', 'Service', 'Repository', 'Model', 'View',
            'Manager', 'Handler', 'Factory', 'Builder', 'Utils',
            'Exception', 'Error', 'Test', 'Config', 'Constants'
        ]
        
        if any(pattern in name for pattern in technical_patterns):
            return False
        
        # 感情的・詩的な単語を含む場合
        poetic_words = [
            'Love', 'Life', 'Heart', 'Soul', 'Dream', 'Hope',
            'Memory', 'Emotion', 'Feeling', 'Thought'
        ]
        
        if any(word in name for word in poetic_words):
            return True
        
        return False
    
    def _is_poetic_method_name(self, name: str) -> bool:
        """メソッド名が詩的かどうか判定"""
        # getterやsetterなどの技術的パターンではない
        if name.startswith(('get', 'set', 'is', 'has', 'add', 'remove', 'update', 'delete')):
            return False
        
        # 詩的・感情的な動詞を含む場合
        poetic_verbs = [
            'love', 'dream', 'hope', 'feel', 'think', 'believe',
            'remember', 'forget', 'miss', 'wish'
        ]
        
        name_lower = name.lower()
        if any(verb in name_lower for verb in poetic_verbs):
            return True
        
        return False


def create_java_adapter():
    """Java言語アダプター作成"""
    return JavaLanguageAdapter()