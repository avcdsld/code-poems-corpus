def read_into_buffer(buffer, size)
      tmp = read_all(size)
      i = 0
      tmp.each_byte do |byte|
        Bytes.set_string_byte(buffer, i, byte)
        i += 1
      end
      i
    end