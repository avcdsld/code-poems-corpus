def dom_id_namespace
      namespace = options[:custom_namespace]
      parent = options[:parent_builder]

      case
        when namespace then namespace
        when parent && parent != self then parent.dom_id_namespace
        else custom_namespace
      end
    end