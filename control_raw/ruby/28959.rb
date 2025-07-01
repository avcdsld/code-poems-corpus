def min=(m)
      m = m.to_i
      raise ArgumentError.new("Minimum value must be greater than 0 and less than or equal to maximum (#{max})") unless m > 0 && m <= max
      @min_threads = m
      m
    end