def _get_interpretation_description_and_output_type(interpretation, dtype):
    """
    Returns the description and output type for a given interpretation.
    """

    type_string = dtype.__name__
    name = "%s__%s" % (interpretation, type_string)

    if not hasattr(_interpretations_class, name):
        raise ValueError("No transform available for type '%s' with interpretation '%s'."
                         % (type_string, interpretation))

    # Need unbound method to get the attributes
    func = getattr(_interpretations_class, name)

    return func.description, func.output_type