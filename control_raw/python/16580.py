def newProp(self, name, value):
        """Create a new property carried by a node. """
        ret = libxml2mod.xmlNewProp(self._o, name, value)
        if ret is None:raise treeError('xmlNewProp() failed')
        __tmp = xmlAttr(_obj=ret)
        return __tmp