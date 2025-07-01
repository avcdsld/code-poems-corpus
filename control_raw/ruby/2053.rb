def trim(n)
      result = self
      while n > 0 && !result.empty?
        result = result.tail
        n -= 1
      end
      result
    end