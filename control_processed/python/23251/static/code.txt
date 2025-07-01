def user_exists(name, database=None, user=None, password=None, host=None, port=None):
    '''
    Checks if a cluster admin or database user exists.

    If a database is specified: it will check for database user existence.
    If a database is not specified: it will check for cluster admin existence.

    name
        User name

    database
        The database to check for the user to exist

    user
        The user to connect as

    password
        The password of the user

    host
        The host to connect to

    port
        The port to connect to

    CLI Example:

    .. code-block:: bash

        salt '*' influxdb08.user_exists <name>
        salt '*' influxdb08.user_exists <name> <database>
        salt '*' influxdb08.user_exists <name> <database> <user> <password> <host> <port>
    '''
    users = user_list(database, user, password, host, port)
    if not isinstance(users, list):
        return False

    for user in users:
        # the dict key could be different depending on influxdb version
        username = user.get('user', user.get('name'))
        if username:
            if username == name:
                return True
        else:
            log.warning('Could not find username in user: %s', user)

    return False