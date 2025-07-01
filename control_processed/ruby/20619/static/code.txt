def process_staged
      @staging_lock.synchronize {
        if @staging_queue.size > 0
          @staging_queue.delete_if do |t|
            if t.complete?
              ::Instana.logger.debug("Moving staged complete trace to main queue: #{t.id}")
              add(t)
              true
            elsif t.discard?
              ::Instana.logger.debug("Discarding trace with uncompleted async spans over 5 mins old. id: #{t.id}")
              true
            else
              false
            end
          end
        end
      }
    end