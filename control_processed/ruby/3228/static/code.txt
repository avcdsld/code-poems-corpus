def id=(id)

      if !id.nil? && id.to_s.length > 255
        fail ArgumentError, "invalid value for 'id', the character length must be smaller than or equal to 255."
      end

      @id = id
    end