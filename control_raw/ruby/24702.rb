def align(a)
      case a
      when 1
        nil
      when 2, 4, 8
        bits = a - 1
        @idx = @idx + bits & ~bits
        raise IncompleteBufferException if @idx > @buffy.bytesize
      else
        raise "Unsupported alignment #{a}"
      end
    end