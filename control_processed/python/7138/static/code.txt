def convert_pad(node, **kwargs):
    """Map MXNet's pad operator attributes to onnx's Pad operator
    and return the created node.
    """
    name, input_nodes, attrs = get_inputs(node, kwargs)

    mxnet_pad_width = convert_string_to_list(attrs.get("pad_width"))
    onnx_pad_width = transform_padding(mxnet_pad_width)

    pad_mode = attrs.get("mode")

    if pad_mode == "constant":
        pad_value = float(attrs.get("constant_value")) \
            if "constant_value" in attrs else 0.0
        node = onnx.helper.make_node(
            'Pad',
            inputs=input_nodes,
            outputs=[name],
            mode='constant',
            value=pad_value,
            pads=onnx_pad_width,
            name=name
        )
    else:
        node = onnx.helper.make_node(
            'Pad',
            inputs=input_nodes,
            outputs=[name],
            mode=pad_mode,
            pads=onnx_pad_width,
            name=name
        )

    return [node]