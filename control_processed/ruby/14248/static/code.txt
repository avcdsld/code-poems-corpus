def fatal(message = nil, ex = nil, data = nil, &block)
      log(FATAL, message, ex, data, block)
    end