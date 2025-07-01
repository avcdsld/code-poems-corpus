def collection_set_options(collection_name, options, **kwargs):
    '''
    Change collection options

    Additional parameters (kwargs) may be passed, they will be proxied to http.query

    Note that not every parameter can be changed after collection creation

    CLI Example:

    .. code-block:: bash

        salt '*' solrcloud.collection_set_options collection_name options={"replicationFactor":4}
    '''

    for option in list(options.keys()):
        if option not in CREATION_ONLY_OPTION:
            raise ValueError('Option '+option+' can\'t be modified after collection creation.')

    options_string = _validate_collection_options(options)

    _query('admin/collections?action=MODIFYCOLLECTION&wt=json&collection='+collection_name+options_string, **kwargs)