def _get_diff_text(old, new):
    '''
    Returns the diff of two text blobs.
    '''
    diff = difflib.unified_diff(old.splitlines(1),
                                new.splitlines(1))
    return ''.join([x.replace('\r', '') for x in diff])