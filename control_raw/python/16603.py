def validNormalizeAttributeValue(self, doc, name, value):
        """Does the validation related extra step of the normalization
          of attribute values:  If the declared value is not CDATA,
          then the XML processor must further process the normalized
          attribute value by discarding any leading and trailing
          space (#x20) characters, and by replacing sequences of
           space (#x20) characters by single space (#x20) character. """
        if doc is None: doc__o = None
        else: doc__o = doc._o
        ret = libxml2mod.xmlValidNormalizeAttributeValue(doc__o, self._o, name, value)
        return ret