def get_cache(name, key)
      cache = instance_variable_get("@#{name}_map")
      value = cache[key]
      if value.nil? && block_given?
        set_cache(name, key, value = yield)
      end
      value == :_nil ? nil : value
    end