def field=(field)
      validator = EnumAttributeValidator.new('String', ["START_AT", "END_AT", "CREATED_AT", "UPDATED_AT"])
      unless validator.valid?(field)
        fail ArgumentError, "invalid value for 'field', must be one of #{validator.allowable_values}."
      end
      @field = field
    end