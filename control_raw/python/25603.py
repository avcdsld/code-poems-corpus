def _compare(cur_cmp, cur_struct):
    '''
    Compares two objects and return a boolean value
    when there's a match.
    '''
    if isinstance(cur_cmp, dict) and isinstance(cur_struct, dict):
        log.debug('Comparing dict to dict')
        for cmp_key, cmp_value in six.iteritems(cur_cmp):
            if cmp_key == '*':
                # matches any key from the source dictionary
                if isinstance(cmp_value, dict):
                    found = False
                    for _, cur_struct_val in six.iteritems(cur_struct):
                        found |= _compare(cmp_value, cur_struct_val)
                    return found
                else:
                    found = False
                    if isinstance(cur_struct, (list, tuple)):
                        for cur_ele in cur_struct:
                            found |= _compare(cmp_value, cur_ele)
                    elif isinstance(cur_struct, dict):
                        for _, cur_ele in six.iteritems(cur_struct):
                            found |= _compare(cmp_value, cur_ele)
                    return found
            else:
                if isinstance(cmp_value, dict):
                    if cmp_key not in cur_struct:
                        return False
                    return _compare(cmp_value, cur_struct[cmp_key])
                if isinstance(cmp_value, list):
                    found = False
                    for _, cur_struct_val in six.iteritems(cur_struct):
                        found |= _compare(cmp_value, cur_struct_val)
                    return found
                else:
                    return _compare(cmp_value, cur_struct[cmp_key])
    elif isinstance(cur_cmp, (list, tuple)) and isinstance(cur_struct, (list, tuple)):
        log.debug('Comparing list to list')
        found = False
        for cur_cmp_ele in cur_cmp:
            for cur_struct_ele in cur_struct:
                found |= _compare(cur_cmp_ele, cur_struct_ele)
        return found
    elif isinstance(cur_cmp, dict) and isinstance(cur_struct, (list, tuple)):
        log.debug('Comparing dict to list (of dicts?)')
        found = False
        for cur_struct_ele in cur_struct:
            found |= _compare(cur_cmp, cur_struct_ele)
        return found
    elif isinstance(cur_cmp, bool) and isinstance(cur_struct, bool):
        log.debug('Comparing booleans: %s ? %s', cur_cmp, cur_struct)
        return cur_cmp == cur_struct
    elif isinstance(cur_cmp, (six.string_types, six.text_type)) and \
         isinstance(cur_struct, (six.string_types, six.text_type)):
        log.debug('Comparing strings (and regex?): %s ? %s', cur_cmp, cur_struct)
        # Trying literal match
        matched = re.match(cur_cmp, cur_struct, re.I)
        if matched:
            return True
        return False
    elif isinstance(cur_cmp, (six.integer_types, float)) and \
         isinstance(cur_struct, (six.integer_types, float)):
        log.debug('Comparing numeric values: %d ? %d', cur_cmp, cur_struct)
        # numeric compare
        return cur_cmp == cur_struct
    elif isinstance(cur_struct, (six.integer_types, float)) and \
         isinstance(cur_cmp, (six.string_types, six.text_type)):
        # Comapring the numerical value agains a presumably mathematical value
        log.debug('Comparing a numeric value (%d) with a string (%s)', cur_struct, cur_cmp)
        numeric_compare = _numeric_regex.match(cur_cmp)
        # determine if the value to compare agains is a mathematical operand
        if numeric_compare:
            compare_value = numeric_compare.group(2)
            return getattr(float(cur_struct), _numeric_operand[numeric_compare.group(1)])(float(compare_value))
        return False
    return False