import sys
from pathlib import Path
import yaml
import html
from tree_sitter_language_pack import get_parser

# ---------- Configuration ----------
BASE_DIR = Path(__file__).resolve().parents[2]
RAW_DIR = BASE_DIR / "corpus_raw"
TEI_DIR = BASE_DIR / "corpus_tei" / "draft"  # 出力先を変更
LANGMAP_YML = BASE_DIR / "tools" / "parser" / "langmap.yml"
CLASSMAP_YML = BASE_DIR / "tools" / "parser" / "classmap.yml"

# デバッグモード
DEBUG = False

DEFAULT_LANGMAP = {
    ".pde": "java",
    ".py": "python",
    ".java": "java",
    ".js": "javascript",
    ".cpp": "cpp",
    ".cs": "csharp",
    ".clj": "clojure",
    ".c": "c",
    ".rb": "ruby",
    ".sh": "bash",
    ".html": "html",
}

DEFAULT_CLASSMAP = {
    "string_literal": "icon",
    "number_literal": "icon",
    "comment": "icon",
    "regex_literal": "icon",
    "template_string": "icon",
    "identifier": "index",
    "type_identifier": "symbol",
    "primitive_type": "symbol",
    "property_identifier": "index",
    "operator": "symbol",
    "keyword": "symbol"
}

# 言語ごとの特定キーワードのリスト
JS_KEYWORDS = [
    "function", "if", "else", "for", "while", "try", "catch", "return", "var", 
    "let", "const", "break", "continue", "switch", "case", "default", "new", "this"
]

CPP_KEYWORDS = [
    "class", "struct", "void", "int", "float", "double", "char", "bool", "public", 
    "private", "protected", "const", "static", "if", "else", "for", "while", "try", 
    "catch", "return", "new", "delete", "throw"
]

PYTHON_KEYWORDS = [
    "def", "class", "if", "else", "elif", "for", "while", "try", "except", 
    "finally", "with", "return", "import", "from", "as", "pass", "break", "continue"
]

# 言語ごとの演算子リスト
JS_OPERATORS = ["&&", "||", "!", "==", "===", "!=", "!==", "+", "-", "*", "/", "%", "=", "+=", "-=", "*=", "/="]
CPP_OPERATORS = ["&&", "||", "!", "==", "!=", "+", "-", "*", "/", "%", "=", "+=", "-=", "*=", "/=", "->", "::"]
PYTHON_OPERATORS = ["and", "or", "not", "==", "!=", "+", "-", "*", "/", "%", "=", "+=", "-=", "*=", "/="]

def load_yaml_map(path: Path, default: dict) -> dict:
    if path.exists():
        return {k: v for k, v in yaml.safe_load(path.read_text()).items()}
    return default

def get_language_specific_tokens(language):
    """言語ごとの特定トークンを取得"""
    keywords = []
    operators = []
    
    if language == "javascript":
        keywords = JS_KEYWORDS
        operators = JS_OPERATORS
    elif language in ["cpp", "c"]:
        keywords = CPP_KEYWORDS
        operators = CPP_OPERATORS
    elif language == "python":
        keywords = PYTHON_KEYWORDS
        operators = PYTHON_OPERATORS
    
    return keywords, operators

def collect_all_tokens(node, source_code, classmap, language, tokens=None):
    """すべてのタイプのトークンを収集"""
    if tokens is None:
        tokens = []
    
    # ノードのタイプをチェック
    node_type = node.type
    cls = classmap.get(node_type)
    
    # ノードのテキスト内容を取得
    start_byte = node.start_byte
    end_byte = node.end_byte
    text = source_code[start_byte:end_byte].decode('utf8', errors='replace')
    
    # 特定の言語キーワードと演算子をチェック
    keywords, operators = get_language_specific_tokens(language)
    
    # 1. クラスマップに定義されたノードタイプを処理
    if cls:
        s_line, s_col = node.start_point
        e_line, e_col = node.end_point
        
        if DEBUG:
            print(f"Found {cls} token from type '{node_type}': '{text}' at ({s_line+1}:{s_col}-{e_line+1}:{e_col})")
        
        tokens.append((cls, s_line + 1, s_col, e_line + 1, e_col, text))
    
    # 2. 言語特有のキーワードを処理
    elif text in keywords:
        s_line, s_col = node.start_point
        e_line, e_col = node.end_point
        
        if DEBUG:
            print(f"Found symbol token from keyword: '{text}' at ({s_line+1}:{s_col}-{e_line+1}:{e_col})")
        
        tokens.append(("symbol", s_line + 1, s_col, e_line + 1, e_col, text))
    
    # 3. 言語特有の演算子を処理
    elif text in operators:
        s_line, s_col = node.start_point
        e_line, e_col = node.end_point
        
        if DEBUG:
            print(f"Found symbol token from operator: '{text}' at ({s_line+1}:{s_col}-{e_line+1}:{e_col})")
        
        tokens.append(("symbol", s_line + 1, s_col, e_line + 1, e_col, text))
    
    # 子ノードを処理
    for child in node.children:
        collect_all_tokens(child, source_code, classmap, language, tokens)
    
    return tokens

def remove_overlapping_tokens(tokens):
    """トークン間の重複を最小限に抑えつつ排除"""
    if not tokens:
        return []
    
    # トークンをクラス、位置でソート
    def token_sort_key(token):
        cls, s_line, s_col, e_line, e_col, _ = token
        priority = {"symbol": 3, "index": 2, "icon": 1}.get(cls, 0)
        return (s_line, s_col, -priority)
    
    sorted_tokens = sorted(tokens, key=token_sort_key)
    
    # 厳密な包含関係をチェック（完全に含まれる場合のみ重複と見なす）
    def strictly_contains(t1, t2):
        cls1, s_line1, s_col1, e_line1, e_col1, _ = t1
        cls2, s_line2, s_col2, e_line2, e_col2, _ = t2
        
        # t1がt2を完全に含む場合
        return (s_line1 <= s_line2 and e_line1 >= e_line2 and 
                (s_line1 < s_line2 or s_col1 <= s_col2) and 
                (e_line1 > e_line2 or e_col1 >= e_col2))
    
    # 特定のクラスの組み合わせでは共存を許可
    def can_coexist(t1, t2):
        cls1, _, _, _, _, _ = t1
        cls2, _, _, _, _, _ = t2
        
        # symbolとindexの組み合わせは共存可能
        return (cls1 == "symbol" and cls2 == "index") or (cls1 == "index" and cls2 == "symbol")
    
    # 重複排除（完全包含のみ）
    result = []
    for i, token in enumerate(sorted_tokens):
        # このトークンが他のどのトークンにも完全に含まれていない場合、または
        # 特定の条件で共存可能な場合に追加
        should_keep = True
        for other in result:
            if strictly_contains(other, token) and not can_coexist(other, token):
                should_keep = False
                break
        
        if should_keep:
            result.append(token)
    
    # 位置順に並べ直す
    result.sort(key=lambda t: (t[1], t[2]))
    
    return result

def generate_xml_id(line, col, text):
    """XMLのid属性を生成（一意性のために行と列を含める）"""
    # 識別子として使える形式のテキストに変換
    id_text = ''.join(c for c in text if c.isalnum())
    if len(id_text) > 10:  # 長すぎる場合は切り詰める
        id_text = id_text[:10]
    # 空の場合はプレースホルダーを使用
    if not id_text:
        id_text = "empty"
    # 行と列の情報を含めて一意性を確保
    return f"l{line}c{col}-{id_text}"

def parse_and_tei(src: Path, lang_key: str, classmap: dict):
    parser = get_parser(lang_key)
    source_code = src.read_bytes()
    tree = parser.parse(source_code)
    lines = source_code.decode(errors="replace").splitlines()
    
    if DEBUG:
        print(f"\nParsing {src.name} with {lang_key} parser")
    
    # すべてのトークンを収集
    tokens = collect_all_tokens(tree.root_node, source_code, classmap, lang_key)
    
    # 重なりのあるトークンを削除
    clean_tokens = remove_overlapping_tokens(tokens)
    
    if DEBUG:
        print(f"Collected {len(tokens)} tokens, kept {len(clean_tokens)} after removing overlaps")
    
    # TEI line elements
    line_elements = [
        f'        <l xml:id="l{n+1}">{html.escape(line, quote=False)}</l>'
        for n, line in enumerate(lines)
    ]
    
    # 新しい形式のスパンを生成
    spans = []
    for cls, sl, sc, el, ec, text in clean_tokens:
        xml_id = generate_xml_id(sl, sc, text)
        span = (
            f'        <span xml:id="{xml_id}"\n'
            f'              static-sign="{cls}"\n'
            f'              from="l{sl}:{sc}" to="l{el}:{ec}"\n'
            f'              text="{html.escape(text, quote=True)}"/>'
        )
        spans.append(span)
    
    # TEI XMLを生成
    tei_xml = (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<TEI xmlns="http://www.tei-c.org/ns/1.0">\n'
        '  <teiHeader>\n'
        '    <fileDesc>\n'
        f'      <titleStmt><title>{src.name}</title></titleStmt>\n'
        '      <publicationStmt><p>Generated by parse_corpus.py</p></publicationStmt>\n'
        '      <sourceDesc><p>Original source code</p></sourceDesc>\n'
        '    </fileDesc>\n'
        '  </teiHeader>\n'
        '  <text>\n'
        '    <body>\n'
        '      <div type="code" xml:lang="en">\n'
        + "\n".join(line_elements) + '\n'
        '      </div>\n'
        '    </body>\n'
        '  </text>\n'
        '  <standOff>\n'
        '    <spanGrp type="peirce-classification">\n'
        + "\n".join(spans) + '\n'
        '    </spanGrp>\n'
        '  </standOff>\n'
        '</TEI>\n'
    )
    
    # 出力を保存
    TEI_DIR.mkdir(exist_ok=True, parents=True)
    out_path = TEI_DIR / (src.stem + ".xml")
    out_path.write_text(tei_xml, encoding="utf-8")
    print(f"✓ {src.name} → {out_path.relative_to(BASE_DIR)}")

def main():
    # コマンドライン引数の処理
    global DEBUG
    args = []
    for arg in sys.argv[1:]:
        if arg == "--debug":
            DEBUG = True
        else:
            args.append(arg)
    
    # 設定の読み込み
    langmap = load_yaml_map(LANGMAP_YML, DEFAULT_LANGMAP)
    classmap = load_yaml_map(CLASSMAP_YML, DEFAULT_CLASSMAP)
    
    # 処理対象ファイルの決定
    src_paths = args
    if not src_paths:
        src_paths = sorted(RAW_DIR.glob("*"))
    
    # 各ファイルの処理
    for path_str in src_paths:
        src_path = Path(path_str)
        if not src_path.exists():
            print(f"File not found: {src_path}")
            continue
        
        key = langmap.get(src_path.suffix.lower())
        if not key:
            print(f"✗ skip (no parser): {src_path.name}")
            continue
        
        try:
            parse_and_tei(src_path, key, classmap)
        except Exception as e:
            print(f"Error processing {src_path.name}: {e}")
            if DEBUG:
                import traceback
                traceback.print_exc()

if __name__ == "__main__":
    main()
