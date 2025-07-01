def read_uleb128(data: nil, stream: nil, offset: 0)
      if (data && stream) || (!data && !stream)
        raise ArgumentError, "Either data or stream must be specified."
      end
      if data
        data = BTC::Data.ensure_binary_encoding(data)
      end
      if stream
        if stream.eof?
          raise ArgumentError, "Can't read LEB128 from stream because it is already closed."
        end
        if offset > 0
          buf = stream.read(offset)
          return [nil, 0] if !buf
          return [nil, buf.bytesize] if buf.bytesize < offset
        end
      end
      result = 0
      shift = 0
      while true
        byte = if data
          return [nil, offset] if data.bytesize < 1 + offset
          BTC::Data.bytes_from_data(data, offset: offset, limit: 1)[0]
        elsif stream
          buf = stream.read(1)
          return [nil, offset] if !buf || buf.bytesize == 0
          buf.bytes[0]
        end
        result |= (byte & 0x7f) << shift
        break if byte & 0x80 == 0
        shift += 7
        offset += 1
      end
      [result, offset + 1]
    end