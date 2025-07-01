def _StructMessageToJsonObject(self, message):
    """Converts Struct message according to Proto3 JSON Specification."""
    fields = message.fields
    ret = {}
    for key in fields:
      ret[key] = self._ValueMessageToJsonObject(fields[key])
    return ret