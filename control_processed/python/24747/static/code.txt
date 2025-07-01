def template_delete(call=None, kwargs=None):
    '''
    Deletes the given template from OpenNebula. Either a name or a template_id must
    be supplied.

    .. versionadded:: 2016.3.0

    name
        The name of the template to delete. Can be used instead of ``template_id``.

    template_id
        The ID of the template to delete. Can be used instead of ``name``.

    CLI Example:

    .. code-block:: bash

        salt-cloud -f template_delete opennebula name=my-template
        salt-cloud --function template_delete opennebula template_id=5
    '''
    if call != 'function':
        raise SaltCloudSystemExit(
            'The template_delete function must be called with -f or --function.'
        )

    if kwargs is None:
        kwargs = {}

    name = kwargs.get('name', None)
    template_id = kwargs.get('template_id', None)

    if template_id:
        if name:
            log.warning(
                'Both the \'template_id\' and \'name\' arguments were provided. '
                '\'template_id\' will take precedence.'
            )
    elif name:
        template_id = get_template_id(kwargs={'name': name})
    else:
        raise SaltCloudSystemExit(
            'The template_delete function requires either a \'name\' or a \'template_id\' '
            'to be provided.'
        )

    server, user, password = _get_xml_rpc()
    auth = ':'.join([user, password])
    response = server.one.template.delete(auth, int(template_id))

    data = {
        'action': 'template.delete',
        'deleted': response[0],
        'template_id': response[1],
        'error_code': response[2],
    }

    return data