def _validate_forbidden(self, forbidden_values, field, value):
        """ {'type': 'list'} """
        if isinstance(value, _str_type):
            if value in forbidden_values:
                self._error(field, errors.FORBIDDEN_VALUE, value)
        elif isinstance(value, Sequence):
            forbidden = set(value) & set(forbidden_values)
            if forbidden:
                self._error(field, errors.FORBIDDEN_VALUES, list(forbidden))
        elif isinstance(value, int):
            if value in forbidden_values:
                self._error(field, errors.FORBIDDEN_VALUE, value)