def process_features(features, exclude):
    """
    Parameters
    ----------
    features : list[str] | str | None, optional
        Column names of features to be transformed. If None, all columns
        are selected. If string, that column is transformed. If list of strings,
        this list of column names is selected.

    exclude : list[str] | str | None, optional
        Column names of features to be ignored in transformation. Can be string
        or list of strings. Either 'exclude' or 'features' can be passed, but
        not both.

    Returns
    -------
    (features, exclude) that are processed.

    """

    # Check types
    _raise_error_if_not_of_type(features, [NoneType, str, list], 'features')
    _raise_error_if_not_of_type(exclude, [NoneType, str, list], 'exclude')

    # Make a copy of the parameters.
    _features = _copy.copy(features)
    _exclude = _copy.copy(exclude)

    # Check of both are None or empty.
    if _features and _exclude:
        raise ValueError("The parameters 'features' and 'exclude' cannot both be set."
                " Please set one or the other.")
    if _features == [] and not _exclude:
        raise ValueError("Features cannot be an empty list.")


    # Allow a single list
    _features = [_features] if type(_features) == str else _features
    _exclude = [_exclude] if type(_exclude) == str else _exclude

    # Type check each feature/exclude
    if _features:
        for f in _features:
            _raise_error_if_not_of_type(f, str, "Feature names")
    if _exclude:
        for e in _exclude:
            _raise_error_if_not_of_type(e, str, "Excluded feature names")

    if _exclude is not None and _features is not None:
        feature_set = set(_features)
        for col_name in _exclude:
            if col_name in feature_set:
                raise ValueError("'%s' appears in both features and excluded_features." % col_name)

    return _features, _exclude