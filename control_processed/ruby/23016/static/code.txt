def add_instance_variable( name , type )
      raise "No nil name" unless name
      raise "No nil type" unless type
      hash = to_hash
      hash[name] = type
      return Type.for_hash( object_class , hash)
    end