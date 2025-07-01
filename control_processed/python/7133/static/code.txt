def convert_deconvolution(node, **kwargs):
    """Map MXNet's deconvolution operator attributes to onnx's ConvTranspose operator
    and return the created node.
    """
    name, inputs, attrs = get_inputs(node, kwargs)

    kernel_dims = list(parse_helper(attrs, "kernel"))
    stride_dims = list(parse_helper(attrs, "stride", [1, 1]))
    pad_dims = list(parse_helper(attrs, "pad", [0, 0]))
    num_group = int(attrs.get("num_group", 1))
    dilations = list(parse_helper(attrs, "dilate", [1, 1]))
    adj_dims = list(parse_helper(attrs, "adj", [0, 0]))

    pad_dims = pad_dims + pad_dims

    deconv_node = onnx.helper.make_node(
        "ConvTranspose",
        inputs=inputs,
        outputs=[name],
        kernel_shape=kernel_dims,
        strides=stride_dims,
        dilations=dilations,
        output_padding=adj_dims,
        pads=pad_dims,
        group=num_group,
        name=name
    )

    return [deconv_node]