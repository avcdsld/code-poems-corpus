def writable?(key, parameters = {}, conditions = {})
      case key
      when String, Numeric, Symbol
        !conditions.has_key?(:expire_in)
      else nil
      end
    end