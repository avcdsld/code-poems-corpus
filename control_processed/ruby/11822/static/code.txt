def init_on_load(persisted_rel, from_node_id, to_node_id, type)
      @rel_type = type
      @_persisted_obj = persisted_rel
      changed_attributes_clear!
      @attributes = convert_and_assign_attributes(persisted_rel.props)
      load_nodes(from_node_id, to_node_id)
    end