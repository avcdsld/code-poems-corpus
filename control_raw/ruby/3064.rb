def connect(options = {})
      @options = options
      set_up_amqp_connection
      if http_api_use_enabled?
        logger.info "HTTP API use is enabled"
        set_up_api_connection
      else
        logger.info "HTTP API use is disabled"
      end

      if tracing_enabled?
        logger.info "tracing is enabled using #{@config[:tracer]}"
      else
        logger.info "tracing is disabled"
      end

      if block_given?
        begin
          yield
        ensure
          disconnect
        end
      end
    end