def htmlCreateMemoryParserCtxt(buffer, size):
    """Create a parser context for an HTML in-memory document. """
    ret = libxml2mod.htmlCreateMemoryParserCtxt(buffer, size)
    if ret is None:raise parserError('htmlCreateMemoryParserCtxt() failed')
    return parserCtxt(_obj=ret)