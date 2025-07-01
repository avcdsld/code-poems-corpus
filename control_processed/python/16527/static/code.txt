def newPI(name, content):
    """Creation of a processing instruction element. Use
       xmlDocNewPI preferably to get string interning """
    ret = libxml2mod.xmlNewPI(name, content)
    if ret is None:raise treeError('xmlNewPI() failed')
    return xmlNode(_obj=ret)