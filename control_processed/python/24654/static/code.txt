def user_grant_roles(name, roles, database, user=None, password=None, host=None,
                     port=None, authdb=None):
    '''
    Grant one or many roles to a MongoDB user

    CLI Examples:

    .. code-block:: bash

        salt '*' mongodb.user_grant_roles johndoe '["readWrite"]' dbname admin adminpwd localhost 27017

    .. code-block:: bash

        salt '*' mongodb.user_grant_roles janedoe '[{"role": "readWrite", "db": "dbname" }, {"role": "read", "db": "otherdb"}]' dbname admin adminpwd localhost 27017
    '''
    conn = _connect(user, password, host, port, authdb=authdb)
    if not conn:
        return 'Failed to connect to mongo database'

    try:
        roles = _to_dict(roles)
    except Exception:
        return 'Roles provided in wrong format'

    try:
        log.info('Granting roles %s to user %s', roles, name)
        mdb = pymongo.database.Database(conn, database)
        mdb.command("grantRolesToUser", name, roles=roles)
    except pymongo.errors.PyMongoError as err:
        log.error('Granting roles %s to user %s failed with error: %s', roles, name, err)
        return six.text_type(err)

    return True