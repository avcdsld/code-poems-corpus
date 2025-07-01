def read_attribute_before_type_cast(name)
      attr = name.to_s
      if attributes_before_type_cast.key?(attr)
        attributes_before_type_cast[attr]
      else
        read_raw_attribute(attr)
      end
    end