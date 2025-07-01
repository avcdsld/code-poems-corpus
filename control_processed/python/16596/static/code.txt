def setTreeDoc(self, doc):
        """update all nodes under the tree to point to the right
           document """
        if doc is None: doc__o = None
        else: doc__o = doc._o
        libxml2mod.xmlSetTreeDoc(self._o, doc__o)