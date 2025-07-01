def convert_simple_rnn(builder, layer, input_names, output_names, keras_layer):
    """Convert an SimpleRNN layer from keras to coreml.

    Parameters
    ----------
    keras_layer: layer
        A keras layer object.

    builder: NeuralNetworkBuilder
        A neural network builder object.
    """
    # Get input and output names
    hidden_size = keras_layer.output_dim
    input_size = keras_layer.input_shape[-1]

    output_all = keras_layer.return_sequences
    reverse_input = keras_layer.go_backwards

    if keras_layer.consume_less not in ['cpu', 'gpu']:
        raise ValueError('Cannot convert Keras layer with consume_less = %s' % keras_layer.consume_less)

    W_h = np.zeros((hidden_size, hidden_size))
    W_x = np.zeros((hidden_size, input_size))
    b = np.zeros((hidden_size,))

    if keras_layer.consume_less == 'cpu':
        W_h = keras_layer.get_weights()[1].T
        W_x = keras_layer.get_weights()[0].T
        b = keras_layer.get_weights()[2]
    else:
        W_h = keras_layer.get_weights()[1].T
        W_x = keras_layer.get_weights()[0].T
        b = keras_layer.get_weights()[2]

    # Set actication type
    activation_str = _get_recurrent_activation_name_from_keras(keras_layer.activation)

    # Add to the network
    builder.add_simple_rnn(
        name = layer,
        W_h = W_h, W_x = W_x, b = b,
        hidden_size = hidden_size,
        input_size = input_size,
        activation = activation_str,
        input_names = input_names,
        output_names = output_names,
        output_all=output_all,
        reverse_input=reverse_input)