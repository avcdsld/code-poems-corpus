def _conv_name(x):
    '''
    If this XML tree has an xmlns attribute, then etree will add it
    to the beginning of the tag, like: "{http://path}tag".
    '''
    if '}' in x:
        comps = x.split('}')
        name = comps[1]
        return name
    return x