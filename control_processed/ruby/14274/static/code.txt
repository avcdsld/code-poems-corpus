def define_child_node(klass, extra_params = {})
      child_nodes = obtain_class_variable(:@@ooxml_child_nodes)
      child_node_name = (extra_params[:node_name] || klass.class_variable_get(:@@ooxml_tag_name)).to_s
      accessor = (extra_params[:accessor] || accessorize(child_node_name)).to_sym

      child_nodes[child_node_name] = {
        :class => klass,
        :is_array => extra_params[:collection],
        :accessor => accessor
      }

      define_count_attribute if extra_params[:collection] == :with_count

      self.send(:attr_accessor, accessor)
    end