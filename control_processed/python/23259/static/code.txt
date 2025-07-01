def query(database,
          query,
          time_precision='s',
          chunked=False,
          user=None,
          password=None,
          host=None,
          port=None):
    '''
    Querying data

    database
        The database to query

    query
        Query to be executed

    time_precision
        Time precision to use ('s', 'm', or 'u')

    chunked
        Whether is chunked or not

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

        salt '*' influxdb08.query <database> <query>
        salt '*' influxdb08.query <database> <query> <time_precision> <chunked> <user> <password> <host> <port>
    '''
    client = _client(user=user, password=password, host=host, port=port)
    client.switch_database(database)
    return client.query(query, time_precision=time_precision, chunked=chunked)