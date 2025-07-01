def xpathNextAncestor(self, cur):
        """Traversal function for the "ancestor" direction the
          ancestor axis contains the ancestors of the context node;
          the ancestors of the context node consist of the parent of
          context node and the parent's parent and so on; the nodes
          are ordered in reverse document order; thus the parent is
          the first node on the axis, and the parent's parent is the
           second node on the axis """
        if cur is None: cur__o = None
        else: cur__o = cur._o
        ret = libxml2mod.xmlXPathNextAncestor(self._o, cur__o)
        if ret is None:raise xpathError('xmlXPathNextAncestor() failed')
        __tmp = xmlNode(_obj=ret)
        return __tmp