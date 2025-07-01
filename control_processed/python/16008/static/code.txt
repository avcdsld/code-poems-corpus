def convert_cropping(builder, layer, input_names, output_names, keras_layer):
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
    is_1d = isinstance(keras_layer, _keras.layers.Cropping1D)

    cropping = keras_layer.cropping
    top = left = bottom = right = 0
    if is_1d:
        if type(cropping) is int:
            left = right = cropping
        elif type(cropping) is tuple:
            if type(cropping[0]) is int:
                left, right = cropping
            elif type(cropping[0]) is tuple and len(cropping[0]) == 2:
                left, right = cropping[0]
            else:
                raise ValueError("Unrecognized cropping option: %s" % (str(cropping)))
        else:
            raise ValueError("Unrecognized cropping option: %s" % (str(cropping)))
    else:
        if type(cropping) is int:
            top = left = bottom = right = cropping
        elif type(cropping) is tuple:
            if type(cropping[0]) is int:
                top, left = cropping
                bottom, right = cropping
            elif type(cropping[0]) is tuple:
                top, bottom = cropping[0]
                left, right = cropping[1]
            else:
                raise ValueError("Unrecognized cropping option: %s" % (str(cropping)))
        else:
            raise ValueError("Unrecognized cropping option: %s" % (str(cropping)))

    # Now add the layer
    builder.add_crop(name = layer,
        left = left, right=right, top=top, bottom=bottom, offset = [0,0],
        input_names = [input_name], output_name=output_name
        )