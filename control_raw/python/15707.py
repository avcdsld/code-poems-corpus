def subfeature (feature_name, value_string, subfeature, subvalues, attributes = []):
    """ Declares a subfeature.
        feature_name:   Root feature that is not a subfeature.
        value_string:   An optional value-string specifying which feature or
                        subfeature values this subfeature is specific to,
                        if any.
        subfeature:     The name of the subfeature being declared.
        subvalues:      The allowed values of this subfeature.
        attributes:     The attributes of the subfeature.
    """
    parent_feature = validate_feature (feature_name)

    # Add grist to the subfeature name if a value-string was supplied
    subfeature_name = __get_subfeature_name (subfeature, value_string)

    if subfeature_name in __all_features[feature_name].subfeatures:
        message = "'%s' already declared as a subfeature of '%s'" % (subfeature, feature_name)
        message += " specific to '%s'" % value_string
        raise BaseException (message)

    # First declare the subfeature as a feature in its own right
    f = feature (feature_name + '-' + subfeature_name, subvalues, attributes + ['subfeature'])
    f.set_parent(parent_feature, value_string)

    parent_feature.add_subfeature(f)

    # Now make sure the subfeature values are known.
    extend_subfeature (feature_name, value_string, subfeature, subvalues)