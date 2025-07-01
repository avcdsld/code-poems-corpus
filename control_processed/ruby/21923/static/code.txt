def notify_state(node, state, latency = nil)
      @lock.synchronize do
        if running?
          update_current_state(node, state, latency)
        end
      end
    rescue => ex
      logger.error("Error handling state report #{[node, state].inspect}: #{ex.inspect}")
      logger.error(ex.backtrace.join("\n"))
    end