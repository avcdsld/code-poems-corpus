def set_identity_pool_roles(IdentityPoolId, AuthenticatedRole=None, UnauthenticatedRole=None,
        region=None, key=None, keyid=None, profile=None):
    '''
    Given an identity pool id, set the given AuthenticatedRole and UnauthenticatedRole (the Role
    can be an iam arn, or a role name)  If AuthenticatedRole or UnauthenticatedRole is not given,
    the authenticated and/or the unauthenticated role associated previously with the pool will be
    cleared.

    Returns set True if successful, set False if unsuccessful with the associated errors.

    CLI Example:

    .. code-block:: bash

        salt myminion boto_cognitoidentity.set_identity_pool_roles my_id_pool_roles  # this clears the roles
        salt myminion boto_cognitoidentity.set_identity_pool_roles my_id_pool_id \
            AuthenticatedRole=my_auth_role UnauthenticatedRole=my_unauth_role  # this set both roles
        salt myminion boto_cognitoidentity.set_identity_pool_roles my_id_pool_id \
            AuthenticatedRole=my_auth_role  # this will set the auth role and clear the unauth role
        salt myminion boto_cognitoidentity.set_identity_pool_roles my_id_pool_id \
            UnauthenticatedRole=my_unauth_role  # this will set the unauth role and clear the auth role

    '''
    conn_params = dict(region=region, key=key, keyid=keyid, profile=profile)
    conn = _get_conn(**conn_params)

    try:
        if AuthenticatedRole:
            role_arn = _get_role_arn(AuthenticatedRole, **conn_params)
            if role_arn is None:
                return {'set': False, 'error': 'invalid AuthenticatedRole {0}'.format(AuthenticatedRole)}
            AuthenticatedRole = role_arn

        if UnauthenticatedRole:
            role_arn = _get_role_arn(UnauthenticatedRole, **conn_params)
            if role_arn is None:
                return {'set': False, 'error': 'invalid UnauthenticatedRole {0}'.format(UnauthenticatedRole)}
            UnauthenticatedRole = role_arn

        Roles = dict()
        if AuthenticatedRole:
            Roles['authenticated'] = AuthenticatedRole
        if UnauthenticatedRole:
            Roles['unauthenticated'] = UnauthenticatedRole

        conn.set_identity_pool_roles(IdentityPoolId=IdentityPoolId, Roles=Roles)

        return {'set': True, 'roles': Roles}
    except ClientError as e:
        return {'set': False, 'error': __utils__['boto3.get_error'](e)}