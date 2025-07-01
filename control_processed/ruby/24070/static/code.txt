def scale=(attrs)
      @scale = if attrs[:function_code]
        Functional.new(attrs[:value], attrs[:unit_code], attrs[:function_code])
      else
        Scale.new(attrs[:value], attrs[:unit_code])
      end
    end