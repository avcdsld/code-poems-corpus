def connection
      @connection ||= build_connection

      unless @connection.builder.handlers.include?(FaradayMiddleware::FollowRedirects)
        @connection.builder.insert(-2, FaradayMiddleware::FollowRedirects)
      end

      return @connection
    end