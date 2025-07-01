def hostgroup_delete(hostgroupids, **kwargs):
    '''
    Delete the host group.

    .. versionadded:: 2016.3.0

    :param hostgroupids: IDs of the host groups to delete
    :param _connection_user: Optional - zabbix user (can also be set in opts or pillar, see module's docstring)
    :param _connection_password: Optional - zabbix password (can also be set in opts or pillar, see module's docstring)
    :param _connection_url: Optional - url of zabbix frontend (can also be set in opts, pillar, see module's docstring)

    :return: ID of the deleted host groups, False on failure.

    CLI Example:
    .. code-block:: bash

        salt '*' zabbix.hostgroup_delete 23
    '''
    conn_args = _login(**kwargs)
    ret = {}
    try:
        if conn_args:
            method = 'hostgroup.delete'
            if not isinstance(hostgroupids, list):
                params = [hostgroupids]
            else:
                params = hostgroupids
            ret = _query(method, params, conn_args['url'], conn_args['auth'])
            return ret['result']['groupids']
        else:
            raise KeyError
    except KeyError:
        return ret