def parse_integer attr_name, xpath
      v = parse_value xpath
      v = v.to_i if v.respond_to?(:to_i)
      send("#{attr_name}=", v)
    end