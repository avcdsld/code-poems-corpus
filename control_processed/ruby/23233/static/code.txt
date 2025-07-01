def write_msg(socket, msg)
      sio = StringIO.new('', 'r+')
      len = msg.serialize(sio)
      sio.rewind
      data = sio.read
      len = data.length
      data = [len, data].pack("La#{len}")
      socket.write(data)
      data
    end