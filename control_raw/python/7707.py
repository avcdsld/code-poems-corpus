def fully_connected(attrs, inputs, proto_obj):
    """Applies a linear transformation: Y=XWT+b."""
    new_attrs = translation_utils._remove_attributes(attrs, ['axis'])

    new_attrs = translation_utils._fix_bias('FullyConnected', new_attrs, len(inputs))

    new_attrs = translation_utils._fix_channels('FullyConnected', new_attrs, inputs, proto_obj)

    return 'FullyConnected', new_attrs, inputs