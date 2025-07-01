def break_name=(break_name)
      if break_name.nil?
        fail ArgumentError, "break_name cannot be nil"
      end

      if break_name.to_s.length < 1
        fail ArgumentError, "invalid value for 'break_name', the character length must be great than or equal to 1."
      end

      @break_name = break_name
    end