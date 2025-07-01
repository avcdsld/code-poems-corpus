def checksum_type=(new_val)
      return if new_val == @checksum_type
      raise JSS::InvalidDataError, "Checksum type must be one of: #{CHECKSUM_HASH_TYPES.keys.join ', '} " unless CHECKSUM_HASH_TYPES.key? new_val

      @checksum_type = new_val
      @need_to_update = true
    end