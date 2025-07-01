def to_s
      result = ""
      @words.each do |w|
        result += w.to_s(2).rjust(BITS_PER_WORD,'0') + ":"
      end
      result
    end