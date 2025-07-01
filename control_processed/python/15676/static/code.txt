def __convert_string_list(node):
    """Converts a StringListProperty node to JSON format."""
    converted = __convert_node(node)

    # Determine flags for the string list
    flags = vsflags(VSFlags.UserValue)

    # Check for a separator to determine if it is semicolon appendable
    # If not present assume the value should be ;
    separator = __get_attribute(node, 'Separator', default_value=';')

    if separator == ';':
        flags = vsflags(flags, VSFlags.SemicolonAppendable)

    converted['flags'] = flags

    return __check_for_flag(converted)