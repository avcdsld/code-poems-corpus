def convert_padding(builder, layer, input_names, output_names, keras_layer):
    """
    Convert padding layer from keras to coreml.
    Keras only supports zero padding at this time.
    Parameters
    ----------
    keras_layer: layer
        A keras layer object.

    builder: NeuralNetworkBuilder
        A neural network builder object.
    """
    _check_data_format(keras_layer)
    # Get input and output names
    input_name, output_name = (input_names[0], output_names[0])

    is_1d = isinstance(keras_layer, _keras.layers.ZeroPadding1D)

    padding = keras_layer.padding
    top = left = bottom = right = 0
    if is_1d:
        if type(padding) is int:
            left = right = padding
        elif type(padding) is tuple:
            if type(padding[0]) is int:
                left, right = padding
            elif type(padding[0]) is tuple and len(padding[0]) == 2:
                left, right = padding[0]
            else:
                raise ValueError("Unrecognized padding option: %s" % (str(padding)))
        else:
            raise ValueError("Unrecognized padding option: %s" % (str(padding)))
    else:
        if type(padding) is int:
            top = left = bottom = right = padding
        elif type(padding) is tuple:
            if type(padding[0]) is int:
                top, left = padding
                bottom, right = padding
            elif type(padding[0]) is tuple:
                top, bottom = padding[0]
                left, right = padding[1]
            else:
                raise ValueError("Unrecognized padding option: %s" % (str(padding)))
        else:
            raise ValueError("Unrecognized padding option: %s" % (str(padding)))

    # Now add the layer
    builder.add_padding(name = layer,
        left = left, right=right, top=top, bottom=bottom, value = 0,
        input_name = input_name, output_name=output_name
        )