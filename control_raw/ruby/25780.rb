def assert_either_value_or_block(value, block)
      if value.nil? && block.nil?
        raise ArgumentError, 'Need to set either value or block'
      elsif !(value.nil? || block.nil?)
        raise ArgumentError, "Can't set both value and block"
      end
    end