def schema_get(name, profile=None):
    '''
    Known valid names of schemas are:
      - image
      - images
      - member
      - members

    CLI Example:

    .. code-block:: bash

        salt '*' glance.schema_get name=f16-jeos
    '''
    g_client = _auth(profile)
    schema_props = {}
    for prop in g_client.schemas.get(name).properties:
        schema_props[prop.name] = prop.description
    log.debug(
        'Properties of schema %s:\n%s',
        name, pprint.PrettyPrinter(indent=4).pformat(schema_props)
    )
    return {name: schema_props}