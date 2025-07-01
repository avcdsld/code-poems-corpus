def percentage=(percentage)

      if !percentage.nil? && percentage.to_s.length > 10
        fail ArgumentError, "invalid value for 'percentage', the character length must be smaller than or equal to 10."
      end

      @percentage = percentage
    end