
import json
import os

def load_classification(path):
    with open(path, "r", encoding="utf-8") as f:
        return {entry["nodeType"]: entry for entry in json.load(f)}

def annotate_ast(ast_node, classification, parent_type=None):
    if not isinstance(ast_node, dict):
        return ast_node

    node_type = ast_node.get("type")
    if node_type is None:
        return ast_node

    camel_node_type = to_camel_case(node_type)

    annotation = {}
    cls = classification.get(camel_node_type)
    if cls:
        annotation["representamen"] = cls["default"]["representamen"]
        annotation["relationToObject"] = cls["default"]["relationToObject"]
        annotation["rationale"] = cls["default"]["rationale"]

        if parent_type and "contextualConditions" in cls:
            condition_key = f"parentIs:{parent_type}"
            if condition_key in cls["contextualConditions"]:
                ctx = cls["contextualConditions"][condition_key]
                annotation.update({
                    "representamen": ctx["representamen"],
                    "relationToObject": ctx["relationToObject"],
                    "rationale": ctx["rationale"]
                })

    ast_node["_semiotic"] = annotation

    for child in ast_node.get("children", []):
        annotate_ast(child, classification, camel_node_type)

    return ast_node

def to_camel_case(s):
    parts = s.split("_")
    return parts[0] + ''.join(p.title() for p in parts[1:])

def process_file(ast_path, classification_path, output_path):
    with open(ast_path, "r", encoding="utf-8") as f:
        ast = json.load(f)
    classification = load_classification(classification_path)
    annotated = annotate_ast(ast, classification)
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(annotated, f, indent=2, ensure_ascii=False)
    print(f"[✓] Annotated AST written to {output_path}")

if __name__ == "__main__":
    process_file(
        # "corpus_processed/js/5_disfunction/static/ast.json",
        # "tools/parser/semiotic_classification.json",
        # "corpus_processed/js/5_disfunction/annotated.json"

        "corpus_processed/js/35_immediate_function/static/ast.json",
        "tools/parser/semiotic_classification.json",
        "corpus_processed/js/35_immediate_function/annotated.json"
    )
