def write_set_attribute(attribute_name, value)
      column_type = ((column_definition = self.class.columns_hash[attribute_name.to_s]) and column_definition.type)
      value = value.to_s(10) if column_type == :string
      write_attribute(attribute_name, value)
    end