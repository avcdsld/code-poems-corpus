def escape_uri(str)
      str = str.dup
      binary_encode(str)
      str.gsub(UNESCAPED) { "%%%02X" % $1[0].ord }
    end