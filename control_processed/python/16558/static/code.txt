def addNextSibling(self, elem):
        """Add a new node @elem as the next sibling of @cur If the new
          node was already inserted in a document it is first
          unlinked from its existing context. As a result of text
          merging @elem may be freed. If the new node is ATTRIBUTE,
          it is added into properties instead of children. If there
           is an attribute with equal name, it is first destroyed. """
        if elem is None: elem__o = None
        else: elem__o = elem._o
        ret = libxml2mod.xmlAddNextSibling(self._o, elem__o)
        if ret is None:raise treeError('xmlAddNextSibling() failed')
        __tmp = xmlNode(_obj=ret)
        return __tmp