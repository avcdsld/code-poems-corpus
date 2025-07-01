def Preserve(self):
        """This tells the XML Reader to preserve the current node. The
          caller must also use xmlTextReaderCurrentDoc() to keep an
           handle on the resulting document once parsing has finished """
        ret = libxml2mod.xmlTextReaderPreserve(self._o)
        if ret is None:raise treeError('xmlTextReaderPreserve() failed')
        __tmp = xmlNode(_obj=ret)
        return __tmp