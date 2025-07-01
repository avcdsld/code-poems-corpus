#!/usr/bin/env python3
"""analyze_displacement.py

コード構文解析ツール
"""

import sys
import json
import os
from pathlib import Path

# tools モジュールをインポート
sys.path.append('.')
from tools.parser.plugins import get_parser_for_language


def parse_code(file_path: str, language: str, output_dir: Path):
    """コードを処理し、構文解析結果を保存する"""
    try:
        # コードを読み込み
        with open(file_path, 'r', encoding='utf-8') as f:
            code_text = f.read()
            
        # 言語に対応したパーサーを取得
        parser = get_parser_for_language(language)
        if not parser:
            raise ValueError(f"未対応の言語です: {language}")
            
        # 構文解析を実行
        ast = parser.parse_ast(code_text)
        
        # 結果を保存
        ast_file = output_dir / "ast.json"
        code_file = output_dir / "code.txt"
        
        with open(ast_file, 'w', encoding='utf-8') as f:
            json.dump(ast, f, indent=2, ensure_ascii=False)
            
        with open(code_file, 'w', encoding='utf-8') as f:
            f.write(code_text)
            
        print(f"[✓] {file_path} の処理が完了しました")
        print(f"    AST: {ast_file}")
        print(f"    Code: {code_file}")
        
    except Exception as e:
        print(f"[!] {file_path} の処理中にエラーが発生しました: {e}")


def process_control_directory(language: str):
    """対照群のディレクトリ全体を処理"""
    control_dir = Path(f"control_raw/{language}")
    if not control_dir.exists():
        print(f"[!] 対照群ディレクトリが見つかりません: {control_dir}")
        return
        
    print(f"=== {language.upper()} の対照群処理を開始 ===")
    
    for file_path in control_dir.glob("*.*"):
        if file_path.is_file():
            # ファイル名から番号を抽出
            file_name = file_path.stem
            code_id = file_name.split('_')[0] if '_' in file_name else file_name
            
            # 出力ディレクトリを準備
            output_dir = Path(f"control_processed/{language}/{code_id}/static")
            output_dir.mkdir(parents=True, exist_ok=True)
            
            parse_code(str(file_path), language, output_dir)
            
    print(f"=== {language.upper()} の対照群処理が完了 ===")


def process_poem_directory(language: str):
    """コードポエトリーのディレクトリ全体を処理"""
    poem_dir = Path(f"corpus_raw/{language}")
    if not poem_dir.exists():
        print(f"[!] コードポエトリーディレクトリが見つかりません: {poem_dir}")
        return
        
    print(f"=== {language.upper()} のコードポエトリー処理を開始 ===")
    
    for file_path in poem_dir.glob("*.*"):
        if file_path.is_file():
            # 出力ディレクトリを準備
            poem_id = file_path.stem
            output_dir = Path(f"corpus_processed/{language}/{poem_id}/static")
            output_dir.mkdir(parents=True, exist_ok=True)
            
            parse_code(str(file_path), language, output_dir)
            
    print(f"=== {language.upper()} のコードポエトリー処理が完了 ===")


def process_all_languages(command: str):
    """すべての言語を処理"""
    languages = ['python', 'js', 'java', 'ruby']
    
    for language in languages:
        if command == "process-control":
            process_control_directory(language)
        elif command == "process-poems":
            process_poem_directory(language)


def main():
    """メイン処理"""
    
    if len(sys.argv) < 2:
        print("使用方法:")
        print("  analyze_displacement.py process-control [--language <lang>]")
        print("  analyze_displacement.py process-poems [--language <lang>]")
        print("  analyze_displacement.py process-all-control")
        print("  analyze_displacement.py process-all-poems")
        return

    command = sys.argv[1]
    
    if command in ["process-all-control", "process-all-poems"]:
        actual_command = "process-control" if command == "process-all-control" else "process-poems"
        process_all_languages(actual_command)
        return
    
    # 単一言語の処理
    language = "js"  # デフォルト言語
    
    # オプション解析
    i = 2
    while i < len(sys.argv):
        if sys.argv[i] == "--language":
            if i + 1 < len(sys.argv):
                language = sys.argv[i + 1]
                i += 2
            else:
                print("エラー: --language オプションには言語を指定してください")
                return
        else:
            print(f"警告: 不明なオプション: {sys.argv[i]}")
            i += 1
    
    if command == "process-control":
        process_control_directory(language)
    elif command == "process-poems":
        process_poem_directory(language)
    else:
        print(f"エラー: 不明なコマンド: {command}")
        return


if __name__ == "__main__":
    main()
