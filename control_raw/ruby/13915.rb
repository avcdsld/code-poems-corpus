def mine(rounds=1000, start_nonce=0)
      blk = @block
      bin_nonce, mixhash = _mine(blk.number, blk.difficulty, blk.mining_hash, start_nonce, rounds)

      if bin_nonce.true?
        blk.mixhash = mixhash
        blk.nonce = bin_nonce
        return blk
      end
    end