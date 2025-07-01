def validateDocumentFinal(self, doc):
        """Does the final step for the document validation once all
          the incremental validation steps have been completed
          basically it does the following checks described by the XML
          Rec  Check all the IDREF/IDREFS attributes definition for
           validity """
        if doc is None: doc__o = None
        else: doc__o = doc._o
        ret = libxml2mod.xmlValidateDocumentFinal(self._o, doc__o)
        return ret