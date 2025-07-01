def revoke_privilege(database, privilege, username, **client_args):
    '''
    Revoke a privilege on a database from a user.

    database
        Name of the database to grant the privilege on.

    privilege
        Privilege to grant. Can be one of 'read', 'write' or 'all'.

    username
        Name of the user to grant the privilege to.
    '''
    client = _client(**client_args)
    client.revoke_privilege(privilege, database, username)

    return True