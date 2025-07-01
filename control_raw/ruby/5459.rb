def log_errors!
      if AnyCable.config.debug?
        # Print error with backtrace in debug mode
        AnyCable.capture_exception do |e|
          AnyCable.logger.error("#{e.message}:\n#{e.backtrace.take(20).join("\n")}")
        end
      else
        AnyCable.capture_exception { |e| AnyCable.logger.error(e.message) }
      end
    end