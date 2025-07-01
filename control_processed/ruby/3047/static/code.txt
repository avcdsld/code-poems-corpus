def read_user_class
      klass_name = read(cache: false)
      klass = safe_const_get(klass_name)
      value = read(cache: false)

      result = if klass < Hash
                 klass[value]
               else
                 klass.new(value)
               end

      @object_cache << result

      result
    end