def select (features, properties):
    """ Selects properties which correspond to any of the given features.
    """
    assert is_iterable_typed(properties, basestring)
    result = []

    # add any missing angle brackets
    features = add_grist (features)

    return [p for p in properties if get_grist(p) in features]