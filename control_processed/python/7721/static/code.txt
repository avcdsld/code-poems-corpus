def flatten(attrs, inputs, proto_obj):
    """Flattens the input array into a 2-D array by collapsing the higher dimensions."""
    #Mxnet does not have axis support. By default uses axis=1
    if 'axis' in attrs and attrs['axis'] != 1:
        raise RuntimeError("Flatten operator only supports axis=1")
    new_attrs = translation_utils._remove_attributes(attrs, ['axis'])
    return 'Flatten', new_attrs, inputs