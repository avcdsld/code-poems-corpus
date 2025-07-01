def convert_activation(builder, layer, input_names, output_names, keras_layer):
    """Convert an activation layer from keras to coreml.

    Parameters
    ----------
    keras_layer: layer
        A keras layer object.

    builder: NeuralNetworkBuilder
        A neural network builder object.
    """
    # Get input and output names
    input_name, output_name = (input_names[0], output_names[0])
    non_linearity = _get_activation_name_from_keras_layer(keras_layer)

    # Add a non-linearity layer
    if non_linearity == 'SOFTMAX':
        builder.add_softmax(name = layer, input_name = input_name,
                output_name = output_name)
        return

    params = None
    if non_linearity == 'LEAKYRELU':
        params = [keras_layer.alpha]

    elif non_linearity == 'PRELU':
        # In Keras 1.2  PReLU layer's weights are stored as a
        # backend tensor, not a numpy array as it claims in documentation.
        shared_axes = list(keras_layer.shared_axes)
        if not (shared_axes == [1,2,3] or shared_axes == [1,2]):
            _utils.raise_error_unsupported_scenario("Shared axis not being [1,2,3] or [1,2]", 'parametric_relu', layer)
        params = keras.backend.eval(keras_layer.weights[0])
    elif non_linearity == 'ELU':
        params = keras_layer.alpha

    elif non_linearity == 'PARAMETRICSOFTPLUS':
        # In Keras 1.2  Parametric Softplus layer's weights are stored as a
        # backend tensor, not a numpy array as it claims in documentation.
        alphas = keras.backend.eval(keras_layer.weights[0])
        betas = keras.backend.eval(keras_layer.weights[1])

        if len(alphas.shape) == 3:  # (H,W,C)
            if not (_same_elements_per_channel(alphas) and _same_elements_per_channel(betas)):
                _utils.raise_error_unsupported_scenario("Different parameter values", 'parametric_softplus', layer)
            alphas = alphas[0,0,:]
            betas = betas[0,0,:]
        params = [alphas, betas]

    elif non_linearity == 'THRESHOLDEDRELU':
        params = keras_layer.theta
    else:
        pass # do nothing to parameters
    builder.add_activation(name = layer,
            non_linearity = non_linearity,
            input_name = input_name, output_name = output_name,
            params = params)