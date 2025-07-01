def write_to(io)
      nbytes = @limit - @position
      raise UnderflowError, "no data remaining in buffer" if nbytes.zero?

      bytes_written = IO.try_convert(io).write_nonblock(@buffer[@position...@limit], exception: false)
      return 0 if bytes_written == :wait_writable

      @position += bytes_written
      bytes_written
    end