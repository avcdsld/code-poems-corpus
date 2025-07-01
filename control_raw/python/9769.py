def validated(self, *args, **kwargs):
        """ Wrapper around :meth:`~cerberus.Validator.validate` that returns
            the normalized and validated document or :obj:`None` if validation
            failed. """
        always_return_document = kwargs.pop('always_return_document', False)
        self.validate(*args, **kwargs)
        if self._errors and not always_return_document:
            return None
        else:
            return self.document