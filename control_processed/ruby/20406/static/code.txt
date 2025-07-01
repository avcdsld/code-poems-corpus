def crc16(msg)
      crc_lo = 0xff
      crc_hi = 0xff

      msg.unpack('c*').each do |byte|
        i = crc_hi ^ byte
        crc_hi = crc_lo ^ CrcHiTable[i]
        crc_lo = CrcLoTable[i]
      end

      return ((crc_hi << 8) + crc_lo)
    end