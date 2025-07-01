def loaddata(settings_module,
             fixtures,
             bin_env=None,
             database=None,
             pythonpath=None,
             env=None):
    '''
    Load fixture data

    Fixtures:
        comma separated list of fixtures to load

    CLI Example:

    .. code-block:: bash

        salt '*' django.loaddata <settings_module> <comma delimited list of fixtures>

    '''
    args = []
    kwargs = {}
    if database:
        kwargs['database'] = database

    cmd = '{0} {1}'.format('loaddata', ' '.join(fixtures.split(',')))

    return command(settings_module,
                   cmd,
                   bin_env,
                   pythonpath,
                   env,
                   *args, **kwargs)