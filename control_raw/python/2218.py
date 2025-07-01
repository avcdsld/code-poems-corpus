def get_api_items(api_doc_fd):
    """
    Yield information about all public API items.

    Parse api.rst file from the documentation, and extract all the functions,
    methods, classes, attributes... This should include all pandas public API.

    Parameters
    ----------
    api_doc_fd : file descriptor
        A file descriptor of the API documentation page, containing the table
        of contents with all the public API.

    Yields
    ------
    name : str
        The name of the object (e.g. 'pandas.Series.str.upper).
    func : function
        The object itself. In most cases this will be a function or method,
        but it can also be classes, properties, cython objects...
    section : str
        The name of the section in the API page where the object item is
        located.
    subsection : str
        The name of the subsection in the API page where the object item is
        located.
    """
    current_module = 'pandas'
    previous_line = current_section = current_subsection = ''
    position = None
    for line in api_doc_fd:
        line = line.strip()
        if len(line) == len(previous_line):
            if set(line) == set('-'):
                current_section = previous_line
                continue
            if set(line) == set('~'):
                current_subsection = previous_line
                continue

        if line.startswith('.. currentmodule::'):
            current_module = line.replace('.. currentmodule::', '').strip()
            continue

        if line == '.. autosummary::':
            position = 'autosummary'
            continue

        if position == 'autosummary':
            if line == '':
                position = 'items'
                continue

        if position == 'items':
            if line == '':
                position = None
                continue
            item = line.strip()
            func = importlib.import_module(current_module)
            for part in item.split('.'):
                func = getattr(func, part)

            yield ('.'.join([current_module, item]), func,
                   current_section, current_subsection)

        previous_line = line