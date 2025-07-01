def doc_type(self, *doc_type, **kwargs):
        """
        Set the type to search through. You can supply a single value or
        multiple. Values can be strings or subclasses of ``Document``.

        You can also pass in any keyword arguments, mapping a doc_type to a
        callback that should be used instead of the Hit class.

        If no doc_type is supplied any information stored on the instance will
        be erased.

        Example:

            s = Search().doc_type('product', 'store', User, custom=my_callback)
        """
        # .doc_type() resets
        s = self._clone()
        if not doc_type and not kwargs:
            s._doc_type = []
            s._doc_type_map = {}
        else:
            s._doc_type.extend(doc_type)
            s._doc_type.extend(kwargs.keys())
            s._doc_type_map.update(kwargs)
        return s