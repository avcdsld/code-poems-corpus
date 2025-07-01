def attribute_will_change!(attr)
      unless changed_attributes.key?(attr)
        changed_attributes[attr] = read_raw_attribute(attr).__deep_copy__
      end
    end