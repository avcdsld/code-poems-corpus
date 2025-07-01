def NewFd(self, fd, URL, encoding, options):
        """Setup an xmltextReader to parse an XML from a file
          descriptor. NOTE that the file descriptor will not be
          closed when the reader is closed or reset. The parsing
          flags @options are a combination of xmlParserOption. This
           reuses the existing @reader xmlTextReader. """
        ret = libxml2mod.xmlReaderNewFd(self._o, fd, URL, encoding, options)
        return ret