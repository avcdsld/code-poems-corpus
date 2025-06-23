"""displacement_patterns.py

記号転位パターンの定義と分類
"""

from enum import Enum
from dataclasses import dataclass
from typing import List, Dict, Any
import re


class PoetryPattern(Enum):
    """詩的転位パターンの分類"""
    EMOTIONAL_EXPRESSION = "emotional_expression"     # 感情的表現
    NARRATIVE_IDENTIFIER = "narrative_identifier"     # 物語的識別子
    METAPHORICAL_SYNTAX = "metaphorical_syntax"       # 比喩的構文使用
    SEMANTIC_INVERSION = "semantic_inversion"         # 意味の反転
    VISUAL_POETRY = "visual_poetry"                   # 視覚的詩作
    TEMPORAL_EXPRESSION = "temporal_expression"       # 時間的表現


@dataclass
class DisplacementEvent:
    """記号転位イベント"""
    pattern: PoetryPattern
    node_type: str
    node_text: str
    line_number: int
    column_start: int
    column_end: int
    intensity: float  # 0.0-1.0
    description: str
    poetic_function: str


class PatternDetector:
    """詩的パターン検出器"""
    
    def __init__(self):
        # 詩的パターンの検出ルール
        self.patterns = {
            'emotional_identifiers': [
                r'.*[Cc]annot.*', r'.*[Ww]ill[Nn]ot.*', r'.*[Hh]old.*',
                r'.*[Ww]ait.*', r'.*[Cc]hange.*', r'.*[Pp]ass.*',
                r'.*[Ss]ilent.*', r'.*[Ss]hout.*', r'.*[Mm]ood.*',
                r'.*[Dd]esperate.*', r'.*[Bb]arely.*', r'.*[Uu]nderstand.*',
                r'.*[Aa]wake.*', r'.*[Ss]top.*'
            ],
            
            'negation_patterns': [
                r'.*[Nn]o[A-Z].*', r'.*[Nn]ot[A-Z].*', r'.*[Cc]annot.*'
            ],
            
            'philosophical_concepts': [
                r'.*[Jj]esus.*', r'.*[Gg]od.*', r'.*[Hh]ope.*', r'.*[Ff]aith.*',
                r'.*[Ll]ove.*', r'.*[Dd]eath.*', r'.*[Ll]ife.*'
            ],
            
            'abstract_concepts': [
                'anything', 'something', 'whatever', 'whoCares',
                'timePassesBy', 'hopePassesOut', 'ious', 'ied',
                'al', 'ing', 'y'
            ],
            
            'word_manipulation': [
                r'brie.*f', r'med.*it.*at.*ions', r'var.*ious', r'var.*ied',
                r'hold.*ing', r'stop.*ing', r'bare.*ly'
            ]
        }
    
    def analyze_identifier(self, identifier: str, node_type: str, 
                          start_pos: List[int], end_pos: List[int], 
                          parent_type: str = None) -> DisplacementEvent:
        """識別子の詩的使用を分析"""
        
        # 感情的識別子の検出
        for pattern in self.patterns['emotional_identifiers']:
            if re.match(pattern, identifier):
                return DisplacementEvent(
                    pattern=PoetryPattern.EMOTIONAL_EXPRESSION,
                    node_type=node_type,
                    node_text=identifier,
                    line_number=start_pos[0],
                    column_start=start_pos[1],
                    column_end=end_pos[1],
                    intensity=0.8,
                    description=f"識別子 '{identifier}' が感情的・状態的意味を表現",
                    poetic_function="変数名による感情状態の表現"
                )
        
        # 否定的表現の検出
        for pattern in self.patterns['negation_patterns']:
            if re.match(pattern, identifier):
                return DisplacementEvent(
                    pattern=PoetryPattern.NARRATIVE_IDENTIFIER,
                    node_type=node_type,
                    node_text=identifier,
                    line_number=start_pos[0],
                    column_start=start_pos[1],
                    column_end=end_pos[1],
                    intensity=0.7,
                    description=f"否定的表現 '{identifier}' による状況の描写",
                    poetic_function="否定による現実状況の表現"
                )
        
        # 哲学的概念の検出
        for pattern in self.patterns['philosophical_concepts']:
            if re.match(pattern, identifier):
                return DisplacementEvent(
                    pattern=PoetryPattern.METAPHORICAL_SYNTAX,
                    node_type=node_type,
                    node_text=identifier,
                    line_number=start_pos[0],
                    column_start=start_pos[1],
                    column_end=end_pos[1],
                    intensity=0.9,
                    description=f"哲学的概念 '{identifier}' の技術的文脈での使用",
                    poetic_function="抽象概念の具象化"
                )
        
        # 抽象概念の検出
        if identifier in self.patterns['abstract_concepts']:
            return DisplacementEvent(
                pattern=PoetryPattern.SEMANTIC_INVERSION,
                node_type=node_type,
                node_text=identifier,
                line_number=start_pos[0],
                column_start=start_pos[1],
                column_end=end_pos[1],
                intensity=0.85,
                description=f"抽象概念 '{identifier}' の変数としての使用",
                poetic_function="抽象性と具体性の反転"
            )
        
        return None
    
    def analyze_structural_patterns(self, ast_data: Dict[str, Any]) -> List[DisplacementEvent]:
        """構造的な詩的パターンを検出"""
        displacements = []
        
        # if文の連鎖パターンを検出
        if_chain = self._count_nested_ifs(ast_data)
        if if_chain > 3:
            displacements.append(DisplacementEvent(
                pattern=PoetryPattern.VISUAL_POETRY,
                node_type='if_statement_chain',
                node_text=f'{if_chain}重のif文',
                line_number=2,
                column_start=0,
                column_end=50,
                intensity=0.95,
                description=f"{if_chain}重のif文による条件の積み重ね",
                poetic_function="条件の階層による絶望感の表現"
            ))
        
        # while文の連鎖パターンを検出
        while_chain = self._count_nested_whiles(ast_data)
        if while_chain > 2:
            displacements.append(DisplacementEvent(
                pattern=PoetryPattern.TEMPORAL_EXPRESSION,
                node_type='while_statement_chain',
                node_text=f'{while_chain}重のwhile文',
                line_number=7,
                column_start=0,
                column_end=50,
                intensity=0.9,
                description=f"{while_chain}重のwhile文による反復表現",
                poetic_function="時間の経過と永続的状況の表現"
            ))
        
        # try-catch構文の詩的使用
        if self._find_node_type(ast_data, 'try_statement'):
            displacements.append(DisplacementEvent(
                pattern=PoetryPattern.METAPHORICAL_SYNTAX,
                node_type='try_statement',
                node_text='try{...}catch(me){...}',
                line_number=10,
                column_start=0,
                column_end=50,
                intensity=0.95,
                description="try-catch構文の人格化（catch(me)）",
                poetic_function="プログラム例外処理の人間関係への転用"
            ))
        
        return displacements
    
    def _count_nested_ifs(self, node: Dict[str, Any], count: int = 0) -> int:
        """ネストしたif文の数をカウント"""
        if not isinstance(node, dict):
            return count
        
        if node.get('type') == 'if_statement':
            count += 1
        
        max_count = count
        for child in node.get('children', []):
            child_count = self._count_nested_ifs(child, count)
            max_count = max(max_count, child_count)
        
        return max_count
    
    def _count_nested_whiles(self, node: Dict[str, Any], count: int = 0) -> int:
        """ネストしたwhile文の数をカウント"""
        if not isinstance(node, dict):
            return count
        
        if node.get('type') == 'while_statement':
            count += 1
        
        max_count = count
        for child in node.get('children', []):
            child_count = self._count_nested_whiles(child, count)
            max_count = max(max_count, child_count)
        
        return max_count
    
    def _find_node_type(self, node: Dict[str, Any], target_type: str) -> bool:
        """指定されたタイプのノードが存在するかチェック"""
        if not isinstance(node, dict):
            return False
        
        if node.get('type') == target_type:
            return True
        
        for child in node.get('children', []):
            if self._find_node_type(child, target_type):
                return True
        
        return False