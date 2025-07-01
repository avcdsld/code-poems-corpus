def read_string(data: nil, stream: nil, offset: 0)
      if data && !stream

        string_length, read_length = read_varint(data: data, offset: offset)

        # If failed to read the length prefix, return nil.
        return [nil, read_length] if !string_length

        # Check if we have enough bytes to read the string itself
        return [nil, read_length] if data.bytesize < read_length + string_length

        string = BTC::Data.ensure_binary_encoding(data)[read_length, string_length]

        return [string, read_length + string_length]

      elsif stream && !data

        string_length, read_length = read_varint(stream: stream, offset: offset)
        return [nil, read_length] if !string_length

        buf = stream.read(string_length)

        return [nil, read_length] if !buf
        return [nil, read_length + buf.bytesize] if buf.bytesize < string_length

        return [buf, read_length + buf.bytesize]
      else
        raise ArgumentError, "Either data or stream must be specified."
      end
    end