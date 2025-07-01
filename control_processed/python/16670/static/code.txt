def newDocNodeEatName(self, ns, name, content):
        """Creation of a new node element within a document. @ns and
          @content are optional (None). NOTE: @content is supposed to
          be a piece of XML CDATA, so it allow entities references,
          but XML special chars need to be escaped first by using
          xmlEncodeEntitiesReentrant(). Use xmlNewDocRawNode() if you
           don't need entities support. """
        if ns is None: ns__o = None
        else: ns__o = ns._o
        ret = libxml2mod.xmlNewDocNodeEatName(self._o, ns__o, name, content)
        if ret is None:raise treeError('xmlNewDocNodeEatName() failed')
        __tmp = xmlNode(_obj=ret)
        return __tmp