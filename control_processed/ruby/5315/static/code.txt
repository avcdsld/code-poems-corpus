def write_attribute(name, value)
      name = name.to_sym

      if association = @associations[name]
        association.reset
      end

      @attributes_before_type_cast[name] = value

      value_casted = TypeCasting.cast_field(value, self.class.attributes[name])
      attributes[name] = value_casted
    end