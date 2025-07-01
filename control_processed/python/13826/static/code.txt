def to_query_parameters_dict(parameters):
    """Converts a dictionary of parameter values into query parameters.

    :type parameters: Mapping[str, Any]
    :param parameters: Dictionary of query parameter values.

    :rtype: List[google.cloud.bigquery.query._AbstractQueryParameter]
    :returns: A list of named query parameters.
    """
    return [
        scalar_to_query_parameter(value, name=name)
        for name, value in six.iteritems(parameters)
    ]