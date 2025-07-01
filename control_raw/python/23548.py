def auth(username, password):
    '''
    Authenticate using a MySQL user table
    '''
    _info = __get_connection_info()

    if _info is None:
        return False

    try:
        conn = MySQLdb.connect(_info['hostname'],
                               _info['username'],
                               _info['password'],
                               _info['database'])
    except OperationalError as e:
        log.error(e)
        return False

    cur = conn.cursor()
    cur.execute(_info['auth_sql'].format(username, password))

    if cur.rowcount == 1:
        return True

    return False