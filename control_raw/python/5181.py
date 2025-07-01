def build_from_generator(cls,
                           generator,
                           target_size,
                           max_subtoken_length=None,
                           reserved_tokens=None):
    """Builds a SubwordTextEncoder from the generated text.

    Args:
      generator: yields text.
      target_size: int, approximate vocabulary size to create.
      max_subtoken_length: Maximum length of a subtoken. If this is not set,
        then the runtime and memory use of creating the vocab is quadratic in
        the length of the longest token. If this is set, then it is instead
        O(max_subtoken_length * length of longest token).
      reserved_tokens: List of reserved tokens. The global variable
        `RESERVED_TOKENS` must be a prefix of `reserved_tokens`. If this
        argument is `None`, it will use `RESERVED_TOKENS`.

    Returns:
      SubwordTextEncoder with `vocab_size` approximately `target_size`.
    """
    token_counts = collections.defaultdict(int)
    for item in generator:
      for tok in tokenizer.encode(native_to_unicode(item)):
        token_counts[tok] += 1
    encoder = cls.build_to_target_size(
        target_size, token_counts, 1, 1e3,
        max_subtoken_length=max_subtoken_length,
        reserved_tokens=reserved_tokens)
    return encoder