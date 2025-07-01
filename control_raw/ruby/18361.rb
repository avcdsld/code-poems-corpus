def [](pos, len=nil)
      if pos.is_a?(Range)
        @buffer.get_lines(*range_indices(pos), true)
      else
        start, stop = length_indices(pos, len || 1)
        lines = @buffer.get_lines(start, stop, true)
        len ? lines : lines.first
      end
    end