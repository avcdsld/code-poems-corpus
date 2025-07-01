def substitute_params(input_object, extend_params=None, filter_key='name', **kwargs):
    '''
    .. versionadded:: 2017.7

    Go through Zabbix object params specification and if needed get given object ID from Zabbix API and put it back
    as a value. Definition of the object is done via dict with keys "query_object" and "query_name".

    :param input_object: Zabbix object type specified in state file
    :param extend_params: Specify query with params
    :param filter_key: Custom filtering key (default: name)
    :param _connection_user: Optional - zabbix user (can also be set in opts or pillar, see module's docstring)
    :param _connection_password: Optional - zabbix password (can also be set in opts or pillar, see module's docstring)
    :param _connection_url: Optional - url of zabbix frontend (can also be set in opts, pillar, see module's docstring)

    :return: Params structure with values converted to string for further comparison purposes
    '''
    if extend_params is None:
        extend_params = {}
    if isinstance(input_object, list):
        return [substitute_params(oitem, extend_params, filter_key, **kwargs) for oitem in input_object]
    elif isinstance(input_object, dict):
        if 'query_object' in input_object:
            query_params = {}
            if input_object['query_object'] not in ZABBIX_TOP_LEVEL_OBJECTS:
                query_params.update(extend_params)
            try:
                query_params.update({'filter': {filter_key: input_object['query_name']}})
                return get_object_id_by_params(input_object['query_object'], query_params, **kwargs)
            except KeyError:
                raise SaltException('Qyerying object ID requested '
                                    'but object name not provided: {0}'.format(input_object))
        else:
            return {key: substitute_params(val, extend_params, filter_key, **kwargs)
                    for key, val in input_object.items()}
    else:
        # Zabbix response is always str, return everything in str as well
        return six.text_type(input_object)