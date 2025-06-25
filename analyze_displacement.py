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
from tools.displacement_analysis import analyze_single_poem, load_poem_data, MinimalDisplacementAnalyzer
from tools.visualization import DisplacementVisualizer


def list_available_poems():
    """利用可能な詩作品をリスト"""
    languages = ["js", "python", "html", "c", "java", "cpp"] 
    
    print("利用可能な作品:")
    for lang in languages:
        lang_dir = Path(f"corpus_processed/{lang}")
        if lang_dir.exists():
            print(f"\n{lang.upper()}:")
            poem_files = []
            for poem_dir in lang_dir.iterdir():
                if poem_dir.is_dir() and poem_dir.name != "_cache":
                    poem_files.append(poem_dir.name)
            
            for poem_id in sorted(poem_files):
                print(f"  {poem_id}")
        else:
            print(f"\n{lang.upper()}: (処理済みファイルなし)")


def show_ast_command(poem_id: str, language: str = "js", output_to_file: bool = False):
    """構文解析結果（AST）を表示"""
    
    print(f"=== {poem_id} の構文解析結果 (AST) ===")
    
    try:
        # ASTデータを読み込み
        ast_data, code_text = load_poem_data(poem_id, language)
        
        # 出力内容を準備
        output_lines = []
        output_lines.append(f"=== {poem_id} の構文解析結果 (AST) ===")
        output_lines.append("")
        output_lines.append("ソースコード:")
        output_lines.append("-" * 40)
        for i, line in enumerate(code_text.splitlines(), 1):
            output_lines.append(f"{i:2}: {line}")
        
        output_lines.append("")
        output_lines.append("構文解析結果 (AST):")
        output_lines.append("-" * 40)
        output_lines.append(json.dumps(ast_data, indent=2, ensure_ascii=False))
        
        # 画面に出力
        for line in output_lines:
            print(line)
        
        # ファイルに出力（オプション）
        if output_to_file:
            os.makedirs('output/ast', exist_ok=True)
            output_file = f"output/ast/{poem_id}_ast_{language}.txt"
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write("\n".join(output_lines))
            print(f"\n構文解析結果をファイルに保存: {output_file}")
        
    except FileNotFoundError as e:
        print(f"エラー: {e}")
    except Exception as e:
        print(f"分析中にエラーが発生しました: {e}")

def analyze_poem_command(poem_id: str, language: str = "js", 
                        generate_visualization: bool = False):
    """詩作品を分析（記号転位検出のみ）"""
    
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
            print("\n検出された記号転位:")
            for disp in analysis['detected_displacements']:
                print(f"  行{disp['line']}: {disp['text']}")
                print(f"    → {disp['description']}")
                print(f"    転位: {disp['expected_sign_type']} → {disp['actual_sign_type']}")
                print(f"    根拠: {disp['theoretical_basis']}")
                print()
            
            print("理論的要約:")
            print(analysis['theoretical_summary'])
        else:
            print(analysis['message'])
            if 'theoretical_summary' in analysis:
                print(analysis['theoretical_summary'])
        
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
        print("  python analyze_displacement.py ast <poem_id> [--lang js|python] [--output file]")
        print("  python analyze_displacement.py analyze <poem_id> [--lang js|python] [--viz]")
        print("  python analyze_displacement.py visualize <poem_id> [--lang js|python]")
        print("  python analyze_displacement.py compare <poem_id1> <poem_id2> ... [--lang js|python]")
        print()
        list_available_poems()
        return
    
    command = sys.argv[1]
    
    if command == "list":
        list_available_poems()
    
    elif command == "ast":
        if len(sys.argv) < 3:
            print("エラー: 詩作品IDを指定してください")
            return
        
        poem_id = sys.argv[2]
        language = "js"  # デフォルト
        if "--lang" in sys.argv:
            lang_idx = sys.argv.index("--lang")
            if lang_idx + 1 < len(sys.argv):
                language = sys.argv[lang_idx + 1]
        
        output_to_file = "--output" in sys.argv and "file" in sys.argv
        show_ast_command(poem_id, language, output_to_file)
    
    elif command == "analyze":
        if len(sys.argv) < 3:
            print("エラー: 詩作品IDを指定してください")
            return
        
        poem_id = sys.argv[2]
        language = "js"  # デフォルト
        if "--lang" in sys.argv:
            lang_idx = sys.argv.index("--lang")
            if lang_idx + 1 < len(sys.argv):
                language = sys.argv[lang_idx + 1]
        
        generate_viz = "--viz" in sys.argv
        analyze_poem_command(poem_id, language, generate_viz)
    
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
        print("利用可能なコマンド: list, ast, analyze, visualize, compare")


if __name__ == "__main__":
    main()