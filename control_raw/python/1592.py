def _make_flex_doc(op_name, typ):
    """
    Make the appropriate substitutions for the given operation and class-typ
    into either _flex_doc_SERIES or _flex_doc_FRAME to return the docstring
    to attach to a generated method.

    Parameters
    ----------
    op_name : str {'__add__', '__sub__', ... '__eq__', '__ne__', ...}
    typ : str {series, 'dataframe']}

    Returns
    -------
    doc : str
    """
    op_name = op_name.replace('__', '')
    op_desc = _op_descriptions[op_name]

    if op_desc['reversed']:
        equiv = 'other ' + op_desc['op'] + ' ' + typ
    else:
        equiv = typ + ' ' + op_desc['op'] + ' other'

    if typ == 'series':
        base_doc = _flex_doc_SERIES
        doc_no_examples = base_doc.format(
            desc=op_desc['desc'],
            op_name=op_name,
            equiv=equiv,
            reverse=op_desc['reverse']
        )
        if op_desc['series_examples']:
            doc = doc_no_examples + op_desc['series_examples']
        else:
            doc = doc_no_examples
    elif typ == 'dataframe':
        base_doc = _flex_doc_FRAME
        doc = base_doc.format(
            desc=op_desc['desc'],
            op_name=op_name,
            equiv=equiv,
            reverse=op_desc['reverse']
        )
    elif typ == 'panel':
        base_doc = _flex_doc_PANEL
        doc = base_doc.format(
            desc=op_desc['desc'],
            op_name=op_name,
            equiv=equiv,
            reverse=op_desc['reverse']
        )
    else:
        raise AssertionError('Invalid typ argument.')
    return doc