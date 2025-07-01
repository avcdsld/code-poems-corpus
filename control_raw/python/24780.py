def _move_before(xpath, target):
    '''
    Moves an xpath to the bottom of its section.

    '''
    query = {'type': 'config',
             'action': 'move',
             'xpath': xpath,
             'where': 'before',
             'dst': target}

    response = __proxy__['panos.call'](query)

    return _validate_response(response)