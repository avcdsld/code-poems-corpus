def get_param(key, default=nil)
      key = expand_local_name(@node_name, key)
      param = @parameter.get_param(key)
      if param
        param
      else
        default
      end
    end