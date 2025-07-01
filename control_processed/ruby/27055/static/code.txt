def state_run_block(channel)
      debug :run_block
      channel[:state] = nil
      blk = channel[:block]
      channel[:block] = nil
      begin
        instance_eval &blk
      rescue => ex
        channel[:exception] = ex
      end
      channel[:state] = :exit
    end