def create_apply_graph(self, signature, input_tensors, name):
    """See `ModuleImpl.create_apply_graph`."""
    signature_def = self._meta_graph.signature_def.get(signature)
    meta_graph = meta_graph_pb2.MetaGraphDef()
    meta_graph.CopyFrom(self._meta_graph)
    apply_graph = tf_v1.get_default_graph()
    infeed_map = tensor_info.build_input_map(signature_def.inputs,
                                             input_tensors)

    # Build a input map to feed when importing the apply-graph by augmenting the
    # state_map with the input args. This allows an input to override a tensor
    # from the state-graph.
    feed_map = dict(self._state_map)
    # If we are applying the module in a function with a TPUReplicateContext, we
    # must capture the state tensors in generating our feedmap and prune out
    # assign ops. Function graph semantics are different in that all ops are
    # executed regardless of dependency.
    # TODO(b/112575006): The following adds functionality of function call
    # within a TPU context. Work to generalize this for all function calls is
    # ongoing.
    if self._is_tpu_graph_function():
      for k, v in self._state_map.items():
        feed_map[k] = apply_graph.capture(v)
      meta_graph_lib.prune_unused_nodes(meta_graph, signature_def)
      # After we prune the metagraph def, we might need to prune away
      # infeeds which no longer exist.
      meta_graph_lib.prune_feed_map(meta_graph, infeed_map)
    elif apply_graph.building_function:
      raise NotImplementedError(
          "Using TF-Hub module within a TensorFlow defined function "
          "is currently not supported.")

    # As state ops in the apply graph are unused, replace them with Placeholders
    # so that in a heirarchical instantiation, apply_graph state ops are
    # ignored.
    replace_apply_state(meta_graph,
                        list_registered_stateful_ops_without_inputs(), feed_map)
    feed_map.update(infeed_map)

    # Make state tensors enter the current context. This way the Module can be
    # applied inside a control flow structure such as a while_loop.
    control_flow = apply_graph._get_control_flow_context()  # pylint: disable=protected-access
    if control_flow:
      for key, value in sorted(feed_map.items()):
        feed_map[key] = control_flow.AddValue(value)

    # Don't mark the name as used at this point - import_scoped_meta_graph will
    # start using it.
    absolute_scope_name = apply_graph.unique_name(name, mark_as_used=False)
    relative_scope_name = absolute_scope_name.split("/")[-1]

    import_collections = [
        # In most cases ASSET_FILEPATHS are only used for the TABLE_INITIALIZERS
        # ops, however one could create a graph that uses an asset at any other
        # time. As so everytime we bring the tensor with that has the asset
        # filename we must annotate it as so, so later re-exports have that
        # semantic information and can handle it.
        tf_v1.GraphKeys.ASSET_FILEPATHS,
        tf_v1.GraphKeys.COND_CONTEXT,
        tf_v1.GraphKeys.WHILE_CONTEXT,
    ]
    if self._trainable:
      import_collections.extend([tf_v1.GraphKeys.UPDATE_OPS])

    meta_graph_lib.filter_collections(meta_graph, import_collections)
    meta_graph_lib.prefix_shared_name_attributes(meta_graph,
                                                 absolute_scope_name)
    if len(meta_graph.collection_def) and self._is_tpu_graph_function():
      raise NotImplementedError(
          "Applying modules with collections inside TPU functions is not "
          "supported.")

    tf_v1.train.import_meta_graph(
        meta_graph,
        input_map=feed_map,
        import_scope=relative_scope_name)
    fix_colocation_after_import(input_map=feed_map,
                                absolute_import_scope=absolute_scope_name)

    def get_tensor(name):
      # When trying to output an input tensor there are no nodes created within
      # the apply scope. So one must look into the input map.
      try:
        return feed_map[name]
      except KeyError:
        return apply_graph.get_tensor_by_name(
            meta_graph_lib.prepend_name_scope(
                name, import_scope=absolute_scope_name))

    return tensor_info.build_output_map(signature_def.outputs, get_tensor)