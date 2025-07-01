def at_exit(&block)
      return proc {} unless running || block_given?
      @at_exit = block if block_given?
      @at_exit ||= proc { SimpleCov.result.format! }
    end