"""displacement_patterns.py

記号転位パターンの定義と分類
"""

from enum import Enum
from dataclasses import dataclass
from typing import List, Dict, Any
import re


class DisplacementType(Enum):
    """記号転位のタイプ（理論的に確実なもののみ）"""
    UNDECLARED_IDENTIFIER = "undeclared_identifier"   # 未宣言識別子の存在論的転位


@dataclass
class DisplacementEvent:
    """記号転位イベント（最小限の確実な検出）"""
    displacement_type: DisplacementType
    node_type: str
    node_text: str
    line_number: int
    column_start: int
    column_end: int
    expected_sign_type: str  # "Index" (variable)
    actual_sign_type: str    # "Icon" (undefined value)
    theoretical_basis: str   # 理論的根拠
    description: str


class MinimalDisplacementDetector:
    """最小限の確実な記号転位検出器"""
    
    def __init__(self):
        # 最小限の確実な検出基準のみ
        pass
    
    def detect_undeclared_identifier_displacement(self, identifier: str, node_type: str, 
                                                 start_pos: List[int], end_pos: List[int], 
                                                 is_declared: bool) -> DisplacementEvent:
        """未宣言識別子の存在論的転位を検出（理論的に確実）"""
        
        # 未宣言識別子のみを検出（JavaScriptセマンティクスによる客観的根拠）
        if not is_declared:
            return DisplacementEvent(
                displacement_type=DisplacementType.UNDECLARED_IDENTIFIER,
                node_type=node_type,
                node_text=identifier,
                line_number=start_pos[0],
                column_start=start_pos[1],
                column_end=end_pos[1],
                expected_sign_type="Index",  # Peirce: 指示的関係（変数→値）
                actual_sign_type="Icon",     # Peirce: 直接的表現（undefined自体）
                theoretical_basis="JavaScript実行セマンティクス: 未宣言識別子はundefined値を返し、指示機能から直接的表現機能に転位",
                description=f"未宣言識別子 '{identifier}' の存在論的転位: Index(指示) → Icon(直接表現)"
            )
        
        return None
    
    # 最小限の実装では構造的パターン検出は除外
    # 理由: 主観的判断が多く、理論的根拠が不十分
    
