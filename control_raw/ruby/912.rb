def coerce_non_null_input(value_name, ctx)
      if @values_by_name.key?(value_name)
        @values_by_name.fetch(value_name).value
      elsif match_by_value = @values_by_name.find { |k, v| v.value == value_name }
        # this is for matching default values, which are "inputs", but they're
        # the Ruby value, not the GraphQL string.
        match_by_value[1].value
      else
        nil
      end
    end