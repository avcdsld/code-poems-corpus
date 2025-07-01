def thread_timeout=(t)
      t = t.to_f
      raise ArgumentError.new('Value must be great than zero or nil') unless t > 0
      @thread_timeout = t
      @thread.raise Retimeout.new if waiting?
      t
    end