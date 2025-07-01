def on_value_event(self, event):
    """Records the summary values based on an updated message from the debugger.

    Logs an error message if writing the event to disk fails.

    Args:
      event: The Event proto to be processed.
    """
    if not event.summary.value:
      logger.info('The summary of the event lacks a value.')
      return None

    # The node name property in the event proto is actually a watch key, which
    # is a concatenation of several pieces of data.
    watch_key = event.summary.value[0].node_name
    tensor_value = debug_data.load_tensor_from_event(event)
    device_name = _extract_device_name_from_event(event)
    node_name, output_slot, debug_op = (
        event.summary.value[0].node_name.split(':'))
    maybe_base_expanded_node_name = (
        self._run_states.get_maybe_base_expanded_node_name(node_name,
                                                           self._run_key,
                                                           device_name))
    self._tensor_store.add(watch_key, tensor_value)
    self._outgoing_channel.put(_comm_tensor_data(
        device_name, node_name, maybe_base_expanded_node_name, output_slot,
        debug_op, tensor_value, event.wall_time))

    logger.info('on_value_event(): waiting for client ack (tensors)...')
    self._incoming_channel.get()
    logger.info('on_value_event(): client ack received (tensor).')

    # Determine if the particular debug watch key is in the current list of
    # breakpoints. If it is, send an EventReply() to unblock the debug op.
    if self._is_debug_node_in_breakpoints(event.summary.value[0].node_name):
      logger.info('Sending empty EventReply for breakpoint: %s',
                      event.summary.value[0].node_name)
      # TODO(cais): Support receiving and sending tensor value from front-end.
      return debug_service_pb2.EventReply()
    return None