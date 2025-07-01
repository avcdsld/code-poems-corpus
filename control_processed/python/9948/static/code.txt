def path_to_url(path):
    # type: (str) -> Text
    """Convert the supplied local path to a file uri.

    :param str path: A string pointing to or representing a local path
    :return: A `file://` uri for the same location
    :rtype: str

    >>> path_to_url("/home/user/code/myrepo/myfile.zip")
    'file:///home/user/code/myrepo/myfile.zip'
    """
    from .misc import to_text, to_bytes

    if not path:
        return path
    path = to_bytes(path, encoding="utf-8")
    normalized_path = to_text(normalize_drive(os.path.abspath(path)), encoding="utf-8")
    return to_text(Path(normalized_path).as_uri(), encoding="utf-8")