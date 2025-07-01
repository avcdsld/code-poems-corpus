def _load_text(handle, split=False, encoding="utf-8"):
    """Load and decode a string."""
    string = handle.read().decode(encoding)
    return string.splitlines() if split else string