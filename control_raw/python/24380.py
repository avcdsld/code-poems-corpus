def _object_reducer(o, names=('id', 'name', 'path', 'httpMethod',
                              'statusCode', 'Created', 'Deleted',
                              'Updated', 'Flushed', 'Associated', 'Disassociated')):
    '''
    Helper function to reduce the amount of information that will be kept in the change log
    for API GW related return values
    '''
    result = {}
    if isinstance(o, dict):
        for k, v in six.iteritems(o):
            if isinstance(v, dict):
                reduced = v if k == 'variables' else _object_reducer(v, names)
                if reduced or _name_matches(k, names):
                    result[k] = reduced
            elif isinstance(v, list):
                newlist = []
                for val in v:
                    reduced = _object_reducer(val, names)
                    if reduced or _name_matches(k, names):
                        newlist.append(reduced)
                if newlist:
                    result[k] = newlist
            else:
                if _name_matches(k, names):
                    result[k] = v
    return result