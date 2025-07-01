def dump(new_data):
    '''
    Replace the entire datastore with a passed data structure

    CLI Example:

    .. code-block:: bash

        salt '*' data.dump '{'eggs': 'spam'}'
    '''
    if not isinstance(new_data, dict):
        if isinstance(ast.literal_eval(new_data), dict):
            new_data = ast.literal_eval(new_data)
        else:
            return False

    try:
        datastore_path = os.path.join(__opts__['cachedir'], 'datastore')
        with salt.utils.files.fopen(datastore_path, 'w+b') as fn_:
            serial = salt.payload.Serial(__opts__)
            serial.dump(new_data, fn_)

        return True

    except (IOError, OSError, NameError):
        return False