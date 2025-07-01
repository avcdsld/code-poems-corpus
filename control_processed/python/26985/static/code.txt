def list_path_traversal(path):
    '''
    Returns a full list of directories leading up to, and including, a path.

    So list_path_traversal('/path/to/salt') would return:
        ['/', '/path', '/path/to', '/path/to/salt']
    in that order.

    This routine has been tested on Windows systems as well.
    list_path_traversal('c:\\path\\to\\salt') on Windows would return:
        ['c:\\', 'c:\\path', 'c:\\path\\to', 'c:\\path\\to\\salt']
    '''
    out = [path]
    (head, tail) = os.path.split(path)
    if tail == '':
        # paths with trailing separators will return an empty string
        out = [head]
        (head, tail) = os.path.split(head)
    while head != out[0]:
        # loop until head is the same two consecutive times
        out.insert(0, head)
        (head, tail) = os.path.split(head)
    return out