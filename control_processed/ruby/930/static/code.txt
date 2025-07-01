def input(name, options = {})
      if options[:as]
        send(options[:as].to_s, name, options[:input] || {})
      else
        type = find_input_type(name.to_s)
        input_field(name, type)
      end
    end