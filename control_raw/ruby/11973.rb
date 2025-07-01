def resolve_parameter(target_typed_method_name, parameter_field, default_value, *args)
        if respond_to?(target_typed_method_name)
          send(target_typed_method_name, *args)
        elsif parameter_field
          resolve_value(parameter_field, *args)
        else
          default_value
        end
      end