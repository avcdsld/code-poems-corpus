def searchNsByHref(self, doc, href):
        """Search a Ns aliasing a given URI. Recurse on the parents
          until it finds the defined namespace or return None
           otherwise. """
        if doc is None: doc__o = None
        else: doc__o = doc._o
        ret = libxml2mod.xmlSearchNsByHref(doc__o, self._o, href)
        if ret is None:raise treeError('xmlSearchNsByHref() failed')
        __tmp = xmlNs(_obj=ret)
        return __tmp