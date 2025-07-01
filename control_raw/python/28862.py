def tree(path, load_path=None):
    '''
    Returns recursively the complete tree of a node

    CLI Example:

    .. code-block:: bash

        salt '*' augeas.tree /files/etc/

    path
        The base of the recursive listing

    .. versionadded:: 2016.3.0

    load_path
        A colon-spearated list of directories that modules should be searched
        in. This is in addition to the standard load path and the directories
        in AUGEAS_LENS_LIB.
    '''
    load_path = _check_load_paths(load_path)

    aug = _Augeas(loadpath=load_path)

    path = path.rstrip('/') + '/'
    match_path = path
    return dict([i for i in _recurmatch(match_path, aug)])