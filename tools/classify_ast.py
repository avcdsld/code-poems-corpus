#!/usr/bin/env python3
"""
設定ファイル駆動のパース記号論分析システム
Configuration-driven Peircean Semiotic Analysis
"""

import json
import yaml
import numpy as np
import pandas as pd
from pathlib import Path
from typing import Dict, List, Tuple, Optional
from collections import defaultdict, Counter
from dataclasses import dataclass
import logging
from datetime import datetime

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@dataclass
class SemioticNode:
    """記号分類されたノード"""
    node_type: str
    sign_type: str      # qualisign, sinsign, legisign
    sign_mode: str      # icon, index, symbol
    count: int = 0

class ConfigBasedSemioticAnalyzer:
    """設定ファイル駆動のパース記号分析"""
    
    def __init__(self, config_path: str = "config.yml", 
                 output_dir: str = "output"):
        self.config_path = Path(config_path)
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(exist_ok=True)
        
        # 設定読み込み
        self.classification_config = self._load_config()
        
        # データ格納
        self.poetry_data = defaultdict(list)
        self.control_data = defaultdict(list)
        
        # 分析結果
        self.analysis_results = {}
        
    def _load_config(self) -> Dict:
        """YAML設定ファイルの読み込み"""
        try:
            with open(self.config_path, 'r', encoding='utf-8') as f:
                config = yaml.safe_load(f)
            logger.info(f"設定ファイル読み込み成功: {self.config_path}")
            return config['semiotic_classification']
        except FileNotFoundError:
            logger.error(f"設定ファイルが見つかりません: {self.config_path}")
            raise
        except yaml.YAMLError as e:
            logger.error(f"YAML解析エラー: {e}")
            raise
    
    def load_data(self):
        """データの読み込み"""
        logger.info("データ読み込み開始")
        
        for lang in ['java', 'python', 'js']:
            # 詩的コードの読み込み
            poetry_dir = Path(f"corpus_processed/{lang}")
            if poetry_dir.exists():
                for ast_path in poetry_dir.glob("**/static/ast.json"):
                    try:
                        with open(ast_path, 'r', encoding='utf-8') as f:
                            ast_data = json.load(f)
                        
                        self.poetry_data[lang].append({
                            'ast': ast_data,
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
                        
                        self.control_data[lang].append({
                            'ast': ast_data,
                            'id': ast_path.parent.parent.name,
                            'path': str(ast_path)
                        })
                    except Exception as e:
                        logger.error(f"Error loading {ast_path}: {e}")
        
        # データ読み込み結果
        for lang in ['java', 'python', 'js']:
            logger.info(f"{lang}: Poetry={len(self.poetry_data[lang])}, "
                       f"Control={len(self.control_data[lang])}")
    
    def classify_node(self, node_type: str, language: str) -> Optional[SemioticNode]:
        """ノードの記号分類"""
        lang_config = self.classification_config.get(language, {})
        node_config = lang_config.get(node_type)
        
        if node_config:
            return SemioticNode(
                node_type=node_type,
                sign_type=node_config['sign_type'],
                sign_mode=node_config['sign_mode']
            )
        else:
            # 未分類のノードは記録するが、分析では除外
            logger.debug(f"未分類ノード: {language}.{node_type}")
            return None
    
    def extract_semiotic_distribution(self, samples: List[Dict], language: str) -> Dict:
        """サンプル群の記号分布を抽出"""
        # 記号カテゴリ別カウント
        sign_type_counts = Counter()  # qualisign, sinsign, legisign
        sign_mode_counts = Counter()  # icon, index, symbol
        
        # 個別ノード分類結果
        classified_nodes = {}
        unclassified_nodes = set()
        
        total_classified_nodes = 0
        
        for sample in samples:
            node_types = self._extract_node_types(sample['ast'])
            
            for node_type, count in node_types.items():
                classification = self.classify_node(node_type, language)
                
                if classification:
                    # 分類成功
                    sign_type_counts[classification.sign_type] += count
                    sign_mode_counts[classification.sign_mode] += count
                    total_classified_nodes += count
                    
                    # ノード別集計
                    if node_type not in classified_nodes:
                        classified_nodes[node_type] = SemioticNode(
                            node_type=node_type,
                            sign_type=classification.sign_type,
                            sign_mode=classification.sign_mode,
                            count=0
                        )
                    classified_nodes[node_type].count += count
                else:
                    # 未分類
                    unclassified_nodes.add(node_type)
        
        # 割合計算
        sign_type_ratios = {
            category: count / total_classified_nodes * 100 if total_classified_nodes > 0 else 0
            for category, count in sign_type_counts.items()
        }
        
        sign_mode_ratios = {
            mode: count / total_classified_nodes * 100 if total_classified_nodes > 0 else 0
            for mode, count in sign_mode_counts.items()
        }
        
        return {
            'sign_type_distribution': sign_type_ratios,
            'sign_mode_distribution': sign_mode_ratios,
            'classified_nodes': classified_nodes,
            'unclassified_nodes': unclassified_nodes,
            'total_classified': total_classified_nodes,
            'classification_coverage': len(classified_nodes) / (len(classified_nodes) + len(unclassified_nodes)) * 100 if (len(classified_nodes) + len(unclassified_nodes)) > 0 else 0
        }
    
    def _extract_node_types(self, ast: Dict) -> Counter:
        """ASTからノードタイプを抽出"""
        node_types = Counter()
        
        def traverse(node: Dict):
            if not isinstance(node, dict):
                return
            
            node_type = node.get('type')
            if node_type:
                node_types[node_type] += 1
            
            for child in node.get('children', []):
                traverse(child)
        
        traverse(ast)
        return node_types
    
    def analyze_semiotic_patterns(self):
        """記号パターンの分析"""
        logger.info("記号パターン分析開始")
        
        results = {}
        
        for lang in ['java', 'python', 'js']:
            if not self.poetry_data[lang] or not self.control_data[lang]:
                logger.warning(f"{lang}のデータが不足")
                continue
            
            # 各群の分析
            poetry_analysis = self.extract_semiotic_distribution(
                self.poetry_data[lang], lang
            )
            control_analysis = self.extract_semiotic_distribution(
                self.control_data[lang][:30], lang  # 比較用に制限
            )
            
            # 差異の計算
            sign_type_diff = {}
            for category in ['qualisign', 'sinsign', 'legisign']:
                poetry_ratio = poetry_analysis['sign_type_distribution'].get(category, 0)
                control_ratio = control_analysis['sign_type_distribution'].get(category, 0)
                sign_type_diff[category] = poetry_ratio - control_ratio
            
            sign_mode_diff = {}
            for mode in ['icon', 'index', 'symbol']:
                poetry_ratio = poetry_analysis['sign_mode_distribution'].get(mode, 0)
                control_ratio = control_analysis['sign_mode_distribution'].get(mode, 0)
                sign_mode_diff[mode] = poetry_ratio - control_ratio
            
            results[lang] = {
                'poetry': poetry_analysis,
                'control': control_analysis,
                'sign_type_differences': sign_type_diff,
                'sign_mode_differences': sign_mode_diff
            }
        
        self.analysis_results = results
        return results
    
    def generate_detailed_report(self):
        """詳細分析レポートの生成"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        report_path = self.output_dir / "semiotic_analysis_detailed.txt"
        
        with open(report_path, 'w', encoding='utf-8') as f:
            f.write("=" * 80 + "\n")
            f.write("パース記号論分析 - 詳細レポート\n")
            f.write("Peircean Semiotic Analysis - Detailed Report\n")
            f.write("=" * 80 + "\n\n")
            f.write(f"生成日時: {timestamp}\n")
            f.write(f"設定ファイル: {self.config_path}\n\n")
            
            # 分析概要
            self._write_analysis_overview(f)
            
            # 言語別詳細分析
            for lang in ['java', 'python', 'js']:
                if lang not in self.analysis_results:
                    continue
                
                self._write_language_analysis(f, lang)
            
            # 横断的分析
            self._write_cross_language_analysis(f)
            
            # 分類カバレッジレポート
            self._write_classification_coverage(f)
            
            # 統計的注意事項
            self._write_statistical_caveats(f)
        
        logger.info(f"詳細レポート生成: {report_path}")
    
    def _write_analysis_overview(self, f):
        """分析概要の記述"""
        f.write("【分析概要】\n")
        f.write("このレポートは、パース記号論の三分類を用いてコード構文を分析します:\n\n")
        
        f.write("存在カテゴリー (Sign Type):\n")
        f.write("• Qualisign: 質的記号 - 抽象的性質や概念（型、修飾子等）\n")
        f.write("• Sinsign: 単一記号 - 具体的存在や実例（リテラル、識別子出現等）\n")
        f.write("• Legisign: 法則記号 - 構文規則や慣習（制御構造、演算子等）\n\n")
        
        f.write("対象関係 (Sign Mode):\n")
        f.write("• Icon: 類似記号 - 対象との類似関係（構造的表現、視覚的類似等）\n")
        f.write("• Index: 指標記号 - 対象との因果/指示関係（実行順序、参照等）\n")
        f.write("• Symbol: 象徴記号 - 対象との慣習的関係（キーワード、演算子等）\n\n")
        
    def _write_language_analysis(self, f, lang: str):
        """言語別分析の記述"""
        result = self.analysis_results[lang]
        
        f.write(f"【{lang.upper()} 分析結果】\n")
        f.write("=" * 60 + "\n\n")
        
        # 分類カバレッジ
        poetry_coverage = result['poetry']['classification_coverage']
        control_coverage = result['control']['classification_coverage']
        f.write(f"分類カバレッジ:\n")
        f.write(f"• Poetry: {poetry_coverage:.1f}%\n")
        f.write(f"• Control: {control_coverage:.1f}%\n\n")
        
        # 存在カテゴリー分布
        f.write("存在カテゴリー分布 (%):\n")
        f.write("-" * 50 + "\n")
        f.write(f"{'Category':<12} {'Poetry':<10} {'Control':<10} {'Diff':<10}\n")
        f.write("-" * 50 + "\n")
        
        for category in ['qualisign', 'sinsign', 'legisign']:
            poetry_val = result['poetry']['sign_type_distribution'].get(category, 0)
            control_val = result['control']['sign_type_distribution'].get(category, 0)
            diff = result['sign_type_differences'].get(category, 0)
            
            f.write(f"{category:<12} {poetry_val:<10.1f} {control_val:<10.1f} {diff:<+10.1f}\n")
        
        f.write("\n")
        
        # 対象関係分布
        f.write("対象関係分布 (%):\n")
        f.write("-" * 50 + "\n")
        f.write(f"{'Mode':<12} {'Poetry':<10} {'Control':<10} {'Diff':<10}\n")
        f.write("-" * 50 + "\n")
        
        for mode in ['icon', 'index', 'symbol']:
            poetry_val = result['poetry']['sign_mode_distribution'].get(mode, 0)
            control_val = result['control']['sign_mode_distribution'].get(mode, 0)
            diff = result['sign_mode_differences'].get(mode, 0)
            
            f.write(f"{mode:<12} {poetry_val:<10.1f} {control_val:<10.1f} {diff:<+10.1f}\n")
        
        f.write("\n")
        
        # 未分類ノード一覧
        unclassified_poetry = result['poetry']['unclassified_nodes']
        unclassified_control = result['control']['unclassified_nodes']
        all_unclassified = unclassified_poetry | unclassified_control
        
        if all_unclassified:
            f.write(f"未分類ノードタイプ ({len(all_unclassified)}個):\n")
            sorted_unclassified = sorted(all_unclassified)
            for i in range(0, len(sorted_unclassified), 5):
                line_nodes = sorted_unclassified[i:i+5]
                f.write(f"  {', '.join(line_nodes)}\n")
            f.write("\n")
        
        f.write("=" * 60 + "\n\n")
    
    def _write_cross_language_analysis(self, f):
        """横断的分析の記述"""
        f.write("【言語横断的パターン】\n")
        f.write("=" * 50 + "\n\n")
        
        # 存在カテゴリーの平均差異
        f.write("存在カテゴリー - 平均差異 (Poetry - Control):\n")
        for category in ['qualisign', 'sinsign', 'legisign']:
            diffs = []
            for lang in ['java', 'python', 'js']:
                if lang in self.analysis_results:
                    diff = self.analysis_results[lang]['sign_type_differences'].get(category, 0)
                    diffs.append((lang, diff))
            
            if diffs:
                avg_diff = np.mean([d[1] for d in diffs])
                f.write(f"\n{category.capitalize()}: 平均 {avg_diff:+.1f}%\n")
                for lang, diff in diffs:
                    f.write(f"  {lang}: {diff:+.1f}%\n")
        
        f.write("\n")
        
        # 対象関係の平均差異
        f.write("対象関係 - 平均差異 (Poetry - Control):\n")
        for mode in ['icon', 'index', 'symbol']:
            diffs = []
            for lang in ['java', 'python', 'js']:
                if lang in self.analysis_results:
                    diff = self.analysis_results[lang]['sign_mode_differences'].get(mode, 0)
                    diffs.append((lang, diff))
            
            if diffs:
                avg_diff = np.mean([d[1] for d in diffs])
                f.write(f"\n{mode.capitalize()}: 平均 {avg_diff:+.1f}%\n")
                for lang, diff in diffs:
                    f.write(f"  {lang}: {diff:+.1f}%\n")
        
        f.write("\n" + "=" * 50 + "\n\n")
    
    def _write_classification_coverage(self, f):
        """分類カバレッジレポート"""
        f.write("【分類カバレッジ分析】\n")
        f.write("=" * 40 + "\n\n")
        
        for lang in ['java', 'python', 'js']:
            if lang in self.analysis_results:
                result = self.analysis_results[lang]
                
                poetry_total = len(result['poetry']['classified_nodes']) + len(result['poetry']['unclassified_nodes'])
                control_total = len(result['control']['classified_nodes']) + len(result['control']['unclassified_nodes'])
                
                f.write(f"{lang.upper()}:\n")
                f.write(f"• Poetry: {len(result['poetry']['classified_nodes'])}/{poetry_total} ノードタイプが分類済み\n")
                f.write(f"• Control: {len(result['control']['classified_nodes'])}/{control_total} ノードタイプが分類済み\n")
                f.write(f"• 分類率: Poetry {result['poetry']['classification_coverage']:.1f}%, "
                       f"Control {result['control']['classification_coverage']:.1f}%\n\n")
        
        f.write("=" * 40 + "\n\n")
    
    def _write_statistical_caveats(self, f):
        """統計的注意事項"""
        f.write("【統計的注意事項・研究制約】\n")
        f.write("=" * 40 + "\n\n")
        
        f.write("1. サンプルサイズの制約:\n")
        f.write("   • 詩的コードは15作品と極めて限定的\n")
        f.write("   • 統計的推論には不十分な規模\n\n")
        
        f.write("2. 記号分類の主観性:\n")
        f.write("   • パース記号論の適用は研究者の解釈に依存\n")
        f.write("   • 同一構文要素でも文脈により分類が変わりうる\n\n")
        
        f.write("3. 理論的妥当性の課題:\n")
        f.write("   • プログラミング構文への記号論適用の妥当性は未検証\n")
        f.write("   • 構文構造と記号機能の対応関係は複雑\n\n")
        
        f.write("4. 分析の位置づけ:\n")
        f.write("   • この分析は予備的・探索的研究として位置づけられる\n")
        f.write("   • 確定的結論ではなく、仮説生成のための初期観察\n\n")
        
        f.write("5. 今後の課題:\n")
        f.write("   • より大規模なサンプルでの検証\n")
        f.write("   • 記号分類の妥当性・信頼性の検証\n")
        f.write("   • 代替的理論枠組みとの比較検討\n\n")
        
    def export_classification_data(self):
        """分類データのCSV出力"""
        for lang in ['java', 'python', 'js']:
            if lang not in self.analysis_results:
                continue
            
            # Poetry データ
            poetry_data = []
            for node_type, node_obj in self.analysis_results[lang]['poetry']['classified_nodes'].items():
                poetry_data.append({
                    'language': lang,
                    'group': 'poetry',
                    'node_type': node_type,
                    'sign_type': node_obj.sign_type,
                    'sign_mode': node_obj.sign_mode,
                    'count': node_obj.count
                })
            
            # Control データ
            control_data = []
            for node_type, node_obj in self.analysis_results[lang]['control']['classified_nodes'].items():
                control_data.append({
                    'language': lang,
                    'group': 'control',
                    'node_type': node_type,
                    'sign_type': node_obj.sign_type,
                    'sign_mode': node_obj.sign_mode,
                    'count': node_obj.count
                })
            
            # CSV出力
            all_data = poetry_data + control_data
            if all_data:
                df = pd.DataFrame(all_data)
                csv_path = self.output_dir / f"semiotic_classification_{lang}.csv"
                df.to_csv(csv_path, index=False, encoding='utf-8')
                logger.info(f"分類データ出力: {csv_path}")
    
    def run_analysis(self):
        """分析の実行"""
        logger.info("設定駆動記号論分析開始")
        
        # データ読み込み
        self.load_data()
        
        # 記号パターン分析
        self.analyze_semiotic_patterns()
        
        # レポート生成
        self.generate_detailed_report()
        
        # データ出力
        self.export_classification_data()
        
        logger.info("分析完了")
        print(f"\n結果は {self.output_dir} ディレクトリに保存されました")

def main():
    """メイン処理"""
    analyzer = ConfigBasedSemioticAnalyzer(
        config_path="config.yml",
        output_dir="output/semiotic_analysis"
    )
    analyzer.run_analysis()

if __name__ == "__main__":
    main()
