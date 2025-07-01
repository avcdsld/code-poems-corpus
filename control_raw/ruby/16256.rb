def otherwise(first, second)
      first = first.to_s
      first.empty? ? second : first
    end