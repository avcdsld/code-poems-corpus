def _convert_md_table_to_rst(table):
    """Convert a markdown table to rst format"""
    if len(table) < 3:
        return ''
    out = '```eval_rst\n.. list-table::\n   :header-rows: 1\n\n'
    for i,l in enumerate(table):
        cols = l.split('|')[1:-1]
        if i == 0:
            ncol = len(cols)
        else:
            if len(cols) != ncol:
                return ''
        if i == 1:
            for c in cols:
                if len(c) is not 0 and '---' not in c:
                    return ''
        else:
            for j,c in enumerate(cols):
                out += '   * - ' if j == 0 else '     - '
                out += pypandoc.convert_text(
                    c, 'rst', format='md').replace('\n', ' ').replace('\r', '') + '\n'
    out += '```\n'
    return out