def delete_message(message_title)
      full_path = "#{full_queue_path}/#{message_title}"
      locker = @zk.locker("#{full_queue_path}/#{message_title}")
      if locker.lock!
        begin
          @zk.delete(full_path)
          return true
        ensure
          locker.unlock!
        end
      else
        return false
      end
    end