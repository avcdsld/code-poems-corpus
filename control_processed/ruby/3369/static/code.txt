def valid?
      schedule_type_validator = EnumAttributeValidator.new('String', ["SCHEDULED", "ASAP"])
      return false unless schedule_type_validator.valid?(@schedule_type)
      return false if !@note.nil? && @note.to_s.length > 500
      return false if !@cancel_reason.nil? && @cancel_reason.to_s.length > 100
      return true
    end