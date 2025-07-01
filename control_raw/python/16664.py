def intSubset(self):
        """Get the internal subset of a document """
        ret = libxml2mod.xmlGetIntSubset(self._o)
        if ret is None:raise treeError('xmlGetIntSubset() failed')
        __tmp = xmlDtd(_obj=ret)
        return __tmp