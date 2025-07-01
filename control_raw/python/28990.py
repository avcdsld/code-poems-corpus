def grant_privilege(database, privilege, username, **client_args):
    '''
    Grant a privilege on a database to a user.

    database
        Name of the database to grant the privilege on.

    privilege
        Privilege to grant. Can be one of 'read', 'write' or 'all'.

    username
        Name of the user to grant the privilege to.
    '''
    client = _client(**client_args)
    client.grant_privilege(privilege, database, username)

    return True