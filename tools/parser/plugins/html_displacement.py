"""html_displacement.py

HTML言語サポート for 記号転位検出
"""

from typing import Dict, List, Any, Set

class HtmlLanguageAdapter:
    """HTML言語の記号転位検出アダプター"""
    
    def __init__(self):
        self.html_tags = {
            # 標準HTMLタグ
            'html', 'head', 'body', 'title', 'meta', 'link', 'style', 'script',
            'div', 'span', 'p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6',
            'a', 'img', 'ul', 'ol', 'li', 'table', 'tr', 'td', 'th',
            'form', 'input', 'button', 'textarea', 'select', 'option',
            'br', 'hr', 'strong', 'em', 'b', 'i', 'u', 'small',
            'header', 'footer', 'nav', 'section', 'article', 'aside',
            'main', 'figure', 'figcaption', 'details', 'summary',
            
            # HTML5 semantic tags
            'time', 'mark', 'code', 'pre', 'blockquote', 'cite',
            'abbr', 'address', 'del', 'ins', 'sub', 'sup'
        }
        
        self.html_attributes = {
            # 標準HTML属性
            'id', 'class', 'style', 'title', 'lang', 'dir',
            'href', 'src', 'alt', 'width', 'height', 'target',
            'type', 'name', 'value', 'placeholder', 'required',
            'disabled', 'readonly', 'checked', 'selected',
            'action', 'method', 'enctype', 'autocomplete',
            'data-', 'aria-', 'role', 'tabindex'
        }
    
    def extract_declared_variables(self, ast_data: Dict[str, Any]) -> Set[str]:
        """HTML ASTから宣言された要素を抽出"""
        declared_vars = set()
        declared_vars.update(self.html_tags)      # 標準HTMLタグを事前登録
        declared_vars.update(self.html_attributes) # 標準HTML属性を事前登録
        
        self._collect_html_declarations(ast_data, declared_vars)
        return declared_vars
    
    def _collect_html_declarations(self, node: Dict[str, Any], declared_vars: Set[str]):
        """HTML固有の宣言パターンを収集"""
        if not isinstance(node, dict):
            return
        
        node_type = node.get('type', '')
        node_text = node.get('text', '')
        
        # HTMLタグ名の収集
        if node_type == 'tag_name':
            tag_name = node_text.lower()
            if tag_name:
                declared_vars.add(tag_name)
        
        # HTML属性名の収集  
        elif node_type == 'attribute_name':
            attr_name = node_text.lower()
            if attr_name:
                declared_vars.add(attr_name)
        
        # id属性の値を収集（要素として扱われる可能性）
        elif node_type == 'attribute_value' and node_text:
            # id="value" の value 部分
            value = node_text.strip('"\'')
            if value and self._is_identifier_like(value):
                declared_vars.add(value)
        
        # カスタムタグや要素を検出
        elif node_type == 'element':
            # カスタム要素の場合、子ノードから tag_name を探す
            for child in node.get('children', []):
                if child.get('type') == 'start_tag':
                    for grandchild in child.get('children', []):
                        if grandchild.get('type') == 'tag_name':
                            tag_name = grandchild.get('text', '').lower()
                            if tag_name:
                                declared_vars.add(tag_name)
        
        # 子ノードを再帰的に処理
        for child in node.get('children', []):
            self._collect_html_declarations(child, declared_vars)
    
    def _is_identifier_like(self, value: str) -> bool:
        """文字列が識別子のようなものかチェック"""
        if not value:
            return False
        # 英数字とハイフン、アンダースコアのみ
        return value.replace('-', '').replace('_', '').isalnum()
    
    def get_comment_patterns(self) -> List[str]:
        """HTMLコメントパターン"""
        return [r'<!--.*?-->', r'<!-.*?->']  # 標準コメントと詩的コメント
    
    def is_poetic_comment(self, comment_text: str) -> bool:
        """HTMLコメントが詩的かどうか判定"""
        comment = comment_text.strip()
        
        # 詩的HTMLコメントの特徴
        # 1. 短いコメント（<!-word->形式）
        if comment.startswith('<!-') and comment.endswith('->') and len(comment) < 20:
            return True
        
        # 2. 通常のHTMLコメントではない内容
        if comment.startswith('<!--') and comment.endswith('-->'):
            inner = comment[4:-3].strip()
            # 技術的でない内容
            if not any(tech in inner.lower() for tech in [
                'todo', 'fixme', 'hack', 'note', 'debug', 'temp', 'remove'
            ]):
                return True
        
        return False
    
    def extract_poetic_elements(self, ast_data: Dict[str, Any]) -> List[Dict[str, Any]]:
        """HTMLから詩的要素を抽出"""
        poetic_elements = []
        self._collect_poetic_elements(ast_data, poetic_elements)
        return poetic_elements
    
    def _collect_poetic_elements(self, node: Dict[str, Any], poetic_elements: List[Dict[str, Any]]):
        """詩的なHTML要素を収集"""
        if not isinstance(node, dict):
            return
        
        node_type = node.get('type', '')
        node_text = node.get('text', '')
        start_pos = node.get('start', [0, 0])
        end_pos = node.get('end', [0, 0])
        
        # HTMLコメントの詩的使用を検出
        if node_type == 'comment':
            if self.is_poetic_comment(node_text):
                poetic_elements.append({
                    'type': 'poetic_comment',
                    'text': node_text,
                    'start': start_pos,
                    'end': end_pos,
                    'description': f"詩的HTMLコメント: '{node_text}'"
                })
        
        # 非標準タグの使用を検出
        elif node_type == 'tag_name':
            tag_name = node_text.lower()
            if tag_name and tag_name not in self.html_tags:
                # カスタムタグは詩的表現の可能性
                poetic_elements.append({
                    'type': 'custom_tag',
                    'text': node_text,
                    'start': start_pos,
                    'end': end_pos,
                    'description': f"カスタムタグによる詩的表現: '<{node_text}>'"
                })
        
        # 子ノードを再帰的に処理
        for child in node.get('children', []):
            self._collect_poetic_elements(child, poetic_elements)


def create_html_adapter():
    """HTML言語アダプター作成"""
    return HtmlLanguageAdapter()