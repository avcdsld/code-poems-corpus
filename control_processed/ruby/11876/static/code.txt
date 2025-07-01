def resource_name(thing)
      if thing.respond_to?(:declared_type) && thing.declared_type
        name = thing.declared_type
      elsif thing.respond_to?(:resource_name)
        name = thing.resource_name
      else
        name = thing
      end
      name.to_s.gsub('-', '_').to_sym
    end