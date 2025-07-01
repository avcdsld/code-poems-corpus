def serialize(serializer, obj, **mod_kwargs):
    '''
    Serialize a Python object using a :py:mod:`serializer module
    <salt.serializers>`

    CLI Example:

    .. code-block:: bash

        salt '*' --no-parse=obj slsutil.serialize 'json' obj="{'foo': 'Foo!'}

    Jinja Example:

    .. code-block:: jinja

        {% set json_string = salt.slsutil.serialize('json',
            {'foo': 'Foo!'}) %}
    '''
    kwargs = salt.utils.args.clean_kwargs(**mod_kwargs)
    return _get_serialize_fn(serializer, 'serialize')(obj, **kwargs)