def read_varint(data: nil, stream: nil, offset: 0)
      if data && !stream
        return [nil, 0] if data.bytesize < 1 + offset

        bytes = BTC::Data.bytes_from_data(data, offset: offset, limit: 9) # we don't need more than 9 bytes.

        byte = bytes[0]

        if byte < 0xfd
          return [byte, offset + 1]
        elsif byte == 0xfd
          return [nil, 1] if data.bytesize < 3 + offset # 1 byte prefix, 2 bytes uint16
          return [bytes[1] +
                  bytes[2]*256, offset + 3]
        elsif byte == 0xfe
          return [nil, 1] if data.bytesize < 5 + offset # 1 byte prefix, 4 bytes uint32
          return [bytes[1] +
                  bytes[2]*256 +
                  bytes[3]*256*256 +
                  bytes[4]*256*256*256, offset + 5]
        elsif byte == 0xff
          return [nil, 1] if data.bytesize < 9 + offset # 1 byte prefix, 8 bytes uint64
          return [bytes[1] +
                  bytes[2]*256 +
                  bytes[3]*256*256 +
                  bytes[4]*256*256*256 +
                  bytes[5]*256*256*256*256 +
                  bytes[6]*256*256*256*256*256 +
                  bytes[7]*256*256*256*256*256*256 +
                  bytes[8]*256*256*256*256*256*256*256, offset + 9]
        end

      elsif stream && !data

        if stream.eof?
          raise ArgumentError, "Can't parse varint from stream because it is already closed."
        end

        if offset > 0
          buf = stream.read(offset)
          return [nil, 0] if !buf
          return [nil, buf.bytesize] if buf.bytesize < offset
        end

        prefix = stream.read(1)

        return [nil, offset] if !prefix || prefix.bytesize == 0

        byte = prefix.bytes[0]

        if byte < 0xfd
          return [byte, offset + 1]
        elsif byte == 0xfd
          buf = stream.read(2)
          return [nil, offset + 1] if !buf
          return [nil, offset + 1 + buf.bytesize] if buf.bytesize < 2
          return [buf.unpack("v").first, offset + 3]
        elsif byte == 0xfe
          buf = stream.read(4)
          return [nil, offset + 1] if !buf
          return [nil, offset + 1 + buf.bytesize] if buf.bytesize < 4
          return [buf.unpack("V").first, offset + 5]
        elsif byte == 0xff
          buf = stream.read(8)
          return [nil, offset + 1] if !buf
          return [nil, offset + 1 + buf.bytesize] if buf.bytesize < 8
          return [buf.unpack("Q<").first, offset + 9]
        end

      else
        raise ArgumentError, "Either data or stream must be specified."
      end
    end