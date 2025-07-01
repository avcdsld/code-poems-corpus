def parseDoc(cur):
    """parse an XML in-memory document and build a tree. """
    ret = libxml2mod.xmlParseDoc(cur)
    if ret is None:raise parserError('xmlParseDoc() failed')
    return xmlDoc(_obj=ret)