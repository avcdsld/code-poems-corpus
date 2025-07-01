def Block(contract_hash)
      pc = Handshake::ProcContract.new
      pc.signature = contract_hash
      pc
    end