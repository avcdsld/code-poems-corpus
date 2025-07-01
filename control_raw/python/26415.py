def get_or_set_hash(name,
        length=8,
        chars='abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'):
    '''
    Perform a one-time generation of a hash and write it to the local grains.
    If that grain has already been set return the value instead.

    This is useful for generating passwords or keys that are specific to a
    single minion that don't need to be stored somewhere centrally.

    State Example:

    .. code-block:: yaml

        some_mysql_user:
          mysql_user:
            - present
            - host: localhost
            - password: {{ salt['grains.get_or_set_hash']('mysql:some_mysql_user') }}

    CLI Example:

    .. code-block:: bash

        salt '*' grains.get_or_set_hash 'django:SECRET_KEY' 50

    .. warning::

        This function could return strings which may contain characters which are reserved
        as directives by the YAML parser, such as strings beginning with ``%``. To avoid
        issues when using the output of this function in an SLS file containing YAML+Jinja,
        surround the call with single quotes.
    '''
    ret = get(name, None)

    if ret is None:
        val = ''.join([random.SystemRandom().choice(chars) for _ in range(length)])

        if DEFAULT_TARGET_DELIM in name:
            root, rest = name.split(DEFAULT_TARGET_DELIM, 1)
            curr = get(root, _infinitedict())
            val = _dict_from_path(rest, val)
            curr.update(val)
            setval(root, curr)
        else:
            setval(name, val)

    return get(name)