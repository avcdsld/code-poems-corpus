def get_parent
      raise UnknownParentError, "Genesis block has no parent" if number == 0
      Block.find env, prevhash
    rescue KeyError
      raise UnknownParentError, Utils.encode_hex(prevhash)
    end