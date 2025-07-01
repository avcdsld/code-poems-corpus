def image_list(auth=None, **kwargs):
    '''
    List images

    CLI Example:

    .. code-block:: bash

        salt '*' glanceng.image_list
        salt '*' glanceng.image_list
    '''
    cloud = get_operator_cloud(auth)
    kwargs = _clean_kwargs(**kwargs)
    return cloud.list_images(**kwargs)