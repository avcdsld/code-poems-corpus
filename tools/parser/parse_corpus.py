#!/usr/bin/env python3
"""parse_corpus.py

Static‑analysis front‑end for *code‑poems‑corpus*.

▸ Traverses `corpus_raw/` and, for every source file recognised in
  `config.yml`, produces Tree‑sitter token and AST dumps under
  `corpus_processed/<lang>/<work‑id>/static/`.
▸ Designed to be **language‑pluggable**: each language implements a
  lightweight `ParserPlugin` declared in `tools/parser/plugins/<lang>.py`.

Running example
---------------
$ python tools/parser/parse_corpus.py --lang python
$ python tools/parser/parse_corpus.py  # all languages

Dependencies
------------
* tree_sitter>=0.23.2
* PyYAML>=6.0  (for config.yml)

"""
from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path
from importlib import import_module
from typing import Dict, List, Tuple

import yaml  # type: ignore

RAW_ROOT = Path("corpus_raw")
PROC_ROOT = Path("corpus_processed")
CFG_PATH = Path("config.yml")
PLUG_DIR = Path(__file__).parent / "plugins"


class ParserPlugin:
    """Abstract base for language plugins.

    Each plugin **must** expose a subclass named `Plugin` implementing
    `tokenise()` and `parse_ast()`.
    """

    #: file extensions that trigger this plugin (e.g. ['.py'] )
    extensions: List[str] = []

    def tokenise(self, code: str) -> List[Dict]:
        raise NotImplementedError

    def parse_ast(self, code: str) -> Dict:
        raise NotImplementedError


# ---------------------------------------------------------------------------
# Utility helpers
# ---------------------------------------------------------------------------


def load_config() -> Dict:
    if not CFG_PATH.exists():
        sys.exit("config.yml not found – run in repo root or create the file.")
    with CFG_PATH.open() as fp:
        return yaml.safe_load(fp)


def discover_plugins(cfg: Dict, lang_filter: List[str] | None) -> Dict[str, ParserPlugin]:
    plugins: Dict[str, ParserPlugin] = {}
    for lang, meta in cfg.get("languages", {}).items():
        print(f"[INFO] loading language '{lang}'")

        if lang_filter and lang not in lang_filter:
            continue
        try:
            module = import_module(f".{lang}", package="tools.parser.plugins")
            plugin_cls = getattr(module, "Plugin")
            plugin: ParserPlugin = plugin_cls()
            plugins[lang] = plugin
        except Exception as exc:  # pylint: disable=broad-except
            print(f"[WARN] skipping language '{lang}': {exc}")
    return plugins


def enumerate_source_files(cfg: Dict, lang: str, plugin: ParserPlugin) -> List[Tuple[Path, str]]:
    # (path, work_id)
    src: List[Tuple[Path, str]] = []
    for ext in plugin.extensions:
        for file in RAW_ROOT.glob(f"{lang}/*{ext}"):
            work_id = file.stem  # retains leading number + title
            src.append((file, work_id))
    return src


def ensure_dir(path: Path):
    path.mkdir(parents=True, exist_ok=True)


# ---------------------------------------------------------------------------
# Main pipeline per file
# ---------------------------------------------------------------------------

def process_file(lang: str, work_id: str, path: Path, plugin: ParserPlugin):
    print(f"[INFO] {lang}/{work_id}: parsing …", end=" ")
    code = path.read_text(encoding="utf-8", errors="ignore")

    # 1) tokens ----------------------------------------------------------------
    tokens = plugin.tokenise(code)

    # 2) AST -------------------------------------------------------------------
    ast = plugin.parse_ast(code)

    # 3) write -----------------------------------------------------------------
    out_dir = PROC_ROOT / lang / work_id / "static"
    ensure_dir(out_dir)

    (out_dir / "tokens.jsonl").write_text("\n".join(json.dumps(t) for t in tokens), "utf-8")
    (out_dir / "ast.json").write_text(json.dumps(ast, indent=2), "utf-8")

    print("✔")


# ---------------------------------------------------------------------------
# CLI entry‑point
# ---------------------------------------------------------------------------

def main():
    ap = argparse.ArgumentParser(description="Generate Tree‑sitter dumps for code‑poems corpus.")
    ap.add_argument("--lang", nargs="*", help="limit to given language(s)")
    args = ap.parse_args()

    cfg = load_config()
    plugins = discover_plugins(cfg, args.lang)

    if not plugins:
        sys.exit("[ERR] no languages found – check --lang or config.yml")

    for lang, plugin in plugins.items():
        files = enumerate_source_files(cfg, lang, plugin)
        if not files:
            print(f"[WARN] no source files for '{lang}'")
            continue
        for path, work_id in files:
            process_file(lang, work_id, path, plugin)

    print("[DONE] static parsing stage complete.")


if __name__ == "__main__":
    main()
