def ToJsonString(self):
    """Converts FieldMask to string according to proto3 JSON spec."""
    camelcase_paths = []
    for path in self.paths:
      camelcase_paths.append(_SnakeCaseToCamelCase(path))
    return ','.join(camelcase_paths)