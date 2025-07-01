def compile!(path, &block)
      method_name = path
      route_method = Application.generate_method(method_name, &block)
      pattern, keys = compile path

      [ pattern, keys, route_method ]
    end