def role_remove(role, **kwargs):
    '''
    Remove a database role.

    CLI Example:

    .. code-block:: bash

        salt minion mssql.role_create role=test_role01
    '''
    try:
        conn = _get_connection(**kwargs)
        conn.autocommit(True)
        cur = conn.cursor()
        cur.execute('DROP ROLE {0}'.format(role))
        conn.autocommit(True)
        conn.close()
        return True
    except Exception as e:
        return 'Could not create the role: {0}'.format(e)