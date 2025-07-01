def close
      threads = @mutex.synchronize do
        raise Airbrake::Error, 'attempted to close already closed sender' if closed?

        unless @unsent.empty?
          msg = "#{LOG_LABEL} waiting to send #{@unsent.size} unsent notice(s)..."
          logger.debug(msg + ' (Ctrl-C to abort)')
        end

        @config.workers.times { @unsent << [:stop, Airbrake::Promise.new] }
        @closed = true
        @workers.list.dup
      end

      threads.each(&:join)
      logger.debug("#{LOG_LABEL} closed")
    end