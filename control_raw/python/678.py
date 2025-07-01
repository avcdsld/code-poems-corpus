def _resetUid(self, newUid):
        """
        Changes the uid of this instance. This updates both
        the stored uid and the parent uid of params and param maps.
        This is used by persistence (loading).
        :param newUid: new uid to use, which is converted to unicode
        :return: same instance, but with the uid and Param.parent values
                 updated, including within param maps
        """
        newUid = unicode(newUid)
        self.uid = newUid
        newDefaultParamMap = dict()
        newParamMap = dict()
        for param in self.params:
            newParam = copy.copy(param)
            newParam.parent = newUid
            if param in self._defaultParamMap:
                newDefaultParamMap[newParam] = self._defaultParamMap[param]
            if param in self._paramMap:
                newParamMap[newParam] = self._paramMap[param]
            param.parent = newUid
        self._defaultParamMap = newDefaultParamMap
        self._paramMap = newParamMap
        return self