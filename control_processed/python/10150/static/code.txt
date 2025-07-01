def poplistitem(self, last=True):
        """
        Pop and return a key:valuelist item comprised of a key and that key's
        list of values. If <last> is False, a key:valuelist item comprised of
        keys()[0] and its list of values is popped and returned. If <last> is
        True, a key:valuelist item comprised of keys()[-1] and its list of
        values is popped and returned.

        Example:
          omd = omdict([(1,1), (1,11), (1,111), (2,2), (3,3)])
          omd.poplistitem(last=True) == (3,[3])
          omd.poplistitem(last=False) == (1,[1,11,111])

        Params:
          last: Boolean whether to pop the first or last key and its associated
            list of values.
        Raises: KeyError if the dictionary is empty.
        Returns: A two-tuple comprised of the first or last key and its
          associated list of values.
        """
        if not self._items:
            s = 'poplistitem(): %s is empty' % self.__class__.__name__
            raise KeyError(s)

        key = self.keys()[-1 if last else 0]
        return key, self.poplist(key)