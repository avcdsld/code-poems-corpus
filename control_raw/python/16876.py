def xpathNextParent(self, cur):
        """Traversal function for the "parent" direction The parent
          axis contains the parent of the context node, if there is
           one. """
        if cur is None: cur__o = None
        else: cur__o = cur._o
        ret = libxml2mod.xmlXPathNextParent(self._o, cur__o)
        if ret is None:raise xpathError('xmlXPathNextParent() failed')
        __tmp = xmlNode(_obj=ret)
        return __tmp