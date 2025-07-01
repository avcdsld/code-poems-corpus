def request(method, uri, data: nil, headers: {}, **kwargs)
      request = Request.new(
        headers: default_headers.merge(headers),
        **kwargs,
        method: method,
        uri: join(uri),
        data: data
      )

      ret = cache.call(request) {|req| adapter.call(req) }
      ret.then do |response|
        if !response.errored?
          process response
        else
          raise ResponseError.from_code(response)
        end
      end
    end