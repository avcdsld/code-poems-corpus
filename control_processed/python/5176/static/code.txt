def _token_to_subtoken_ids(self, token):
    """Converts token to a list of subtoken ids.

    Args:
      token: a string.
    Returns:
      a list of integers in the range [0, vocab_size)
    """
    cache_location = hash(token) % self._cache_size
    cache_key, cache_value = self._cache[cache_location]
    if cache_key == token:
      return cache_value
    ret = self._escaped_token_to_subtoken_ids(
        _escape_token(token, self._alphabet))
    self._cache[cache_location] = (token, ret)
    return ret