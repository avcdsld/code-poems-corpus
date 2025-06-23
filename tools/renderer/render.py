import json
import html


def load_ast_with_annotations(ast_path):
    with open(ast_path, "r", encoding="utf-8") as f:
        return json.load(f)


def load_code(code_path):
    with open(code_path, "r", encoding="utf-8") as f:
        return f.read()


def build_char_indexed_text(code_text):
    lines = code_text.splitlines(keepends=True)
    char_index = []
    for i, line in enumerate(lines):
        for j, ch in enumerate(line):
            char_index.append(((i, j), ch))
    return char_index


def flat_nodes(ast, results=None):
    if results is None:
        results = []
    if isinstance(ast, dict):
        if "start" in ast and "end" in ast:
            results.append(ast)
        for child in ast.get("children", []):
            flat_nodes(child, results)
    return results


def to_flat_index(position, char_index):
    for i, (pos, _) in enumerate(char_index):
        if pos == tuple(position):
            return i
    return -1


def wrap_code_with_spans(code_text, ast):
    char_index = build_char_indexed_text(code_text)
    text = [ch for _, ch in char_index]

    flat = flat_nodes(ast)
    flat.sort(key=lambda n: (n["start"], -n["end"][0], -n["end"][1]))  # outer first

    inserts = []
    for node in flat:
        start = to_flat_index(node["start"], char_index)
        end = to_flat_index(node["end"], char_index)
        if start == -1 or end == -1:
            continue

        sem = node.get("_semiotic")
        if not sem:
            continue

        cls = sem.get("relationToObject", "unknown")
        tip = html.escape(f"{sem.get('representamen', '')} / {sem.get('relationToObject', '')}\n{sem.get('rationale', '')}")

        inserts.append((start, f'<span class="token {cls}" title="{tip}">'))
        inserts.append((end, "</span>"))

    for index, tag in sorted(inserts, reverse=True):
        text.insert(index, tag)

    return "".join(text)


def render_to_html(code_text, annotated_ast):
    highlighted = wrap_code_with_spans(code_text, annotated_ast)
    return f"""
<!DOCTYPE html>
<html lang=\"en\">
<head>
  <meta charset=\"UTF-8\">
  <title>Annotated CodePoetry</title>
  <style>
    body {{ font-family: monospace; background: #f9f9f9; padding: 2rem; }}
    .token {{ padding: 0.1em 0.2em; border-radius: 0.2em; cursor: help; }}
    .symbol {{ background-color: #d0eaff; }}
    .index {{ background-color: #ffe2e2; }}
    .icon {{ background-color: #e6ffe2; }}
  </style>
</head>
<body>
<pre>{highlighted}</pre>
</body>
</html>
"""


def export_annotated_html(code_path, ast_path, output_path):
    code = load_code(code_path)
    ast = load_ast_with_annotations(ast_path)
    html_out = render_to_html(code, ast)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(html_out)
    print(f"[✓] HTML written to {output_path}")

if __name__ == "__main__":
    export_annotated_html(
        # "corpus_raw/js/5_disfunction.js",
        # "corpus_processed/js/5_disfunction/annotated.json",
        # "corpus_processed/js/5_disfunction/output.html"

        "corpus_raw/js/35_immediate_function.js",
        "corpus_processed/js/35_immediate_function/annotated.json",
        "corpus_processed/js/35_immediate_function/output.html"
    )
