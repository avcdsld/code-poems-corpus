def perform
      http = Net::HTTP.new(uri.host, uri.port)
      http.use_ssl = true
      http.ssl_timeout = @options[:ssl_timeout] unless @options[:ssl_timeout].nil?
      http.open_timeout = @options[:open_timeout] unless @options[:open_timeout].nil?
      http.read_timeout = @options[:read_timeout] unless @options[:read_timeout].nil?

      req = Net::HTTP::Post.new(uri.request_uri, headers)
      req.body = body
      resp = http.request(req)
      verify_response(resp)

      resp
    end