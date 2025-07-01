def load_bookmarks(filename):
    """Load all bookmarks for a specific file from config."""
    bookmarks = _load_all_bookmarks()
    return {k: v for k, v in bookmarks.items() if v[0] == filename}