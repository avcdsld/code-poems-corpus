def convert_advanced_relu(builder, layer, input_names, output_names, keras_layer):
    """
    Convert an ReLU layer with maximum value from keras to coreml.

    Parameters
    ----------
    keras_layer: layer
        A keras layer object.

    builder: NeuralNetworkBuilder
        A neural network builder object.
    """
    # Get input and output names
    input_name, output_name = (input_names[0], output_names[0])

    if keras_layer.max_value is None:
        builder.add_activation(layer, 'RELU', input_name, output_name)
        return

    # No direct support of RELU with max-activation value - use negate and
    # clip layers
    relu_output_name = output_name + '_relu'
    builder.add_activation(layer, 'RELU', input_name, relu_output_name)
    # negate it
    neg_output_name = relu_output_name + '_neg'
    builder.add_activation(layer+'__neg__', 'LINEAR', relu_output_name,
            neg_output_name,[-1.0, 0])
    # apply threshold
    clip_output_name = relu_output_name + '_clip'
    builder.add_unary(layer+'__clip__', neg_output_name, clip_output_name,
            'threshold', alpha = -keras_layer.max_value)
    # negate it back
    builder.add_activation(layer+'_neg2', 'LINEAR', clip_output_name,
            output_name,[-1.0, 0])