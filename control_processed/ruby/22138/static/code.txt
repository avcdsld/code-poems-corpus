def method_missing(method_name, *arguments, &block)
      super unless dynamic_method?(method_name)

      if dynamic_state_check?(method_name)
        # Used to check state - allows for methods such as #published? and #expired?
        # Will return true if the active_state corresponds to the name of the method
        "#{publish_state.downcase}?" == method_name.to_s
      else
        # Used to query for any field on the relevant ContentType and return data from the content_item
        field_items.find { |field_item| field_item.field.name.parameterize(separator: '_') == method_name.to_s }.data.values.first
      end
    end