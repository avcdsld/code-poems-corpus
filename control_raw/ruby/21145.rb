def safe_call(callbacks)
      cbs = callbacks.dup

      # exceptions in these hooks will be raised normally

      while cb = cbs.shift
        cb.call
      end
    end