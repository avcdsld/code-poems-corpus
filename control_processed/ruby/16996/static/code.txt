def child(name_or_data, options = {})
      data, name  = extract_data_and_name(name_or_data)
      name        = options[:root] if options.has_key? :root
      template    = partial_or_block(data, options) { yield }
      @template.add_node Nodes::Child.new(name, template)
    end