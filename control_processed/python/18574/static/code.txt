def _internal_set(self, obj, value, hint=None, setter=None):
        ''' Internal implementation to set property values, that is used
        by __set__, set_from_json, etc.

        Delegate to the |Property| instance to prepare the value appropriately,
        then `set.

        Args:
            obj (HasProps)
                The object the property is being set on.

            old (obj) :
                The previous value of the property to compare

            hint (event hint or None, optional)
                An optional update event hint, e.g. ``ColumnStreamedEvent``
                (default: None)

                Update event hints are usually used at times when better
                update performance can be obtained by special-casing in
                some way (e.g. streaming or patching column data sources)

            setter (ClientSession or ServerSession or None, optional) :
                This is used to prevent "boomerang" updates to Bokeh apps.
                (default: None)

                In the context of a Bokeh server application, incoming updates
                to properties will be annotated with the session that is
                doing the updating. This value is propagated through any
                subsequent change notifications that the update triggers.
                The session can compare the event setter to itself, and
                suppress any updates that originate from itself.

        Returns:
            None

        '''
        value = self.property.prepare_value(obj, self.name, value)

        old = self.__get__(obj, obj.__class__)
        self._real_set(obj, old, value, hint=hint, setter=setter)