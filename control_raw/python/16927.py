def _check_categorical_option_type(option_name, option_value, possible_values):
    """
    Check whether or not the requested option is one of the allowed values.
    """
    err_msg = '{0} is not a valid option for {1}. '.format(option_value, option_name)
    err_msg += ' Expected one of: '.format(possible_values)

    err_msg += ', '.join(map(str, possible_values))
    if option_value not in possible_values:
        raise ToolkitError(err_msg)