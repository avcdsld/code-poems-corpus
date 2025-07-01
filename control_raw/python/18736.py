def remove_on_change(self, attr, *callbacks):
        ''' Remove a callback from this object '''
        if len(callbacks) == 0:
            raise ValueError("remove_on_change takes an attribute name and one or more callbacks, got only one parameter")
        _callbacks = self._callbacks.setdefault(attr, [])
        for callback in callbacks:
            _callbacks.remove(callback)