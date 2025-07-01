def reduce_prod(attrs, inputs, proto_obj):
    """Reduce the array along a given axis by product value"""
    new_attrs = translation_utils._fix_attribute_names(attrs, {'axes':'axis'})
    return 'prod', new_attrs, inputs