def write(s)
      begin
        retry_id ||= 0
        @socket.send(:write, s)
      rescue => e
        if (retry_id += 1) < @retries
          connect
          retry
        else
          raise e
        end
      end
    end