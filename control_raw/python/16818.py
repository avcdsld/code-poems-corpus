def MoveToAttributeNo(self, no):
        """Moves the position of the current instance to the attribute
          with the specified index relative to the containing element. """
        ret = libxml2mod.xmlTextReaderMoveToAttributeNo(self._o, no)
        return ret