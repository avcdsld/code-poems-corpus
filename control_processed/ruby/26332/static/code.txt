def put(path, stream, length)
      path = @uri.merge(path).path
      res = @handler.request_sending_stream(:put, path, stream, length, @headers)
      res.body
    end