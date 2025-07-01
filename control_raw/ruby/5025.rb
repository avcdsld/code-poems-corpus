def stored_fields(field_name, dynamic_field_name = nil)
      @stored_field_factories_cache[field_name.to_sym].map do |field_factory|
        if dynamic_field_name
          field_factory.build(dynamic_field_name)
        else
          field_factory.build
        end
      end
    end