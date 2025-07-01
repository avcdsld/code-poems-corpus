def get_entity(ent_type, **kwargs):
    '''
    Attempt to query Keystone for more information about an entity
    '''
    try:
        func = 'keystoneng.{}_get'.format(ent_type)
        ent = __salt__[func](**kwargs)
    except OpenStackCloudException as e:
        # NOTE(SamYaple): If this error was something other than Forbidden we
        # reraise the issue since we are not prepared to handle it
        if 'HTTP 403' not in e.inner_exception[1][0]:
            raise

        # NOTE(SamYaple): The user may be authorized to perform the function
        # they are trying to do, but not authorized to search. In such a
        # situation we want to trust that the user has passed a valid id, even
        # though we cannot validate that this is a valid id
        ent = kwargs['name']

    return ent