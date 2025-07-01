def phone_number=(phone_number)

      if !phone_number.nil? && phone_number.to_s.length > 16
        fail ArgumentError, "invalid value for 'phone_number', the character length must be smaller than or equal to 16."
      end

      @phone_number = phone_number
    end