def recv_io(klass = IO, negotiate = true)
      write("pass IO") if negotiate
      io = @io.recv_io(klass)
      write("got IO") if negotiate
      return io
    end