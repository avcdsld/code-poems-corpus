#!/usr/bin/env python3
"""
コードポエトリー分析の実践的実装
実験群15作品（Java:7, Python:4, JS:4）vs 対照群3000件
層別マッチドサンプリングとメタ分析を実施
"""

import json
import random
import numpy as np
import pandas as pd
from pathlib import Path
from typing import Dict, List, Tuple, Optional
from collections import defaultdict, Counter
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
from dataclasses import dataclass, field, asdict
import logging
from datetime import datetime

# ロギング設定
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

@dataclass
class ASTMetrics:
    """AST メトリクス"""
    total_nodes: int
    max_depth: int
    avg_depth: float
    unique_node_types: int
    node_type_entropy: float
    complexity: int
    has_functions: bool
    has_classes: bool
    has_loops: bool
    has_conditionals: bool
    identifier_count: int
    literal_count: int
    
@dataclass
class ComparisonResult:
    """比較結果"""
    metric: str
    poetry_mean: float
    poetry_std: float
    control_mean: float
    control_std: float
    difference: float
    cohens_d: float
    p_value: Optional[float]
    confidence_interval: Tuple[float, float]

@dataclass
class LanguageResult:
    """言語別分析結果"""
    language: str
    n_poetry: int
    n_control: int
    n_iterations: int
    metrics: Dict[str, Dict[str, float]]
    significant_metrics: List[str]

class CodePoetryAnalyzer:
    """コードポエトリー分析クラス"""
    
    def __init__(self, output_dir: str = "output"):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(exist_ok=True)
        
        # サンプル数の定義
        self.poetry_counts = {
            'java': 7,
            'python': 4,
            'js': 4,
            # 'ruby': 2
        }
        self.control_counts = {
            'java': 1000,
            'python': 1000,
            'js': 1000,
            # 'ruby': 1000
        }
        
        # データ格納
        self.poetry_data = defaultdict(list)
        self.control_data = defaultdict(list)
        
        # 結果格納
        self.results = {
            'by_language': {},
            'pooled': {},
            'meta_analysis': {},
            'summary': {}
        }
        
        # 言語別のノードタイプマッピング
        self.node_type_mappings = self._initialize_node_mappings()
        
        # 収集されたノードタイプ（デバッグ用）
        self.collected_node_types = defaultdict(set)
        
    def _initialize_node_mappings(self) -> Dict[str, Dict[str, List[str]]]:
        """言語別のノードタイプマッピングを初期化"""
        # 注: 実際のマッピングは使用するパーサーによって異なる
        # これは一般的な例であり、実際のデータで確認が必要
        return {
            'python': {
                'function': ['FunctionDef', 'AsyncFunctionDef', 'function_definition'],
                'class': ['ClassDef', 'class_definition'],
                'loop': ['For', 'While', 'for_statement', 'while_statement'],
                'conditional': ['If', 'if_statement', 'conditional_expression'],
                'identifier': ['Name', 'identifier'],
                'literal': ['Constant', 'Num', 'Str', 'string', 'number', 'integer_literal', 'string_literal']
            },
            'java': {
                'function': ['method_declaration', 'constructor_declaration'],
                'class': ['class_declaration', 'interface_declaration'],
                'loop': ['for_statement', 'while_statement', 'do_statement', 'enhanced_for_statement'],
                'conditional': ['if_statement', 'switch_statement', 'ternary_expression'],
                'identifier': ['identifier'],
                'literal': ['string_literal', 'integer_literal', 'floating_point_literal', 'boolean_literal']
            },
            'js': {
                'function': ['function_declaration', 'arrow_function', 'function_expression', 'method_definition'],
                'class': ['class_declaration', 'class_expression'],
                'loop': ['for_statement', 'for_in_statement', 'for_of_statement', 'while_statement', 'do_statement'],
                'conditional': ['if_statement', 'switch_statement', 'conditional_expression'],
                'identifier': ['identifier'],
                'literal': ['string', 'number', 'template_string', 'regex', 'true', 'false', 'null']
            },
            # 'ruby': {
            #     'function': ['method_definition', 'singleton_method_definition', 'lambda'],
            #     'class': ['class_definition', 'module_definition'],
            #     'loop': ['for', 'while', 'until', 'while_statement', 'for_statement'],
            #     'conditional': ['if', 'unless', 'case', 'if_statement', 'case_statement'],
            #     'identifier': ['identifier', 'constant'],
            #     'literal': ['string', 'integer', 'float', 'symbol', 'string_literal', 'integer_literal']
            # }
        }
    
    def load_data(self):
        """データの読み込み"""
        logger.info("データ読み込み開始")
        
        # for lang in ['java', 'python', 'js', 'ruby']:
        for lang in ['java', 'python', 'js']:
            # 詩的コードの読み込み
            poetry_dir = Path(f"corpus_processed/{lang}")
            if poetry_dir.exists():
                for ast_path in poetry_dir.glob("**/static/ast.json"):
                    try:
                        with open(ast_path, 'r', encoding='utf-8') as f:
                            ast_data = json.load(f)
                        
                        code_path = ast_path.parent / "code.txt"
                        with open(code_path, 'r', encoding='utf-8') as f:
                            code_text = f.read()
                        
                        self.poetry_data[lang].append({
                            'ast': ast_data,
                            'code': code_text,
                            'id': ast_path.parent.parent.name,
                            'path': str(ast_path)
                        })
                    except Exception as e:
                        logger.error(f"Error loading {ast_path}: {e}")
            
            # 対照群の読み込み
            control_dir = Path(f"control_processed/{lang}")
            if control_dir.exists():
                for ast_path in control_dir.glob("**/static/ast.json"):
                    try:
                        with open(ast_path, 'r', encoding='utf-8') as f:
                            ast_data = json.load(f)
                        
                        code_path = ast_path.parent / "code.txt"
                        with open(code_path, 'r', encoding='utf-8') as f:
                            code_text = f.read()
                        
                        self.control_data[lang].append({
                            'ast': ast_data,
                            'code': code_text,
                            'id': ast_path.parent.parent.name,
                            'path': str(ast_path)
                        })
                    except Exception as e:
                        logger.error(f"Error loading {ast_path}: {e}")
        
        # データ読み込み結果の表示
        logger.info("データ読み込み完了:")
        # for lang in ['java', 'python', 'js', 'ruby']:
        for lang in ['java', 'python', 'js']:
            logger.info(f"  {lang}: 詩的={len(self.poetry_data[lang])}, "
                       f"対照群={len(self.control_data[lang])}")
    
    def analyze_node_types(self):
        """実際のノードタイプを収集して分析"""
        logger.info("ノードタイプの収集開始")
        
        # for lang in ['java', 'python', 'js', 'ruby']:
        for lang in ['java', 'python', 'js']:
            # 詩的コードのノードタイプ収集
            for sample in self.poetry_data[lang]:
                self._collect_node_types(sample['ast'], lang)
            
            # 対照群のノードタイプ収集（サンプル）
            for sample in self.control_data[lang][:10]:  # 最初の10個だけ
                self._collect_node_types(sample['ast'], lang)
        
        # ノードタイプレポートの生成
        self._generate_node_type_report()
    
    def _collect_node_types(self, node: Dict, language: str):
        """ノードタイプを再帰的に収集"""
        if not isinstance(node, dict):
            return
        
        node_type = node.get('type', 'unknown')
        self.collected_node_types[language].add(node_type)
        
        for child in node.get('children', []):
            self._collect_node_types(child, language)
    
    def _generate_node_type_report(self):
        """ノードタイプレポートを生成"""
        report_path = self.output_dir / "node_types_report.txt"
        
        with open(report_path, 'w', encoding='utf-8') as f:
            f.write("=== 収集されたノードタイプ（構造的ノードのみ） ===\n\n")
            
            # for lang in ['java', 'python', 'js', 'ruby']:
            for lang in ['java', 'python', 'js']:
                structural_types = {t for t in self.collected_node_types[lang] 
                                  if self._is_structural_node(t)}
                f.write(f"{lang.upper()}:\n")
                sorted_types = sorted(structural_types)
                
                # カテゴリ別に整理
                categorized = defaultdict(list)
                uncategorized = []
                
                for node_type in sorted_types:
                    category = self._categorize_node_type(node_type, lang)
                    if category:
                        categorized[category].append(node_type)
                    else:
                        uncategorized.append(node_type)
                
                # カテゴリ別に出力
                for category in ['function', 'class', 'loop', 'conditional', 'identifier', 
                               'literal', 'call', 'assignment']:
                    if category in categorized:
                        f.write(f"  {category}: {categorized[category]}\n")
                
                if uncategorized:
                    f.write(f"  未分類: {uncategorized[:20]}\n")  # 最初の20個
                
                f.write(f"  構造的ノード合計: {len(structural_types)}種類\n\n")
            
            # 統計情報
            f.write("\n=== 統計情報 ===\n") 
            # for lang in ['java', 'python', 'js', 'ruby']:
            for lang in ['java', 'python', 'js']:
                total = len(self.collected_node_types[lang])
                structural = len({t for t in self.collected_node_types[lang] 
                                if self._is_structural_node(t)})
                f.write(f"{lang.upper()}: 全{total}種類中、構造的ノード{structural}種類 "
                       f"({structural/total*100:.1f}%)\n")
        
        logger.info(f"ノードタイプレポートを生成: {report_path}")
    
    def _categorize_node_type(self, node_type: str, language: str) -> Optional[str]:
        """ノードタイプをカテゴリに分類"""
        mappings = self.node_type_mappings.get(language, {})
        
        for category, types in mappings.items():
            if node_type in types:
                return category
        
        # フォールバック: 部分文字列マッチング
        node_type_lower = node_type.lower()
        
        if any(term in node_type_lower for term in ['function', 'method', 'def']):
            return 'function'
        elif any(term in node_type_lower for term in ['class', 'interface']):
            return 'class'
        elif any(term in node_type_lower for term in ['for', 'while', 'loop']):
            return 'loop'
        elif any(term in node_type_lower for term in ['if', 'switch', 'conditional', 'ternary']):
            return 'conditional'
        elif 'identifier' in node_type_lower:
            return 'identifier'
        elif any(term in node_type_lower for term in ['literal', 'string', 'number', 'integer', 'float']):
            return 'literal'
        
        return None
    
    def _is_structural_node(self, node_type: str) -> bool:
        """構造的に意味のあるノードかどうかを判定（記号や演算子を除外）"""
        # 単一文字の記号は除外
        if len(node_type) == 1 and not node_type.isalnum():
            return False
        
        # 演算子パターンを除外
        operator_patterns = [
            '==', '!=', '<=', '>=', '&&', '||', '<<', '>>', '++', '--',
            '+=', '-=', '*=', '/=', '&=', '|=', '^=', '<<=', '>>=',
            '===', '!==', '=>', '=~', '::', '...', '->', '${', '#{'
        ]
        if node_type in operator_patterns:
            return False
        
        # ERRORノードを除外
        if node_type == 'ERROR':
            return False
        
        return True
    
    def extract_metrics(self, data: Dict, language: str) -> ASTMetrics:
        """ASTからメトリクスを抽出（言語を考慮）"""
        ast = data['ast']
        code = data['code']
        
        # 基本メトリクスの計算
        node_types = Counter()
        node_categories = Counter()
        depths = []
        identifiers = 0
        literals = 0
        
        # 構造フラグ
        has_functions = False
        has_classes = False
        has_loops = False
        has_conditionals = False
        
        def traverse(node: Dict, depth: int = 0):
            nonlocal identifiers, literals, has_functions, has_classes, has_loops, has_conditionals
            
            if not isinstance(node, dict):
                return
            
            node_type = node.get('type', 'unknown')
            
            # 構造的ノードのみカウント
            if self._is_structural_node(node_type):
                node_types[node_type] += 1
                depths.append(depth)
                
                # カテゴリ分類
                category = self._categorize_node_type(node_type, language)
                if category:
                    node_categories[category] += 1
                    
                    # 構造の検出
                    if category == 'function':
                        has_functions = True
                    elif category == 'class':
                        has_classes = True
                    elif category == 'loop':
                        has_loops = True
                    elif category == 'conditional':
                        has_conditionals = True
                    elif category == 'identifier':
                        identifiers += 1
                    elif category == 'literal':
                        literals += 1
            
            # 子ノードの走査
            for child in node.get('children', []):
                traverse(child, depth + 1)
        
        traverse(ast)
        
        # エントロピーの計算（構造的ノードのみ）
        total_nodes = sum(node_types.values())
        entropy = 0
        if total_nodes > 0:
            for count in node_types.values():
                p = count / total_nodes
                if p > 0:
                    entropy -= p * np.log2(p)
        
        # 複雑度の計算（カテゴリベース）
        complexity = 1  # 基本パス
        complexity += node_categories.get('conditional', 0)
        complexity += node_categories.get('loop', 0)
        # try-catchなども考慮
        complexity += node_types.get('try_statement', 0)
        complexity += node_types.get('catch_clause', 0)
        
        return ASTMetrics(
            total_nodes=total_nodes,
            max_depth=max(depths) if depths else 0,
            avg_depth=np.mean(depths) if depths else 0,
            unique_node_types=len(node_types),
            node_type_entropy=entropy,
            complexity=complexity,
            has_functions=has_functions,
            has_classes=has_classes,
            has_loops=has_loops,
            has_conditionals=has_conditionals,
            identifier_count=identifiers,
            literal_count=literals
        )
    
    def analyze_language(self, lang: str, n_iterations: int = 100) -> LanguageResult:
        """単一言語の層別分析"""
        logger.info(f"{lang}の分析開始")
        
        poetry_samples = self.poetry_data[lang]
        control_samples = self.control_data[lang]
        
        if not poetry_samples or not control_samples:
            logger.warning(f"{lang}のデータが不足")
            return None
        
        n_poetry = len(poetry_samples)
        n_control = len(control_samples)
        
        # メトリクスの抽出（言語を渡す）
        poetry_metrics = [self.extract_metrics(s, lang) for s in poetry_samples]
        
        # 反復マッチドサンプリング
        iteration_results = []
        actual_iterations = min(n_iterations, n_control // n_poetry)
        
        for i in range(actual_iterations):
            # 対照群からランダムサンプリング
            sampled_control = random.sample(control_samples, n_poetry)
            control_metrics = [self.extract_metrics(s, lang) for s in sampled_control]
            
            # 各メトリクスの比較
            comparisons = self.compare_metrics(poetry_metrics, control_metrics)
            iteration_results.append(comparisons)
        
        # 結果の集約
        aggregated = self.aggregate_iterations(iteration_results)
        
        # 有意なメトリクスの特定
        significant_metrics = [
            metric for metric, result in aggregated.items()
            if result['significant_ratio'] > 0.8  # 80%以上の反復で有意
        ]
        
        return LanguageResult(
            language=lang,
            n_poetry=n_poetry,
            n_control=n_control,
            n_iterations=actual_iterations,
            metrics=aggregated,
            significant_metrics=significant_metrics
        )
    
    def compare_metrics(self, poetry_metrics: List[ASTMetrics], 
                       control_metrics: List[ASTMetrics]) -> Dict[str, ComparisonResult]:
        """メトリクスの比較"""
        results = {}
        
        # 数値メトリクスのリスト
        numeric_metrics = [
            'total_nodes', 'max_depth', 'avg_depth', 'unique_node_types',
            'node_type_entropy', 'complexity', 'identifier_count', 'literal_count'
        ]
        
        for metric in numeric_metrics:
            poetry_values = [getattr(m, metric) for m in poetry_metrics]
            control_values = [getattr(m, metric) for m in control_metrics]
            
            # 基本統計量
            poetry_mean = np.mean(poetry_values)
            poetry_std = np.std(poetry_values, ddof=1) if len(poetry_values) > 1 else 0
            control_mean = np.mean(control_values)
            control_std = np.std(control_values, ddof=1) if len(control_values) > 1 else 0
            
            # Cohen's d
            pooled_std = np.sqrt((poetry_std**2 + control_std**2) / 2)
            cohens_d = (poetry_mean - control_mean) / pooled_std if pooled_std > 0 else 0
            
            # 統計的検定
            if len(poetry_values) >= 5 and len(control_values) >= 5:
                # Mann-Whitney U検定（ノンパラメトリック）
                statistic, p_value = stats.mannwhitneyu(
                    poetry_values, control_values, alternative='two-sided'
                )
            else:
                p_value = None
            
            # 信頼区間（ブートストラップ）
            ci_low, ci_high = self.bootstrap_ci(poetry_values, control_values)
            
            results[metric] = ComparisonResult(
                metric=metric,
                poetry_mean=poetry_mean,
                poetry_std=poetry_std,
                control_mean=control_mean,
                control_std=control_std,
                difference=poetry_mean - control_mean,
                cohens_d=cohens_d,
                p_value=p_value,
                confidence_interval=(ci_low, ci_high)
            )
        
        # ブール値メトリクス
        bool_metrics = ['has_functions', 'has_classes', 'has_loops', 'has_conditionals']
        for metric in bool_metrics:
            poetry_ratio = sum(getattr(m, metric) for m in poetry_metrics) / len(poetry_metrics)
            control_ratio = sum(getattr(m, metric) for m in control_metrics) / len(control_metrics)
            
            results[f"{metric}_ratio"] = ComparisonResult(
                metric=f"{metric}_ratio",
                poetry_mean=poetry_ratio,
                poetry_std=0,
                control_mean=control_ratio,
                control_std=0,
                difference=poetry_ratio - control_ratio,
                cohens_d=(poetry_ratio - control_ratio) * 2,  # 簡易効果量
                p_value=None,
                confidence_interval=(poetry_ratio - control_ratio, poetry_ratio - control_ratio)
            )
        
        return results
    
    def bootstrap_ci(self, group1: List[float], group2: List[float], 
                     n_bootstrap: int = 1000, confidence: float = 0.95) -> Tuple[float, float]:
        """ブートストラップ信頼区間"""
        differences = []
        
        for _ in range(n_bootstrap):
            # リサンプリング
            sample1 = np.random.choice(group1, size=len(group1), replace=True)
            sample2 = np.random.choice(group2, size=len(group2), replace=True)
            
            # 差の計算
            diff = np.mean(sample1) - np.mean(sample2)
            differences.append(diff)
        
        # パーセンタイル法
        alpha = 1 - confidence
        lower = np.percentile(differences, alpha/2 * 100)
        upper = np.percentile(differences, (1 - alpha/2) * 100)
        
        return lower, upper
    
    def aggregate_iterations(self, iteration_results: List[Dict]) -> Dict:
        """反復結果の集約"""
        aggregated = defaultdict(lambda: defaultdict(list))
        
        # 各反復の結果を収集
        for iteration in iteration_results:
            for metric, result in iteration.items():
                aggregated[metric]['difference'].append(result.difference)
                aggregated[metric]['cohens_d'].append(result.cohens_d)
                if result.p_value is not None:
                    aggregated[metric]['p_value'].append(result.p_value)
        
        # 統計量の計算
        summary = {}
        for metric, values in aggregated.items():
            summary[metric] = {
                'mean_difference': np.mean(values['difference']),
                'std_difference': np.std(values['difference']),
                'mean_cohens_d': np.mean(values['cohens_d']),
                'std_cohens_d': np.std(values['cohens_d']),
                'p_values': values['p_value'],
                'significant_ratio': sum(1 for p in values['p_value'] if p < 0.05) / len(values['p_value'])
                                   if values['p_value'] else 0
            }
        
        return summary
    
    def pooled_analysis(self, n_iterations: int = 100) -> Dict:
        """全言語プール分析"""
        logger.info("プール分析開始")
        
        # 全データの結合
        all_poetry = []
        all_control = []
        
        # for lang in ['java', 'python', 'js', 'ruby']:
        for lang in ['java', 'python', 'js']:
            all_poetry.extend([(s, lang) for s in self.poetry_data[lang]])
            all_control.extend([(s, lang) for s in self.control_data[lang]])
        
        if not all_poetry or not all_control:
            logger.warning("プール分析用のデータが不足")
            return {}
        
        n_poetry = len(all_poetry)
        poetry_metrics = [self.extract_metrics(s[0], s[1]) for s in all_poetry]
        
        # 反復分析
        iteration_results = []
        for i in range(n_iterations):
            sampled_control = random.sample(all_control, n_poetry)
            control_metrics = [self.extract_metrics(s[0], s[1]) for s in sampled_control]
            
            comparisons = self.compare_metrics(poetry_metrics, control_metrics)
            iteration_results.append(comparisons)
        
        return self.aggregate_iterations(iteration_results)
    
    def meta_analysis(self, language_results: Dict[str, LanguageResult]) -> Dict:
        """メタ分析"""
        logger.info("メタ分析開始")
        
        meta_results = defaultdict(list)
        
        # 各言語の効果量を収集
        for lang, result in language_results.items():
            if result is None:
                continue
            
            for metric, values in result.metrics.items():
                meta_results[metric].append({
                    'language': lang,
                    'effect_size': values['mean_cohens_d'],
                    'n': result.n_poetry,
                    'variance': values['std_cohens_d']**2 if values['std_cohens_d'] > 0 else 0.01
                })
        
        # 重み付き平均効果量の計算
        summary = {}
        for metric, effects in meta_results.items():
            if not effects:
                continue
            
            # 逆分散重み付け
            weights = [1/e['variance'] for e in effects]
            effect_sizes = [e['effect_size'] for e in effects]
            
            if sum(weights) > 0:
                weighted_mean = np.average(effect_sizes, weights=weights)
                
                # 異質性の検定（Q統計量）
                q_stat = sum(w * (es - weighted_mean)**2 
                           for w, es in zip(weights, effect_sizes))
                df = len(effects) - 1
                p_heterogeneity = 1 - stats.chi2.cdf(q_stat, df) if df > 0 else 1
                
                # I²統計量（異質性の程度）
                i_squared = max(0, (q_stat - df) / q_stat) if q_stat > 0 else 0
                
                summary[metric] = {
                    'weighted_mean_effect': weighted_mean,
                    'n_languages': len(effects),
                    'q_statistic': q_stat,
                    'p_heterogeneity': p_heterogeneity,
                    'i_squared': i_squared,
                    'by_language': effects
                }
        
        return summary
    
    def create_visualizations(self):
        """結果の可視化"""
        logger.info("可視化作成開始")
        
        # 1. 言語別効果量のフォレストプロット
        self.create_forest_plot()
        
        # 2. メトリクス比較のヒートマップ
        self.create_heatmap()
        
        # 3. プール分析の分布図
        self.create_distribution_plots()
    
    def create_forest_plot(self):
        """フォレストプロット"""
        fig, axes = plt.subplots(2, 2, figsize=(15, 12))
        axes = axes.ravel()
        
        metrics_to_plot = ['total_nodes', 'max_depth', 'complexity', 'node_type_entropy']
        
        for idx, metric in enumerate(metrics_to_plot):
            ax = axes[idx]
            
            # データ収集
            languages = []
            effects = []
            lower_ci = []
            upper_ci = []
            
            # for lang in ['java', 'python', 'js', 'ruby']:
            for lang in ['java', 'python', 'js']:
                if lang in self.results['by_language'] and self.results['by_language'][lang]:
                    result = self.results['by_language'][lang]
                    if metric in result.metrics:
                        languages.append(lang.upper())
                        effects.append(result.metrics[metric]['mean_cohens_d'])
                        # 簡易的な信頼区間（±2SE）
                        se = result.metrics[metric]['std_cohens_d'] / np.sqrt(result.n_poetry)
                        lower_ci.append(result.metrics[metric]['mean_cohens_d'] - 2*se)
                        upper_ci.append(result.metrics[metric]['mean_cohens_d'] + 2*se)
            
            # メタ分析の結果を追加
            if metric in self.results['meta_analysis']:
                languages.append('POOLED')
                effects.append(self.results['meta_analysis'][metric]['weighted_mean_effect'])
                lower_ci.append(effects[-1] - 0.2)  # 簡易的
                upper_ci.append(effects[-1] + 0.2)
            
            # プロット
            y_pos = np.arange(len(languages))
            ax.errorbar(effects, y_pos, xerr=[np.array(effects)-np.array(lower_ci), 
                                              np.array(upper_ci)-np.array(effects)],
                       fmt='o', capsize=5)
            ax.axvline(x=0, color='gray', linestyle='--', alpha=0.5)
            ax.set_yticks(y_pos)
            ax.set_yticklabels(languages)
            ax.set_xlabel("Effect Size (Cohen's d)")
            ax.set_title(f"{metric}")
            ax.grid(True, alpha=0.3)
        
        plt.tight_layout()
        plt.savefig(self.output_dir / "forest_plot.png", dpi=300, bbox_inches='tight')
        plt.close()
    
    def create_heatmap(self):
        """効果量のヒートマップ"""
        # データ準備
        metrics = ['total_nodes', 'max_depth', 'avg_depth', 'unique_node_types',
                  'node_type_entropy', 'complexity', 'identifier_count']
        # languages = ['java', 'python', 'js', 'ruby']
        languages = ['java', 'python', 'js']
        
        effect_matrix = []
        for lang in languages:
            row = []
            if lang in self.results['by_language'] and self.results['by_language'][lang]:
                result = self.results['by_language'][lang]
                for metric in metrics:
                    if metric in result.metrics:
                        row.append(result.metrics[metric]['mean_cohens_d'])
                    else:
                        row.append(0)
            else:
                row = [0] * len(metrics)
            effect_matrix.append(row)
        
        # ヒートマップ作成
        plt.figure(figsize=(10, 6))
        sns.heatmap(effect_matrix, 
                   xticklabels=metrics,
                   yticklabels=[l.upper() for l in languages],
                   cmap='RdBu_r', center=0,
                   annot=True, fmt='.2f',
                   cbar_kws={'label': "Effect Size (Cohen's d)"})
        plt.title("Effect Sizes by Language and Metric")
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        plt.savefig(self.output_dir / "effect_size_heatmap.png", dpi=300, bbox_inches='tight')
        plt.close()
    
    def create_distribution_plots(self):
        """分布の比較プロット"""
        fig, axes = plt.subplots(2, 2, figsize=(12, 10))
        axes = axes.ravel()
        
        # 全データのメトリクス（言語情報付き）
        all_poetry = []
        all_control = []
        
        # for lang in ['java', 'python', 'js', 'ruby']:
        for lang in ['java', 'python', 'js']:
            all_poetry.extend([(s, lang) for s in self.poetry_data[lang]])
            all_control.extend([(s, lang) for s in self.control_data[lang][:20]])  # 可視化用にサンプリング
        
        if not all_poetry or not all_control:
            return
        
        poetry_metrics = [self.extract_metrics(s[0], s[1]) for s in all_poetry]
        control_metrics = [self.extract_metrics(s[0], s[1]) for s in all_control]
        
        metrics_to_plot = [
            ('total_nodes', 'Total Nodes'),
            ('max_depth', 'Maximum Depth'),
            ('complexity', 'Cyclomatic Complexity'),
            ('node_type_entropy', 'Node Type Entropy')
        ]
        
        for idx, (metric, title) in enumerate(metrics_to_plot):
            ax = axes[idx]
            
            poetry_values = [getattr(m, metric) for m in poetry_metrics]
            control_values = [getattr(m, metric) for m in control_metrics]
            
            # バイオリンプロット
            data = [poetry_values, control_values]
            positions = [1, 2]
            parts = ax.violinplot(data, positions=positions, showmeans=True)
            
            # カスタマイズ
            colors = ['lightblue', 'lightcoral']
            for pc, color in zip(parts['bodies'], colors):
                pc.set_facecolor(color)
                pc.set_alpha(0.7)
            
            ax.set_xticks(positions)
            ax.set_xticklabels(['Poetry', 'Control'])
            ax.set_ylabel(title)
            ax.set_title(f"Distribution of {title}")
            ax.grid(True, alpha=0.3)
        
        plt.tight_layout()
        plt.savefig(self.output_dir / "distribution_comparison.png", dpi=300, bbox_inches='tight')
        plt.close()
    
    def generate_report(self):
        """包括的なレポート生成"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        report = []
        report.append("=" * 80)
        report.append("コードポエトリー分析レポート")
        report.append(f"生成日時: {timestamp}")
        report.append("=" * 80)
        report.append("")
        
        # 1. サンプル情報
        report.append("【1. サンプル情報】")
        report.append("詩的コード（code {poems} アンソロジー）:")
        total_poetry = 0
        # for lang in ['java', 'python', 'js', 'ruby']:
        for lang in ['java', 'python', 'js']:
            count = len(self.poetry_data[lang])
            total_poetry += count
            report.append(f"  - {lang.upper()}: {count}作品")
        report.append(f"  合計: {total_poetry}作品")
        report.append("")
        report.append("対照群（CodeSearchNetコーパス）:")
        # for lang in ['java', 'python', 'js', 'ruby']:
        for lang in ['java', 'python', 'js']:
            count = len(self.control_data[lang])
            report.append(f"  - {lang.upper()}: {count}件")
        report.append("")
        
        # 2. 言語別分析結果
        report.append("【2. 言語別分析結果】")
        # for lang in ['java', 'python', 'js', 'ruby']:
        for lang in ['java', 'python', 'js']:
            if lang not in self.results['by_language'] or not self.results['by_language'][lang]:
                continue
            
            result = self.results['by_language'][lang]
            report.append(f"\n{lang.upper()}:")
            report.append(f"  サンプル数: 詩的={result.n_poetry}, 対照群={result.n_control}")
            report.append(f"  反復回数: {result.n_iterations}")
            
            # 主要なメトリクス
            report.append("  主要な効果量（Cohen's d）:")
            for metric in ['total_nodes', 'complexity', 'node_type_entropy']:
                if metric in result.metrics:
                    d = result.metrics[metric]['mean_cohens_d']
                    sig = result.metrics[metric]['significant_ratio']
                    report.append(f"    - {metric}: d={d:.3f} (有意率={sig*100:.1f}%)")
            
            if result.significant_metrics:
                report.append(f"  統計的に有意なメトリクス: {', '.join(result.significant_metrics)}")
        
        # 3. プール分析結果
        report.append("\n【3. 全言語統合分析（プール分析）】")
        report.append(f"総サンプル数: {total_poetry}作品")
        
        if self.results['pooled']:
            report.append("主要メトリクスの効果量:")
            for metric in ['total_nodes', 'max_depth', 'complexity', 'node_type_entropy']:
                if metric in self.results['pooled']:
                    result = self.results['pooled'][metric]
                    report.append(f"  - {metric}:")
                    report.append(f"    平均差: {result['mean_difference']:.3f}")
                    report.append(f"    Cohen's d: {result['mean_cohens_d']:.3f}")
                    report.append(f"    有意率: {result['significant_ratio']*100:.1f}%")
        
        # 4. メタ分析結果
        report.append("\n【4. メタ分析結果】")
        if self.results['meta_analysis']:
            for metric in ['total_nodes', 'complexity', 'node_type_entropy']:
                if metric in self.results['meta_analysis']:
                    meta = self.results['meta_analysis'][metric]
                    report.append(f"\n{metric}:")
                    report.append(f"  統合効果量: {meta['weighted_mean_effect']:.3f}")
                    report.append(f"  言語数: {meta['n_languages']}")
                    report.append(f"  異質性 I²: {meta['i_squared']*100:.1f}%")
                    if meta['p_heterogeneity'] < 0.05:
                        report.append("  ※言語間で効果に有意な異質性あり")
        
        # 5. 主要な発見
        report.append("\n【5. 主要な発見】")
        
        # 効果量の解釈
        large_effects = []
        medium_effects = []
        small_effects = []
        
        if self.results['pooled']:
            for metric, result in self.results['pooled'].items():
                d = abs(result['mean_cohens_d'])
                if d >= 0.8:
                    large_effects.append((metric, result['mean_cohens_d']))
                elif d >= 0.5:
                    medium_effects.append((metric, result['mean_cohens_d']))
                elif d >= 0.2:
                    small_effects.append((metric, result['mean_cohens_d']))
        
        if large_effects:
            report.append("\n大きな効果（|d| ≥ 0.8）:")
            for metric, d in large_effects:
                direction = "少ない" if d < 0 else "多い"
                report.append(f"  - {metric}: 詩的コードの方が{direction} (d={d:.3f})")
        
        if medium_effects:
            report.append("\n中程度の効果（0.5 ≤ |d| < 0.8）:")
            for metric, d in medium_effects:
                direction = "低い" if d < 0 else "高い"
                report.append(f"  - {metric}: 詩的コードの方が{direction} (d={d:.3f})")
        
        # 6. 制約と注意事項
        report.append("\n【6. 制約と注意事項】")
        report.append("- サンプルサイズが限定的（詩的コード17作品）")
        report.append("- 'code {poems}'アンソロジーの作品のみを対象")
        report.append("- 結果の一般化には慎重を要する")
        report.append("- 効果量（Cohen's d）を主要な指標として使用")
        
        # 7. 技術的詳細
        report.append("\n【7. 技術的詳細】")
        report.append("- 分析手法: 層別マッチドサンプリング")
        report.append("- 統計検定: Mann-Whitney U検定（ノンパラメトリック）")
        report.append("- 信頼区間: ブートストラップ法（1000回反復）")
        report.append("- メタ分析: 逆分散重み付け法")
        
        # ファイル保存
        report_text = "\n".join(report)
        report_path = self.output_dir / "analysis_report.txt"
        with open(report_path, 'w', encoding='utf-8') as f:
            f.write(report_text)
        
        # 結果のJSON保存
        json_results = {
            'metadata': {
                'timestamp': timestamp,
                'poetry_counts': dict(self.poetry_counts),
                'control_counts': {k: len(v) for k, v in self.control_data.items()}
            },
            'results': {
                'by_language': {
                    lang: asdict(result) if result else None
                    for lang, result in self.results['by_language'].items()
                },
                'pooled': self.results['pooled'],
                'meta_analysis': self.results['meta_analysis']
            }
        }
        
        json_path = self.output_dir / "analysis_results.json"
        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump(json_results, f, indent=2, ensure_ascii=False, default=str)
        
        return report_text
    
    def create_node_type_visualizations(self, usage_stats: Dict[str, Dict[str, Dict[str, int]]]):
        """ノードタイプ使用頻度の可視化"""
        logger.info("ノードタイプ使用頻度の可視化開始")
        
        # プレゼンテーション用のスタイル設定
        plt.style.use('seaborn-v0_8-talk')  # より大きなフォントとクリアな表示
        
        # 1. 言語別の上位ノードタイプ棒グラフ（プレゼン用）
        for lang in ['java', 'python', 'js']:
            plt.figure(figsize=(16, 9))  # 16:9のアスペクト比
            
            # データ準備
            poetry_data = usage_stats['poetry'][lang]
            control_data = usage_stats['control'][lang]
            
            # データ正規化
            poetry_total = sum(poetry_data.values())
            control_total = sum(control_data.values())
            
            # 正規化したデータを作成
            poetry_normalized = {k: v / poetry_total * 100 for k, v in poetry_data.items()}
            control_normalized = {k: v / control_total * 100 for k, v in control_data.items()}
            
            # 全ノードタイプの平均使用頻度を計算してソート
            all_types = set(poetry_normalized.keys()) | set(control_normalized.keys())
            type_avg_freq = {
                t: (poetry_normalized.get(t, 0) + control_normalized.get(t, 0)) / 2
                for t in all_types
            }
            
            # 平均頻度で降順ソート
            sorted_types = sorted(type_avg_freq.items(), key=lambda x: x[1], reverse=True)[:8]
            top_types = [t[0] for t in sorted_types]
            
            # データ準備
            poetry_values = [poetry_normalized.get(t, 0) for t in top_types]
            control_values = [control_normalized.get(t, 0) for t in top_types]
            
            # プロット
            x = np.arange(len(top_types))
            width = 0.35
            
            ax = plt.gca()
            rects1 = ax.bar(x - width/2, poetry_values, width, label='Code Poetry', color='#2ecc71', alpha=0.8)
            rects2 = ax.bar(x + width/2, control_values, width, label='Control Group', color='#e74c3c', alpha=0.8)
            
            # グラフの装飾
            plt.title(f'{lang.upper()}\nNode Type Usage Frequency (%)', pad=20)
            plt.xlabel('Node Type', labelpad=15)
            plt.ylabel('Usage Frequency (%)', labelpad=15)
            
            # X軸ラベルを見やすく調整
            plt.xticks(x, [t.replace('_', '\n') for t in top_types], rotation=0)
            
            # 凡例を見やすい位置に
            plt.legend(loc='upper right', bbox_to_anchor=(1, 1))
            
            # グリッド追加（薄く）
            plt.grid(True, alpha=0.3, axis='y')
            
            # 値のラベルを追加
            def autolabel(rects):
                for rect in rects:
                    height = rect.get_height()
                    ax.annotate(f'{height:.1f}%',
                              xy=(rect.get_x() + rect.get_width() / 2, height),
                              xytext=(0, 3),  # 3 points vertical offset
                              textcoords="offset points",
                              ha='center', va='bottom',
                              fontsize=10)
            
            autolabel(rects1)
            autolabel(rects2)
            
            # レイアウト調整
            plt.tight_layout()
            
            # 保存（高解像度、白背景）
            plt.savefig(self.output_dir / f"node_type_frequency_{lang}_presentation.png",
                       dpi=300, bbox_inches='tight', facecolor='white')
            plt.close()
        
        # 2. 比率のヒートマップ（プレゼン用）
        plt.figure(figsize=(16, 9))
        
        # データ準備
        languages = ['java', 'python', 'js']
        node_types = set()
        
        # 全言語の主要なノードタイプを収集（上位8個に制限）
        for lang in languages:
            poetry_data = usage_stats['poetry'][lang]
            control_data = usage_stats['control'][lang]
            
            poetry_total = sum(poetry_data.values())
            control_total = sum(control_data.values())
            
            poetry_normalized = {k: v / poetry_total * 100 for k, v in poetry_data.items()}
            control_normalized = {k: v / control_total * 100 for k, v in control_data.items()}
            
            # 平均使用頻度でソート
            all_types = set(poetry_normalized.keys()) | set(control_normalized.keys())
            type_avg_freq = {
                t: (poetry_normalized.get(t, 0) + control_normalized.get(t, 0)) / 2
                for t in all_types
            }
            sorted_types = sorted(type_avg_freq.items(), key=lambda x: x[1], reverse=True)[:8]
            node_types.update(t[0] for t in sorted_types)
        
        node_types = sorted(node_types, key=lambda t: max(
            [type_avg_freq.get(t, 0) for lang in languages]
        ), reverse=True)
        
        # 比率行列の作成
        ratio_matrix = np.zeros((len(languages), len(node_types)))
        
        for i, lang in enumerate(languages):
            poetry_data = usage_stats['poetry'][lang]
            control_data = usage_stats['control'][lang]
            
            poetry_total = sum(poetry_data.values())
            control_total = sum(control_data.values())
            
            for j, node_type in enumerate(node_types):
                poetry_ratio = poetry_data.get(node_type, 0) / poetry_total if poetry_total > 0 else 0
                control_ratio = control_data.get(node_type, 0) / control_total if control_total > 0 else 0
                
                if control_ratio > 0:
                    ratio = np.log2(poetry_ratio / control_ratio)
                else:
                    ratio = 0
                ratio_matrix[i, j] = ratio
        
        # ヒートマップの作成
        sns.heatmap(ratio_matrix,
                   xticklabels=[t.replace('_', '\n') for t in node_types],
                   yticklabels=[l.upper() for l in languages],
                   cmap='RdBu_r',
                   center=0,
                   annot=True,
                   fmt='.2f',
                   cbar_kws={'label': 'Code Poetry/Control Group Ratio (log2)'},
                   square=True)
        
        plt.title('Node Type Usage Ratio by Language\n(Code Poetry vs Control Group)', pad=20)
        plt.tight_layout()
        
        # 保存
        plt.savefig(self.output_dir / "node_type_ratio_heatmap_presentation.png",
                   dpi=300, bbox_inches='tight', facecolor='white')
        plt.close()
        
        logger.info("ノードタイプ使用頻度の可視化を完了")

    def analyze_node_type_usage(self) -> Dict[str, Dict[str, Dict[str, int]]]:
        """各言語のノードタイプ使用頻度を分析"""
        logger.info("ノードタイプ使用頻度の分析開始")
        
        usage_stats = {
            'poetry': defaultdict(lambda: defaultdict(int)),
            'control': defaultdict(lambda: defaultdict(int))
        }
        
        def count_node_types(node: Dict, language: str, group: str):
            """ノードタイプを再帰的にカウント"""
            if not isinstance(node, dict):
                return
            
            node_type = node.get('type', 'unknown')
            if self._is_structural_node(node_type):
                usage_stats[group][language][node_type] += 1
            
            for child in node.get('children', []):
                count_node_types(child, language, group)
        
        # 詩的コードの分析
        for lang in ['java', 'python', 'js']:
            for sample in self.poetry_data[lang]:
                count_node_types(sample['ast'], lang, 'poetry')
        
        # 対照群の分析（各言語から最初の20サンプルのみ）
        for lang in ['java', 'python', 'js']:
            for sample in self.control_data[lang][:20]:
                count_node_types(sample['ast'], lang, 'control')
        
        # 結果の出力（テキスト形式）
        report_path = self.output_dir / "node_type_usage_report.txt"
        with open(report_path, 'w', encoding='utf-8') as f:
            f.write("=== ノードタイプ使用頻度分析 ===\n\n")
            
            for lang in ['java', 'python', 'js']:
                f.write(f"\n{lang.upper()}:\n")
                f.write("\n詩的コード上位10ノードタイプ:\n")
                sorted_poetry = sorted(
                    usage_stats['poetry'][lang].items(),
                    key=lambda x: x[1],
                    reverse=True
                )[:10]
                for node_type, count in sorted_poetry:
                    category = self._categorize_node_type(node_type, lang) or '未分類'
                    f.write(f"  - {node_type} ({category}): {count}回\n")
                
                f.write("\n対照群上位10ノードタイプ:\n")
                sorted_control = sorted(
                    usage_stats['control'][lang].items(),
                    key=lambda x: x[1],
                    reverse=True
                )[:10]
                for node_type, count in sorted_control:
                    category = self._categorize_node_type(node_type, lang) or '未分類'
                    f.write(f"  - {node_type} ({category}): {count}回\n")
                
                # 特徴的な差異の分析
                f.write("\n特徴的な差異（詩的コードと対照群の比率）:\n")
                poetry_total = sum(usage_stats['poetry'][lang].values())
                control_total = sum(usage_stats['control'][lang].values())
                
                ratios = []
                for node_type in set(usage_stats['poetry'][lang]) | set(usage_stats['control'][lang]):
                    poetry_ratio = usage_stats['poetry'][lang][node_type] / poetry_total if poetry_total > 0 else 0
                    control_ratio = usage_stats['control'][lang][node_type] / control_total if control_total > 0 else 0
                    
                    if poetry_ratio > 0 and control_ratio > 0:
                        ratio = poetry_ratio / control_ratio
                        ratios.append((node_type, ratio))
                
                # 比率の大きい順にソート
                sorted_ratios = sorted(ratios, key=lambda x: abs(x[1] - 1), reverse=True)[:5]
                for node_type, ratio in sorted_ratios:
                    category = self._categorize_node_type(node_type, lang) or '未分類'
                    if ratio > 1:
                        f.write(f"  - {node_type} ({category}): 詩的コードで{ratio:.2f}倍多い\n")
                    else:
                        f.write(f"  - {node_type} ({category}): 詩的コードで{1/ratio:.2f}倍少ない\n")
                
                f.write("\n" + "="*50 + "\n")
        
        # Frequency詳細の出力（CSV形式）
        freq_path = self.output_dir / "node_type_frequencies.csv"
        with open(freq_path, 'w', encoding='utf-8') as f:
            f.write("Language,Group,Node Type,Category,Count,Frequency(%),Rank\n")
            
            # 言語ごとに処理
            for lang in ['java', 'python', 'js']:
                # Poetry と Control のデータを準備
                poetry_total = sum(usage_stats['poetry'][lang].values())
                control_total = sum(usage_stats['control'][lang].values())
                
                # データを整形
                poetry_data = [
                    {
                        'Language': lang,
                        'Group': 'poetry',
                        'Node Type': node_type,
                        'Category': self._categorize_node_type(node_type, lang) or 'Uncategorized',
                        'Count': count,
                        'Frequency': (count / poetry_total * 100) if poetry_total > 0 else 0
                    }
                    for node_type, count in usage_stats['poetry'][lang].items()
                ]
                
                control_data = [
                    {
                        'Language': lang,
                        'Group': 'control',
                        'Node Type': node_type,
                        'Category': self._categorize_node_type(node_type, lang) or 'Uncategorized',
                        'Count': count,
                        'Frequency': (count / control_total * 100) if control_total > 0 else 0
                    }
                    for node_type, count in usage_stats['control'][lang].items()
                ]
                
                # Frequencyで降順ソート
                poetry_data = sorted(poetry_data, key=lambda x: x['Frequency'], reverse=True)
                control_data = sorted(control_data, key=lambda x: x['Frequency'], reverse=True)
                
                # ランク付け
                for i, item in enumerate(poetry_data, 1):
                    item['Rank'] = i
                for i, item in enumerate(control_data, 1):
                    item['Rank'] = i
                
                # データを書き出し
                for item in poetry_data:
                    f.write(f"{item['Language']},{item['Group']},{item['Node Type']},{item['Category']},"
                           f"{item['Count']},{item['Frequency']:.2f},{item['Rank']}\n")
                for item in control_data:
                    f.write(f"{item['Language']},{item['Group']},{item['Node Type']},{item['Category']},"
                           f"{item['Count']},{item['Frequency']:.2f},{item['Rank']}\n")
                
                # 言語間の区切りを追加
                f.write("\n")
        
        # サマリーレポートの出力（テキスト形式）
        summary_path = self.output_dir / "node_type_frequency_summary.txt"
        with open(summary_path, 'w', encoding='utf-8') as f:
            f.write("=== Node Type Frequency Summary ===\n\n")
            
            for lang in ['java', 'python', 'js']:
                f.write(f"\n{lang.upper()}\n")
                f.write("=" * 50 + "\n\n")
                
                # Poetry の上位10
                f.write("Top 10 Node Types in Code Poetry:\n")
                f.write("-" * 40 + "\n")
                poetry_total = sum(usage_stats['poetry'][lang].values())
                sorted_poetry = sorted(
                    [(k, v / poetry_total * 100) for k, v in usage_stats['poetry'][lang].items()],
                    key=lambda x: x[1],
                    reverse=True
                )[:10]
                
                for i, (node_type, freq) in enumerate(sorted_poetry, 1):
                    category = self._categorize_node_type(node_type, lang) or 'Uncategorized'
                    f.write(f"{i:2d}. {node_type:30} ({category:15}) : {freq:6.2f}%\n")
                
                # Control の上位10
                f.write("\nTop 10 Node Types in Control Group:\n")
                f.write("-" * 40 + "\n")
                control_total = sum(usage_stats['control'][lang].values())
                sorted_control = sorted(
                    [(k, v / control_total * 100) for k, v in usage_stats['control'][lang].items()],
                    key=lambda x: x[1],
                    reverse=True
                )[:10]
                
                for i, (node_type, freq) in enumerate(sorted_control, 1):
                    category = self._categorize_node_type(node_type, lang) or 'Uncategorized'
                    f.write(f"{i:2d}. {node_type:30} ({category:15}) : {freq:6.2f}%\n")
                
                f.write("\n" + "=" * 50 + "\n")
        
        logger.info(f"ノードタイプ使用頻度レポートを生成: {report_path}")
        logger.info(f"ノードタイプ頻度詳細を生成: {freq_path}")
        logger.info(f"ノードタイプ頻度サマリーを生成: {summary_path}")
        
        # 可視化の作成
        self.create_node_type_visualizations(usage_stats)
        
        return usage_stats
    
    def run_analysis(self):
        """完全な分析の実行"""
        logger.info("分析開始")
        
        # 1. データ読み込み
        self.load_data()
        
        # 2. ノードタイプの分析（デバッグ・確認用）
        self.analyze_node_types()
        
        # 3. ノードタイプの使用頻度分析
        self.analyze_node_type_usage()
        
        # 4. 言語別分析
        for lang in ['java', 'python', 'js']:
            result = self.analyze_language(lang)
            if result:
                self.results['by_language'][lang] = result
        
        # 5. プール分析
        self.results['pooled'] = self.pooled_analysis()
        
        # 6. メタ分析
        self.results['meta_analysis'] = self.meta_analysis(self.results['by_language'])
        
        # 7. 可視化
        self.create_visualizations()
        
        # 8. レポート生成
        report = self.generate_report()
        
        logger.info("分析完了")
        print("\n" + report)
        print(f"\n結果は {self.output_dir} ディレクトリに保存されました")
        print("node_types_report.txt でノードタイプの確認ができます")
        print("node_type_usage_report.txt でノードタイプの使用頻度を確認できます")

def main():
    """メイン処理"""
    analyzer = CodePoetryAnalyzer(output_dir="output/code_poetry_analysis")
    analyzer.run_analysis()

if __name__ == "__main__":
    main()
