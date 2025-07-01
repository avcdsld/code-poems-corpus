def format_path(parameters)
      path = link_schema['href']
      parameter_size = path.scan(PARAMETER_REGEX).size
      too_few_parameters = parameter_size > parameters.size
      # FIXME We should use the schema to detect when a request body is
      # permitted and do the calculation correctly here. -jkakar
      too_many_parameters = parameter_size < (parameters.size - 1)
      if too_few_parameters || too_many_parameters
        raise ArgumentError.new("wrong number of arguments " +
                                "(#{parameters.size} for #{parameter_size})")
      end

      (0...parameter_size).each do |i|
        path = path.sub(PARAMETER_REGEX, format_parameter(parameters[i]))
      end
      body = parameters.slice(parameter_size)
      return path, body
    end