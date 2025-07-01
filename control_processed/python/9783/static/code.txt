def _validate_keyschema(self, schema, field, value):
        """ {'type': ['dict', 'string'], 'validator': 'bulk_schema',
            'forbidden': ['rename', 'rename_handler']} """
        if isinstance(value, Mapping):
            validator = self._get_child_validator(
                document_crumb=field,
                schema_crumb=(field, 'keyschema'),
                schema=dict(((k, schema) for k in value.keys())))
            if not validator(dict(((k, k) for k in value.keys())),
                             normalize=False):
                self._drop_nodes_from_errorpaths(validator._errors,
                                                 [], [2, 4])
                self._error(field, errors.KEYSCHEMA, validator._errors)