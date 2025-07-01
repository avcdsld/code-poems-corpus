def start_tls(req, options)
      return unless req.uri.https? && !failed_proxy_connect?

      ssl_context = options.ssl_context

      unless ssl_context
        ssl_context = OpenSSL::SSL::SSLContext.new
        ssl_context.set_params(options.ssl || {})
      end

      @socket.start_tls(req.uri.host, options.ssl_socket_class, ssl_context)
    end