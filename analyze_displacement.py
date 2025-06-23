#!/usr/bin/env python3
"""analyze_displacement.py

コードポエトリー記号転位分析ツール
"""

import sys
import json
import os
from pathlib import Path

# tools モジュールをインポート
sys.path.append('.')
from tools.displacement_analysis import analyze_single_poem, load_poem_data, DisplacementAnalyzer
from tools.visualization import DisplacementVisualizer


def list_available_poems():
    """利用可能な詩作品をリスト"""
    print("利用可能な作品:")
    
    js_dir = Path("corpus_processed/js")
    if js_dir.exists():
        for poem_dir in js_dir.iterdir():
            if poem_dir.is_dir() and poem_dir.name != "_cache":
                print(f"  {poem_dir.name}")


def analyze_poem_command(poem_id: str, language: str = "js", 
                        generate_visualization: bool = False):
    """詩作品を分析"""
    
    print(f"=== {poem_id} の記号転位分析 ===")
    
    try:
        # 分析を実行
        result = analyze_single_poem(poem_id, language)
        
        if "error" in result:
            print(f"エラー: {result['error']}")
            return
        
        analysis = result['analysis']
        displacements = result['displacements']
        
        # 基本統計を表示
        print(f"検出された転位: {analysis['total_displacements']}")
        
        if analysis['total_displacements'] > 0:
            print(f"最大強度: {analysis['max_intensity']:.2f}")
            print(f"平均強度: {analysis['avg_intensity']:.2f}")
            
            print("\n主要な転位:")
            for disp in analysis['top_displacements']:
                print(f"  行{disp['line']}: {disp['text']}")
                print(f"    → {disp['description']}")
                print(f"    パターン: {disp['pattern']}, 強度: {disp['intensity']:.2f}")
                print()
            
            print("詩的解釈:")
            print(analysis['poetic_interpretation'])
        else:
            print("詩的転位が検出されませんでした。")
            if 'suggestions' in analysis:
                print("提案:")
                for suggestion in analysis['suggestions']:
                    print(f"  - {suggestion}")
        
        # 結果をJSONファイルに保存
        os.makedirs('output/analysis', exist_ok=True)
        output_file = f"output/analysis/{poem_id}_displacement_analysis.json"
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(result, f, ensure_ascii=False, indent=2)
        print(f"\n詳細分析結果を保存: {output_file}")
        
        # 可視化を生成（オプション）
        if generate_visualization and analysis['total_displacements'] > 0:
            generate_visualization_command(poem_id, language)
        
    except Exception as e:
        print(f"分析中にエラーが発生しました: {e}")


def generate_visualization_command(poem_id: str, language: str = "js"):
    """可視化HTMLを生成"""
    
    print(f"=== {poem_id} の可視化生成 ===")
    
    try:
        # データを読み込み
        ast_data, code_text = load_poem_data(poem_id, language)
        
        # 分析を実行
        analyzer = DisplacementAnalyzer()
        displacements = analyzer.analyze_poem(ast_data, code_text)
        analysis_report = analyzer.generate_analysis_report(displacements)
        
        # 可視化を生成
        visualizer = DisplacementVisualizer()
        html_output = visualizer.generate_html_visualization(
            poem_id, code_text, displacements, analysis_report
        )
        
        # HTMLファイルに保存
        os.makedirs('output/visualization', exist_ok=True)
        output_file = f"output/visualization/{poem_id}_displacement_visualization.html"
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(html_output)
        
        print(f"可視化HTMLを生成: {output_file}")
        print(f"検出された転位数: {len(displacements)}")
        
    except Exception as e:
        print(f"可視化生成中にエラーが発生しました: {e}")


def compare_poems_command(poem_ids: list, language: str = "js"):
    """複数の詩作品を比較"""
    
    print("=== 詩作品比較分析 ===")
    
    results = []
    for poem_id in poem_ids:
        try:
            result = analyze_single_poem(poem_id, language)
            if "error" not in result:
                results.append(result)
            else:
                print(f"警告: {poem_id} の分析に失敗: {result['error']}")
        except Exception as e:
            print(f"警告: {poem_id} の分析中にエラー: {e}")
    
    if not results:
        print("比較可能な分析結果がありません")
        return
    
    # 比較表を表示
    print(f"\n{'作品名':<20} {'転位数':<8} {'最大強度':<10} {'平均強度':<10} {'主要パターン'}")
    print("-" * 70)
    
    for result in results:
        poem_id = result['poem_id']
        analysis = result['analysis']
        total = analysis['total_displacements']
        max_intensity = analysis.get('max_intensity', 0)
        avg_intensity = analysis.get('avg_intensity', 0)
        
        # 主要パターンを取得
        patterns = analysis.get('pattern_distribution', {})
        main_pattern = max(patterns.keys(), key=lambda k: patterns[k]['count']) if patterns else "なし"
        
        print(f"{poem_id:<20} {total:<8} {max_intensity:<10.2f} {avg_intensity:<10.2f} {main_pattern}")
    
    # 比較結果をJSONで保存
    comparison_result = {
        "comparison_timestamp": str(Path().cwd()),
        "poems": results,
        "summary": {
            "total_poems": len(results),
            "avg_displacements": sum(r['analysis']['total_displacements'] for r in results) / len(results),
            "most_displaced": max(results, key=lambda r: r['analysis']['total_displacements'])['poem_id'],
            "least_displaced": min(results, key=lambda r: r['analysis']['total_displacements'])['poem_id']
        }
    }
    
    os.makedirs('output/comparison', exist_ok=True)
    output_file = f"output/comparison/poem_comparison_{len(results)}_works.json"
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(comparison_result, f, ensure_ascii=False, indent=2)
    
    print(f"\n比較結果を保存: {output_file}")


def main():
    """メイン関数"""
    
    if len(sys.argv) < 2:
        print("コードポエトリー記号転位分析ツール")
        print()
        print("使用法:")
        print("  python analyze_displacement.py list")
        print("  python analyze_displacement.py analyze <poem_id> [--viz]")
        print("  python analyze_displacement.py visualize <poem_id>")
        print("  python analyze_displacement.py compare <poem_id1> <poem_id2> ...")
        print()
        list_available_poems()
        return
    
    command = sys.argv[1]
    
    if command == "list":
        list_available_poems()
    
    elif command == "analyze":
        if len(sys.argv) < 3:
            print("エラー: 詩作品IDを指定してください")
            return
        
        poem_id = sys.argv[2]
        generate_viz = "--viz" in sys.argv
        analyze_poem_command(poem_id, generate_visualization=generate_viz)
    
    elif command == "visualize":
        if len(sys.argv) < 3:
            print("エラー: 詩作品IDを指定してください")
            return
        
        poem_id = sys.argv[2]
        generate_visualization_command(poem_id)
    
    elif command == "compare":
        if len(sys.argv) < 4:
            print("エラー: 比較する詩作品IDを2つ以上指定してください")
            return
        
        poem_ids = sys.argv[2:]
        compare_poems_command(poem_ids)
    
    else:
        print(f"不明なコマンド: {command}")
        print("利用可能なコマンド: list, analyze, visualize, compare")


if __name__ == "__main__":
    main()