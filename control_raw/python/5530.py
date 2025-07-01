def parse_json(self, values_json):
    """Override existing hyperparameter values, parsing new values from a json object.

    Args:
      values_json: String containing a json object of name:value pairs.

    Returns:
      The `HParams` instance.

    Raises:
      KeyError: If a hyperparameter in `values_json` doesn't exist.
      ValueError: If `values_json` cannot be parsed.
    """
    values_map = json.loads(values_json)
    return self.override_from_dict(values_map)