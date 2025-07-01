def validNormalizeAttributeValue(self, elem, name, value):
        """Does the validation related extra step of the normalization
          of attribute values:  If the declared value is not CDATA,
          then the XML processor must further process the normalized
          attribute value by discarding any leading and trailing
          space (#x20) characters, and by replacing sequences of
           space (#x20) characters by single space (#x20) character. """
        if elem is None: elem__o = None
        else: elem__o = elem._o
        ret = libxml2mod.xmlValidNormalizeAttributeValue(self._o, elem__o, name, value)
        return ret