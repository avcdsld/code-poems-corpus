def method_missing(method, *args)
      getter_name = "get_#{method}"
      return send(getter_name, *args) if respond_to?(getter_name)

      if method.to_s =~ /(.*)=$/
        setter_name = "set_#{Regexp.last_match[1]}"
        return send(setter_name, *args) if respond_to?(setter_name)
      end
      super
    end