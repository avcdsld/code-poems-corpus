def absent(name,
           user=None,
           password=None,
           host=None,
           port=None,
           database="admin",
           authdb=None):
    '''
    Ensure that the named user is absent

    name
        The name of the user to remove

    user
        MongoDB user with sufficient privilege to create the user

    password
        Password for the admin user specified by the ``user`` parameter

    host
        The hostname/IP address of the MongoDB server

    port
        The port on which MongoDB is listening

    database
        The database from which to remove the user specified by the ``name``
        parameter

    authdb
        The database in which to authenticate
    '''
    ret = {'name': name,
           'changes': {},
           'result': True,
           'comment': ''}

    #check if user exists and remove it
    user_exists = __salt__['mongodb.user_exists'](name, user, password, host, port, database=database, authdb=authdb)
    if user_exists is True:
        if __opts__['test']:
            ret['result'] = None
            ret['comment'] = ('User {0} is present and needs to be removed'
                    ).format(name)
            return ret
        if __salt__['mongodb.user_remove'](name, user, password, host, port, database=database, authdb=authdb):
            ret['comment'] = 'User {0} has been removed'.format(name)
            ret['changes'][name] = 'Absent'
            return ret

    # if the check does not return a boolean, return an error
    # this may be the case if there is a database connection error
    if not isinstance(user_exists, bool):
        ret['comment'] = user_exists
        ret['result'] = False
        return ret

    # fallback
    ret['comment'] = 'User {0} is not present'.format(name)
    return ret