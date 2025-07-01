def cstring(address)
      base = base_of(address)
      len = 1
      cur = ''
      loop do
        cur << (dump(base + len - 1, len) || '')
        break if cur.index("\x00")

        len <<= 1
        return cur if cur.size != len - 1 # reached undumpable memory
      end
      cur[0, cur.index("\x00")]
    end