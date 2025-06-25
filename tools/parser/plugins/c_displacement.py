"""c_displacement.py

C言語サポート for 記号転位検出
"""

from typing import Dict, List, Any, Set

class CLanguageAdapter:
    """C言語の記号転位検出アダプター"""
    
    def __init__(self):
        # C言語標準ライブラリ関数
        self.c_standard_functions = {
            # stdio.h
            'printf', 'scanf', 'fprintf', 'fscanf', 'sprintf', 'sscanf',
            'fopen', 'fclose', 'fread', 'fwrite', 'fseek', 'ftell',
            'getc', 'putc', 'getchar', 'putchar', 'gets', 'puts',
            'fgets', 'fputs', 'feof', 'ferror', 'fflush', 'rewind',
            
            # stdlib.h
            'malloc', 'calloc', 'free', 'realloc', 'exit', 'abort',
            'atexit', 'atoi', 'atof', 'atol', 'strtol', 'strtod',
            'rand', 'srand', 'system', 'getenv', 'abs', 'labs',
            'div', 'ldiv', 'qsort', 'bsearch',
            
            # string.h
            'strlen', 'strcpy', 'strncpy', 'strcat', 'strncat',
            'strcmp', 'strncmp', 'strchr', 'strrchr', 'strstr',
            'strtok', 'memcpy', 'memmove', 'memcmp', 'memset',
            'memchr',
            
            # math.h
            'sin', 'cos', 'tan', 'asin', 'acos', 'atan', 'atan2',
            'sinh', 'cosh', 'tanh', 'exp', 'log', 'log10',
            'pow', 'sqrt', 'ceil', 'floor', 'fabs', 'fmod',
            
            # ctype.h
            'isalpha', 'isdigit', 'isalnum', 'isspace', 'ispunct',
            'isupper', 'islower', 'toupper', 'tolower',
            
            # time.h
            'time', 'clock', 'difftime', 'mktime', 'asctime',
            'ctime', 'gmtime', 'localtime', 'strftime'
        }
        
        # C言語キーワード
        self.c_keywords = {
            'auto', 'break', 'case', 'char', 'const', 'continue',
            'default', 'do', 'double', 'else', 'enum', 'extern',
            'float', 'for', 'goto', 'if', 'int', 'long',
            'register', 'return', 'short', 'signed', 'sizeof', 'static',
            'struct', 'switch', 'typedef', 'union', 'unsigned', 'void',
            'volatile', 'while'
        }
        
        # C言語型
        self.c_types = {
            'char', 'short', 'int', 'long', 'float', 'double',
            'signed', 'unsigned', 'void', 'size_t', 'FILE',
            'NULL', 'EOF'
        }
    
    def extract_declared_variables(self, ast_data: Dict[str, Any]) -> Set[str]:
        """C ASTから宣言された変数・関数を抽出"""
        declared_vars = set()
        
        # 標準ライブラリ関数を事前登録
        declared_vars.update(self.c_standard_functions)
        declared_vars.update(self.c_keywords)
        declared_vars.update(self.c_types)
        
        self._collect_c_declarations(ast_data, declared_vars)
        return declared_vars
    
    def _collect_c_declarations(self, node: Dict[str, Any], declared_vars: Set[str]):
        """C固有の宣言パターンを収集"""
        if not isinstance(node, dict):
            return
        
        node_type = node.get('type', '')
        node_text = node.get('text', '')
        
        # 変数宣言を検出
        if node_type == 'declaration':
            self._extract_variable_names_from_declaration(node, declared_vars)
        
        # 関数定義を検出
        elif node_type == 'function_definition':
            # 関数名を抽出
            function_name = self._extract_function_name(node)
            if function_name:
                declared_vars.add(function_name)
            
            # パラメータ名を抽出
            self._extract_parameter_names(node, declared_vars)
        
        # 関数宣言（プロトタイプ）を検出
        elif node_type == 'function_declarator':
            function_name = self._extract_function_name_from_declarator(node)
            if function_name:
                declared_vars.add(function_name)
        
        # typedef宣言を検出
        elif node_type == 'type_definition':
            type_name = self._extract_typedef_name(node)
            if type_name:
                declared_vars.add(type_name)
        
        # 構造体/union/enum宣言を検出
        elif node_type in ['struct_specifier', 'union_specifier', 'enum_specifier']:
            type_name = self._extract_struct_name(node)
            if type_name:
                declared_vars.add(type_name)
        
        # マクロ定義を検出
        elif node_type == 'preproc_def':
            macro_name = self._extract_macro_name(node)
            if macro_name:
                declared_vars.add(macro_name)
        
        # 子ノードを再帰的に処理
        for child in node.get('children', []):
            self._collect_c_declarations(child, declared_vars)
    
    def _extract_variable_names_from_declaration(self, node: Dict[str, Any], declared_vars: Set[str]):
        """変数宣言から変数名を抽出"""
        # declarationノードの子ノードから変数名を探す
        for child in node.get('children', []):
            if child.get('type') == 'init_declarator':
                # init_declaratorの中のidentifierを探す
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
        return ''
    
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
    
    def _extract_typedef_name(self, node: Dict[str, Any]) -> str:
        """typedef宣言から型名を抽出"""
        # type_definitionの最後のidentifierが新しい型名
        identifiers = []
        self._collect_identifiers(node, identifiers)
        return identifiers[-1] if identifiers else ''
    
    def _extract_struct_name(self, node: Dict[str, Any]) -> str:
        """構造体/union/enum名を抽出"""
        for child in node.get('children', []):
            if child.get('type') == 'type_identifier':
                return child.get('text', '')
        return ''
    
    def _extract_macro_name(self, node: Dict[str, Any]) -> str:
        """マクロ定義から名前を抽出"""
        for child in node.get('children', []):
            if child.get('type') == 'identifier':
                return child.get('text', '')
        return ''
    
    def _collect_identifiers(self, node: Dict[str, Any], identifiers: List[str]):
        """ノードから全識別子を収集"""
        if node.get('type') == 'identifier':
            identifiers.append(node.get('text', ''))
        
        for child in node.get('children', []):
            self._collect_identifiers(child, identifiers)
    
    def detect_poetic_macros(self, ast_data: Dict[str, Any]) -> List[Dict[str, Any]]:
        """詩的なマクロ使用を検出"""
        poetic_macros = []
        self._find_poetic_macros(ast_data, poetic_macros)
        return poetic_macros
    
    def _find_poetic_macros(self, node: Dict[str, Any], poetic_macros: List[Dict[str, Any]]):
        """詩的マクロを探す"""
        if not isinstance(node, dict):
            return
        
        node_type = node.get('type', '')
        node_text = node.get('text', '')
        start_pos = node.get('start', [0, 0])
        end_pos = node.get('end', [0, 0])
        
        # マクロ定義での詩的表現
        if node_type == 'preproc_def':
            macro_name = self._extract_macro_name(node)
            if macro_name and self._is_poetic_macro_name(macro_name):
                poetic_macros.append({
                    'type': 'poetic_macro',
                    'name': macro_name,
                    'text': node_text,
                    'start': start_pos,
                    'end': end_pos,
                    'description': f"詩的マクロ定義: '{macro_name}'"
                })
        
        # 子ノードを再帰的に処理
        for child in node.get('children', []):
            self._find_poetic_macros(child, poetic_macros)
    
    def _is_poetic_macro_name(self, name: str) -> bool:
        """マクロ名が詩的かどうか判定"""
        # 通常の技術的マクロ名パターンではない場合
        technical_patterns = [
            '_H', '_H_', 'MAX_', 'MIN_', 'SIZE_', 'LEN_',
            'DEBUG', 'VERSION', 'CONFIG', 'BUFFER'
        ]
        
        name_upper = name.upper()
        if any(pattern in name_upper for pattern in technical_patterns):
            return False
        
        # 短く、英単語のようなマクロ名は詩的可能性
        if len(name) < 15 and name.isalpha():
            return True
        
        return False


def create_c_adapter():
    """C言語アダプター作成"""
    return CLanguageAdapter()