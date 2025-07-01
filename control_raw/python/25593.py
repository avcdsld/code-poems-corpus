def set_user_password(uid, mode='set_password', password=None, **kwargs):
    '''
    Set user password and (modes)

    :param uid: id number of user.  see: get_names_uid()['name']

    :param mode:
        - disable       = disable user connections
        - enable        = enable user connections
        - set_password  = set or ensure password
        - test_password = test password is correct
    :param password: max 16 char string
        (optional when mode is [disable or enable])
    :param kwargs:
        - api_host=127.0.0.1
        - api_user=admin
        - api_pass=example
        - api_port=623
        - api_kg=None

    :return:
        True on success
        when mode = test_password, return False on bad password

    CLI Example:

    .. code-block:: bash

        salt-call ipmi.set_user_password api_host=127.0.0.1 api_user=admin api_pass=pass
                                         uid=1 password=newPass
        salt-call ipmi.set_user_password uid=1 mode=enable
    '''
    with _IpmiCommand(**kwargs) as s:
        s.set_user_password(uid, mode='set_password', password=password)
    return True