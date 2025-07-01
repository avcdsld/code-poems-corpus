def keep_trying_to(title)
      begin
        yield
      rescue RestClient::ResourceNotFound => e
        log "work unit ##{@unit['id']} doesn't exist. discarding..."
      rescue Exception => e
        log "failed to #{title} -- retry in #{@retry_wait} seconds"
        log e.message
        log e.backtrace
        sleep @retry_wait
        retry
      end
    end