def camel_to_snake_case(camel_input):
    '''
    Converts camelCase (or CamelCase) to snake_case.
    From https://codereview.stackexchange.com/questions/185966/functions-to-convert-camelcase-strings-to-snake-case

    :param str camel_input: The camelcase or CamelCase string to convert to snake_case

    :return str
    '''
    res = camel_input[0].lower()
    for i, letter in enumerate(camel_input[1:], 1):
        if letter.isupper():
            if camel_input[i-1].islower() or (i != len(camel_input)-1 and camel_input[i+1].islower()):
                res += '_'
        res += letter.lower()
    return res