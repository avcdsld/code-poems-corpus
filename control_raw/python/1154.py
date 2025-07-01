def format_object_summary(obj, formatter, is_justify=True, name=None,
                          indent_for_name=True):
    """
    Return the formatted obj as a unicode string

    Parameters
    ----------
    obj : object
        must be iterable and support __getitem__
    formatter : callable
        string formatter for an element
    is_justify : boolean
        should justify the display
    name : name, optional
        defaults to the class name of the obj
    indent_for_name : bool, default True
        Whether subsequent lines should be be indented to
        align with the name.

    Returns
    -------
    summary string

    """
    from pandas.io.formats.console import get_console_size
    from pandas.io.formats.format import _get_adjustment

    display_width, _ = get_console_size()
    if display_width is None:
        display_width = get_option('display.width') or 80
    if name is None:
        name = obj.__class__.__name__

    if indent_for_name:
        name_len = len(name)
        space1 = "\n%s" % (' ' * (name_len + 1))
        space2 = "\n%s" % (' ' * (name_len + 2))
    else:
        space1 = "\n"
        space2 = "\n "  # space for the opening '['

    n = len(obj)
    sep = ','
    max_seq_items = get_option('display.max_seq_items') or n

    # are we a truncated display
    is_truncated = n > max_seq_items

    # adj can optionally handle unicode eastern asian width
    adj = _get_adjustment()

    def _extend_line(s, line, value, display_width, next_line_prefix):

        if (adj.len(line.rstrip()) + adj.len(value.rstrip()) >=
                display_width):
            s += line.rstrip()
            line = next_line_prefix
        line += value
        return s, line

    def best_len(values):
        if values:
            return max(adj.len(x) for x in values)
        else:
            return 0

    close = ', '

    if n == 0:
        summary = '[]{}'.format(close)
    elif n == 1:
        first = formatter(obj[0])
        summary = '[{}]{}'.format(first, close)
    elif n == 2:
        first = formatter(obj[0])
        last = formatter(obj[-1])
        summary = '[{}, {}]{}'.format(first, last, close)
    else:

        if n > max_seq_items:
            n = min(max_seq_items // 2, 10)
            head = [formatter(x) for x in obj[:n]]
            tail = [formatter(x) for x in obj[-n:]]
        else:
            head = []
            tail = [formatter(x) for x in obj]

        # adjust all values to max length if needed
        if is_justify:

            # however, if we are not truncated and we are only a single
            # line, then don't justify
            if (is_truncated or
                    not (len(', '.join(head)) < display_width and
                         len(', '.join(tail)) < display_width)):
                max_len = max(best_len(head), best_len(tail))
                head = [x.rjust(max_len) for x in head]
                tail = [x.rjust(max_len) for x in tail]

        summary = ""
        line = space2

        for i in range(len(head)):
            word = head[i] + sep + ' '
            summary, line = _extend_line(summary, line, word,
                                         display_width, space2)

        if is_truncated:
            # remove trailing space of last line
            summary += line.rstrip() + space2 + '...'
            line = space2

        for i in range(len(tail) - 1):
            word = tail[i] + sep + ' '
            summary, line = _extend_line(summary, line, word,
                                         display_width, space2)

        # last value: no sep added + 1 space of width used for trailing ','
        summary, line = _extend_line(summary, line, tail[-1],
                                     display_width - 2, space2)
        summary += line

        # right now close is either '' or ', '
        # Now we want to include the ']', but not the maybe space.
        close = ']' + close.rstrip(' ')
        summary += close

        if len(summary) > (display_width):
            summary += space1
        else:  # one row
            summary += ' '

        # remove initial space
        summary = '[' + summary[len(space2):]

    return summary