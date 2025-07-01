def read_primitive_with_ivars
      object = read

      primitive_ivars = read_hash(cache: false)

      if primitive_ivars.any? && object.is_a?(String)
        object = `new String(object)`
      end

      primitive_ivars.each do |name, value|
        if name != 'E'
          object.instance_variable_set(name, value)
        end
      end

      object
    end