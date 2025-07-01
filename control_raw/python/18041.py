def _create_state_graph(self, name):
    """Creates the graph nodes that hold the state of the Module.

    Args:
      name: name scope to create the state graph in.

    Returns:
      A tuple consisting of:
        variables_tensor_map: a map from tensor names in the original graph def
          to the created Variables objects.
        state_map: a map from tensors names in the original graph def to the
          instantiated tensors to be used as a state_map.
    """
    import_collections = [
        tf_v1.GraphKeys.GLOBAL_VARIABLES,
        tf_v1.GraphKeys.MODEL_VARIABLES,
        tf_v1.GraphKeys.TABLE_INITIALIZERS,
        tf_v1.GraphKeys.ASSET_FILEPATHS,  # Typically used to initialize tables.
        tf_v1.GraphKeys.COND_CONTEXT,
        tf_v1.GraphKeys.WHILE_CONTEXT,
    ]
    if self._trainable:
      # TODO(b/64049014): Import UPDATE_OPS which do not depend on inputs.
      import_collections.extend([tf_v1.GraphKeys.TRAINABLE_VARIABLES,
                                 tf_v1.GraphKeys.REGULARIZATION_LOSSES])

    absolute_scope_name = tf_v1.get_default_graph().unique_name(
        name, mark_as_used=False)
    relative_scope_name = absolute_scope_name.split("/")[-1]
    assert relative_scope_name == name  # verify name scope was indeed unused.

    meta_graph = meta_graph_pb2.MetaGraphDef()
    meta_graph.CopyFrom(self._meta_graph)

    meta_graph_lib.filter_collections(meta_graph, import_collections)
    meta_graph_lib.prefix_shared_name_attributes(meta_graph,
                                                 absolute_scope_name)

    tf_v1.train.import_meta_graph(
        meta_graph,
        input_map={},
        import_scope=relative_scope_name)

    # Build a list from the variable name in the module definition to the actual
    # instantiated variables.
    variables_tensor_map = {}
    for var in tf_v1.global_variables():
      if var.op.name.startswith(absolute_scope_name + "/"):
        variables_tensor_map[var.name[len(absolute_scope_name)+1:]] = var

    # Build a map of tensors to feed from the state-graph into subsequent
    # apply-graphs.
    def _get_tensor(tensor_name):
      return tf_v1.get_default_graph().get_tensor_by_name(
          meta_graph_lib.prepend_name_scope(
              tensor_name, import_scope=absolute_scope_name))

    state_op_names = list_registered_stateful_ops_without_inputs()
    state_map = get_state_map(meta_graph, state_op_names, set(), _get_tensor)

    return variables_tensor_map, state_map