def request(method, options)
      host = options.fetch(:host, S3.host)
      path = options.fetch(:path)
      body = options.fetch(:body, nil)
      params = options.fetch(:params, {})
      headers = options.fetch(:headers, {})

      # Must be done before adding params
      # Encodes all characters except forward-slash (/) and explicitly legal URL characters
      path = Addressable::URI.escape(path)

      if params
        params = params.is_a?(String) ? params : self.class.parse_params(params)
        path << "?#{params}"
      end

      request = Request.new(@chunk_size, method.to_s.upcase, !!body, method.to_s.upcase != "HEAD", path)

      headers = self.class.parse_headers(headers)
      headers.each do |key, value|
        request[key] = value
      end

      if body
        if body.respond_to?(:read)
          request.body_stream = body
        else
          request.body = body
        end
        request.content_length = body.respond_to?(:lstat) ? body.stat.size : body.size
      end

      send_request(host, request)
    end