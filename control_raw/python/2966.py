def find_comment_markers(cellsource):
    """Look through the cell source for comments which affect nbval's behaviour

    Yield an iterable of ``(MARKER_TYPE, True)``.
    """
    found = {}
    for line in cellsource.splitlines():
        line = line.strip()
        if line.startswith('#'):
            # print("Found comment in '{}'".format(line))
            comment = line.lstrip('#').strip()
            if comment in comment_markers:
                # print("Found marker {}".format(comment))
                marker = comment_markers[comment]
                if not isinstance(marker, tuple):
                    # If not an explicit tuple ('option', True/False),
                    # imply ('option', True)
                    marker = (marker, True)
                marker_type = marker[0]
                if marker_type in found:
                    warnings.warn(
                        "Conflicting comment markers found, using the latest: "
                        " %s VS %s" %
                        (found[marker_type], comment))
                found[marker_type] = comment
                yield marker