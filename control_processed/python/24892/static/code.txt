def _login(**kwargs):
    '''
    Log in to the API and generate the authentication token.

    .. versionadded:: 2016.3.0

    :param _connection_user: Optional - zabbix user (can also be set in opts or pillar, see module's docstring)
    :param _connection_password: Optional - zabbix password (can also be set in opts or pillar, see module's docstring)
    :param _connection_url: Optional - url of zabbix frontend (can also be set in opts, pillar, see module's docstring)

    :return: On success connargs dictionary with auth token and frontend url, False on failure.

    '''
    connargs = dict()

    def _connarg(name, key=None):
        '''
        Add key to connargs, only if name exists in our kwargs or, as zabbix.<name> in __opts__ or __pillar__

        Evaluate in said order - kwargs, opts, then pillar. To avoid collision with other functions,
        kwargs-based connection arguments are prefixed with 'connection_' (i.e. '_connection_user', etc.).

        Inspired by mysql salt module.
        '''
        if key is None:
            key = name

        if name in kwargs:
            connargs[key] = kwargs[name]
        else:
            prefix = '_connection_'
            if name.startswith(prefix):
                try:
                    name = name[len(prefix):]
                except IndexError:
                    return
            val = __salt__['config.option']('zabbix.{0}'.format(name), None)
            if val is not None:
                connargs[key] = val

    _connarg('_connection_user', 'user')
    _connarg('_connection_password', 'password')
    _connarg('_connection_url', 'url')

    if 'url' not in connargs:
        connargs['url'] = _frontend_url()

    try:
        if connargs['user'] and connargs['password'] and connargs['url']:
            params = {'user': connargs['user'], 'password': connargs['password']}
            method = 'user.login'
            ret = _query(method, params, connargs['url'])
            auth = ret['result']
            connargs['auth'] = auth
            connargs.pop('user', None)
            connargs.pop('password', None)
            return connargs
        else:
            raise KeyError
    except KeyError as err:
        raise SaltException('URL is probably not correct! ({})'.format(err))