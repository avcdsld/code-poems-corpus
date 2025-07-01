def skip_conversion?(obj, attr, value)
      value.nil? || !obj.class.attributes.key?(attr)
    end