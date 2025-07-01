def config_get(feature, property, *args)
      ref = @cmd_ref.lookup(feature, property)

      # If we have a default value but no getter, just return the default
      return ref.default_value if ref.default_value? && !ref.getter?

      get_args, ref = massage_structured(ref.getter(*args).clone, ref)
      data = get(command:     get_args[:command],
                 data_format: get_args[:data_format],
                 context:     get_args[:context],
                 value:       get_args[:value])
      massage(data, ref)
    end