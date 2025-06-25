"""cpp_displacement.py

C++言語サポート for 記号転位検出
"""

from typing import Dict, List, Any, Set

class CppLanguageAdapter:
    """C++言語の記号転位検出アダプター"""
    
    def __init__(self):
        # C++言語キーワード（C言語キーワード含む）
        self.cpp_keywords = {
            # C keywords
            'auto', 'break', 'case', 'char', 'const', 'continue',
            'default', 'do', 'double', 'else', 'enum', 'extern',
            'float', 'for', 'goto', 'if', 'int', 'long',
            'register', 'return', 'short', 'signed', 'sizeof', 'static',
            'struct', 'switch', 'typedef', 'union', 'unsigned', 'void',
            'volatile', 'while',
            
            # C++ specific keywords
            'asm', 'bool', 'catch', 'class', 'const_cast', 'delete',
            'dynamic_cast', 'explicit', 'export', 'false', 'friend',
            'inline', 'mutable', 'namespace', 'new', 'operator',
            'private', 'protected', 'public', 'reinterpret_cast',
            'static_cast', 'template', 'this', 'throw', 'true',
            'try', 'typeid', 'typename', 'using', 'virtual', 'wchar_t',
            
            # C++11 and later
            'alignas', 'alignof', 'char16_t', 'char32_t', 'constexpr',
            'decltype', 'noexcept', 'nullptr', 'static_assert', 'thread_local'
        }
        
        # C++型
        self.cpp_types = {
            'bool', 'char', 'short', 'int', 'long', 'float', 'double',
            'void', 'wchar_t', 'char16_t', 'char32_t', 'size_t',
            'ptrdiff_t', 'nullptr_t'
        }
        
        # C++標準ライブラリ
        self.cpp_standard_library = {
            # iostream
            'std', 'cout', 'cin', 'cerr', 'clog', 'endl',
            'ostream', 'istream', 'iostream', 'fstream', 'stringstream',
            
            # string
            'string', 'wstring', 'u16string', 'u32string',
            
            # containers
            'vector', 'list', 'deque', 'array', 'forward_list',
            'set', 'multiset', 'map', 'multimap',
            'unordered_set', 'unordered_multiset', 'unordered_map', 'unordered_multimap',
            'stack', 'queue', 'priority_queue',
            
            # algorithms
            'sort', 'find', 'copy', 'transform', 'accumulate',
            'min', 'max', 'swap', 'reverse', 'unique',
            
            # memory
            'unique_ptr', 'shared_ptr', 'weak_ptr', 'make_unique', 'make_shared',
            
            # utility
            'pair', 'tuple', 'optional', 'variant', 'any',
            'move', 'forward', 'declval',
            
            # C標準ライブラリ関数も含む
            'printf', 'scanf', 'malloc', 'free', 'memcpy', 'strlen',
            'strcpy', 'strcmp', 'fopen', 'fclose', 'fread', 'fwrite',
            
            # 特殊な識別子
            'NULL', 'nullptr', 'true', 'false'
        }
        
        # よく使われるSTLメソッド
        self.cpp_methods = {
            'begin', 'end', 'rbegin', 'rend', 'cbegin', 'cend',
            'size', 'length', 'empty', 'clear', 'push_back', 'pop_back',
            'push_front', 'pop_front', 'insert', 'erase', 'emplace',
            'emplace_back', 'front', 'back', 'at', 'data',
            'find', 'count', 'lower_bound', 'upper_bound',
            'c_str', 'substr', 'append', 'compare', 'replace',
            'get', 'release', 'reset', 'use_count', 'lock', 'unlock'
        }
    
    def extract_declared_variables(self, ast_data: Dict[str, Any]) -> Set[str]:
        """C++ ASTから宣言された変数・関数・クラスを抽出"""
        declared_vars = set()
        
        # 標準的な識別子を事前登録
        declared_vars.update(self.cpp_keywords)
        declared_vars.update(self.cpp_types)
        declared_vars.update(self.cpp_standard_library)
        declared_vars.update(self.cpp_methods)
        
        self._collect_cpp_declarations(ast_data, declared_vars)
        return declared_vars
    
    def _collect_cpp_declarations(self, node: Dict[str, Any], declared_vars: Set[str]):
        """C++固有の宣言パターンを収集"""
        if not isinstance(node, dict):
            return
        
        node_type = node.get('type', '')
        node_text = node.get('text', '')
        
        # 変数宣言
        if node_type == 'declaration':
            self._extract_variable_names_from_declaration(node, declared_vars)
        
        # 関数定義
        elif node_type == 'function_definition':
            function_name = self._extract_function_name(node)
            if function_name:
                declared_vars.add(function_name)
            self._extract_parameter_names(node, declared_vars)
        
        # クラス定義
        elif node_type == 'class_specifier':
            class_name = self._extract_class_name(node)
            if class_name:
                declared_vars.add(class_name)
        
        # 構造体定義
        elif node_type == 'struct_specifier':
            struct_name = self._extract_struct_name(node)
            if struct_name:
                declared_vars.add(struct_name)
        
        # enum定義
        elif node_type == 'enum_specifier':
            enum_name = self._extract_enum_name(node)
            if enum_name:
                declared_vars.add(enum_name)
            # enumメンバーも抽出
            self._extract_enum_members(node, declared_vars)
        
        # テンプレート宣言
        elif node_type == 'template_declaration':
            self._extract_template_parameters(node, declared_vars)
        
        # 名前空間
        elif node_type == 'namespace_definition':
            namespace_name = self._extract_namespace_name(node)
            if namespace_name:
                declared_vars.add(namespace_name)
        
        # using宣言
        elif node_type == 'using_declaration':
            self._extract_using_declaration(node, declared_vars)
        
        # typedef/using alias
        elif node_type in ['type_definition', 'alias_declaration']:
            type_name = self._extract_type_alias_name(node)
            if type_name:
                declared_vars.add(type_name)
        
        # マクロ定義
        elif node_type == 'preproc_def':
            macro_name = self._extract_macro_name(node)
            if macro_name:
                declared_vars.add(macro_name)
        
        # ラムダ式のキャプチャ
        elif node_type == 'lambda_expression':
            self._extract_lambda_captures(node, declared_vars)
        
        # 子ノードを再帰的に処理
        for child in node.get('children', []):
            self._collect_cpp_declarations(child, declared_vars)
    
    def _extract_variable_names_from_declaration(self, node: Dict[str, Any], declared_vars: Set[str]):
        """変数宣言から変数名を抽出"""
        for child in node.get('children', []):
            if child.get('type') == 'init_declarator':
                var_name = self._find_identifier_in_declarator(child)
                if var_name:
                    declared_vars.add(var_name)
            elif child.get('type') == 'identifier':
                declared_vars.add(child.get('text', ''))
    
    def _find_identifier_in_declarator(self, node: Dict[str, Any]) -> str:
        """declaratorノードから識別子を抽出"""
        if node.get('type') == 'identifier':
            return node.get('text', '')
        
        for child in node.get('children', []):
            if child.get('type') == 'identifier':
                return child.get('text', '')
            result = self._find_identifier_in_declarator(child)
            if result:
                return result
        
        return ''
    
    def _extract_function_name(self, node: Dict[str, Any]) -> str:
        """関数定義から関数名を抽出"""
        for child in node.get('children', []):
            if child.get('type') == 'function_declarator':
                return self._extract_function_name_from_declarator(child)
        return ''
    
    def _extract_function_name_from_declarator(self, node: Dict[str, Any]) -> str:
        """function_declaratorから関数名を抽出"""
        for child in node.get('children', []):
            if child.get('type') == 'identifier':
                return child.get('text', '')
            elif child.get('type') == 'qualified_identifier':
                # クラスメソッドの場合
                return self._extract_qualified_name(child)
            elif child.get('type') == 'field_identifier':
                return child.get('text', '')
        return ''
    
    def _extract_qualified_name(self, node: Dict[str, Any]) -> str:
        """qualified_identifierから最後の名前を抽出"""
        identifiers = []
        self._collect_identifiers(node, identifiers)
        return identifiers[-1] if identifiers else ''
    
    def _extract_parameter_names(self, node: Dict[str, Any], declared_vars: Set[str]):
        """関数のパラメータ名を抽出"""
        for child in node.get('children', []):
            if child.get('type') == 'parameter_list':
                self._extract_from_parameter_list(child, declared_vars)
    
    def _extract_from_parameter_list(self, node: Dict[str, Any], declared_vars: Set[str]):
        """parameter_listから各パラメータ名を抽出"""
        for child in node.get('children', []):
            if child.get('type') == 'parameter_declaration':
                param_name = self._find_identifier_in_declarator(child)
                if param_name:
                    declared_vars.add(param_name)
    
    def _extract_class_name(self, node: Dict[str, Any]) -> str:
        """クラス定義からクラス名を抽出"""
        for child in node.get('children', []):
            if child.get('type') == 'type_identifier':
                return child.get('text', '')
        return ''
    
    def _extract_struct_name(self, node: Dict[str, Any]) -> str:
        """構造体定義から名前を抽出"""
        for child in node.get('children', []):
            if child.get('type') == 'type_identifier':
                return child.get('text', '')
        return ''
    
    def _extract_enum_name(self, node: Dict[str, Any]) -> str:
        """enum定義から名前を抽出"""
        for child in node.get('children', []):
            if child.get('type') == 'type_identifier':
                return child.get('text', '')
        return ''
    
    def _extract_enum_members(self, node: Dict[str, Any], declared_vars: Set[str]):
        """enumメンバーを抽出"""
        for child in node.get('children', []):
            if child.get('type') == 'enumerator_list':
                self._extract_from_enumerator_list(child, declared_vars)
    
    def _extract_from_enumerator_list(self, node: Dict[str, Any], declared_vars: Set[str]):
        """enumerator_listから各メンバーを抽出"""
        for child in node.get('children', []):
            if child.get('type') == 'enumerator':
                # enumeratorの最初の識別子がメンバー名
                for grandchild in child.get('children', []):
                    if grandchild.get('type') == 'identifier':
                        declared_vars.add(grandchild.get('text', ''))
                        break
    
    def _extract_namespace_name(self, node: Dict[str, Any]) -> str:
        """名前空間定義から名前を抽出"""
        for child in node.get('children', []):
            if child.get('type') == 'identifier':
                return child.get('text', '')
        return ''
    
    def _extract_template_parameters(self, node: Dict[str, Any], declared_vars: Set[str]):
        """テンプレートパラメータを抽出"""
        for child in node.get('children', []):
            if child.get('type') == 'template_parameter_list':
                self._extract_from_template_params(child, declared_vars)
    
    def _extract_from_template_params(self, node: Dict[str, Any], declared_vars: Set[str]):
        """template_parameter_listからパラメータ名を抽出"""
        for child in node.get('children', []):
            if child.get('type') in ['type_parameter_declaration', 'parameter_declaration']:
                param_name = self._find_last_identifier(child)
                if param_name:
                    declared_vars.add(param_name)
    
    def _extract_using_declaration(self, node: Dict[str, Any], declared_vars: Set[str]):
        """using宣言から名前を抽出"""
        identifiers = []
        self._collect_identifiers(node, identifiers)
        if identifiers:
            declared_vars.add(identifiers[-1])
    
    def _extract_type_alias_name(self, node: Dict[str, Any]) -> str:
        """typedef/using aliasから新しい型名を抽出"""
        identifiers = []
        self._collect_identifiers(node, identifiers)
        return identifiers[-1] if identifiers else ''
    
    def _extract_macro_name(self, node: Dict[str, Any]) -> str:
        """マクロ定義から名前を抽出"""
        for child in node.get('children', []):
            if child.get('type') == 'identifier':
                return child.get('text', '')
        return ''
    
    def _extract_lambda_captures(self, node: Dict[str, Any], declared_vars: Set[str]):
        """ラムダ式のキャプチャ変数を抽出"""
        for child in node.get('children', []):
            if child.get('type') == 'lambda_capture_specifier':
                self._extract_from_captures(child, declared_vars)
    
    def _extract_from_captures(self, node: Dict[str, Any], declared_vars: Set[str]):
        """lambda_capture_specifierから変数名を抽出"""
        for child in node.get('children', []):
            if child.get('type') == 'identifier':
                declared_vars.add(child.get('text', ''))
    
    def _find_last_identifier(self, node: Dict[str, Any]) -> str:
        """ノードから最後の識別子を見つける"""
        identifiers = []
        self._collect_identifiers(node, identifiers)
        return identifiers[-1] if identifiers else ''
    
    def _collect_identifiers(self, node: Dict[str, Any], identifiers: List[str]):
        """ノードから全識別子を収集"""
        if node.get('type') in ['identifier', 'type_identifier', 'field_identifier']:
            identifiers.append(node.get('text', ''))
        
        for child in node.get('children', []):
            self._collect_identifiers(child, identifiers)
    
    def detect_poetic_cpp_patterns(self, ast_data: Dict[str, Any]) -> List[Dict[str, Any]]:
        """詩的なC++パターンを検出"""
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
        
        # オペレーターオーバーロードでの詩的表現
        if node_type == 'operator_name':
            operator = node_text
            if self._is_poetic_operator_overload(operator):
                poetic_patterns.append({
                    'type': 'poetic_operator_overload',
                    'operator': operator,
                    'text': node_text,
                    'start': start_pos,
                    'end': end_pos,
                    'description': f"詩的演算子オーバーロード: '{operator}'"
                })
        
        # テンプレートでの詩的表現
        elif node_type == 'template_declaration':
            template_name = self._extract_template_name(node)
            if template_name and self._is_poetic_template_name(template_name):
                poetic_patterns.append({
                    'type': 'poetic_template',
                    'name': template_name,
                    'text': node_text,
                    'start': start_pos,
                    'end': end_pos,
                    'description': f"詩的テンプレート: '{template_name}'"
                })
        
        # クラス名での詩的表現
        elif node_type == 'class_specifier':
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
        
        # 子ノードを再帰的に処理
        for child in node.get('children', []):
            self._find_poetic_patterns(child, poetic_patterns)
    
    def _is_poetic_operator_overload(self, operator: str) -> bool:
        """演算子オーバーロードが詩的かどうか判定"""
        # 通常の算術・論理演算子以外の使用
        standard_ops = [
            '=', '+', '-', '*', '/', '%', '++', '--',
            '==', '!=', '<', '>', '<=', '>=',
            '&&', '||', '!', '&', '|', '^', '~',
            '<<', '>>', '+=', '-=', '*=', '/=',
            '[]', '()', '->', '->*'
        ]
        
        # 標準的でない演算子の使用は詩的可能性
        return operator not in standard_ops
    
    def _extract_template_name(self, node: Dict[str, Any]) -> str:
        """テンプレート宣言から名前を抽出"""
        # template宣言の次の要素（クラスや関数）から名前を取得
        for i, child in enumerate(node.get('children', [])):
            if child.get('type') in ['class_specifier', 'function_definition']:
                if child.get('type') == 'class_specifier':
                    return self._extract_class_name(child)
                else:
                    return self._extract_function_name(child)
        return ''
    
    def _is_poetic_template_name(self, name: str) -> bool:
        """テンプレート名が詩的かどうか判定"""
        # 技術的でない、感情的・詩的な名前
        poetic_words = [
            'Love', 'Heart', 'Soul', 'Dream', 'Memory',
            'Emotion', 'Feeling', 'Thought', 'Life', 'Death'
        ]
        
        return any(word in name for word in poetic_words)
    
    def _is_poetic_class_name(self, name: str) -> bool:
        """クラス名が詩的かどうか判定"""
        # 通常の技術的クラス名パターンではない場合
        technical_patterns = [
            'Manager', 'Handler', 'Factory', 'Builder', 'Controller',
            'Service', 'Repository', 'Model', 'View', 'Iterator',
            'Exception', 'Error', 'Interface', 'Abstract', 'Base'
        ]
        
        if any(pattern in name for pattern in technical_patterns):
            return False
        
        # 感情的・詩的な単語を含む場合
        poetic_words = [
            'Love', 'Life', 'Heart', 'Soul', 'Dream', 'Hope',
            'Memory', 'Emotion', 'Feeling', 'Thought', 'Spirit'
        ]
        
        if any(word in name for word in poetic_words):
            return True
        
        return False


def create_cpp_adapter():
    """C++言語アダプター作成"""
    return CppLanguageAdapter()