def pop(log_trx = true)
      raise NoTransactionLog if log_trx && !@trx

      begin
        rv = super(!log_trx)
      rescue ThreadError
        puts "WARNING: The queue was empty when trying to pop(). Technically this shouldn't ever happen. Probably a bug in the transactional underpinnings. Or maybe shutdown didn't happen cleanly at some point. Ignoring."
        rv = [now_usec, '']
      end
      transaction "\001" if log_trx
      @current_age = (now_usec - rv[0]) / 1000
      rv[1]
    end