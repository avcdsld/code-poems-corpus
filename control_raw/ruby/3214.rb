def sort_order=(sort_order)
      validator = EnumAttributeValidator.new('String', ["DESC", "ASC"])
      unless validator.valid?(sort_order)
        fail ArgumentError, "invalid value for 'sort_order', must be one of #{validator.allowable_values}."
      end
      @sort_order = sort_order
    end