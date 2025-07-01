def _copy_with_changed_callback(self, new_callback):
        ''' Dev API used to wrap the callback with decorators. '''
        return PeriodicCallback(self._document, new_callback, self._period, self._id)