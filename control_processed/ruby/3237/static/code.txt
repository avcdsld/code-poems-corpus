def reason=(reason)

      if !reason.nil? && reason.to_s.length > 192
        fail ArgumentError, "invalid value for 'reason', the character length must be smaller than or equal to 192."
      end

      @reason = reason
    end