def user_remove(username, **kwargs):
    '''
    Removes an user.

    CLI Example:

    .. code-block:: bash

        salt minion mssql.user_remove USERNAME database=DBNAME
    '''
    # 'database' argument is mandatory
    if 'database' not in kwargs:
        return False
    try:
        conn = _get_connection(**kwargs)
        conn.autocommit(True)
        cur = conn.cursor()
        cur.execute("DROP USER {0}".format(username))
        conn.autocommit(False)
        conn.close()
        return True
    except Exception as e:
        return 'Could not create the user: {0}'.format(e)