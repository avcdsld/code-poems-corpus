"""displacement_analysis.py

記号転位分析のメインシステム
"""

from typing import List, Dict, Any, Tuple
import json
import re
from pathlib import Path
from .displacement_patterns import MinimalDisplacementDetector, DisplacementEvent, DisplacementType
import statistics
from collections import Counter

from .parser.plugins.python_displacement import create_python_adapter
from .parser.plugins.html_displacement import create_html_adapter
from .parser.plugins.c_displacement import create_c_adapter
from .parser.plugins.java_displacement import create_java_adapter
from .parser.plugins.cpp_displacement import create_cpp_adapter
from .classify_ast import load_classification_rules, classify_ast


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
            # 言語固有のフィルタリング
            if language == "java":
                # Javaの場合、メンバーアクセスやメソッド呼び出しの一部は除外
                if parent_type in ['member_access', 'method_invocation', 'scoped_identifier']:
                    pass  # これらのコンテキストでは検出しない
                else:
                    is_declared = node_text in declared_vars
                    displacement = self.displacement_detector.detect_undeclared_identifier_displacement(
                        node_text, node_type, start_pos, end_pos, is_declared
                    )
                    if displacement:
                        displacements.append(displacement)
            elif language in ["c", "cpp"]:
                # C/C++の場合、型宣言やパラメータ宣言の一部は除外
                if parent_type in ['parameter_declaration', 'field_identifier', 'type_identifier']:
                    pass  # これらのコンテキストでは検出しない
                else:
                    is_declared = node_text in declared_vars
                    displacement = self.displacement_detector.detect_undeclared_identifier_displacement(
                        node_text, node_type, start_pos, end_pos, is_declared
                    )
                    if displacement:
                        displacements.append(displacement)
            else:
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
            adapter = create_python_adapter()
            return adapter.extract_declared_variables(ast_data)
        elif language == "html":
            adapter = create_html_adapter()
            return adapter.extract_declared_variables(ast_data)
        elif language == "c":
            adapter = create_c_adapter()
            return adapter.extract_declared_variables(ast_data)
        elif language == "java":
            adapter = create_java_adapter()
            return adapter.extract_declared_variables(ast_data)
        elif language == "cpp":
            adapter = create_cpp_adapter()
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


def load_poem_data(poem_id: str, language: str = "js") -> Tuple[Dict, str]:
    """詩作品のASTとソースコードを読み込む"""
    proc_base_path = Path(f"corpus_processed/{language}/{poem_id}")
    raw_base_path = Path(f"corpus_raw/{language}")
    
    ast_path = proc_base_path / "static/ast.json"
    classified_ast_path = proc_base_path / "static/ast_classified.json"

    # Try to find the code file with any of the registered extensions for the language
    code_path = None
    # A bit inefficient, but should be fine. We can get extensions from config.yml later.
    for ext in [".js", ".mjs", ".cjs", ".py", ".html", ".htm", ".c", ".h", ".java", ".cpp", ".cc", ".cxx"]:
        p = raw_base_path / f"{poem_id}{ext}"
        if p.exists():
            code_path = p
            break
    
    if not code_path:
        raise FileNotFoundError(f"ソースファイルが見つかりません: {raw_base_path}/{poem_id}.*")


    if classified_ast_path.exists():
        # キャッシュされた分類済みASTを読み込む
        print("(Loading classified AST from cache...)")
        with open(classified_ast_path, 'r', encoding='utf-8') as f:
            ast_data = json.load(f)
    elif ast_path.exists():
        # ASTを読み込んで分類し、キャッシュする
        print("(Classifying AST and creating cache...)")
        with open(ast_path, 'r', encoding='utf-8') as f:
            ast_data = json.load(f)
        
        # 分類ルールを読み込んでASTを変換
        classification_rules = load_classification_rules()
        ast_data = classify_ast(ast_data, classification_rules, language)
        
        # 結果をキャッシュファイルに保存
        with open(classified_ast_path, 'w', encoding='utf-8') as f:
            json.dump(ast_data, f, indent=2, ensure_ascii=False)
    else:
        raise FileNotFoundError(f"ASTファイルが見つかりません: {ast_path}")

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

class CodePoemAnalyzer:
    def __init__(self, ast_dir: Path):
        self.ast_dir = ast_dir
        self.poems = self._load_asts()

    def _load_asts(self) -> Dict[str, Any]:
        """ASTファイルを読み込む"""
        poems = {}
        for ast_file in self.ast_dir.glob("*.json"):
            with open(ast_file) as f:
                poems[ast_file.stem] = json.load(f)
        return poems

    def analyze_structural_complexity(self) -> Dict[str, Any]:
        """構造的複雑さの分析"""
        results = {}
        for poem_id, ast in self.poems.items():
            # AST深さの計算
            max_depth = self._calculate_max_depth(ast)
            # ノードタイプの分布
            node_types = self._count_node_types(ast)
            # 入れ子レベルの分析
            nesting_levels = self._analyze_nesting(ast)
            
            results[poem_id] = {
                "max_depth": max_depth,
                "node_type_distribution": node_types,
                "nesting_analysis": nesting_levels
            }
        return results

    def analyze_identifiers(self) -> Dict[str, Any]:
        """識別子の意味論的分析"""
        results = {}
        for poem_id, ast in self.poems.items():
            # 識別子の抽出と分類
            identifiers = self._extract_identifiers(ast)
            # 命名パターンの分析
            naming_patterns = self._analyze_naming_patterns(identifiers)
            # 感情表現の検出
            emotional_expr = self._detect_emotional_expressions(identifiers)
            
            results[poem_id] = {
                "identifiers": identifiers,
                "naming_patterns": naming_patterns,
                "emotional_expressions": emotional_expr
            }
        return results

    def analyze_cross_language_patterns(self) -> Dict[str, Any]:
        """言語横断的なパターン分析"""
        # 言語ごとの特徴を抽出
        lang_features = self._extract_language_features()
        # 共通パターンの特定
        common_patterns = self._identify_common_patterns()
        
        return {
            "language_features": lang_features,
            "common_patterns": common_patterns
        }

    def analyze_temporal_spatial(self) -> Dict[str, Any]:
        """時間的・空間的要素の分析"""
        results = {}
        for poem_id, ast in self.poems.items():
            # 視覚的構造の分析
            visual_structure = self._analyze_visual_structure(ast)
            # 実行フローの分析
            flow_analysis = self._analyze_execution_flow(ast)
            # 時間表現の分析
            temporal_expr = self._analyze_temporal_expressions(ast)
            
            results[poem_id] = {
                "visual_structure": visual_structure,
                "flow_analysis": flow_analysis,
                "temporal_expressions": temporal_expr
            }
        return results

    def _calculate_max_depth(self, node: Dict[str, Any], current_depth: int = 0) -> int:
        """ASTの最大深さを計算"""
        if not isinstance(node, dict):
            return current_depth
        
        max_child_depth = current_depth
        for child in node.get("children", []):
            child_depth = self._calculate_max_depth(child, current_depth + 1)
            max_child_depth = max(max_child_depth, child_depth)
        
        return max_child_depth

    def _count_node_types(self, node: Dict[str, Any]) -> Counter:
        """ノードタイプの出現回数をカウント"""
        counter = Counter()
        if isinstance(node, dict):
            counter[node["type"]] += 1
            for child in node.get("children", []):
                counter.update(self._count_node_types(child))
        return counter

    def _analyze_nesting(self, node: Dict[str, Any]) -> Dict[str, Any]:
        """入れ子構造の分析"""
        nesting_info = {
            "block_nesting": [],
            "loop_nesting": [],
            "conditional_nesting": []
        }
        
        def analyze_node(node: Dict[str, Any], depth: int = 0):
            if not isinstance(node, dict):
                return
            
            node_type = node.get("type", "")
            
            # ブロック、ループ、条件分岐の検出
            if "block" in node_type.lower():
                nesting_info["block_nesting"].append(depth)
            elif any(loop_kw in node_type.lower() for loop_kw in ["loop", "while", "for"]):
                nesting_info["loop_nesting"].append(depth)
            elif any(cond_kw in node_type.lower() for cond_kw in ["if", "else", "switch"]):
                nesting_info["conditional_nesting"].append(depth)
            
            for child in node.get("children", []):
                analyze_node(child, depth + 1)
        
        analyze_node(node)
        return nesting_info

    def _extract_identifiers(self, node: Dict[str, Any]) -> List[str]:
        """識別子を抽出"""
        identifiers = []
        
        def extract_from_node(node: Dict[str, Any]):
            if not isinstance(node, dict):
                return
            
            if node.get("type") in ["identifier", "variable", "function_name"]:
                identifiers.append(node.get("text", ""))
            
            for child in node.get("children", []):
                extract_from_node(child)
        
        extract_from_node(node)
        return identifiers

    def _analyze_naming_patterns(self, identifiers: List[str]) -> Dict[str, Any]:
        """命名パターンの分析"""
        patterns = {
            "metaphorical": [],  # メタファー的な命名
            "narrative": [],     # 物語的な命名
            "emotional": [],     # 感情表現を含む命名
            "technical": []      # 技術的な命名
        }
        
        # TODO: 各パターンの判定ロジックを実装
        
        return patterns

    def _detect_emotional_expressions(self, identifiers: List[str]) -> List[str]:
        """感情表現の検出"""
        emotional_words = []
        # TODO: 感情表現の検出ロジックを実装
        return emotional_words

    def _extract_language_features(self) -> Dict[str, Any]:
        """言語固有の特徴を抽出"""
        features = {}
        # TODO: 言語固有の特徴抽出ロジックを実装
        return features

    def _identify_common_patterns(self) -> List[Dict[str, Any]]:
        """共通パターンを特定"""
        patterns = []
        # TODO: 共通パターン特定ロジックを実装
        return patterns

    def _analyze_visual_structure(self, ast: Dict[str, Any]) -> Dict[str, Any]:
        """視覚的構造の分析"""
        structure = {}
        # TODO: 視覚的構造分析ロジックを実装
        return structure

    def _analyze_execution_flow(self, ast: Dict[str, Any]) -> Dict[str, Any]:
        """実行フローの分析"""
        flow = {}
        # TODO: 実行フロー分析ロジックを実装
        return flow

    def _analyze_temporal_expressions(self, ast: Dict[str, Any]) -> Dict[str, Any]:
        """時間表現の分析"""
        expressions = {}
        # TODO: 時間表現分析ロジックを実装
        return expressions