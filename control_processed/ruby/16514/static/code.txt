def enable_tls(context = SMTP.default_ssl_context)
      raise 'openssl library not installed' unless defined?(OpenSSL)
      raise ArgumentError, "SMTPS and STARTTLS is exclusive" if @starttls
      @tls = true
      @ssl_context = context
    end