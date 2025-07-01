import yaml
from pathlib import Path

def load_classification_rules(config_path="config.yml"):
    """
    Load semiotic classification rules from the YAML config file.
    """
    with open(config_path, "r", encoding="utf-8") as f:
        config = yaml.safe_load(f)
    return config.get("semiotic_classification", {})

def classify_ast(ast_node, rules, language):
    """
    Recursively traverse the AST and add classification fields.

    Args:
        ast_node (dict or list): The current AST node or list of nodes.
        rules (dict): The classification rules for all languages.
        language (str): The language of the current AST.
    
    Returns:
        The modified AST node with added 'sign_type' and 'sign_mode'.
    """
    if isinstance(ast_node, list):
        return [classify_ast(node, rules, language) for node in ast_node]

    if not isinstance(ast_node, dict):
        return ast_node

    node_type = ast_node.get("type")
    lang_rules = rules.get(language, {})

    if node_type and node_type in lang_rules:
        classification = lang_rules[node_type]
        # Insert classification right after 'type'
        items = list(ast_node.items())
        # Find the index of 'type'
        try:
            type_index = [i for i, item in enumerate(items) if item[0] == 'type'][0]
            # Insert new keys after 'type'
            items.insert(type_index + 1, ("sign_type", classification.get("sign_type")))
            items.insert(type_index + 2, ("sign_mode", classification.get("sign_mode")))
            ast_node = dict(items)
        except IndexError:
            # 'type' key not found, just append
            ast_node["sign_type"] = classification.get("sign_type")
            ast_node["sign_mode"] = classification.get("sign_mode")

    if "children" in ast_node:
        ast_node["children"] = [classify_ast(child, rules, language) for child in ast_node["children"]]

    return ast_node
