"""displacement_analysis.py

記号転位分析のメインシステム
"""

from typing import List, Dict, Any
import json
import re
from pathlib import Path
from .displacement_patterns import MinimalDisplacementDetector, DisplacementEvent, DisplacementType


class MinimalDisplacementAnalyzer:
    """最小限の確実な記号転位分析器"""
    
    def __init__(self):
        self.displacement_detector = MinimalDisplacementDetector()
    
    def analyze_poem(self, ast_data: Dict[str, Any], code_text: str, language: str = "js") -> List[DisplacementEvent]:
        """詩作品の記号転位を分析（最小限の確実な検出のみ）"""
        displacements = []
        declared_vars = self._extract_declared_variables(ast_data, language)
        
        # ASTを走査して未宣言識別子の転位を検出
        self._traverse_for_poetry(ast_data, displacements, declared_vars, language)
        
        return displacements
    
    def _traverse_for_poetry(self, 
                           node: Dict[str, Any], 
                           displacements: List[DisplacementEvent],
                           declared_vars: set,
                           language: str = "js",
                           parent_type: str = None):
        """ASTを再帰的に走査して語彙的転位を検出（未宣言識別子の意味転位）"""
        
        if not isinstance(node, dict):
            return
        
        node_type = node.get('type', '')
        node_text = node.get('text', '')
        start_pos = node.get('start', [0, 0])
        end_pos = node.get('end', [0, 0])
        
        # 未宣言識別子の転位を検出
        if node_type == 'identifier' and node_text:
            is_declared = node_text in declared_vars
            displacement = self.displacement_detector.detect_undeclared_identifier_displacement(
                node_text, node_type, start_pos, end_pos, is_declared
            )
            if displacement:
                displacements.append(displacement)
        
        # HTMLの詩的エラー要素を転位として検出
        elif node_type == 'ERROR' and node_text and language == "html":
            # HTML詩的コメント <!-word-> の検出
            if node_text.startswith('-') and node_text.endswith('-') and len(node_text) > 2:
                word = node_text[1:-1]  # - を除去
                if word and word.isalpha():
                    displacement = self.displacement_detector.detect_undeclared_identifier_displacement(
                        word, 'poetic_html_comment', start_pos, end_pos, False
                    )
                    if displacement:
                        displacements.append(displacement)
        
        # 最小限の実装ではコメント検出は除外
        
        # 子ノードを再帰的に処理
        for child in node.get('children', []):
            self._traverse_for_poetry(child, displacements, declared_vars, language, node_type)
    
    def _extract_declared_variables(self, ast_data: Dict[str, Any], language: str = "js") -> set:
        """宣言された変数を抽出（言語固有セマンティクスに基づく）"""
        if language == "python":
            from .parser.plugins.python_displacement import create_python_adapter
            adapter = create_python_adapter()
            return adapter.extract_declared_variables(ast_data)
        elif language == "html":
            from .parser.plugins.html_displacement import create_html_adapter
            adapter = create_html_adapter()
            return adapter.extract_declared_variables(ast_data)
        else:
            # JavaScript (デフォルト)
            declared_vars = set()
            self._collect_declarations(ast_data, declared_vars)
            return declared_vars
    
    def _collect_declarations(self, node: Dict[str, Any], declared_vars: set):
        """再帰的に宣言を収集"""
        if not isinstance(node, dict):
            return
        
        node_type = node.get('type', '')
        
        # JavaScript の変数宣言パターン
        if node_type in ['variable_declarator', 'function_declaration', 'parameter']:
            name = node.get('name') or node.get('text')
            if name:
                declared_vars.add(name)
        
        # 子ノードを再帰的に処理
        for child in node.get('children', []):
            self._collect_declarations(child, declared_vars)
    
    def _analyze_comment_displacement(self, comment_text: str, start_pos: List[int], end_pos: List[int]) -> DisplacementEvent:
        """コメントの記号転位を分析（理論的基準）"""
        
        comment = comment_text.strip()
        
        # 技術的コメントの特徴（期待される機能）
        technical_patterns = [
            r'^//\s*TODO:', r'^//\s*FIXME:', r'^//\s*NOTE:',
            r'^//\s*\w+\s*\(.*\)', r'^//\s*\d+', r'^//\s*@'
        ]
        
        # 技術的でないコメントを検出
        is_technical = any(re.match(pattern, comment, re.IGNORECASE) 
                          for pattern in technical_patterns)
        
        # 短く、技術的説明ではない場合は転位の可能性
        if not is_technical and len(comment) < 50:
            # 人称代名詞の使用（読者との対話性）
            has_personal_pronouns = bool(re.search(r'\b(you|me|i|we|us)\b', comment, re.IGNORECASE))
            
            # 感情的・詩的語彙
            has_poetic_language = bool(re.search(r'\b(try|left|when|all|that)\b', comment, re.IGNORECASE))
            
            if has_personal_pronouns or has_poetic_language:
                intensity = 0.6 + (0.3 if has_personal_pronouns else 0) + (0.1 if has_poetic_language else 0)
                
                return DisplacementEvent(
                    pattern=PoetryPattern.NARRATIVE_IDENTIFIER,
                    node_type='comment',
                    node_text=comment_text,
                    line_number=start_pos[0],
                    column_start=start_pos[1],
                    column_end=end_pos[1],
                    intensity=min(intensity, 1.0),
                    description=f"技術的説明から詩的語りかけへの転位: '{comment}'",
                    poetic_function="コメントの詩的・対話的機能への転位"
                )
        
        return None
    
    def generate_analysis_report(self, displacements: List[DisplacementEvent]) -> Dict[str, Any]:
        """分析レポートを生成（最小限の実装）"""
        
        if not displacements:
            return {
                "total_displacements": 0,
                "message": "未宣言識別子による記号転位は検出されませんでした",
                "theoretical_summary": "このコードは技術的機能を主体としており、Peirce記号論的な転位は観察されません。"
            }
        
        return {
            "total_displacements": len(displacements),
            "detected_displacements": [
                {
                    "line": d.line_number + 1,
                    "text": d.node_text,
                    "displacement_type": d.displacement_type.value,
                    "expected_sign_type": d.expected_sign_type,
                    "actual_sign_type": d.actual_sign_type,
                    "theoretical_basis": d.theoretical_basis,
                    "description": d.description
                }
                for d in displacements
            ],
            "theoretical_summary": f"検出された記号転位: {len(displacements)}個。JavaScript未宣言識別子のIndex→Icon転位により、技術的指示機能から直接的表現機能への転位が確認されました。"
        }
    
    # 最小限の実装では詩的解釈は除外（主観的判断のため）
        """詩的解釈を生成"""
        
        high_intensity = [d for d in displacements if d.intensity > 0.8]
        
        if not high_intensity:
            return "軽微な詩的効果が検出されました。"
        
        interpretation = "この作品は以下の詩的技法を使用しています：\n"
        
        # 主要なパターンを分析
        patterns_found = set(d.pattern for d in high_intensity)
        
        if PoetryPattern.EMOTIONAL_EXPRESSION in patterns_found:
            interpretation += "- 感情的識別子による内面状態の表現\n"
        
        if PoetryPattern.VISUAL_POETRY in patterns_found:
            interpretation += "- 構文の視覚的配置による詩的効果\n"
        
        if PoetryPattern.METAPHORICAL_SYNTAX in patterns_found:
            interpretation += "- プログラム構文の比喩的使用\n"
        
        if PoetryPattern.SEMANTIC_INVERSION in patterns_found:
            interpretation += "- 技術的要素と抽象概念の意味的反転\n"
        
        interpretation += f"\n全体として、{len(high_intensity)}個の強い詩的転位により、"
        interpretation += "技術的なコード構造を通じて人間的な感情や状況を表現する作品です。"
        
        return interpretation


def load_poem_data(poem_id: str, language: str = "js") -> tuple[Dict[str, Any], str]:
    """詩作品のデータを読み込み"""
    
    # ASTデータを読み込み
    ast_path = Path(f"corpus_processed/{language}/{poem_id}/static/ast.json")
    if not ast_path.exists():
        raise FileNotFoundError(f"ASTファイルが見つかりません: {ast_path}")
    
    with open(ast_path, 'r', encoding='utf-8') as f:
        ast_data = json.load(f)
    
    # ソースコードを読み込み
    if language == "python":
        code_path = Path(f"corpus_raw/{language}/{poem_id}.py")
    elif language == "html":
        code_path = Path(f"corpus_raw/{language}/{poem_id}.html")
    else:
        code_path = Path(f"corpus_raw/{language}/{poem_id}.{language}")
    
    if not code_path.exists():
        raise FileNotFoundError(f"ソースファイルが見つかりません: {code_path}")
    
    with open(code_path, 'r', encoding='utf-8') as f:
        code_text = f.read()
    
    return ast_data, code_text


def analyze_single_poem(poem_id: str, language: str = "js") -> Dict[str, Any]:
    """単一の詩作品を分析"""
    
    try:
        ast_data, code_text = load_poem_data(poem_id, language)
    except FileNotFoundError as e:
        return {"error": str(e)}
    
    analyzer = MinimalDisplacementAnalyzer()
    displacements = analyzer.analyze_poem(ast_data, code_text, language)
    report = analyzer.generate_analysis_report(displacements)
    
    return {
        "poem_id": poem_id,
        "language": language,
        "analysis": report,
        "displacements": [
            {
                "displacement_type": d.displacement_type.value,
                "node_type": d.node_type,
                "node_text": d.node_text,
                "line_number": d.line_number + 1,
                "expected_sign_type": d.expected_sign_type,
                "actual_sign_type": d.actual_sign_type,
                "theoretical_basis": d.theoretical_basis,
                "description": d.description
            }
            for d in displacements
        ]
    }