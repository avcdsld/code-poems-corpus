def _find_module(mod_name):
    """
    Iterate over each part instead of calling imp.find_module directly.
    This function is able to find submodules (e.g. sickit.tree)
    """
    path = None
    for part in mod_name.split('.'):
        if path is not None:
            path = [path]
        file, path, description = imp.find_module(part, path)
        if file is not None:
            file.close()
    return path, description