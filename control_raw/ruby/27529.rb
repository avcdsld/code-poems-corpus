def blank?(str)
      str.nil? or (str.is_a? String and str.strip.empty?)
    end