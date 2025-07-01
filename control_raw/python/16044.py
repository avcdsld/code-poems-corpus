def create_with_validation (raw_properties):
    """ Creates new 'PropertySet' instances after checking
        that all properties are valid and converting implicit
        properties into gristed form.
    """
    assert is_iterable_typed(raw_properties, basestring)
    properties = [property.create_from_string(s) for s in raw_properties]
    property.validate(properties)

    return create(properties)