def goal_type=(goal_type)
      validator = EnumAttributeValidator.new('String', ['TB', 'TBD', 'MF'])
      unless validator.valid?(goal_type)
        fail ArgumentError, 'invalid value for "goal_type", must be one of #{validator.allowable_values}.'
      end
      @goal_type = goal_type
    end