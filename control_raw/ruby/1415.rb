def run_request(method, url, body, headers)
      unless METHODS.include?(method)
        raise ArgumentError, "unknown http method: #{method}"
      end

      # Resets temp_proxy
      @temp_proxy = proxy_for_request(url)

      request = build_request(method) do |req|
        req.options = req.options.merge(proxy: @temp_proxy)
        req.url(url)                if url
        req.headers.update(headers) if headers
        req.body = body             if body
        yield(req) if block_given?
      end

      builder.build_response(self, request)
    end