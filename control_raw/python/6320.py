def sort_and_run_forward(self,
                             module: Callable[[PackedSequence, Optional[RnnState]],
                                              Tuple[Union[PackedSequence, torch.Tensor], RnnState]],
                             inputs: torch.Tensor,
                             mask: torch.Tensor,
                             hidden_state: Optional[RnnState] = None):
        """
        This function exists because Pytorch RNNs require that their inputs be sorted
        before being passed as input. As all of our Seq2xxxEncoders use this functionality,
        it is provided in a base class. This method can be called on any module which
        takes as input a ``PackedSequence`` and some ``hidden_state``, which can either be a
        tuple of tensors or a tensor.

        As all of our Seq2xxxEncoders have different return types, we return `sorted`
        outputs from the module, which is called directly. Additionally, we return the
        indices into the batch dimension required to restore the tensor to it's correct,
        unsorted order and the number of valid batch elements (i.e the number of elements
        in the batch which are not completely masked). This un-sorting and re-padding
        of the module outputs is left to the subclasses because their outputs have different
        types and handling them smoothly here is difficult.

        Parameters
        ----------
        module : ``Callable[[PackedSequence, Optional[RnnState]],
                            Tuple[Union[PackedSequence, torch.Tensor], RnnState]]``, required.
            A function to run on the inputs. In most cases, this is a ``torch.nn.Module``.
        inputs : ``torch.Tensor``, required.
            A tensor of shape ``(batch_size, sequence_length, embedding_size)`` representing
            the inputs to the Encoder.
        mask : ``torch.Tensor``, required.
            A tensor of shape ``(batch_size, sequence_length)``, representing masked and
            non-masked elements of the sequence for each element in the batch.
        hidden_state : ``Optional[RnnState]``, (default = None).
            A single tensor of shape (num_layers, batch_size, hidden_size) representing the
            state of an RNN with or a tuple of
            tensors of shapes (num_layers, batch_size, hidden_size) and
            (num_layers, batch_size, memory_size), representing the hidden state and memory
            state of an LSTM-like RNN.

        Returns
        -------
        module_output : ``Union[torch.Tensor, PackedSequence]``.
            A Tensor or PackedSequence representing the output of the Pytorch Module.
            The batch size dimension will be equal to ``num_valid``, as sequences of zero
            length are clipped off before the module is called, as Pytorch cannot handle
            zero length sequences.
        final_states : ``Optional[RnnState]``
            A Tensor representing the hidden state of the Pytorch Module. This can either
            be a single tensor of shape (num_layers, num_valid, hidden_size), for instance in
            the case of a GRU, or a tuple of tensors, such as those required for an LSTM.
        restoration_indices : ``torch.LongTensor``
            A tensor of shape ``(batch_size,)``, describing the re-indexing required to transform
            the outputs back to their original batch order.
        """
        # In some circumstances you may have sequences of zero length. ``pack_padded_sequence``
        # requires all sequence lengths to be > 0, so remove sequences of zero length before
        # calling self._module, then fill with zeros.

        # First count how many sequences are empty.
        batch_size = mask.size(0)
        num_valid = torch.sum(mask[:, 0]).int().item()

        sequence_lengths = get_lengths_from_binary_sequence_mask(mask)
        sorted_inputs, sorted_sequence_lengths, restoration_indices, sorting_indices =\
            sort_batch_by_length(inputs, sequence_lengths)

        # Now create a PackedSequence with only the non-empty, sorted sequences.
        packed_sequence_input = pack_padded_sequence(sorted_inputs[:num_valid, :, :],
                                                     sorted_sequence_lengths[:num_valid].data.tolist(),
                                                     batch_first=True)
        # Prepare the initial states.
        if not self.stateful:
            if hidden_state is None:
                initial_states = hidden_state
            elif isinstance(hidden_state, tuple):
                initial_states = [state.index_select(1, sorting_indices)[:, :num_valid, :].contiguous()
                                  for state in hidden_state]
            else:
                initial_states = hidden_state.index_select(1, sorting_indices)[:, :num_valid, :].contiguous()

        else:
            initial_states = self._get_initial_states(batch_size, num_valid, sorting_indices)

        # Actually call the module on the sorted PackedSequence.
        module_output, final_states = module(packed_sequence_input, initial_states)

        return module_output, final_states, restoration_indices