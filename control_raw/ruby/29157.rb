def receive_newblockhashes(proto, newblockhashes)
      logger.debug 'received newblockhashes', num: newblockhashes.size, proto: proto

      newblockhashes = newblockhashes.select {|h| !@chainservice.knows_block(h) }

      known = @protocols.include?(proto)
      if !known || newblockhashes.empty? || @synctask
        logger.debug 'discarding', known: known, synctask: syncing?, num: newblockhashes.size
        return
      end

      if newblockhashes.size != 1
        logger.warn 'supporting only one newblockhash', num: newblockhashes.size
      end
      blockhash = newblockhashes[0]

      logger.debug 'starting synctask for newblockhashes', blockhash: Utils.encode_hex(blockhash)
      @synctask = SyncTask.new self, proto, blockhash, 0, true
    end