def _summarize_accessible_fields(field_descriptions, width=40,
                                 section_title='Accessible fields'):
    """
    Create a summary string for the accessible fields in a model. Unlike
    `_toolkit_repr_print`, this function does not look up the values of the
    fields, it just formats the names and descriptions.

    Parameters
    ----------
    field_descriptions : dict{str: str}
        Name of each field and its description, in a dictionary. Keys and
        values should be strings.

    width : int, optional
        Width of the names. This is usually determined and passed by the
        calling `__repr__` method.

    section_title : str, optional
        Name of the accessible fields section in the summary string.

    Returns
    -------
    out : str
    """
    key_str = "{:<{}}: {}"

    items = []
    items.append(section_title)
    items.append("-" * len(section_title))

    for field_name, field_desc in field_descriptions.items():
        items.append(key_str.format(field_name, width, field_desc))

    return "\n".join(items)