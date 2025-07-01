def convert_concat(node, **kwargs):
    """Map MXNet's Concat operator attributes to onnx's Concat operator
    and return the created node.
    """
    name, input_nodes, attrs = get_inputs(node, kwargs)

    axis = int(attrs.get("dim", 1))
    concat_node = onnx.helper.make_node(
        "Concat",
        input_nodes,
        [name],
        axis=axis,
        name=name
    )
    return [concat_node]