def removing(range, &block)
      return if range.count == 0

      @access.begin_remove(range.min, range.max)
      ret = yield
      @access.end_remove
      ret
    end