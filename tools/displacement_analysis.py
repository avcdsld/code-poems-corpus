"""displacement_analysis.py

記号転位分析のメインシステム
"""

from typing import List, Dict, Any
import json
from pathlib import Path
from .displacement_patterns import PatternDetector, DisplacementEvent, PoetryPattern


class DisplacementAnalyzer:
    """記号転位分析器"""
    
    def __init__(self):
        self.pattern_detector = PatternDetector()
    
    def analyze_poem(self, ast_data: Dict[str, Any], code_text: str) -> List[DisplacementEvent]:
        """詩作品の記号転位を分析"""
        displacements = []
        code_lines = code_text.splitlines()
        
        # ASTを走査して詩的パターンを検出
        self._traverse_for_poetry(ast_data, displacements, code_lines)
        
        # 構造的パターンを検出
        structural_displacements = self.pattern_detector.analyze_structural_patterns(ast_data)
        displacements.extend(structural_displacements)
        
        # 強度でソート
        displacements.sort(key=lambda d: d.intensity, reverse=True)
        
        return displacements
    
    def _traverse_for_poetry(self, 
                           node: Dict[str, Any], 
                           displacements: List[DisplacementEvent],
                           code_lines: List[str],
                           parent_type: str = None):
        """ASTを再帰的に走査して詩的使用を検出"""
        
        if not isinstance(node, dict):
            return
        
        node_type = node.get('type', '')
        node_text = node.get('text', '')
        start_pos = node.get('start', [0, 0])
        end_pos = node.get('end', [0, 0])
        
        # 識別子の詩的使用を検出
        if node_type == 'identifier' and node_text:
            displacement = self.pattern_detector.analyze_identifier(
                node_text, node_type, start_pos, end_pos, parent_type
            )
            if displacement:
                displacements.append(displacement)
        
        # コメントの詩的機能を検出
        elif node_type == 'comment':
            displacement = self._analyze_comment_poetry(node_text, start_pos, end_pos)
            if displacement:
                displacements.append(displacement)
        
        # 子ノードを再帰的に処理
        for child in node.get('children', []):
            self._traverse_for_poetry(child, displacements, code_lines, node_type)
    
    def _analyze_comment_poetry(self, comment_text: str, start_pos: List[int], end_pos: List[int]) -> DisplacementEvent:
        """コメントの詩的機能を分析"""
        
        if comment_text.strip() in ['//try', '//all that\'s left when you']:
            return DisplacementEvent(
                pattern=PoetryPattern.NARRATIVE_IDENTIFIER,
                node_type='comment',
                node_text=comment_text,
                line_number=start_pos[0],
                column_start=start_pos[1],
                column_end=end_pos[1],
                intensity=0.9,
                description=f"コメント '{comment_text}' による物語的進行",
                poetic_function="コードと自然言語の橋渡し"
            )
        
        return None
    
    def generate_analysis_report(self, displacements: List[DisplacementEvent]) -> Dict[str, Any]:
        """分析レポートを生成"""
        
        if not displacements:
            return {
                "total_displacements": 0,
                "message": "詩的転位が検出されませんでした",
                "suggestions": [
                    "識別子により明確な詩的意味を持たせる",
                    "構文構造による視覚的・リズム的効果を追加",
                    "コメントとコードの相互作用を強化"
                ]
            }
        
        # パターン別統計
        pattern_stats = {}
        for disp in displacements:
            pattern_name = disp.pattern.value
            if pattern_name not in pattern_stats:
                pattern_stats[pattern_name] = {
                    'count': 0,
                    'avg_intensity': 0,
                    'examples': []
                }
            
            pattern_stats[pattern_name]['count'] += 1
            pattern_stats[pattern_name]['avg_intensity'] += disp.intensity
            
            if len(pattern_stats[pattern_name]['examples']) < 3:
                pattern_stats[pattern_name]['examples'].append({
                    'text': disp.node_text,
                    'description': disp.description,
                    'function': disp.poetic_function
                })
        
        # 平均強度を計算
        for stats in pattern_stats.values():
            stats['avg_intensity'] /= stats['count']
        
        return {
            "total_displacements": len(displacements),
            "max_intensity": max(d.intensity for d in displacements),
            "avg_intensity": sum(d.intensity for d in displacements) / len(displacements),
            "pattern_distribution": pattern_stats,
            "top_displacements": [
                {
                    "line": d.line_number + 1,
                    "text": d.node_text,
                    "pattern": d.pattern.value,
                    "intensity": d.intensity,
                    "description": d.description,
                    "poetic_function": d.poetic_function
                }
                for d in displacements[:5]
            ],
            "poetic_interpretation": self._generate_interpretation(displacements)
        }
    
    def _generate_interpretation(self, displacements: List[DisplacementEvent]) -> str:
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
    
    analyzer = DisplacementAnalyzer()
    displacements = analyzer.analyze_poem(ast_data, code_text)
    report = analyzer.generate_analysis_report(displacements)
    
    return {
        "poem_id": poem_id,
        "language": language,
        "analysis": report,
        "displacements": [
            {
                "pattern": d.pattern.value,
                "node_type": d.node_type,
                "node_text": d.node_text,
                "line_number": d.line_number + 1,
                "intensity": d.intensity,
                "description": d.description,
                "poetic_function": d.poetic_function
            }
            for d in displacements
        ]
    }