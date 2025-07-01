def decode_seq(self, inputs, states, valid_length=None):
        """Decode the decoder inputs. This function is only used for training.

        Parameters
        ----------
        inputs : NDArray, Shape (batch_size, length, C_in)
        states : list of NDArrays or None
            Initial states. The list of initial decoder states
        valid_length : NDArray or None
            Valid lengths of each sequence. This is usually used when part of sequence has
            been padded. Shape (batch_size,)

        Returns
        -------
        output : NDArray, Shape (batch_size, length, C_out)
        states : list
            The decoder states, includes:

            - rnn_states : NDArray
            - attention_vec : NDArray
            - mem_value : NDArray
            - mem_masks : NDArray, optional
        additional_outputs : list
            Either be an empty list or contains the attention weights in this step.
            The attention weights will have shape (batch_size, length, mem_length) or
            (batch_size, num_heads, length, mem_length)
        """
        length = inputs.shape[1]
        output = []
        additional_outputs = []
        inputs = _as_list(mx.nd.split(inputs, num_outputs=length, axis=1, squeeze_axis=True))
        rnn_states_l = []
        attention_output_l = []
        fixed_states = states[2:]
        for i in range(length):
            ele_output, states, ele_additional_outputs = self.forward(inputs[i], states)
            rnn_states_l.append(states[0])
            attention_output_l.append(states[1])
            output.append(ele_output)
            additional_outputs.extend(ele_additional_outputs)
        output = mx.nd.stack(*output, axis=1)
        if valid_length is not None:
            states = [_nested_sequence_last(rnn_states_l, valid_length),
                      _nested_sequence_last(attention_output_l, valid_length)] + fixed_states
            output = mx.nd.SequenceMask(output,
                                        sequence_length=valid_length,
                                        use_sequence_length=True,
                                        axis=1)
        if self._output_attention:
            additional_outputs = [mx.nd.concat(*additional_outputs, dim=-2)]
        return output, states, additional_outputs