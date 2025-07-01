def http_get(path, extra=nil, params={})
      payload = self.class.get path, params
      APICake::Payload.new payload
    end