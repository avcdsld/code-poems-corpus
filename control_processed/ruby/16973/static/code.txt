def variant
      variant_raw = (clock_seq_hi_and_reserved >> 5)
      result = nil
      if (variant_raw >> 2) == 0
        result = 0x000
      elsif (variant_raw >> 1) == 2
        result = 0x100
      else
        result = variant_raw
      end
      return (result >> 6)
    end