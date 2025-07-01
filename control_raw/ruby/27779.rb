def add(severity, message = nil, progname = nil)
      if severity >= self.level
        # super logger.
        if message.nil?
          if block_given?
            message = yield
          else
            message = progname
            progname = self.progname
          end
        end
        super(severity, message, progname)

        # record errors (with detail) and warnings.
        if @recording_messages
          if severity >= Logger::ERROR
            @errors << [nil, :log, message]
          elsif severity == ::Logger::WARN
            @warnings << message
          end
        end
      end
      true
    end