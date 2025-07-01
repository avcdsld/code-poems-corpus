def cache(key)
      key_hash = key2hash(key)
      read(key_hash) || (write(key_hash, yield) if block_given?)
    end