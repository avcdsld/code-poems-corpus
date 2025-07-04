"""
言語別パーサープラグインの管理モジュール
"""

from typing import Dict, List, Any


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


from .python import Plugin as python_plugin
from .java.plugin import Plugin as java_plugin
from .js import Plugin as js_plugin
from .ruby import Plugin as ruby_plugin


def get_parser_for_language(language: str):
    """
    指定された言語に対応するパーサーを返す
    
    Args:
        language (str): 言語識別子 ('python', 'java', 'js', 'ruby', 'processing')
        
    Returns:
        Parser: 言語に対応したパーサーオブジェクト。未対応の言語の場合はNone。
    """
    plugin_classes = {
        'python': python_plugin,
        'java': java_plugin,
        'js': js_plugin,
        'ruby': ruby_plugin,
        'processing': java_plugin  # Processing uses Java parser
    }
    
    plugin_class = plugin_classes.get(language.lower())
    if plugin_class:
        return plugin_class()
