def removeRef(self, doc):
        """Remove the given attribute from the Ref table maintained
           internally. """
        if doc is None: doc__o = None
        else: doc__o = doc._o
        ret = libxml2mod.xmlRemoveRef(doc__o, self._o)
        return ret