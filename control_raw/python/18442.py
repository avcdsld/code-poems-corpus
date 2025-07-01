def jsbuild_prompt():
    ''' Prompt users whether to build a new BokehJS or install an existing one.

    Returns:
        bool : True, if a new build is requested, False otherwise

    '''
    print(BOKEHJS_BUILD_PROMPT)
    mapping = {"1": True, "2": False}
    value = input("Choice? ")
    while value not in mapping:
        print("Input '%s' not understood. Valid choices: 1, 2\n" % value)
        value = input("Choice? ")
    return mapping[value]