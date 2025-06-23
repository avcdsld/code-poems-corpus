import json
import glob
from collections import defaultdict

file_paths = glob.glob("corpus_processed/js/*/static/ast.json")

all_types = set()
parent_child_relations = defaultdict(set)  # parent -> children
child_parent_relations = defaultdict(set)  # child -> parents

def traverse_ast(node, parent_type=None):
    if not isinstance(node, dict):
        return
    node_type = node.get("type")
    if node_type:
        all_types.add(node_type)
        if parent_type:
            child_parent_relations[node_type].add(parent_type)
            parent_child_relations[parent_type].add(node_type)
    for child in node.get("children", []):
        traverse_ast(child, node_type)

for path in file_paths:
    with open(path, "r", encoding="utf-8") as f:
        ast = json.load(f)
        traverse_ast(ast)

print("type\tparent_type\tchild_type")

for child_type, parent_types in sorted(child_parent_relations.items()):
    for parent in sorted(parent_types):
        print(f"{child_type}\t{parent}\t")

for parent_type, child_types in sorted(parent_child_relations.items()):
    for child in sorted(child_types):
        print(f"{parent_type}\t\t{child}")
