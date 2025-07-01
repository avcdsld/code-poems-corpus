def GetAttributeNo(self, no):
        """Provides the value of the attribute with the specified
           index relative to the containing element. """
        ret = libxml2mod.xmlTextReaderGetAttributeNo(self._o, no)
        return ret