def server_error_handling(&blk)
    begin
      blk.call
    rescue Sequel::DatabaseError => e
      if e.message =~ /duplicate key value/i
        raise Taps::DuplicatePrimaryKeyError, e.message
      else
        raise
      end
    end
  end