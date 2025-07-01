def iterations=(n)
      n = Integer(n)
      Kernel.raise ArgumentError, 'iterations must be between 0 and 65535' if n < 0 || n > 65_535
      @images.each { |f| f.iterations = n }
      self
    end