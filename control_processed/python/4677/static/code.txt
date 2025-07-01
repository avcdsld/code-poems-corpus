def universal_transformer_basic(layer_inputs,
                                step, hparams,
                                ffn_unit,
                                attention_unit):
  """Basic Universal Transformer.

  This model is pretty similar to the vanilla transformer in which weights are
  shared between layers. For some tasks, this simple idea brings a
  generalization that is not achievable by playing with the size of the model
  or drop_out parameters in the vanilla transformer.

  Args:
    layer_inputs:
        - state: state
    step: indicates number of steps taken so far
    hparams: model hyper-parameters
    ffn_unit: feed-forward unit
    attention_unit: multi-head attention unit

  Returns:
    layer_output:
         new_state: new state
  """
  state, inputs, memory = tf.unstack(layer_inputs, num=None, axis=0,
                                     name="unstack")
  new_state = step_preprocess(state, step, hparams)

  for i in range(hparams.num_inrecurrence_layers):
    with tf.variable_scope("rec_layer_%d" % i):
      new_state = ffn_unit(attention_unit(new_state))

  return new_state, inputs, memory