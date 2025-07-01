def user_delete(auth=None, **kwargs):
    '''
    Delete a user

    CLI Example:

    .. code-block:: bash

        salt '*' keystoneng.user_delete name=user1
        salt '*' keystoneng.user_delete name=user2 domain_id=b62e76fbeeff4e8fb77073f591cf211e
        salt '*' keystoneng.user_delete name=a42cbbfa1e894e839fd0f584d22e321f
    '''
    cloud = get_openstack_cloud(auth)
    kwargs = _clean_kwargs(**kwargs)
    return cloud.delete_user(**kwargs)