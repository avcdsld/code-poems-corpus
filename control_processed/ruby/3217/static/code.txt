def visibility=(visibility)
      validator = EnumAttributeValidator.new('String', ["PUBLIC", "PRIVATE"])
      unless validator.valid?(visibility)
        fail ArgumentError, "invalid value for 'visibility', must be one of #{validator.allowable_values}."
      end
      @visibility = visibility
    end