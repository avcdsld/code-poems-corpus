def _build_dataframe(time_series_iterable, label=None, labels=None):  # pragma: NO COVER
    """Build a :mod:`pandas` dataframe out of time series.

    :type time_series_iterable:
        iterable over :class:`~google.cloud.monitoring_v3.types.TimeSeries`
    :param time_series_iterable:
        An iterable (e.g., a query object) yielding time series.

    :type label: str
    :param label:
        (Optional) The label name to use for the dataframe header. This can be
        the name of a resource label or metric label (e.g.,
        ``"instance_name"``), or the string ``"resource_type"``.

    :type labels: list of strings, or None
    :param labels:
        A list or tuple of label names to use for the dataframe header.
        If more than one label name is provided, the resulting dataframe
        will have a multi-level column header.

        Specifying neither ``label`` or ``labels`` results in a dataframe
        with a multi-level column header including the resource type and
        all available resource and metric labels.

        Specifying both ``label`` and ``labels`` is an error.

    :rtype: :class:`pandas.DataFrame`
    :returns: A dataframe where each column represents one time series.

    :raises: :exc:`RuntimeError` if `pandas` is not installed.
    """
    if pandas is None:
        raise RuntimeError("This method requires `pandas` to be installed.")

    if label is not None:
        if labels:
            raise ValueError("Cannot specify both `label` and `labels`.")
        labels = (label,)

    columns = []
    headers = []
    for time_series in time_series_iterable:
        pandas_series = pandas.Series(
            data=[_extract_value(point.value) for point in time_series.points],
            index=[
                point.interval.end_time.ToNanoseconds() for point in time_series.points
            ],
        )
        columns.append(pandas_series)
        headers.append(_extract_header(time_series))

    # Implement a smart default of using all available labels.
    if labels is None:
        resource_labels = set(
            itertools.chain.from_iterable(header.resource.labels for header in headers)
        )
        metric_labels = set(
            itertools.chain.from_iterable(header.metric.labels for header in headers)
        )
        labels = (
            ["resource_type"]
            + _sorted_resource_labels(resource_labels)
            + sorted(metric_labels)
        )

    # Assemble the columns into a DataFrame.
    dataframe = pandas.DataFrame.from_records(columns).T

    # Convert the timestamp strings into a DatetimeIndex.
    dataframe.index = pandas.to_datetime(dataframe.index)

    # Build a multi-level stack of column headers. Some labels may
    # be undefined for some time series.
    levels = []
    for key in labels:
        level = [_extract_labels(header).get(key, "") for header in headers]
        levels.append(level)

    # Build a column Index or MultiIndex. Do not include level names
    # in the column header if the user requested a single-level header
    # by specifying "label".
    dataframe.columns = pandas.MultiIndex.from_arrays(
        levels, names=labels if not label else None
    )

    # Sort the rows just in case (since the API doesn't guarantee the
    # ordering), and sort the columns lexicographically.
    return dataframe.sort_index(axis=0).sort_index(axis=1)