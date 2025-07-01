def readpartial(maxlen, outbuf = "")
      data = @socket.readpartial(maxlen, outbuf)
      log :read, data
      data
    end