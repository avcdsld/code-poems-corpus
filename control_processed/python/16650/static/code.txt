def parameterEntity(self, name):
        """Do an entity lookup in the internal and external subsets and """
        ret = libxml2mod.xmlGetParameterEntity(self._o, name)
        if ret is None:raise treeError('xmlGetParameterEntity() failed')
        __tmp = xmlEntity(_obj=ret)
        return __tmp