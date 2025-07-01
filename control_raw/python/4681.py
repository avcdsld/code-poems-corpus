def universal_transformer_with_lstm_as_transition_function(
    layer_inputs, step, hparams, ffn_unit, attention_unit, pad_remover=None):
  """Universal Transformer which uses a lstm as transition function.

  It's kind of like having a lstm, filliped vertically next to the Universal
  Transformer that controls the flow of the  information in depth,
  over different steps of the Universal Transformer.

  Args:
    layer_inputs:
      - state: state
      - inputs: the original embedded inputs (= inputs to the first step)
      - memory: memory used in lstm.
    step: indicates number of steps taken so far
    hparams: model hyper-parameters.
    ffn_unit: feed-forward unit
    attention_unit: multi-head attention unit
    pad_remover: to mask out padding in convolutional layers (efficiency).
  Returns:
    layer_output:
        new_state: new state
        inputs: the original embedded inputs (= inputs to the first step)
        memory: contains information of state from all the previous steps.
  """

  state, unused_inputs, memory = tf.unstack(
      layer_inputs, num=None, axis=0, name="unstack")
  # NOTE:
  # state (ut_state): output of the lstm in the previous step
  # inputs (ut_input): original input --> we don't use it here
  # memory: lstm memory

  # Multi_head_attention:
  assert not hparams.add_step_timing_signal  # Let lstm count for us!
  mh_attention_input = step_preprocess(state, step, hparams)
  transition_function_input = attention_unit(mh_attention_input)

  # Transition Function:
  if hparams.add_ffn_unit_to_the_transition_function:
    transition_function_input = ffn_unit(transition_function_input)

  transition_function_input = common_layers.layer_preprocess(
      transition_function_input, hparams)
  with tf.variable_scope("lstm"):
    # lstm input gate: i_t = sigmoid(W_i.x_t + U_i.h_{t-1})
    transition_function_input_gate = _ffn_layer_multi_inputs(
        [transition_function_input, state],
        hparams,
        name="input",
        bias_initializer=tf.zeros_initializer(),
        activation=tf.sigmoid,
        pad_remover=pad_remover,
        preprocess=False,
        postprocess=False)

    tf.contrib.summary.scalar("lstm_input_gate",
                              tf.reduce_mean(transition_function_input_gate))

    # lstm forget gate: f_t = sigmoid(W_f.x_t + U_f.h_{t-1})
    transition_function_forget_gate = _ffn_layer_multi_inputs(
        [transition_function_input, state],
        hparams,
        name="forget",
        bias_initializer=tf.zeros_initializer(),
        activation=None,
        pad_remover=pad_remover,
        preprocess=False,
        postprocess=False)
    forget_bias_tensor = tf.constant(hparams.lstm_forget_bias)
    transition_function_forget_gate = tf.sigmoid(
        transition_function_forget_gate + forget_bias_tensor)

    tf.contrib.summary.scalar("lstm_forget_gate",
                              tf.reduce_mean(transition_function_forget_gate))

    # lstm output gate: o_t = sigmoid(W_o.x_t + U_o.h_{t-1})
    transition_function_output_gate = _ffn_layer_multi_inputs(
        [transition_function_input, state],
        hparams,
        name="output",
        bias_initializer=tf.zeros_initializer(),
        activation=tf.sigmoid,
        pad_remover=pad_remover,
        preprocess=False,
        postprocess=False)

    tf.contrib.summary.scalar("lstm_output_gate",
                              tf.reduce_mean(transition_function_output_gate))

    # lstm input modulation
    transition_function_input_modulation = _ffn_layer_multi_inputs(
        [transition_function_input, state],
        hparams,
        name="input_modulation",
        bias_initializer=tf.zeros_initializer(),
        activation=tf.tanh,
        pad_remover=pad_remover,
        preprocess=False,
        postprocess=False)

    transition_function_memory = (
        memory * transition_function_forget_gate +
        transition_function_input_gate * transition_function_input_modulation)

    transition_function_output = (
        tf.tanh(transition_function_memory) * transition_function_output_gate)

  transition_function_output = common_layers.layer_preprocess(
      transition_function_output, hparams)

  return transition_function_output, unused_inputs, transition_function_memory