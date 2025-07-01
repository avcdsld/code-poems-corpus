def read(num_bytes)
      unless IO.select([@socket], nil, nil, @timeout)
        raise Errno::ETIMEDOUT
      end

      @socket.read(num_bytes)
    rescue IO::EAGAINWaitReadable
      retry
    end