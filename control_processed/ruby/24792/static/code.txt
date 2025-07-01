def flag_color=(flag_color)
      validator = EnumAttributeValidator.new('String', ['red', 'orange', 'yellow', 'green', 'blue', 'purple'])
      unless validator.valid?(flag_color)
        fail ArgumentError, 'invalid value for "flag_color", must be one of #{validator.allowable_values}.'
      end
      @flag_color = flag_color
    end